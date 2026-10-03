"""BreakHook parametric model (build123d), TRL 3, constructable design (BHK-DDR-002).

Run from the repo root:
    python cad/src/model.py            export STEP and STL to cad/step and cad/stl
    python cad/src/model.py --check    constructability checks (overlaps, fits, masses)

One BreakHook set is a steel hook head on a three-section fibreglass pole, a short steel wire
rope leader shackled to the hook head, a 25 m pull rope, ten hauling toggles, a fork prop carried
separately (BHK-DDR-003) and a share of a wall rack. A community kit is two sets and one rack.

Coordinates in mm. The pole axis is the X axis, the hook head at +X, the butt at -X. The hook
plate lies in the XZ plane, centred on Y = 0; the hook arm points down (-Z), which is how it
sits over a beam in use. The open end of the socket on the hook head is at X = 0.
Every main dimension is in PARAMS; derived() gives the positions the drawings and pictures use.
CONCEPT, NOT FOR FABRICATION until a TRL 4 build and proof load confirm it.
"""
import math
import sys
from pathlib import Path

from build123d import (Axis, Box, BuildSketch, Circle, Compound, Cylinder, Locations, Plane, Polygon, Pos,
                       Rectangle, Rot, Sphere, Torus, export_step, export_stl, extrude, fillet)

ROOT = Path(__file__).resolve().parents[2]

PARAMS = {
    # hook plate: 10 mm S355 steel plate, profile cut (x along the pole, z up)
    "plate_t": 10.0,
    "root": (-50.0, 12.0, 28.0),          # part in the socket: from x, to x, half height
    "shank": (300.0, 18.0),               # shank to x = 300, half height 18 (36 wide)
    "spike": (440.0,),                    # spike tip on the axis
    "arm_top": (243.0, 291.0),            # arm where it leaves the shank (back face, front face)
    "arm_bot": (208.0, 256.0, -135.0),    # arm at its bottom (back face, front face, z)
    "barb_tip": (183.0, -148.0),          # barb points back toward the user
    "tab": (25.0, 85.0, -62.0, 30.0),     # rope tab: from x, to x, centre z of its round end, end radius
    "eye": (55.0, -55.0, 13.0),           # shackle hole: x, z, diameter
    "fillet_r": 8.0,                      # inside corners of the profile
    # socket: 50.8 x 2.0 mm welded steel tube (2 in OD, 14 gauge)
    "socket": (50.8, 2.0, 180.0),         # OD, wall, length (x from -180 to 0)
    "slot": (10.5, 50.0),                 # slot width and depth, cut across the tube end, top and bottom
    "weld_leg": 6.0,
    # pole: pultruded fibreglass round tube, foam filled, 44.5 x 3.2 mm (1.75 in x 1/8 in)
    "pole": (44.5, 3.2),
    "sec_len": 1800.0,                    # three sections, each 1.8 m
    "n_sec": 3,
    "joint_gap": 2.0,                     # gap between section ends inside a sleeve
    "sleeve": (50.8, 44.9, 300.0),        # sleeve OD, bore after sanding, length (bonded 150, sliding 150)
    "pin": (10.0, 10.5, 75.0),            # nylon pin diameter, hole diameter, pin from the joint line
    "ring": (46.6, 40.0, 110.0),          # friction ring on the pole tip: OD, length, start from the tip
    "band": (1550.0, 50.0),               # red hand band: from the butt, width
    "cap": (50.5, 46.0, 6.0),             # butt cap OD, length, end thickness
    # rope system
    "shackle": (11.0, 5.0, 16.8, 40.0),   # pin diameter, body radius, jaw width, pin to bow centre
    "leader": (6.0, 1500.0),              # 6 mm galvanised wire rope, eye to eye
    "thimble": (15.0, 4.0, 4.0),          # eye ring radius, wire radius, drop below the bow wire (model)
    "rope": (12.0, 25000.0),              # 12 mm polyester double braid, 25 m
    "coil": (220.0, 40.0),                # rope coil for storage: ring radius, bundle radius
    # hauling toggles: 32 x 3 mm fibreglass tube, 300 long, 10 mm cross hole, 6 mm cord prusik sling
    "toggle": (32.0, 3.0, 300.0, 10.0),
    "n_toggle": 10,
    "cord": 6.0,
    # wall rack: 40 x 6 mm steel flat bar
    "flat": (40.0, 6.0),
    "upright_h": 800.0,
    "arm_len": 250.0,
    "arm_z": (250.0, 500.0),
    "lip_h": 30.0,
    "peg": (700.0, 380.0, 40.0),          # rope peg: height, length, lip height (coil hangs clear of the arms)
    "rack_pitch": 1200.0,                 # upright spacing
    "wall_hole": (11.0, 50.0, 750.0),     # hole diameter and heights for M10 anchors
    # fork prop (BHK-DDR-003): carried separately, holds the pole at mid-length while the hook is set
    "prop_outer": (32.0, 3.0, 1000.0),    # lower tube: fibreglass 32 x 3 (toggle stock), length
    "prop_inner": (25.4, 3.2, 1100.0),    # upper tube: fibreglass 25.4 x 3.2, slides in the lower tube
    "prop_holes": (150.0, 50.0, 16),      # setting holes in the upper tube: first from its foot, pitch, count
    "prop_pin_down": 50.0,                # setting pin hole below the top of the lower tube
    "prop_fork": (12.0, 100.0, 85.0, 60.0, 50.0, 30.0),   # HDPE plate: thick, wide, height above the tube top,
                                          # tongue depth in the slot, notch width, notch bottom above the tube top
    "prop_slot": 12.5,                    # slot across the top of the upper tube for the fork tongue
    "prop_bolts": (8.0, 15.0, 45.0),      # nylon M8 bolts through tube and tongue, depths below the tube top
    "prop_cap": (36.0, 40.0, 6.0),        # rubber foot cap: OD, length, end thickness
    "prop_band": (850.0, 50.0),           # red hand band on the lower tube: from the foot, width (hold below)
    "prop_lean": 10.0,                    # target lean of the prop, top toward the wall (deg)
    # materials (kg/m3)
    "rho_steel": 7850.0,
    "rho_frp": 1900.0,
    "rho_foam": 60.0,
    "rho_nylon": 1140.0,
}


def derived(P=PARAMS):
    od, wall = P["pole"]
    L = P["sec_len"]
    tip = P["root"][0]                                  # pole tip sits against the end of the plate
    secs = []
    x_hi = tip
    for i in range(P["n_sec"]):
        x_lo = x_hi - L
        secs.insert(0, (x_lo, x_hi))
        x_hi = x_lo - P["joint_gap"]
    joints = [(secs[i][1] + secs[i + 1][0]) / 2 for i in range(P["n_sec"] - 1)]   # joint centre lines
    butt = secs[0][0]
    D = dict(secs=secs, joints=joints, butt=butt, tip=tip,
             socket_x=(-P["socket"][2], 0.0),
             overall=(butt - (P["cap"][1] - 40.0), P["spike"][0]),
             band_x=(butt + P["band"][0], butt + P["band"][0] + P["band"][1]),
             insertion=tip - (-P["socket"][2]))
    D["length"] = D["overall"][1] - D["overall"][0]
    D["insulated"] = (-P["socket"][2]) - D["band_x"][1]        # socket mouth to the top of the hand band
    D["prop_x"] = (D["overall"][0] + D["overall"][1]) / 2      # the prop holds the pole at mid-length
    sx, sz = P["eye"][0], P["eye"][1]
    D["shackle_c"] = (sx, 0.0, sz)
    D["bow_z"] = sz - P["shackle"][3]                           # centre of the shackle bow
    D["leader_z"] = D["bow_z"] - (P["shackle"][2] / 2 + P["shackle"][1])
    return D


# ----------------------------------------------------------------------------------- helpers
def _xz(face_builder_shape, t):
    """Extrude a sketch made in local XY by t (centred) and stand it in the world XZ plane."""
    s = extrude(face_builder_shape, amount=t / 2, both=True)
    return Rot(90, 0, 0) * s


def _tube_x(od, idia, x0, x1, y=0.0, z=0.0):
    L = x1 - x0
    o = Cylinder(od / 2, L, rotation=(0, 90, 0))
    if idia:
        o = o - Cylinder(idia / 2, L + 2, rotation=(0, 90, 0))
    return Pos((x0 + x1) / 2, y, z) * o


def _rod(p0, p1, d):
    """Round rod of diameter d from p0 to p1 (any direction)."""
    import numpy as np
    a, b = np.array(p0, float), np.array(p1, float)
    v = b - a
    L = float(np.linalg.norm(v))
    c = Cylinder(d / 2, L)
    u = v / L
    ang = math.degrees(math.acos(max(-1.0, min(1.0, u[2]))))
    ax = np.cross([0, 0, 1], u)
    m = (a + b) / 2
    if np.linalg.norm(ax) < 1e-9:
        return Pos(*m) * (c if u[2] > 0 else Rot(180, 0, 0) * c)
    from build123d import Location, Vector
    return Pos(*m) * Location((0, 0, 0), Vector(*ax), ang) * c


def _fuse(shapes):
    out = None
    for s in shapes:
        out = s if out is None else out + s
    return out


# ----------------------------------------------------------------------------------- hook head
def hook_plate(P=PARAMS):
    x0, x1, hr = P["root"]
    xs, hs = P["shank"]
    tx0, tx1, tz, tr = P["tab"]
    a0, a1 = P["arm_top"]
    b0, b1, bz = P["arm_bot"]
    with BuildSketch() as sk:
        Polygon((x0, -hr), (x1, -hr), (30, -hs), (xs, -hs), (xs, hs), (30, hs), (x1, hr), (x0, hr), align=None)
        Polygon((xs - 1, -hs), (420, -5), (P["spike"][0], 0), (420, 5), (xs - 1, hs), align=None)
        Polygon((a0, -hs + 1), (a1, -hs + 1), (b1, bz), (b0, bz), align=None)
        Polygon((b0 + 2, bz + 17), (b1, bz), (b1 - 14, bz - 17), P["barb_tip"], align=None)
        Polygon((tx0, -hs + 1), (tx1, -hs + 1), (tx1, tz), (tx0, tz), align=None)
        with Locations(((tx0 + tx1) / 2, tz)):
            Circle(tr)
        # inside corners where the arm and the tab meet the shank get a radius
        inner = [v for v in sk.vertices() if abs(v.Y + hs) < 0.6 and (abs(v.X - a0) < 0.6 or abs(v.X - a1) < 0.6
                                                                         or abs(v.X - tx1) < 0.6 or abs(v.X - tx0) < 0.6)]
        if inner:
            fillet(inner, P["fillet_r"])
        with Locations((P["eye"][0], P["eye"][1])):
            from build123d import Mode
            Circle(P["eye"][2] / 2, mode=Mode.SUBTRACT)
    return _xz(sk.sketch, P["plate_t"])


def socket(P=PARAMS):
    od, w, L = P["socket"]
    t = _tube_x(od, od - 2 * w, -L, 0.0)
    sw, sd = P["slot"]
    cut = Pos(-sd / 2 + 0.5, 0, 0) * Box(sd + 1, sw, od + 4)
    return t - cut


def welds(P=PARAMS):
    """Four fillet welds, one along each side of each slot, outside the tube (6 mm leg)."""
    od = P["socket"][0]
    sd = P["slot"][1]
    t = P["plate_t"]
    leg = P["weld_leg"]
    out = []
    for zs in (1, -1):
        for ys in (1, -1):
            # a triangular bead in the corner between the plate face and the tube surface
            y = ys * (t / 2 + leg / 2 - 0.6)
            z = zs * (math.sqrt((od / 2) ** 2 - y ** 2) + leg / 2 - 1.6)
            out.append(Pos(-sd / 2, y, z) * Box(sd, leg - 1, leg - 1))
    return _fuse(out)


# ----------------------------------------------------------------------------------- pole
def pole_sections(P=PARAMS):
    D = derived(P)
    od, wall = P["pole"]
    out = []
    for i, (a, b) in enumerate(D["secs"]):
        s = _tube_x(od, od - 2 * wall, a, b)
        # pin holes: in the upper (toward the hook) section of each joint, 75 mm from the joint line
        for j in D["joints"]:
            xp = j + P["pin"][2]
            if a < xp < b:
                s = s - Pos(xp, 0, 0) * Cylinder(P["pin"][1] / 2, od + 4)
        out.append(s)
    return out


def sleeves(P=PARAMS):
    D = derived(P)
    od, bore, L = P["sleeve"]
    out = []
    for j in D["joints"]:
        s = _tube_x(od, bore, j - L / 2, j + L / 2)
        s = s - Pos(j + P["pin"][2], 0, 0) * Cylinder(P["pin"][1] / 2, od + 4)
        out.append(s)
    return out


def pins(P=PARAMS):
    """Nylon clevis pins, vertical through each joint, head on top, clip below."""
    D = derived(P)
    d = P["pin"][0]
    od = P["sleeve"][0]
    out = []
    for j in D["joints"]:
        x = j + P["pin"][2]
        body = Pos(x, 0, 0) * Cylinder(d / 2, od + 16)
        head = Pos(x, 0, od / 2 + 2.5) * Cylinder(9, 5)
        clip = Pos(x, 0, -od / 2 - 5) * (Rot(90, 0, 0) * Torus(7, 1.2))
        out.append(body + head + clip)
    return out


def friction_ring(P=PARAMS):
    od, L, start = P["ring"]
    tip = derived(P)["tip"]
    return _tube_x(od, P["pole"][0], tip - start - L, tip - start)


def hand_band(P=PARAMS):
    D = derived(P)
    a, b = D["band_x"]
    return _tube_x(P["pole"][0] + 0.6, P["pole"][0], a, b)


def butt_cap(P=PARAMS):
    od, L, t = P["cap"]
    D = derived(P)
    x0 = D["butt"] - t
    outer = _tube_x(od, None, x0, x0 + L)
    return outer - _tube_x(P["pole"][0], None, D["butt"], x0 + L + 1)


# ----------------------------------------------------------------------------------- rope system
def shackle(c, P=PARAMS):
    """Bow shackle, pin along Y through c, bow hanging below (-Z)."""
    pd, r, jaw, leg = P["shackle"]
    x, y, z = c
    yl = jaw / 2 + r
    pin = Pos(x, 0, z) * Cylinder(pd / 2, 2 * yl + 2 * r + 8, rotation=(90, 0, 0))
    head = Pos(x, -(yl + r + 4), z) * Cylinder(pd / 2 + 3, 5, rotation=(90, 0, 0))
    legs = [Pos(x, s * yl, z - leg / 2) * Cylinder(r, leg) for s in (1, -1)]
    bow = Pos(x, 0, z - leg) * (Rot(0, 90, 0) * Torus(yl, r))
    bow = bow - Pos(x, 0, z - leg + 50) * Box(200, 200, 100)       # keep the lower half
    return _fuse([pin, head] + legs + [bow])


def leader(P=PARAMS):
    """6 mm wire rope with a thimble eye and ferrule at each end, lying back along the pole."""
    D = derived(P)
    R, rw, drop = P["thimble"]
    d, L = P["leader"]
    x, _, _ = D["shackle_c"]
    zb = D["bow_z"] - (P["shackle"][2] / 2 + P["shackle"][1]) - drop   # eye hangs on the bottom of the bow
    e1c = (x, 0.0, zb)
    eye1 = Pos(*e1c) * (Rot(90, 0, 0) * Torus(R, rw))
    x_end = x - L
    eye2 = Pos(x_end, 0, zb) * (Rot(90, 0, 0) * Torus(R, rw))
    cable = _tube_x(d, None, x_end + R + rw, x - R - rw, z=zb)
    fer = [_tube_x(14, None, x - R - rw - 45, x - R - rw - 5, z=zb),
           _tube_x(14, None, x_end + R + rw + 5, x_end + R + rw + 45, z=zb)]
    return _fuse([eye1, eye2, cable] + fer), (x_end, zb)


def rope_end(P=PARAMS):
    """Second shackle and the spliced eye of the pull rope at the far end of the leader."""
    _, (xe, ze) = leader(P)
    R = P["thimble"][0]
    # the second shackle's pin passes through the middle of the leader's far eye; its bow hangs below
    pd, r, jaw, leg = P["shackle"]
    sh = shackle((xe, 0.0, ze), P)
    # spliced eye of the 12 mm rope round the bottom of the bow, in the XZ plane, dropped 7 mm
    Re = 20.0
    zb = ze - leg - (jaw / 2 + r) - 7.0
    eye = Pos(xe, 0, zb) * (Rot(90, 0, 0) * Torus(Re, P["rope"][0] / 2))
    return sh, eye


def rope_coil(c=(0, 0, 0), P=PARAMS):
    R, r = P["coil"]
    return Pos(*c) * Torus(R, r)


def toggle(c=(0, 0, 0), P=PARAMS):
    """Hauling toggle along Y with a 10 mm cross hole along Z."""
    od, w, L, h = P["toggle"]
    t = Cylinder(od / 2, L, rotation=(90, 0, 0)) - Cylinder((od - 2 * w) / 2, L + 2, rotation=(90, 0, 0))
    t = t - Cylinder(h / 2, od + 4)
    return Pos(*c) * t


def toggle_on_rope(P=PARAMS, length=600.0):
    """A short length of pull rope (along X) with one toggle hung on a prusik cord: for pictures."""
    rd = P["rope"][0]
    cd = P["cord"]
    rope = _tube_x(rd, None, -length / 2, length / 2)
    wraps = _fuse([Pos(dx, 0, 0) * (Rot(0, 90, 0) * Torus(rd / 2 + cd / 2 + 0.5, cd / 2)) for dx in (-14, 0, 14)])
    zt = -170.0
    tog = toggle((0, 0, zt), P)
    legs = _fuse([_rod((s * 7, 0, -rd / 2 - cd / 2 - 1), (0, 0, zt + P["toggle"][0] / 2 + 1), cd) for s in (1, -1)])
    thru = Pos(0, 0, zt) * Cylinder(cd / 2, P["toggle"][0] + 2)
    knot = Pos(0, 0, zt - P["toggle"][0] / 2 - 9) * Sphere(9)
    return {"rope": rope, "prusik": wraps + legs + thru + knot, "toggle": tog}


# ----------------------------------------------------------------------------------- rack
def rack_upright(P=PARAMS, x=0.0):
    """One rack upright: flat bar against the wall (wall plane y = 0), two arms and a rope peg."""
    fw, ft = P["flat"]
    H = P["upright_h"]
    up = Pos(x, ft / 2, H / 2) * Box(fw, ft, H)
    for zh in (P["wall_hole"][1], P["wall_hole"][2]):
        up = up - Pos(x, ft / 2, zh) * Cylinder(P["wall_hole"][0] / 2, ft + 2, rotation=(90, 0, 0))
    arms = []
    for za in P["arm_z"]:
        arms.append(Pos(x, ft + P["arm_len"] / 2, za + ft / 2) * Box(fw, P["arm_len"], ft))
        arms.append(Pos(x, ft + P["arm_len"] - ft / 2, za + ft + P["lip_h"] / 2) * Box(fw, ft, P["lip_h"]))
    pz, pl, ph = P["peg"]
    arms.append(Pos(x, ft + pl / 2, pz + ft / 2) * Box(fw, pl, ft))
    arms.append(Pos(x, ft + pl - ft / 2, pz + ft + ph / 2) * Box(fw, ft, ph))
    return up, _fuse(arms)


def rack_slots(P=PARAMS):
    """Centres (y, z) of the pole positions on one arm level: four per arm."""
    ft = P["flat"][1]
    d = P["pole"][0]
    return [ft + 5 + d / 2 + k * (d + 11.5) for k in range(4)]


# ----------------------------------------------------------------------------------- fork prop
def prop_notch(P=PARAMS, k=0):
    """Height of the bottom of the fork notch above the ground at setting hole k (0 = longest)."""
    zpin = P["prop_cap"][2] + P["prop_outer"][2] - P["prop_pin_down"]
    h0, pitch, n = P["prop_holes"]
    zb = zpin - (h0 + k * pitch)
    return zb + P["prop_inner"][2] + P["prop_fork"][5], zb


def prop(P=PARAMS, k=0):
    """Fork prop in its own frame: foot on the ground at the origin, axis +Z, fork plate in the YZ plane
    (its notch takes a pole running along X). k is the setting hole (0 = longest, 7 = shortest).
    Returns {name: shape}."""
    od, w, L = P["prop_outer"]
    idd, iw, Li = P["prop_inner"]
    cod, cl, ct = P["prop_cap"]
    t, fw, fh, tongue, nw, nb = P["prop_fork"]
    h0, pitch, n = P["prop_holes"]
    zpin = ct + L - P["prop_pin_down"]
    _, zb = prop_notch(P, k)
    ztop = zb + Li

    def tz(o, i, z0, z1):
        c = Pos(0, 0, (z0 + z1) / 2) * Cylinder(o / 2, z1 - z0)
        return c - Pos(0, 0, (z0 + z1) / 2) * Cylinder(i / 2, z1 - z0 + 2) if i else c

    out = {}
    lower = tz(od, od - 2 * w, ct, ct + L)
    lower = lower - Pos(0, 0, zpin) * Cylinder(P["pin"][1] / 2, od + 4, rotation=(90, 0, 0))
    out["prop_lower"] = lower
    upper = tz(idd, idd - 2 * iw, zb, ztop)
    for i in range(n):
        upper = upper - Pos(0, 0, zb + h0 + i * pitch) * Cylinder(P["pin"][1] / 2, idd + 4, rotation=(90, 0, 0))
    upper = upper - Pos(0, 0, ztop - tongue / 2 + 0.5) * Box(P["prop_slot"], idd + 4, tongue + 1)
    bd, b1, b2 = P["prop_bolts"]
    for zb_ in (b1, b2):
        upper = upper - Pos(0, 0, ztop - zb_) * Cylinder(bd / 2 + 0.25, idd + 4, rotation=(0, 90, 0))
    out["prop_upper"] = upper
    head = Pos(0, 0, ztop + fh / 2) * Box(t, fw, fh)
    head = head - Pos(0, 0, ztop + nb + nw / 2 + fh / 2) * Box(t + 2, nw, fh)
    head = head - Pos(0, 0, ztop + nb + nw / 2) * Cylinder(nw / 2, t + 2, rotation=(0, 90, 0))
    fork = head + Pos(0, 0, ztop - tongue / 2) * Box(t, idd, tongue)
    for zb_ in (b1, b2):
        fork = fork - Pos(0, 0, ztop - zb_) * Cylinder(bd / 2 + 0.25, t + 2, rotation=(0, 90, 0))
    out["prop_fork"] = fork
    bolts = []
    for zb_ in (b1, b2):
        z = ztop - zb_
        bolts += [Pos(0, 0, z) * Cylinder(bd / 2, idd + 12, rotation=(0, 90, 0)),
                  Pos(-(idd / 2 + 2.5), 0, z) * Cylinder(6.5, 5, rotation=(0, 90, 0)),
                  Pos(idd / 2 + 3.5, 0, z) * Cylinder(6.5, 7, rotation=(0, 90, 0))]
    out["prop_bolts"] = _fuse(bolts)
    pd = P["pin"][0]
    out["prop_pin"] = (Pos(0, 0, zpin) * Cylinder(pd / 2, od + 16, rotation=(90, 0, 0))
                       + Pos(0, -(od / 2 + 2.5), zpin) * Cylinder(9, 5, rotation=(90, 0, 0))
                       + Pos(0, od / 2 + 5, zpin) * Torus(7, 1.2))
    cap = tz(cod, None, 0.0, cl) - Pos(0, 0, ct + cl / 2) * Cylinder(od / 2, cl)
    out["prop_cap"] = cap
    b0, bw = P["prop_band"]
    out["prop_band"] = tz(od + 0.6, od, b0, b0 + bw)
    return out


PROP_ORDER = ["prop_cap", "prop_lower", "prop_band", "prop_upper", "prop_fork", "prop_bolts", "prop_pin"]


def prop_setting(P=PARAMS, contact_z=None):
    """Setting hole k and lean (deg) that put the fork under a pole whose underside is contact_z above the
    ground at the prop, as near the target lean as the holes allow (lean between 0 and 20 deg)."""
    best = None
    for k in range(P["prop_holes"][2]):
        h, _ = prop_notch(P, k)
        if h < contact_z:
            continue
        lean = math.degrees(math.acos(contact_z / h))
        if lean <= 20.0 and (best is None or abs(lean - P["prop_lean"]) < abs(best[1] - P["prop_lean"])):
            best = (k, lean)
    return best


def prop_in_use(P=PARAMS, beam=None):
    """The prop under the pole at mid-length in the deployed pose, in world coordinates (as posed()).
    The fork notch is brought to 0.5 mm under the middle pole section. Returns ({name: shape}, info)."""
    D = derived(P)
    th_d, (tx, tz) = deploy_pose(P) if beam is None else deploy_pose(P, beam)
    th = math.radians(th_d)
    r = P["pole"][0] / 2
    xp = D["prop_x"]
    cx, cz = _rot_xz((xp, -r / math.cos(th)), th)
    cx, cz = cx + tx, cz + tz                                   # pole underside, straight below its axis
    k, lean = prop_setting(P, cz)
    sec = posed(build_components(P)["section_2"], P) if beam is None else None
    h, _ = prop_notch(P, k)
    parts = prop(P, k)
    fork0, cap0 = parts["prop_fork"], parts["prop_cap"]
    lr = math.radians(lean)

    def place(lr, shift):
        ux, uz = math.sin(lr), math.cos(lr)
        return Pos(cx - h * ux + shift * ux, 0, cz - h * uz + shift * uz) * Rot(0, math.degrees(lr), 0)

    shift = 0.0
    for _ in range(4):                     # lean so the foot cap sits on the ground, then close the fork
        lo, hi = -20.0, 20.0               # bisect for the shift where the fork first touches the pole
        for _ in range(14):
            mid = (lo + hi) / 2
            if (place(lr, mid) * fork0 & sec).volume > 0.01:
                hi = mid
            else:
                lo = mid
        shift = lo - 0.5                   # leave about 0.5 mm under the pole
        gap = (place(lr, shift) * fork0).distance_to(sec)
        low = (place(lr, shift) * cap0).bounding_box().min.Z
        if abs(low) < 0.3:
            break
        lr -= low / (h * math.sin(lr))
    lean = math.degrees(lr)
    loc = place(lr, shift)
    ux = math.sin(lr)
    foot_x = cx - h * ux + shift * ux
    out = {kname: loc * sh for kname, sh in parts.items()}
    return out, dict(k=k, lean=lean, notch=h, foot=(foot_x, low), contact=(cx, cz), gap=gap)


def prop_stowed(P=PARAMS, x_foot=-680.0, k=6):
    """One prop lying on an upper rack arm (rack coordinates), fork plate standing up, fork toward +X."""
    ft = P["flat"][1]
    zr = P["arm_z"][1] + ft + P["prop_outer"][0] / 2
    parts = prop(P, k)
    return {n: Pos(x_foot, 0, zr) * (Rot(0, 90, 0) * (Rot(0, 0, 90) * s)) for n, s in parts.items()}


# ----------------------------------------------------------------------------------- components
def build_components(P=PARAMS):
    """Every component of one set, in place on the assembled hook (rack and coil at their own spots)."""
    D = derived(P)
    C = {}
    C["plate"] = hook_plate(P)
    C["socket"] = socket(P)
    C["welds"] = welds(P)
    secs = pole_sections(P)
    for i, s in enumerate(secs):
        C[f"section_{i + 1}"] = s
    for i, s in enumerate(sleeves(P)):
        C[f"sleeve_{i + 1}"] = s
    for i, s in enumerate(pins(P)):
        C[f"pin_{i + 1}"] = s
    C["ring"] = friction_ring(P)
    C["band"] = hand_band(P)
    C["cap"] = butt_cap(P)
    C["shackle_1"] = shackle(D["shackle_c"], P)
    C["leader"], _ = leader(P)
    C["shackle_2"], C["rope_eye"] = rope_end(P)
    return C


SET_ORDER = ["plate", "socket", "welds", "section_1", "section_2", "section_3", "sleeve_1", "sleeve_2",
             "pin_1", "pin_2", "ring", "band", "cap", "shackle_1", "leader", "shackle_2", "rope_eye"]


def assembly(P=PARAMS, with_rope=False):
    C = build_components(P)
    keys = [k for k in SET_ORDER if with_rope or k not in ("shackle_2", "rope_eye")]
    return Compound([C[k] for k in keys])


def head_weldment(P=PARAMS):
    return hook_plate(P) + socket(P) + welds(P)


def stowed(P=PARAMS):
    """The community kit on its rack (rack coordinates: wall at y = 0, floor of the rack at z = 0).
    Lower arms: sections 1 and 2 of both sets (sleeves at alternate ends). Upper arms: section 3 of each
    set with its hook head, shackle and leader left on, and the two fork props between them, set short.
    Rope coils hang on the pegs.
    Returns {name: shape}."""
    D = derived(P)
    ft = P["flat"][1]
    d = P["pole"][0]
    ys = rack_slots(P)
    z_lo = P["arm_z"][0] + ft + d / 2
    z_hi = P["arm_z"][1] + ft + d / 2
    C = build_components(P)
    out = {}
    for i, x in enumerate((-P["rack_pitch"] / 2, P["rack_pitch"] / 2)):
        up, arms = rack_upright(P, x)
        out[f"upright_{i + 1}"] = up + arms
    x_mid = lambda a, b: -(a + b) / 2                                      # noqa: E731
    s1, s2, s3 = D["secs"]
    for k, (sec, slv, y) in enumerate((("section_1", "sleeve_1", ys[0]), ("section_2", "sleeve_2", ys[1]),
                                       ("section_1", "sleeve_1", ys[2]), ("section_2", "sleeve_2", ys[3]))):
        a, b = D["secs"][0] if sec == "section_1" else D["secs"][1]
        flip = Rot(0, 0, 180) if k in (1, 3) else Rot(0, 0, 0)            # sleeves at alternate ends
        sh = C[sec] + C[slv]
        if sec == "section_1":
            sh = sh + C["band"] + C["cap"]
        out[f"lower_{k + 1}"] = Pos(0, y, z_lo) * (flip * (Pos(x_mid(a, b), 0, 0) * sh))
    a, b = s3
    head = ["plate", "socket", "welds", "ring", "shackle_1", "leader", "shackle_2", "rope_eye"]
    for k, y in enumerate((ys[0], ys[2])):
        sh = _fuse([C["section_3"]] + [C[h] for h in head])
        out[f"upper_{k + 1}"] = Pos(0, y, z_hi) * (Pos(x_mid(a, b), 0, 0) * sh)
    for k, y in enumerate((ys[1], ys[3])):
        out[f"prop_{k + 1}"] = Compound([Pos(0, y, 0) * s for s in prop_stowed(P).values()])
    pz, pl, ph = P["peg"]
    R, r = P["coil"]
    for i, x in enumerate((-P["rack_pitch"] / 2, P["rack_pitch"] / 2)):
        out[f"coil_{i + 1}"] = Pos(x, ft + pl - ft - r - 40, pz + ft - (R - r) + 2.0) * (Rot(90, 0, 0) * Torus(R, r))
    return out


def rack_assembly(P=PARAMS):
    parts = []
    for x in (-P["rack_pitch"] / 2, P["rack_pitch"] / 2):
        up, arms = rack_upright(P, x)
        parts += [up, arms]
    return parts


# ----------------------------------------------------------------------------------- in use (pictures)
BEAM = (50.0, 75.0, 2400.0)       # wall plate of the test frame: width, depth, top height (mm)


def _rot_xz(v, th):
    """Rotate a local (x, z) vector by the pole elevation th (radians), +X toward +Z."""
    x, z = v
    return (x * math.cos(th) - z * math.sin(th), x * math.sin(th) + z * math.cos(th))


def deploy_pose(P=PARAMS, beam=BEAM):
    """Pole elevation and offset that set the hook over the wall plate of the test frame with the butt
    resting on the ground. The plate's far face is at world x = 0; the user is toward -x.
    Returns (theta in degrees, (tx, tz)) to apply as Pos(tx, 0, tz) * Rot(0, -theta, 0) * shape."""
    w, d, top = beam
    D = derived(P)
    Ql = (P["arm_top"][0], -P["shank"][1])                     # inside corner of arm and shank
    a = (P["arm_bot"][0] - P["arm_top"][0], P["arm_bot"][2] + P["shank"][1])
    butt = (D["overall"][0], -P["cap"][0] / 2)

    def place(th):
        ax, az = _rot_xz(a, th)
        k = ax / az
        qz = top + w * math.tan(th) + 3.0
        qx = 0.0 - k * (top - qz) + 2.0
        rq = _rot_xz(Ql, th)
        return qx - rq[0], qz - rq[1]

    lo, hi = math.radians(10), math.radians(60)
    for _ in range(60):
        th = (lo + hi) / 2
        tx, tz = place(th)
        bz = tz + _rot_xz(butt, th)[1]
        if bz > 0:
            lo = th
        else:
            hi = th
    th = (lo + hi) / 2
    return math.degrees(th), place(th)


def posed(shape, P=PARAMS):
    th, (tx, tz) = deploy_pose(P)
    return Pos(tx, 0, tz) * (Rot(0, -th, 0) * shape)


def rope_deployed(P=PARAMS):
    """Pull rope in the in-use pictures: from its eye down to the ground, along it, and a coil (before
    any scene turn). Returns (run, coil)."""
    eye = posed(rope_end(P)[1], P).bounding_box()
    e = (eye.center().X, 0.0, eye.min.Z + 8)
    g1 = (e[0] - 600, 250.0, 7.0)
    g2 = (-4300.0, 1250.0, 7.0)
    run = _rod(e, g1, P["rope"][0]) + _rod(g1, g2, P["rope"][0])
    return run, rope_coil((-4650.0, 1500.0, 40.0), P)


def test_frame(beam=BEAM, split=False):
    """Context only: a single-storey test dwelling frame, 3.0 x 3.0 m, open at the near wall top so the
    hook can be seen. Timber posts, plates and rafters; corrugated sheet on the far and side walls."""
    w, d, top = beam
    L, Wd = 3000.0, 3000.0
    parts = []
    y0 = Wd / 2
    for x in (-w, L - w):
        parts.append(Pos(x + w / 2, 0, top - d / 2) * Box(w, Wd, d))                    # near and far plates
        for y in (-y0 + 37.5, y0 - 37.5, 0.0 if x > 0 else None):
            if y is None:
                continue
            parts.append(Pos(x + w / 2, y, (top - d) / 2) * Box(w, 75, top - d))
    # near wall mid posts either side of the hook
    for y in (-750.0, 750.0):
        parts.append(Pos(-w / 2, y, (top - d) / 2) * Box(w, 75, top - d))
    for y in (-y0 + 25, y0 - 25):
        parts.append(Pos(L / 2 - w, y, top - d / 2) * Box(L, w, d))                       # side plates
    rise = 300.0
    import math as _m
    slope = _m.degrees(_m.atan(rise / L))
    for y in (-1200.0, -400.0, 400.0, 1200.0):
        parts.append(Pos(L / 2 - w, y, top + 50 + rise / 2) * (Rot(0, -slope, 0) * Box(L + 300, 50, 100)))
    sheet = 2.0
    parts.append(Pos(L - w + sheet / 2 + w, 0, (top - d) / 2) * Box(sheet, Wd, top - d))     # far wall sheet
    for y in (-y0 - sheet / 2, y0 + sheet / 2):
        parts.append(Pos(L / 2 - w, y, (top - d) / 2) * Box(L, sheet, top - d))           # side wall sheets
    if split:
        return _fuse(parts[:-3]), _fuse(parts[-3:])
    return _fuse(parts)


# ----------------------------------------------------------------------------------- checks
def masses(P=PARAMS):
    C = build_components(P)
    od, wall = P["pole"]
    foam_area = math.pi * ((od - 2 * wall) / 2) ** 2
    st = P["rho_steel"] * 1e-9
    frp = P["rho_frp"] * 1e-9
    m = {}
    m["hook plate"] = C["plate"].volume * st
    m["socket"] = C["socket"].volume * st
    m["welds"] = C["welds"].volume * st * 0.5            # a fillet bead is half its bounding box
    m["pole sections (tube)"] = sum(C[f"section_{i + 1}"].volume for i in range(P["n_sec"])) * frp
    m["foam core"] = foam_area * P["sec_len"] * P["n_sec"] * P["rho_foam"] * 1e-9
    m["sleeves"] = sum(C[f"sleeve_{i + 1}"].volume for i in range(P["n_sec"] - 1)) * frp
    m["pins"] = sum(C[f"pin_{i + 1}"].volume for i in range(P["n_sec"] - 1)) * P["rho_nylon"] * 1e-9
    m["cap, ring, band"] = 0.08
    m["shackle 1"] = C["shackle_1"].volume * st
    m["leader"] = C["leader"].volume * st
    return m


def prop_mass(P=PARAMS):
    """Fork prop mass (kg), carried separately from the pole and hook head."""
    Q = prop(P, 0)
    frp = P["rho_frp"] * 1e-9
    m = {"lower tube": Q["prop_lower"].volume * frp, "upper tube": Q["prop_upper"].volume * frp,
         "fork plate (HDPE)": Q["prop_fork"].volume * 960e-9, "bolts and pin (nylon)":
         (Q["prop_bolts"].volume + Q["prop_pin"].volume) * P["rho_nylon"] * 1e-9,
         "foot cap and band": Q["prop_cap"].volume * 1200e-9 + 0.01}
    return m


def check(P=PARAMS):
    D = derived(P)
    C = build_components(P)
    allowed = {frozenset(p) for p in [("plate", "welds"), ("socket", "welds"), ("pin_1", "section_2"),
                                      ("pin_2", "section_3"), ("pin_1", "sleeve_1"), ("pin_2", "sleeve_2"),
                                      ("ring", "section_3"), ("band", "section_1")]}
    keys = list(C)
    bad = []
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b = keys[i], keys[j]
            if frozenset((a, b)) in allowed:
                continue
            ba, bb = C[a].bounding_box(), C[b].bounding_box()
            if (ba.min.X > bb.max.X or bb.min.X > ba.max.X or ba.min.Y > bb.max.Y or bb.min.Y > ba.max.Y
                    or ba.min.Z > bb.max.Z or bb.min.Z > ba.max.Z):
                continue
            v = (C[a] & C[b]).volume
            if v > 1.0:
                bad.append((a, b, round(v, 1)))
    print("overlaps over 1 mm3:", bad or "none")
    # fits
    od, wall = P["pole"]
    sid = P["socket"][0] - 2 * P["socket"][1]
    print(f"pole in socket: radial clearance {(sid - od) / 2:.2f} mm; ring clearance {(sid - P['ring'][0]) / 2:.2f} mm; "
          f"insertion {D['insertion']:.0f} mm")
    print(f"plate in slot: {(P['slot'][0] - P['plate_t']) / 2:.2f} mm each side; plate stands "
          f"{P['root'][2] - P['socket'][0] / 2:.1f} mm proud of the tube for the weld")
    print(f"sleeve on pole: radial gap {(P['sleeve'][1] - od) / 2:.2f} mm (sanded bore)")
    print(f"pin in hole: {(P['pin'][1] - P['pin'][0]) / 2:.2f} mm radial")
    pd, r, jaw, leg = P["shackle"]
    print(f"shackle pin {pd} in {P['eye'][2]} hole; jaw {jaw} over {P['plate_t']} plate")
    # touching parts (each must touch at least one neighbour)
    pairs = [("section_3", "plate"), ("section_1", "sleeve_1"), ("section_2", "sleeve_2"), ("cap", "section_1")]
    for a, b in pairs:
        d = C[a].distance_to(C[b])
        print(f"{a} to {b}: gap {d:.2f} mm")
    # rack: poles rest on arms inside the lips
    ys = rack_slots(P)
    print("rack pole centres from wall:", [round(y, 1) for y in ys], "lip inner face at",
          P["flat"][1] + P["arm_len"] - P["flat"][1])
    m = masses(P)
    pole_hook = sum(v for k, v in m.items() if k not in ("shackle 1", "leader"))
    for k, v in m.items():
        print(f"  {k}: {v:.3f} kg")
    print(f"pole and hook head: {pole_hook:.2f} kg; with shackle and leader {sum(m.values()):.2f} kg")
    print(f"overall length {D['length']:.0f} mm; insulated length {D['insulated']:.0f} mm; sections {D['secs']}")
    bad += check_prop(P)
    return bad


def _overlaps(S, allowed=()):
    allowed = {frozenset(p) for p in allowed}
    keys = list(S)
    bad = []
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b = keys[i], keys[j]
            if frozenset((a, b)) in allowed:
                continue
            ba, bb = S[a].bounding_box(), S[b].bounding_box()
            if (ba.min.X > bb.max.X or bb.min.X > ba.max.X or ba.min.Y > bb.max.Y or bb.min.Y > ba.max.Y
                    or ba.min.Z > bb.max.Z or bb.min.Z > ba.max.Z):
                continue
            v = (S[a] & S[b]).volume
            if v > 1.0:
                bad.append((a, b, round(v, 1)))
    return bad


def check_prop(P=PARAMS):
    """Fork prop (BHK-DDR-003): its own parts, the fits, its place under the pole and on the rack."""
    bad = []
    for k in (0, P["prop_holes"][2] - 1):
        b = _overlaps(prop(P, k), [("prop_band", "prop_lower"), ("prop_cap", "prop_lower")])
        print(f"prop setting {k}: overlaps over 1 mm3:", b or "none")
        bad += b
    od, w, _ = P["prop_outer"]
    idd = P["prop_inner"][0]
    print(f"prop upper tube in lower tube: radial clearance {(od - 2 * w - idd) / 2:.2f} mm; fork tongue in slot "
          f"{(P['prop_slot'] - P['prop_fork'][0]) / 2:.2f} mm each side; notch {P['prop_fork'][4]:.0f} for a "
          f"{P['pole'][0]} pole")
    Q = prop(P, 0)
    for a, b in (("prop_fork", "prop_upper"), ("prop_cap", "prop_lower"), ("prop_upper", "prop_lower")):
        print(f"{a} to {b}: gap {Q[a].distance_to(Q[b]):.2f} mm")
    lo, hi = prop_notch(P, P["prop_holes"][2] - 1)[0], prop_notch(P, 0)[0]
    print(f"prop notch height range {lo:.0f} to {hi:.0f} mm in {P['prop_holes'][1]:.0f} mm steps; "
          f"shortest length {hi - (hi - lo) + P['prop_fork'][2] - P['prop_fork'][5]:.0f} mm")
    U, info = prop_in_use(P)
    C = {k: posed(v, P) for k, v in build_components(P).items()}
    allc = dict(C)
    allc.update(U)
    b = [x for x in _overlaps(allc, [("prop_band", "prop_lower"), ("prop_cap", "prop_lower")])
         if x[0].startswith("prop") or x[1].startswith("prop")]
    print(f"prop in use: setting {info['k']}, lean {info['lean']:.1f} deg, fork to pole gap {info['gap']:.2f} mm, "
          f"foot {-info['foot'][0] / 1000:.2f} m from the wall plate face; overlaps with the set:", b or "none")
    bad += b
    ft = U["prop_cap"].bounding_box().min.Z
    print(f"prop foot cap lowest point {ft:.1f} mm (ground at 0)")
    S = stowed(P)
    b = [x for x in _overlaps(S) if x[0].startswith("prop") or x[1].startswith("prop")]
    print("props on the rack: overlaps over 1 mm3:", b or "none")
    bad += b
    for nm, q in S.items():
        if nm.startswith("prop"):
            bb = q.bounding_box()
            print(f"  {nm}: x {bb.min.X:.0f} to {bb.max.X:.0f}, lowest {bb.min.Z:.1f} (arm top "
                  f"{P['arm_z'][1] + P['flat'][1]:.0f})")
    pm = prop_mass(P)
    for k, v in pm.items():
        print(f"  prop {k}: {v:.3f} kg")
    print(f"fork prop: {sum(pm.values()):.2f} kg, carried separately")
    return bad


def export(P=PARAMS):
    step = ROOT / "cad" / "step"
    stl = ROOT / "cad" / "stl"
    step.mkdir(parents=True, exist_ok=True)
    stl.mkdir(parents=True, exist_ok=True)
    C = build_components(P)
    export_step(assembly(P, with_rope=True), str(step / "breakhook-assembly.step"))
    export_step(head_weldment(P), str(step / "hook-head.step"))
    export_step(hook_plate(P), str(step / "hook-plate.step"))
    export_step(socket(P), str(step / "socket.step"))
    export_step(C["section_2"], str(step / "pole-section-middle.step"))
    export_step(C["sleeve_1"], str(step / "joint-sleeve.step"))
    export_step(toggle((0, 0, 0), P), str(step / "hauling-toggle.step"))
    export_step(Compound(rack_upright(P, 0.0)), str(step / "rack-upright.step"))
    Q = prop(P, 0)
    export_step(Compound([Q[k] for k in PROP_ORDER]), str(step / "fork-prop.step"))
    export_step(Q["prop_fork"], str(step / "fork-prop-plate.step"))
    export_stl(head_weldment(P), str(stl / "hook-head.stl"), tolerance=0.2, angular_tolerance=0.3)
    export_stl(toggle((0, 0, 0), P), str(stl / "hauling-toggle.stl"), tolerance=0.2, angular_tolerance=0.3)
    export_stl(Q["prop_fork"], str(stl / "fork-prop-plate.stl"), tolerance=0.2, angular_tolerance=0.3)
    print("exported STEP and STL")


if __name__ == "__main__":
    if "--check" in sys.argv:
        check()
    else:
        export()
