# Report, run 2026-11-18-navigate

Request (Leon, 18 November 2026): navigate the physics graph; look for open problems, not necessarily the listed
ones; look for cross-pollination of ideas; make headway where possible.

Method: lean (see RUN.md). One session surveyed the graph and attacked three targets itself; one blind referee
(Claude Opus 5.5) read the proposals twice (R1, R2) and the numerical restatement once (R3); one maintainer agent
restated the numbers that depend on the corrected production rate (maintainer-M1.md). The survey is LEADS.md.

## What was established

### 1. Conjecture 7.9 of the first paper is decided (unlisted problem)
synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump. R1 OVERSTATED, R2 SOUND WITH FIXES
(applied).
- proved: a signature jump obstructs every completion of one exterior signature, with no tameness; where the
  degeneration then sits is not fixed by the family (it can be the original locus or either side).
- proved: without a jump the doubling is such a completion; the doubling adjoins one generator anticommuting with
  the family.
- proved: transfer. A completion that is nondegenerate everywhere carries on its complement the opposite of the
  class of the family's eigenbundles relative to the base.
- proved: with one fixed exterior form there are further obstructions; [[x,y],[y,-x]] over the plane has no such
  completion for bounded U (twisted positive eigenline).
- proved: x^2, diag(x,-x), x^2+y^2 complete with a fixed exterior form: the conjecture is false in each
  tameness-failure mode.
- proved: x id in rank four jumps (4,0) to (0,4) with equal residues modulo 8 and is obstructed.
- proved (removable half), computed (m up to 4), cited and not used (the rest): multiplication by the position
  vector on the least module of Cl(m,0) is repaired on the same module for m = 0, 4, 6, 7 mod 8.
Ledger: transport-convenient. Decision (Leon): the conjecture is recorded as refuted as stated (version 4), and
op.eigenbundle-class-of-degenerations holds what is still open.

### 2. The gravitational production rate (op.graviton-rate-as-classical-field-process)
synthesis.gravitational-pair-production-from-the-operator-source-at-first-order. R1 SOUND WITH FIXES, R2 SOUND.
- proved: at non-null momentum the first-order gauge field is fixed by its source up to a displacement (Einstein
  map kernel four; six at null momentum).
- proved given (OS): interaction 8 pi G B/Q(k), normalised by the stored Newtonian coupling.
- computed: nine channel weights (pi/180)(c_i c_j + 5 tau_i tau_j), c = 1, 3, 12.
- proved given (OS) and the standard collision integral: Gamma = alpha T^8/Mbar^4; from (4, 45, 12):
  5789 pi^3/82944000 (scalar), 16087 pi^3/82944000 (chiral fermion), 16087 pi^3/20736000 (massless vector), per
  creation event of two quanta.
- read at source (proposer and referee): the stored coefficient was one sixteenth of the same group's later value
  (half the canonical coupling in the 2018 paper; its appendix confirms it) and both papers weight chiral fermions
  as Dirac. Net: the stored scalar coefficient was low by 46312/3997 = 11.6. The correction holds on the standard
  account as well as under (OS).
- argued: a mean-field source gives no such rate.
Ledger: transport-absent. Decisions (Leon): (OS) stays a hypothesis of the result; the Fact and its users are
restated now. The problem is partial: the field at null momentum and the burst baseline remain.

### 3. Slaved field and commutation at spacelike separation (unlisted gap)
synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation. R1 OVERSTATED, R2 SOUND
WITH FIXES (applied).
- proved in an exact lattice scalar model: the slaved field fails to commute with the source's later detection at
  172 of 502 spacelike events; its own bracket vanishes; an instantaneous slaved field fails likewise; a free part
  with canonical commutators restores commutation at all 502, to first order.
- argued: the reading for the gravitational gauge field, conditional on a requirement the store does not state
  and on an extension of the element reading that the store does not hold.
Ledger: transport-absent; prior art named. Decision (Leon): recorded as open,
op.gravitational-field-at-null-momentum, with a scope paragraph in the conventions; no position or prediction
changed.

## Maintainer pass
- Accepted: the three results, with coverage records.
- transport.obstructions-are-moved-never-destroyed: version 4, status refuted, refuted_by the deciding result.
- store/open_problems.yaml: two new problems; op.graviton-rate-as-classical-field-process set to partial with the
  18 November paragraph; op.wall-class-invariant annotated; stale quoted numbers in op.odd-towers,
  op.pre-descent-theory and op.matter-asymmetry-origin restated.
- store/conventions.md: a scope paragraph under "Gravity and the graviton".
- dark-matter.imported-massless-graviton-production-rate: version 4 (both published values, the sixteen, the
  fermion weight, the derived coefficients; flag replaced by a citation). New reference CleryEtAl2022.
- The four direct users and nine dependants restated (maintainer-M1.md), and
  synthesis.majorana-scale-free-on-pati-salam-route (a quoted number).

Numbers that moved (stored energy convention, ceiling reheating): mirror floor 2.8 to 3.2e-4 -> 5.2e-4; nine
vectors 3.5e-4 -> 6.4e-4; eta' at the mirror's floor 19 to 26 -> 4.4; yield shortfall 3 to 5e4 -> 4.4e3; rescue
temperature 31.9 to 36.2 -> 16.4 times the ceiling; Pati-Salam exclusion margins 4.0 and 2.5 -> 2.2 and 1.5; Dirac
mass needed 8.2 -> 6.4 GeV against the cap 5.2.

Conclusions that changed (all weakened, none lost): the Delta N_eff bounds at the floors are one order weaker;
"more than four orders too few" is "more than three"; the mirror's neutron-rich composition is established only at
the old floor, xi = 2.8 to 3.2e-4, and is not recomputed at 5.2e-4; in the Pati-Salam result's clause (iii) one
inequality reverses at four Standard-Model contents, enlarging the surviving branch.

## Cross-links found (LEADS.md, section B)
The stored first-order theorem of the Einstein subject is the lemma both the rate and the locality question needed;
the doubling of the wall-class theorem is "one more anticommuting generator", which turns Conjecture 7.9 for
Clifford multiplication into module extension; the scalars' curvature coupling enters the dark towers' heating;
the Kerr ring is a codimension-two degeneration of the kind the new degree-one class lives on.

## Review of the restatement (R3)
Every changed number was reproduced by the referee. Fixes applied: the operator-source condition restored in three
sentences of the Fact and in the conventions paragraph; the clause (iii) reversal of the Pati-Salam result stated
with its factor and its 7 percent margin (not decided at four Standard-Model contents); two entities outside the
Fact's cone that still placed the neutron-rich composition "at the floor" reworded
(dark-matter.mirror-share-one-how-fragile, simulations.s3-mirror-cluster); "an obstruction", not "the invariant",
in the conjecture's note and the new problem's text. Final check: 0 errors, 1 warning (the baseline's own); build 0
errors; 445 unit tests pass.

## Left open, for Leon
1. The energy per creation event in the floor formula. The stored convention is 3T per event (energy fraction 4Y).
   The referee computed the mean from the rate integral: 4 zeta(5)/zeta(4) T = 3.83 T per Bose leg, 4.11 T per Fermi
   leg, about 7.9 T per event for the Standard Model's bath, energy fraction 10.5 Y. At that energy the floors are
   1.27 times the stated ones (mirror 6.6e-4, nine vectors 8.1e-4), eta' at the mirror's floor is 2.1, and the round
   upper bounds built from the floor (Delta N_eff at the floors; the bounds under (R)) are exceeded by up to 2.7. No
   conclusion changes. In this pass the stored convention is kept and each such bound is marked as holding on it,
   with the computed values beside it. Adopting the computed energy is a further restatement of the same entities.
2. dark-tower-matter.mirrors-composition clause (i) at the new floor needs the MIR and CHECK_COS scripts of the
   papers suite; they are not in the repository.
3. legacy/verify_T14.py and the deposited T14 text still carry the first coefficients.
4. Three setting notes quote old figures (note.dark-matter.setting-successor-problems,
   note.dark-matter.setting-dark-stable-counted, note.simulations.setting-composition-recombination).
5. sheaf.wall-class clause (c) still cites the refuted conjecture; its rewording is an attack item of the new
   problem.
6. Unlisted items of LEADS.md not acted on: rows 5, 6, 8, 9, 10.
