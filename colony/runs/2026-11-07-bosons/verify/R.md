# Referee R, run 2026-11-07-bosons

Proposal: synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum (v1).
Read: REFEREE.md, BRIEF.md "Role: referee", entity.md, proof-main.tex, check.py, check4 log (0 errors, pass).
Not read: findings/, work/, RUN.md.

## Progress log
- Read proposal and check. Next: cited store entities at pinned versions.
- Read cited store entities at pinned versions: imported-tower-limit@3 (CAR of planes), how-close-tower-comes-ccr@4
  ([B,B*] = n - (N_c+N_d), K3 = (N_c+N_d-n)/2, ladder 1 - 2k/n), no-canonical-commutation-relations-tower@3,
  current-commutator-exactly-edge-split@4 (B_m - T_m; forward direction "scalar m on edge-clean"; cross commutators
  annihilate edge-clean states; [a_m,a_m'] = 0), floor-regulator@3 ((ii) edge operator, (iii) min(p,2N-p) on sea),
  null-vacuum-on-a-horizon-generator@1 ((ii) symbol chi_(-inf,0)(P), no premise). All say what the proof needs.
- Also read (not cited as premises): bosonisation-bridge-s-wave-sector@8, whose clause (1) already states
  [a_m, a_n] = m delta_{m+n,0} on the infinite filled-sea array (proof: finite window exact, "the infinite array has
  no edges"), and imported-schwinger-term-and-mattis-lieb-density-algebra@1. n-plus-null-ground-state@12 covers
  horizons (a) Schwarzschild, (b) de Sitter, (c) local Rindler (plus collapse via J3 in one-liner), not "every horizon".
- Store precedent: ~33 entities mention (N+) with no assumes edge when the mathematics is about omega_0 and (N+) enters
  only the reading; entities that prove "under (N+) the state is ..." (positive-null-energy-gives-r-premises) carry it.
- Perturbations (copies in work-R/, harness work-R/run1.py; control run of the four unperturbed functions: all PASS):
  A. adjoint as plain reversion (drop the sign per negative-square generator) -> FAIL in checks 1, 2, 3.
  B. null-vacuum window with the reversed sea (symbol chi_(0,inf)) -> FAIL (diagonal entries become -min(q, 2N-q)).
  C. deep sea with the top mode also filled (edges not clean) -> FAIL (finite-excitation CCR check).
  D. variance scaling 1/N -> 1/N^2 -> FAIL (fluctuation check).
- Own route (work-R/own.py, own4.py, exact, lib/GA.py):
  (1) rank of sigma on A_e in the basis of the 8 even blades of Cl(2,2) (not matrix units), 49 product states on the grid
      {0, 1/5, 1/3, 1/2, 2/3, 4/5, 1}^2: 0 mismatches with 2[p1 != p2] + 2[p1 + p2 != 1]. A non-product even state: rank 4.
  (2) Q = b + b*, R = b - b*, occupations (3/4, 1/4), N = 2 built from scratch: mean(D) = 0, var = 3/4; by hand the
      single-block variance is 4(p1(1-p1) + p2(1-p2)) = 3/2, /N = 3/4. Agrees.
  (3) Fermi-Dirac total by hand: M = 4 gives 8/3, M = 6 gives 243/33; sum 331/33, as pinned.
  (4) Infinite-band clause on a deeper excitation: psi = rho_2* rho_1* sea. On a 10-mode window psi is NOT edge-clean at
      depth 3 (reaches modes 2 and 7) and [rho_3, rho_3*] psi = (B_3 - T_3) psi != 3 psi; on 12 modes (edges clean)
      [rho_3, rho_3*] psi = 3 psi and [rho_1, rho_3*] psi = [rho_2, rho_3*] psi = [rho_1, rho_2] psi = 0. This is exactly
      the proof's window condition L' >= L + q + q'; no defect.
  (5) For a real state sigma vanishes on every pair of self-adjoint even elements (computed: max 0), while
      sigma(b, b*) = 1/2 at (3/4, 1/4). So the canonical pairs are (a, a*) with a not self-adjoint, [a, a*] = scalar: no
      imaginary unit is needed or used. A Weyl form with self-adjoint fields would need a central unit, which the block's
      even algebra lacks (its pseudoscalar squares to +1).
- Literature: Cushen-Hudson J. Appl. Probab. 8(3) (1971) 454-469, doi 10.2307/3212170 verified (scilit);
  Holstein-Primakoff Phys. Rev. 58 (1940) 1098 verified (ADS); Goderis-Verbeure-Vets "Non-commutative central limits"
  exists (MaRDI), volume/pages not verified by me; Goderis-Vets CMP 122 and Mattis-Lieb JMP 6 not checked.

## Step-by-step
(i) correct, standard (a(f) for a unit f is one mode). (ii) correct; the reflection is an automorphism and maps the
hopping ladder onto stored how-close-tower-comes-ccr@4 exactly (K3 sign conventions agree). (iii) correct; Gibbs
occupations and tanh(eps/2T) verified by hand. (iv) correct: radical of sigma = commutant of rho in A_e (rho in A_e,
trace pairing nondegenerate on each Mat_2(R)); rank 2[a != d] + 2[beta != gamma], a - d = 1 - p1 - p2,
beta - gamma = p1 - p2; tracial kernel = annihilator of the 6-dim commutator span; pure-state exclusion correct. (v)
correct; the converse is the statement that the q-eigenspace of a diagonal operator with d(s) <= q is the span of the
s with d(s) = q, which are the edge-clean ones when 2q <= M. (vi) restriction lemma correct (disjoint spectral
supports; quasi-free determinants; product state matches). min(q, 2N - q) entries correct; cross terms vanish by gauge
invariance. Infinite band: the finite-sum and window arguments are right (confirmed by (4) above). "Pure" is asserted
and not used. (vii) identity and variance correct; hidden hypothesis: omega must be a state on A_e and omega^{tensor N}
the product state on the even algebras (for a non-even block state the full product need not be a state); F_N(b) = B
needs omega(b) = 0 (gauge invariance), said only in the proof.

## Novelty
(i) new to store, textbook. (ii) restates how-close-tower-comes-ccr@4 under an automorphism (said). (iii) new to store,
standard. (iv) new. (v) identity restates hawking.current-commutator-exactly-edge-split@4 and floor-regulator@3(ii)
(said); forward edge-clean direction stored in edge-split (said implicitly); converse new; product-state value new;
sea value stored in floor-regulator@3(iii) (said). (vi) band restriction of omega_0 and of symbols phi(P) new; window
form values follow from floor-regulator(iii); infinite-band CCR already stated in singularity.bosonisation-bridge-
s-wave-sector@8 clause (1) ("[a_m, a_n] = m delta on the infinite array") and is a corollary of edge-split; the
proposal cites the bridge only for the edge form and the min value and lists the infinite-band relation as new: NOT
said. Domain D is a sharpening. Prior art imported-schwinger... cited as prior art (said). (vii) new to store; standard
(algebraic core of the quantum CLT; said).

## Verdict: SOUND WITH FIXES (fixes in the final report).

## Fixes
1. Novelty of (vi): in the extraction note move "satisfy the canonical relations on the finite excitations of the infinite
   band" out of "New here" and say it is stored in Theorem singularity.bosonisation-bridge-s-wave-sector (1) (there for the
   s-wave boundary modes) and follows from hawking.current-commutator-exactly-edge-split; new is the restriction of
   omega_0 (and of any symbol phi(P) tensor id_K) to band modes, the explicit invariant domain D, and their combination.
   Drop "without normal ordering" as a contrast (for q != 0 there is no diagonal term; the bridge already says the
   normal-ordering constants drop out).
2. Scope of (N+): "every horizon generator" (Reading, technical, extraction note) -> "each generator of a horizon that
   Premise (N+) covers"; lay "every horizon line" -> "the horizon lines it covers". In formal (vi) the parenthetical
   should read "the state Premise (N+) assigns to the generator, by the uniqueness in Theorem
   synthesis.null-vacuum-on-a-horizon-generator(ii)". No assumes edge: the mathematics is about omega_0.
3. Technical: "the fluctuations obey canonical commutation relations with this form" -> "the commutator of the
   fluctuations tends to this form in mean square; in that sense the fluctuations obey canonical commutation relations
   with it (convergence of the fluctuation states is not claimed)".
4. Reading: "they arise as collective fluctuation modes" -> "they arise here as ..."; technical "This reads: bosons are
   density waves of the filled sea" -> "This reads: on the generators (N+) covers, the filled sea carries bosons, its
   chiral density waves, one band at a time; this is not a construction of the photon or other gauge bosons". Lay: after
   "exact bosons", replace "once the tower is taken to be infinite" by "once the band of levels along the line is taken
   to be infinite", and add "These ripples are not the photon or the other force carriers."
5. (vii) hypothesis: "for a state omega of the block's even algebra A_e (for instance the product state of (iv)), with
   omega^{tensor N} the product state on the even algebras of the N blocks"; final sentence: "for a gauge-invariant
   product state, where omega(b) = 0, the hopping mode is F_N(b) = B ...".
6. (vi) proof: drop "pure" (unused, unproved) or cite synthesis.imported-powers-stormer-takesaki-disjointness(d); add the
   one-line GNS derivation ||w_k Omega||^2 = omega_0(v_k w_k) = 0 (k >= 0), ||v_k Omega||^2 = omega_0(w_k v_k) = 0 (k < 0).
7. One-liner: "density forms vanish for balanced edges" -> "density forms vanish in product states with balanced edges";
   "canonical bosons on the infinite band" -> "canonical bosons on the finite excitations of the infinite band".
8. Minor: (v) "filled sea" with M even (lowest M/2 filled); check docstring (4) says 25 product states, code has 26.
