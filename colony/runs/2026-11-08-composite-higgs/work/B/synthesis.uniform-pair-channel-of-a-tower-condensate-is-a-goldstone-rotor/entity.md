---
id: synthesis.uniform-pair-channel-of-a-tower-condensate-is-a-goldstone-rotor
kind: claim
version: 1
title: 'Finite Goldstone bound: a pairing-type condensate''s uniform pair channel is a rotor'
status: proved
region: synthesis
subject: quantum-fields
tags: [symmetry-breaking, car-algebra, mass-generation, no-go]
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
  - tower.ladder-pairs-satisfy-car-vectors@4
  - tower.structure-tower-c-norms@10
  - field-theory.imported-tower-limit@3
  - field-theory.how-close-tower-comes-ccr@4
  - field-theory.composite-scalars-mean-field-level@5
  - synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_no_order_parameter_in_a_sector
- kind: check
  ref: check.py::check_variational_bounds_on_every_sector
- kind: check
  ref: check.py::check_single_shell_rotor_and_uniform_channel
- kind: check
  ref: check.py::check_collective_limit_at_fixed_gap
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.rung-field-is-odd-in-the-tower-and-its-modes-carry-no-even-doublet
  - synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves
extraction:
  open_problem: op.qft-bosons-and-the-rung-field
  note: >-
    Adversarial attack on the problem's last two items (a gapped helicity-zero composite scalar from tower pairing,
    beyond mean field). Question: when a tower condensate breaks a continuous symmetry, is the uniform pair mode
    necessarily gapless, and with what finite-size splitting? Answer, exactly: (i) a charged field has no
    expectation in any sector vector, so a finite order parameter needs an eigenspace of H that meets two sectors;
    (ii) the variational bound on the sector ground energies by a charged field; (iii) for a pairing-type element
    H_0 - G X X* with [H_0, X] = eps X and [X, X*] a function of the charges, the second difference of the sector
    ground energies is at most G times the step of that function, whatever the size, and with the ground state in a
    sector on which neither X nor X* vanishes both neighbouring levels lie in [0, that bound]: a finite Goldstone
    (rotor) bound, a gaplessness statement only where G times the step of c tends to 0; (iv) on the stored single shell the bound is 2G and is attained, the ground state is the band state
    nearest gamma = (n_b + 1)/2 - K/G, and with a condensate the uniform channel P + P* has all its weight on the two
    neighbouring band levels, within 2G, the rotor over the stored pair-breaking threshold G n_b being at most
    2/n_b (4E/n_b at fixed mean-field gap E); without a condensate the bound pair is gapped at 2K - G n_b and the gap
    closes exactly at the condensation threshold; the finite floor's ground state carries <P> != 0 only at the
    degenerate couplings K/G = n_b/2 - n. Stored and cited, not refiled: the single-shell spectrum and the threshold
    G n_b = 2E (synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy), the band and the
    condensation threshold G > 2K/n_b (field-theory.composite-scalars-mean-field-level), the quasi-spin ladder
    (field-theory.how-close-tower-comes-ccr), and the fact that the uniform channel P + P* moves only along the band
    and does not reach the threshold (synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy
    (ii)); the adjoint v* = w is that of tower.structure-tower-c-norms. New here: the general clauses (i) to (iii),
    and in (iv) the global ground state, the rotor values and their bound, the explicit quasi-spin norms of the two
    neighbouring components, the symmetric-phase bound pair and the degenerate couplings. The doublet floor (two doublet modes and a singlet per block, uniform fields
    closing as u(3)) is not of the form (iii), since [P_a, P_b*] = delta_ab(n_b - N_s) - E_ba carries the isospin
    hopping; it is left to the constructive side, with one finding recorded in the run: in the condensed regime its
    ground state is not on the symmetric band (exact on the n_b = 2, 3 floors). Prior art, orientation only, cited
    from memory: the Goldstone theorem (Goldstone 1961; Goldstone, Salam and Weinberg 1962), Nambu's broken-symmetry
    pairing (Nambu 1960), the tower of states of a finite system with a broken continuous symmetry (Anderson 1952), the pairing-rotational
    band E(n) = G(n - gamma)^2 - G gamma^2 of nuclear physics, with a moment of inertia set by 1/G (Bes and Broglia,
    Nucl. Phys. 80 (1966) 289; Bohr and Mottelson, Nuclear Structure II),
    the quasi-spin solution of the degenerate pairing model (Kerman 1961, imported in
    synthesis.imported-quasi-spin-pairing-and-top-condensation, not used here). Ledger: transport-absent (finite CAR
    on tower planes; no transport completion used).
---

## formal
Let the modes be tower planes, $a^{*} = v$, $a = w$, satisfying the canonical anticommutation relations (Theorem \claimref{tower.ladder-pairs-satisfy-car-vectors}, Fact \claimref{field-theory.imported-tower-limit}) on the Fock space $\mathcal{F}$, with its positive inner product and the adjoint $*$ ($v^{*} = w$, Theorem \claimref{tower.structure-tower-c-norms}). Let $Q_{1}, \dots, Q_{r}$ be commuting self-adjoint elements (charges) and $H$ a self-adjoint element commuting with each; a \emph{sector} is a nonzero joint eigenspace $\mathcal{F}_{s}$ ($Q_{i} = s_{i}$), and $E(s)$ is the lowest eigenvalue of $H$ on it. An element $X$ has charge $h \in \mathbb{R}^{r}$ if $[Q_{i}, X] = h_{i}X$ for all $i$; then $X\mathcal{F}_{s} \subset \mathcal{F}_{s+h}$ and $X^{*}$ has charge $-h$.
\begin{enumerate}
\item[(i)] \emph{(No order parameter in a sector.)} If $h \ne 0$, $\langle\psi, X\psi\rangle = 0$ for every $\psi$ in a sector. A one-dimensional eigenspace of $H$ lies in a sector; so an eigenvector $\psi$ of $H$ with $\langle\psi, X\psi\rangle \ne 0$ exists only if the eigenspace meets two sectors $s$ and $s + h$.
\item[(ii)] \emph{(Variational bound.)} Let $\psi \in \mathcal{F}_{s}$, $H\psi = E(s)\psi$. If $X\psi \ne 0$, $E(s + h) - E(s) \le \langle X\psi, [H, X]\psi\rangle/\langle X\psi, X\psi\rangle$; if $X^{*}\psi \ne 0$, $E(s - h) - E(s) \le \langle X^{*}\psi, [H, X^{*}]\psi\rangle/\langle X^{*}\psi, X^{*}\psi\rangle$; each with equality exactly when $X\psi$ (respectively $X^{*}\psi$) is a lowest eigenvector of its sector.
\item[(iii)] \emph{(Finite Goldstone bound for pairing-type elements.)} Let $H = H_{0} - GXX^{*}$, $G > 0$, $H_{0}$ self-adjoint commuting with the charges and $[H_{0}, X] = \varepsilon X$, $\varepsilon$ real, and let $C = [X, X^{*}]$ act on each sector as a scalar $c(s)$. Then the two quotients of (ii) are $\varepsilon + Gc(s)$ and $-\varepsilon - Gc(s - h)$, so whenever $X\psi \ne 0 \ne X^{*}\psi$,
\[
E(s + h) + E(s - h) - 2E(s) \le G\bigl(c(s) - c(s - h)\bigr) ,
\]
and if the ground state of $H$ lies in $\mathcal{F}_{s^{*}}$ with $X\psi \ne 0 \ne X^{*}\psi$, both $E(s^{*} \pm h) - E(s^{*})$ lie in $[0, G(c(s^{*}) - c(s^{*} - h))]$.
\item[(iv)] \emph{(The single shell.)} For the stored element $H_{4} = \sum_{b}K(n_{a} + n_{c}) - GP^{*}P$, $P = \sum_{b}w_{a}w_{c}$, on $n_{b} \ge 2$ blocks, $K \ge 0$, $G > 0$ (Proposition \claimref{field-theory.composite-scalars-mean-field-level}(2)), with charges $N_{a}, N_{c}$ and $X = P^{*}$ ($h = (1, 1)$, $\varepsilon = 2K$, $C = N_{a} + N_{c} - n_{b}$), the bound of (iii) is $2G$ and is attained. The ground energy of $H_{4}$ is $\min_{n}E(n)$, $E(n) = 2Kn - Gn(n_{b} - n + 1) = G(n - \gamma)^{2} - G\gamma^{2}$, $\gamma = (n_{b} + 1)/2 - K/G$, attained at the band vector $\psi_{n^{*}} = (P^{*})^{n^{*}}\Omega$, $n^{*}$ an integer in $[0, n_{b} - 1]$ nearest $\gamma$ (and $0$ if $\gamma < \tfrac12$); the ground eigenspace is spanned by the $\psi_{n}$ with $E(n) = \min E$.
\begin{enumerate}
\item[(a)] \emph{(Condensed: $Gn_{b} > 2K$.)} $n^{*} \ge 1$, $E(n^{*} \pm 1) - E(n^{*}) = G(1 \pm 2(n^{*} - \gamma)) \in [0, 2G]$ with sum $2G$, and $(P + P^{*})\psi_{n^{*}} = \psi_{n^{*}+1} + n^{*}(n_{b} - n^{*} + 1)\psi_{n^{*}-1}$, $\|P^{*}\psi_{n^{*}}\|^{2} = (n^{*} + 1)(n_{b} - n^{*})\|\psi_{n^{*}}\|^{2}$, $\|P\psi_{n^{*}}\|^{2} = n^{*}(n_{b} - n^{*} + 1)\|\psi_{n^{*}}\|^{2}$: the uniform pair channel has all its weight on the two neighbouring band levels. Against the pair-breaking threshold $Gn_{b}$ at fixed numbers (Theorem \claimref{synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy}(ii)) the larger of the two is at most $2/n_{b}$ of it, and at the gap equation $Gn_{b} = 2E$ it is at most $4E/n_{b}$, which tends to $0$ as $n_{b} \to \infty$ at fixed $E$ while the threshold stays $2E$.
\item[(b)] \emph{(Symmetric: $Gn_{b} < 2K$.)} $\Omega$ is the unique ground state, and $P^{*}\Omega$ is an eigenvector at $2K - Gn_{b} > 0$, below the broken-pair level $2K$ of the same sector: the uniform pair is gapped, and its gap closes exactly at the condensation threshold $Gn_{b} = 2K$.
\item[(c)] \emph{(Degenerate couplings.)} At $K/G = n_{b}/2 - n$, $n \in \{0, \dots, \lfloor n_{b}/2\rfloor\}$ (so that $K \ge 0$), $E(n) = E(n + 1) = \min E$ and $\psi = \psi_{n} + \psi_{n+1}$ is a ground state with $\langle\psi, P\psi\rangle = (n + 1)(n_{b} - n)\|\psi_{n}\|^{2} \ne 0$; at every other coupling every ground state of $H_{4}$ has $\langle P\rangle = 0$.
\end{enumerate}
\end{enumerate}
Clauses (i) to (iv) are proved. \emph{Reading (argued).} With a condensate the uniform helicity-zero composite scalar of a floor is the Goldstone rotor of the broken pair phase, the finite-size form of the flat phase direction of Proposition \claimref{field-theory.composite-scalars-mean-field-level}(4): gapless in the collective limit at fixed mean-field gap, with no weight at the pair-breaking threshold. A gapped uniform composite exists only without a condensate. For a composite Higgs doublet, (i) applies to every charge the doublet carries, and the directions of its broken charges are of this rotor kind where (iii) applies; a gapped composite doublet would then have to be one that does not condense, or a mode outside the condensate's pair channel (such as a particle-number-conserving hopping doublet). The doublet floor and inter-condensate couplings, where $[X, X^{*}]$ is not a function of the charges, are not treated here.

## technical
For pairing-type elements, whose pair commutator $[X, X^{*}]$ is a function of the charges: take tower modes on their Fock space, a set of commuting charges and a Hamiltonian commuting with them; sectors are the joint eigenspaces and $E(s)$ the lowest energy in sector $s$. (i) A field of nonzero charge has no expectation in any vector of one sector, so a finite system shows an order parameter only in an energy eigenspace that spans two sectors. (ii) Applying a charged field $X$ to a lowest vector of sector $s$ gives a trial vector for sector $s + h$, so $E(s + h) - E(s)$ is at most $\langle X\psi, [H, X]\psi\rangle/\|X\psi\|^{2}$, and likewise downwards with $X^{*}$. (iii) For $H = H_{0} - GXX^{*}$ with $[H_{0}, X] = \varepsilon X$ and $[X, X^{*}]$ equal to a function $c$ of the charges, the two quotients are $\varepsilon + Gc(s)$ and $-\varepsilon - Gc(s - h)$, so the second difference of the sector ground energies is at most $G(c(s) - c(s - h))$ at every size, and if the ground state's sector is one where $X$ and $X^{*}$ both act nontrivially both neighbouring sector energies are within that bound. (iv) For the stored single-shell pairing element, $c$ steps by $2$, so the bound is $2G$, and it is attained: the band $E(n) = G(n - \gamma)^{2} - G\gamma^{2}$ with $\gamma = (n_{b} + 1)/2 - K/G$ holds the ground state at the integer nearest $\gamma$. With a condensate ($Gn_{b} > 2K$) the two neighbouring band levels are within $2G$, they carry all of $(P + P^{*})\psi$, and against the pair-breaking threshold $Gn_{b} = 2E$ they are at most $2/n_{b}$ of it ($4E/n_{b}$ at fixed $E$). Without one ($Gn_{b} < 2K$) the vacuum is the unique ground state and the bound pair sits at $2K - Gn_{b}$, below the broken-pair level $2K$, closing at the condensation threshold. Only at the degenerate couplings $K/G = n_{b}/2 - n$ does a ground state carry $\langle P\rangle \ne 0$. The doublet floor and coupled condensates, where $[X, X^{*}]$ is not a function of the charges, are not covered. Reading (argued): for pairing-type elements a condensate's uniform composite scalar is its Goldstone rotor, and a gapped uniform composite needs no condensate; a gapped composite doublet would have to be a doublet that does not condense, or a mode outside the condensate's pair channel (such as a particle-number-conserving hopping doublet).

## lay
When fermions pair up and the pairs condense, the condensate picks a phase, and changing that phase costs no energy in the idealised infinite system: the textbook Goldstone mode. This result asks what happens on a finite stack of the tower's modes, where everything is exact. The uniform pair mode then does not become a separate massive particle: all of its response sits on two neighbouring levels whose spacing shrinks in proportion to one over the number of pair sites, while the energy needed to break a pair stays fixed. In this model a genuinely gapped uniform pair state exists only when nothing condenses. The result covers this kind of pairing only: it does not cover a doublet of paired fermions on one stack, or two condensates coupled to each other, where the pairs' bookkeeping depends on more than the charges. As a reading (argued, on this model), a composite Higgs built from a condensate of this kind would not be the condensate's own uniform pair mode; it would have to be a mode outside that pair channel, or a doublet that does not condense.

## one-liner
For a pairing-type tower element ([X, X*] a function of the charges) the sector ground energies have second difference at most G times the step of [X, X*]; on the single shell this is 2G, so a condensate's uniform pair channel is a rotor within 2G (at most 2/n_b of the pair-breaking threshold), and only without a condensate is the bound pair gapped, at 2K - G n_b.
