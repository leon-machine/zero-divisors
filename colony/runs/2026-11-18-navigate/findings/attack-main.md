# Findings, run 2026-11-18-navigate (one attacker; see RUN.md for the method and the kill conditions)

## A. Conjecture 7.9 of the first paper (unlisted)
Routes considered: (1) the stored signature argument with tameness removed; (2) counter-models, one per tameness
clause, completed by the stored doubling; (3) obstruction theory for the eigenbundles of the family on the
exterior. Chosen: (1) and (2) first, (3) when (2) forced it.

Established (labelled):
- proved: a signature jump obstructs every completion with one exterior signature, with no tameness.
- proved: the double g e1 + b e2 is nondegenerate for every family; it is strict exactly when the signature does
  not jump. So under the stored definition of "standard" the signature jump is the whole obstruction.
- proved, and found only on rereading the definition: with a fixed exterior form K0 there is more. For
  [[x,y],[y,-x]] in the plane no completion with a constant K0 is nondegenerate everywhere (the positive
  eigenline is a Moebius line around the origin; a bundle on the plane restricts to an orientable one). The first
  filing (see proposals history) presented this family as a counter-model without saying that its completion needs
  a twisted K; that was an overstatement, corrected before the referee's report was read.
- proved: transfer. Any completion nondegenerate everywhere has, on the exterior, complement eigenbundles carrying
  the opposite class. This is "moved, never destroyed" as a theorem.
- proved: x^2, diag(x,-x), x^2+y^2 have completions with a constant exterior form: the conjecture as a general
  statement is false in each tameness-failure mode.
- proved: x id in rank four: jump (4,0) to (0,4), equal clocks, obstructed.
- proved (removable half), computed (m <= 4), cited (the rest): multiplication by the position vector on the least
  module of Cl(m,0) is repaired on the same module when one more anticommuting generator exists; least-module
  dimensions give m = 0, 4, 6, 7 mod 8.
Ledger: transport-convenient, except the last item.
Next step: derive the eigenbundle class of isolated degenerations in the store's own terms (a successor problem);
the m = 3 case needs a degree-two class.

## B. op.graviton-rate-as-classical-field-process
Routes: (1) the problem's own: operator source beyond the static limit, Green function of the linearised
equations; (2) from another subject: the stored first-order theorem of the Einstein subject (covariant classes at
each momentum), which already says the field at non-null momentum is fixed by the source; (3) own: spin-two
weights and helicity structure to avoid nine separate amplitude computations. Chosen: (2) for the "no quantum
needed" statement, (1) for the normalisation (static limit against the stored Newtonian coupling), (3) for the
coefficients.

Established:
- proved: G_k[T - 1/2 id tr T] = 1/2 Q(k) T; kernel of the Einstein map 4 at non-null k, 6 at null k.
- proved given (OS): interaction 8 pi G B/Q(k), constant fixed by the stored Newtonian coupling.
- computed (exact at seven angles, degree-four argument): nine channel weights (pi/180)(c_i c_j + 5 t_i t_j),
  c = 1, 3, 12.
- proved given (OS) and the standard collision integral: Gamma = alpha T^8/Mbar^4, alpha = 5789 pi^3/82944000
  for a scalar from (4, 45, 12).
- read from sources on the web: the stored 3997 pi^3/663552000 is 1/16 of the same group's later value; both
  weight chiral fermions as Dirac.
- argued (standard): the mean-field source gives no such rate.
Kill condition B1 fired; the diagnosis is the result's clause (vi).
Ledger: transport-absent.
Next: the stored Fact and its four direct users need their numbers restated (maintainer); the fermion channel's
trace part at next order (trace anomaly); the bath's content on the working branch (second doublet, heavy
neutrinos) at the ceiling temperature.

## C. Slaved field against locality (unlisted)
Route: carry the two refereed steps of the 12 October notes into the store as a model result, with the matter
factor written in the algebra of a completed pair; then state which stored positions it sets against each other.
Established: proved in the model (exact): 172 of 502 spacelike events fail for the slaved field; none with the
free part, to first order; Kubo on the lattice.
Ledger: transport-absent; prior art named.
Next: Leon's choice among the positions; if the field stays without quanta, whether (C1), (C2) supply the
localisation floor under which the failure is unobservable.

## Unexpected links
- The stored first-order theorem (Einstein subject) is the missing lemma of the graviton-rate problem (dark-matter
  area) and of the locality conflict (quantum-fields): non-null momentum fixed by the source, null momentum not.
- The double of the wall-class theorem is "one more anticommuting generator"; that turns Conjecture 7.9's question
  for Clifford multiplication into a question about module extension, which the stored classification answers.
- The curvature coupling of op.curvature-coupling-across-subjects enters the dark towers' heating through
  (1 - 6 xi)^2.

## Decisions for Leon
1. Conjecture 7.9: status and restatement.
2. (OS): a stored premise, or a hypothesis local to the rate result.
3. The three positions (element reading, no quantum of the field, locality).
4. The imported Fact's coefficients and its users' numbers.
