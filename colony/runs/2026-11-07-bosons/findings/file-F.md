# Filer F: the boson result (run 2026-11-07-bosons)

Status: filed, one proposal, gates clean.

## Proposal
`proposals/synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum`
Title: "Fluctuation forms of the tower and density-wave bosons of the null vacuum" (73 chars). Status proved, all
seven clauses proved; no imported Fact is a premise.
Gates: `check4.py` exit 0, 0 errors, 0 warnings (two W413 weak-mutation warnings on the first run fixed by pinning
values); `validate_draft` ok (only I305). Nine check functions, exact Fractions, GA.py, modes from Witt pairs
v = (e + f)/2, w = (e - f)/2 of tower planes; runcheck about 4 s.

One proposal rather than two: a second proposal could not cite the first, and the (N+) part is short once the block
and window results are in place. The (N+) dependence is stated in the one-liner and the reading; clause (vi) is a
statement about the null vacuum, which needs no premise, so no assumes edge is needed.

## Duplicate check (entities read in full)

| RUN.md item | Stored where | Decision |
|---|---|---|
| (i) Holstein-Primakoff [B, B*] = 1 - 2k/N, su(2), CCR only as N -> infinity | field-theory.how-close-tower-comes-ccr@4 (pairing form, B = sum w_c w_d) | Stored for the pairing form. Hopping form derived directly (commutator, su(2), ladder) and shown to be the image of the stored one under the reflection f -> -f of each lower plane; cited. |
| (i) no boson from single fermions | field-theory.no-canonical-commutation-relations-tower@3; synthesis.rung-field-is-odd-... (even doublet obeys CAR) | Partly stored. New: S = N^(-1/2) sum w_i is exactly one fermion mode (S^2 = 0, {S, S*} = 1). |
| (i) QCLT, fluctuations form a Weyl algebra with s(Q,R) = phi([Q,R]) | nothing in the store | NEW, clause (vii): exact identity [F_N(Q), F_N(R)] = (1/N) sum [Q_k, R_k] = s(Q,R) + D_N, mean 0, variance (phi(C*C) - phi(C*)phi(C))/N. Convergence of the fluctuation states (full QCLT) not claimed; Cushen-Hudson, Goderis-Verbeure-Vets cited as prior art only. |
| (ii) [b, b*] = n1 - n2; values 1, tanh, 0 | not stored for hopping; pairing per block in how-close | NEW (iii), with [c, c*] = 1 - n1 - n2 values. |
| "non-degeneracy exactly for non-trace states" | nothing | NEW (iv), stated precisely: block form rank 2[p1 != p2] + 2[p1 + p2 != 1]; zero iff tracial on the block's even algebra (lambda tau_even + (1 - lambda) tau_odd), among product states iff the trace state; never for a pure state. |
| (iii) edge form of the density commutator, value on sea, 0 trace | hawking.current-commutator-exactly-edge-split@4, synthesis.floor-regulator-...@3 (ii),(iii), singularity.bosonisation-bridge-s-wave-sector@8 (1) | DUPLICATE (re-derived and cited). New: converse (acts as scalar q only on edge-clean vectors) and product-state value bottom-sum minus top-sum. |
| (iv) under (N+): filled sea, density modes a Weyl algebra | synthesis.null-vacuum-on-a-horizon-generator@1; Mattis-Lieb Fact synthesis.imported-schwinger-term-and-mattis-lieb-density-algebra@1 | NEW link (vi): restriction of the null vacuum to momentum-band modes is the bands' filled sea (pure product), so window density form non-degenerate (min(q, 2N - q)) and blocks rank 2; on finite excitations of the infinite band [rho_q, rho_q'*] = q delta, [rho_q, rho_q'] = 0, derived from the edge identity without normal ordering. Mattis-Lieb Fact NOT a premise; named in the note as agreement/prior art. |
| dark-energy.imported-s-wave-current-algebra-external, synthesis.imported-local-quasi-equivalence-of-hadamard-states, synthesis.modular-data-on-a-generator-fix-neither-... | read | Not duplicated, not used. |

## Uses (all proved entities)
field-theory.imported-tower-limit@3 (status proved: the planes' CAR), field-theory.how-close-tower-comes-ccr@4,
field-theory.no-canonical-commutation-relations-tower@3, hawking.current-commutator-exactly-edge-split@4,
synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off@3,
synthesis.null-vacuum-on-a-horizon-generator@1. Dropped after Leon's instruction: the Mattis-Lieb Fact and
hawking.imported-quasi-free-states-car-algebra (the product state = quasi-free state of its diagonal symbol is
derived and checked: Wick determinants for all 68 balanced monomials up to degree 3 + 3 on four modes).

## Corrections to RUN.md's wording (for Leon)
1. "Only the trace state degenerates" holds for the block's even algebra among product states, not for density
   modes alone: every product state with balanced edge sums (e.g. constant occupation 1/4) has zero density form
   at every q, while its block form has rank 2. Among general block states the degenerate ones are the tracial
   family lambda tau_even + (1 - lambda) tau_odd, not only the trace state.
2. The thermal value tanh(omega/2T) is for Fermi-Dirac occupations of two levels at -+omega about the chemical
   potential (gap 2 omega), i.e. tanh(eps/2T) with eps the level offset; in that state the pairing mode drops out
   (p1 + p2 = 1), so the thermal block carries one boson pair, not two.
3. The polarised vacuum (lower filled, upper empty) gives the hopping boson only; the pairing form vanishes there.

## Facts to import
None. Per Leon's instruction (7 Nov) the QCLT core, Holstein-Primakoff and the infinite-band canonical relation are
derived in GA in the proposal; Cushen-Hudson, Goderis-Verbeure-Vets, Goderis-Vets, Mattis-Lieb and Holstein-Primakoff
are named in the extraction note as prior art only (HP bibliographic data from memory).

## No imaginary unit
None in the entity, proof or check: the algebra is real (Cl^+(2,2) = M2(R) + M2(R)), the fluctuation form is the real
antisymmetric form omega([X, Y]); the only complex structure is the generator's stored unit I_4 in P = I_4 d/du.

## outside_ga
Not declared. The continuum steps of (vi) (spectral supports of band modes, restriction of the null vacuum) are
Hilbert-space arguments in the stored continuum mode space, as in the null-vacuum theorem; the finite algebra they
reduce to is GA and checked. A referee may ask for outside_ga on (vi): if so, kind: bridge.

## Decisions for Leon
- Whether to add an `assumes` edge to synthesis.n-plus-null-ground-state@12: not needed as filed (clause (vi) is
  about the null vacuum; (N+) enters only in the reading), but positive-null-energy-gives-r-premises carries one
  for comparable use.
- Ledger: (i)-(v), (vii) transport-absent; (vi) transport-convenient. Most of the content is standard many-body
  structure restated in the tower; the new parts are the block rank formula, the converse/product values, the
  null-vacuum band restriction and the exact fluctuation-commutator identity.
