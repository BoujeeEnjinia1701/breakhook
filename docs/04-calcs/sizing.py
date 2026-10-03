"""BreakHook sizing calculations, BHK-CAL-001 (TRL 3). First-order hand calculations, stated assumptions.

Run from the repo root:  python docs/04-calcs/sizing.py
Prints every result with its reference ([A1], [B2] ...) used in docs/04-calcs/01-sizing.md and
writes docs/04-calcs/results.csv. Geometry and masses come from cad/src/model.py.
Plan figures only: nothing here has been built or tested (TRL 4 work).
"""
import csv
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "cad" / "src"))
from model import PARAMS as P, derived, masses  # noqa: E402

g = 9.81
R = []          # (ref, quantity, value, unit, note)


def out(ref, q, v, unit="", note=""):
    R.append((ref, q, v, unit, note))
    vs = f"{v:,.3g}" if isinstance(v, float) else str(v)
    print(f"[{ref}] {q}: {vs} {unit}  {note}")
    return v


D = derived(P)
M = masses(P)

# ------------------------------------------------------------------ A. pull needed (R2, R7, R13)
# Assumptions: single-storey dwelling 3.0 x 3.0 m, walls 2.4 m, light timber frame clad in
# corrugated steel sheet, empty of people; total mass 350 kg; pull applied at the top of the near
# wall; posts nailed to sole plates or set 0.3 m in soil (soil restraint ignored, conservative
# for the pull estimate only in the overturning case).
m_dw, b_dw, h_dw = 350.0, 3.0, 2.4
F_ot = out("A1", "Pull to overturn the dwelling as a rigid box", m_dw * g * (b_dw / 2) / h_dw / 1000, "kN",
           "350 kg, 3.0 m base, pulled at 2.4 m")
rack_per_m, side_walls = 0.5, 2 * 3.0
F_rack = out("A2", "Pull to rack an unbraced clad frame", rack_per_m * side_walls, "kN",
             "assumed 0.5 kN per metre of side wall for nailed light cladding")
F_wl = out("A3", "Design working pull (R2)", 3.0, "kN", "covers A1 and A2")
F_proof = out("A4", "Proof load (R2)", 2 * F_wl, "kN", "2 x working pull")
per_person = 0.30
n_haul = out("A5", "Haulers needed at the working pull", math.ceil(F_wl / per_person), "people",
             "assumed 300 N sustained per person on a rope with toggles")
out("A6", "Haulers needed for the overturning case", math.ceil(F_ot / per_person), "people")

# ------------------------------------------------------------------ B. hauling geometry (R3)
H_hook = 3.0
first = 11.0                                   # first toggle, along the line from the hook head (m)
leader_m = P["leader"][1] / 1000
rope_m = P["rope"][1] / 1000
hands = 1.0
ang = math.asin((H_hook - hands) / first)
x_first = out("B1", "Nearest hauler, horizontal distance from the wall", first * math.cos(ang), "m",
              "first toggle 11 m along the line, hook at 3.0 m, hands at 1.0 m")
out("B2", "Required by R3 (1.5 x structure height)", 1.5 * H_hook, "m")
out("B3", "Rope angle below horizontal at the first hauler", math.degrees(ang), "deg")
out("B4", "Horizontal share of the pull", math.cos(ang) * 100, "%")
last = first + (P["n_toggle"] - 1) * 1.0
out("B5", "Last toggle along the line", last, "m", f"toggles 1 m apart; line {leader_m + rope_m:.1f} m long")
out("B6", "Tail left for anchoring or a turn round a post", leader_m + rope_m - last, "m")

# ------------------------------------------------------------------ C. hook plate at the proof load (R2, R11)
fy = 355.0                                    # S355 yield, MPa
t = P["plate_t"]
F = F_proof * 1000
a0, a1 = P["arm_top"]
b0, b1, bz = P["arm_bot"]
rake = math.atan((a0 - b0) / (-P["shank"][1] - bz))
w_arm = (a1 - a0) * math.cos(rake)
out("C1", "Arm rake back from square to the shank", math.degrees(rake), "deg")
Z_arm = t * w_arm ** 2 / 6
for ref, depth in (("C2", 75.0), ("C3", 100.0)):
    e = 20.0 + depth / 2 if depth <= 75 else 20.0 + 0.7 * depth      # load centre below the shank underside
    s = F * (e - 0) / Z_arm
    out(ref, f"Arm root bending stress, {depth:.0f} mm deep beam", s, "MPa",
        f"lever {e:.0f} mm; factor on yield {fy / s:.2f} at proof, {2 * fy / s:.2f} at working")
hs = P["shank"][1]
A_sh = 2 * hs * t
Z_sh = t * (2 * hs) ** 2 / 6
dz = abs(P["eye"][1] - (-hs - 37.5))
s_sh = F / A_sh + F * dz / Z_sh
out("C4", f"Shank tension plus bending from the {dz:.1f} mm line offset", s_sh, "MPa", f"factor on yield {fy / s_sh:.1f}")
tx0, tx1, tz, tr = P["tab"]
ex, ez, ed = P["eye"]
tear = 2 * (ex - tx0 - ed / 2) * t
out("C5", "Eye tear-out shear stress", F / tear, "MPa", f"two planes {ex - tx0 - ed / 2:.1f} mm long")
out("C6", "Pin bearing stress on the plate", F / (P["shackle"][0] * t), "MPa")
s_tab = F * (-hs - ez) / (t * (tx1 - tx0) ** 2 / 6)
out("C7", "Tab root bending stress", s_tab, "MPa")
out("C8", "Throat width at the shank (between tab and arm)", a0 - tx1 - P["fillet_r"], "mm", "after the 8 mm corner radius")
out("C9", "Throat width 100 mm below the shank", a0 - (a0 - b0) * (100 / (-hs - bz)) - tx1, "mm")
out("C10", "Arm reach below the shank (beam depth it can hold)", -hs - bz, "mm")

# ------------------------------------------------------------------ D. socket welds (placement loads only)
F_side = 200.0                                # someone prising with the pole: 200 N at the spike tip
lever = P["spike"][0] + P["slot"][1]
Mw = F_side * lever
throat = 0.7 * P["weld_leg"]
pair_force = Mw / P["socket"][0]
s_w = pair_force / (2 * P["slot"][1] * throat)
out("D1", "Weld stress from a 200 N side load at the spike tip", s_w, "MPa", "4 fillet welds, 6 mm leg, 50 mm long")
out("D2", "Rope load through the socket welds", 0.0, "kN", "the rope pulls the plate, not the socket")

# ------------------------------------------------------------------ E. rope, leader, shackles (R2)
mbs_rope, splice = 25.0, 0.9
out("E1", "Pull rope factor of safety at the working pull", mbs_rope * splice / F_wl, "",
    "12 mm polyester double braid, breaking strength 25 kN or more, spliced eye 90 %")
mbs_wire, ferrule = 20.0, 0.9
out("E2", "Leader factor of safety at the working pull", mbs_wire * ferrule / F_wl, "",
    "6 mm 6x19 galvanised wire rope, 20 kN, pressed ferrules 90 %")
wll_sh = 9.8
out("E3", "Shackle working load limit against the working pull", wll_sh / F_wl, "", "3/8 in (10 mm) bow shackle, 1 t")
out("E4", "Load per prusik cord at the working pull", F_wl / P["n_toggle"] * 1000, "N", "6 mm cord, about 7 kN breaking")

# ------------------------------------------------------------------ F. pole placement (R1, R5, R6)
od, wall = P["pole"]
I = math.pi / 64 * (od ** 4 - (od - 2 * wall) ** 4)
Z = I / (od / 2)
E = 20000.0                                   # MPa, pultruded tube along its length (assumed, 17 to 28 GPa)
f_flex = 200.0                                # MPa, flexural strength along the tube (assumed)
H_hand = 1.1
H_hook = 3.0
stand = 4.0
reach_x = a0                                  # the arm-shank corner sits on the beam
theta = math.atan((H_hook - H_hand) / stand)
s_front = math.hypot(stand, H_hook - H_hand)
out("F1", "Pole elevation when the hook is set at 3.0 m from 4.0 m away", math.degrees(theta), "deg")
x_front = reach_x - s_front * 1000            # front hand on the pole axis
x_rear = D["butt"] + 100
out("F2", "Front hand from the butt", x_front - D["butt"], "mm", "must be below the hand band")
out("F3", "Hand band from the butt", D["band_x"][0] - D["butt"], "mm")
# loads along the axis: (x, kg)
head_kg = M["hook plate"] + M["socket"] + M["welds"]
tip_extra = M["shackle 1"] + M["leader"] + 0.30          # plus about 3 m of rope hanging
loads = [(130.0, head_kg), (P["eye"][0], tip_extra)]
lin = (M["pole sections (tube)"] + M["foam core"]) / (P["sec_len"] * P["n_sec"])
for (a, b) in D["secs"]:
    n = 40
    for k in range(n):
        loads.append((a + (k + 0.5) * (b - a) / n, lin * (b - a) / n))
for j in D["joints"]:
    loads.append((j, M["sleeves"] / len(D["joints"])))
W = sum(m for _, m in loads) * g
c = math.cos(theta)
M_front = sum(m * g * (x - x_front) * c for x, m in loads if x > x_front)        # N mm, ahead of the front hand
M_all = sum(m * g * (x - x_front) * c for x, m in loads)
spacing = x_front - x_rear
F_rear = M_all / spacing
F_fr = W + F_rear
out("F4", "Pole set weight (pole, head, leader, hanging rope)", W, "N")
out("F5", "Rear hand pushes down with", F_rear, "N", f"hands {spacing / 1000:.2f} m apart")
out("F6", "Front hand lifts", F_fr, "N", "two-person pole team: one lifts, one holds the butt down")
s_pole = M_front / Z
out("F7", "Pole bending stress at the front hand", s_pole, "MPa", f"factor {f_flex / s_pole:.1f} on 200 MPa")
# tip deflection of a cantilever from the front hand (numerical, unit-load method on point loads)
L_c = (P["spike"][0] - x_front)
defl = 0.0
for x, m in loads:
    a = x - x_front
    if a <= 0:
        continue
    Pz = m * g * c
    # deflection at the reach point (distance L_r) from a point load at distance a
    L_r = reach_x - x_front
    if a >= L_r:
        d_ = Pz * L_r ** 2 * (3 * a - L_r) / (6 * E * I)
    else:
        d_ = Pz * a ** 2 * (3 * L_r - a) / (6 * E * I)
    defl += d_
out("F8", "Droop of the hook at the reach point", defl, "mm", "aim this much high, then lower onto the beam")
out("F9", "Pole tube second moment of area", I / 1e4, "cm^4")
m_set = sum(v for k, v in M.items() if k not in ("shackle 1", "leader"))
out("F10", "Pole and hook head mass (R5)", m_set, "kg", "target 8 kg or less")
out("F11", "Margin on R5", 8.0 - m_set, "kg")
out("F12", "Longest piece to carry (R8)", (P["sec_len"] + P["sleeve"][2] / 2) / 1000, "m", "a section with its bonded sleeve")

# ------------------------------------------------------------------ G. pole joints and release (R12)
mu = 0.5
A_ring = math.pi * od * P["ring"][1]
G2 = head_kg * g * math.sin(theta)
F_off = out("G1", "Set force to pull the pole out of the hook head", 50.0, "N",
            "friction ring wrapped until this is reached (set by trial); 4 x the hook head weight along the pole")
out("G2", "Hook head weight along the pole at 25 deg", G2, "N", "the ring must hold more than this")
out("G3", "Ring contact pressure that gives G1", F_off / (mu * A_ring), "MPa", "friction 0.5 (assumed)")
tau_nylon = 40.0
A_pin = math.pi * (P["pin"][0] / 2) ** 2
out("G4", "Joint pin double-shear capacity", 2 * A_pin * tau_nylon, "N", "nylon 66, 40 MPa in shear")
out("G5", "Pin capacity against the pull-out force", 2 * A_pin * tau_nylon / F_off, "", "pins never carry the rope pull")
bond = math.pi * od * P["sleeve"][2] / 2 * 5.0
out("G6", "Bonded sleeve capacity", bond / 1000, "kN", "150 mm overlap, 5 MPa allowable epoxy shear")

# ------------------------------------------------------------------ H. insulation (R4, R14)
out("H1", "Insulated length, socket mouth to hand band", D["insulated"], "mm", "no metal in this length; pins are nylon")
out("H2", "Required by R14", 3000.0, "mm")

# ------------------------------------------------------------------ I. deployment and pull time (R6, R7)
steps6 = [("Cut seal, unlock, lift out one set", 20), ("Carry to the fire edge, 100 m at 1 m/s", 100),
          ("Join three sections, two pins", 20), ("Hook head onto the pole", 5),
          ("Set the hook on the beam", 25), ("Withdraw the pole, step out of the fall zone", 10)]
t6 = sum(s for _, s in steps6)
out("I1", "Store to hook set, pole team of two (R6)", t6 / 60, "min",
    "the other two lay out the rope and run the check card in parallel")
steps7 = [("Haulers take toggles, caller checks the zone", 30), ("Take up slack", 10), ("Pull until the frame falls", 30)]
out("I2", "Hook set to frame down (R7)", sum(s for _, s in steps7) / 60, "min", "estimate; set by a timed trial at TRL 4")


def main():
    with (ROOT / "docs" / "04-calcs" / "results.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ref", "quantity", "value", "unit", "note"])
        for ref, q, v, u, n in R:
            w.writerow([ref, q, f"{v:.4g}" if isinstance(v, float) else v, u, n])


if __name__ == "__main__":
    main()
