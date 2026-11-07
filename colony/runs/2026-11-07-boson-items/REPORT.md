# Run 2026-11-07-boson-items: report

Targets: the outstanding boson items after the 7 November boson result. Item 4 (the GA unit of Hermitian boson
fields) filed directly; items 1 (gauge bosons), 2 (dimension), 3 (spin and statistics), 5 (convergence of states),
6 (dynamics) and 7 (a new angle on op.r-premises-external) attacked. Method: filer U; two attacker pairs, cluster S
(SA constructive, SB adversarial) and cluster G (GA constructive, GB adversarial); blind referees S and G; one fix
round; close-out. Leon's rules: everything in GA, imports derived rather than imported (literature as prior art in
extraction notes only), no imaginary unit (unit principle U1 to U6).

## Accepted (eight results, all proved at their stated strength, no imported Fact used)
- synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower (U; SOUND WITH FIXES). Item 4. In a
  tower level Cl(N, N+2) the planes alone have no even unit; the commutant of transport is the quaternion algebra
  span{1, J, Gamma e2, Gamma e3} with unique even unit +-J (J the kernel bivector); I_n = J Gamma; phi = X + X*,
  pi = J(X* - X) self-adjoint with [phi, pi] = 2J[X, X*]; nothing in transport fixes the sign of J (argued: it is the
  (N+) orientation datum, now shared by fermions and bosons).
- synthesis.central-limit-of-tower-fluctuation-states-with-the-kernel-unit (SA; SOUND WITH FIXES). Item 5. For product
  block states the characteristic functions of the normalised collective fields converge to the Gaussian state with the
  stored covariance and symplectic form, with an explicit error bound of order N^(-1/2).
- synthesis.ladder-states-are-locally-product-with-non-gaussian-fluctuations (SB; SOUND WITH FIXES). Item 5, the
  limit of the above: the ladder (Dicke) states are locally product but their fluctuations are not Gaussian, so the
  product hypothesis cannot be dropped.
- synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves (SA; SOUND WITH FIXES).
  Item 6. Exact finite-window Sugawara identity, linear dispersion [H, rho_q*] = q rho_q* with phase flow e^{JtH}, the
  band compression of the null momentum with weights Delta(k + 1/2), and Luttinger normal modes. Prior art
  (Kronig; Schoenhammer and Meden 1996) in the note.
- synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes (SB; OVERSTATED, restated; Leon accepted the
  restatement). Item 3. Title: "On the ladder the bosons' spin and statistics are fixed by the single modes' spins".
  Spin and statistics agree on the whole tower algebra exactly when every mode is a spinor; the bosons alone obey the
  rule exactly when the assignment is uniform; a mixed assignment gives a commuting boson of half-integer spin. The
  collective limit neither creates nor repairs the connection.
- synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators (GA; SOUND WITH FIXES). Item 1. Maxwell in
  STA on a null plane gives the photon's transverse null data, two helicities, positive null energy, with I4 acting as
  right multiplication by -J_perp on the data; the ladder gives helicity 0 exactly and helicity +-1 only collectively,
  in mean square.
- synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins (GB; SOUND WITH FIXES). Item 1, adversarial:
  helicity-one pair modes are quasi-spins of finite capacity, not exact bosons; the Krein form is not excluded.
- synthesis.density-modes-bosonise-only-along-one-null-direction (GB; OVERSTATED, restated; Leon accepted). Item 2.
  Title: "Window density forms are strip differences; total densities of uniform seas carry none". The id keeps the
  original wording, which the restated content contradicts (see Open below).

## Leon's decisions (7 November)
- Both restated (OVERSTATED) proposals accepted.
- Spin enters by a note citing the stored locality result for the attached free fields (already in the spin-statistics
  entity's extraction note); no definition of tower spin adopted.
- Notes recorded: (a) conventions, unit principle U2: J is the unit on a tower level whenever the radial atom's modes
  are among the modes; I4 stays for the horizon continuum. (b) op.r-premises-external known: bosonic positivity adds no
  datum (the J flip is inner, Ad(Gamma g); O(2) action on the unit); the orientation stays the one datum (N+) assumes.
  (c) The photon stays elementary and the Krein form a premise (reading of the photon entity). (d) The half-integer
  offset of (Q) appears as the band centre of the compressed null momentum (note on
  singularity.q-joint-quasi-freeness-s-wave, premise unchanged).

## Maintainer pass
Plain-text citations of sibling proposals turned into store references (claimref in levels and proofs, plain ids in
extraction notes); kernel-bivector now lists ladder-bosons@1 in its uses (it uses that entity's product formula).

## Open
- Item 2 in full: higher-dimensional bosonisation beyond the strip identity (channel-resolved densities can carry a
  pair; not pursued).
- Item 1: transverse dynamics, coupling to charges, gluons, W, Z and the Higgs are not derived.
- Item 7: the orientation of the unit relative to time remains a datum.
- The density entity's id says the opposite of its restated title; renaming it (with its citing entities) is a
  later change if Leon wants it.

## Checks
Baseline (store at 1cfac5d) 0 errors 0 warnings. Gate: every proposal check4 exit 0 and validate_draft ok after fixes
(the quasi-spin check strengthened once more to clear W413). Final check 0 errors 0 warnings (verify/final-check.log; first pass flagged W405 on the added uses edge, excused in
coverage, and E602 for the missing author); build 0 errors (2278 entities, 7178 edges); layout, site, lock; 393 tests OK.
