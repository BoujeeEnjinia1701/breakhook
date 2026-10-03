---
doc_id: BHK-CAL-001
title: BreakHook sizing calculations
project: BreakHook
doc_type: Calculation
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First issue for TRL 3 on the constructable design (pull needed, hauling geometry, hook plate, welds, rope system, pole placement, joints, insulation, deployment time, mass and cost)
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: Fork prop at mid-length added under Amish's decision 6A (BHK-DDR-003); droop, reach, prop load, buckling, prop mass, insulated path to the prop holder [F13 to F24, H3]; kit cost re-run
---

# BreakHook sizing calculations

The constructable design meets its strength, mass, insulation and reach targets on paper: the hook plate keeps a factor of 2.3 or more on yield at the 6 kN proof load, the pole and hook head weigh 7.82 kg against 8 kg, and haulers stand 10.8 m from the wall. With the fork prop at mid-length (BHK-DDR-003) the hook droops about 0.27 m instead of 0.66 m, and nobody lifts the pole: the prop carries 100 N into the ground. Two results still need care: the prop holder stands about 2.9 m from the wall while the hook is set, nearer than the 4 m of R1, and deployment comes out at exactly the 3 minute target. Times and pulls are estimates that a TRL 4 trial on a purpose-built test frame must confirm.

> **Safety:** This note sizes a tool that pulls down a structure with a rope. The numbers assume the dwelling has been checked empty, nobody is inside the fall zone, the pole has been withdrawn before the haul and there are no overhead lines within 3 m. Nothing in this note has been built or tested. Proof loads are applied to each hook head before issue, never to a person or an occupied structure.

## Scope and method

First-order hand calculations, run by `docs/04-calcs/sizing.py`, which takes every dimension and mass from the model (`cad/src/model.py`) and writes `docs/04-calcs/results.csv`. Each result has a reference in brackets, for example [A1]. Loads are static; no dynamic or impact factor is applied beyond the 2 x proof load, which is stated where it matters.

## Assumptions

Table 1. Assumptions

| # | Assumption | Value | Basis |
| --- | --- | --- | --- |
| 1 | Target dwelling | Single storey, 3.0 x 3.0 m, walls 2.4 m, light timber frame clad in corrugated steel sheet, 350 kg | Typical informal dwelling (BHK-PRB-001); to be confirmed with the co-design partner |
| 2 | Racking resistance of a nailed, clad, unbraced frame | 0.5 kN per metre of side wall | Engineering judgement for light cladding; to be measured on the TRL 4 test frame |
| 3 | Sustained pull per hauler on a rope with toggles | 300 N | Conservative for adults on dry ground; peak pulls are higher |
| 4 | Pull rope breaking strength | 25 kN or more, spliced eye 90 % | Bought to this specification (BOM 13) |
| 5 | Leader breaking strength | 20 kN or more, pressed ferrules 90 % | 6 mm 6x19 galvanised wire rope (BOM 12) |
| 6 | Hook plate | S355, yield 355 MPa, 10 mm | BOM 1 |
| 7 | Fibreglass pole tube | E = 20 GPa along the tube; flexural strength 200 MPa; density 1,900 kg/m³; foam 60 kg/m³ | Low end of published values for pultruded round tube; to be confirmed from the maker's data sheet |
| 8 | Placement geometry | Hook at 3.0 m, front hand 1.1 m high and 4.0 m from the wall | R1 |
| 9 | Store distance | Kit stored within 100 m of the dwellings it covers; walking 1 m/s with the kit | Community fire plan rule |
| 10 | Nylon 66 shear strength | 40 MPa | Conservative for a moulded pin |
| 11 | Epoxy allowable lap shear | 5 MPa | One third of a typical 15 MPa structural epoxy |
| 12 | Fork prop | Holds the pole at mid-length, leaning about 13° with its top toward the wall and its foot on the ground; the rear hand holds the butt 100 mm from its end; both are simple supports | BHK-DDR-003 |

## A. How hard to pull (R2, R7, R13)

Pulled at the top of the near wall, a rigid 350 kg dwelling tips over its near edge at 2.15 kN [A1]. A clad frame more often racks: at 0.5 kN per metre of the two 3 m side walls it needs about 3.0 kN [A2]. The working pull is set at 3 kN [A3] and every pulling part is sized for a 6 kN proof load [A4]. At 300 N each, ten haulers give the working pull [A5]; eight are enough for the overturning case [A6].

## B. Hauling geometry (R3)

The first toggle is 11 m along the line from the hook head. With the hook at 3.0 m and hands at 1.0 m, the nearest hauler stands 10.8 m from the wall [B1], against 4.5 m required by R3 [B2]. The rope rises at 10.5° [B3], so 98.3 % of the pull acts along the ground [B4]. The ten toggles run to 20 m along the 26.5 m line [B5], leaving a 6.5 m tail [B6].

## C. Hook plate at the 6 kN proof load (R2, R11)

Table 2. Hook plate stresses at the proof load

| Ref | Check | Result | Factor on yield (355 MPa) |
| --- | --- | --- | --- |
| C2 | Arm root bending, 75 mm deep beam (lever 58 mm) | 97.9 MPa | 3.6 at proof, 7.3 at working |
| C3 | Arm root bending, 100 mm deep beam (lever 90 mm) | 153 MPa | 2.3 at proof, 4.6 at working |
| C4 | Shank tension and bending (rope line 0.5 mm off the arm load line) | 18.1 MPa | 19.7 |
| C5 | Shackle hole tear-out, two 23.5 mm planes | 12.8 MPa | large |
| C6 | Shackle pin bearing on the plate | 54.5 MPa | 6.5 |
| C7 | Rope tab root bending | 37 MPa | 9.6 |

The arm is raked back 16.7° [C1] so a pull draws the beam deeper into the hook. The shackle hole is placed so the rope line passes through the middle of a 75 mm beam; the shank then carries almost pure tension [C4]. The throat takes beams up to 150 mm wide at the shank and 128 mm wide 100 mm down [C8, C9], and up to 117 mm deep [C10].

## D. Socket welds

The rope pulls the plate, never the socket [D2]. The welds carry only placement loads: a 200 N side push at the spike tip gives 4.6 MPa in the four 6 mm fillet welds [D1].

## E. Rope, leader and shackles (R2)

Factors at the 3 kN working pull: pull rope 7.5 [E1], wire rope leader 6.0 [E2], shackle working load limit 3.3 times the pull [E3]. Each prusik cord carries about 300 N [E4] against a breaking strength near 7 kN. The proof load of 6 kN is within the shackle's working load limit.

## F. Pole placement (R1, R5, R8)

Setting the hook at 3.0 m from 4.0 m away puts the pole at 25.4° [F1]. The front hand is 1.27 m from the butt [F2], below the hand band at 1.55 m [F3]. The pole, hook head, leader and the rope hanging from it weigh 84 N [F4]. Held with the hands 1.17 m apart, the rear hand pushes down with 168 N [F5] and the front hand lifts 252 N [F6], so the pole is handled by a team of two: one lifts, one holds the butt down. The tube stress at the front hand is 50.6 MPa, a factor of 4.0 on its flexural strength [F7].

The tube is flexible: with E = 20 GPa the hook droops about 658 mm below the straight line [F8] (second moment of area 8.91 cm⁴ [F9]). Held out by hand, the team would have to aim about 0.7 m high; a stiffer tube would add mass against R5. The fork prop below takes most of this droop out.

### With the fork prop (BHK-DDR-003)

Amish's decision 6A adds a light fork prop that holds the pole at its mid-length, 2,944 mm from the butt [F13]. In the R1 placement the pole's underside is 1.79 m above the ground there [F14]; the prop is set at its third hole (fork notch 1.84 m above the foot) and leans 12.8° with its top toward the wall [F15]. The pole then rests on two supports, the prop and the rear hand at the butt, with the hook end overhanging the prop.

- **Droop:** the hook droops 274 mm below the line through the two supports [F16], against 658 mm when the pole is held out by hand [F8]. The team aims about 0.3 m high and lowers the hook onto the beam.
- **Effort:** the prop carries 100 N into the ground through its foot [F17]; the rear hand pushes down with only 24 N [F18], against 252 N lifted and 168 N pushed down by hand [F5, F6]. The prop holder only steadies the prop.
- **Reach:** the hook is set at 3.0 m. The rear hand is 5.06 m from the wall [F20]. The prop foot is 2.89 m from the wall [F19], and the prop holder stands at or just behind it, so the nearest person is about 2.9 m from the wall while the hook is set, against 4.0 m for the front hand in R1.
- **Strength:** the prop's upper tube alone buckles at 822 N over the whole prop length, 8 times the prop load [F21].
- **Mass:** the prop weighs 1.08 kg [F22] and is carried separately, so the pole and hook head stay at 7.82 kg (R5). Closed, the prop is 1.24 m long (R8).

Moving the prop toward the butt until its foot is 4.0 m from the wall puts it 1,577 mm from the butt [F23]; the hook then droops 720 mm [F24], more than by hand, because nearly all the pole overhangs the prop. The prop only helps near mid-length.

Mass: the pole and hook head weigh 7.82 kg [F10], 0.18 kg under the 8 kg limit [F11]. The longest piece to carry is a section with its sleeve, 1.95 m [F12].

## G. Pole joints and release (R12)

The friction ring is wrapped until a 50 N pull frees the pole from the hook head [G1]. That is about four times the hook head's own weight along the pole at 25° [G2] and needs only 0.018 MPa of contact pressure [G3]. A nylon pin in double shear holds 6.3 kN [G4], about 126 times the release force [G5]; the pins never carry the rope pull. The bonded sleeve holds about 105 kN [G6].

## H. Insulation (R4, R14)

There is no metal between the mouth of the socket and the top of the hand band: 3.67 m of foam-filled fibreglass with nylon pins [H1], against 3.0 m required [H2]. The prop holder's hand is 3.27 m of fibreglass, HDPE and nylon from the socket mouth: along the pole to the fork, then down the prop to the top of its red hand band [H3]. Whether that length insulates depends on the bought tube's certificate (R4). The hook, leader and shackles are metal and a wet rope conducts.

> **Safety:** The insulated length is a second line of defence only. The rule on the check card stands: never raise the pole within 3 m of any overhead line, whatever the pole is made of.

## I. Deployment and pull time (R6, R7)

Table 3. Deployment estimate (pole team of two)

| Step | Seconds |
| --- | --- |
| Cut seal, unlock, lift out one set | 20 |
| Carry to the fire edge, 100 m at 1 m/s | 100 |
| Join three sections, two pins | 20 |
| Hook head onto the pole | 5 |
| Set the hook on the beam | 25 |
| Withdraw the pole, step out of the fall zone | 10 |
| **Total** | **180 (3.0 min) [I1]** |

The other two of the four lay out the rope and run the check card at the same time. The pole team is the rear handler and the prop holder: the prop is stored at the hole marked for the community's usual wall height and goes under the pole in place of the front-hand lift, so the estimate is unchanged; a timed drill at TRL 4 must confirm it. From hook set to frame down: crew on the toggles and the caller's zone check 30 s, slack taken up 10 s, pull 30 s, about 1.2 minutes [I2].

## L. Results against every requirement

Table 4. Requirements against the calculations (requirement text in BHK-REQ-001)

| ID | Target | Result | Status |
| --- | --- | --- | --- |
| R1 | Hook at 3 m from 4 m away | 25.4° pole on the fork prop: droop 0.27 m (0.66 m by hand), rear hand 24 N; rear hand 5.06 m and prop holder 2.9 m from the wall [F13 to F20] | Hook placement met on paper with much less droop; the prop holder stands 1.1 m nearer than the 4 m front-hand distance |
| R2 | 3 kN working, 6 kN proof | Plate factor 2.3 on yield at proof; rope 7.5, leader 6.0, shackle 3.3 [C, E] | Met |
| R3 | Haulers at 1.5 x height or more | 10.8 m against 4.5 m [B1] | Met |
| R4 | Non-conductive handled length, test voltage set | Foam-filled tube with a maker's ASTM F711 certificate [H1] | Met by specification; confirm the certificate when bought |
| R5 | 8 kg or less | 7.82 kg [F10]; the 1.08 kg prop is carried separately [F22] | Met, 0.18 kg margin |
| R6 | 3 min or less with four people | 3.0 min [I1] | Met on estimate, no margin; timed drill at TRL 4 |
| R7 | Under 2 min to bring down a test frame | About 1.2 min [I2] | Estimate only; timed trial at TRL 4 |
| R8 | No piece over 2 m | 1.95 m [F12]; prop 1.24 m closed | Met |
| R9 | 12 months outdoor storage | Material choices only | Not verifiable at TRL 3 |
| R10 | Kit cost against the USD 2,000 target | USD 1,170 with two fork props (bom/bom.csv) | USD 830 under the value-engineering target |
| R11 | Beams up to 100 x 120 mm | 117 mm deep, 128 to 150 mm wide [C8 to C10] | Met |
| R12 | Pole frees from the head before the haul | 50 N release [G1] | Met by design; set by trial |
| R13 | 300 N or less per hauler | 300 N with ten haulers [A5] | Met at the limit |
| R14 | 3.0 m or more insulated length | 3.67 m [H1]; 3.27 m to the prop holder's hand [H3] | Met |

## Checks against the TRL 1 figures

The TRL 1 precis gave a 4 to 6 m pole; the design is 5.9 m overall. The 8 kg mass target holds with 0.18 kg to spare only because the hook plate was trimmed to a 36 mm shank (BHK-DDR-002). The 3 kN working pull stands; the calculation shows it needs about ten people, not four, so the four-person team of R6 deploys the kit and the hauling crew comes from residents on the scene.
