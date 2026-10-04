---
doc_id: BHK-DEC-001
title: BreakHook design decisions register
project: BreakHook
doc_type: Design decisions register
version: "0.3"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Register opened at TRL 3; all decisions made under Amish's 2026-10-03 pre-approval
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: Fork prop at mid-length decided by Amish (6A, BHK-DDR-003); new open decision on the prop holder's distance from the wall; value engineering re-costed
- version: "0.3"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Open decision 1 (prop holder distance) decided, round 2, 5A (BHK-DDR-004); no open decisions"
---

# BreakHook design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/`; this register is the index Amish works from.

> **Safety:** Decisions that touch safety (the pole withdrawn before the haul, the 3 m overhead line rule, hauling distance, proof loading, scope limited to free-standing single-storey dwellings) took the conservative option. Each record states what evidence would relax it.

## Open decisions

None. Open decision 1 (where the prop holder stands while the hook is set) was decided by Amish on 2026-10-03: 2.9 m for placement only; see Decisions made and BHK-DDR-004.

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | The pole tube carries the maker's dielectric test certificate to ASTM F711 for live-line tool tube, and its stated test voltage | R4 is met only by this certificate | BHK-DDR-001, decision 1 |
| 2 | Actual outside diameter of the 44.5 mm tube and bore of the 50.8 x 3.2 sleeve tube; how much sanding gives a 0.2 mm slip fit | Nominal sizes give no clearance | BHK-DDR-002 |
| 3 | Stiffness of the tube from the maker's data (E along the tube); measured hook droop at 25° on the fork prop | The 0.27 m droop estimate with the prop (0.66 m by hand) uses E = 20 GPa | BHK-CAL-001 [F8], [F16] |
| 9 | Outside diameter of the 25.4 x 3.2 prop tube and bore of the 32 x 3 tube; the upper tube slides freely | 0.3 mm radial clearance on nominal sizes | BHK-DDR-003 |
| 4 | Bore of the 50.8 x 2.0 steel socket tube (46.8 mm nominal) | Sets the 1.15 mm clearance and the friction ring wrap | BHK-DDR-002 |
| 5 | Turns of rubber tape that give a 50 N release | R12 | BHK-CAL-001 [G1] |
| 6 | Shackle jaw width at least 12 mm and pin no larger than 12 mm | Fits the 10 mm plate and the 13 mm hole | bom/bom.csv line 11 |
| 7 | Breaking strengths on the rope, leader and cord labels | Factors in BHK-CAL-001 section E | bom/bom.csv lines 12, 13, 15 |
| 8 | Weighed mass of the pole and hook head | R5 has 0.18 kg of margin | BHK-CAL-001 [F10] |

## Value engineering

Value-engineering target: USD 2,000 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 1,170 (USD 830 under the target), including two fork props at USD 36 each. Main cost drivers and savings worth trying:

- Certified, foam-filled pole tube: USD 270 for six sections (25 % of the kit). A bulk order across several communities, or a local pultruder, is the main saving; uncertified tube is not an option (R4).
- Pull ropes: USD 140. Polyester double braid could give way to a cheaper three-strand polyester of the same breaking strength, with a check on hand grip and prusik hold.
- Hook head fabrication: USD 80 of welder time. Plasma-cut plates in a batch of ten would roughly halve it.
- Gloves, proof loading and the rack are each about USD 50 to 60 and are kept for safety and governance.

## Decisions made

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | Pole: foam-filled, electrical-grade fibreglass tube 44.5 x 3.2 with an ASTM F711 certificate, three 1.8 m sections | Amish Chadha, pre-approval: "I pre-approve the batch runs along with any recommendations you come up with." | [BHK-DDR-001](decisions/0001-trl2-review-decisions.md), decision 1 |
| 2026-10-03 | The pole is withdrawn before the haul; the rope alone pulls | As above | BHK-DDR-001, decision 2 |
| 2026-10-03 | Hook head cut from 10 mm plate, welded in a slotted socket; WLL 3 kN, proof 6 kN before issue | As above | BHK-DDR-001, decision 3 |
| 2026-10-03 | Wire rope leader, rated shackles, 25 m polyester pull rope | As above | BHK-DDR-001, decision 4 |
| 2026-10-03 | Crew of four to deploy and about ten haulers on toggles; no pulley in the base kit | As above | BHK-DDR-001, decision 5 |
| 2026-10-03 | Nearest hauler at 1.5 x the dwelling height and never closer than 10 m | As above | BHK-DDR-001, decision 6 |
| 2026-10-03 | Never raise the pole within 3 m of an overhead or informal line | As above | BHK-DDR-001, decision 7 |
| 2026-10-03 | Hand band and 3.0 m minimum insulated length | As above | BHK-DDR-001, decision 8 |
| 2026-10-03 | Kit governance: locked, sealed rack, two keyholders, use log, pulls only during a fire under the fire plan | As above | BHK-DDR-001, decision 9 |
| 2026-10-03 | Firebreak at least two dwellings ahead of the fire | As above | BHK-DDR-001, decision 10 |
| 2026-10-03 | Free-standing dwellings and end units only | As above | BHK-DDR-001, decision 11 |
| 2026-10-03 | Monthly check card; fresh proof load after a seal break | As above | BHK-DDR-001, decision 12 |
| 2026-10-03 | First co-design candidate to approach: City of Cape Town Fire and Rescue Service reservists (Western Cape), then Kenya Red Cross Society (not agreed) | As above | BHK-DDR-001, decision 13 |
| 2026-10-03 | Requirements updated, R11 to R14 added | As above | BHK-DDR-001, decision 14 |
| 2026-10-03 | `budget_usd` stays at USD 2,000 as the value-engineering target | Amish Chadha: "I also accept any cost overruns or variations from the assumed scope cost." | BHK-DDR-001, decision 15 |
| 2026-10-03 | Design for construction: plate hook in slotted socket, slip-fit pole with friction ring, bonded sleeves and nylon pins, rope tab with shackle and leader, S355 plate with 36 mm shank and 48 mm arm, prusik toggles, welded wall rack | Amish Chadha, pre-approval as above | [BHK-DDR-002](decisions/0002-design-for-construction.md) |
| 2026-10-03 | R1: add a light fork prop that supports the pole at mid-length, carried separately so the pole and hook head stay under 8 kg (decision 6A) | Amish Chadha: "1A 2A 3A 4A 5A 6A 7A 8A 9A 10A 11A" | [BHK-DDR-003](decisions/0003-fork-prop.md) |
| 2026-10-03 | 5A (round 2): prop holder accepted at 2.9 m from the wall during placement only (about 25 s); the holder withdraws with the pole; R1's stand-off wording restated (4 m for the pole hands); confirmed in the TRL 4 reach trial. No design change | Amish: "i agree with all the 46 recommendations you provided. please proceed." | BHK-DDR-004 |
