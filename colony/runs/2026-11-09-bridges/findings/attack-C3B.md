# Attack C3B (cluster C3, constructive), run 2026-11-09-bridges: target Z2

Labels: proved / computed / argued / conjectured; "memory" = literature cited from memory, unchecked.
Status of this section: PRE-REGISTRATION, written before any computation of this run (orientation by lookup and
hand algebra only). Results are added below it and kept current.

## Z2. The tensor product in the eviction comparisons replaced by the geometric-algebra split

### Orientation (lookup)
Stored results concerned, with pinned versions:
- singularity.eviction-window-thermal-product-radiation-entropy v7 (the eviction theorem; window state written
  as a tensor product of diag(c^2, s^2)).
- synthesis.eviction-keeps-one-replica-saddle v3 (Renyi 2; clause (iii), (iv) carry the Haar column
  (m+n)/(mn+1); cites synthesis.imported-haar-average-purity by claimref only, not in uses).
- synthesis.eviction-keeps-one-of-catalan-many-replica-saddles v3 (every Renyi index; uses
  synthesis.imported-haar-average-purity@2 and synthesis.imported-haar-moments-of-random-pure-state@2).
- synthesis.eviction-deficit-against-page-deficit v4 (von Neumann; Page column from
  singularity.imported-page-average-entropy-subsystem@1).
- singularity.assembled-page-curve-up-typicality v3 (Page-typical assembly; hypothesis (ii) is typicality on
  radiation (x) partner-mode space).
- singularity.descent-parity-average v5 (E = parity average onto the even algebra).
- Klein twist in the store: tower.commuting-copies v5 (twisted generators x omega_1...omega_k give commuting
  subalgebras and the tensor product), synthesis.even-slots-need-a-spectator-generator v3 (iii) (s -> s Gamma_W),
  synthesis.joint-clifford-clause-is-a-klein-convention-on-the-composite-space v1 (the twist a(-1)^k, uniqueness
  up to a unit). Mode algebra: null pairs of Cl(m,m) satisfy the CAR as vectors
  (tower.ladder-pairs-satisfy-car-vectors v4); mode parity 1 - 2 v w = e f.
- Sibling proposals (cannot be cited; intended citations): synthesis.finite-normaliser-averages-leave-the-haar-
  moments-at-order-four-and-on-a-parity-sector clause (iv) (the sector form of the Haar moments,
  2 sum (dA/2)^#(dB/2)^# / prod(D/2 + l), and the sector mean purity (dA+dB)/(dA dB+2)); synthesis.quarter-turn-
  rotors-of-the-even-subalgebra-form-a-state-design-of-order-three (derived second moment). Not re-filed here.

### Routes
 R1 (the target's own): modes as null pairs of Cl(m,m); a subsystem = the sub-Clifford algebra Cl(A) of a subset
    of modes; reduction = the blade projection E_A; relation to the tensor product by the stored commuting-copies
    twist (B' = Cl(B) twisted by the parity blade Gamma_A commutes with Cl(A), Cl(A) (x) B' = Cl(m,m)). Delivers
    the dictionary on reduced states. Needs: partial trace over B' = E_A (commutant argument). Fails if the
    twisted and untwisted reductions differ on the even states the store uses.
 R2 (other subject): the descent's conditional expectation (singularity.descent-parity-average) and the
    superselection reading: restrict to even states first, then every local algebra is the even part and the
    two splits share it. Delivers the "which quantities agree" clause directly. Fails for states that are not
    even (expected: a pure non-even state has unequal spectra on the two sides of the GA split).
 R3 (own): work on a parity sector as a Hilbert space (even x even) + (odd x odd), block decomposition of a
    sector state, Beta-distributed block weight: gives the mean entropy of the sector exactly from Page's Fact
    applied to the two blocks, and the exact rational difference from Page's value. Needs the Gaussian form of
    the invariant measure (background).
Choice: R1 for (a), (b); R2 for the agreement clause and the counterexample; R3 for the recomputed von Neumann
comparison. Renyi comparisons from the sector form of the Haar moments (sibling's clause; re-derived only as a
lemma where a self-contained proof is needed).

### Kill conditions (registered before computing)
 K-Z2 (the run's): an eviction result whose LEADING term changes on the GA split (the eviction-side purity
      max(2^-j, 2^-c), the flat spectrum, S_R = sum h_k; or the leading comparison terms: ln 2 at Renyi 2,
      ln C_n/(n-1) at index n, half a nat at the crossing). If any fires, that result fails and is reported so.
 K-a: the blade projection E_A differs from the partial trace of the Klein-twisted tensor split on some even
      state (then the GA split is not the tensor split on the store's states and (b) has no clean form).
 K-b: an even pure state with different nonzero spectra of its two GA reductions (Schmidt symmetry lost): then
      "tr rho_R^2 = tr rho_L^2" in the stored proofs fails on the GA split.
 K-c: the eviction state of the store is not even (does not commute with the total parity): then the sector
      column does not apply to it and bridge B6's reading fails.
Predictions written before computing (hand algebra): none of K-Z2, K-a, K-b, K-c fires. E_A equals the twisted
partial trace for EVERY state; E_B differs from it exactly on the odd-odd blades, so for even states all
reductions agree and a non-even pure state breaks Schmidt symmetry on the GA split. Eviction clauses survive
unchanged; what changes is the random-state column when it is read on a parity sector: Renyi 2 at the crossing
2d/(d^2+2) in place of 2d/(d^2+1); index n: limit C_n unchanged, a permutation of genus g weighted 4^g relative
to the unrestricted value; von Neumann: mean entropy sum_{k=n/2+1}^{mn/2} 1/k - (m-2)/(2n) in place of
sum_{k=n+1}^{mn} 1/k - (m-1)/(2n), deficit smaller than Page's by a rational amount between 1/(2mn) and
1/(2(mn+1)) + 1/(2n(n+1)); at m = n = 2 the values 1/2 against 1/3.

### Results
First computations (scripts work/C3B/z2_explore.py exact, z2_mc.py float sanity only; then work/C3B/p1/check.py):
- K-a did not fire (computed at 1|1, 1|2, 2|1 modes; proved by blade count): the blade projection onto Cl(A) is
  the partial trace of the twisted tensor split for every element. The projection onto Cl(B) differs from the
  twisted one only on odd blades of Cl(B) and on the parity blade of A times odd blades of Cl(B); none occurs in
  an even element.
- K-b did not fire for even states (computed: an even pure state of three modes, moments 2, 3, 4 equal on both
  sides of every split, e.g. 5/9, 1/3, 17/81). It fires, as predicted, for pure states that are not even:
  rho = (1 + e_1 - f_1 e_2 + f_1 e_1 e_2)/4 has purities 1 and 1/2 on the two sides; a generic three-mode one
  117/200 against 141/200.
- K-c did not fire: the pair state c|00> + s|11> is the even idempotent
  (1 + p p')(1 + r p)/4 + c s (w w' + v' v), pairs commute, their product is the Fock state with product
  amplitudes, commutes with the total parity; window reduction = product of (1 + r_k p_k)/2; purity
  prod(c^4 + s^4) on both sides; flat spectrum at zero weight, also after an eviction.
- K-Z2 did not fire: no leading term changes (see the fate table below).
- Sector columns (exact): Renyi 2 (m+n)/(mn+2); index n at the crossing
  d^{n-1}<tr rho^n> = sum_g N_g (4/d^2)^g / prod_{l<n}(1 + 2l/d^2), N_0 = C_n (limit unchanged), against
  sum_g N_g d^{-2g} / prod(1 + l/d^2) unrestricted (N_1 = 0, 1, 10, 70, 420 for n = 2..6); sector below
  unrestricted below C_n d^{1-n} for n <= 6, d <= 32 (computed). Von Neumann: sector mean entropy
  sum_{k=n/2+1}^{mn/2} 1/k - (m-2)/(2n) (1/2, 7/12, 271/280 at (2,2), (2,4), (4,4); float sampling agrees to
  three digits), above Page's by a rational amount between 1/(2mn) and 1/(2(mn+1)) + 1/(2n(n+1)).

### What was established (final)
- proved: (a) the split (sub-Clifford algebras of sets of modes of Cl(l,l), graded-commuting; blade projection E_A
  is the trace-preserving conditional expectation, positive; purity d_A d_B^2 <E_A(rho)^2>_0).
- proved: (b) the Klein twist: generators of B times the parity blade Gamma_A give B' commuting with Cl(A),
  Cl(A) (x) B' the ordinary tensor product (tower.commuting-copies); the twist is unique up to sign (blade count
  with the stored form b; same count as clause (iv) of the joint-Clifford-clause result); d_B E_A is the partial
  trace over B' for EVERY element; d_A E_B equals the other partial trace exactly on elements with no component
  on odd blades of Cl(B) or Gamma_A times them, so on every even element.
- proved: even states: both reductions are the tensor-split ones; pure even: equal moments on both sides, one
  parity sector (not a tensor product). Counterexample for non-even pure states (purities 1 and 1/2): computed.
- proved: products of even states of disjoint mode sets are products in the algebra (no twist); the pair state
  formula; hence every eviction-side clause transfers verbatim.
- proved (given the imported all-moment Fact on the sector): sector moments, crossing coefficient
  sum_g N_g (4/d^2)^g / prod(1 + 2l/d^2) -> C_n; lower bound d^{1-n}. computed only: sector < unrestricted <
  C_n d^{1-n} for n <= 6, d <= 32. (The moment formula itself is the sibling C1B's clause (iv); rederived as a
  lemma, not claimed as new.)
- proved (given Page's Fact on a block and background: Gaussian form of the invariant measure, Beta moment):
  sector mean entropy sum_{k=n/2+1}^{mn/2} 1/k - (m-2)/(2n); exact rational excess over Page's value with
  1/(2mn) < Delta < 1/(2(mn+1)) + 1/(2n(n+1)); deficit bounds
  (m-2)/(2n) + 2(m-1)/(2mn+m+1) < delta_sec < m/(2n) - 1/(mn); crossing deficit in (2/5, 1/2) for m >= 4.
- argued: that the sector column is the right "typical" column (bridge B6: after the descent's parity average
  the pure states are sector states). The stored abstract-tensor statements stay true as mathematics.
All transport-absent (algebra of the modes and counting), the eviction results being the series' own.

### Fate of each stored result on the GA split (even states)
| stored result | fate |
|---|---|
| singularity.eviction-window-thermal-product-radiation-entropy v7 | survives unchanged (all four clauses); "tensor product of marginals" is the product prod (1 + r_k p_k)/2 of commuting even elements; S_R = S_L by evenness. Wording only, no version change needed. |
| synthesis.eviction-keeps-one-replica-saddle v3 | (i), (ii), (v) unchanged. (iii), (iv): changed subleading term: random-state value (m+n)/(mn+2), crossing 2m/(m^2+2), gap ln 2 - ln(1 + 2 m^-2) (order m^-2 term doubled); leading ln 2 unchanged. Corrected version filed (v4). |
| synthesis.eviction-keeps-one-of-catalan-many-replica-saddles v3 | (i), (ii), (iv) unchanged (limit C_n, gap ln C_n/(n-1), half nat at n -> 1). (iii): changed subleading terms (genus weight 4^g, denominators d^2/2 + l). Corrected version filed (v4). |
| synthesis.eviction-deficit-against-page-deficit v4 | (ii), (iii) unchanged. (i): changed subleading term; the stored lower bound (m-1)/(2n) FAILS on a sector at m = 2 only (delta_sec < 1/(2n) there) and holds for m >= 4; positivity, "< 1", half a nat at the crossing and the closing interval (2/5, 1/2 + 1/m) for m >= 4 survive. NOT filed (cap of three); exact replacement text is clause (vii) of the new claim. For the maintainer. |
| singularity.assembled-page-curve-up-typicality v3 | survives unchanged at the order it states; hypothesis (ii) would read "typical in its parity sector". Wording only. |
| singularity.descent-parity-average v5 | used, not changed (evenness = invariance under it, with sigma the product of mode parities). |
| singularity.imported-page-average-entropy-subsystem v1 | stays (used on the two blocks of a sector). |
| synthesis.imported-haar-moments-of-random-pure-state v2 | stays (used on the sector). |
None fails; K-Z2 did not fire.

### Proposals (all: check4 exit 0 with no findings on the registered folder, validate ok, registered)
1. synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product (new, v1): (a), (b),
   the dictionary, the recomputed columns, the fate list.
2. synthesis.eviction-keeps-one-replica-saddle v4 (restatement; all four stored files kept; credit and
   amendments entries added; new check function; claimref to the retired Fact removed from the proof).
3. synthesis.eviction-keeps-one-of-catalan-many-replica-saddles v4 (restatement; all three stored files kept;
   synthesis.imported-haar-average-purity dropped from uses and from the check; new check function).
Logs: verify/final/check4-<id>.log, <id>.validate.json; drafts in work/C3B/.

### Dependants of the retired synthesis.imported-haar-average-purity
- store: synthesis.eviction-keeps-one-of-catalan-many-replica-saddles v3 (uses edge @2, premise() in its check,
  claimref in proof (iii)): all removed in the filed v4. synthesis.eviction-keeps-one-replica-saddle v3 (claimref
  in proof (iii) only, not a uses edge): removed in the filed v4; its extraction notes still name the Fact as
  history. synthesis.imported-haar-moments-of-random-pure-state v2 (claimref in its formal text, "At n = 2 this
  is Lubkin's", and its note). store/open_problems.yaml op.island-dictionary (claimref at line 2986, entity list
  at 3032).
- proposals of this run: synthesis.finite-normaliser-averages-... (uses @2, premise() in check, claimrefs in
  formal and proof) and synthesis.quarter-turn-rotors-... (check, entity, proof mention it): both must be
  repointed before the Fact is tombstoned. The new claim of this attack does not cite it.

### For the maintainer (not filed)
1. eviction-deficit-against-page-deficit: restate clause (i) and the closing sentence with clause (vii) of the
   new claim (bounds above; lower bound lost at m = 2).
2. eviction theorem and assembled-page-curve: wording only (product of commuting even elements; typical in a
   parity sector).
3. After acceptance: cut the inline "split" paragraphs of the two corrected proofs and the lemma of clause (vi)
   of the new claim to claimrefs (new claim; sibling's clause (iv)); repin the Catalan result's pin on the
   Renyi-2 result from 3 to 4.
4. In the Catalan v4 the unrestricted "lies strictly between d^{1-n} and C_n d^{1-n}" is now marked as verified
   for n = 2, 3, 4, d = 2, 4, 8 (the stored proof only gave a weaker general bound); the sector upper bound
   likewise verified for n <= 6, d <= 32, not proved.
5. The stored check function check_member_purity_in_pauli_algebra (Cl(3,0), e_3 as a stand-in for the mode
   parity) is kept; the new function does the same in the algebra of the modes.

### What failed or was not done
- No proof of the upper comparisons sector < unrestricted < C_n d^{1-n} in general.
- The mean-entropy clause rests on background not derived in the store (Gaussian form of the invariant measure,
  Beta moment via the digamma function) and on Page's Fact; the literature may already contain the closed form.
- No fourth proposal for the von Neumann comparison (cap).
- First draft of the Renyi check had a wrong genus-one count at n = 6 (308; the count is 420) and a too-small
  remainder bound; found by the check itself and corrected before filing.

## Unexpected links
- The uniqueness of the twist for an arbitrary pair of mode sets is the same blade count as clause (iv) of
  synthesis.joint-clifford-clause-is-a-klein-convention-on-the-composite-space: the "clause (f) is a convention"
  result of the standard-model subject and the window/radiation split of the entropy subject are one device
  (tower.commuting-copies read in the two directions). proved.
- For a pure state that is not even, whether it is entangled depends on the split: the counterexample is a
  product state of the twisted tensor split with purities 1 and 1/2 on the algebra split. Evenness (the
  descent) is exactly what removes the ambiguity. computed; the general statement is clause (iii).
- On a parity sector the non-planar terms of the moment sum carry 4^g: read with the replica dictionary of the
  stored comparison (d^2 = e^{2S}), the first correction beyond the planar saddles is four times larger per
  genus for parity-restricted states. argued (the replica reading is the stored identification, not derived).
- The parity restriction makes a random state slightly MORE entangled across a mode cut (purity lower, entropy
  higher by about 1/(2mn)), so the Page-typical branch moves toward the eviction branch, by a subleading amount;
  at one window mode (m = 2) the sector deficit is exactly ln 2 - sum_{k=n/2+1}^{n} 1/k, below the stored bound.
- With one mode on the small side the sector's reduced state is diag(t, 1 - t) with t Beta(n/2, n/2): the moment
  formula of the sibling and the entropy formula here are two readings of one Beta law. computed.

## Decisions for Leon
1. Accept the two restatements (random-state column stated on a parity sector, abstract-tensor value kept
   beside it), or keep the stored versions and let the new claim alone carry the dictionary. Recommendation:
   accept; every leading term and every eviction clause is unchanged, and the retired Fact drops out.
2. Retirement of synthesis.imported-haar-average-purity: with the two corrected versions no stored proof cites
   it; remaining mentions are listed above (one imported Fact's text, the open problem, two proposals of this
   run). The corrected Renyi-2 proof still obtains both second moments from Schur's lemma on a symmetric square,
   inline, as version 3 did; repoint to the derived second moment once that proposal is accepted
   (recommendation: yes; dimensions there are powers of two).
3. Whether the eviction comparisons are meant before or after the descent (bridge B6). The eviction state is
   even either way, so only the random-state ensemble depends on it. Recommendation: after (sector column).
4. The mean entropy of a sector uses Page's Fact on blocks plus two pieces of background; prior art cited from
   memory (Bianchi, Hackl, Kieburg, Rigol, Vidmar 2022 on random fermionic states with a symmetry; Banuls, Cirac,
   Wolf 2007 and Friis, Lee, Bruschi 2013 on fermionic mode entanglement and the parity rule). Import as prior
   art, or leave as notes.
5. A corrected synthesis.eviction-deficit-against-page-deficit (v5) with the sector bounds: file in a later
   round, or let the maintainer restate it from clause (vii).
6. Open-problem tag used: op.island-dictionary (nearest existing). Maintainer may retag.
