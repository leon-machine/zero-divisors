# Referee G (gauge and dimension), run 2026-11-07-boson-items

Referee: Claude (referee G). Blind: I did not read findings/, work/, RUN.md, scalars-context.md or verify/S.md.
I read the three proposals in full (entity.md, proof-main.tex, check.py), the cited store entities at their pinned
versions (formal levels), the related stored entities named in REFEREE.md, and the formal levels of the five
structure-cluster proposals (for overlaps only). check4 logs: all three 0 errors, pass. Own work:
`verify/work-G/` (Fock-space route `fock.py`, independent of the tower/GA route of the checks; GA.py for the
spacetime-algebra computation; perturbed copies `pp_*.py` run with `colony/runcheck.py`).

## Summary

| id | verdict | one-line reason |
|---|---|---|
| synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators | SOUND WITH FIXES | (i), (ii), (iv), (v) correct and recomputed; (iii)'s "on null data I4 is right multiplication by J" is proved on n^u, which carries no null data (on the data I4 is right multiplication by -J); the Reading credits the ladder with Maxwell kinematics it does not supply; two different J's are conflated. |
| synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins | SOUND WITH FIXES | (i) to (iv) correct and recomputed (normality criterion, quasi-spin norms with J-valued rank-2 M); (v) is correct only for the positive adjoint, so "the indefinite form of (KF) not at all" is false (a pair mode is a Gupta-Bleuler timelike mode for a Krein form built as (KF) builds it); one false sentence in the proof of (iv). |
| synthesis.density-modes-bosonise-only-along-one-null-direction | OVERSTATED | (i) to (iv) as formally stated are correct; the title, one-liner, lay and reading's "only along one null direction" and "relativistic and bounded seas give density modes no canonical pair" are false beyond total densities (quadrant, tilted and edge-crossing seas; chiral densities of the 1+1 and 3+1 relativistic seas). |

## 1. synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators

### Proof steps and premises
- (i) Symplectic current identity: proof correct ((a.F).b = a.(F.b) for bivector F; the cancelled F1.F2 terms are
  symmetric). Check verifies it with nonvacuous fields. Standard covariant phase space (Crnkovic and Witten 1987; Lee
  and Wald 1990), here in the spacetime algebra; the ledger's "transport-absent" is right, the novelty is notation only.
- (ii) n.(n.F) = 0, the decomposition, E_perp = 2r, n.T(n) = -Q(E_perp) > 0: correct (re-derived by hand; check
  verifies on three bivectors). Gauge n.A = 0: n.F = d_n A, n.omega = d_n A1perp.A2perp - d_n A2perp.A1perp: correct.
  Modes: I recomputed by hand the flux 2 pi s sum k(a b' - b a'), P = pi s sum k^2(a^2 + b^2), the velocity
  (kb, -ka), the bracket {a, b} = 1/(2 pi s k), [alpha, alpha*] = k, [P, alpha] = -k alpha: all correct. These mode
  statements are not machine-checked (proof only).
  Hidden steps: (a) the quantisation rule [ , ] = J{ , } is Dirac's rule, a hypothesis, not derived; (b) the flux of
  omega through N being the full symplectic form of the free field (characteristic data complete, zero modes dropped)
  is the standard light-front statement (Kogut and Soper, verified: Phys. Rev. D 1 (1970) 2901), not proved here;
  (c) the generator "closed to period 2 pi" is discretised light-cone quantisation (Maskawa and Yamawaki 1976; Pauli
  and Brodsky 1985, cited from memory), a different setting from the store's null vacuum on the full line that (v) uses.
- (iii) **Error.** The printed identity I4(n^u) = (n^u)J = -J(n^u) is true (checked), but n^u has E_perp(n^u) = 0:
  it is the part of F invisible in the data of N (the waves moving along n, constant along the generators, the
  analogue of the spinor's Lambda(k) part in the light-ray result). The data E_perp sit in the nbar^r component, and
  there I4(nbar^u) = J(nbar^u) = -(nbar^u)J. Own GA computation (`work-G/g1_unit_on_data.py`): for three generic
  bivectors F, E_perp(I4 F) = -E_perp J = J E_perp, and eps(I4 F) = -eps J for eps = g1 E_perp. So "on null data the
  field theory's unit I4 is the transverse quarter turn, right multiplication by J" is false in sign: on the data it is
  right multiplication by -J (left multiplication by J, matching L_J = L_I on the spinor's canonical part in
  synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays (iv)). Perturbation P1 (test the check's identity on
  nbar^a instead of n^a) fails, confirming. The helicity statement ("two relative orientations") survives as a
  definition, but which of alpha_+- is co-rotating relative to the store's unit I4 flips, and the clause never compares
  with field-theory.fock-space-maxwell-modes (ii), (iii) (null bivectors I4-stable; with I4, positive frequency is
  helicity +1), which it overlaps.
- (iv) CAR identity, edge-clean reduction, [H, j_m] = -m j_m, rotation U(phi): correct; check verifies the full
  window identity (all labels, |m|, |l| <= 1, L = 3). Hidden step: the channel phases z_+- = e^{+-J phi/2} are taken
  from light-ray (iv), which states them with Hestenes' unit i_H (and L_J = L_I), not with a tower kernel bivector; the
  proposal "reads them with the tower's unit J". That is a matching convention, not a derivation, and the entity uses
  the letter J for two different elements (gamma_1 gamma_2 in (ii), (iii); the kernel bivector of the tower in (iv),
  (v), as the check shows: T.J = gen(2M) gen(2M + 1)). The store's unit rule (U6) requires different units to be named
  and kept apart. Also "modes of distinct generators are distinct planes" needs transverse cells (the premise's CAR is
  a continuum delta^2(y - y')); the check tests distinct channels as a proxy.
- (v) Defect formula: correct. Own route (Fock space, exact, M with J entries, which the check does not test;
  `work-G/g2_photon_defect.py`): N = 2, L = 4, h = 2, M = [[1, J], [2, -J]]: tr MM* = 7, ||MM*||_F^2 = 31, central
  value 7, ||D Omega||^2 = 62, 124, 124, 62, 0 for (m, l) = (0,1), (0,2), (-1,1), (1,2), (2,1), all = 2(l - m)
  ||MM*||_F^2 (and 0 for m > l); N = 3 non-uniform complex M: 104 = 2 * 52 >= 2 tr^2/N = 200/3; N = 3 uniform: 6 = 2
  tr^2/3. The check's numbers 4, 14, 56 and central values 2, 3, 6 recomputed by hand (MM* Frobenius 2, 7, 28).
  Note: for m = l the fluctuation of [eps_m, eps_m*] on Omega vanishes exactly (j_0^{xy} Omega = delta_xy h Omega), so
  the defect is only in the off-diagonal commutators.
- Dispersion: "with the same linear dispersion along the generator" uses H = sum k n_k, the window level operator. On
  the full generator the band modes g_k are not P eigenvectors; the compression of P to them is diagonal with weights
  Delta(k + 1/2) (this is clause (iii) of the structure-cluster Sugawara proposal), so the statement holds for the
  compression, not for P. Say so.

### Check and perturbations (runcheck on copies in work-G)
Original: all 7 functions pass (0.4 s). P1 identity on the data component nbar^a: FAIL (the finding above). P2
omega = F1.A2 + F2.A1: FAIL (two functions). P3 same phase z_+ for both channels: FAIL. P4 many-generator vacuum with
one channel not bottom-filled: FAIL (both defect checks). P5 window-identity RHS without the inner edge restriction:
FAIL. The check does not test the Fourier-mode algebra of (ii) or complex M in (v).

### Overclaiming and literature
- Reading and technical: "The ladder gives the kinematics of photon quantisation on a null plane: two transverse
  chiral fields per generator with positive null energy and no indefinite form, and the sign of their relations fixed
  by positive null energy." Clauses (i) to (iii) use no ladder, tower or transport: they are free Maxwell theory in the
  spacetime algebra plus Dirac's quantisation rule. The ladder supplies only (iv) and (v). This credits the series with
  what is classical (Kogut and Soper). It does not claim a derivation of the photon field or its dynamics: the
  formal Reading, the extraction note and the lay level all say the transverse dynamics and coupling to charges are not
  given; the technical level and one-liner do not.
- One-liner: "the generators' pair currents give them exactly at helicity 0" reads as if the photon's data came out
  at helicity 0; the photon has no helicity-0 data on N. The helicity-0 pairs are the density bosons, not photons.
- Lay: "reproduce the photon's commutation relations" needs "in mean square on the vacuum, in the limit of a
  continuum of light rays".
- Novelty: (i) covariant phase space; (ii) light-front quantisation; (iii) overlaps field-theory.fock-space-maxwell-modes
  (ii), (iii), uncited; (iv) the level-one u(2) current algebra (Goddard and Olive cited; verified Int. J. Mod. Phys. A 1
  (1986) 303 from memory only); (v) finite exact form of Pryce's observation (verified: M. H. L. Pryce, "On the
  neutrino theory of light", Proc. Roy. Soc. A 165 (1938) 247; title and venue confirmed by search, volume and page as
  cited in secondary literature). The genuinely new content is the exact defect 2(l - m)||MM*||_F^2 and its 1/N bound.
- House style: E_perp^2 (square of a vector) should be Q(E_perp) (entity lines 84, 104; proof lines 7, 9).

### Exact fixes
1. (iii), formal and proof: replace "For transverse $u$, $I_{4}(n\wedge u) = (n\wedge u)J = n\wedge(uJ) = -J(n\wedge u)$:
   on null data the field theory's unit $I_{4}$ is the transverse quarter turn, right multiplication by $J$." by "For
   transverse $u$, $I_{4}(\bar n\wedge u) = J(\bar n\wedge u) = -(\bar n\wedge u)J$, while $I_{4}(n\wedge u) = (n\wedge u)J$;
   the null data sit in the $\bar n\wedge E_{\perp}$ part of $F$ ($E_{\perp}(n\wedge u) = 0$), and $E_{\perp}(I_{4}F) =
   JE_{\perp} = -E_{\perp}J$: on the null data the field theory's unit $I_{4}$ is the transverse quarter turn, right
   multiplication by $-J$." Then restate the helicity sentence relative to $I_{4}$ (with $I_{4}$ the unit, the
   translation phase on $\varepsilon$ is $e^{+Jk\lambda}$ written in $J$), compare with
   \claimref{field-theory.fock-space-maxwell-modes} (ii), (iii) (cite it), and change the check's identity to the
   $\bar n$ component (perturbation P1 is the test). Remove "the identification of the field theory's unit $I_{4}$ with
   the transverse bivector $J$ on null data" from "New here" or reword it as the computed relation above.
2. Name the two J's: $J_{\perp} = \gamma_{1}\gamma_{2}$ (spacetime, (ii), (iii)) and $J$ the tower's kernel bivector
   ((iv), (v)); state that the rotation about the generator acts on the tower modes of channel $\pm$ with weights
   $\pm\tfrac12$ and the unit $J$ by definition, matched to the weights of light-ray (iv) (which uses $i_{H}$), not
   derived from it. State which unit the photon modes of (ii) are quantised with and why it may differ from $I_{4}$ (U1).
3. (ii): label the quantisation rule $[\,,\,] = J\{\,,\,\}$ as the quantisation hypothesis; say the generator closed to
   period $2\pi$ is the discretised light-cone setting and that completeness of the data on $N$ (zero modes dropped) is
   the standard light-front statement, cited (Kogut and Soper) as prior art.
4. Reading and technical: replace "The ladder gives the kinematics of photon quantisation on a null plane" by "Free
   Maxwell theory in the spacetime algebra gives, on a null plane, the kinematics of photon quantisation (transverse,
   classical, Kogut and Soper): ...; the ladder's fermions add exact canonical pairs of helicity 0 and the photon's
   helicity $\pm1$ relations only collectively, in mean square on the null vacuum in the continuum of generators". Add to
   the technical level and the one-liner: "not the transverse dynamics, the coupling to charges, or other gauge bosons".
5. One-liner: "the generators' pair currents give exact canonical pairs only at helicity 0 (density waves, not
   photons), and the helicity $\pm1$ relations only collectively, with defect ...".
6. Lay: after "reproduce the photon's commutation relations" add "on the vacuum, on average, in the limit of
   infinitely many light rays".
7. "same linear dispersion along the generator": say "for the window level operator $H = \sum k n_{k}$, the second
   quantisation of the compression of $P$ to the band modes up to the shift $\tfrac12$ and the scale $\Delta$".
8. Prior art: add covariant phase space (Crnkovic and Witten; Lee and Wald) for (i), discretised light-cone
   quantisation for the closed generator, both "cited from memory".
9. Q(E_perp) for E_perp^2 (four places). Optional: check the (ii) mode algebra exactly and (v) with a J-valued M.

## 2. synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins

### Proof steps and premises
- Preliminaries: J = g1 g2 commutes with every mode (std-algebra.orthogonal-anticommute, pinned v1, says what is
  needed); hat-map identities correct.
- (i) Window identity via S_q S_q^T, S_q^T S_q: correct; edge-clean value q tr(M'*M) + rho_0([M, M'*]): correct.
- (ii) Converse via one particle at a bulk momentum in channel state u: correct (the vector psi_0 fixes the scalar to 0,
  so X = 0). Own route (`work-G/g3_quasispin.py`, Fock space, window N = 2, two channels, q = 1, all 16 edge-clean
  basis vectors): normal M (Hermitian [[2, 1+J], [1-J, 0]], unitary [[0, J], [J, 0]], [[1, J], [J, 1]]) give the single
  value q tr(M*M) = 8, 2, 4; non-normal [[1, 1], [0, 1]], E_{+-}, J E_{-+} give 5 distinct values (E_{+-}: -1 to 3).
  Note: "canonical boson on the edge-clean vectors" is an identity on those vectors; rho_q(M)* does not preserve the
  edge-clean subspace (same reading as the stored edge-split result).
- (iii) Helicity criterion [W, M] = hM, nilpotency, normal and nilpotent implies zero, the doublet argument with
  M_+- = M_1 -+ J M_2: all correct (re-derived; J[W, M_+] = M_2 + J M_1 = J M_+).
- (iv) Quasi-spin norms: result correct; one proof sentence is false. "A term with k + q < 0 vanishes on every vector
  reached, since its target mode at k + q is filled in every channel and only modes at momenta >= 0 change": modes at
  momenta -q, ..., -1 do change (their u_s directions are emptied). The conclusion holds because the emptied directions
  are the u_s, orthogonal to every t_s, so the target t-mode is still filled. Own route: four channels, weights
  (1/2, 1/2, -1/2, -1/2), helicity +1, rank 2, M = [[0, K], [0, 0]], K = [[1, J], [0, 2]] (singular values squared with
  sum 6, product 4): |B^p Omega|^2 = (p!)^2 e_p exactly, N = 2, q = 1: 1, 6, 16, 0; N = 2 and N = 3, q = 2: 1, 12, 176,
  1728, 9216, 0 (the N = 3, q = 2 case has the k + q < 0 terms of the false sentence); Bose comparison p!|B Omega|^{2p}
  = 1, 12, 288, 10368. The check uses rank-one M only.
- (v) Correct as stated (positive adjoint). It is the elementary positivity fact, true for every element of every
  C*-algebra and every state, not specific to pair modes or to the tower; this should be said.

### Check and perturbations
Original passes (2.7 s). P1 equal weights for both channels: FAIL (helicity). P2 projector not edge-clean: FAIL
(edge-clean value). P3 Cartan mode in place of the flip in the quasi-spin test: FAIL. P4 sea k <= 0: FAIL (three
functions).

### Overclaiming
- Reading: "the indefinite form of (KF) not at all" is false. (KF) builds its Krein form as <x, eta y> from a positive
  form with a fundamental symmetry eta (eta = (-1)^{n_0} in (K1)); the store already gives the tower an indefinite form
  for ghosts (synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts (ii), b^dag =
  d*). Counter-model (`work-G/g4_krein_pair.py`): two tower modes, eta = (-1)^{n_2}, X = a_1* a_2, Omega = |1, 0>;
  X Omega = 0, the Krein adjoint X^dag = eta X* eta = -X*, [X, X^dag] Omega = -Omega, Krein norm of X^dag Omega = -1:
  a pair mode is exactly the timelike Gupta-Bleuler mode for that form. (v) excludes only the positive adjoint.
- Title "not bosons": should be "not exact bosons" (the formal itself has the contraction to bosons).
- Novelty: (i) is the level-one u(n) current algebra in matrix form (Frenkel and Kac; Pressley and Segal cited from
  memory, orientation only), and (ii) is its immediate corollary; (iii) is elementary linear algebra on it; (iv)
  generalises the stored quasi-spin (field-theory.how-close-tower-comes-ccr, fluctuation-forms (ii)). The ledger
  transport-absent is right. Nothing is presented as transport-derived.
- Literature: Weinberg and Witten is invoked via the stored entity, correctly scoped as a different obstruction.

### Exact fixes
1. Reading: replace "and the indefinite form of (KF) not at all" by "and no pair mode is the timelike mode of (K1) for
   the tower's positive adjoint; with a Krein adjoint $\eta X^{*}\eta$ (as (KF) and
   \claimref{synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts} construct it) a pair
   mode can be, so (v) does not exclude (KF)". Same change in the technical level ("so no pair mode is the timelike
   Gupta-Bleuler mode" add "for the positive adjoint"), the one-liner ("no pair mode is a Gupta-Bleuler timelike mode"
   add "for the tower's positive adjoint"), the lay level ("cannot come from these ripples" becomes "cannot come from
   these ripples with the fermions' own positive bookkeeping; an indefinite bookkeeping can still be imposed on them, as
   the standard construction does") and the extraction note.
2. (v): add "This holds for every element $X$ of every algebra with a positive state; it is the reason Gupta and Bleuler
   need an indefinite form, not a property of pair modes."
3. Proof of (iv): replace "since its target mode at $k + q$ is filled in every channel and only modes at momenta $\ge 0$
   change" by "since its target mode $c_{k+q}(t_{s})$ is filled: modes at negative momenta change only in the
   directions $u_{s'}$, which are orthogonal to every $t_{s}$".
4. Title: "Helicity-one pair modes on a null generator are quasi-spins, not exact bosons".
5. Extraction note: say (i) is the level-one u(n) window current algebra and (ii) its corollary; keep "new here" only
   for the window and matrix statements.

## 3. synthesis.density-modes-bosonise-only-along-one-null-direction

### Proof steps and premises
- (i) Strip identity and |E_-| = |E_+|: correct. Own route (`work-G/g5_density.py`, Fock space, operator identity on
  every basis vector): irregular d = 2 window of 6 momenta, 6 values of q, 64 vectors each: holds; 2 x 2 window, two
  channels, J-valued M, M' (4 pairs), 4 values of q, 256 vectors: holds. This is quasi-spin (i) in d dimensions.
- (ii) Correct for the uniform sea at every q. For the bounded sea the hypothesis F inside W cap (W - q) cap (W + q)
  depends on q, but the proof says "In each case ... at every q and on every window" and the technical level "any
  bounded Fermi sea away from the window's edges; their density modes have no canonical pair on any window": false at
  large q. Example: d = 1, N = 3, F = {-2, -1, 0}: values 0, 1, 1 at q = 1, 2, 3.
  Unstated step: "carry no canonical pair" needs also omega([rho_q, rho_q'^*]) = 0 for q != q'; true for the
  momentum-diagonal states used, not said.
- (iii) Counting correct; check recounts every q for N = 2, 3, d = 2, 3 and in the algebra on a 4 x 2 window.
  Recomputed: d = 2, N = 3, half-space, q = (1, 0): 6 = 1 * 6.
- (iv) Value sum |k_d|/|k| over the strips, count 2q(2N)^{d-1}, d = 1 value 2q, d = 3 interval (4qN(N - q), 8qN^2]:
  correct (proof's termwise bounds checked). Own float cross-check N = 2..7, all q < N: inside the interval (for
  example N = 7: S = 302.0, 584.3, 840.9, 1063.8, 1242.3, 1362.4 for q = 1..6).

### Check and perturbations
check4 pass. Perturbed copies run with runcheck: P1 strips swapped in the window identity: FAIL. P2
min(q_1, 2N - q_1) replaced by q_1: FAIL (at q = (-3, -3), N = 2). P3 the 1+1 sea with channel 0 at every momentum:
FAIL (zero-form check). P4 the termwise lower bound tightened to (N - q + 1)/(2N): FAIL, so the stated bound is not
vacuous slack.

### Overclaiming
- "Only along one null direction" (title), "only a half-space sea along one null direction does" (one-liner), "it is
  nonzero only through a sea that is a half-space in one direction" (extraction note), "Exact density bosons need a
  sea that is a half-space in one direction" (reading): not proved and false. By (i) the form is nonzero whenever the
  entry and exit strips are unequally occupied. Counterexamples (d = 2, N = 3, one channel, exact counts): quadrant
  {k1 < 0, k2 < 0}: 3 at q = (1, 0), 5 at q = (1, 1); tilted half-space {k1 + k2 < 0}: 5 at q = (1, 0); a disc crossing
  the window edge: -2, -3; a shifted disc: 2. No null direction appears in the formal statement at all; "null" is the
  reading's interpretation of k_1.
- "relativistic and bounded seas give density modes no canonical pair in any dimension" (one-liner), "gives density
  ripples with no boson behaviour at all" (lay), "its densities are not bosons" (reading): true only for the total
  density rho_q(1). The proposal's own (ii) says each chirality of the 1+1 Dirac sea alone gives +-min(q, 2N - q); and
  in d = 3 the channel-resolved density b = rho_q(P_+), P_+ = (1 + sigma_3)/2, has mean form S/2 (S the sum of (iv))
  and relative mean-square defect V/(S/2)^2 with V = sum_E (1 - k3^2/|k|^2)/4: 0.036, 0.012, 0.0059, 0.0036, 0.0024,
  0.0017, 0.0013 for N = 2..8, q = 1, about 0.08/N^2 (`work-G/g6_chiral_density_3d.py`, floats). So the chiral
  densities of the 3+1 window sea satisfy the canonical relation in mean square as the cut-off grows, the same
  standard the photon proposal accepts. What distinguishes the half-space sea is that its value is sharp (the
  commutator is a scalar on the sea), not that the form is nonzero.
- "located at the cut-off and growing as its square" against "2q in d = 1": the half-space value (iii) is also carried
  by the window-edge strips and also scales as (2N)^{d-1}; per transverse momentum the d = 3 value S/(2N)^2 is of order
  q (1.54 at N = 7, q = 1, against 2q = 2). The square of the cut-off is the transverse mode count, not a different
  mechanism.
- Novelty: (iii) is the finite-window form of the Fermi-surface patch commutator of higher-dimensional bosonisation
  (Haldane; Houghton and Marston; Castro Neto and Fradkin, cited from memory): a patch is locally a half-space sea, the
  value is proportional to q.n times the patch area and vanishes for transverse q. The extraction says that work's
  "corrections at patch edges" are not computed, but (iii) itself is the classical leading term and should be
  credited as such. (ii) for total densities is the stored imported Mattis-Lieb (ii) (finite band, no central term)
  sized on windows. (iv) is the classical quadratic divergence of the 3+1 Schwinger term (Schwinger 1959), here
  bounded on a cube.
- House style: proof (iv) "$\hat k^{2} = 1$" should be "$Q(\hat k) = 1$" ($\hat k$ a vector of $\Cl(3,0)$).

### True weaker statement, at every level
- Title: "On finite windows the density form is a strip difference; total densities of uniform seas carry none".
- One-liner: "On any finite window of momenta the density form is the occupation of an entry strip minus that of an
  exit strip, so total density modes carry no canonical pair in seas with uniform occupation on the strips (one-band
  relativistic seas in any dimension, bounded seas clear of the strips); a half-space sea gives the sharp
  one-dimensional value times the transverse overlap, and the two-component relativistic sea carries its form in the
  density-current pairing, in $(4qN(N - q), 8qN^{2}]$ for $d = 3$ and not sharp on the sea."
- Formal (ii): "This holds at every $q$ and on every window for the sea that fills one channel state per momentum ...,
  and, for a given $q$, for a sea contained in $W \cap (W - q) \cap (W + q)$"; add "the forms $\omega([\rho_{q},
  \rho_{q'}^{*}])$, $q \ne q'$, vanish in every momentum-diagonal state, so the total density modes carry no canonical
  pair"; add "channel-resolved densities $\rho_{q}(M)$ need not: each chirality of the $1 + 1$ Dirac sea, and
  $\rho_{q}(\tfrac12(1 + \sigma_{3}))$ of the $d = 3$ sea by (iv)".
- Formal Reading: replace "Exact density bosons need a sea that is a half-space in one direction" by "Density modes
  with a sharp central value on the sea arise for a sea that is a half-space in one direction, as on a null generator
  (and, approximately, on each patch of a Fermi surface); other seas with unequal strip occupations (quadrants, tilted
  or edge-crossing seas) give nonzero but different values, and the chiral densities of the $3 + 1$ relativistic sea
  have a nonzero mean form at the cut-off with relative fluctuation of order $1/N$". Replace "its density modes carry
  no canonical pair" by "its total density modes carry no canonical pair". Keep "So the series' exact bosons are
  per generator" as argued, dropping "and not propagating 3 + 1 bosons" or labelling it as not addressed (the result
  does not test propagating bosons).
- Technical: same two changes ("total density", bounded sea "for $q$ with the sea clear of the strips").
- Lay: replace "A sea of the kind that fills ordinary three-dimensional space gives density ripples with no boson
  behaviour at all, on any finite piece of it, and its only trace of the effect sits at the cut-off and grows with it"
  by "In a sea of the kind that fills ordinary three-dimensional space, the total density ripples have no boson
  behaviour on any finite piece of it; ripples of one spin component do, on average, through the edge of the momentum
  range, but not sharply"; and "it needs a sea filled on one side of a single direction" by "it is sharp for a sea
  filled on one side of a single direction".
- Extraction: credit (iii) to patch bosonisation as the classical leading term; drop "nonzero only through a sea that
  is a half-space".

## 4. Overlaps

- The same window identity is proved three times: photon (iv) (two channels, components, arbitrary m, l), quasi-spin (i)
  (d = 1, channel matrices, equal q) and density (i) (any d, channel matrices, equal q). Density (i) contains quasi-spin
  (i) at d = 1; photon (iv) adds unequal indices and many generators. One statement should hold it (density (i),
  extended to unequal shifts q, q', or a single lemma), and the others cite it. All three are transport-absent
  generalisations of hawking.current-commutator-exactly-edge-split.
- The rotation about the generator with unit J and weights: photon (iv) (z_+- = e^{+-J phi/2}), quasi-spin (iii)
  (W = diag(w_alpha)) and the structure proposal synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes (i)
  (U_s(theta) = e^{theta J L_s}) define the same action. One definition (the spin-statistics one is the general form)
  should be cited by the other two; quasi-spin's helicity [W, M] = hM is that proposal's spin of an even element.
- Photon (v) at N = 1 is quasi-spin (iii) for M = E_{+-}: both say the helicity-one flip current of one generator is
  not canonical. Photon (v) at many generators is the case M (x) E_{+-} of quasi-spin, whose (iv) gives the exact norms;
  for uniform smearing M = N^{-1/2} 1, |B^p Omega|^2 = (p!)^2 C(qN, p)/N^p -> p! q^p. So the photon's mean-square
  continuum statement and the quasi-spin's argued contraction over transverse cells are the same fact, consistent, and
  complementary (photon: off-diagonal defect 2(l - m)||MM*||_F^2; quasi-spin: number-of-quanta capacity q rank M).
  Recommend quasi-spin's reading cite photon (v) for the contraction instead of calling it argued, and photon (v) cite
  quasi-spin (iv) for the finite capacity. No contradiction between them; both should use the same unit J and name it.
- Photon (iv) [H, j_m] = -m j_m duplicates the structure proposal
  synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves (ii) for one channel; that
  proposal's (iii) (compression of P to the band modes is Delta(k + 1/2)) is what photon's "same linear dispersion
  along the generator" needs.
- The unit J: all three proposals use a kernel bivector J commuting with every mode; quasi-spin and density define it
  in place (J = g1 g2) and prove the commutation from std-algebra.orthogonal-anticommute; photon does not define it at
  (iv). synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower (structure cluster) is the result
  that would justify this choice; until it is stored, each should define J in its statement, and photon must keep it
  apart from gamma_1 gamma_2 and I4 (U6). The kernel proposal's (iii) records that I4 also commutes with transport
  when the radial plane is in the ground, which is the situation in the photon proposal's (ii), (iii).
- Mean-square standard: photon (v), synthesis.central-limit-of-tower-fluctuation-states-with-the-kernel-unit (i) and
  stored fluctuation-forms (vii) all state canonical relations in mean square as a limit; density's reading should be
  judged by the same standard (it is not: see section 3).
- Density (iii) on one generator (d = 1) is the stored edge-split value; its stacking over transverse modes is stored
  fluctuation-forms (vi) "for each eta in K". Not a duplicate, but the reading's per-generator claim is that result.
