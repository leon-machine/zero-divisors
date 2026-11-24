# Fixes H-A, run 2026-11-24-three-routes

## synthesis.wall-conjugation-invariance-on-a-radiation-type-descent-floors-the-dirac-deposit-and-selects-none
Verdict: SOUND WITH FIXES. All eight fixes applied, in place, at every level. Nothing rebutted.
runcheck: 7/7 PASS (one check added). check4: pending (orchestrator). validate_draft: pending (orchestrator).

What changed
1. Class of states (fix 1). Formal, proof, technical, one-liner, note: clauses (i) to (vi) are now for states that
   are homogeneous, isotropic, diagonal in helicity with the same vector in the two helicities, and
   charge-symmetric. The reason is stated: the antilinear conjugation theta = cW carries the sector of momentum k
   to a sector of momentum -k. (i)(b) now says theta induces O_A between paired sectors and W with the
   particle-hole exchange induces it within each sector; (i)(c) says "only the tracial state" holds in the
   isotropic class. New clause (vii), proved, with a new exact check (check_pair_bound_without_isotropy): without
   isotropy invariance is v_{-k}(0) = O_A v_k(0), the per-sector floor fails (the pair (s_out, s_in) has occupations
   0 and q), and n_k + n_{-k} = 1 - sqrt(1-q) v_k(0).m >= 2 n0 with equality only at v = m; so the floor state still
   has the least number in every pair. For W with the exchange, (ii), (iv)(b), (vi) hold sector by sector without
   isotropy. The referee's derivation of the pair bound was reproduced and is the one in the proof.
2. One-liner (fix 2): names the class; adds the pair bound, "given the same Fact" for the wall-instant vacuum, and
   that the background is prescribed.
3. Argued, not proved (fix 3). Formal (v)(b): the tracial state is not Hadamard, proved for mu = 0 (stored moment
   criterion), argued for mu > 0 (its two-point function is half the anticommutator distribution, whose wave front
   set contains both C+ and C-; no massive necessity criterion is stored). Formal (iv)(c), technical, lay, proof:
   the Fock states of the energy-reversing reflection are "argued, not proved" not Hadamard. "(CW) neither implies
   (HD) nor is implied by it" now reads "given the Fact", and the proof says which half rests on what.
4. Number density (fix 4). Proof (iv)(c): 0.012760 (mu/pi)^(3/2) is the density summed over the two helicities;
   per sector 0.006380 (mu/pi)^(3/2). Labelled computed, with the method. My attack findings had the same slip;
   a correction paragraph is appended there. No floating-point number is in the formal, technical, lay or
   one-liner text.
5. Lay (fix 5): "well behaved, given a standard theorem on such states"; "would also make the two sides equally hot
   (argued)"; "argued not to be well behaved" for the half-filled state.
6. Prior art (fix 6). Credit moved into the formal text at the end of (iv)(c): the pure-state profile, the
   transition probability and the least-number choice are Boyle, Finn and Turok's, arXiv:1803.08930, Eqs. (3.48),
   (3.49), (5.13); proof and note add (5.15), (5.16) for the number density. Worded "locators confirmed in review
   against the arXiv text" (store text may not name a referee). "Read in part, through a summarising fetch" is
   gone. The PRL is cited by journal reference only, flagged from memory; no arXiv number is asserted for it.
7. Coverage (fix 7): coverage.yaml added (seven functions); the Weber function is marked "exponent bookkeeping
   only", the value of q "proof-only (confirmed numerically outside the check)"; the check's docstring says the same.
8. Cross-reference (fix 8), text only, not in uses or lineage: formal (after the hypotheses), technical, proof
   Reading, note and a flag say that (RD) and (DF) prescribe the background, that with the expected stress as the
   source the exact radiation field does not reach the wall given the hypotheses (A) and (E) of the result filed
   alongside (synthesis.trace-anomaly-leaves-no-exact-radiation-field-at-a-tame-wall), and that the present result
   is for a test field on a prescribed background. The Reading adds that W needs M exactly odd at the wall.
Bridge entries
- B4, checked against the store and it holds: note.synthesis.n-plus-orientation-datum (v1) says the datum (N+)
  assumes "is carried by the Hadamard deposit premise where that premise reaches", and (O1) on the problem record
  says lifting the deposit off one half needs it. One sentence added to the Reading: the bundle (CW) + purity +
  least occupation + orientation does not source the datum; it trades (HD) for the same datum and three further
  clauses. Part (b) and (c) of B4 concern the positivity problem and are not mine.
- B6, checked (dark-matter.p2-indifference v2 is scoped to sector labels, not thermal states): one sentence added
  to the Reading: the mirror tension is a cost of (CW) alone and touches no stored premise.
Title unchanged (79 characters; names (CW) and the radiation-type descent; the one-liner names all three hypotheses).

## Repin on acceptance
None: every pin is to a stored version. If the trace-anomaly result is accepted, its mention "filed alongside" in
the formal, technical, proof and note can become a \claimref and a lineage link.

## Next steps (not pursued)
- Make the tracial clause proved for mu > 0: needs the wave front set of the causal propagator as a stored Fact.
- Necessity half of a massive moment criterion.
- The referee's estimate (argued, his): the Landau-Zener window |eta| ~ 1/sqrt(m a') is far from the Planck region
  where the trace-anomaly correction is of order one, so the floor would be insensitive to it at order
  sqrt(m t_P), while the reflection W needs exact oddness at the wall. Not computed here.
- B6's lead: under (CW) with a co-present mirror a cold mirror survives only among non-quasi-free states.
- Scalar field under (CW); the Riemannian far side for the massive Dirac field.

## Decisions for Leon
1. (CW): recommendation unchanged, do not adopt. Restated after B4: the bundle (CW) + purity + least occupation +
   orientation gives a number-free Hadamard vacuum part but does not derive the orientation datum; it replaces
   (HD) by the same datum plus three clauses, so it is not a simplification of the premises.
2. Imports the entry would cite as Facts (maintainer-only): the Weber-function facts (the referee recommends DLMF
   section 12 with equation numbers) or Zener 1932; Boyle, Finn and Turok arXiv:1803.08930 as prior art; the wave
   front set of the anticommutator distribution, which would turn the tracial clause from argued to proved.
3. The PRL's arXiv number: the referee recalls 1803.08928; a web search result title I saw agrees, but I did not
   open it. Not asserted in the entry.
4. (RD), (DF), (A), (E) do not hold together. If any are stored as postulates, a result resting on all four should
   be flagged; until then the two text cross-references are the record.
5. Whether (DF), the far side as the other sign of conformal time, is a reading the series wants at all, given the
   trace-anomaly result.

## Second pass
Second referee (verify/R-2.md, item 2): SOUND WITH FIXES; clause (vii) confirmed by an independent route. Three
fixes applied in place, entity.md only; nothing rebutted. runcheck 7/7 PASS (check unchanged). check4: pending
(orchestrator).
1. One-liner and technical level: the class now reads "homogeneous, isotropic, diagonal in helicity with the same
   vector in both helicities, charge-symmetric".
2. One-liner: "without isotropy, for the conjugation with charge conjugation, only the pair bound holds (the floor
   holds sector by sector for the reflection followed by the exchange of particles and holes)".
3. Clause (vii): "where q < 1" added before the displayed bound (the unit vector along s_in(0) + s_out(0) is
   undefined at q = 1).
Repin, next steps and decisions for Leon: unchanged.
