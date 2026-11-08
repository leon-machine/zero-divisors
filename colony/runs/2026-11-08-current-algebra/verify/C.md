# Referee C report: the current algebra (run 2026-11-08-current-algebra)

Blindness kept: I did not read findings/, work/, RUN.md, verify/final/ or the other referee's report (one directory
listing of verify/ showed the file names in verify/final/; no file there was opened). check4 was not rerun. All checks
were run with PYTHONDONTWRITEBYTECODE=1; no __pycache__ is left in proposals/ or work-C/.

Work files: `verify/work-C/indep.py` (independent recomputation, own exterior-algebra code, own so(10) basis),
`verify/work-C/pert/p*.py` (perturbed copies of the checks), `verify/work-C/store/*.json` (premises at the pinned
versions, read with labcli get_claim).

## Summary

| id | verdict | one-line reason |
|---|---|---|
| synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split | SOUND WITH FIXES | Embedding, trace identity, levels, Casimirs, split and central values all re-derived and correct; on the band domain the window H must be replaced by the sea-normal-ordered H, and "central charges" must be marked as defined values (Virasoro relations not derived) in the formal and lay levels. |
| synthesis.window-energy-of-one-generation-is-exactly-the-so10-sugawara-energy | SOUND WITH FIXES | Lemma, u(n) form and A_so = -3 A_N, K = 45/16, lambda = 4 re-derived (independent Majorana basis, and analytically from Casimirs of 16, 45, 120); consistent with c = 15 + 1 = 16 at so(10) level 4. Title omits the number term, and the operator-level identity is the Goddard-Nahm-Olive symmetric-space criterion (prior art not cited); novelty is the exact window form only. |
| synthesis.light-ray-gauge-currents-of-a-generation-do-not-see-its-anomaly-cancellation | OVERSTATED | Clauses (i), (ii), (iv) and the counts are right, but "levels carry no anomaly information" and "the one-dimensional picture cannot tell the 32 apart" are false: the hypercharge zero-mode constant (the sea's hypercharge) and the Y-N central term of u(16) equal tr_{V+} Y, the mixed gravitational anomaly coefficient, which separates 24 of the 32 halvings. Only the cubic conditions are invisible (2 anomaly-free among the 8 with tr Y = 0). |

## Common checks

Premises read at the pinned versions: null-plane-photon-data@1 (iv), (v); exact-window-sugawara@1 (i), (iii);
slot-module-light-ray-arrays-are-weyl-components@3 (ii); cpt-closure@1 (4); spin10-clause-content@2 (ii);
helicity-one-pair-modes@1 (i); light-ray-good-part@5 (iii), (iv); gauge-algebra-minimal-massive-composite@4;
witt-basis-car@1; imported-tower-limit@3; fluctuation-forms@1 (vi); null-vacuum@1 (ii); imported-anomaly-coefficients@1.
Each says what the proposals use. In particular stored null-plane (iv) gives the exact window commutator and its
edge-clean form `delta_yz j^{xu} - delta_xu j^{zy} + m delta delta delta`; stored (v) gives `[H, j_m] = -m j_m` exactly for
the level operator; stored exact-window (i) gives the one-channel identity that proposal 2 (ii) reduces to at n = 1 (I
checked the reduction: `2H = 2T + N^2` with `H = sum (j + 1/2) n_j` is the stored `T = sum j n_j - N(N - 1)/2`).
spin10 (ii) gives 32 sign patterns times any pair of complementary neutral lines (a continuum of lines, not two).

House style: no em dashes, no "honest", no "load-bearing" in any of the three; macros \gl, \su, \uu, \so, \C, \Z, \ip
are in notation.yaml; no imaginary unit (proposal 3's check is in GA with J = g_1 g_2; proposal 1 checks the
anti-Hermiticity over span{1, J} in GA; proposal 2 needs only rational Casimir tensors).

All three checks pass (proposal 1: 16 s; proposal 2: 28 s; proposal 3: under 1 s).

## 1. synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split

**Proof steps.** (i) homomorphism, adjoint, `tr rho(X) = 8 tr X`, preservation of V_+, hypercharge list: correct.
(ii) the trace computation `tr(rho X rho X') = 8 sum X_aa X'_aa + 4 sum_{a != c} X_aa X'_cc + 4 sum_{a != b} X_ab X'_ba
= 4 tr(XX') + 4 trX trX'` is right (8 even states contain a given mode, 4 contain two given modes, 4 contain a and not
b). Levels: su(3) and su(2) at 4 against the fundamental trace (which is the root-normalised form), `tr rho(Y)^2 = 10/3
= 4 tr_5 Y^2` with the normalisation stated. Trace-orthogonality and tracelessness give the vanishing mixed central
terms with N. (iii) I redid the Sugawara commutator: the central part gives `-2m X_m`, the identity
`P_{a,b} + P_{b,a} = lambda X_{a+b}` from invariance and symmetry of the Casimir tensor, and the telescoping
`-2 sum_{q=1}^{m} P_{m-q,q} + P_{0,m} - P_{m,0} = -m lambda X_m` are correct; so `[H_f, X_m] = -m X_m`. The locality
bound `min(s, L - s) >= 3(K + |m|)` follows from the stated bookkeeping (H_f on a j-local vector uses q <= 2j - 1 and
gives (3j - 1)-local vectors; window and band operators agree for `|q| <= min(s, L - s) - j`). (iv) the level-two norm
argument `J(t_b)_1 v = (2 + lambda) J(t_b)_{-1} Omega` is correct, as is the u(16) total `255/34 + 1/2 = 8`.

**Numbers, my own route.** `lambda = 2h/k`: su(3) 6/4 = 3/2, su(2) 4/4 = 1. `c = k dim/(k + h)`: su(3)_4 = 32/7,
su(2)_4 = 2. The coset value by a different route: c(so(10)_4) = 4*45/12 = 15 (see proposal 2), and
15 - 32/7 - 2 - 1 = 52/7, matching `16 - 32/7 - 2 - 1 - 1`. `indep.py` recomputes the gl(5) identity on all 625 pairs
(0 failures) and `tr rho(Y)^2 = 10/3`, `tr rho(Y) = 0` with its own exterior-algebra code.

**Perturbations.** p1a (Y with -1/2 on the third pair mode, so not traceless): four of five checks fail (traceless,
hypercharges, levels, split, orthogonality). p1b (lambda + 1/4 on the nonabelian factors): Casimir, central-value, split
and level-two checks fail. p1c (localised window shrunk to L = 4, s = 2): all checks still pass, so the sampled
localised vectors do not test the bound; the bound is proved, not run (the coverage file says so), and the failing edge
vector is a 2-local vector in that window, consistent with the statement.

**Hidden hypotheses, level claims.** Abelian normalisation is stated at every level (formal (ii), reading, technical,
lay, one-liner). The I4-to-J matching is stated once, in the proof of (i). Not a Yang-Mills claim at any level ("not the
four-dimensional gauge field" in reading and lay). Two gaps:
- Formal (iii) asserts the relations "on the domain D of finite excitations of the band", but H is defined in the
  formal preamble as the window operator `sum (k + 1/2) n`, which is infinite on D. The proof says "zero modes counted from
  the sea" but never replaces H.
- "Central charges" (lay) and "the coset carries c_c = 52/7" (formal (iv)) read as Virasoro central charges; the
  formal text defines c_f as twice the level-two norm, and only the extraction note says the Virasoro relations are not
  derived.

**Overlap.** With proposal 3: (i) and the trace form 4 tr_5, tr Y^2 = 10/3 are also proved there (proposal 3 (i), (iii),
(iv)). With proposal 2: H_c here equals H_so(10) - H_su(3) - H_su(2) - H_Y exactly on every window vector (proposal 2
(iv)), which explains the coset value 52/7 as the so(10)_4 coset. No stored duplicate (searched the store for the
Sugawara split, 10/3, so(10) level).

**Verdict: SOUND WITH FIXES.** Required fixes:
1. Formal (iii): say that on D, H means the sea-normal-ordered `H_inf` of exact-window-sugawara (iii) per channel (and
   the zero modes `J(M)_0` are counted from the sea), and that the window statement is for the window H.
2. Formal (iv) and lay: add one sentence: "The Virasoro relations of the L^f are not derived; c_f is defined as
   2 dim f/(2 + lambda_f), equal to twice the level-two norm, and would be the central charge if they hold." In the lay,
   replace "(central charges)" with "(central values, the central charges if the factor energies obey the Virasoro
   algebra, which is not shown here)".
3. Cite the other two proposals once both are accepted: the coset remainder is a function of the so(10) currents
   (proposal 2 (iv)); the embedding and trace form are shared with proposal 3.

## 2. synthesis.window-energy-of-one-generation-is-exactly-the-so10-sugawara-energy

**Proof steps.** (i) The reordering `j^{xy}_{-q} j^{zu}_q = delta_yz sum c*_{x,k+q} c_{u,k+q} - sum c*c*cc`, the
weight count `2l + 1` (q = 1..l with weight 2, q = 0 with weight 1), the unique labelling of each level-conserving
quadruple with k_alpha >= k_gamma, the relabelling (alpha, beta, gamma, delta) -> (beta, alpha, delta, gamma) using the
symmetry of C, and the gamma-delta antisymmetrisation are all correct; this is exact on every window with no edge term.
(ii) `K = (n + 1)1`, `A = 0` correct; n = 1 reproduces the stored identity. (iii) from (i) with K and A:
`H_so = (15/16)H + Q(Delta)/64`, `H_N = H/16 - Q(Delta)/64`, sum H. Correct. (iv) correct but is a direct corollary.

**Key numbers, my own route.** In `indep.py` I built so(10) from the 45 Majorana bilinears gamma_p gamma_q (a
different basis from the proposal's a*a, a*a*, aa), restricted to the even half by my own code, and computed the
trace-dual Casimir tensor: C symmetric, `K = 45/16` (scalar), `A_C/Delta = {-3/16}` on all 16^4 quadruples,
`lambda = 4`. Analytically, with Casimirs (lambda, lambda + 2 rho) for D5: C2(16) = 45/4, C2(45) = 16, C2(120) = 21;
scaling to the trace form (factor 1/4) gives adjoint 4 and the eigenvalue of sum M^A (x) M_A on Lambda^2 16 = 120 as
(21 - 2*45/4)/8 = -3/16. Level: lambda = 2h/k with h = 8 gives k = 4 (directly: tr_16 H_alpha^2 = 8 against the
root-normalised value 2). Central-charge counting: c(so(10)_4) = 4*45/12 = 15, plus 1 for the number current equals 16,
the value for sixteen complex chiral channels, and equals c(su(16)_1) = 15. The identity is consistent with the conformal
embedding so(10)_4 in su(16)_1.

**Perturbations.** p2a (drop the 20 pair bilinears, keep the so(10) coefficient 1/6): the operator identity fails on all
seven states. p2b (coefficient 1/(1 + lambda)): fails on all seven states. The lemma and u(n) checks already include
built-in negative controls (coefficient n in place of n + 1 fails).

**Overclaiming and prior art.** The title says the energy "is the so(10) Sugawara energy"; it is the so(10) energy
plus the number part H_N (the formal statement and one-liner are right). Conformal embeddings and so(10)_4 in su(16)_1
are cited as prior art; but the operator-level statement (the free-fermion Sugawara energy equals the subalgebra's
Sugawara energy exactly, because the quartic term cancels) is the Goddard-Nahm-Olive criterion (P. Goddard, W. Nahm and
D. Olive, Phys. Lett. B 160 (1985) 111, "Symmetric spaces, Sugawara's energy momentum tensor in two dimensions and free
fermions"; existence and journal confirmed via MaRDI/DOI 10.1016/0370-2693(85)91475-3, volume and page from memory). Its
condition is in substance A_C proportional to Delta, here the symmetric space E6/(SO(10) x U(1)) with 78 = 45 + 1 + 16 +
16bar (from memory). So "New here ... the exact window form of the so(10) equality, proved by the finite tensor
identity" should credit the tensor identity as classical and claim only its exact finite-window form (lemma (i) with no
edge term). No grand-unification claim in formal, technical or reading ("not claimed: that the so(10) currents are
gauge currents"); the lay "the forty-five-dimensional symmetry ... contains the Standard Model forces" could be read as
a unified gauge symmetry. Units: only rational Casimir tensors enter, no I4 matching needed. No stored duplicate.

**Verdict: SOUND WITH FIXES.** Required fixes:
1. Title: "On every window one generation's channel energy is the so(10) Sugawara energy plus the number term" (or
   "...the su(16) Sugawara energy of one generation equals the so(10) one on every window").
2. Prior art: add Goddard, Nahm and Olive (1985) as the operator form of the equality (cited from memory as to volume
   and page), and change "New here" to: the window quadratic-form lemma (i) and the exact window form of (iii), with the
   tensor identity A_so = -3 A_N recognised as the classical symmetric-space condition, computed exactly here.
3. State the level once in (iii): "so(10) at level 4 (lambda = 2h/k, h = 8), c = 15".
4. Lay: after "This symmetry contains the Standard Model forces" add "; here it is a symmetry of the currents along the
   light ray, not a unified gauge symmetry".

## 3. synthesis.light-ray-gauge-currents-of-a-generation-do-not-see-its-anomaly-cancellation

**Proof steps.** (i) block diagonality, anti-Hermiticity, u(16) not so(32): correct; the partner blocks -M^T via the
top-degree pairing and the derivation property with tr t = 0: correct; traces on components correct. (ii) the
reflections: f -> -f for u = f, swaps for u = e - e' (Q = 2) and f - f' (Q = -2); 2L factors so the signs cancel;
`u u~ = (-1)^L 2^{L/2} (-2)^{L/2}` (16 at L = 4); `phi(a*_k) = a_{L-1-k}`, `phi(n_k) = 1 - n_{L-1-k}`; centred H fixed;
edge-clean sets and the sea fixed; `phi(a*_{x,k} a_{y,k+q}) = -a*_{y,k'} a_{x,k'+q} + delta_xy delta_q0`, so the
currents map to those of -M^T plus `delta_q0 L tr_C M`. All correct. (iii) the counts: I enumerated the 32 sign patterns
independently: the quadratic traces (T3^2, H3^2, Y^2) = (2, 2, 10/3) for all 32, and exactly 2 are anomaly-free. (iv)
2, 10/3, 16/3, 3 : 5 : 8, 120, 48, gcd 1: correct.

**Perturbations.** p3a (f -> +f' in phi): the reversal check fails. p3b (drop the signs eps(S) in the partner basis):
the partner-block check fails.

**The overstatement (decisive).** The constant `delta_q0 L tr_C rho_+(T)` in (ii) is not a harmless normalisation: for
the hypercharge it is the change of the sea's hypercharge, which is `(L/2) tr_{V+} Y J` for the halving V+; and in the
u(16) current algebra of the same channels the mixed central term between J(rho_+ Y) and the number current N is
`m tr_{V+} Y J`. Both equal the mixed gravitational anomaly coefficient sum Y. `indep.py` finds tr_{V+} Y in
{-6, -4, -2, 0, 2, 4, 6} over the 32 patterns, zero for exactly 8. So the gauge currents with their sea (through the
zero-mode constant), or the u(16) current algebra with N (through a quadratic trace tr(rho(Y) 1)), separate 24 of the
32 halvings; among the 8 with tr Y = 0 the constant vanishes, phi_C is an exact isomorphism of currents, energy and sea,
and 2 of the 8 are anomaly-free. What is true: no quadratic trace on g, and no structure of the gauge currents with
energy and sea beyond the linear datum tr_{V+} Y, sees the cubic conditions. The proposal's own formal (iii) sentence
"anomaly cancellation is not a function of the gauge currents along a generator with their energy and sea" remains true
(witnessed by the 8), but the following do not:
- one-liner: "levels carry no anomaly information";
- extraction note (b): "the whole window current algebra ... is the same for all 32 ... so no relation between levels and
  anomaly cancellation per generation exists" (the whole u(16) algebra includes N);
- lay: "of which thirty are inconsistent, and the one-dimensional picture cannot tell them apart";
- reading and formal (iii): "four-dimensional anomaly cancellation is a cubic condition" and "each anomaly coefficient is
  a weighted cubic trace" (the mixed gravitational coefficient is linear).
The stored-adjacent proposal 1 itself records the correct statement: tr rho(Y) = 0 enters as the vanishing of the
hypercharge-number central term.

**Other points.** "32 halvings and either neutral line": the neutral block admits any line (spin10 (ii)); say "32 sign
patterns, any neutral line". The classical fact behind (iii) (a representation and its conjugate have equal quadratic
indices and opposite anomaly coefficients) should be listed as prior art. Units: the I4-to-J matching is stated once in
the formal preamble, with the other sign discussed. Overlap with proposal 1: (i) first sentence and the trace form
4 tr_5, tr Y^2 = 10/3, and the abelian-normalisation remark duplicate proposal 1 (i), (ii); the new content here is the
partner blocks, phi_C and the halving comparison. No Yang-Mills or GUT overclaim (the 3/8 ratio is stated as a ratio of
traces, not as a Weinberg angle).

**Verdict: OVERSTATED.** True weaker statement at each level:
- Formal (iii): "...the same for all 32 sign patterns up to phi_C and the zero-mode constant L tr_C rho_+(Y); that
  constant is the change of the sea's hypercharge (L/2) tr_{V+} Y, and tr_{V+} Y is also the mixed central term of
  J(rho_+ Y) with the number current N. It vanishes for exactly 8 of the 32 patterns, the mixed gravitational condition;
  on those 8 the gauge currents, energy and sea are isomorphic, and exactly 2 of them are anomaly-free. Hence the linear
  anomaly condition is visible along one generator and the three cubic conditions are not; every trace quadratic in g is
  the same for all 32." Replace "each anomaly coefficient is a weighted cubic trace" by "each anomaly coefficient is a
  weighted trace (linear for the mixed gravitational condition, cubic for the others)".
- Reading: "four-dimensional anomaly cancellation has one linear condition, seen along a generator as the sea's
  hypercharge and the Y-N central term, and cubic conditions that need the channel weights".
- One-liner: "...the same for all 32 gauge-commuting halvings up to a hypercharge constant equal to tr Y; that constant
  sees the mixed gravitational condition (8 of 32 pass) but no quadratic datum sees the cubic conditions (2 of those 8
  are anomaly-free); the abelian level is a normalisation."
- Lay: "...cannot tell apart the eight arrangements whose total hypercharge is zero, of which six are inconsistent."
- Extraction note (b): restrict "the whole window current algebra" to "the gauge currents with energy and sea, up to the
  hypercharge constant", and replace "no relation between levels and anomaly cancellation" by "no relation between the
  levels of g and the cubic anomaly conditions; the linear condition is the Y-N mixed level".
- Also: "32 sign patterns, any neutral line"; add the classical conjugate-representation fact to prior art; cite
  proposal 1 for the embedding and trace form if both are accepted.

## Literature verified

Schellekens and Warner, "Conformal subalgebras of Kac-Moody algebras", Phys. Rev. D 34 (1986): journal and volume
confirmed (OSTI record 6982697), first page 3092 not displayed. Bais and Bouwknegt, "A classification of subgroup
truncations of the bosonic string": title confirmed (INSPIRE record 18571), journal details not loadable. Goddard and
Olive, "Kac-Moody and Virasoro algebras in relation to quantum physics": title confirmed as their standard review,
journal, volume and page not verified. Sugawara, "A Field Theory of Currents": title confirmed (Scilit), volume and page
not verified. Goddard, Nahm and Olive (1985), recommended above: authors, title, journal and DOI confirmed (MaRDI).
GKO 1985, Kac 1968, Moody 1968, Frenkel-Kac 1980, and the anomaly references of proposal 3 were not checked; all are
marked "cited from memory" by the proposals and used as prior art only.
