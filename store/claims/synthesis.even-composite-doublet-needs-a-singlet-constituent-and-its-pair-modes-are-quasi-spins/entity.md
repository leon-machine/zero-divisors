---
id: synthesis.even-composite-doublet-needs-a-singlet-constituent-and-its-pair-modes-are-quasi-spins
kind: claim
version: 1
title: 'An even composite doublet needs a singlet constituent, and its pair modes are quasi-spins'
status: proved
region: synthesis
subject: quantum-fields
tags: [car-algebra, bosonisation, symmetry-breaking, no-go]
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
  - synthesis.rung-field-is-odd-in-the-tower-and-its-modes-carry-no-even-doublet@3
  - synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_doublets_are_odd_in_the_doublet_modes
- kind: check
  ref: check.py::check_bilinear_doublets_and_their_hypercharge
- kind: check
  ref: check.py::check_charged_pair_modes_are_quasi_spins
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - field-theory.composite-scalars-mean-field-level
  - synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy
extraction:
  open_problem: op.qft-bosons-and-the-rung-field
  note: >-
    Adversarial attack on the problem's last item: is an even composite doublet excluded on the tower by the rung
    field's oddness, and what charges and statistics can its components have? Answer, exactly: (i) for modes in
    isospin doublets and singlets (any number of species and further labels), the algebra splits by the parities of
    the doublet and the singlet factors, isospin and hypercharge preserve the split, and the T_3 weights on the part
    of doublet parity p_D lie in p_D/2 + Z; so every doublet (every half-integer isospin) is odd in the doublet modes,
    and an even one is odd in the singlet modes: a singlet constituent is necessary, and it is the only condition
    from parity (the four doublet-singlet bilinears are even doublets, with hypercharges +-(Y_d - Y_s) and
    +-(Y_d + Y_s), so hypercharge 1/2 fixes Y_s from Y_d); with one doublet pair of modes the doublet-odd part is
    all of isospin 1/2 and the doublet-even part has isospin 0 and 1, whatever the singlets. This generalises the
    stored no-even-doublet clause (2) of synthesis.rung-field-is-odd-in-the-tower-and-its-modes-carry-no-even-doublet
    (no singlet modes) and makes precise its clause (3) (a spectator factor). (ii) every component of a doublet of
    pair densities on a null generator has T_3 = +-1/2, so its channel matrix is charged under the isospin weights
    (and under the hypercharge weights if Y != 0), hence nilpotent and never normal: no component is a canonical
    boson on the edge-clean vectors, and when M^2 = 0 (for example a single doublet-singlet hopping, or nonzero
    hypercharge with all doublet channels of one hypercharge) on the chiral sea each is a quasi-spin of q rank(M)
    sites (q sites for a doublet-singlet hopping); without M^2 = 0 the count fails (M = E_{up,s} + E_{s,down}, of
    T_3 weight +1/2, has M^2 = E_{up,down} and norms 1, 2, 6, 18 at q = 1); for the hopping doublet the two components having the isospin raising density as their mutual commutator.
    The nilpotency and quasi-spin steps are those of synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins
    (iii), (iv), whose extraction note already records that the weights may be any real numbers; (ii) is that result
    read with the isospin and hypercharge weights, filed here as the doublet's consequence, with the doublet-specific
    values (the edge-clean values q +- 1 and the mutual commutator). Stored and cited, not refiled: the rung-plane
    isospin multiplicities, the window identity, the normality criterion and the quasi-spin norms. The particle-pair
    doublets reduce to hoppings by the particle-hole reflection of the singlet planes (argued in the proof's reading).
    This is about the composite's statistics and charges, not its gap, which is a separate question. Prior art, orientation only, cited from memory: the Yukawa structure of the Standard Model, in which the
    Higgs doublet couples a doublet fermion to a singlet one; the Bardeen-Hill-Lindner and Nambu-Jona-Lasinio
    composites of that form (imported in synthesis.imported-quasi-spin-pairing-and-top-condensation, not used here).
    Elementary representation theory; ledger: transport-absent.
---

## formal
Let the modes be tower planes, $a^{*} = v$, $a = w$, with the canonical anticommutation relations (Theorem \claimref{tower.ladder-pairs-satisfy-car-vectors}) and $v^{*} = w$ (Theorem \claimref{tower.structure-tower-c-norms}), each carrying a channel that is either a member of an isospin doublet, $(\delta, \uparrow)$ or $(\delta, \downarrow)$ ($\delta$ in a finite set of further labels: species, colour, momentum, generation), or a singlet $s \in S$. Let $\mathcal{A}$ be the real algebra they generate, $\mathcal{A}_{D}$ and $\mathcal{A}_{S}$ the subalgebras generated by the doublet and by the singlet modes, and $\mathcal{A}^{(p_{D}, p_{S})}$ the span of the products $xy$ with $x \in \mathcal{A}_{D}$ of parity $p_{D}$ and $y \in \mathcal{A}_{S}$ of parity $p_{S}$. Isospin acts by commutators with $T_{+} = \sum_{\delta}a_{\delta\uparrow}^{*}a_{\delta\downarrow}$, $T_{-} = T_{+}^{*}$, $T_{3} = \tfrac12\sum_{\delta}(n_{\delta\uparrow} - n_{\delta\downarrow})$, with Casimir $C = (\operatorname{ad}T_{3})^{2} + \tfrac12(\operatorname{ad}T_{+}\operatorname{ad}T_{-} + \operatorname{ad}T_{-}\operatorname{ad}T_{+})$; a hypercharge is $Y = \sum_{x}Y_{x}n_{x}$ with real channel weights equal on the two members of each doublet.
\begin{enumerate}
\item[(i)] \emph{(Selection rule.)} $\mathcal{A} = \bigoplus_{p_{D}, p_{S}}\mathcal{A}^{(p_{D}, p_{S})}$, each summand invariant under $\operatorname{ad}T_{j}$ and $\operatorname{ad}Y$, and every eigenvalue of $\operatorname{ad}T_{3}$ on $\mathcal{A}^{(p_{D}, \cdot)}$ lies in $\tfrac12p_{D} + \mathbb{Z}$. Hence every element of half-integer isospin, in particular every doublet, is odd in the doublet modes, and an even one lies in $\mathcal{A}^{(1,1)}$: it is odd in the singlet modes, so it needs $S \ne \emptyset$. For one doublet pair of modes and any singlets, $C = \tfrac34$ on all of $\mathcal{A}^{(1, \cdot)}$, and on $\mathcal{A}^{(0, p_{S})}$ the eigenvalues are $0$ and $2$, the latter with multiplicity $3\dim\mathcal{A}_{S}^{p_{S}}$. The lowest even doublets are the bilinears, for each $\delta$ and $s$ the four (upper, lower) pairs
\[
(a_{\delta\uparrow}^{*}a_{s}, a_{\delta\downarrow}^{*}a_{s}),\quad (a_{s}^{*}a_{\delta\downarrow}, -a_{s}^{*}a_{\delta\uparrow}),\quad (a_{\delta\downarrow}a_{s}, -a_{\delta\uparrow}a_{s}),\quad (a_{s}^{*}a_{\delta\uparrow}^{*}, a_{s}^{*}a_{\delta\downarrow}^{*}),
\]
of hypercharge $Y_{\delta} - Y_{s}$, $Y_{s} - Y_{\delta}$, $-(Y_{\delta} + Y_{s})$, $Y_{\delta} + Y_{s}$: a bilinear doublet of hypercharge $\pm\tfrac12$ needs $|Y_{\delta} - Y_{s}| = \tfrac12$ or $|Y_{\delta} + Y_{s}| = \tfrac12$.
\item[(ii)] \emph{(Pair modes of a doublet are quasi-spins.)} On one null generator, in the notation of Theorem \claimref{synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins} (window $I = \{-N, \dots, N - 1\}$, $\rho_{q}(M) = \sum_{k}a_{k}^{*}Ma_{k+q}$), let $W$ be a diagonal matrix of real channel weights. If $[W, M] = hM$ with $h \ne 0$, $M$ is nilpotent, hence not normal if nonzero, so for $N > q$, $\rho_{q}(M)$ is not a canonical boson on the edge-clean vectors, and if $M^{2} = 0$, $B = \rho_{q}(M)^{*}$ on the chiral sea $\Omega$ has $|B^{p}\Omega|^{2} = (p!)^{2}e_{p}$ over the $q\operatorname{rank}M$ squared singular values, zero for $p > q\operatorname{rank}M$. Every component of a doublet of pair densities has $T_{3} = \pm\tfrac12$, so its matrix satisfies this with the isospin weights ($\pm\tfrac12$ on the members of each doublet, $0$ on singlets), and with the hypercharge weights when its hypercharge is nonzero. For the hopping $M = E_{(\delta\uparrow), s}$: $M^{2} = 0$, $\operatorname{rank}M = 1$, $|B^{p}\Omega|^{2} = (p!)^{2}\binom{q}{p}$; on edge-clean vectors $[\rho_{q}(M), \rho_{q}(M)^{*}]$ is $q + 1$ with one extra bulk particle in channel $\delta\uparrow$ and $q - 1$ with one in channel $s$; and with $M' = E_{(\delta\downarrow), s}$, $[\rho_{q}(M), \rho_{q}(M')^{*}]$ acts on edge-clean vectors as the bulk isospin raising density $\sum_{k\ \mathrm{bulk}}a_{k,\delta\uparrow}^{*}a_{k,\delta\downarrow}$.
\end{enumerate}
Clauses (i) and (ii) are proved. \emph{Reading (argued).} The rung field's oddness does not exclude a composite doublet of two kinds of fermions: the condition is a singlet constituent with matching hypercharge. Particle-pair doublets reduce to hoppings by the particle-hole reflection of the singlet planes. No component of a composite doublet is among the exact (normal, neutral) pair bosons of a generator; each is a quasi-spin of finite capacity, canonical only in a contraction over many sites. This concerns the composite's charges and statistics, not its gap.

## technical
Let tower modes carry isospin-doublet channels and singlet channels. (i) The algebra they generate splits by the parity of the doublet factors and the parity of the singlet factors; isospin and hypercharge act within each part, and on the part with doublet parity $p_{D}$ the isospin-3 weights lie in $p_{D}/2 + \mathbb{Z}$. So every doublet is odd in the doublet modes, and an even doublet is odd in the singlet modes: a composite doublet needs a singlet constituent, and that is the only condition parity imposes. With one doublet pair of modes the doublet-odd part is entirely isospin one-half and the doublet-even part is isospin zero and one. The simplest even doublets are the doublet-singlet bilinears (two hoppings and two pairs), of hypercharge $\pm(Y_{\delta} - Y_{s})$ and $\pm(Y_{\delta} + Y_{s})$, so hypercharge one-half fixes the singlet's hypercharge from the doublet's. (ii) On a null generator a component of a doublet of pair densities has isospin-3 weight $\pm\tfrac12$, so its channel matrix is charged under the isospin weights (and under hypercharge if the doublet has any), hence nilpotent and never normal. As a corollary of the stored helicity-one theorem (\claimref{synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins}(iii), (iv)) read with isospin weights, whose argument uses only real weights, it is never a canonical boson on the edge-clean vectors, and when $M^{2} = 0$ (for example a single doublet-singlet hopping, or nonzero hypercharge with all doublet channels of one hypercharge) on the sea it is a quasi-spin of $q\operatorname{rank}M$ sites; without $M^{2} = 0$ the quasi-spin count can fail. For a doublet-singlet hopping the capacity is $q$, the norms are $(p!)^{2}\binom{q}{p}$, the commutator on edge-clean vectors is $q \pm 1$ according to a bulk particle in the doublet or the singlet channel, and the two components' mutual commutator is the isospin raising density. Reading (argued): the composite doublet is allowed by parity, needs a singlet constituent, and its components are quasi-spins, canonical only in a contraction; its gap is a separate question.

## lay
The Higgs field comes in a pair of components, an isospin doublet. The graph already showed that such a doublet cannot be built from the Higgs field's own tower modes as an even, boson-like element. This result says what it takes instead: a doublet built from fermion modes is boson-like only if it combines an odd number of doublet fermions with an odd number of fermions that carry no isospin, the simplest case being one of each, and the charges must then match so that the pair has the Higgs field's hypercharge. Such pairs exist, so the composite route is open as far as charges go. But each component of such a pair mode, on a single light ray, is never an exact boson because it carries charge, and for the simplest such pair it behaves like a finite bank of two-state switches rather than an exact boson; it approaches boson behaviour only when very many such sites are pooled.

## one-liner
For tower modes in isospin doublets and singlets every doublet is odd in the doublet modes, so an even composite doublet needs an odd singlet factor (the doublet-singlet bilinears, with hypercharge fixed by Y_s); every component of a doublet of pair densities is charged, nilpotent and never a canonical boson, and, by the stored helicity-one theorem (iii), (iv) read with isospin weights (a corollary), a quasi-spin of q rank(M) sites when M^2 = 0 (for example a single doublet-singlet hopping, or nonzero hypercharge with all doublet channels of one hypercharge).
