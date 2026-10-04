---
doc_id: BHK-DDR-004
title: BreakHook prop holder stand-off accepted
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
  change: Amish's round-2 decision 5A on the prop holder's distance recorded
---

# 0004: Prop holder at 2.9 m for placement only

- **Date:** 2026-10-03
- **Status:** decided by Amish, 2026-10-03 (round 2): "i agree with all the 46 recommendations you provided. please proceed." For BreakHook this is decision 5A, the open decision in BHK-DEC-001 v0.2.

## Context

The fork prop (BHK-DDR-003) works only near the pole's mid-length. There its holder stands about 2.9 m from the wall for the 25 s of placement, 1.1 m nearer than R1's 4 m front-hand distance. The rear handler is 5.06 m away. The firebreak is opened two dwellings ahead of the fire (BHK-DDR-001, decision 10), so the dwelling being hooked is not yet burning.

## Options considered

| Option | What it means |
| --- | --- |
| A (chosen) | Accept 2.9 m for the prop holder during placement only; restate R1's distance as applying to the pole hands; the holder withdraws with the pole before the haul |
| B | Keep 4 m for everyone and move the prop back (droop 0.72 m, no better than by hand) |
| C | Keep 4 m and set the prop, then let it stand alone in the fork while its holder steps back (untested) |

## Decision

Option A. No change to parts. R1 is restated: "Places the hook at a height of 3 m (10 ft) with the pole hands (front hand) 4 m (13 ft) from the wall; the prop holder may stand 2.9 m from the wall during placement only (about 25 s) and withdraws with the pole before the haul". The reach trial at TRL 4 confirms the distance, the time at 2.9 m and the withdrawal.

*Table 1. Effects.*

| Item | Result |
| --- | --- |
| R1 | Met on paper as restated: droop about 0.27 m, rear hand 5.06 m, prop holder 2.9 m for about 25 s (BHK-CAL-001 [F19], [F24]); confirmed at TRL 4 |
| Other requirements | None changed; pole and hook 7.82 kg |
| Wording changed | Requirements v0.4 (R1), build plan (reach and drill checks), register v0.3 |
| Cost | Unchanged. Value-engineering target: USD 2,000. Estimated cost of the constructable design: USD 1,170 (USD 830 under the target). `budget_usd` unchanged |

## Safety

> **Safety:** BreakHook pulls down a structure with a rope: haulers stand at least 10 m from the wall and at least 1.5 times the structure's height away. The prop holder is the nearest person to the wall, at 2.9 m, only while the hook is set and the structure is not burning; the holder withdraws with the pole before anyone hauls, and nobody is inside the fall zone at the haul. Overhead lines stay at least 3 m clear. It is an open engineering reference, not certified equipment.
