---
doc_id: BHK-DDR-002
title: BreakHook design for construction
project: BreakHook
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Concept made constructable (STANDARDS section 18), under Amish's 2026-10-03 pre-approval
---

# 0002: Design for construction

- **Date:** 2026-10-03
- **Status:** accepted
- **Decided by:** Amish Chadha, by pre-approval: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." Standing instruction (2026-09-30): "fix the design assumptions to match and be physically feasible".

> **Safety:** These changes keep every safety feature of the concept: the pole is withdrawn before the haul, there is no metal in the insulated length, and every part in the rope load path is rated and proof-loaded. None of them changes what the product does or its pitch.

## Context

The TRL 2 massing model showed a hook, a pole and a rope in the right proportions but left open how each part is made and how it joins its neighbours. A constructability review of `cad/src/model.py` checked every pair of parts for overlap (none over 1 mm³ after the changes), every fit (clearances printed by `python cad/src/model.py --check`) and the order of assembly.

## Changes

| Component | The concept had | The constructable design has | Why |
| --- | --- | --- | --- |
| Hook head | A forged or fabricated hook with a spike | One profile cut from 10 mm S355 plate (spike, 36 mm shank, raked arm, rope tab) | No forging; a local welder can cut it by plasma or by drilling and grinding |
| Hook to pole | Hook on the end of the pole | A 50.8 x 2.0 steel socket, slotted 10.5 x 50 across one end; the plate's 56 mm wide root sits in both slots and stands 2.6 mm proud for four 6 mm fillet welds | Face-to-face, welded joint that a welder can check by eye |
| Pole in socket | Not defined | Slip fit, 1.15 mm radial clearance, 130 mm deep, stopping on the plate; a rubber tape ring gives a 50 N release | The pole must come off before the haul (BHK-DDR-001, decision 2) |
| Pole joints | Not defined | External fibreglass sleeve 50.8 x 3.2 x 300, bored to a slip fit, bonded 150 mm to the lower section; nylon 10 mm pin 75 mm above the joint | Foam-filled tube cannot take an internal spigot; nylon keeps metal out of the insulated length |
| Rope attachment | Pull rope tied to the hook head | 13 mm hole in a rope tab in line with the arm; rated bow shackle; 1.5 m wire rope leader; second shackle to the rope's spliced eye | A knot is weaker and can be cut by sheet edges; the line through the arm keeps the shank in tension |
| Hook plate | 40 mm shank, 40 mm arm, S275 | 36 mm shank, 48 mm arm, S355 | The arm on a 100 mm beam was at 1.24 on yield at proof with S275; the narrower shank pays for the wider arm and keeps R5 |
| Hauling handles | Handles or toggles | 300 mm fibreglass toggles on 6 mm prusik cord loops, 1 m apart from 11 m | Movable on the rope, nothing to cut into the rope, and no metal |
| Pole ends and markings | Not defined | Rubber butt cap; epoxy-sealed ends and pin holes; red hand band 1.55 m from the butt | Keeps water out of the foam; tells the pole team where to hold |
| Storage rack | Rack and seal | Two welded uprights of 40 x 6 flat bar with lipped arms and a rope peg; poles 56 mm apart with sleeves at alternate ends; coated lock cable, padlock, numbered seal | Every piece rests on an arm and nothing touches its neighbour |

## Consequences

- Mass rises to 7.82 kg for the pole and hook head, inside the 8 kg limit (BHK-CAL-001 [F10]).
- The model, STEP and STL exports, the general arrangement BHK-DWG-001 Rev P1, the making sketches BHK-DWG-101 to 106 and the concept media were regenerated from the constructable model.
- `design_state: constructable` is set in `project.yaml`.
- Fits that depend on bought parts (sleeve bore, tube tolerance, shackle jaw) are listed under "To confirm when parts are bought" in BHK-DEC-001.
