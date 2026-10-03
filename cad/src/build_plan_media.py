"""BreakHook prototype build plan pictures (BHK-BLD-001, STANDARDS section 18).

Run from the repo root:  python cad/src/build_plan_media.py [overview|sheets|joints|steps ...]
With no argument it draws everything. Every picture is drawn from cad/src/model.py, so the pictures
and the model never disagree:
    docs/05-build-plan/overview.png        every component pulled apart, numbered in build order
    cad/drawings/BHK-DWG-101 to 106        making sketches for the made components
    cad/drawings/BHK-DWG-107               making sketch for the fork prop (BHK-DDR-003)
    docs/05-build-plan/joint-NN.png        close-ups of the joints that need explaining
    docs/05-build-plan/step-NN.png         one picture per assembly step
Uses .kit/build_views.py. BUILD PLAN ILLUSTRATION, PLAN NOT YET BUILT.
Long parts (the 1.8 m pole sections) are cut to a window round the joint in close-ups and steps.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
import build_views as bv  # noqa: E402
from build_views import Part  # noqa: E402
from build123d import Box, Compound, Pos, Rot  # noqa: E402
from model import (PARAMS as P, derived, build_components, toggle, toggle_on_rope, rack_upright, stowed,  # noqa: E402
                   posed, test_frame, rope_coil, _fuse, _tube_x, prop, prop_in_use, prop_notch)

OUT = ROOT / "docs" / "05-build-plan"
DWG = ROOT / "cad" / "drawings"
DATE = "2026-10-03"
D = derived(P)
C = build_components(P)
COL = {"plate": "#D9A400", "socket": "#B7791F", "welds": "#374151", "section": "#E07B24", "sleeve": "#9A3412",
       "pin": "#E5E7EB", "ring": "#1F2937", "band": "#DC2626", "cap": "#111827", "shackle": "#64748B",
       "leader": "#475569", "rope": "#1D4ED8", "toggle": "#0F766E", "cord": "#7C3AED", "rack": "#57534E",
       "frame": "#B08D5B", "prop": "#0E7490", "fork": "#F8FAFC", "propband": "#DC2626"}
Q = prop(P, 0)                                   # fork prop at its longest setting, foot at the origin, axis +Z
QL = {k: Rot(0, 90, 0) * (Rot(0, 0, 90) * v) for k, v in Q.items()}      # the same lying along X, fork at +X


def win(shape, x0, x1, y=400.0, z=600.0):
    return shape & Pos((x0 + x1) / 2, 0, 0) * Box(x1 - x0, 2 * y, 2 * z)


def part(name, shape, color, explode=(0, 0, 0), alpha=1.0):
    return Part(name, shape, color, None, tuple(explode), alpha)


J1, J2 = D["joints"]


# ----------------------------------------------------------------- overview
def overview():
    s1, s2, s3 = D["secs"]
    sh1 = s3[0] - s1[0]
    sh2 = s3[0] - s2[0]
    tog = _fuse([Pos(-1500 + k * 140, 1900, -350) * toggle((0, 0, 0), P) for k in range(P["n_toggle"])])
    up, arms = rack_upright(P, 0.0)
    rack = Pos(-700, -1900, -600) * (Rot(0, 0, -90) * (up + arms))
    items = [
        ("Hook plate", C["plate"], COL["plate"], (700, 0, 250)),
        ("Socket tube", C["socket"], COL["socket"], (350, 0, 0)),
        ("Hook head welds", C["welds"], COL["welds"], (450, 0, 150)),
        ("Pole section 1 (butt)", C["section_1"], COL["section"], (sh1, -900, 0)),
        ("Pole section 2 (middle)", C["section_2"], COL["section"], (sh2, -450, 0)),
        ("Pole section 3 (top)", C["section_3"], COL["section"], (0, 0, 0)),
        ("Joint sleeves (2, one shown)", C["sleeve_2"], COL["sleeve"], (0, -225, 260)),
        ("Joint pins (2, one shown)", C["pin_2"], COL["pin"], (0, -225, 480)),
        ("Hand band", C["band"], COL["band"], (sh1, -900, 220)),
        ("Butt cap", C["cap"], COL["cap"], (sh1 - 400, -900, 0)),
        ("Friction ring", C["ring"], COL["ring"], (200, 0, 160)),
        ("Shackles (2, one shown)", C["shackle_1"], COL["shackle"], (300, 450, -120)),
        ("Wire rope leader", C["leader"], COL["leader"], (0, 650, 0)),
        ("Pull rope", rope_coil((-900, 1300, -350), P), COL["rope"], (0, 0, 0)),
        ("Hauling toggles and prusik cords (10)", tog, COL["toggle"], (0, 0, 0)),
        ("Fork prop: lower tube, foot cap and band", Pos(-2700, -1500, -300) * (QL["prop_lower"] + QL["prop_cap"]
                                                                          + QL["prop_band"]), COL["prop"], (0, 0, 0)),
        ("Fork prop: upper tube", Pos(-2700, -1500, -300) * QL["prop_upper"], "#22A3C3", (700, 0, 0)),
        ("Fork plate and two nylon bolts", Pos(-2700, -1500, -300) * (QL["prop_fork"] + QL["prop_bolts"]),
         "#94A3B8", (1050, 0, 0)),
        ("Prop setting pin", Pos(-2700, -1500, -300) * QL["prop_pin"], COL["pin"], (0, 0, 200)),
        ("Rack uprights (2, one shown)", rack, COL["rack"], (0, 0, 0)),
    ]
    parts = [part(n, s, c, e) for n, s, c, e in items]
    bv.overview(parts, OUT / "overview.png", "BreakHook: one set and its rack, in build order", key=True,
                size=(11, 7))


# ----------------------------------------------------------------- making sketches
def sheets():
    tip = _tube_x(P["pole"][0], P["pole"][0] - 2 * P["pole"][1], -400, D["tip"])
    common = dict(project="BreakHook", date=DATE)
    bv.component_sheet(part("Hook plate", C["plate"], COL["plate"]),
                       [part("", C["socket"], ""), part("", C["welds"], ""), part("", C["shackle_1"], ""),
                        part("", tip, "")], **common, dwg_no="BHK-DWG-101", title="Hook plate: making sketch",
                       material="10 mm S355 steel plate, one per set", notes=[
            "Cut from 10 mm S355 plate, blank 500 x 200; one piece, no forging",
            "Spike: tip on the centre line, 440 from the socket end of the plate",
            "Shank 36 wide; the 56 wide end (62 long) goes into the socket slots",
            "Arm 48 wide hangs 117 below the shank, raked back 17 deg; barb at its foot",
            "Rope tab under the shank, 25 to 85 from the socket end, round end R30",
            "Shackle hole 13, centred 55 from the socket end and 55 below the axis",
            "Inside corners at the arm and tab: drill 16 and file to R8; no sharp notch",
            "Cut by plasma or chain drill and grinder; dress all edges, break corners 1",
            "Throat between tab and arm: 150 wide at the shank, 128 at 100 below",
            "Fits: plate stands 2.6 proud of the tube top and bottom for the welds",
            "Check: lay on the full-size print; every edge within 1 mm",
            "Stamp WLL 3 kN and the serial number on the shank before painting",
        ])
    bv.component_sheet(part("Socket tube", C["socket"], COL["socket"]),
                       [part("", C["plate"], ""), part("", tip, "")], **common, dwg_no="BHK-DWG-102",
                       title="Socket tube: making sketch", material="Welded steel tube 50.8 x 2.0, one per set", notes=[
            "Cut 180 long from 50.8 x 2.0 welded steel tube; square the ends",
            "Slot one end across a diameter: two slots 10.5 wide, 50 deep, top and bottom",
            "Mark the slots with a strip of paper round the tube so they line up",
            "Cut with a hacksaw or thin cutting disc; file to 10.5, square at the root",
            "Deburr the bore at the open end and break its edge 1 x 45 deg",
            "The bore is 46.8: the 44.5 pole slides in with 1.15 clearance each side",
            "The pole goes in 130 and stops against the end of the plate",
            "Fits: the plate slides into both slots with no more than 0.5 total play",
            "Check: a 300 offcut of pole tube slides in and out by hand",
        ])
    sec = C["section_2"]
    bv.component_sheet(part("Pole section", sec, COL["section"]),
                       [part("", C["sleeve_1"], ""), part("", C["sleeve_2"], ""), part("", win(C["section_1"], J1 - 400, J1), ""),
                        part("", win(C["section_3"], J2, J2 + 400), "")], **common, dwg_no="BHK-DWG-103",
                       title="Pole section (make 3): making sketch",
                       material="Foam-filled fibreglass tube 44.5 x 3.2, electrical grade", notes=[
            "Cut three lengths of 1800 from foam-filled fibreglass tube 44.5 x 3.2",
            "Fine-tooth saw with the tube wrapped in tape; wear a dust mask outdoors",
            "Seal every cut end with a thin coat of epoxy so water cannot get into the foam",
            "Middle and top sections: drill one 10.5 hole across the tube, 74 from the",
            "  bottom end (75 above the joint line), square to the tube, through both walls",
            "Butt section: no pin hole; its sleeve is bonded at its top end",
            "Middle section: sleeve bonded at its top end; pin hole at its bottom end",
            "Top section: pin hole at its bottom end; friction ring at its top end",
            "Coat each pin hole bore with epoxy as well",
            "Check: each section 1800 within 2; holes square to the tube by eye",
        ], view_shape=Pos(-(sec.bounding_box().center().X), 0, 0) * sec)
    slv = C["sleeve_2"]
    bv.component_sheet(part("Joint sleeve", slv, COL["sleeve"]),
                       [part("", win(C["section_2"], J2 - 400, J2), ""), part("", win(C["section_3"], J2, J2 + 400), ""),
                        part("", C["pin_2"], "")], **common, dwg_no="BHK-DWG-104", title="Joint sleeve (make 2): making sketch",
                       material="Fibreglass tube 50.8 x 3.2, 300 long", notes=[
            "Cut two lengths of 300 from 50.8 x 3.2 fibreglass tube; seal the ends",
            "Sand the bore with coarse paper on a dowel until the pole tube slides in",
            "  (about 0.2 clearance each side); try it often, do not overdo it",
            "Drill one 10.5 hole across the sleeve, 75 from the middle (225 from one end)",
            "Bond the other half (150) onto the top of the lower section with epoxy,",
            "  the hole end sticking up; wipe off squeeze-out; cure a full day",
            "Then slide the upper section in, drill through its pin hole into line",
            "Check: upper section slides in and out by hand; the pin goes through both",
        ], view_shape=Pos(-slv.bounding_box().center().X, 0, 0) * slv)
    T = toggle_on_rope(P)
    bv.component_sheet(part("Hauling toggle", T["toggle"], COL["toggle"]),
                       [part("", T["rope"], ""), part("", T["prusik"], "")], **common, dwg_no="BHK-DWG-105",
                       title="Hauling toggle (make 10 per set): making sketch",
                       material="Fibreglass tube 32 x 3, 300 long", notes=[
            "Cut ten lengths of 300 from 32 x 3 fibreglass tube; round and seal the ends",
            "Drill a 10 hole straight across at mid length (150 from each end)",
            "Sling: 1.2 m of 6 mm cord through the hole, tied into a loop with a",
            "  double fisherman's knot that sits under the toggle",
            "Hitch the loop to the pull rope with a three-turn prusik hitch",
            "  (it slides when loose and grips when pulled)",
            "Space the toggles 1 m apart, the first 11 m from the hook head",
            "Check: hang 30 kg on one toggle; the prusik must not slip",
        ])
    up, arms = rack_upright(P, 0.0)
    S = stowed(P)
    bv.component_sheet(part("Rack upright", up + arms, COL["rack"]),
                       [part("", win(S["lower_1"], -900, -350), ""), part("", win(S["upper_1"], -900, -350), "")],
                       **common, dwg_no="BHK-DWG-106", title="Rack upright (make 2): making sketch",
                       material="40 x 6 steel flat bar, welded, primed and painted", notes=[
            "Upright: 40 x 6 flat bar, 800 long; two 11 holes 50 and 750 up for M10 anchors",
            "Arms: two pieces 250 long, welded square to the front face, tops 256 and 506 up",
            "Lips: 30 tall, welded on the arm ends so poles cannot roll off",
            "Rope peg: 380 long at 700 up with a 40 tall lip; the coil hangs clear",
            "  of the arms below it",
            "Weld all round each arm root (5 fillet); grind smooth; prime and paint",
            "Two uprights 1200 apart on a wall, out of the sun and rain where possible",
            "Each arm holds four poles 56 apart; sleeves go at alternate ends",
            "Check: arms level and square to the wall; a 10 kg load leaves no movement",
        ], inset_view=(20, -50))
    prop_sheet()


def prop_sheet():
    common = dict(project="BreakHook", date=DATE)
    U, info = prop_in_use(P)
    sec = posed(C["section_2"], P)
    pole_w = sec & Pos(info["contact"][0], 0, info["contact"][1]) * Box(900, 300, 600)
    prop_all = Compound([Q[k] for k in ("prop_cap", "prop_lower", "prop_band", "prop_upper", "prop_fork", "prop_bolts",
                                     "prop_pin")])
    lo, hi = prop_notch(P, P["prop_holes"][2] - 1)[0], prop_notch(P, 0)[0]
    bv.component_sheet(part("Fork prop", Compound([U[k] for k in U]), COL["prop"]),
                       [part("", pole_w, "")], **common, dwg_no="BHK-DWG-107",
                       title="Fork prop (make 1 per set): making sketch",
                       material="Fibreglass tube 32 x 3 and 25.4 x 3.2; 12 HDPE fork plate; nylon bolts and pin", notes=[
            "Lower tube: 32 x 3 fibreglass, 1000 long; one 10.5 hole across, 50 below its top",
            "Upper tube: 25.4 x 3.2 fibreglass, 1100 long; it slides inside the lower tube",
            "  (0.3 clearance each side); sixteen 10.5 holes, 50 apart, the first 150 up",
            "  from its bottom end; all holes in one line, square to the tube",
            "Slot across the top of the upper tube: 12.5 wide, 60 deep (as the socket slots)",
            "Fork plate: 12 HDPE, 100 wide; notch 50 wide, round bottom R25, 30 above the",
            "  tube top; tongue 25.4 wide, 60 long into the slot; round all edges",
            "Two nylon M8 bolts through tube and tongue, 15 and 45 below the tube top",
            "Rubber foot cap; red band 850 to 900 up from the foot; hold below the band",
            f"Notch height {lo / 1000:.2f} to {hi / 1000:.2f} m in 50 steps; 1.24 m long when closed",
            "Seal cut ends and hole bores with epoxy; no metal anywhere in the prop",
            "Check: upper tube slides freely; the pin goes through at every hole",
        ], view_shape=prop_all, inset_view=(14, -70))


# ----------------------------------------------------------------- joints
def joints():
    tip = _tube_x(P["pole"][0], P["pole"][0] - 2 * P["pole"][1], -330, D["tip"])
    bv.joint([part("Hook plate", win(C["plate"], -60, 120), COL["plate"]),
              part("Socket tube", C["socket"], COL["socket"]),
              part("Four fillet welds, 6 mm, 50 long", C["welds"], COL["welds"])],
             OUT / "joint-01.png", "Joint 1: hook plate in the socket slots",
             "The plate goes 50 into slots top and bottom and is welded along both sides of each slot",
             elev=28, azim=-55)
    bv.joint([part("Socket tube (cut open)", C["socket"], COL["socket"]),
              part("Hook plate", win(C["plate"], -60, 60), COL["plate"]),
              part("Friction ring, rubber tape", C["ring"], COL["ring"]),
              part("Top pole section", tip, COL["section"])],
             OUT / "joint-02.png", "Joint 2: pole tip in the hook head",
             "Cut open: the pole goes in 130 and stops on the plate; the tape ring gives a firm 50 N push-off",
             cut="+Y", elev=20, azim=-70)
    bv.joint([part("Lower section", win(C["section_2"], J2 - 260, J2), COL["section"]),
              part("Joint sleeve, bonded to the lower section", C["sleeve_2"], COL["sleeve"]),
              part("Upper section", win(C["section_3"], J2, J2 + 260), "#F59E0B"),
              part("Nylon pin and clip", C["pin_2"], COL["pin"])],
             OUT / "joint-03.png", "Joint 3: pole joint",
             "Cut open: sections meet in the middle of the sleeve; glued below, pinned above", cut="+Y",
             elev=20, azim=-70)
    lx = C["leader"]
    bv.joint([part("Rope tab of the hook plate", win(C["plate"], 0, 120, z=200), COL["plate"]),
              part("Bow shackle, 3/8 in", C["shackle_1"], COL["shackle"]),
              part("Leader thimble eye", win(lx, -120, 120), COL["leader"])],
             OUT / "joint-04.png", "Joint 4: shackle in the rope eye",
             "Shackle pin through the 13 mm hole, nut side moused with wire; the leader eye on the bow",
             elev=18, azim=-60)
    xe = P["eye"][0] - P["leader"][1]
    bv.joint([part("Leader far eye", win(lx, xe - 60, xe + 150), COL["leader"]),
              part("Second shackle", C["shackle_2"], COL["shackle"]),
              part("Pull rope spliced eye", C["rope_eye"], COL["rope"])],
             OUT / "joint-05.png", "Joint 5: leader to pull rope",
             "Second shackle through the leader eye; the rope's spliced eye on its bow", elev=18, azim=-60)
    T = toggle_on_rope(P)
    bv.joint([part("Pull rope", T["rope"], COL["rope"]), part("Prusik cord, three turns", T["prusik"], COL["cord"]),
              part("Hauling toggle", T["toggle"], COL["toggle"])],
             OUT / "joint-06.png", "Joint 6: hauling toggle on the rope",
             "Three-turn prusik: slides when slack, grips under load", elev=22, azim=-60)
    w = Pos(-150, 0, 2300) * Box(900, 500, 700)
    frame = test_frame() & w
    head = [posed(C[k], P) & w for k in ("plate", "socket", "welds", "shackle_1", "section_3")]
    bv.joint([part("Wall plate of the test frame", frame, COL["frame"]),
              part("Hook plate", head[0], COL["plate"]), part("Socket", head[1] + head[2], COL["socket"]),
              part("Shackle", head[3], COL["shackle"]), part("Top pole section", head[4], COL["section"])],
             OUT / "joint-07.png", "Joint 7: the hook on a wall plate (in use)",
             "Shank on the plate, arm behind it; a pull on the rope draws the plate toward the haulers",
             elev=10, azim=-75)
    S = stowed(P)
    w = Pos(-600, 150, 400) * Box(500, 500, 900)
    bv.joint([part("Rack upright", S["upright_1"] & w, COL["rack"]),
              part("Butt and middle sections", _fuse([S[f"lower_{k}"] & w for k in range(1, 5)]), COL["section"]),
              part("Top sections, leader and shackles on", _fuse([S[f"upper_{k}"] & w for k in (1, 2)]), "#F59E0B"),
              part("Rope coil on the peg", S["coil_1"] & Pos(-600, 300, 500) * Box(800, 300, 800), COL["rope"])],
             OUT / "joint-08.png", "Joint 8: poles on the rack arms",
             "Four poles per arm, 56 apart, held by the lips; the coil hangs on the peg clear of the arms",
             elev=22, azim=-35)
    prop_joints()


def prop_joints():
    kmin = P["prop_holes"][2] - 1
    Q7 = prop(P, kmin)                              # shortest setting: fork and setting pin close together
    top = prop_notch(P, kmin)[1] + P["prop_inner"][2]
    w = Pos(0, 0, top - 60) * Box(300, 300, 400)
    bv.joint([part("Upper tube (cut open)", Q7["prop_upper"] & w, "#22A3C3"),
              part("Fork plate, 12 HDPE", Q7["prop_fork"], "#94A3B8"),
              part("Two nylon M8 bolts", Q7["prop_bolts"], COL["pin"]),
              part("Lower tube", Q7["prop_lower"] & w, COL["prop"]),
              part("Setting pin and clip", Q7["prop_pin"], "#F59E0B")],
             OUT / "joint-09.png", "Joint 9: fork plate and setting pin on the prop",
             "Tongue 60 deep in the slot, two nylon bolts; the pin sets the height in 50 mm steps", cut="+Y",
             elev=18, azim=-30)
    U, info = prop_in_use(P)
    cx, cz = info["contact"]
    w = Pos(cx, 0, cz - 40) * Box(600, 400, 420)
    bv.joint([part("Middle pole section", posed(C["section_2"], P) & w, COL["section"]),
              part("Fork plate", U["prop_fork"] & w, "#94A3B8"),
              part("Prop upper tube", U["prop_upper"] & w, "#22A3C3"),
              part("Nylon bolts", U["prop_bolts"] & w, COL["pin"])],
             OUT / "joint-10.png", "Joint 10: the pole resting in the fork (in use)",
             "The pole lies loose in the notch at mid-length; the fork lifts, it never clamps", elev=12, azim=-60)


# ----------------------------------------------------------------- steps
def steps():
    tip_w = lambda s: win(s, -420, 500)          # noqa: E731
    def st(n, done, new, title, sub=None, **kw):
        bv.step(done, new, OUT / f"step-{n:02d}.png", f"Step {n}: {title}", sub, **kw)
    st(1, [part("Socket tube", C["socket"], "")], [part("Hook plate", C["plate"], COL["plate"], (300, 0, 0))],
       "hook plate into the socket slots", "Slide the plate's wide end into both slots until it is 50 deep")
    st(2, [part("Socket tube", C["socket"], ""), part("Hook plate", C["plate"], "")],
       [part("Four fillet welds", C["welds"], COL["welds"])], "weld, clean and paint the hook head",
       "Tack, check square, then weld both sides of each slot; prime and paint yellow", elev=28, azim=-55)
    a1 = D["secs"][0][1]
    st(3, [part("Butt section", win(C["section_1"], a1 - 500, a1), "")],
       [part("Joint sleeve 1", C["sleeve_1"], COL["sleeve"], (400, 0, 0))],
       "bond a sleeve onto the butt section", "150 onto the top end with epoxy; cure a full day")
    a2 = D["secs"][1][1]
    st(4, [part("Middle section", win(C["section_2"], a2 - 500, a2), "")],
       [part("Joint sleeve 2", C["sleeve_2"], COL["sleeve"], (400, 0, 0))],
       "bond a sleeve onto the middle section", "Same as step 3, on the middle section's top end")
    b0 = D["butt"]
    st(5, [part("Butt section", win(C["section_1"], b0 - 10, b0 + 1800), "")],
       [part("Butt cap", C["cap"], COL["cap"], (-250, 0, 0)), part("Hand band", C["band"], COL["band"], (0, 0, 200))],
       "butt cap and hand band", "Cap pushed on; red band 1550 to 1600 from the butt end, under clear sleeve")
    st(6, [part("Top section", win(C["section_3"], -700, D["tip"]), "")],
       [part("Friction ring", C["ring"], COL["ring"], (0, 0, 150))],
       "friction ring on the top section", "Two or three turns of tape, 110 to 150 below the tip")
    st(7, [part("Butt section and sleeve", win(C["section_1"] + C["sleeve_1"], J1 - 500, J1 + 160), "")],
       [part("Middle section", win(C["section_2"], J1, J1 + 500), COL["section"], (400, 0, 0)),
        part("Nylon pin", C["pin_1"], COL["pin"], (0, 0, 200))],
       "join the butt and middle sections", "Push fully home, line up the holes, pin and clip")
    st(8, [part("Middle section and sleeve", win(C["section_2"] + C["sleeve_2"], J2 - 500, J2 + 160), "")],
       [part("Top section", win(C["section_3"], J2, J2 + 500), COL["section"], (400, 0, 0)),
        part("Nylon pin", C["pin_2"], COL["pin"], (0, 0, 200))],
       "join the middle and top sections", "As step 7")
    st(9, [part("Top section", tip_w(C["section_3"] + C["ring"]), "")],
       [part("Hook head", C["plate"] + C["socket"] + C["welds"], COL["plate"], (300, 0, 0))],
       "hook head onto the pole", "Push on over the friction ring until the pole stops on the plate")
    st(10, [part("Hook head and pole", tip_w(C["plate"] + C["socket"] + C["welds"] + C["section_3"]), "")],
       [part("Shackle", C["shackle_1"], COL["shackle"], (0, 0, -200)),
        part("Leader", win(C["leader"], -420, 200), COL["leader"], (0, 0, -200))],
       "shackle and leader onto the hook", "Leader eye on the shackle bow; pin through the hole, tighten and mouse")
    xe = P["eye"][0] - P["leader"][1]
    st(11, [part("Leader", win(C["leader"], xe - 50, xe + 500), "")],
       [part("Second shackle", C["shackle_2"], COL["shackle"], (0, 0, -150)),
        part("Pull rope eye", C["rope_eye"], COL["rope"], (0, 0, -300))],
       "pull rope onto the leader", "Second shackle through the far leader eye, rope eye on its bow; mouse the pin")
    T = toggle_on_rope(P)
    st(12, [part("Pull rope", T["rope"], "")],
       [part("Prusik cord", T["prusik"], COL["cord"], (0, 0, -150)), part("Toggle", T["toggle"], COL["toggle"], (0, 0, -150))],
       "toggles onto the rope", "Ten toggles, 1 m apart, the first 11 m from the hook head")
    st(13, [part("Lower tube, foot cap and band", QL["prop_lower"] + QL["prop_cap"] + QL["prop_band"], "")],
       [part("Upper tube with fork plate and bolts", QL["prop_upper"] + QL["prop_fork"] + QL["prop_bolts"], "#22A3C3",
             (700, 0, 0)), part("Setting pin", QL["prop_pin"], "#F59E0B", (0, 0, 220))],
       "assemble the fork prop", "Fork bolted into the upper tube; upper tube into the lower; pin at the set hole",
       elev=22, azim=-50)
    S = stowed(P)
    st(14, [], [part("Rack upright", S["upright_1"], COL["rack"], (0, 300, 0)),
                part("Rack upright", S["upright_2"], COL["rack"], (0, 300, 0))],
       "rack uprights onto the wall", "1200 apart, plumb, two M10 anchors each", elev=22, azim=-35)
    kit = [S[k] for k in S if k.startswith(("lower", "upper"))]
    coils = [S[k] for k in S if k.startswith("coil")]
    props = [S[k] for k in S if k.startswith("prop")]
    st(15, [part("Rack", S["upright_1"] + S["upright_2"], "")],
       [part("Pole sections and hook heads, two sets", _fuse(kit), COL["section"], (0, 500, 150)),
        part("Fork props, closed short", Compound(props), COL["prop"], (0, 500, 300)),
        part("Rope coils on the pegs", _fuse(coils), COL["rope"], (0, 500, 150))],
       "stow the kit, lock and seal", "Cable through every section, both props and both hook eyes; padlock and seal",
       elev=22, azim=-35, label_done=False)


if __name__ == "__main__":
    want = sys.argv[1:] or ["overview", "sheets", "joints", "steps"]
    for w in want:
        globals()[w]()
        print("done", w)
