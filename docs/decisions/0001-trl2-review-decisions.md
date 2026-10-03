---
doc_id: BHK-DDR-001
title: BreakHook TRL 2 review decisions
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
  change: TRL 2 review decisions, made under Amish's 2026-10-03 pre-approval
---

# 0001: TRL 2 review decisions

- **Date:** 2026-10-03
- **Status:** accepted
- **Decided by:** Amish Chadha, by pre-approval: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." Each recommendation below was made in the TRL 2 review of this repo and is recorded as decided under that pre-approval.

> **Safety:** BreakHook pulls a structure down with a rope near a fire. Every decision that touches safety below takes the conservative option and states what evidence would relax it.

## Context

The TRL 1 scaffold (BHK-PRC-001 v0.1) left the pole material, the hook construction, the rope system, the hauling crew and five open questions in BHK-PRB-001 undecided. TRL 3 needs each settled so the design can be calculated, modelled and planned.

## Decisions

| # | Decision | Options considered | Why | Safety note and what would relax it |
| --- | --- | --- | --- | --- |
| 1 | Pole: foam-filled, electrical-grade pultruded fibreglass round tube 44.5 x 3.2, three 1.8 m sections, with the maker's ASTM F711 dielectric certificate | Hollow fibreglass tube; bamboo; aluminium | Light, stiff enough, and the only option whose insulation can be certified | Conservative: foam fill and certificate even though the pole is never meant to touch a line. Relax only with a field study showing no wiring hazard, which is unlikely |
| 2 | Pole is withdrawn before the haul; the rope alone pulls | Pole stays on and is pulled with the rope; pole used as a lever | Keeps the pole team out of the fall zone and keeps the pole out of the load path | Conservative. No evidence would relax it |
| 3 | Hook head: plate cut from 10 mm steel, welded into a slotted steel socket; WLL 3 kN; proof 6 kN before issue | Forged hook; bought pike-pole head | Makeable by any local welder; the pike-pole heads on sale are not rated for a rope pull | Proof load before issue and after any seal break; relax to sample proof loading only after a batch of 20 heads all pass |
| 4 | Rope system: 1.5 m galvanised wire rope leader, rated bow shackles, 25 m of 12 mm polyester double braid | Rope tied straight to the hook; chain leader | Leader keeps heat and sheet edges off the rope; chain is too heavy at the pole tip | Factors 6 or more on the rope and leader; relax to a lighter rope only with test data |
| 5 | Crew: four to deploy (pole team of two, caller, fall zone marker) and about ten haulers on toggles; requirement R13 added (300 N each) | Four haulers; a pulley or capstan | The pull needs about 3 kN (BHK-CAL-001); a pulley needs a strong anchor that settlements rarely have | Pulley left out; it could be added as an option where a tested anchor (a stake system) exists |
| 6 | Hauling distance: nearest hauler at 1.5 x the dwelling height and never closer than 10 m (R3 tightened) | 1.5 x height only | Keeps haulers well outside the fall zone and further from heat | Conservative; relax only with fall-zone measurements from TRL 4 trials |
| 7 | Overhead lines: never raise the pole within 3 m of any overhead or informal line, whatever the pole's insulation | Rely on the insulated pole | Informal wiring is unpredictable; the hook and wet rope conduct | Conservative; no evidence would relax it |
| 8 | Hand band 1.55 m from the butt; hands stay below it; insulated length 3.0 m or more (R14 added) | No marking | Gives the insulated length a meaning in use | None |
| 9 | Misuse safeguard: settlement committee holds the kit in a locked, sealed rack with two named keyholders and a use log; pulls only during a fire under the community fire plan | Open storage; fire service storage only | Answers the dispute and eviction concern while keeping the kit near the homes | Conservative |
| 10 | Firebreak rule for training: at least two dwellings ahead of the burning one, and only if the pull can finish first; otherwise evacuate | One dwelling ahead | Spread can take under a minute | Relax only with evidence from fire-spread studies in the partner's settlements |
| 11 | Scope: free-standing dwellings and end units only; no shared-wall rows, multi-storey or masonry | Allow shared walls | A shared wall can bring down the neighbour or fall unpredictably | Conservative; relax only after trials on a shared-wall test frame |
| 12 | Kit storage and checks: monthly check card; a broken seal means a full check and a fresh proof load | Annual check | Outdoor storage and community use | None |
| 13 | Co-design partner, first candidate to approach (not agreed): City of Cape Town Fire and Rescue Service volunteer reservists with a Western Cape settlement committee; second: Kenya Red Cross Society, Nairobi | Others in BHK-PRB-001 | Strongest evidence base (Stellenbosch and Imizamo Yethu studies) and an existing reservist system | Not a safety decision |
| 14 | Requirements: targets of R1 to R10 kept, R6 measured to hook set with the pole withdrawn and the store within 100 m; R11 to R14 added | Leave as TRL 1 | Makes each target measurable | None |
| 15 | Budget: `budget_usd` stays at USD 2,000 as a value-engineering target | Change it | Amish's pre-approval accepts variations; the estimate is under the target anyway | Not a safety decision |

## Consequences

- BHK-REQ-001 v0.2, BHK-PRC-001 v0.2 and BHK-PRB-001 v0.2 carry these decisions.
- The design for construction (BHK-DDR-002) builds on decisions 1 to 4.
- The check card, training material and fall zone kit are part of the community kit (BOM 19 to 24).
