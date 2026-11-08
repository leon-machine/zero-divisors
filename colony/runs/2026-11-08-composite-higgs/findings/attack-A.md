# Attack A (constructive): the two-species pairing floor and its doublet pair mode

Target: op.qft-bosons-and-the-rung-field, attack items 5 and 6.
Status: done. One proposal filed (gate clean).

## Orientation
Read: RUN.md, BRIEF, POLICIES, the problem (incl. the 8 November paragraph), and the stored entities RUN.md lists:
pairing gap (one species, one shell: band, pair-breaking gap G n_b = 2E), composite-scalars mean field, rung-odd
(even doublet needs an odd factor from outside the rung planes, clause (3); its argued step 5 names the
doublet-singlet route b_a = n^{-1/2} sum v_{a,j} u_j), kernel bivector (unit J; collective pairs with defect 2j/M),
density modes along one null direction, Sugawara/Luttinger, central limit, locality. Read attack-B.md at orientation,
midway and at the end.

## Model
Floor of n_b blocks; block b holds tower modes psi_1(b), psi_2(b) (a doublet) and chi(b) (a singlet).
S = sum_b w_1 w_2 (isospin-singlet pair), B_a = sum_b w_a w_chi (doublet pair),
H = K_psi N_psi + K_chi N_chi - G_S S*S - G_D sum_a B_a* B_a. On modes 1, 2 alone it is the stored pairing element.

## Routes
1. (the problem's own) Two-condensate pairing on one shell, exact spectrum by sector. Chosen.
2. (another subject: kernel-bivector collective pairs, Sugawara) doublet quanta as transfers between pair kinds; the
   stored Hermitian-field lemma (unit J) gives the canonical defect. Folded into 1.
3. (own) Compare with the equal-coupling point: H = const - (G_S - G_D) S*S - G_D W on a fixed-number sector, W the
   pair sum; bound the sector by the two largest eigenvalues of W (Weyl). Folded into 1.
Kill condition (pre-registered before computing): the lowest level of the one-quantum doublet sector is not reached
by any doublet pair operator from the singlet band, or it does not lie below the G_D = 0 threshold by an amount growing
with n_b at fixed filling. Not triggered: the collective level is reached (Z_2* from the singlet band, B_2* from the
band with one pair fewer), its binding is G_D(n_b - P + 1), and below n_b - 2 pairs it is the lowest level (computed
for n_b <= 6).

## Results (labelled)
PROVED (every n_b):
- (ii) any two pair creators of one block multiply to zero, so the block-symmetric even states are a three-kind
  boson (Schwinger) band: E(n_S, n) = K_psi(2 n_S + n) + K_chi n - (G_S n_S + G_D n)(n_b - P + 1), isospin n/2.
- (iii) doublet quanta Z_2* = sum w_1 v_chi (turn a singlet pair into a doublet pair): Z_2* x_n = (P - n) x_{n+1},
  exactly harmonic at fixed P with omega_D = (K_chi - K_psi) + (G_S - G_D)(n_b - P + 1); [Z_2, Z_2*] = N_1 - N_chi
  (P - 2n on the ladder); with the kernel unit J, [Phi, Pi] = (1 - 2n/P) J. Charges: isospin 1/2, N_chi + 1,
  N_psi - 1; even in the tower.
- (iv) on the band the energy is affine in the number of doublet pairs, so the two condensates coexist only at
  omega_D = 0. omega_D > 0: singlet band lowest, doublet gapped. omega_D < 0: doublet band, its isospin multiplet
  exactly degenerate, both components add pairs alike, the return quantum (at -omega_D) carries two units of the
  unbroken N_psi - N_chi; stretched sector (0, P, P): next level exactly G_D n_b up, none between (stored result).
- (v) collective level E_D = E_th - G_D(n_b - P + 1), E_th the G_D = 0 threshold (free chi beside an unpaired psi);
  E_D - E(P, 0) = omega_D.
- (vi) Casimir identity 2W = N(n_b + 2) - C_3 - C_O (flavour and block-rotation Casimirs), by normal ordering.
- (vii) reduction: for G_S >= G_D, levels >= E_D - G_D(X - P(n_b - P + 1)); second level >= E_th - G_D(X_2 - (P-1)(n_b-P+1)).
COMPUTED (exact inertia, n_b <= 6, every P): X = (P-1)(n_b-P+1) + max(n_b-P+1, 3), X_2 = (P-1)(n_b-P+1) + 3. So for
  n_b - P >= 2 the doublet gap at fixed N is exactly omega_D, and for n_b - P >= 3 the bound state is split off by
  >= G_D(n_b - P - 2) (rest >= E_th - 3 G_D). Above n_b - 2 pairs a block holding all three modes lies lower, by at
  most (P + 2 - n_b) G_D (attained at P = n_b). H inertia confirms directly for n_b <= 5.
CONJECTURED: the X, X_2 formulas for every n_b (argued route: Howe duality branching via (vi); prior art only).
ARGUED (reading): gapped composite doublet only while it does not condense (isospin unbroken, a pseudo-Goldstone of the
  equal-coupling point, light only by tuning G_D to G_S: omega_D / (E_th - E(P,0)) = 1 - G_D/G_S at equal K); once it
  condenses, the band gives a degenerate multiplet and no sub-threshold amplitude level. Even, so not the rung field.
  Helicity is not modelled (modes carry no momentum or spin).

Infinite floor (proved): with G = g/n_b, omega_D = (K_chi - K_psi) + (g_S - g_D)(1 - P/n_b + 1/n_b), error from the limit
exactly (g_S - g_D)/n_b at P = f n_b; binding g_D(1 - f + 1/n_b); canonical defect 2n/P.

## Filed
synthesis.two-species-floor-pairing-has-a-gapped-doublet-pair-mode-that-closes-where-it-condenses
("A two-species floor has a gapped doublet pair mode that closes where it condenses").
Gate: runcheck 7/7 pass; check4 exit 0, 0 errors, 1 other finding (I405 info: the rung-odd premise declared and
untouched, as recorded in coverage.yaml), mutants ok; validate_one ok, no codes (I305 info only); registered with
propose_claim, entity.md, proof-main.tex, check.py identical, coverage.yaml copied.

## Coordination with B
No overlap in filed results: B filed a general finite Goldstone bound with the one-species shell, and a parity
selection rule (an even doublet needs a singlet constituent) with the quasi-spin statement on generators. Small
contact point for referees: my clause (i) states that B_a and Z_a are even doublets in this model; B's selection rule
is the general statement. B's adversarial points (unbroken isospin in my gapped phase; pseudo-Goldstone at the u(3)
point; the doublet-condensed ground state is not on the band) are built into my statement and reading. B's (iii) does
not cover this floor; a Goldstone bound for two coupled condensates stays open.

## Unexpected links
- The three-kind band is the stored one-shell band with the empty blocks shared; the doublet quantum is the stored
  quasi-spin collective pair, exact here as a transfer between two kinds of pair.
- The Casimir identity ties the pair sum to the block-rotation Casimir: the band is the block-rotation-invariant part.

## Decisions for Leon
1. Reading of item 6 (recommendation: record it as the status): on a floor, a gapped even composite doublet exists
   exactly while it does not condense (gap omega_D, a pseudo-Goldstone of the equal-coupling point); a condensed one
   has a degenerate multiplet and no sub-threshold amplitude level on the band. A Higgs-like composite (doublet vev
   plus a light neutral scalar) is not produced; the elementary reading stands, argued.
2. Whether the general-n_b formula for the pair-sum spectrum should be pursued (via the duality of block rotations and
   flavour rotations) as a follow-up open item, which would make (viii) a theorem for every n_b. Recommendation: yes,
   low priority.
3. No new imported Facts, postulates or assumes edges requested. Prior art cited from memory in the extraction note
   (Bardasis-Schrieffer, Nambu-Jona-Lasinio, Bardeen-Hill-Lindner, Kaplan-Georgi, Howe) is orientation only.
