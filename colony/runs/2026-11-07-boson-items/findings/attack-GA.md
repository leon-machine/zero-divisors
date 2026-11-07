# attack-GA (constructive, cluster G)

Status: done. One proposal filed (bos.gauge-bosons); bos.dimension and item 7 recorded here only (sibling GB files them). Labels: proved / computed / argued / conjectured.

## Orientation (direct lookups)
- Photon in the store: field-theory.fock-space-maxwell-modes (CCR put in by the palatial polynomial representation, an
  imported Fact; RS field F = sum [e^{-I4 kx} a_+ + e^{+I4 kx} a_-^*]); field-theory.elementary-photon-ga (helicity
  polarisations with unit I4); synthesis.clifford-conjugation-...-gupta-bleuler-form and premise (KF) (covariant route
  needs a Krein form); field-theory.composite-gauge-bosons-what-excluded (composite photon: Lorentz-breaking condensate
  and Weinberg-Witten excluded; "elementary route chosen, not forced"); synthesis.locality-of-the-attached-free-fields-
  fixes-their-statistics (positive-norm local photon is CCR, palatial).
- Null planes: synthesis.bulk-hadamard-states-restrict-...-flat-null-planes (i): generator CAR
  {psi_N(l,y), psi_N^*(l',y')} = delta(l-l') delta^2(y-y') Lambda(m): transversally ultralocal; two chirality channels
  (synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays (iii)-(iv): helicity about the generator = minus
  chirality, transverse rotation e^{-J phi/2} acts on channel eps as a phase of weight eps/2).
- Bosons: hawking.current-commutator-exactly-edge-split ([a_m, a_m^dag] = B_m - T_m exactly on a window);
  synthesis.fluctuation-forms-... (quasi-spin, HP); item 4 (filer U): unit J = kernel bivector = transverse bivector.
- No store entity on: the Maxwell symplectic current, null-plane photon data, Kac-Moody / non-abelian currents,
  higher-dimensional bosonisation.

## bos.gauge-bosons
Routes:
- R1 (own + light-front subject): derive in STA the conserved symplectic current of free Maxwell,
  omega = F1.A2 - F2.A1, and its flux through a null plane: in the gauge n.A = 0 it is the transverse expression
  d_n A1perp . A2perp - d_n A2perp . A1perp (no constraint component, no transverse derivative): two real chiral bosons
  per generator. Then realise this algebra by the generator CAR (two chirality channels per generator) and test
  helicity covariance. Delivers: what part of photon quantisation the ladder gives, exactly, on finite windows.
  Needs: the u(2) current algebra of two channels with its edge split. Fails if: the flux keeps a constrained or
  transverse-derivative term, or the currents do not close.
- R2 (store's covariant route): Gupta-Bleuler / Krein form from the tower's twisted trace (KF, K2). Delivers the covariant
  CCR only with an indefinite form; already premised (KF); not a derivation.
- R3 (pair route in momentum space, "neutrino theory of light"): photon modes as collinear particle-antiparticle pairs
  with helicities adding to +-1; this is R1's chirality-flip currents read in momentum space; same algebra.
Choice: R1 (R3 as its helicity half). Reason: the null plane is the series' setting, gauge fixing there needs no
indefinite metric, and the generator CAR is already proved on null planes.
Kill conditions (pre-registered before computing):
- KG1: the GA divergence identity div(F1.A2 - F2.A1) = (div F1).A2 - (div F2).A1 fails on polynomial test fields, or the
  null flux in the gauge n.A = 0 keeps a term other than the transverse one: then no per-generator chiral structure.
- KG2: on a finite window with two channels the u(2) currents J^{ab}_m = sum_k c_{a,k}^dag c_{b,k+m} do not satisfy
  [J^{ab}_m, J^{cd}_n] = delta_bc J^{ad}_{m+n} - delta_ad J^{cb}_{m+n} + (edge operators), with central value m
  delta_ad delta_bc on edge-clean states (n = -m): the realisation fails.
- KG3 (abelian obstruction): if some channel rotation (number-preserving, J-linear) maps the density rho_+ to
  cos t rho_+ + sin t rho_- with t not a multiple of pi/2, the claim "transverse rotation is not a fermion symmetry
  of the abelian realisation" dies.
- KG4 (helicity half): if [J^+_m, J^-_n] for m + n != 0 vanishes on the null vacuum (zero mean square), the claim that
  helicity-carrying pairs are non-canonical at level 1 dies.

## bos.dimension
Routes:
- R1 (series' setting): null seas. Modes (k_par, k_perp), k_perp on a transverse torus, sea a graph k_par < f(k_perp).
  Show the densities rho_q = sum_k c^dag_{k+q} c_k have exactly the 1D edge-split commutators with central term
  q_par |T|, independent of q_perp and f; generator-wise densities commute across generators.
- R2 (spacelike / Fermi-surface patches, Haldane, Houghton-Marston, Castro Neto-Fradkin): densities with all momentum
  directions on a torus commute exactly (zero central term); patch densities have boundary corrections.
- R3 (Lorentz, 3+1 current algebra): equal-time charge densities commute; Schwinger term only in [J^0, J^i]; argued
  from the literature only.
Choice: R1 with R2's exact zero as the contrast.
Kill conditions (pre-registered):
- KD1: for some window, torus and graph sea the commutator [rho_q, rho_q'] differs from delta_{q+q'} q_par |T| by
  something not supported on the edge of the window (on edge-clean states): then null seas do not bosonise exactly.
- KD2: the torus densities with all directions included fail to commute: then the contrast is wrong.

## op.r-premises-external (item 7, new angle only)
Route: the orientation enters (a) the quantisation rule [ , ] = sigma J { , } of the photon null data with future
time, (b) the sign of the density Schwinger term in the fermion state, (c) the ground state. Test whether realising
the positive photon commutator by densities (bosonic positivity) fixes sigma, or only ties the fermion state to sigma.
Kill condition (KR): if the kernel reflection g2 -> -g2 (fixes every transport element, J -> -J) fails to map the
sigma theory onto the -sigma theory (state, commutator sign and flow), the "remains free" conclusion dies.

## Established so far (scripts in work/GA/: tower_currents.py, null_seas.py, maxwell_null.py; all exact, all pass)
bos.gauge-bosons (route R1 chosen; KG1-KG4 all survived):
- proved+computed: STA symplectic current omega = F1.A2 - F2.A1, div omega = (div F1).A2 - (div F2).A1 (polynomial
  fields). In the gauge n.A = 0: n.F = d_n A and n.omega = d_n A1perp.A2perp - d_n A2perp.A1perp identically; the
  longitudinal coefficient drops out, no transverse derivative: photon null data = two real chiral fields per generator,
  no Krein form needed on a null plane. n.(n.F) = 0, n.T(n) = -Eperp^2 > 0: null energy positive on Eperp alone.
- proved: I4 (n^a) = (n^a) J (J = g1 g2): duality = transverse quarter turn on null data, so I4 and J agree there;
  eps = g1 Eperp in span{1,J}, rotation about the generator is a phase: the two helicities are the two relative
  orientations of the rotation phase and the null-translation phase (both read with J).
- computed: two-channel u(2) currents on a window: exact identity with edge terms; level one on edge-clean states.
  Densities: helicity 0, exact CCR (so they are null data of two scalars, not of a photon). Flip currents J^{+-}, J^{-+}:
  helicity +-1, [J^+, J^+] = 0, central m, but defect 2 J^3_{m+n}: ||[J^+_m, J^-_n] Omega||^2 = 2|m+n| (not canonical on
  one generator). Across N generators with weights M: ||D Omega||^2 = 2|q| ||M M*||_F^2 >= 2|q| (tr M M*)^2 / N, equality
  iff M M* scalar (uniform transverse smearing). Since the generator CAR is transversally ultralocal with infinitely
  many generators per unit area, transversally smeared flip currents (normalised by the cell size) satisfy the photon's
  helicity-covariant CCR in mean square on the null vacuum in the continuum of generators (defect O(cell area)).
  [H, J^{ab}_m] = -m J^{ab}_m: linear dispersion along the generator exact.
- computed: central value +1 on bottom-filled window (null vacuum band restriction), -1 on top-filled (filled sea).
bos.dimension (KD1, KD2 survived; but sibling GB is filing this target, so not filed by GA):
- computed: modes (k_par in window, k_perp on a transverse torus), graph seas k_par <= h(k_perp): the density
  commutator is exactly a difference of window-edge sums; on edge-clean graph seas [rho_(q,p), rho_(-q,p')] = q T
  delta_(p+p') exactly, independent of p (transverse momentum) and of the graph h; other commutators kill the state.
  Closed torus (all directions periodic, a spacelike slice's lattice): all densities commute exactly (no central term).
op.r-premises-external (item 7): KR survived.
- computed: kernel reflection kappa (g2 -> -g2) fixes every transport generator, J -> -J, maps pi_sigma to pi_-sigma
  and the flow Ad exp(sigma J H t) to the -sigma flow; the ground state of a real H is J-free and kappa-invariant;
  S kills it for both orientations; omega(J X) = 0 for every transport blade X.
- argued: for the photon null data the J-orientation cancels between the quantisation rule [ , ] = J{ , } and the
  Fourier factor, so [alpha_m, alpha_m*] = +m is fixed by the classical bracket with future time; the composite
  realises it with the right sign exactly in the bottom-filled (null vacuum) window, the conjugate in the filled sea.
  So bosonic positivity is the fermionic ground-state clause read on pairs: it adds no datum; the orientation of J
  relative to time stays the one datum (N+) assumes, now shared. GB files the inner-flip form of this (Ad(Gamma g1)),
  so GA files nothing on item 7 and only adds clause (vii) to the gauge proposal.

## Proposal filed
- synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators (open_problem bos.gauge-bosons; check4 exit 0,
  0 findings; validate_draft ok, no warnings). Clauses: (i) STA symplectic current identity; (ii) null data, positive
  null energy, gauge n.A = 0 flux is transverse only, exact mode brackets, CCR [alpha_ik, alpha_jl*] = k delta with sign
  independent of the orientation of J; (iii) I4 (n^u) = (n^u) J on null data, helicities = relative orientation of
  rotation and translation phases; (iv) pair currents of the generators, exact window identity, level one on edge-clean
  vectors, [H, j] = -m j, helicity phases; (v) collective realisation: defect ||D Omega||^2 = 2(l-m)||M M*||_F^2 >=
  2(l-m)(tr M M*)^2/N, equality iff M M* scalar; vanishing for transversally smeared fields as the cell area -> 0 (limit
  argued by Riemann sums). Overlap with GB's synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins:
  the N = 1 case of (v) and "densities are exact helicity-0 bosons"; GB has the single-generator normality criterion,
  quasi-spin norms and the Krein positivity, GA has the Maxwell side and the many-generator bound. Complementary; the
  orchestrator may want them cross-referenced rather than merged.

## Unexpected links
- bos.qclt-states (SA, synthesis.central-limit-of-tower-fluctuation-states-with-the-kernel-unit): clause (v)'s limit is a
  central limit across generators (blocks = generators, observable = flip current). SA's state convergence, applied with
  the generators as blocks, would upgrade (v) from commutators in mean square to convergence of the composite photon's
  states to the Gaussian (quasi-free) photon vacuum on the null plane. Worth a bridge test.
- bos.dynamics (SA): [H, j^{ab}_m] = -m j^{ab}_m for all four u(2) currents, so the flip composites have the photon's
  linear dispersion along the generator exactly; the null energy of the two channels is the u(2) level-one Sugawara form.
- synthesis.massless-frequency-sign-relative-to-i4-is-not-the-chirality (helicity locked to frequency sign relative to I4
  for spinors) has its photon analogue in clause (iii): on null data I4 is right multiplication by J, and helicity is the
  relative orientation of the rotation phase and the translation phase.
- op.r-premises-external: the photon's commutator sign is independent of the orientation of the unit (it cancels between
  the quantisation rule and the Fourier factor); the composite realises it with the right sign only on the null vacuum.
  Bosonic positivity is the fermionic ground-state clause read on pairs; the orientation of J relative to time stays one
  shared datum (kernel reflection: computed in work/GA/null_seas.py; GB has the inner-flip form Ad(Gamma g1)).

## Decisions for Leon
1. Photon status: keep the stored elementary photon (field-theory.fock-space-maxwell-modes) as the field the series uses,
   and record the collective realisation as kinematic only? Recommendation: yes. The composite's normalisation vanishes
   with the cell size, so it is free: its coupling e to charges is not derived, and no interacting photon follows.
2. The tower clauses read the tower's kernel bivector J as the transverse bivector of the generator (item 4 (f), and the
   K5 reading in which the radial plane is a transport plane). Confirm that reading. Recommendation: confirm (it is the
   reading under which the channel phases of synthesis.light-ray-good-part-...(iv) are kernel rotations).
3. Literature cited from memory in the extraction note (Kogut and Soper 1970; Goddard and Olive 1986; Jordan 1935;
   Pryce 1938): verify and, if wanted, import as Facts in the maintainer pass (they are prior art only, not premises).
4. bos.dimension: no GA proposal (GB files it). If GB's proposal lacks it, the GA computation adds: on graph seas
   k_par <= h(k_perp) over a transverse torus the central term is q T, independent of transverse momentum and of the
   graph; on a closed torus all densities commute (work/GA/null_seas.py). Recommendation: pass to GB's fix round.
5. Item 7: record on op.r-premises-external that bosonic positivity supplies no datum (with GB's proposal as the
   reference). Recommendation: yes, one sentence in "known".
