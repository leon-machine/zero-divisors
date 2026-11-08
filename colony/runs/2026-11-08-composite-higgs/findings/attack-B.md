# Attack B (adversarial): obstructions to a gapped composite doublet on the tower

Target: op.qft-bosons-and-the-rung-field, attack items 5 and 6 (two-condensate pairing; a gapped helicity-zero
composite doublet with today's exact boson results).

Status: done. Two proposals filed (both gates clean).

## Orientation (direct lookups)
- rung-odd (synthesis.rung-field-is-odd-in-the-tower-and-its-modes-carry-no-even-doublet): on the two rung planes alone
  every doublet element is odd; an even doublet needs an odd factor from outside (clause 3). A second fermion species
  supplies it: a doublet mode times a singlet mode is even and a doublet. So parity alone does NOT exclude a composite
  doublet of two species.
- pairing gap (synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy): one species, one shell;
  uniform scalar channel P + P* moves only along the band; pair-breaking threshold G n_b = 2E.
- helicity-one quasi-spins (synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins (iii), (iv)): the
  nilpotency argument uses only real channel weights W with [W, M] = hM, h != 0. Any channel U(1) (hypercharge, T_3)
  serves as W. So every pair density mode with nonzero charge is nilpotent, never a canonical boson on edge-clean
  vectors, a quasi-spin of capacity q rank(M). Every component of a hypercharge-1/2 doublet is charged. (Its
  extraction note already says the weights may be any real numbers, so this is a corollary, not new.)
- composite-scalars mean field (4): the axial phase is an exactly flat direction of the mean-field energy (classical
  Goldstone direction). No finite-size statement stored. No stored Goldstone theorem.

## Routes
1. Finite Goldstone theorem on a floor (own route). CHOSEN, filed (proposal 1).
   Kill condition (pre-registered): the second difference of the band is not O(G) = O(E/n_b), or some uniform pair
   field applied to the ground band state has a component on a non-band level. Not triggered.
2. Charge and parity selection (the problem's own route, via rung-odd). Kill condition: an even doublet in the algebra
   of doublet modes alone, or a charged (h != 0) channel matrix that is normal. Not triggered (proposal 2).
3. Window Goldstone with dispersion (from the bosonisation results). Not pursued: needs a condensate on the window and
   a lattice f-sum; kept as a reading.

## Results (labelled)
Proposal 1: synthesis.uniform-pair-channel-of-a-tower-condensate-is-a-goldstone-rotor
("Finite Goldstone bound: the uniform pair channel of a pairing condensate is a rotor"). Gate: runcheck 4/4 pass;
check4 exit 0, 0 errors, 0 other findings (mutants ok in all four functions); validate_one ok, no codes (I305 info
only); registered, files identical, coverage.yaml copied.
- PROVED (i): a field of nonzero charge has no expectation in any sector vector; a finite order parameter needs an
  energy eigenspace meeting two sectors s, s + h.
- PROVED (ii): variational bound E(s + h) - E(s) <= <X psi, [H, X] psi>/|X psi|^2 (and downwards with X*), equality iff
  X psi is a lowest vector.
- PROVED (iii), the finite Goldstone bound: H = H_0 - G X X*, [H_0, X] = eps X, [X, X*] = c(charges): second
  difference of sector ground energies <= G(c(s) - c(s - h)) at every size; with the ground state in a sector where X
  and X* both act nontrivially, both neighbours are within that bound.
- PROVED (iv), single shell: bound 2G attained; ground state = band state at the integer nearest
  gamma = (n_b + 1)/2 - K/G (global ground state on the whole Fock space); condensed (G n_b > 2K): neighbours at
  G(1 +- 2(n* - gamma)) in [0, 2G], (P + P*) psi has all its weight there; rotor / pair-breaking threshold <= 2/n_b,
  <= 4E/n_b at fixed mean-field gap E. Symmetric (G n_b < 2K): unique vacuum, bound pair at 2K - G n_b below the
  broken-pair level 2K, closing exactly at G n_b = 2K. Ground state has <P> != 0 only at K/G = n_b/2 - n.
- COMPUTED (exact, n_b = 2, 3, not filed): for the doublet floor H_D = K(N_d + N_s) - G sum_a P_a* P_a,
  P_a = sum_b w_a w_s, the uniform fields P_a, P_a*, E_ab, N_s close as u(3) ([P_a, P_b*] = delta_ab(n_b - N_s) - E_ba);
  the symmetric band (P_1*)^t (P_2*)^u Omega has isospin exactly p/2 (p = t + u) and energy 2Kp - Gp(n_b - p + 1);
  in the symmetric phase the doublet P_a* Omega is gapped at 2K - G n_b; but in the condensed regime the ground state
  is NOT on the symmetric band (n_b = 2, K = 1, G = 2: ground -3 in sector (N_1, N_2, N_s) = (1, 1, 1) against band
  minimum -2; n_b = 3, K = 0, G = 1: ground -6 at (2, 2, 2) against -4). So (iii) does not cover the doublet floor:
  [X, X*] there carries the isospin hopping.
Proposal 2: synthesis.even-composite-doublet-needs-a-singlet-constituent-and-its-pair-modes-are-quasi-spins
("An even composite doublet needs a singlet constituent, and its pair modes are quasi-spins"). Gate: runcheck 3/3
pass; check4 exit 0, 0 errors, 0 other findings (mutants ok); validate_one ok, no codes; registered, files identical,
coverage.yaml copied.
- PROVED (i), selection rule: the mode algebra splits by doublet parity and singlet parity, isospin and hypercharge
  preserve the split, T_3 weights on doublet parity p_D lie in p_D/2 + Z. Every doublet is odd in the doublet modes; an
  even doublet is odd in the singlet modes (a singlet constituent is necessary, and parity imposes nothing more). One
  doublet pair of modes: doublet-odd part all isospin 1/2, doublet-even part isospin 0 and 1 (eigenvalue 2 with
  multiplicity 3 dim A_S^{p_S}), checked complete with 0, 1, 2 singlet planes. The four doublet-singlet bilinears are
  even doublets of hypercharge +-(Y_d - Y_s), +-(Y_d + Y_s).
- PROVED (ii), as the stored helicity-one argument read with isospin/hypercharge weights (flagged in the note as a
  corollary): every component of a doublet of pair densities has T_3 = +-1/2, so it is nilpotent, never a canonical
  boson on edge-clean vectors, a quasi-spin of q rank(M) sites on the sea; doublet-singlet hopping: capacity q, norms
  (p!)^2 C(q, p), edge-clean values q +- 1, mutual commutator = bulk isospin raising density.
- ARGUED: particle-pair doublets reduce to hoppings by the particle-hole reflection of the singlet planes.
- ARGUED (reading): a condensate's uniform helicity-zero composite is its Goldstone rotor; a gapped uniform composite
  exists only without a condensate. A gapped composite doublet must be one that does not condense, or non-uniform.

## Coordination with attacker A
Read attack-A.md midway (11:08). A's model: block (psi_1, psi_2, chi), singlet pair S = sum w_1 w_2 and doublet pairs
B_a = sum w_a w_chi, H = K_psi N_psi + K_chi N_chi - G_S S*S - G_D sum_a B_a* B_a. A finds a gapped doublet quantum
C_2 = sum v_chi w_1 on the singlet band, omega_D = (K_chi - K_psi) + (G_S - G_D)(Omega - P + 1), and trion levels below
the collective doublet when P > Omega - 2. No overlap with what I filed (I file only the general bound, the single
shell and the reading; I do not file the u(3) doublet floor). Points for A (adversarial reading of A's result):
1. A's gapped doublet rides on a SINGLET condensate: isospin is unbroken in that state (no doublet order parameter;
   by (i) of my proposal its ground state, a sector vector, has <B_a> = 0). It is a gapped doublet in the symmetric
   electroweak phase, not a Higgs that breaks the symmetry.
2. At K_chi = K_psi and G_S = G_D the element is u(3)-symmetric and C_a are generators: the doublet is then an exact
   (type-B, since [C*, C] = P - 2n != 0) Goldstone pair of the broken u(3), at zero cost. So A's gap is the explicit
   u(3) breaking: a pseudo-Goldstone doublet (prior art: composite Higgs as a pseudo-Goldstone boson). Its gap is
   tuned by G_S - G_D and K_chi - K_psi, and it closes where the doublet would condense.
3. If the doublet does condense (omega_D -> 0 and below), the condensed directions are of the rotor kind; whether (iii)
   applies needs [C, C*] to be a function of the charges on the relevant sectors (A's ladder says it is, P - 2n, on the
   singlet band).

## Final read of attack-A.md (end of round)
A's results (computed, exploration; exact certification planned): Schwinger band of the three-mode floor,
E(n_S, n_1, n_2), the doublet quantum C_2 with omega_D = (K_chi - K_psi) + (G_S - G_D)(Omega - P + 1), the collective
doublet G_D(Omega - P + 1) below the G_D = 0 threshold, trion levels below it for P > Omega - 2. No overlap with my two
proposals: neither files A's model or its spectrum; my (iii) does not cover A's model (it is not of the one-field
pairing form), and my P2 (ii) is on a null generator's window, A's C_2 algebra on a floor. My points 1 to 3 above stand
as the adversarial reading of A's gapped doublet (unbroken isospin; pseudo-Goldstone of the u(3) point; rotor once it
condenses).

## Answer (one paragraph)
Parity does not exclude an even composite doublet: an even doublet needs exactly an odd number of singlet factors (the
doublet-singlet bilinears, with Y_s fixed by Y_d), which generalises the rung field's no-even-doublet result (proved).
Its components are never exact bosons on a generator: each is charged (T_3 = +-1/2), nilpotent, a quasi-spin of
capacity q rank(M), canonical only in a contraction (proved, via the stored helicity-one argument). On gaps: for any
pairing-type element whose pair commutator is a function of the charges, the sector ground energies have second
difference at most G times its step (the finite Goldstone bound, proved); on the single shell this is 2G and is
attained, so with a condensate the uniform pair channel is a rotor within 2G, at most 2/n_b of the pair-breaking
threshold (4E/n_b at fixed gap), with no weight at the threshold, while without a condensate the bound pair is gapped
at 2K - G n_b and the gap closes exactly where condensation starts (proved). A finite order parameter needs a
degenerate eigenspace across sectors (proved). So a gapped composite doublet survives only while it does not
condense, as in A's construction on a singlet condensate, where its gap is the explicit breaking of a u(3) point at
which it is a Goldstone pair (computed by A, read here as argued); the doublet that condenses supplies rotor
directions. Not settled: a Goldstone bound for the doublet floor and for two coupled condensates, where [X, X*]
carries the isospin hopping (the doublet floor's condensed ground state is not on its symmetric band, computed).

## Decisions for Leon
1. Whether the store should carry a general finite Goldstone statement (proposal 1 (i) to (iii)) as the
   reference for later composite-scalar work, or only the single-shell clause (iv). Recommendation: keep both; (iii)
   is what any two-condensate model will need for its Goldstone directions.
2. Reading of the problem after this run (argued): a composite doublet on the tower is not excluded by parity, but it
   is gapped only while it does not condense; the one that condenses supplies rotor (Goldstone) directions. So a
   composite Higgs needs a second, non-condensing (or pseudo-Goldstone) doublet for the gapped scalar, which mirrors the
   elementary working branch's heavy second doublet. Recommendation: record this as the status of item 6, with the
   explicit gaps from A.
3. Proposal 2 clause (ii) is the stored helicity-one theorem read with isospin and hypercharge weights. If the
   referees judge it a restatement, drop (ii) and keep (i) alone; recommendation: keep it, since it is the doublet's
   statistics obstruction stated where the problem needs it.
4. No new imported Facts, postulates or assumes edges are requested. Prior art cited from memory in the notes
   (Goldstone; Goldstone, Salam and Weinberg; Nambu; Anderson's tower of states; Kerman) is orientation only.
