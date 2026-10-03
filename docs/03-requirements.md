---
doc_id: BHK-REQ-001
title: BreakHook requirements
project: BreakHook
doc_type: Requirements
version: "0.2"
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
---

# BreakHook requirements

Fourteen requirements, each with a measurable target. At TRL 3 they are checked by calculation (BHK-CAL-001); verification by test is TRL 4 work. Ten are met on paper, R1 is at risk from pole droop, R6 and R13 are met with no margin, and R7 and R9 can only be shown by trial.

> **Safety:** BreakHook pulls a structure down with a rope. Every requirement assumes the safety rules of BHK-PRC-001: the dwelling is checked empty, the fall zone is clear and taped, nobody is within 3 m of an overhead line, and the pole is withdrawn before the haul. A requirement is never met by relaxing those rules.

Table 1. Requirements

| ID | Requirement | Target | Verification (TRL 4 or later) | Status at TRL 3 |
| --- | --- | --- | --- | --- |
| R1 | Reach of the hook | Places the hook at a height of 3 m (10 ft) with the front hand 4 m (13 ft) from the wall | Reach trial on the test frame | Met on paper with a two-person pole team; at risk: the hook droops about 0.66 m (CAL [F8]) |
| R2 | Hook and rope working pull | 3 kN (675 lbf) working, every hook head proof-loaded to 6 kN (1,350 lbf) before issue | Proof load with CalRig or at a rigging shop | Met: least factor 2.3 on yield at proof (CAL [C3]) |
| R3 | Hauling distance | Nearest hauler at least 1.5 times the structure height from the wall, and never closer than 10 m | Field layout check | Met: 10.8 m (CAL [B1]) |
| R4 | Pole electrical insulation | The handled length is foam-filled fibreglass carrying the maker's dielectric test certificate to ASTM F711 for live-line tool tube | Certificate check on receipt; no field electrical test | Met by specification; confirm the certificate when bought |
| R5 | Pole and hook mass | 8 kg (18 lb) or less | Weigh | Met: 7.82 kg (CAL [F10]) |
| R6 | Deployment time | From store to hook set in 3 min or less with four people, store within 100 m | Timed drill | Met on estimate with no margin: 3.0 min (CAL [I1]) |
| R7 | Time to bring down a test dwelling frame | Under 2 min from hook set, single-storey timber and sheet frame | Timed trial on a purpose-built test frame, never an occupied area | Estimate only: about 1.2 min (CAL [I2]) |
| R8 | Section length for narrow paths | No piece longer than 2 m (6.5 ft) | Measure | Met: 1.95 m (CAL [F12]) |
| R9 | Storage life | No loss of function after 12 months in the rack | Inspection and repeat proof load after exposure | Not verifiable at TRL 3; material choices only |
| R10 | Cost | Community kit (two sets, rack, cards, tape, gloves) against the USD 2,000 value-engineering target | Costed bill of materials | USD 1,098, USD 902 under the target |
| R11 | Beam size the hook takes | Timber up to 100 mm deep and 120 mm wide | Fit check on timber offcuts | Met: 117 mm deep, 128 to 150 mm wide (CAL [C8] to [C10]) |
| R12 | Pole release | The pole comes free of the hook head with a pull of about 50 N, so it is withdrawn before the haul | Push-off check with a spring balance | Met by design; set by trial (CAL [G1]) |
| R13 | Effort per hauler | 300 N or less per person at the working pull | Count of toggles and crew | Met at the limit: ten haulers at 300 N (CAL [A5]) |
| R14 | Insulated length | At least 3.0 m with no metal between the hook head and the hand band | Measure | Met: 3.67 m (CAL [H1]) |

## Requirements at risk

- **R1:** the fibreglass tube is flexible. If the reach trial shows the droop makes placement too slow, the options are a stiffer 50.8 mm tube (about 0.6 kg more, breaking R5) or a shorter reach. Recorded in the design decisions register as an item to confirm.
- **R6 and R13:** both sit exactly on their targets, so a slower carry or a weaker crew misses them. The community fire plan sets the store within 100 m and calls for ten haulers.
- **R5:** 0.18 kg of margin; heavier paint or a thicker tube wall would use it up.

## Assumptions

- Typical dwellings are single storey with timber or light steel frames that a crew can pull down with a hook (BHK-CAL-001, assumption 1).
- Communities already accept firebreaks as a response and can agree rules on use; the kit's governance (sealed rack, named keyholders, use log) supports those rules but does not replace them.
- The fire service supports community action in the first minutes.
- Test frames are built to represent real dwellings; occupied homes are never used for tests.
