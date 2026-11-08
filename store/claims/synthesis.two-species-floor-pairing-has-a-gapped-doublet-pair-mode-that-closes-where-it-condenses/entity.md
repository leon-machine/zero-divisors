---
id: synthesis.two-species-floor-pairing-has-a-gapped-doublet-pair-mode-that-closes-where-it-condenses
kind: claim
version: 1
title: "Two-species floor band: the doublet pair mode is gapped until the band's doublet condenses"
status: proved
region: synthesis
subject: quantum-fields
tags: [pairing-and-bogoliubov, symmetry-breaking, finite-models, limits]
proposed_by:
  kind: ai
  session: 2026-11-08-composite-higgs
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-08-composite-higgs
review: draft
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - field-theory.imported-tower-limit@3
  - field-theory.composite-scalars-mean-field-level@5
  - synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy@2
  - synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower@1
  - field-theory.how-close-tower-comes-ccr@4
  - synthesis.rung-field-is-odd-in-the-tower-and-its-modes-carry-no-even-doublet@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_block_algebra_in_the_tower_planes
- kind: check
  ref: check.py::check_symmetric_band_spectrum_and_isospin
- kind: check
  ref: check.py::check_doublet_quanta_ladder_charges_and_canonical_defect
- kind: check
  ref: check.py::check_condensed_doublet_is_degenerate_and_has_no_subthreshold_amplitude
- kind: check
  ref: check.py::check_casimir_identity_for_the_pair_sum
- kind: check
  ref: check.py::check_threshold_binding_and_the_pair_sum_spectrum
- kind: check
  ref: check.py::check_lowest_doublet_level_and_its_separation
- kind: check
  ref: check.py::check_band_need_not_hold_the_ground_state_and_condensate_levels_below_threshold
- kind: proof
  derivation: main
extraction:
  open_problem: op.qft-bosons-and-the-rung-field
  note: >-
    Attack on op.qft-bosons-and-the-rung-field, items 5 and 6 (the light multi-species composite; a gapped
    helicity-zero composite doublet with the exact boson results). The store held the one-species floor (the pairing
    element of field-theory.composite-scalars-mean-field-level and its closed spectrum and pair-breaking gap,
    synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy), the parity statement that a
    doublet of the rung modes alone is odd and that the remaining composite route is a doublet-singlet condensate
    (synthesis.rung-field-is-odd-in-the-tower-and-its-modes-carry-no-even-doublet, step 5, argued there), and the
    kernel unit J of Hermitian boson fields. New to the store: the two-species floor (three tower modes per block, a
    doublet psi and a singlet chi, a singlet pair channel S and a doublet pair channel B) with its exactly solvable
    block-symmetric band at every size; the doublet quanta Z (each turns a singlet pair into a doublet pair), harmonic
    at fixed pair number with quantum omega_D = (K_chi - K_psi) + (G_S - G_D)(n_b - P + 1), isospin one half, even in
    the tower, with the canonical defect 2n/P under the unit J; the dichotomy on the band (gapped while the band's doublet
    does not condense; once it does, an exactly degenerate isospin multiplet and no sub-threshold level of the
    condensate's own isospin in its sector); the
    collective doublet level exactly G_D(n_b - P + 1) below the G_D = 0 threshold; the Casimir identity
    2W = N(n_b + 2) - C_3 - C_O for the equal-coupling pair sum; and the reduction of the lowest level and of the
    continuum of the one-quantum sector to the two largest eigenvalues of W, which are computed exactly for n_b <= 6
    (a general formula is conjectured); and, computed exactly, that the band need not hold the ground state at fixed
    N: with omega_D > 0 a level with N_chi = 2 lies below the singlet band (n_b = 5, 6, 7, P = 3), and with a doublet
    condensate levels of lower isospin lie below the pair-breaking threshold. Prior art, not premises: collective modes of a second pairing channel below
    the pair-breaking threshold of a condensate are the excitons of A. Bardasis and J. R. Schrieffer, Phys. Rev. 121
    (1961) 1050 (cited from memory); the quasi-spin solution of one-shell pairing is Kerman's (as in the stored Fact
    synthesis.imported-quasi-spin-pairing-and-top-condensation); composite Higgs doublets from fermion condensates are
    Nambu-Jona-Lasinio and top-condensation physics (Y. Nambu and G. Jona-Lasinio, Phys. Rev. 122 (1961) 345;
    W. A. Bardeen, C. T. Hill and M. Lindner, Phys. Rev. D 41 (1990) 1647; both cited from memory), and a composite
    Higgs as a pseudo-Goldstone boson of an approximate symmetry is the idea of D. B. Kaplan and H. Georgi,
    Phys. Lett. B 136 (1984) 183 (cited from memory); the Casimir identity is the fermionic form of Howe duality for
    the pair (O(n_b), so(6)) (R. Howe, Trans. Amer. Math. Soc. 313 (1989) 539, cited from memory), whose branching
    would give the general formula for the pair-sum spectrum; none of these is used in the proof. Not claimed: the
    modes carry no momentum or spin label, so helicity is not modelled; there is no hypercharge, colour or gauge field;
    the floor is a single shell; the general-n_b formula for the pair-sum spectrum is conjectured; the global ground
    state at fixed N is not determined: for P <= 2 and n_b = 4, 5 it is the singlet band up to omega_D = 0 and the
    doublet band beyond (in floating point, not part of the proof; at n_b = 3, P = 2 it is neither), but at P = 3 with n_b = 5, 6, 7 a level with N_chi = 2 lies
    below the singlet band although omega_D > 0 (clause (x)), so the gap of (viii) is a gap between sector minima, an
    excitation gap only where the singlet band is the ground state; the doublet-condensed statements concern the band
    and the stretched sector only, and in other sectors at the condensate's numbers levels of lower isospin lie below
    the pair-breaking threshold (clause (x)). Ledger: transport-absent (a finite
    CAR algebra of tower planes); the unit J of the Hermitian fields is the series' (transport-convenient).
---

## formal
Let a floor carry $n_{b} \ge 1$ blocks, block $b$ holding three tower planes with null pairs $v_{i}(b) = \tfrac12(e_{i,b} + f_{i,b})$, $w_{i}(b) = \tfrac12(e_{i,b} - f_{i,b})$, $Q(e_{i,b}) = 1$, $Q(f_{i,b}) = -1$, $i = 1, 2, 3$; they obey the CAR with $v$ creating (Fact \claimref{field-theory.imported-tower-limit}) and $v^{*} = w$; $\Omega_{0}$ is the vector annihilated by every $w_{i}(b)$. Modes $1, 2$ form a doublet $\psi$, mode $3$ a singlet $\chi$. Write $N_{i} = \sum_{b}v_{i}w_{i}$, $N_{\psi} = N_{1} + N_{2}$, $N_{\chi} = N_{3}$, $N = N_{\psi} + N_{\chi}$, $E_{ij} = \sum_{b}v_{i}(b)w_{j}(b)$, isospin $t_{+} = E_{12}$, $t_{-} = E_{21}$, $t_{3} = \tfrac12(N_{1} - N_{2})$ with Casimir $C_{I} = t_{3}^{2} + \tfrac12(t_{+}t_{-} + t_{-}t_{+})$, and $\Gamma$ the fermion parity. Let
\[
S = \sum_{b}w_{1}(b)w_{2}(b),\quad B_{\alpha} = \sum_{b}w_{\alpha}(b)w_{3}(b),\quad H = K_{\psi}N_{\psi} + K_{\chi}N_{\chi} - G_{S}S^{*}S - G_{D}\sum_{\alpha = 1,2}B_{\alpha}^{*}B_{\alpha},
\]
with real $K_{\psi}, K_{\chi}$ and $G_{S}, G_{D} \ge 0$ (on modes $1, 2$ alone, $H$ is the stored pairing element of Proposition \claimref{field-theory.composite-scalars-mean-field-level}(2)); the doublet quanta $Z_{2}^{*} = \sum_{b}w_{1}(b)v_{3}(b)$, $Z_{1}^{*} = \sum_{b}v_{3}(b)w_{2}(b)$; the pair sum $W = S^{*}S + \sum_{\alpha}B_{\alpha}^{*}B_{\alpha}$; and $x(n_{S}, n_{1}, n_{2}) = (S^{*})^{n_{S}}(B_{1}^{*})^{n_{1}}(B_{2}^{*})^{n_{2}}\Omega_{0}$, with $n = n_{1} + n_{2}$ and $P = n_{S} + n$.
\begin{enumerate}
\item[(i)] \emph{(Charges and parity.)} $H$ commutes with $N_{1}$, $N_{2}$, $N_{3}$, $t_{\pm}$ and $\Gamma$. $S$, $B_{\alpha}$ and $Z_{\alpha}$ are even; $[t_{-}, B_{1}^{*}] = B_{2}^{*}$, $[t_{+}, Z_{2}^{*}] = Z_{1}^{*}$, $[t_{+}, B_{1}^{*}] = [t_{+}, Z_{1}^{*}] = [t_{\pm}, S^{*}] = 0$, so $(B_{1}^{*}, B_{2}^{*})$ and $(Z_{1}^{*}, Z_{2}^{*})$ are isospin doublets and $S$ a singlet; $Z_{\alpha}^{*}$ raises $N_{\chi}$ by one and lowers $N_{\psi}$ by one, and $[Z_{\alpha}^{*}, S^{*}] = B_{\alpha}^{*}$.
\item[(ii)] \emph{(The band.)} In one block any two of the pair creators $v_{2}v_{1}$, $v_{3}v_{1}$, $v_{3}v_{2}$ multiply to zero. $x(n_{S}, n_{1}, n_{2}) \neq 0$ exactly when $P \le n_{b}$, and then $Hx = E(n_{S}, n)x$ with
\[
E(n_{S}, n) = K_{\psi}(2n_{S} + n) + K_{\chi}n - (G_{S}n_{S} + G_{D}n)(n_{b} - P + 1);
\]
at fixed $n_{S}$ and $n$ the $n + 1$ vectors span isospin $n/2$ ($C_{I} = \tfrac{n}{2}(\tfrac{n}{2} + 1)$).
\item[(iii)] \emph{(Doublet quanta.)} $Z_{2}^{*}x(P - n, 0, n) = (P - n)\,x(P - n - 1, 0, n + 1)$, $[Z_{2}, Z_{2}^{*}] = N_{1} - N_{3}$, which is $P - 2n$ on $x(P - n, 0, n)$, and $E(P - n, n) = E(P, 0) + n\,\omega_{D}$ with
\[
\omega_{D} = (K_{\chi} - K_{\psi}) + (G_{S} - G_{D})(n_{b} - P + 1),
\]
exactly harmonic at fixed $P$. With $J$ the kernel bivector of a tower level containing these planes, $\phi = Z_{2} + Z_{2}^{*}$ and $\pi = J(Z_{2}^{*} - Z_{2})$ are self-adjoint and $[\phi, \pi] = 2J(N_{1} - N_{3})$, equal to $2(P - 2n)J$ on the ladder.
\item[(iv)] \emph{(Two phases of the band.)} At fixed $P$ the band energy is affine in $n$ with slope $\omega_{D}$, so the two condensates coexist on the band only at $\omega_{D} = 0$. For $\omega_{D} > 0$ the lowest band vector is the singlet band $x(P, 0, 0)$ and each doublet quantum costs $\omega_{D}$. For $\omega_{D} < 0$ it is the doublet band ($n = P$), whose isospin-$P/2$ multiplet is exactly degenerate; $B_{1}^{*}$ and $B_{2}^{*}$ take it to the doublet band of $P + 1$ pairs, both at energy $E(0, P + 1)$; on the band, its excitations at fixed $P$ are return quanta $Z_{2}$, each at $-\omega_{D}$, each carrying two units of $N_{\psi} - N_{\chi}$, a charge the doublet condensate leaves unbroken. In the stretched sector $(N_{1}, N_{2}, N_{3}) = (0, P, P)$, $0 < P < n_{b}$, which holds exactly the levels of isospin $P/2$ at $N_{\psi} = N_{\chi} = P$, the next level lies exactly $G_{D}n_{b}$ above the doublet band, with none between: no level of the condensate's own isospin lies below pair breaking.
\item[(v)] \emph{(Threshold and binding.)} In the one-quantum sector $V_{P} = \{(N_{1}, N_{2}, N_{3}) = (P - 1, P, 1)\}$, $1 \le P \le n_{b}$, the lowest level at $G_{D} = 0$ is $E_{\mathrm{th}} = K_{\psi}(2P - 1) + K_{\chi} - G_{S}(P - 1)(n_{b} - P + 1)$ (a free $\chi$ beside $P - 1$ singlet pairs and an unpaired $\psi_{2}$); the collective level $E_{D} = E(P - 1, 1)$ satisfies $E_{D} = E_{\mathrm{th}} - G_{D}(n_{b} - P + 1)$, $E_{D} - E(P, 0) = \omega_{D}$ and $E_{\mathrm{th}} - E(P, 0) = (K_{\chi} - K_{\psi}) + G_{S}(n_{b} - P + 1)$.
\item[(vi)] \emph{(Casimir identity.)} With $C_{3} = \sum_{i,j}E_{ij}E_{ji}$ and $C_{O} = \sum_{b < c}L_{bc}^{*}L_{bc}$, $L_{bc} = \sum_{i}(v_{i}(b)w_{i}(c) - v_{i}(c)w_{i}(b))$: $2W = N(n_{b} + 2) - C_{3} - C_{O}$, and $C_{O} \ge 0$.
\item[(vii)] \emph{(Reduction.)} Let $G_{S} \ge G_{D} \ge 0$ and let $X \ge X_{2}$ be the two largest eigenvalues of $W$ on $V_{P}$, counted with multiplicity. Every level of $H$ on $V_{P}$ is at least $E_{D} - G_{D}(X - P(n_{b} - P + 1))$, and every level but the lowest is at least $E_{\mathrm{th}} - G_{D}(X_{2} - (P - 1)(n_{b} - P + 1))$.
\item[(viii)] \emph{(Computed.)} For $n_{b} \le 6$ and every $P$: $X = (P - 1)(n_{b} - P + 1) + \max(n_{b} - P + 1, 3)$ for $P \ge 2$, $X = n_{b}$ for $P = 1$; and when $n_{b} - P + 1 > 3$ or $P = 1$, $X = P(n_{b} - P + 1)$ is simple and $X_{2} = (P - 1)(n_{b} - P + 1) + 3$ ($X_{2} = 0$ for $P = 1$). Hence, for $n_{b} \le 6$ and $G_{S} \ge G_{D} \ge 0$: if $n_{b} - P + 1 \ge 3$ the lowest level of $V_{P}$ is $E_{D}$, so the doublet gap at $N = 2P$, the gap between sector minima (lowest level with $N_{\chi} = 1$ less lowest level with $N_{\chi} = 0$, which is $E(P, 0)$), is exactly $\omega_{D}$; if $n_{b} - P + 1 > 3$ every other level lies at or above $E_{\mathrm{th}} - 3G_{D}$, so $E_{D}$ is split off by at least $G_{D}(n_{b} - P - 2)$; if $n_{b} - P + 1 < 3$ no level lies below $E_{D} - (P + 2 - n_{b})G_{D}$, and at $P = n_{b}$ that value is a level (a block holding all three modes). The formulas for $X$ and $X_{2}$ are conjectured for every $n_{b}$.
\item[(ix)] \emph{(The infinite floor.)} With $G_{S} = g_{S}/n_{b}$ and $G_{D} = g_{D}/n_{b}$, exactly $\omega_{D} = (K_{\chi} - K_{\psi}) + (g_{S} - g_{D})(1 - P/n_{b} + 1/n_{b})$, so at $P/n_{b} = f$ it differs from its limit $(K_{\chi} - K_{\psi}) + (g_{S} - g_{D})(1 - f)$ by exactly $(g_{S} - g_{D})/n_{b}$; the binding is $g_{D}(1 - f + 1/n_{b})$; and $\Phi = \phi/\sqrt{2P}$, $\Pi = \pi/\sqrt{2P}$ satisfy $[\Phi, \Pi] = (1 - 2n/P)J$ on the ladder. Under the conjecture in (viii), for $P \le n_{b} - 2$ the doublet gap is $\omega_{D}$ with no error, and for $P \le n_{b} - 3$ the rest of $V_{P}$ lies at or above $E_{\mathrm{th}} - 3g_{D}/n_{b}$.
\item[(x)] \emph{(Off the band, computed.)} The band need not hold the ground state at fixed $N$. At $K_{\psi} = K_{\chi} = 0$, $G_{S} = 1$ and $(n_{b}, P, G_{D}) = (5, 3, \tfrac12), (6, 3, \tfrac45), (7, 3, \tfrac{9}{10})$, where $\omega_{D} > 0$ and $n_{b} - P + 1 \ge 3$, the sector $(2, 2, 2)$ (two $\chi$ particles) has a level below the singlet band $E(P, 0)$, which is the lowest level with $N_{\chi} = 0$: so the gap of (viii) is a gap between sector minima, and an excitation gap of the ground state only where the singlet band is the ground state at $N = 2P$. At $K = 0$, $G_{S} = 1$, $G_{D} = 3$ ($\omega_{D} < 0$) and $(n_{b}, P) = (4, 2), (5, 2)$, the stretched sector has one level below the pair-breaking threshold $E(0, P) + G_{D}n_{b}$ while the sector $(1, P - 1, P)$, at the same $N_{\psi}$ and $N_{\chi}$, has $n_{b}^{2}$ ($16$, $25$), all but one of isospin below $P/2$, and none below the doublet band.
\end{enumerate}
Clauses (i) to (vii) and (ix) without its last sentence are proved for every $n_{b}$; (viii) is proved by exact computation for $n_{b} \le 6$ and conjectured beyond; (x) is computed exactly at the couplings listed. \emph{Reading (argued).} The doublet quantum is the doublet-singlet composite of \claimref{synthesis.rung-field-is-odd-in-the-tower-and-its-modes-carry-no-even-doublet} (step 5), realised exactly: an even, helicity-unmodelled scalar doublet, bound below the pair-breaking threshold for every $G_{D} > 0$; where the singlet band is the ground state, isospin is unbroken and the doublet is a massive composite; it is a pseudo-Goldstone doublet of the point $G_{S} = G_{D}$, $K_{\chi} = K_{\psi}$, where the $Z_{\alpha}$ are symmetry generators and the gap closes, and it is light only near $\omega_{D} = 0$ (at $K_{\chi} = K_{\psi}$, $G_{D}$ near $G_{S}$; then $\omega_{D}/(E_{\mathrm{th}} - E(P, 0)) = 1 - G_{D}/G_{S}$). Once the band's doublet condenses, the band gives an exactly degenerate isospin multiplet and no level of the condensate's isospin below the pair-breaking threshold. So on the band no gapped doublet neutral under the unbroken $N_{\psi} - N_{\chi}$ accompanies a doublet condensate; the return quanta are gapped doublets charged under it. Off the band the ground state at fixed $N$ can change (clause (x)), so these statements concern the band. Being even in the tower the quantum is not the rung field, which is odd.

## technical
Put three tower modes in every block of a floor: a doublet $\psi_{1}, \psi_{2}$ and a singlet $\chi$. Two pair channels act: the singlet pair $\psi_{1}\psi_{2}$ with coupling $G_{S}$ and the doublet pairs $\psi_{\alpha}\chi$ with coupling $G_{D}$. Because any two pairs in one block share a mode, a block holds at most one pair, of one of three kinds, and on the block-symmetric even states the model is a three-kind version of the one-shell pairing band: the energy is $K_{\psi}(2n_{S} + n) + K_{\chi}n - (G_{S}n_{S} + G_{D}n)(n_{b} - P + 1)$, with $n_{S}$ singlet pairs, $n$ doublet pairs (isospin $n/2$) and $P$ pairs in all.

The operator $Z_{2}^{*} = \sum_{b}w_{1}v_{3}$ turns a singlet pair into a doublet pair. On the singlet band it creates a harmonic ladder of doublet quanta of energy $\omega_{D} = (K_{\chi} - K_{\psi}) + (G_{S} - G_{D})(n_{b} - P + 1)$ each, with $[Z_{2}, Z_{2}^{*}] = N_{1} - N_{\chi}$ ($P - 2n$ on the ladder), so with the kernel unit $J$ the Hermitian fields are canonical up to the defect $2n/P$. The quantum is even, an isospin doublet, and moves one unit from $\psi$ to $\chi$. On the band, if $\omega_{D} > 0$ the doublet is gapped and does not condense; if $\omega_{D} < 0$ the doublet band is lower, its isospin multiplet is exactly degenerate, both components add pairs alike, and in its own sector the next level is the pair-breaking one at $G_{D}n_{b}$. The band need not be the ground state at fixed $N$: computed exactly, a level with two $\chi$ lies below the singlet band at $P = 3$ for $n_{b} = 5, 6, 7$ although $\omega_{D} > 0$, so the doublet gap is one between sector minima; and with a doublet condensate, levels of lower isospin at the condensate's numbers lie below the pair-breaking threshold.

In the sector of one doublet quantum the collective level lies $G_{D}(n_{b} - P + 1)$ below the energy of a free $\chi$ beside a broken pair. Writing $H$ as a constant minus $(G_{S} - G_{D})S^{*}S$ minus $G_{D}W$, with $W$ the equal-coupling pair sum, bounds the whole sector by the two largest eigenvalues of $W$, and $2W = N(n_{b} + 2) - C_{3} - C_{O}$ (flavour and block-rotation Casimirs). Computed exactly for up to six blocks: below $n_{b} - 2$ pairs the collective level is the lowest and every other level is within $3G_{D}$ of the threshold or above; with more pairs a block holding all three modes lies lower by at most $2G_{D}$. With couplings $g/n_{b}$ the gap tends to $(K_{\chi} - K_{\psi}) + (g_{S} - g_{D})(1 - f)$ with error $(g_{S} - g_{D})/n_{b}$.

## lay
The series has asked whether the Higgs particle could be made of other particles bound together, the way a Cooper pair is made of two electrons. A single kind of particle on one energy shell was already known not to work. This result builds the simplest two-kind model on the series' tower: one kind comes in two versions (a doublet, like the Higgs's charges), the other in one version. Pairs can form in two ways; the model's symmetric band can be solved exactly, and the rest is computed for up to six blocks. One kind of pair can turn into the other, and that change behaves like a particle with the Higgs doublet's charges. On the band it costs energy, so it has a mass, only while the doublet pairs themselves do not take over. The mass shrinks to zero as the two pairing strengths become equal and the two kinds have the same energy. Once the doublet pairs do take over the band, the doublet's directions cost nothing and no extra bound state of the condensate's own isospin appears below the energy needed to break a pair. The band is not always the lowest-energy arrangement, though: for some strengths other arrangements lie lower. Read on the band (an interpretation, not a proof), the model gives either a massive composite doublet or a condensed one, not a condensed doublet together with a light neutral bound scalar of the Higgs kind.

## one-liner
On a floor whose blocks hold a doublet and a singlet tower mode, the block-symmetric band is exact, $E = K_{\psi}(2n_{S} + n) + K_{\chi}n - (G_{S}n_{S} + G_{D}n)(n_{b} - P + 1)$, and the even doublet quanta $\sum w_{1}v_{3}$ are harmonic with gap $\omega_{D} = (K_{\chi} - K_{\psi}) + (G_{S} - G_{D})(n_{b} - P + 1)$, a bound state $G_{D}(n_{b} - P + 1)$ below threshold (the lowest level for $n_{b} - P \ge 2$, computed for $n_{b} \le 6$); on the band, for $\omega_{D} < 0$ the doublet condenses into an exactly degenerate multiplet with no sub-threshold level of the condensate's isospin; the band need not hold the ground state at fixed $N$, even for $\omega_{D} > 0$.
