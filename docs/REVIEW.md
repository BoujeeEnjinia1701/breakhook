# Review note: BreakHook

## Session 2026-09-30: scaffolded

### What was done

- Repository created from kit 1.6.0 at TRL 1, target TRL 2.
- `docs/01-problem.md` (BHK-PRB-001 v0.1): problem with cited evidence, users, environment, constraints, prior work, open questions.
- `docs/02-concept.md` (BHK-PRC-001 v0.1): how it works, components, patent design-arounds, shared blocks, safety.
- `docs/03-requirements.md` (BHK-REQ-001 v0.1): 10 proposed requirements.
- `README.md` with concept rationale, burning platform, where it could be used, and what sparked the idea.

### Next

- Run `/populate` to bring the repo to a strong TRL 2 with concept media.

## Session 2026-10-03: TRL 2 (/populate), run as part of /to-trl3 on kit 1.7.0

Amish Chadha, 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." On that basis every recommendation in this note is recorded as decided, not proposed.

### What was done

- Kit 1.7.0 installed (`.kit/`, `.claude/commands/`, root `CLAUDE.md` replaced by `.kit/CLAUDE.md`; `.kit/PHASE.yaml` as installed).
- Problem statement BHK-PRB-001 v0.2: co-design candidate named, the five TRL 1 questions answered, safety section.
- Requirements BHK-REQ-001 v0.2: R1 to R10 made measurable, R11 to R14 added (beam size, pole release, effort per hauler, insulated length).
- Precis BHK-PRC-001 v0.2: how it works in six steps, components, choices, numbers, safety.
- Massing model and concept media. The TRL 2 massing model was replaced in the same session by the constructable model, so every file in `media/` comes from `cad/src/model.py` (see the TRL 3 section).
- BOM with 25 priced lines (`bom/bom.csv`).

### Results at TRL 2

- The pull needed to bring down the target dwelling is 2.15 to 3.0 kN, so the working pull of 3 kN in R2 stands, but it needs about ten haulers, not four. R6's four people deploy the kit; the hauling crew comes from residents present.

### Decisions made under the pre-approval (BHK-DDR-001)

Fifteen decisions, all in `docs/decisions/0001-trl2-review-decisions.md` and the register `docs/06-design-decisions.md`: foam-filled, certified fibreglass pole; pole withdrawn before the haul; plate hook in a welded socket, WLL 3 kN, proof 6 kN; wire rope leader, rated shackles and polyester pull rope; ten haulers on toggles and no pulley; haulers at 1.5 x height and never closer than 10 m; never within 3 m of overhead lines; hand band and 3.0 m insulated length; locked, sealed rack with two keyholders and a use log; firebreak two dwellings ahead; free-standing and end units only; monthly checks; first co-design candidate (City of Cape Town Fire and Rescue Service reservists, then Kenya Red Cross Society, neither agreed); requirement updates; `budget_usd` unchanged.

### Safety concerns

- Structure collapse, occupied dwellings, electrical wiring, rope system failure, heat and crowds. Each safety-related decision took the conservative option and states what evidence would relax it.

## Session 2026-10-03: TRL 3 (/advance-trl3 and /build-plan)

### What was done

- Calculation note BHK-CAL-001 v0.1 (`docs/04-calcs/01-sizing.md`), script `docs/04-calcs/sizing.py`, results `docs/04-calcs/results.csv`.
- Parametric build123d model `cad/src/model.py` with `--check` (overlaps, fits, masses); STEP in `cad/step/` (assembly, hook head, hook plate, socket, pole section, sleeve, toggle, rack upright) and STL in `cad/stl/` (hook head, toggle).
- General arrangement BHK-DWG-001 Rev P1 (`cad/src/sheets.py`): set at 1:50 with section lengths, detail A (hook head) and detail B (pole joint) at 1:5.
- Concept media regenerated from the model (`cad/src/concept_media.py`): hero (hook over a test frame, 1.75 m figure), exploded, flow (force path), concept blueprint BHK-DWG-010, model.glb and viewer.html (meshed at 1 mm and 0.35 rad, colours kept).
- Design made constructable (decision record BHK-DDR-002); `design_state: constructable`.
- Build plan BHK-BLD-001 (`docs/05-build-plan.md`) with pictures from `cad/src/build_plan_media.py`: overview, six making sketches (BHK-DWG-101 to 106), eight joint close-ups and fourteen step pictures.
- Design decisions register BHK-DEC-001 (`docs/06-design-decisions.md`).
- Appearance model `cad/src/product_model.py` (hero, exploded and detail views; mannequin for scale) and render scenes exported to `/home/claude/renders/breakhook` for photoreal rendering on Amish's Mac.
- `project.yaml` at trl 3, trl_target 3, with trl_evidence; README leads with `media/render-hero.png` (made on the Mac), adds the links line, key figures and "Building the prototype".

### Key results (BHK-CAL-001)

- Working pull 3 kN; proof 6 kN. Least factor on yield in the hook plate at proof 2.3 (100 mm beam); rope 7.5, leader 6.0, shackle 3.3 at the working pull.
- Ten haulers at 300 N; nearest 10.8 m from the wall (R3 needs 4.5 m).
- Pole and hook head 7.82 kg (R5: 8 kg). Pole team of two: 252 N lift, 168 N hold-down.
- Insulated length 3.67 m (R14: 3.0 m).
- Deployment 3.0 min within 100 m of the store (R6: 3 min); pull 1.2 min (R7, estimate).
- Value-engineering target: USD 2,000. Estimated cost of the constructable design: USD 1,098 (USD 902 under the target).

### Requirements not met or at risk

- **R1 at risk:** the hook droops about 0.66 m when the pole is held out at 25° (E = 20 GPa assumed). Placement is possible by aiming high, but this is the first thing to measure at TRL 4. A stiffer 50.8 mm tube would break R5.
- **R6 and R13 met with no margin:** 3.0 min and 300 N per hauler exactly.
- **R4 met by specification only:** depends on the bought tube's ASTM F711 certificate.
- **R7 and R9:** cannot be shown on paper; estimate and material choices only.
- **R5:** 0.18 kg margin.

### Decisions made under the pre-approval

- BHK-DDR-001 (fifteen TRL 2 review decisions, above) and BHK-DDR-002 (design for construction). Both recorded as decided by Amish on 2026-10-03 with his quote. Open decisions: none.

### Design changes made for construction (BHK-DDR-002), 2026-10-03

- Hook head cut from one 10 mm S355 plate (no forging), welded into two 10.5 x 50 slots in a 50.8 x 2.0 steel socket.
- Pole in socket: 1.15 mm radial clearance, 130 mm deep, rubber tape friction ring for a 50 N release.
- Pole joints: external fibreglass sleeve bonded 150 mm to the lower section, nylon 10 mm pin 75 mm above the joint.
- Rope attachment: 13 mm hole in a rope tab in line with the arm, rated bow shackle, 1.5 m wire rope leader, second shackle to the rope's spliced eye.
- Plate re-proportioned: 36 mm shank and 48 mm arm, S355 instead of S275 (the arm was at 1.24 on yield at proof).
- Toggles on prusik cord loops; rubber butt cap; sealed ends; red hand band.
- Rack: two welded 40 x 6 flat-bar uprights with lipped arms (poles 56 apart, sleeves at alternate ends) and a 380 mm rope peg so the coil clears the arms.

### Build plan findings

- No overlaps over 1 mm³ between any parts of a set, or of the kit on its rack, after the changes.
- Nominal tube sizes give zero clearance for the sleeve; the bore must be sanded. Listed under "To confirm when parts are bought" with seven other items.
- The pole cannot carry the pull and should not: the slip fit makes that physically impossible, which also keeps the pole team out of the load path.

### Appearance model and render scenes

- `cad/src/product_model.py`: TITLE "BreakHook: firebreak hook, pole and pull rope set"; views hero (set over the test frame with the mannequin), exploded (one set, sections side by side, coil and toggles) and detail (hook head on the wall plate, cut to a window). Every dimension comes from `model.py`. Differences from `model.py`: none in dimensions; the scene is turned 180° about Z for the camera, the detail view clips the parts to a window, and the pull rope's run on the ground is drawn as two straight lengths.
- Photoreal renders and the cards are made on Amish's Mac; `media/render-hero.png`, `media/card.png` and `media/social-preview.png` do not exist yet, so `render.py --check` warns about them and the image check.

### Safety concerns

- Falling structure, occupied dwelling, overhead and informal wiring, rope system failure under load, heat and smoke, crowds, and misuse in disputes. Each is answered by a conservative decision (BHK-DDR-001) and by the safety stops S1 to S5 in the build plan. The insulated pole is a second line of defence only.
- The proof load (6 kN) is the first time the rope system is loaded; safety stop S2 keeps everyone out of line with it.

### Recommended next step

- Photoreal renders and cards on Amish's Mac from `/home/claude/renders/breakhook`.
- TRL 4 (recommendation only, not started): build one set and the rack, proof-load it, then a reach trial (R1 droop) and a timed drill on a purpose-built test frame with the first co-design candidate.

## 2026-10-03: photoreal renders

Rendered with Blender Cycles on Amish's Mac from `cad/src/product_model.py`; captioned with `.kit/photo_caption.py`; `media/card.png` and `media/social-preview.png` made with `.kit/cards.py`. Views: hero, exploded, detail. image_qc passes and `render.py --check` has no FAIL.

## 2026-10-03: Amish's requirement decisions carried out

Amish chose option A on every requirement decision put to him: "1A 2A 3A 4A 5A 6A 7A 8A 9A 10A 11A". For BreakHook this is decision 6A (R1): add a light fork prop that supports the pole at mid-length, carried separately so the pole and hook head stay under 8 kg; recompute droop and reach. Not committed or pushed (batch run).

### Changes

- Fork prop added to `cad/src/model.py` (BHK-DDR-003): fibreglass lower tube 32 x 3 x 1,000 with foot cap and red hand band; fibreglass upper tube 25.4 x 3.2 x 1,100 sliding inside it, sixteen setting holes 50 apart; 12 mm HDPE fork plate with a 50 mm notch, held in a slot by two nylon M8 bolts; nylon setting pin. Fork notch 1.19 to 1.94 m above the ground; 1.24 m closed; 1.08 kg; no metal. New model checks: the prop's own parts at its longest and shortest settings, the fits (0.30 mm tube clearance, 0.25 mm each side of the fork tongue), the prop in use under the pole (fork 0.33 mm below the pole, foot on the ground, no overlaps with the set) and both props stowed on the rack's upper arms (no overlaps). STEP (`fork-prop.step`, `fork-prop-plate.step`) and STL (`fork-prop-plate.stl`) added; all STEP and STL regenerated.
- `docs/04-calcs/sizing.py` and `01-sizing.md` v0.2: the pole as a beam on the rear hand and the prop [F13 to F22], an alternative prop position [F23, F24] and the insulated path to the prop holder [H3]; `results.csv` re-run.
- `bom/bom.csv` lines 26 to 31 (two props, USD 72, each line with its price basis).
- `docs/03-requirements.md` v0.3 (targets unchanged, Amish quoted, status of R1, R5, R8, R10, R14 updated); `docs/02-concept.md` v0.3; README key figures.
- `docs/05-build-plan.md` v0.2: new row in Table 1, section 3.8 (fork prop) with Figures 14 to 16, Step 13 (assemble the prop), rack and stowing steps now 14 and 15, reach and prop first checks, S5 includes the prop.
- Pictures: general arrangement BHK-DWG-001 Rev P2 (detail C, fork prop, and a note line); new making sketch BHK-DWG-107; overview, joints 9 and 10, steps 13 to 15 regenerated; concept media (hero with the prop in place, exploded with the prop, blueprint key figures, `model.glb`).
- Register `docs/06-design-decisions.md` v0.2 and decision record `docs/decisions/0003-fork-prop.md` (BHK-DDR-003).
- Appearance model `cad/src/product_model.py`: the prop under the pole in the hero view and closed beside the toggles in the exploded view; scenes re-exported to `/home/claude/renders/breakhook`.

### New results

- R1: hook set at 3.0 m with the pole on the prop: droop 274 mm (was 658 mm by hand); the prop carries 100 N and the rear hand pushes down 24 N (was 252 N lifted, 168 N pushed). Rear hand 5.06 m from the wall; the prop holder stands about 2.9 m from it, 1.1 m nearer than the 4 m front-hand distance. Placement met on paper; the prop holder's distance is a new open decision.
- R5: 7.82 kg, unchanged (0.18 kg margin); the 1.08 kg prop is carried separately.
- R8: met; the prop closes to 1.24 m.
- R14: met; 3.67 m on the pole and 3.27 m of non-metal from the socket mouth to the prop holder's hand band.
- R10: Value-engineering target: USD 2,000. Estimated cost of the constructable design: USD 1,170 (USD 830 under the target). `budget_usd` unchanged.
- R6 estimate unchanged at 3.0 min (the prop is stored at the hole marked for the usual wall height and replaces the front-hand lift); still no margin.
- Prop buckling: 822 N on the upper tube alone, 8 times the prop load.

### For Amish

- New open decision 1 in the register: the prop holder stands about 2.9 m from the wall for the 25 s of placement. Options: (a) accept it for placement only, with R1's 4 m applying to the pole hands and the prop holder withdrawing with the pole; (b) move the prop back to keep 4 m (droop 0.72 m, worse than by hand); (c) let the prop stand alone in the fork while its holder steps back (untested). Recommendation: (a), checked in the TRL 4 reach trial and drill.
- The photoreal renders (`media/render-*.png`), card and social preview do not show the prop yet; re-render on the Mac from the re-exported scenes.

### Safety

- The prop is all fibreglass, HDPE and nylon. The 3 m overhead line rule, withdrawing the pole (and now the prop) before the haul, and leaving the fall zone are unchanged.

## 2026-10-03: photoreal renders redone after Amish's requirement decisions

Rendered with Blender Cycles on Amish's Mac from `cad/src/product_model.py`; captioned with `.kit/photo_caption.py`; `media/card.png` and `media/social-preview.png` made with `.kit/cards.py`. Views: hero, exploded, detail. image_qc passes and `render.py --check` has no FAIL.

## 2026-10-03: Amish's round-2 requirement decisions carried out

Amish, 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed." For BreakHook this is decision 5A on the prop holder's distance, recorded in `docs/decisions/0004-prop-holder-distance.md` (BHK-DDR-004) and in the register `docs/06-design-decisions.md` (BHK-DEC-001 v0.3). A records and wording change only: no geometry, bill of materials, drawing or picture changed.

| Change | Files | New result |
| --- | --- | --- |
| Prop holder accepted at 2.9 m for placement only (about 25 s); holder withdraws with the pole | BHK-DDR-004, register v0.3 | Droop about 0.27 m, rear hand 5.06 m, holder 2.9 m, as before |
| R1 stand-off wording restated: 4 m applies to the pole hands | `docs/03-requirements.md` v0.4 | **R1 met on paper as restated**; the reach trial at TRL 4 confirms the distance, the time at 2.9 m and the withdrawal |
| Reach and drill checks worded for the stand-off | `docs/05-build-plan.md` (checks table) | Distances measured for each person |
| Open decision 1 closed | register v0.3 | Open decisions: none |
| Cost | unchanged | Value-engineering target: USD 2,000. Estimated cost of the constructable design: USD 1,170 (USD 830 under the target). `budget_usd` unchanged |

Mass unchanged (pole and hook 7.82 kg; prop 1.08 kg carried separately). Pictures changed: none; the appearance model is unchanged and no views were re-exported.

### Decisions proposed, awaiting Amish

None.

### Cross-repo actions

None.

### Safety

The prop holder is the person nearest the wall, at 2.9 m, and only while the hook is set on a dwelling that is not yet burning. The holder withdraws with the pole before the haul. The haulers' 10 m and 1.5 times height rule and the 3 m overhead line rule are unchanged.

### Recommended next step

TRL 4 (the reach trial on the test frame with the distances and the 25 s timed, then the drill) needs a new instruction from Amish.

