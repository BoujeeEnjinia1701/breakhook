"""BreakHook general arrangement sheet BHK-DWG-001, Rev P1 (TRL 3, constructable design, BHK-DDR-002).

Run from the repo root:  python cad/src/sheets.py
Writes cad/drawings/BHK-DWG-001.svg, .pdf and .png from cad/src/model.py with .kit/drawing.py:
the assembled set in three views at 1:50 with its main lengths, detail A (hook head) and detail B
(pole joint) at 1:5, and the main dimensions. The concept blueprint in media/ is BHK-DWG-010; the
making sketches BHK-DWG-101 onward come from cad/src/build_plan_media.py.
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
from build123d import Compound  # noqa: E402
from drawing import Sheet, project_views, _viewbox, _t, M, TB_Y, INK, MUTED  # noqa: E402
from model import PARAMS as P, derived, build_components, _tube_x, masses  # noqa: E402

DATE = "2026-10-03"


def cells(sheet, views, names=("front", "top", "right")):
    """Repeat Sheet.add_ortho's layout arithmetic to find where each view lands (x, y, w, h)."""
    ax, ay, aw, ah = M + 10, M + 16, 245, TB_Y - M - 20
    gap, lab, dl = 14, 12, 11
    vb = {n: _viewbox(Path(views[n]).read_text())[2:] for n in names}
    fw, fh = vb["front"]
    tw, th = vb["top"]
    rw, rh = vb["right"]
    k = sheet.scale
    ax += (aw - (k * (max(fw, tw) + rw) + gap + dl)) / 2 + dl
    ay += (ah - (k * (th + max(fh, rh)) + gap + 2 * lab + dl)) / 2 + dl
    colw = k * max(fw, tw)
    front_y = ay + k * th + lab + gap
    row_h = k * max(fh, rh)
    return {"top": (ax, ay, colw, k * th), "front": (ax, front_y, colw, row_h)}, vb


def dim_h(x1, x2, y, text, size=2.2):
    a = 1.2
    return [f'<line x1="{x1:.2f}" y1="{y:.2f}" x2="{x2:.2f}" y2="{y:.2f}" stroke="{INK}" stroke-width="0.18"/>',
            f'<path d="M{x1:.2f} {y:.2f} l{a} -0.45 l0 0.9 Z" fill="{INK}"/>',
            f'<path d="M{x2:.2f} {y:.2f} l{-a} -0.45 l0 0.9 Z" fill="{INK}"/>',
            _t((x1 + x2) / 2, y - 1.0, text, size, 400, INK, "middle", mono=True)]


def ext(x, y1, y2):
    return f'<line x1="{x:.2f}" y1="{y1:.2f}" x2="{x:.2f}" y2="{y2:.2f}" stroke="{MUTED}" stroke-width="0.13"/>'


def leader(x1, y1, x2, y2, text, anchor="start"):
    return [f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{MUTED}" stroke-width="0.15"/>',
            f'<circle cx="{x1:.2f}" cy="{y1:.2f}" r="0.45" fill="{INK}"/>',
            _t(x2 + (1 if anchor == "start" else -1), y2 + 0.8, text, 2.1, 400, INK, anchor)]


def main():
    D = derived(P)
    C = build_components(P)
    work = ROOT / "cad" / "drawings" / "_views"
    keys = ["plate", "socket", "welds", "section_1", "section_2", "section_3", "sleeve_1", "sleeve_2",
            "pin_1", "pin_2", "ring", "band", "cap", "shackle_1", "leader"]
    asm = Compound([C[k] for k in keys])
    views = project_views(asm, work / "ga")
    bb = asm.bounding_box()
    s = Sheet(project="BreakHook", title="Firebreak hook and pole set: general arrangement", dwg_no="BHK-DWG-001",
              rev="P1", author="Amish Chadha", date=DATE, scale=1 / 50, theme="technical",
              concept="PRELIMINARY, NOT FOR FABRICATION",
              material="Hook head S355 plate in 50.8 x 2.0 steel tube, primed and painted; pole foam-filled fibreglass "
                       "tube 44.5 x 3.2; see bom/bom.csv",
              revisions=[("P1", "Preliminary GA of the constructable design (TRL 3; BHK-DDR-002)", DATE, "AC")])
    s.add_ortho(views)
    k = s.scale
    c, vb = cells(s, views)
    L = []
    # front view (looking along +Y): model X to the right, Z up
    x, y, w, h = c["front"]
    fw, fh = vb["front"]
    x0 = x + (w - k * fw) / 2
    y0 = y + (h - k * fh) / 2
    X = lambda mx: x0 + (mx - bb.min.X) * k        # noqa: E731
    Z = lambda mz: y0 + (bb.max.Z - mz) * k        # noqa: E731
    yd = y + h + 17                                # below the view label and its scale line
    xs = [D["overall"][0]] + [a for a, _ in D["secs"][1:]] + [D["secs"][2][1], P["spike"][0]]
    for xx in xs:
        L.append(ext(X(xx), yd - 3, yd + 1))
    for (a, b), lab_ in zip(zip(xs[:-1], xs[1:]), ["1800 + CAP", "1800", "1800", "HEAD"]):
        L += dim_h(X(a), X(b), yd, lab_, 1.9)
    yd2 = yd + 7
    L += dim_h(X(D["overall"][0]), X(P["spike"][0]), yd2, f"{D['length']:.0f} OVERALL")
    L += [ext(X(D["overall"][0]), yd + 1, yd2 + 1), ext(X(P["spike"][0]), yd + 1, yd2 + 1)]
    L += leader(X(D["band_x"][0]), Z(0), X(D["band_x"][0]) - 4, Z(0) - 12, "HAND BAND (9), HOLD BELOW", "end")
    for j, xj in enumerate(D["joints"]):
        L += leader(X(xj), Z(0), X(xj) + 3, Z(0) - 12, "JOINT, DETAIL B (5, 6)" if j == 1 else "JOINT (5, 6)")
    L += leader(X(-90), Z(0), X(-90) - 6, Z(0) - 20, "HOOK HEAD, DETAIL A", "end")
    L.append(_t(X(D["overall"][0]), Z(bb.max.Z) - 4, "BUTT", 2.0, 600, MUTED, "start"))
    L.append(_t(X(P["spike"][0]), Z(bb.max.Z) - 4, "HOOK", 2.0, 600, MUTED, "end"))
    s._layers += L

    # detail A: hook head with the pole tip, shackle and the start of the leader, 1:5
    head = Compound([build_components(P)[k] for k in ("plate", "socket", "welds", "shackle_1", "ring")]
                    + [_tube_x(P["pole"][0], P["pole"][0] - 2 * P["pole"][1], -300, D["tip"])])
    va = project_views(head, work / "a")
    s.add_svg(va["front"], 276, 34, 140, 52, scale=0.2, label="Detail A: hook head",
              sublabel="Scale 1:5; looking at the front (along +Y); pole tip shown cut short")
    # detail B: pole joint, 1:5
    j = D["joints"][1]
    CB = build_components(P)
    from build123d import Box, Pos
    win = Pos(j, 0, 0) * Box(520, 200, 200)
    joint = Compound([CB["sleeve_2"], CB["pin_2"], CB["section_2"] & win, CB["section_3"] & win])
    vbj = project_views(joint, work / "b")
    s.add_svg(vbj["front"], 276, 102, 140, 24, scale=0.2, label="Detail B: pole joint",
              sublabel="Scale 1:5; looking at the front (along +Y); sleeve bonded to the lower section")
    m = masses(P)
    mset = sum(v for kk, v in m.items() if kk not in ("shackle 1", "leader"))
    s.add_notes("Main dimensions and interfaces (mm)", [
        f"Overall {D['length']:.0f}; three sections {P['sec_len']:.0f}, 44.5 x 3.2 fibreglass, foam filled",
        f"Joints: sleeve 50.8 x 3.2 x {P['sleeve'][2]:.0f}, bonded 150; nylon pin 10, {P['pin'][2]:.0f} above joint",
        f"Socket 50.8 x 2.0 x {P['socket'][2]:.0f}; pole goes in {D['insertion']:.0f}, 1.15 radial clearance",
        "Plate 10 S355 in two 10.5 x 50 slots; four 6 fillet welds outside",
        f"Arm reaches {-P['shank'][1] - P['arm_bot'][2]:.0f} below the shank; throat 150 at the shank",
        "Shackle hole 13, in line with the arm; 3/8 in bow shackle, WLL 1 t",
        "Leader 6 wire rope, 1500 eye to eye; pull rope 12 polyester, 25 m",
        f"Hand band {P['band'][0]:.0f} from the butt; insulated length {D['insulated']:.0f}",
        f"Pole and hook head {mset:.1f} kg; working pull 3 kN, proof 6 kN",
        "Third angle; pole along X, hook at +X; (n) = BOM line",
    ], x=276, y=145, width=146)
    out = s.save(ROOT / "cad" / "drawings" / "BHK-DWG-001")
    shutil.rmtree(work, ignore_errors=True)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
