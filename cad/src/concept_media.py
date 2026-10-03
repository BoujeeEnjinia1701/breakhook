"""BreakHook concept media (TRL 3, constructable design BHK-DDR-002), generated from cad/src/model.py.

Run from the repo root:  python cad/src/concept_media.py
Writes, with .kit/concept.py:
    media/hero.png                 the hook set over the wall plate of a test dwelling frame, pole butt on
                                   the ground, 1.75 m person for scale (grey parts are context)
    media/exploded.png             one set pulled apart, numbers match bom/bom.csv
    media/concept-blueprint.*      concept sheet BHK-DWG-010 from the straight assembly
    media/flow.png                 pull force path at the working pull (BHK-CAL-001 estimates)
    media/model.glb, viewer.html   interactive 3D model (meshed here at 1 mm, 0.35 rad, colours kept)
CONCEPT, NOT FOR FABRICATION. Figures on the sheet come from docs/04-calcs/sizing.py (BHK-CAL-001).

Model axes: pole along X, hook head at +X. For the pictures the scene is turned 180 degrees about Z so
the person and the pole butt face the kit's default camera (front right, above).
"""
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
import numpy as np  # noqa: E402
from build123d import Pos, Rot  # noqa: E402
import concept as K  # noqa: E402
from concept import Part, render_all, human_figure  # noqa: E402
from model import (PARAMS as P, derived, build_components, posed, test_frame, rope_coil, toggle,  # noqa: E402
                   rope_deployed, _fuse)

D = derived(P)
TURN = Rot(0, 0, 180)
PROJECT = "BreakHook"

COLOR = {"plate": "#D9A400", "socket": "#C99A06", "welds": "#374151", "section": "#E07B24", "sleeve": "#9A3412",
         "pin": "#F3F4F6", "ring": "#1F2937", "band": "#DC2626", "cap": "#111827", "shackle": "#64748B",
         "leader": "#475569", "rope": "#1D4ED8", "toggle": "#0F766E", "cord": "#7C3AED"}
NAME = {"plate": ("Hook plate", 1), "socket": ("Socket tube", 2), "welds": ("Socket welds", 3),
        "section": ("Pole sections (3)", 4), "sleeve": ("Joint sleeves (2)", 5), "pin": ("Joint pins (2)", 6),
        "ring": ("Friction ring", 8), "band": ("Hand band", 9), "cap": ("Butt cap", 10),
        "shackle": ("Shackles (2)", 11), "leader": ("Wire rope leader", 12), "rope": ("Pull rope", 13),
        "toggle": ("Hauling toggles", 14), "cord": ("Prusik cords", 15)}


def kind(key):
    return key.split("_")[0] if key.split("_")[0] in COLOR else {"rope": "rope"}.get(key, key)


def set_parts(transform, explode=None):
    """One set as concept Parts, each moved by transform (a function on shapes)."""
    C = build_components(P)
    C["rope_eye"] = C.pop("rope_eye")
    out = []
    for key, sh in C.items():
        k = "rope" if key == "rope_eye" else key.split("_")[0]
        name, bom = NAME[k]
        off = (explode or {}).get(key, (0, 0, 0))
        out.append(Part(name, transform(sh), COLOR[k], bom, off))
    return out


# ------------------------------------------------------------------ deployed scene (hero)
def deployed():
    parts = set_parts(lambda s: TURN * posed(s))
    run, coil = rope_deployed(P)
    parts.append(Part("Pull rope", TURN * (run + coil), COLOR["rope"], 13))
    butt_x = -5500.0
    context = [Part("Test dwelling frame (context)", TURN * test_frame(), "#C7CBD1"),
               human_figure(1750.0, x=-(butt_x + 250), y=-650.0, z=0.0)]
    return parts, context


# ------------------------------------------------------------------ straight assembly (sheet, 3D model)
def straight():
    return set_parts(lambda s: TURN * s)


# ------------------------------------------------------------------ one set pulled apart (exploded)
def exploded_parts():
    s1 = D["secs"][0]
    shift1 = D["secs"][2][0] - s1[0]           # butt section moved alongside the top section
    shift2 = D["secs"][2][0] - D["secs"][1][0]
    E = {"plate": (420, 0, 130), "welds": (300, 0, 260), "socket": (150, 0, 0),
         "section_3": (0, 0, 0), "ring": (0, 0, 110),
         "section_2": (shift2, -230, 0), "sleeve_2": (shift2 - 260, -230, 0), "pin_2": (shift2 + 80, -230, 140),
         "section_1": (shift1, -460, 0), "sleeve_1": (shift1 - 260, -460, 0), "pin_1": (shift1 + 80, -460, 140),
         "band": (shift1, -460, 110), "cap": (shift1 - 220, -460, 0),
         "shackle_1": (0, 0, -170), "leader": (0, 260, -260), "shackle_2": (-220, 260, -300),
         "rope_eye": (-420, 260, -330)}
    parts = set_parts(lambda s: TURN * s, {k: (-v[0], -v[1], v[2]) for k, v in E.items()})
    # rope coil and the ten toggles with cords, laid out beside the set
    coil = rope_coil((-1250.0, 700.0, -330.0))
    parts.append(Part("Pull rope", TURN * coil, COLOR["rope"], 13))
    togs, cords = [], []
    for k in range(P["n_toggle"]):
        x = -1700.0 + k * 150
        t = Pos(x, 1250.0, -330.0) * toggle((0, 0, 0), P)
        togs.append(t)
        cords.append(Pos(x, 1250.0, -330.0) * (Rot(90, 0, 0) * __import__("build123d").Torus(70, 3)))
    parts.append(Part("Hauling toggles", TURN * _fuse(togs), COLOR["toggle"], 14))
    parts.append(Part("Prusik cords", TURN * _fuse(cords), COLOR["cord"], 15))
    return parts


# ------------------------------------------------------------------ 3D model for the website
def write_glb(parts, path, tol=1.0, ang=0.35):
    import pygltflib as G
    import matplotlib.colors as mc
    blobs, meshes, nodes, mats, views, accs = b"", [], [], [], [], []
    for i, p in enumerate(parts):
        v, t = p.shape.tessellate(tol, ang)
        V = np.array([[q.X, q.Y, q.Z] for q in v], dtype=np.float32) / 1000.0
        V = V[:, [0, 2, 1]] * np.array([1, 1, -1], np.float32)        # Z up to glTF Y up
        F = np.array(t, dtype=np.uint32).reshape(-1)
        vb, fb = V.tobytes(), F.tobytes()
        for data, target in ((vb, 34962), (fb, 34963)):
            views.append(G.BufferView(buffer=0, byteOffset=len(blobs), byteLength=len(data), target=target))
            blobs += data + b"\x00" * ((4 - len(data) % 4) % 4)
        accs.append(G.Accessor(bufferView=len(views) - 2, componentType=5126, count=len(V), type="VEC3",
                               min=V.min(0).tolist(), max=V.max(0).tolist()))
        accs.append(G.Accessor(bufferView=len(views) - 1, componentType=5125, count=len(F), type="SCALAR"))
        r, g_, b = mc.to_rgb(p.color)
        mats.append(G.Material(name=p.name, pbrMetallicRoughness=G.PbrMetallicRoughness(
            baseColorFactor=[r, g_, b, 1.0], metallicFactor=0.1, roughnessFactor=0.7), doubleSided=True))
        meshes.append(G.Mesh(name=p.name, primitives=[G.Primitive(attributes=G.Attributes(POSITION=len(accs) - 2),
                                                                  indices=len(accs) - 1, material=i)]))
        nodes.append(G.Node(name=p.name, mesh=i))
    gl = G.GLTF2(scene=0, scenes=[G.Scene(nodes=list(range(len(nodes))))], nodes=nodes, meshes=meshes,
                 materials=mats, accessors=accs, bufferViews=views, buffers=[G.Buffer(byteLength=len(blobs))])
    gl.set_binary_blob(blobs)
    gl.save_binary(str(path))
    title = f"{PROJECT}: hook, pole and rope set"
    (Path(path).parent / "viewer.html").write_text(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer@3/dist/model-viewer.min.js"></script>
<style>body{{margin:0;font-family:system-ui,sans-serif;background:#F9FAFB}}model-viewer{{width:100vw;height:100vh}}
.tag{{position:fixed;left:12px;top:10px;font-size:12px;color:#B45309;letter-spacing:.06em}}</style></head>
<body><div class="tag">CONCEPT, NOT FOR FABRICATION</div>
<model-viewer src="model.glb" poster="hero.png" alt="{title}" camera-controls auto-rotate shadow-intensity="0.6"
  exposure="1.0" camera-orbit="-35deg 70deg auto" interaction-prompt="auto"></model-viewer></body></html>
""")


FLOW = {"title": "pull force path at the working pull, kN (BHK-CAL-001 estimates)", "unit": "kN",
        "stages": [("10 haulers at 300 N", 3.0), ("Toggles and pull rope", 3.0), ("Leader and shackles", 3.0),
                   ("Hook plate", 2.95), ("Wall plate of the frame", 2.95)],
        "losses": [(1, "Lifts the rope (vertical share, 2 %)", 0.05)]}

KEY = ["One set: steel hook head on a 5.9 m, three-section fibreglass pole",
       "Working pull 3 kN, proof 6 kN; about 10 haulers at 300 N each",
       "Haulers 10.8 m or more from the wall on a 26.5 m line (leader and rope)",
       "Pole and hook head 7.8 kg; insulated length 3.67 m below the head",
       "Pole withdrawn before the haul; never within 3 m of overhead lines",
       "Kit of two sets and a wall rack: about USD 1,098 against a USD 2,000 target"]


def main():
    sp = straight()
    fig = human_figure(1750.0, x=D["butt"] * -1 + 600, y=-500.0, z=-P["cap"][0] / 2)
    render_all(sp, project=PROJECT, title="Firebreak hook, pole and pull rope concept", dwg_no="BHK-DWG-010",
               key_figures=KEY, scale_figure=False, context=[fig], cut=False, web_model=False, flow=FLOW)
    parts, ctx = deployed()
    K._render(parts + ctx, ROOT / "media" / "hero.png", title=PROJECT,
              note="Seen from the front right and above, 24 deg elevation. Hook set over the wall plate of a "
                   "test frame, butt on the ground. Grey: test frame and a 1.75 m person for scale")
    K._render(exploded_parts(), ROOT / "media" / "exploded.png", offsets=True, labels=True, size=(10, 6.5),
              title=f"{PROJECT}: exploded view",
              note="Seen from the front right and above, 24 deg elevation; one set, pole sections laid side by "
                   "side; numbers match bom/bom.csv")
    write_glb(straight() + [Part("Pull rope coil", TURN * rope_coil((-1250.0, 700.0, -330.0)), COLOR["rope"], 13)],
              ROOT / "media" / "model.glb")
    import shutil
    for d in ("_views", "_views_fig"):
        shutil.rmtree(ROOT / "media" / d, ignore_errors=True)
    print("concept media written")


if __name__ == "__main__":
    main()
