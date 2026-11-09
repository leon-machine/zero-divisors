# Attack C3A (cluster C3, angle A constructive): the mod-24 recurrence test

Targets: op.counted-mode-energy (which fields form the light-ray sea) and op.qft-structural-inputs (three
generations), through the recurrence test recorded in op.counted-mode-energy "known" (argued, not filed).

## Orientation (direct lookups)
- The test was stored only as prose in op.counted-mode-energy (known). No earlier run worked it.
- (Q) version 3 (singularity.q-joint-quasi-freeness-s-wave): "the Killing flow at one modular period 2 pi/kappa
  is the parity automorphism psi -> -psi", automorphism level; identifying the real-time recurrence with the
  Euclidean sign R_{2pi} = -1 is "part of the reading". state-selection.where-fermi-dirac-comes: the Euclidean
  rotor R_{2pi} = -1, also no real-time implementer.
- Window reading (synthesis.window-reading-array-killing-energy v1, postulate): fixes the zero of an array's
  energy (null ground state of (N+)); says explicitly it does not fix which fields form the sea.
- Null ordering (synthesis.null-ordering-of-counted-units-is-zeta-symmetric v4): -kappa/24 per complex
  component per window; equals the symmetric sea only at delta = 1/2.
- Exact window Sugawara identity (synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves v1):
  H = Q^2/2 + T on every window, factorised e^{JtH} with the kernel unit J.
- Slot module (synthesis.slot-module-light-ray-arrays-are-weyl-components v3): 16 Weyl components per generation,
  15 without the neutral singlet (not a CPT halving); "integer-weight fields lie outside this count"; one array
  set per Kaluza-Klein level of a 5D field.
- Light ray (synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays v5 (vi)): vector fields carry
  integer weights "and so would give the other offset". Photon null data: two transverse chiral fields per generator.
- n_g free under slot-module premise and anomaly freedom; n_g <= 5 if SU(2) and SU(3) both asymptotically free
  (synthesis.slot-module-makes-the-faces-separate-composites-and-leaves-the-generation-number-free v2).

## Routes
- R1 (the problem's own): finite windows; stored window identity gives e^{2 pi J H} = grading; window reading
  adds -1/24 per array. Exact, GA, stored premises only. CHOSEN.
- R2 (other subject): T-transformation of the NS character / framing anomaly e^{2 pi i c/24}; same c/24, imports
  modular forms and complex analysis. Used only as prior art.
- R3 (own): Bernoulli route for CCR arrays, deciding what the condition becomes if integer-weight fields join.
  Used for clause (iv).

## Kill condition (pre-registered before computing, 2026-11-09)
K1. Killed if, on an exact finite window, the one-window evolution with the window-reading zero is not
e^{2 pi J n/24} Gamma for n arrays, or U = Gamma holds for some n not = 0 mod 24.
K2. The "choice" verdict is killed if a stored premise in the past cone of the null-ordering result fixes the
implementer of the one-period flow as an operator (not an automorphism).
K3. The n_g = 0 mod 3 consequence is killed if the store places integer-weight fields in (Q)'s arrays.
Result: none fired. K1: the check passes exactly. K2: grep of the 196-entity past cone: only automorphism-level
or Euclidean statements ((Q), half-integer-weight-array, q-splits (iv), where-fermi-dirac-comes). K3: the store
keeps integer-weight fields outside the arrays (slot module v3, light ray v5 (vi)).

## Established
Proposal: synthesis.one-window-parity-recurrence-of-the-light-ray-sea-needs-twenty-four-arrays (REGISTERED in
proposals/, coverage.yaml copied back; check4 0 errors 0 findings (no W413), validate_one ok; source folder
work/C3A/<id>/, gate copies in verify/final/). Overlap note for the orchestrator: C3B's planned
synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content takes my clause (ii) as
given and tabulates the content; my clause (iv) is only the general CCR lemma and mod-8 condition, no content table.
- PROVED (i): on every window, e^{2 pi J H} = (-1)^M prod_j e_j f_j = (-1)^Q, the grading (1 - 2 n_j = e_j f_j);
  spectrum of H in Q/2 + Z; identity at offset 0. Checked on L = 2, 4, all occupation states.
- PROVED (ii): under the window reading (through null-ordering (iv)) one array's null-ordered energy is
  kappa(H - 1/24); the sea's one-window evolution is U = e^{2 pi J n/24} Gamma. For every n, Ad U is the parity
  automorphism and the KMS state is unchanged: so (Q), KMS at 2 pi/kappa, (N+) and the window reading hold at every
  n, and U = Gamma (the recurrence condition) holds iff 24 | n. U^2 = 1 iff 12 | n. Per array e^{2 pi J/24}, per
  counted unit e^{2 pi J/12}, per generation e^{4 pi J/3} (order 3): only the joint sea can satisfy it.
  Rotor exact in Q(sqrt2, sqrt3).
- PROVED (iii): 16 n_g + n_x = 0 mod 24; n_x = 0 gives n_g = 0 mod 3 (NOT n_g = 3). Without nu_R: 15 n_g = 0 mod 24
  iff n_g = 0 mod 8 (n_g = 3 fails); at n_g = 3 with r singlets, r = 3 mod 24. The 2-window version gives the same
  n_g condition on 16 n_g.
- PROVED (iv): complex CCR array zero point -(kappa/2) B_2(delta), equal to -kappa/12 iff delta = 0
  (-(kappa/2)B_2 + kappa/12 = (kappa/2) delta(1 - delta)); real component -kappa/24; integer excitations, so c_B real
  integer-weight components add e^{2 pi J c_B/24}; with 16 n_g the condition needs c_B = 0 mod 8 and n_g = c_B/8 mod 3.
- ARGUED: -kappa/12 is the null-ordered value of a complex chiral boson (Schwarzian rule with c = 2; standard, from
  memory), so the window reading extended to CCR arrays selects integer weights: the reading's offset selection is
  by statistics (CAR 1/2, CCR 0).
- ARGUED: modular (thermofield) implementers of the flow are phase-blind (the constant cancels between the two
  copies), so no modular-theory premise can supply the condition either.
- ARGUED: with the stored asymptotic-freedom bound (n_g <= 5, both factors), n_g = 0 mod 3 leaves n_g = 3 alone;
  colour alone leaves 3 and 6. Asymptotic freedom is not a premise.

Answers to RUN questions:
(1) The condition: the one-window Killing evolution of the light-ray sea, normalised by the window reading, equals
    the grading Gamma. Proved equivalent to 24 | n (n = number of complex arrays = chiral central charge).
(2) A new choice: the operator (implementer) form of (Q)'s automorphism clause. Not derived from the window
    reading, KMS or (N+); each holds for every n.
(3) Which fields: the store decides it for the sea as (Q) and the window reading define it: the CAR arrays, i.e.
    the Weyl components (16 per generation) plus any further spinor arrays n_x (dark towers, KK levels). The
    integer-weight fields are outside (Q)'s arrays; whether they join the recurrence is part of the choice. If they
    did, c_B must be 0 mod 8 first (C3B works out the series' content table: graviton or one doublet kill every n_g,
    two doublets give n_g = 1 mod 3).
(4) n_g = 0 mod 3, not 3. What would fix 3: an upper bound below 6 (SU(2) asymptotic freedom gives <= 5) or an
    independent exact condition (the stored Sakharov cancellation at N_g = 3, an induced-gravity reading).
(5) Without nu_R: 15 n_g, n_g = 0 mod 8; three generations would need r = 3 mod 24 neutral singlets.

Prior art (web, 9 November 2026): J. Wang, arXiv:2312.14928 (c_- = 8 per family of 16 Weyl fermions on a 1+1d
defect, framing anomaly c_- = 0 mod 24 gives N_f in 3Z, 3(E8)_1); Z. Wan, J. Wang, S.-T. Yau, arXiv:2605.26202
(review of that and a mod-3 route through a B+L gravitational anomaly in Z9); I. Garcia-Etxebarria and M. Montero,
arXiv:1808.00009 (Z16 Dai-Freed, 16 per generation). From memory: Witten 1989 framing anomaly. The arithmetic is
prior art; new is the horizon light-ray setting with the absolute phase fixed by (N+) via the window reading, the
exact window proof in GA, the independence from the stored premises, and the CCR mod-8 clause.

## Unexpected links
- synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations: the stored Sakharov
  weight N_V - N_W/4 vanishes exactly at N_g = 3 (12 = 4 N_g); with the recurrence condition (N_g = 0 mod 3) the two
  together single out 3 among N_g <= 5 and agree at 3. Different structure (quadratic vs vacuum-phase), same number.
- The window Sugawara split of one generation (32/7, 2, 1, 1, remainder 52/7; sum 16): only the total enters the
  phase; the parts carry phases of order 168 etc., so no single gauge sector satisfies the condition alone.
- The self-dual point tau = I_4 (remark in counted-unit-energy-at-half-offset): window length equals beta, so the
  condition is the T-transformation phase at the S-fixed point.

## Decisions for Leon
1. Candidate premise (not filed; maintainer-only). Name: the implemented recurrence of the light-ray sea.
   Statement: the one-window Killing evolution of the CAR arrays of a light ray, with energies measured from the null
   ground state of (N+) as the window reading measures them, is the grading of their window algebra (not only a
   unit multiple of it). Consequence (proved in the filed claim): 16 n_g + n_x = 0 mod 24.
   Costs: (a) it constrains a c-number phase that ordinary quantum theory cannot observe; its content rests on the
   window reading treating absolute window energies as physical; (b) it must be scoped to the CAR arrays: if the
   integer-weight light-ray data join, the series' content fails (C3B: the graviton or one doublet kill every n_g;
   two doublets give n_g = 1 mod 3), and C3B argues it cannot be posed on the hole's whole Hamiltonian (label phase
   2S); (c) every spinor array on the light ray counts, so dark towers and 5D KK levels must add n_x = 0 mod 24;
   (d) it needs the neutral singlet in each generation; (e) it gives n_g = 0 mod 3, not 3: three needs a further
   input (asymptotic freedom of SU(2), or the Sakharov reading). Refutation condition: a light-ray CAR content
   (including towers) with array count not 0 mod 24.
   Recommendation: do NOT adopt as a premise now; record it as a test (the filed claim already states it as an
   equivalence). Adopting it buys only n_g = 0 mod 3, already known as prior art (Wang 2023), at the cost of a
   selective scope (CAR only) the store would have to justify, and it constrains the undecided dark-tower content.
2. Import as Facts, if the claim is accepted and Leon wants the prior art in the store: J. Wang arXiv:2312.14928;
   Garcia-Etxebarria and Montero arXiv:1808.00009 (both cited in the claim's note as prior art, not used).
3. Wording for op.counted-mode-energy known: replace "A test, not a derivation" sentence by a pointer to the filed
   claim, and record that the integer-weight fields are outside (Q)'s arrays in the store, so the "78" case is a
   choice of scope, not a stored reading.
