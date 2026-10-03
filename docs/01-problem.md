---
doc_id: BHK-PRB-001
title: BreakHook problem statement
project: BreakHook
doc_type: Problem statement
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
  change: TRL 2 and TRL 3; co-design candidate named; open questions settled under Amish's 2026-10-03 pre-approval (BHK-DDR-001); safety section added
---

# BreakHook problem statement

In the first minutes of a settlement fire, only residents are there. They know that clearing a gap can stop the spread, but they have no tool that lets them do it from a safe distance.

## The problem

Fire can spread between informal dwellings in under a minute ([Stellenbosch University, 2023](https://www0.sun.ac.za/researchforimpact/2023/10/10/su-fire-engineers-explore-risks-for-humans-and-dwellings/)). Fire engines often cannot get in: response times average 68 minutes in informal settlements in the Dhaka and Cape Town study, and pathways can be 60 to 90 cm wide ([Royal Academy of Engineering](https://engineeringx.raeng.org.uk/media/03cd1j4l/engx-a-comparative-study-of-fire-risk-emergence-in-informal-settlements-in-dhaka-and-cape-town-short.pdf)). By then a fire can take hundreds or thousands of homes, as at Imizamo Yethu ([Imizamo Yethu fire spread analysis](https://www.sciencedirect.com/science/article/abs/pii/S2212420918307623)).

Current responses focus on prevention and access: fire safety education, extinguishers and re-blocking into rows with 3 m gaps, which reduces settlement capacity by at least 20 % ([The New Humanitarian, 2013](https://www.thenewhumanitarian.org/analysis/2013/01/23/south-africa-searches-solutions-shack-fires)). Community responders, trained by groups such as the Kenya Red Cross, use buckets and basins and pull structures down by hand ([Ngau and Boit, 2020](https://journals.sagepub.com/doi/10.1177/0956247820924939)). The historical fire hook was built for exactly this job ([London Fire Brigade Museum](https://www.london-fire.gov.uk/museum/london-fire-brigade-history-and-stories/fires-and-incidents-that-changed-history/the-great-fire-of-london/)), but no open, tested version exists for these communities.

## Users and context

| User | Need | Context |
| --- | --- | --- |
| Community fire responders | Pull a structure down from a safe distance to open a firebreak | First minutes of a fire, crowds, smoke, narrow paths |
| Settlement committees and ward leaders | A tool they can store, assign and govern, with a clear rule on when it may be used | Community fire plans and training days |
| Municipal fire services and reservist programmes | Equipment to issue to trained community reservists | City fire and disaster management |
| NGOs and Red Cross societies | A low-cost kit item with training material | Community fire response training |

## Operating environment

- Dense settlements of closely spaced, mostly single-storey dwellings (assumed; to be confirmed with the partner).
- Paths about 0.6 to 0.9 m (2 to 3 ft) wide in places ([Royal Academy of Engineering](https://engineeringx.raeng.org.uk/media/03cd1j4l/engx-a-comparative-study-of-fire-risk-emergence-in-informal-settlements-in-dhaka-and-cape-town-short.pdf)).
- Smoke, radiant heat, crowds and panic during use.
- Overhead and informal electrical wiring may be present.
- Stored outdoors or in a shared shed for long periods between uses.

## Constraints

- Prototype parts budget: USD 2,000 or less for a community kit.
- Pole must be non-conductive along the handled length.
- Light enough to carry and for a team of two to lift into place: 8 kg (18 lb) or less for the pole and hook head.
- Short enough in sections to move along narrow paths.
- Buildable by a local welder from stock steel plus commercial fibreglass tube and rope.
- Open design: hardware under CERN-OHL-S-2.0, training material under a matching open licence.

## Out of scope

- Fire suppression equipment, alarms and detectors.
- Demolition outside an active fire emergency.
- Multi-storey or masonry buildings.
- Rules on who may authorise pulling down a home; that is for each community and its local authority.

## Prior work

| Prior work | What it does | Gap for these users | Source |
| --- | --- | --- | --- |
| Historical fire hooks | Long hooks used to pull down buildings in the path of a fire, as in London in 1666 | No modern, documented, non-conductive version sized for informal dwellings | [link](https://www.london-fire.gov.uk/museum/london-fire-brigade-history-and-stories/fires-and-incidents-that-changed-history/the-great-fire-of-london/) |
| Community fire response in Nairobi | Residents trained by the Kenya Red Cross use buckets and tear down structures to make firebreaks | Done by hand, close to the fire, with no purpose-made tool | [link](https://journals.sagepub.com/doi/10.1177/0956247820924939) |
| Re-blocking (Cape Town) | Rebuilding settlements in rows with 3 m gaps for access and fire separation | Slow, costly, reduces capacity; no help once a fire has started | [link](https://www.thenewhumanitarian.org/analysis/2013/01/23/south-africa-searches-solutions-shack-fires) |

## Co-design

A municipal fire service reservist programme or a Red Cross or Red Crescent society already training community fire responders in informal settlements, working with a settlement committee that can set rules for when the tool is used.

First candidate to approach (not agreed): the City of Cape Town Fire and Rescue Service and its volunteer reservists, with a settlement committee in the Western Cape. Second candidate: the Kenya Red Cross Society's community fire response work in Nairobi (BHK-DDR-001).

## Questions from TRL 1 and where they were settled

All five were decided on 2026-10-03 under Amish's pre-approval and are recorded in the design decisions register (BHK-DEC-001) and decision record BHK-DDR-001.

| Question | Decision |
| --- | --- |
| What stops misuse, for example in disputes or evictions? | The kit is held by the settlement committee in a sealed, locked rack with two named keyholders; every use is logged against the seal number; a pull happens only during a fire, inside a fire plan agreed with the fire service, on a caller's word |
| How far ahead of the fire must the break be? | Training rule: open the break at least two dwellings ahead of the burning one, and only if the pull can finish before the fire reaches it; otherwise evacuate and wait for the fire service |
| A pulley or capstan to cut the crew? | Not in the base kit. A pulley needs a strong anchor that is rarely there; the kit uses ten hauling toggles instead |
| Shared walls? | The tool is used only on free-standing dwellings or the end unit of a row; rows with shared walls are outside its scope |
| Who stores and checks the kit? | The settlement committee, on a monthly check card: seal intact, pins and toggles present, no cracks in the tube, rope dry and unfrayed; a broken seal means a full check and a fresh proof load before reuse |

## Safety

> **Safety:** BreakHook is used to pull down a structure with a hook, a pole and a rope, near a fire. The hazards are a structure falling on people, a dwelling that is not empty, overhead and informal electrical wiring touching the metal hook or a wet rope, a rope or fitting breaking under load, heat and smoke, and crowds. The design answers with a pole that is withdrawn before anyone hauls, haulers at least 10 m away, a rated rope system proof-loaded before issue, an insulated pole length used only well away from wires, and a check card that must be completed before every pull. It is published as an open engineering reference, not certified equipment, and is used only within a community fire plan agreed with the local fire service.
