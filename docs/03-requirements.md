---
doc_id: BHK-REQ-001
title: BreakHook requirements
project: BreakHook
doc_type: Requirements
version: "0.5"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 2 and TRL 3; targets confirmed under Amish's 2026-10-03 pre-approval (BHK-DDR-001); R11 to R14 added; status from BHK-CAL-001
- version: "0.3"
  date: '2026-10-03'
  author: Amish Chadha
  change: 'Fork prop at mid-length added under Amish''s decision 6A (BHK-DDR-003); status of R1, R5, R8, R10 and R14 updated from BHK-CAL-001 v0.2; targets unchanged'
- version: "0.5"
  date: '2026-10-03'
  author: Amish Chadha
  change: "R1 stand-off wording restated after Amish's round-2 decision 5A (BHK-DDR-004): prop holder at 2.9 m during placement only; confirmed in the TRL 4 reach trial"
---

# BreakHook requirements

Fourteen requirements, each with a measurable target. At TRL 3 they are checked by calculation (BHK-CAL-001); verification by test is TRL 4 work. Ten are met on paper; R1's hook placement is met with the fork prop, and the prop holder's 2.9 m placement-only stand-off is accepted by Amish (the TRL 4 reach trial confirms it); R6 and R13 are met with no margin, and R7 and R9 can only be shown by trial.

On 2026-10-03 Amish chose option A on every requirement decision put to him ("1A 2A 3A 4A 5A 6A 7A 8A 9A 10A 11A"). For BreakHook, decision 6A adds a light fork prop that supports the pole at mid-length, carried separately so the pole and hook head stay under 8 kg (BHK-DDR-003). No target changes.

> **Safety:** BreakHook pulls a structure down with a rope. Every requirement assumes the safety rules of BHK-PRC-001: the dwelling is checked empty, the fall zone is clear and taped, nobody is within 3 m of an overhead line, and the pole is withdrawn before the haul. A requirement is never met by relaxing those rules.

Table 1. Requirements

| ID | Requirement | Target | Verification (TRL 4 or later) | Status at TRL 3 |
| --- | --- | --- | --- | --- |
| R1 | Reach of the hook | Places the hook at a height of 3 m (10 ft) with the pole hands (front hand) 4 m (13 ft) from the wall; the prop holder may stand 2.9 m from the wall during placement only (about 25 s) and withdraws with the pole before the haul | Reach trial on the test frame, with the prop holder's distance from the wall and the time at 2.9 m measured | Hook placement met on paper with the fork prop at mid-length: droop about 0.27 m (0.66 m by hand), rear hand 5.06 m from the wall (CAL [F13] to [F20]); the prop holder stands about 2.9 m from the wall for the placement only (about 25 s), accepted by Amish (5A, round 2), and withdraws with the pole; the TRL 4 reach trial confirms it |
| R2 | Hook and rope working pull | 3 kN (675 lbf) working, every hook head proof-loaded to 6 kN (1,350 lbf) before issue | Proof load with CalRig or at a rigging shop | Met: least factor 2.3 on yield at proof (CAL [C3]) |
| R3 | Hauling distance | Nearest hauler at least 1.5 times the structure height from the wall, and never closer than 10 m | Field layout check | Met: 10.8 m (CAL [B1]) |
| R4 | Pole electrical insulation | The handled length is foam-filled fibreglass carrying the maker's dielectric test certificate to ASTM F711 for live-line tool tube | Certificate check on receipt; no field electrical test | Met by specification; confirm the certificate when bought |
| R5 | Pole and hook mass | 8 kg (18 lb) or less | Weigh | Met: 7.82 kg (CAL [F10]); the 1.08 kg fork prop is carried separately (CAL [F22]) |
| R6 | Deployment time | From store to hook set in 3 min or less with four people, store within 100 m | Timed drill | Met on estimate with no margin: 3.0 min (CAL [I1]) |
| R7 | Time to bring down a test dwelling frame | Under 2 min from hook set, single-storey timber and sheet frame | Timed trial on a purpose-built test frame, never an occupied area | Estimate only: about 1.2 min (CAL [I2]) |
| R8 | Section length for narrow paths | No piece longer than 2 m (6.5 ft) | Measure | Met: 1.95 m (CAL [F12]); fork prop 1.24 m closed |
| R9 | Storage life | No loss of function after 12 months in the rack | Inspection and repeat proof load after exposure | Not verifiable at TRL 3; material choices only |
| R10 | Cost | Community kit (two sets, rack, cards, tape, gloves) against the USD 2,000 value-engineering target | Costed bill of materials | USD 1,170 with two fork props, USD 830 under the target |
| R11 | Beam size the hook takes | Timber up to 100 mm deep and 120 mm wide | Fit check on timber offcuts | Met: 117 mm deep, 128 to 150 mm wide (CAL [C8] to [C10]) |
| R12 | Pole release | The pole comes free of the hook head with a pull of about 50 N, so it is withdrawn before the haul | Push-off check with a spring balance | Met by design; set by trial (CAL [G1]) |
| R13 | Effort per hauler | 300 N or less per person at the working pull | Count of toggles and crew | Met at the limit: ten haulers at 300 N (CAL [A5]) |
| R14 | Insulated length | At least 3.0 m with no metal between the hook head and the hand band | Measure | Met: 3.67 m (CAL [H1]); 3.27 m from the socket mouth to the prop holder's hand band (CAL [H3]) |

## Requirements at risk

- **R1:** the fibreglass tube is flexible. The fork prop at mid-length cuts the droop from about 0.66 m to 0.27 m and takes the lift off the pole team, but its holder stands about 2.9 m from the wall while the hook is set, for about 25 s. Amish accepted that for placement only (round 2, 5A: "i agree with all the 46 recommendations you provided. please proceed.") and R1 is restated accordingly: the 4 m applies to the pole hands, and the holder withdraws with the pole before the haul. The reach trial at TRL 4 confirms the distance and the time; the measured droop is an item to confirm.
- **R6 and R13:** both sit exactly on their targets, so a slower carry or a weaker crew misses them. The community fire plan sets the store within 100 m and calls for ten haulers.
- **R5:** 0.18 kg of margin; heavier paint or a thicker tube wall would use it up.

## Assumptions

- Typical dwellings are single storey with timber or light steel frames that a crew can pull down with a hook (BHK-CAL-001, assumption 1).
- Communities already accept firebreaks as a response and can agree rules on use; the kit's governance (sealed rack, named keyholders, use log) supports those rules but does not replace them.
- The fire service supports community action in the first minutes.
- Test frames are built to represent real dwellings; occupied homes are never used for tests.
