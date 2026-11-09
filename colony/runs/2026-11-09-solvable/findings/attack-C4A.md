# attack-C4A (cluster C4, independence sweep): op.window-p3, op.thickness-deposit-rule, op.residue-killing-weights

Status: done; three proposals filed (check4 exit 0 with no warnings, validate_one ok, on the work folders; the
proposal folders are byte-identical copies plus coverage.yaml). Kill conditions were written before the
computations they govern (first version of this file).

## op.window-p3: the lowest causal member of each residue

FIX ROUND (supersedes the window results below where they differ): the referee found that Premise U (U3) was
missing from the audit and fails in M_8 at (10,1) and (1,10). My own check confirms this. The proposal is
restated: independence holds at residues 3 and 5 only (M_8 shifts (4,1), (1,4) to (12,1), (1,12); ratio in
(9.9, 10.0)). At residues 1 and 7, U3 with the stored pair count admits only the lowest causal member, so there
P3's clause follows from U. The independence kill condition therefore fired at residues 1 and 7. Details:
fixes-C4A.md.

Orientation. The number: the dimension of the representatives of the odd reversal pairs {1,7}, {3,5} (3 and 5
under P3, the lowest causal members). {2,6} is pinned by observation and P2; {0}, {4} by the costed single-ideal
clause (separate, untouched). Premise set: union of the past cones of towers-are-residues, unit-ball-rule,
lowest-causal-residues-zero-four-content, residues-zero-four anomaly, oriented-causal, flag-bit,
reversion-pairing, invariant-forms, imported-towers-their-types: F1-F4, P1, P2, P3, R1-R3, H1, indifference,
(Q), tameness, imports (Chevalley, Witt, Morita, Clifford structure/classification, Fock, anomaly coefficients,
inverse-square law, QFT/tractor imports that do not mention a tower's signature).

Routes. 1 (own problem's) a non-periodic selector: (W), the residue-0 anomaly at (1,1), P3's minimality reading.
2 (Bott/Morita, tower subject) the shift beta: (p,q) -> (p+8,q) along the majority sign. 3 (own) P2's sentence
"the descent cannot instantiate uncaused distinctions" read against the choice (argued only; see Decisions).
Chosen: 2 (it settles 1: a derivation exists iff some premise fails in the shifted model).

Kill condition, constructive (registered): a derivation exists only if a premise other than P3 holds in M_L and
fails in M_8. FIRED: every premise holds in both (exact checks plus premise-by-premise proof). Kill condition,
independence (registered): dies if a premise's condition on a signature is not beta-invariant. NOT fired: the only
non-periodic selectors found are (W) (not adopted) and the anomaly obstruction at (1,1) (residue 0 only, costed
clause), both outside the odd residues' premise content.

Established (proved, exact): (i) Cl(beta s) = A (x) B with A = <e_i w8> a faithful copy of Cl(s) (2^(n+8)
distinct blades), B = Cl(8,0) or Cl(0,8) = Mat(16,R) (primitive idempotent f, f~ = f, fBf = Rf on all 256
blades), [A,B] = 0, reversion factorwise, so reversion-pairing type, residue, causality, n mod 8, pseudoscalar
square and centrality invariant. (ii) M_L ((2,1),(1,2),(4,1),(1,4)) and M_8 ((10,1),(1,10),(12,1),(1,12)) both
satisfy every premise of the set minus P3; iterating gives infinitely many models. (iii) (W) admits M_L only and
is the unique-admitted-lowest selector up to dimension 16. (iv) Cost: unit-ball ratio 5.364 in M_L, 1 + 320/pi^4
+ 1920/pi^5 in (10.5, 10.6) in M_8; the window is an input selected by the observed ratio; P3 stays costed.
Aside (computed, not filed): the other causal members (1,8), (8,1), (1,6), (6,1) give 1 + 64/pi^3 + 16/pi^2,
about 4.69, so the observed value sits between models on both sides.
Proposal: synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free.
Not established: that no future premise fixes the window; anything about residues 0 and 4.

## op.thickness-deposit-rule: no rule P2 licenses gives R3

Routes. 1 (problem's) a deposit rule from P2: equal filling of equivalent objects. 2 (other subject: asymmetric
dark-matter coincidence) the 1/epsilon branch. 3 (own) independence family with separate thicknesses for the
5D and 3D pairs. Chosen: 3 for independence, 1+2 for the licensed-rule classification.
Kill condition, constructive (registered): a derivation needs a licensed equality relating a 5D tower's filling to
ours that yields share 8/(3 pi). FIRED: licensed cross-tower shares are 1 or 1/epsilon >= 1; 8/(3 pi) < 1.
Kill condition, independence (registered): dies if a premise other than R3 mentions the counted thickness. NOT
fired.
Established (proved, given a stated definition of "licensed"): (i) every premise but R3 holds for every
(lam, mu), T = 1 + 8/(3 mu) + 16 lam/(3 pi) covers (1, infinity), extends the stored diagonal T(c); P2 as scoped
licenses no filling rule. (ii) own cells of different dimension are not isometric (GA Gram ranks 3, 2, 4, equal
only within reversal orbits), so licensed rules equate only shared objects: shares 1 or 1/epsilon; R3's 5D share
8/(3 pi) in (5/6, 8/9) is neither; licensed lam = 3 pi/8 or 3 pi/(8 epsilon), never 1; the 3D share alone would
match at epsilon = 3/4. (iii) 5.364 stays a fit; R2 and R3 together are democracy in cells P2 does not relate.
Proposal: synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3.
Not established: attack items 2-4 (deposit correlation length, sheets' displacement, evaporation measurement).
The definition of "licensed" is a reading of P2's text plus the store's own per-rung extension; a referee may
want it flagged as the hypothesis it is (it is stated in the formal level).

## op.residue-killing-weights: the count unit

Routes. 1 (problem's) a structural pairing of the 16 Weyl arrays per generation into registered units (CPT,
chirality, particle-hole); chirality closed earlier. 2 (other subject: Susskind-Uglum species degeneracy)
grouping independence. 3 (own) ask what the residue requires of the unit, including non-uniform groupings.
Kill condition, constructive (registered): a derivation needs a premise that mentions a grouping of arrays into
units, or a structural unit carrying exactly ln 2 at the Hawking state. FIRED: no premise mentions a grouping;
(C2) leaves nu free; a ladder pair carries at most s(pi) < 0.21 < ln 2 at the weights of (Q) v3.
Established (proved): (i) every grouping is a model of the cone; kappa_c = 1/(2 u-bar ln 2). (ii) the residue
holds iff the MEAN arrays per unit is 2 (22 of the 231 groupings of a generation by size; uniform only at 2);
no single ladder pair qualifies; at offset 0 no union of whole arrays does. (iii) light rays number
2 pi N^2/(c ln 2) on the cosmological horizon (c arrays per light ray), independent of the unit; registered units
pi N^2/ln 2 only at u-bar = 2; units per light ray c/2 (24 at three generations of fermions). The stored note in
dark-matter.stored-asymmetry-charge-not-number calls pi N^2/ln 2 a count of light rays: it is the count of
registered units (that proof uses only that N is common; unaffected).
Proposal: synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping.
Not established: a derivation of the unit (none exists in the premises); what fixes c (C3's question).
Note: the stored "N copies" independence is not compatible with the proved content (sixteen per generation);
the free datum is the grouping.

## Unexpected links
- Residue (iii) and C3's light-ray sea: the c of my light-ray count is C3's c = 16 n_g + 2 n_V + n_s + 2 eps
  (proposal synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content); whatever C3
  settles for c fixes the light-ray density 1/(2 c ln 2) per Planck area per period, while the count unit stays
  free. At the fermion content the units per light ray are 8 n_g, which is 24 at n_g = 3; I see no derivation
  behind that coincidence with C3's 24 (the 24 there is c, here c/2 at n_g = 3).
- Window and indifference: P2's first sentence (the descent cannot instantiate uncaused distinctions) and the
  series' indifference premise both read, with the window independence, as saying the descent itself cannot have
  picked the representative: P3 is a choice the premises cannot make (see Decisions 1).
- Same shape as C4B's results (model pair plus cone audit): the window, the thickness and the count unit join
  N, xi G, the Majorana scale and the down-type 126 weight as register inputs moved by a model family that fixes
  every stored relation.

## Decisions for Leon
1. (window) P3 stays a costed premise. Should its note record that the lowest-causal clause is independent of the
   descent (the Bott-shifted model), and should op.window-p3 be marked settled on that clause (success clause:
   "show the descent leaves it free")? Recommendation: yes to both; keep the problem partial only for the
   pairing-reading attack item. Also note the tension that P2's "cannot instantiate uncaused distinctions"
   forbids the descent from making the choice P3 makes; recommendation: say in P3's note that P3 is a premise of
   the model, not a step of the descent (no change to content).
2. (window, wording) R2's parenthetical "D dimensions (2, 3 or 4)" is P3's window; recommendation: reword as
   "(under P3, 2, 3 or 4)" so R2 is not read as a selector. Maintainer wording fix.
3. (thickness) Mark attack item 1 (second half) of op.thickness-deposit-rule done under the stated reading of
   "licensed"; the problem stays partial (items 2-4). Recommendation: yes; the reading of P2 used (equal filling
   only of objects in one symmetry orbit, shared objects included) is the store's own, and should be named in the
   problem's known text.
4. (residue) Record the count unit as an input in op.residue-killing-weights (it is already a decision); amend the
   known text: the residue requires a mean of two arrays per unit, not pairs, and the "N copies" independence is
   replaced by grouping independence given the proved content. Recommendation: yes.
5. (residue, correction) dark-matter.stored-asymmetry-charge-not-number v9: "N fixes a count of light rays, about
   pi N^2/ln 2" should read "a count of registered boundary modes, about pi N^2/ln 2, and of light rays,
   2 pi N^2/(c ln 2) for c arrays per light ray". Maintainer wording fix (version+1); its argument is unaffected.
No new postulate, assumes edge or retirement is requested.
