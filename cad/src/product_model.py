"""BreakHook product appearance model (build123d), TRL 3, constructable design (BHK-DDR-002).

Finished look for photoreal renders: the high-visibility yellow hook head (profile-cut plate welded
into its slotted socket), the orange foam-filled fibreglass pole in three sections with its dark
bonded sleeves, white nylon pins, red hand band and black butt cap, the galvanised bow shackles and
wire rope leader, the blue pull rope, the teal hauling toggles on purple prusik cords, the dark teal
fork prop with its white HDPE fork (BHK-DDR-003) and the wall rack. Context: a single-storey test dwelling frame (timber posts, plates and rafters, corrugated
sheet on three walls) and a 1.75 m mannequin standing by the pole butt.
APPEARANCE MODEL ONLY: no tolerances, no fabrication detail. CONCEPT, NOT FOR FABRICATION.

Every main dimension comes from cad/src/model.py (PARAMS, build_components, posed, rope_deployed,
test_frame, toggle, rack_upright, prop, prop_in_use); nothing is typed in again. The scene is turned 180 degrees about
Z so the pole butt and the mannequin face the render camera. Differences from model.py are listed
in docs/REVIEW.md (none change a dimension).

    from product_model import product_parts
    for p in product_parts(): print(p["name"], p["group"], p["material"])
"""
import sys
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent), str(Path(__file__).resolve().parents[2] / ".kit")]

from build123d import Box, Pos, Rot, Torus  # noqa: E402
from model import (PARAMS, derived, build_components, posed, rope_deployed, test_frame, toggle,  # noqa: E402
                   rope_coil, rack_upright, rack_slots, _fuse, _tube_x, prop, prop_in_use)

TITLE = "BreakHook: firebreak hook, pole and pull rope set"

RENDER_VIEWS = [
    {"name": "hero", "groups": ["set", "rope", "context"], "explode": False, "el": 22, "az": -40,
     "note": "Product render from the front right and above (about 22 deg elevation): the hook set over the "
             "wall plate of a test dwelling frame, pole butt on the ground beside a 1.75 m person, wire rope "
             "leader and blue pull rope running back to its coil; the fork prop holds the pole at mid-length. "
             "The pole and prop are withdrawn before anyone hauls"},
    {"name": "exploded", "groups": ["xset", "xkit"], "explode": True, "el": 28, "az": -55,
     "note": "Exploded view from the front right and above (about 28 deg elevation): hook plate, socket and "
             "welds at the hook end; the three pole sections laid side by side with their sleeves, nylon pins, "
             "hand band and butt cap; shackles and wire rope leader below; pull rope coil, ten hauling "
             "toggles on prusik cords and the fork prop, closed, beside"},
    {"name": "detail", "groups": ["dset", "dctx"], "explode": False, "el": 14, "az": -30,
     "note": "Detail from the front right, slightly above (about 14 deg elevation): the hook arm behind the "
             "wall plate, the shank resting on the plate, the shackle in the rope eye in line with the arm and "
             "the pole tip in its socket"},
]

TURN = Rot(0, 0, 180)
COLOR = {"plate": "#D9A400", "socket": "#D9A400", "welds": "#B88A00", "section": "#E07B24", "sleeve": "#9A3412",
         "pin": "#F3F4F6", "ring": "#1F2937", "band": "#DC2626", "cap": "#111827", "shackle": "#A1A1AA",
         "leader": "#71717A", "rope": "#1D4ED8", "toggle": "#0F766E", "cord": "#7C3AED"}
PROP_LOOK = {"prop_cap": ("Fork prop foot cap", "#111827", "rubber"), "prop_lower": ("Fork prop lower tube", "#0E7490", "plastic"),
             "prop_band": ("Fork prop hand band", "#DC2626", "plastic"), "prop_upper": ("Fork prop upper tube", "#0E7490", "plastic"),
             "prop_fork": ("Fork plate, HDPE", "#F3F4F6", "plastic"), "prop_bolts": ("Fork bolts, nylon", "#F3F4F6", "plastic"),
             "prop_pin": ("Prop setting pin, nylon", "#F3F4F6", "plastic")}
MAT = {"plate": "painted", "socket": "painted", "welds": "painted", "section": "plastic", "sleeve": "plastic",
       "pin": "plastic", "ring": "rubber", "band": "plastic", "cap": "rubber", "shackle": "metal",
       "leader": "metal", "rope": "fabric", "toggle": "plastic", "cord": "fabric"}
NAME = {"plate": ("Hook plate", 1), "socket": ("Socket tube", 2), "welds": ("Socket welds", 3),
        "section": ("Pole section", 4), "sleeve": ("Joint sleeve", 5), "pin": ("Joint pin", 6),
        "ring": ("Friction ring", 8), "band": ("Hand band", 9), "cap": ("Butt cap", 10),
        "shackle": ("Shackle", 11), "leader": ("Wire rope leader", 12), "rope": ("Pull rope eye", 13)}


def _kind(key):
    return "rope" if key == "rope_eye" else key.split("_")[0]


def product_parts(P=PARAMS):
    D = derived(P)
    out = []

    def add(name, shape, color, material, bom, group, explode=(0, 0, 0)):
        out.append({"name": name, "shape": shape, "color": color, "material": material,
                    "bom": bom, "group": group, "explode": tuple(float(v) for v in explode)})

    # ---- hero: the set in use, over the test frame
    C = build_components(P)
    for key, sh in C.items():
        k = _kind(key)
        add(f"{NAME[k][0]} ({key})", TURN * posed(sh, P), COLOR[k], MAT[k], NAME[k][1], "set")
    run, coil = rope_deployed(P)
    add("Pull rope", TURN * run, COLOR["rope"], "fabric", 13, "rope")
    add("Pull rope coil", TURN * coil, COLOR["rope"], "fabric", 13, "rope")
    U, _ = prop_in_use(P)
    for key, sh in U.items():
        nm, col, mat = PROP_LOOK[key]
        add(nm, TURN * sh, col, mat, 26, "set")
    timber, sheets = test_frame(split=True)
    add("Test frame timber (context)", TURN * timber, "#B08D5B", "wood", None, "context")
    add("Test frame corrugated sheet, steel (context)", TURN * sheets, "#A3A8AE", "metal", None, "context")
    from context_parts import mannequin
    person = mannequin(1750.0, "stand")
    butt_x = -D["butt"]                                    # after the turn the butt is at +x
    add("Person, 1.75 m (scale)", Pos(butt_x - 250.0, -650.0, 0.0) * (Rot(0, 0, -90) * person), "#9CA3AF",
        "clay", None, "context")

    # ---- exploded: one set straight, pole sections laid side by side, rope coil and toggles beside
    C = build_components(P)
    s1 = D["secs"][0]
    shift1 = D["secs"][2][0] - s1[0]
    shift2 = D["secs"][2][0] - D["secs"][1][0]
    E = {"plate": (420, 0, 130), "welds": (300, 0, 260), "socket": (150, 0, 0), "section_3": (0, 0, 0),
         "ring": (0, 0, 110), "section_2": (shift2, -230, 0), "sleeve_2": (shift2 - 260, -230, 0),
         "pin_2": (shift2 + 80, -230, 140), "section_1": (shift1, -460, 0), "sleeve_1": (shift1 - 260, -460, 0),
         "pin_1": (shift1 + 80, -460, 140), "band": (shift1, -460, 110), "cap": (shift1 - 220, -460, 0),
         "shackle_1": (0, 0, -170), "leader": (0, 260, -260), "shackle_2": (-220, 260, -300),
         "rope_eye": (-420, 260, -330)}
    for key, sh in C.items():
        k = _kind(key)
        ex, ey, ez = E[key]
        add(f"{NAME[k][0]} ({key})", TURN * sh, COLOR[k], MAT[k], NAME[k][1], "xset", (-ex, -ey, ez))
    add("Pull rope coil", TURN * rope_coil((-1250.0, 700.0, -330.0), P), COLOR["rope"], "fabric", 13, "xkit")
    togs, cords = [], []
    for i in range(P["n_toggle"]):
        x = -1700.0 + i * 150
        togs.append(Pos(x, 1250.0, -330.0) * toggle((0, 0, 0), P))
        cords.append(Pos(x, 1250.0, -330.0) * (Rot(90, 0, 0) * Torus(70, P["cord"] / 2)))
    add("Hauling toggles", TURN * _fuse(togs), COLOR["toggle"], "plastic", 14, "xkit")
    add("Prusik cords", TURN * _fuse(cords), COLOR["cord"], "fabric", 15, "xkit")
    Q = prop(P, P["prop_holes"][2] - 1)
    for key, sh in Q.items():
        nm, col, mat = PROP_LOOK[key]
        add(f"{nm} (closed)", TURN * (Pos(-1700.0, 1650.0, -330.0) * (Rot(0, 90, 0) * (Rot(0, 0, 90) * sh))), col, mat,
            26, "xkit")

    # ---- detail: the hook head over the wall plate, cut to a window round the head
    C = build_components(P)
    win = Pos(0, 0, 2300) * Box(1100, 700, 700)
    for key in ("plate", "socket", "welds", "ring", "shackle_1", "section_3", "leader"):
        k = _kind(key)
        sh = posed(C[key], P) & win
        add(f"{NAME[k][0]} ({key}, detail)", TURN * sh, COLOR[k], MAT[k], NAME[k][1], "dset")
    timber, sheets = test_frame(split=True)
    add("Test frame timber (context, detail)", TURN * (timber & win), "#B08D5B", "wood", None, "dctx")
    return out


if __name__ == "__main__":
    for p in product_parts():
        bb = p["shape"].bounding_box()
        print(f"{p['group']:8s} {p['name']:45s} {p['material']:8s} {bb.size.X:7.0f} {bb.size.Y:7.0f} {bb.size.Z:7.0f}")
