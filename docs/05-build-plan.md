---
doc_id: BHK-BLD-001
title: BreakHook prototype build plan
project: BreakHook
doc_type: Build plan
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First build plan; design made constructable (BHK-DDR-002)
---

# BreakHook prototype build plan

**Plan, not yet built.** How to build the first proof-of-concept prototype, component by component. Building and testing to it is TRL 4 work. Decisions still to be made are kept in the design decisions register ([docs/06-design-decisions.md](06-design-decisions.md)), not here.

## 1. What you are building

![Figure 1. Every component, pulled apart and numbered in build order](05-build-plan/overview.png)

*Figure 1. One set and one rack upright, pulled apart and numbered in build order.*

The prototype is one BreakHook set and its wall rack: a yellow steel hook head on a 5.9 m orange fibreglass pole in three sections, a short steel wire rope leader, a 25 m blue pull rope with ten hauling toggles, and two steel rack uprights. A community kit is two sets on one rack. Six components are made: the hook plate and the socket tube (welded together into the hook head), the pole sections, the joint sleeves, the toggles and the rack uprights. Everything else is bought: shackles, wire rope leader, pull rope, nylon pins, cord, tape, caps, the lock and the seals. The work is cutting and welding steel plate and tube, cutting, drilling and gluing fibreglass tube, and tying knots. The parts for a community kit cost about USD 1,098 from the bill of materials.

> **Safety:** This is a pulling tool used near fire, around people and possibly near electrical wiring. In the workshop the hazards are hot work (cutting and welding steel), fibreglass dust, and, at first load, a rope system under 6 kN. Weld only with fire precautions and eye protection; cut and drill fibreglass outdoors or with extraction, in a dust mask and gloves. Never stand in line with a loaded rope or leader. No part of this plan involves pulling down a real dwelling; first trials use a purpose-built test frame, outside this plan.

## 2. What changed to make it buildable

The concept showed what BreakHook does; several parts could not be made or joined as first drawn. Each change below keeps what the tool does and is recorded in decision record BHK-DDR-002.

*Table 1. Changes from the concept.*

| Component | The concept had | The buildable design has | Why |
| --- | --- | --- | --- |
| Hook head | A forged or fabricated hook with a spike | One profile cut from 10 mm steel plate (Figure 2) | No forging; any welder can cut it |
| Hook to pole | Hook on the end of the pole | A slotted steel socket with the plate welded into both slots (Figure 3) | A face-to-face welded joint a welder can check by eye |
| Pole in socket | Not defined | A slip fit with a rubber tape ring that releases at a firm 50 N pull (Figure 5) | The pole must come off before anyone hauls |
| Pole joints | Not defined | A fibreglass sleeve glued to the lower section and a nylon pin through the upper one (Figure 8) | Foam-filled tube cannot take an inside spigot; no metal in the insulated length |
| Rope attachment | Rope tied to the hook head | A shackle in a hole in line with the hook's arm, a 1.5 m wire rope leader, a second shackle to the rope (Figures 12 and 13) | No knot to weaken or cut; the pull runs straight through the hook |
| Hook plate size | 40 mm shank and arm in ordinary steel | 36 mm shank and 48 mm arm in S355 steel | The arm needed more strength on deep beams; the slimmer shank keeps the weight under 8 kg |
| Hauling handles | Handles or toggles | Fibreglass toggles on prusik cord loops (Figure 10) | They slide along the rope when slack and grip when pulled |
| Rack | A rack and a seal | Two welded flat-bar uprights with lipped arms and a rope peg (Figure 11) | Every piece rests on an arm without touching its neighbour |

## 3. Making the components

Make and check each component before the assembly step that needs it. Sizes are in millimetres. "Front" is the end with the hook; the hook's arm points down. Workshop tolerance is 1 mm unless a step says otherwise; drawings carry no tolerances before TRL 4.

### 3.1 Hook plate

![Figure 2. Making sketch of the hook plate](../cad/drawings/BHK-DWG-101.png)

*Figure 2. Hook plate making sketch (BHK-DWG-101).*

**What it is and what it is made from.** The working part of the tool: a forward spike, a straight shank, an arm that hangs down behind a beam, a small barb at the arm's foot, and a rope tab with the shackle hole. One piece of 10 mm S355 steel plate, from a blank 500 x 200.

**How to make it.**

1. Print the profile from the making sketch at full size, glue it to the plate and centre-punch the corners and the hole centre.
2. Drill the 13 mm shackle hole, centred 55 from the socket end of the plate and 55 below the centre line of the shank.
3. Drill a 16 mm hole at each inside corner where the arm and the tab meet the shank, so the corners end up round (about 8 mm radius), never a sharp notch.
4. Cut the outline by plasma, or by chain drilling and an angle grinder with a cutting disc. The end that goes into the socket is 56 wide and 62 long; the shank is 36 wide; the arm is 48 wide and hangs 117 below the shank, sloping back toward the user by about 17°; the spike tip is on the centre line, 440 from the socket end.
5. Grind every edge clean, break the corners by about 1 mm, and dress the spike to a point with no burr.
6. Stamp "WLL 3 kN" and the serial number on the shank, near the socket end.

**How it fits the parts next to it.** The wide end slides 50 deep into the socket's two slots and stands 2.6 proud of the tube top and bottom for the welds (Figure 3). In use the shank rests on the top of a wall plate or rafter and the arm hangs behind it (Figure 4); the rope pulls through the shackle hole, which lines up with the middle of a 75 mm beam.

![Figure 3. Joint 1: hook plate in the socket slots](05-build-plan/joint-01.png)

*Figure 3. The plate sits in slots top and bottom and is welded along both sides of each slot.*

![Figure 4. Joint 7: the hook on a wall plate](05-build-plan/joint-07.png)

*Figure 4. In use: shank on the plate, arm behind it.*

**Check before moving on.** Lay the plate on the full-size print: every edge within 1 mm. A 75 x 50 timber offcut fits under the shank against the arm, and a 100 mm deep one fits too.

### 3.2 Socket tube

![Figure 5a. Making sketch of the socket tube](../cad/drawings/BHK-DWG-102.png)

*Figure 5a. Socket tube making sketch (BHK-DWG-102).*

**What it is and what it is made from.** The short steel tube the pole slides into. Welded steel tube 50.8 x 2.0, cut to 180.

**How to make it.**

1. Cut 180 from the tube and square both ends.
2. Wrap a strip of paper round one end to mark two slots exactly opposite each other, 10.5 wide and 50 deep.
3. Cut the slots with a hacksaw or a thin cutting disc and file them to width, square at the bottom.
4. Deburr the bore at the open end and break its edge.

**How it fits the parts next to it.** The bore is 46.8; the 44.5 pole slides in with about 1.15 clearance all round and goes in 130 until it stops on the end of the plate. A ring of rubber tape on the pole tip makes it a firm push fit (Figure 5).

![Figure 5. Joint 2: pole tip in the hook head](05-build-plan/joint-02.png)

*Figure 5. Cut open: the pole stops on the plate; the tape ring holds it.*

**Check before moving on.** A 300 offcut of pole tube slides in and out by hand; the plate goes into both slots with no more than 0.5 total play.

**Welding the hook head (Step 2).** Tack the plate in the slots, check it is square to the tube and centred, then run a 6 mm fillet weld along both sides of each slot, outside the tube. Clean, prime with zinc-rich primer and paint high-visibility yellow.

### 3.3 Pole sections (make 3)

![Figure 6. Making sketch of a pole section](../cad/drawings/BHK-DWG-103.png)

*Figure 6. Pole section making sketch (BHK-DWG-103).*

**What it is and what it is made from.** Three 1.8 m lengths of foam-filled, electrical-grade fibreglass tube 44.5 x 3.2 that carries the maker's dielectric test certificate. The butt section is the bottom one, the top section carries the hook head.

**How to make it.**

1. Cut three lengths of 1800 with a fine-tooth saw, the tube wrapped in tape where you cut. Work outdoors in a dust mask and gloves.
2. Middle and top sections: drill one 10.5 hole straight across the tube, through both walls, 74 from the bottom end.
3. Seal every cut end and the bore of every pin hole with a thin coat of epoxy, so water cannot get into the foam.

**How it fits the parts next to it.** The butt and middle sections each get a sleeve glued on their top ends (section 3.4); the section above slides into that sleeve and is pinned. The butt section also gets a rubber cap and a red hand band 1550 to 1600 from its bottom end. The top section gets the friction ring 110 to 150 below its tip.

**Check before moving on.** Each section is 1800 within 2; the pin holes are square to the tube by eye.

### 3.4 Joint sleeves (make 2)

![Figure 7. Making sketch of a joint sleeve](../cad/drawings/BHK-DWG-104.png)

*Figure 7. Joint sleeve making sketch (BHK-DWG-104).*

**What it is and what it is made from.** A 300 length of fibreglass tube 50.8 x 3.2 that joins two pole sections.

**How to make it.**

1. Cut two lengths of 300 and seal the ends with epoxy.
2. Sand the bore with coarse paper on a dowel, trying a pole offcut often, until the pole slides in with about 0.2 clearance all round.
3. Drill one 10.5 hole straight across, 75 from the middle of the sleeve.
4. Glue the half without the hole (150) onto the top of the butt section, and the other sleeve onto the top of the middle section, with structural epoxy. Wipe off the squeeze-out and let it cure a full day.

**How it fits the parts next to it.** The two sections meet in the middle of the sleeve with a 2 gap. The upper section slides into the free half and a nylon pin goes through the sleeve and the section (Figure 8).

![Figure 8. Joint 3: pole joint](05-build-plan/joint-03.png)

*Figure 8. Cut open: glued below the joint line, pinned above it.*

**Check before moving on.** The upper section slides in and out by hand and the pin goes through both holes without forcing.

### 3.5 Hauling toggles (make 10 per set)

![Figure 9. Making sketch of a hauling toggle](../cad/drawings/BHK-DWG-105.png)

*Figure 9. Hauling toggle making sketch (BHK-DWG-105).*

**What it is and what it is made from.** A 300 length of fibreglass tube 32 x 3 that a hauler holds, hung from the pull rope on a loop of 6 mm cord.

**How to make it.**

1. Cut ten lengths of 300; round and seal the ends.
2. Drill a 10 hole straight across at mid length.
3. Pass 1.2 m of 6 mm cord through the hole and tie it into a loop with a double fisherman's knot that sits under the toggle.

**How it fits the parts next to it.** The loop goes onto the pull rope with a three-turn prusik hitch, which slides when slack and grips under load (Figure 10). Toggles go 1 m apart from 11 m along the line.

![Figure 10. Joint 6: hauling toggle on the rope](05-build-plan/joint-06.png)

*Figure 10. Three-turn prusik on the 12 mm rope.*

**Check before moving on.** Hang 30 kg from one toggle on a length of the rope: the prusik does not slip.

### 3.6 Rack uprights (make 2)

![Figure 11a. Making sketch of a rack upright](../cad/drawings/BHK-DWG-106.png)

*Figure 11a. Rack upright making sketch (BHK-DWG-106).*

**What it is and what it is made from.** A wall bracket of 40 x 6 steel flat bar: an 800 upright, two 250 arms with 30 lips, and a 380 rope peg with a 40 lip.

**How to make it.**

1. Cut the upright, two arms, a peg and three lips from 40 x 6 flat bar.
2. Drill two 11 holes in the upright, 50 and 750 up, for M10 anchors.
3. Weld the lips on the ends of the arms and the peg, standing up.
4. Weld the arms square to the front face of the upright with their tops 256 and 506 up, and the peg at 700 up. Weld all round each root.
5. Grind smooth, prime and paint.

**How it fits the parts next to it.** The two uprights go 1200 apart on a wall. Each arm holds four poles 56 apart, with the sleeves at alternate ends so they do not touch. The rope coil hangs on the peg clear of the arms below (Figure 11).

![Figure 11. Joint 8: poles on the rack arms](05-build-plan/joint-08.png)

*Figure 11. Lower arms hold the butt and middle sections, upper arms the top sections with their hook heads.*

**Check before moving on.** Arms level and square to the wall; a 10 kg load leaves no movement.

### 3.7 Bought components

- **Shackles (four per kit):** 3/8 in (10 mm) screw-pin bow shackles, galvanised, rated 1 t and marked. Check the jaw takes the 10 mm plate and the pin passes the 13 mm hole. Mouse each pin with soft wire after fitting.
- **Wire rope leaders (two):** 6 mm 6x19 galvanised wire rope, 1.5 m between thimble eyes with pressed ferrules, proof tested and tagged by the rigging shop (Figures 12 and 13).
- **Pull ropes (two):** 12 mm polyester double braid, breaking strength 25 kN or more, 25 m with a spliced eye; whip the tail.
- **Nylon pins (four):** 10 mm nylon 66 clevis pins with nylon hitch clips; tie each to its section with a cord lanyard.
- **Friction ring tape, red tape and clear sleeve, butt caps, structural epoxy, cord, paint:** as the bill of materials.
- **Lock cable and padlock, numbered seals, fall zone tape and stakes, check cards, rigger gloves:** used in Step 14 and in training.

![Figure 12. Joint 4: shackle in the rope eye](05-build-plan/joint-04.png)

*Figure 12. Shackle pin through the 13 mm hole; leader eye on the bow.*

![Figure 13. Joint 5: leader to pull rope](05-build-plan/joint-05.png)

*Figure 13. Second shackle through the far leader eye; the rope's spliced eye on its bow.*

## 4. Putting it together

In each picture the parts already fitted are grey and the part being fitted is in colour, with an arrow showing the way it goes in. Long parts are drawn cut short around the joint.

### Step 1: hook plate into the socket slots

![Step 1](05-build-plan/step-01.png)

Slide the plate's wide end into both slots until it bottoms, 50 deep, with the arm pointing down.

### Step 2: weld, clean and paint the hook head

![Step 2](05-build-plan/step-02.png)

Tack, check square, then weld both sides of each slot (section 3.2). **Hold point:** safety stop S1.

### Step 3: bond a sleeve onto the butt section

![Step 3](05-build-plan/step-03.png)

150 onto the top end with epoxy, the drilled half sticking up. Cure a full day.

### Step 4: bond a sleeve onto the middle section

![Step 4](05-build-plan/step-04.png)

As Step 3, on the middle section's top end.

### Step 5: butt cap and hand band

![Step 5](05-build-plan/step-05.png)

Push the cap onto the butt end. Wrap red tape from 1550 to 1600 up from the butt end and shrink a clear sleeve over it.

### Step 6: friction ring on the top section

![Step 6](05-build-plan/step-06.png)

Two or three turns of rubber tape, 110 to 150 below the tip, stretched as you wrap.

### Step 7: join the butt and middle sections

![Step 7](05-build-plan/step-07.png)

Push the middle section fully into the sleeve, line up the holes, fit the nylon pin from the top and clip it.

### Step 8: join the middle and top sections

![Step 8](05-build-plan/step-08.png)

As Step 7.

### Step 9: hook head onto the pole

![Step 9](05-build-plan/step-09.png)

Push the hook head over the friction ring until the pole stops on the plate. Pull it off and on again: it should need a firm pull of about 50 N (a 5 kg spring balance). Add or remove a turn of tape until it does.

### Step 10: shackle and leader onto the hook

![Step 10](05-build-plan/step-10.png)

Put the leader's eye on the shackle bow, the pin through the 13 mm hole, tighten by hand and mouse it with wire.

### Step 11: pull rope onto the leader

![Step 11](05-build-plan/step-11.png)

Second shackle through the far eye of the leader, the rope's spliced eye on its bow; mouse the pin. **Hold point:** safety stop S2.

### Step 12: toggles onto the rope

![Step 12](05-build-plan/step-12.png)

Ten toggles, 1 m apart, the first 11 m from the hook head.

### Step 13: rack uprights onto the wall

![Step 13](05-build-plan/step-13.png)

1200 apart, plumb, with two M10 anchors each into masonry or coach screws into a timber post.

### Step 14: stow the kit, lock and seal

![Step 14](05-build-plan/step-14.png)

Butt and middle sections on the lower arms, sleeves at alternate ends; top sections with their hook heads, shackles and leaders on the upper arms; ropes coiled on the pegs with the toggles. Run the lock cable through every section and both hook eyes, padlock it and fit a numbered seal. **Hold point:** safety stop S4.

## 5. First checks

These are the checks a TRL 4 test report would record; this plan only lists them. Requirement numbers are those of BHK-REQ-001.

*Table 3. First checks.*

| Check | Requirement | How | Pass when |
| --- | --- | --- | --- |
| Proof load | R2 | Hook head, shackles and leader loaded to 6 kN for 1 minute through a 75 x 100 timber in the hook, on CalRig or at a rigging shop | No crack, no visible bend, no weld mark; hook throat opening changes by less than 1 mm |
| Mass | R5 | Weigh the pole with the hook head | 8 kg or less (7.82 kg estimated) |
| Longest piece | R8 | Measure each section with its sleeve | 2.0 m or less |
| Release | R12 | Spring balance on the pole while the hook head is held | Releases at about 50 N |
| Insulated length and certificate | R4, R14 | Measure from the socket mouth to the top of the band; read the tube certificate | 3.0 m or more; certificate to ASTM F711 present |
| Beam fit | R11 | Hang the hook on 75 x 50 and 100 x 120 timber offcuts | Shank rests on top, arm behind, no forcing |
| Reach | R1 | Pole team sets the hook on a 3 m high timber rail from 4 m away | Hook set in three tries or fewer; droop measured |
| Toggle grip | R13 | 30 kg hung on a toggle on the rope | No slip |
| Deployment drill | R6 | Four people, kit 100 m from the rail, stopwatch | Hook set and pole withdrawn in 3 min or less |

## 6. Safety stops

Stop at each point. Carry on only when everything listed is true.

- **S1. Before any weld is loaded.** The welds have been looked at by the welder and a second person: full length, no cracks, no undercut at the slot ends. The plate is square to the tube.
- **S2. Before the first proof load.** The rig and the load path are rated above 6 kN; the shackle pins are moused; nobody stands in line with the rope, leader or hook, or within 3 m of the load path; a heavy blanket or mat is laid over the leader to catch it if it parts.
- **S3. After the proof load.** Any bend, crack or shifted ferrule takes that part out of service for good; nothing is straightened and reused.
- **S4. Before the kit is issued to a community.** Proof load passed and tagged for both sets; tube certificate on file; check cards, gloves and fall zone tape in the kit; the community's fire plan, agreed with the fire service, names the keyholders and the caller; training has been given.
- **S5. Before any trial pull (outside this plan).** Only on a purpose-built test frame, never an occupied or lived-in structure; the frame checked empty; no overhead lines within 3 m; fall zone taped; pole withdrawn and the pole team out of the zone; haulers at least 10 m back, in gloves, on the caller's word.

## 7. Tools, skills and workspace

**Tools.** Angle grinder with cutting and flap discs, or access to a plasma cutter; bench drill with drills to 16 mm; centre punch and letter stamps; MIG or stick welder; hacksaw; fine-tooth saw for fibreglass; files; coarse abrasive paper and a dowel; tape measure, steel rule, square and calipers; 5 kg spring balance; bathroom or hanging scale; paint brushes; heat gun for the clear sleeve.

**Skills.** A competent welder for the hook head and rack; basic workshop skills for the rest; knot tying (double fisherman's knot, prusik hitch), which a rigging shop or climbing club can teach. The proof load is done by a rigging shop or on CalRig with someone trained to use it.

**Workspace.** A metalworking bench with a fire-safe area for welding; an outdoor or ventilated space for cutting and drilling fibreglass; 6 m of clear floor to lay out and join the pole.

**Personal protective equipment.** Welding helmet, gloves and jacket for hot work; safety glasses for cutting, grinding and drilling; dust mask (FFP2 or N95) and gloves for fibreglass; hearing protection for grinding; rigger gloves for handling rope under load.

## 8. Where the numbers come from

- Model and constructability checks: `cad/src/model.py` (`python cad/src/model.py --check`); STEP and STL exports in `cad/step/` and `cad/stl/`.
- Pictures: `cad/src/build_plan_media.py`, using `.kit/build_views.py`; written to `docs/05-build-plan/` and `cad/drawings/BHK-DWG-101` to `BHK-DWG-106`.
- General arrangement: `cad/drawings/BHK-DWG-001.pdf`, Rev P1.
- Calculations: `docs/04-calcs/01-sizing.md` (BHK-CAL-001 v0.1) and `docs/04-calcs/sizing.py`.
- Bill of materials: `bom/bom.csv`.
- Decisions: `docs/decisions/0001-trl2-review-decisions.md` (BHK-DDR-001) and `docs/decisions/0002-design-for-construction.md` (BHK-DDR-002).
- Requirements: `docs/03-requirements.md` (BHK-REQ-001 v0.2).
