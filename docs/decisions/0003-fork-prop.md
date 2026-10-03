---
doc_id: BHK-DDR-003
title: BreakHook fork prop at mid-length (R1)
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
  change: Amish's requirement decision 6A carried out
---

# 0003: Fork prop at mid-length (R1)

- **Date:** 2026-10-03
- **Status:** accepted
- **Decided by:** Amish Chadha, 2026-10-03, choosing option A on every requirement decision put to him: "1A 2A 3A 4A 5A 6A 7A 8A 9A 10A 11A". For BreakHook, 6A: add a light fork prop that supports the pole at mid-length, carried separately so the pole and hook head stay under 8 kg; recompute droop and reach.

> **Safety:** The prop is fibreglass, HDPE and nylon, with no metal, and carries a red hand band like the pole. Its holder's hand is 3.27 m of non-metal from the hook head (BHK-CAL-001 [H3]). The rule on the check card stands: never raise the pole within 3 m of any overhead line. The prop is withdrawn with the pole before anyone hauls, and its holder leaves the fall zone with the pole team.

## Context

At TRL 3 the hand-held pole drooped about 0.66 m at the hook when held out at 25° (BHK-CAL-001 [F8]), and the front hand had to lift 252 N. R1 was recorded as at risk. A stiffer 50.8 mm tube would have broken R5 (8 kg).

## Options considered

- **A (chosen):** a light fork prop under the pole at mid-length, carried separately.
- B: a stiffer, heavier pole tube (breaks R5).
- C: a shorter reach (weakens R1).

## Decision

A fork prop, one per set (BOM lines 26 to 31, making sketch BHK-DWG-107):

- Lower tube: fibreglass 32 x 3, 1,000 mm (the toggle stock), rubber foot cap, red hand band 850 to 900 mm up from the foot, one 10.5 mm hole 50 mm below its top.
- Upper tube: fibreglass 25.4 x 3.2, 1,100 mm, sliding inside the lower tube with 0.3 mm radial clearance; sixteen 10.5 mm setting holes 50 mm apart; a 12.5 x 60 mm slot across its top.
- Fork plate: 12 mm HDPE, 100 mm wide, with a 50 mm round-bottomed notch for the 44.5 mm pole and a 25.4 mm tongue in the slot, held by two nylon M8 bolts.
- A nylon 10 mm setting pin sets the fork notch from 1.19 m to 1.94 m above the ground in 50 mm steps. Closed, the prop is 1.24 m long; it weighs 1.08 kg.
- In use the prop holds the pole 2,944 mm from the butt, at mid-length, leaning about 13° with its top toward the wall. The pole lies loose in the notch; the fork never clamps it. On the rack the two props lie closed on the upper arms between the top sections.

## Consequences

- R1: the hook droops 274 mm instead of 658 mm (BHK-CAL-001 [F16]). The prop carries 100 N into the ground; the rear hand pushes down with 24 N instead of 252 N lifted and 168 N pushed by hand.
- Reach: the hook is set at 3.0 m; the rear hand is 5.06 m from the wall, and the prop holder stands about 2.9 m from it [F19, F20], 1.1 m nearer than R1's 4 m front-hand distance. Moving the prop back to keep its holder at 4 m gives 720 mm of droop [F24], so the benefit only exists near mid-length. Whether 2.9 m is acceptable is posed to Amish in the design decisions register.
- R5 unchanged at 7.82 kg; the prop is carried separately. R8 met (prop 1.24 m closed). R14 met; 3.27 m to the prop holder's hand.
- Cost: USD 72 for two props. Value-engineering target: USD 2,000. Estimated cost of the constructable design: USD 1,170 (USD 830 under the target).
- R6 estimate unchanged at 3.0 min: the prop is stored at the hole marked for the community's usual wall height and takes the place of the front-hand lift. The timed drill at TRL 4 must confirm it.
- Constructability: no overlaps over 1 mm³ between the prop's own parts at its longest and shortest settings, between the prop and the set in use, or between the props and the kit on the rack (`python cad/src/model.py --check`).
