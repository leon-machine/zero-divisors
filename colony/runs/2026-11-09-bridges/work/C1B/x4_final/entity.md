---
id: synthesis.mass-terms-are-pair-terms-of-the-arrays-and-only-the-charge-separates-majorana-from-dirac
kind: claim
version: 1
title: 'Mass terms as pair terms of tower modes: only a charge separates Majorana from Dirac'
status: proved
region: synthesis
subject: neutrinos
tags: [seesaw-and-majorana, pairing-and-bogoliubov, superselection]
proposed_by:
  kind: ai
  session: 2026-11-09-bridges
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-09-bridges
review: draft
derivations:
- name: main
  uses:
  - field-theory.imported-tower-limit@3
  - field-theory.composite-scalars-mean-field-level@5
  - synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy@2
  - standard-model.majorana-element@7
  - synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_one_mode_has_no_pair_term_and_all_mass_terms_are_pair_terms
- kind: check
  ref: check.py::check_charges_of_the_cross_and_self_pair_terms
- kind: check
  ref: check.py::check_flip_of_the_second_modes_turns_the_block_into_hopping
- kind: check
  ref: check.py::check_block_spectrum_is_the_quadratic_with_sum_M_and_product_minus_m_squared
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.majorana-element
  - synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy
extraction:
  open_problem: op.pair-sector-current
  note: >-
    Adversarial test of the suggestion that the Majorana mass of the neutral singlet is a pairing term of the
    tower and that the stored pairing gap is the heavy mass. Kill condition registered before computing: the
    stored pairing results hold only at fixed charges, where a number-violating term has no matrix elements. It
    fires, and more widely than expected: in the stored mode language every mass term, Dirac included, is a pair
    term and changes the fixed charges of the gap theorem, so that theorem sees no mass term at all; the gap
    formula G n_b belongs to the quartic element and is not the Majorana scale. What the suggestion keeps: the
    bilinear block on two arrays has the seesaw quadratic exactly. What it loses: being a pair term does not
    single out the Majorana term; the only difference from a Dirac term is its charge under the number that is
    opposite on the two arrays, the mode-level counterpart of [B - L, T] = -2T, and that difference is a choice of
    charge, not a property of the block, since an automorphism of the mode algebra turns the block into
    number-conserving hopping. The premise that the framework realises the Majorana term and fixes its scale
    (Premise (M) of the neutrino subject) is not used and not touched: nothing here produces the term or its
    scale. Also recorded: the grading commutes with every pair term, so the stored one-window and two-window
    tests, which use the count of arrays and the grading, are unchanged by any mass term; the earlier lead that
    the verdict on generations needs the number current is not supported by the stored statement. The seesaw
    quadratic for a symmetric two-by-two mass matrix is textbook; the Bogoliubov form of a fermion mass is
    Nambu and Jona-Lasinio's (cited from memory). Transport-absent: algebra of the canonical anticommutation
    relations on four modes.
---

## formal
Let $v_{j}, w_{j}$ ($j = 0, \dots, 3$) be tower modes, null vectors with $Q(v_{j}) = Q(w_{j}) = 0$ and $\{v_{j}, w_{k}\} = \delta_{jk}$ (Fact \claimref{field-theory.imported-tower-limit}); in $\Cl(4,4)$ with generators $e_{j}$, $f_{j}$, $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, they are $w_{j} = \tfrac12(e_{j} + f_{j})$, $v_{j} = \tfrac12(e_{j} - f_{j})$, and the adjoint is reversion composed with $f_{j} \mapsto -f_{j}$. Put $n_{j} = v_{j}w_{j}$. Modes $0, 1$ are the two modes $(a, c)$ of one array in a block of Proposition \claimref{field-theory.composite-scalars-mean-field-level}(1), whose mass term is $\mu w_{a}w_{c} + \mu^{*}v_{c}v_{a}$; modes $2, 3$ are the two modes $(a', c')$ of a second array. Let $D = w_{0}w_{3} + w_{2}w_{1}$ (the cross pair term), $S = w_{2}w_{3}$ (the self pair term of the second array), $H = K\sum_{j}n_{j} + m(D + D^{*}) + M(S + S^{*})$ with $K, m, M$ real, and the charges $N = \sum_{j}n_{j}$, $L = n_{0} + n_{1} - n_{2} - n_{3}$ (opposite on the two arrays), $N_{a} = n_{0} + n_{2}$, $N_{c} = n_{1} + n_{3}$, and the grading $\Gamma = \prod_{j}(1 - 2n_{j})$.
\begin{enumerate}
\item[(i)] \emph{(Mass terms are pair terms, and one mode has none; proved.)} Every $x$ in the span of the $w_{j}$ has $Q(x) = 0$, so $xx = 0$ and the pair terms $w_{j}w_{k}$, $j < k$, span a space of dimension $\binom{n}{2}$ on $n$ modes: none on one mode, six on four. The stored mass block is the pair term of the two modes of one array; a mass term of an array with itself needs both its modes and is its self pair term $S$; a mass term between two arrays is a cross pair term $D$. So in the stored mode language every mass term is a pair term.
\item[(ii)] \emph{(Charges; proved.)} $[N, X] = -2X$, $[N_{a}, X] = [N_{c}, X] = -X$, $[N_{a} - N_{c}, X] = 0$ and $[\Gamma, X] = 0$ for $X = D$ and $X = S$ alike; $[L, D] = 0$ and $[L, S] = 2S$. Hence on every sector of fixed $(N_{a}, N_{c})$, the setting of Theorem \claimref{synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy}(i), (ii), the compression of $D$, $S$ and their adjoints vanishes: that theorem's spectrum and its gap $Gn_{b}$ belong to the quartic element $-GP^{*}P$ and contain no bilinear mass term, of either kind. $H$ commutes with $N_{a} - N_{c}$ and with $\Gamma$ for all $K, m, M$; with $L$ exactly when $M = 0$; with $N$, or with $N_{a}$, exactly when $m = M = 0$. Among the charges of the block, $L$ alone separates $S$ from $D$; it is the mode-level counterpart of $[B - L, T] = -2T$ of Proposition \claimref{standard-model.majorana-element}(2), up to the sign convention of the charge.
\item[(iii)] \emph{(The separation is a choice of charge; proved.)} The map $\theta$: $f_{1} \mapsto -f_{1}$, $f_{3} \mapsto -f_{3}$, the other generators fixed, is an automorphism of the algebra commuting with the adjoint; it exchanges $v_{j}$ and $w_{j}$ for $j = 1, 3$, carries $N_{a} - N_{c}$ to $N - 2$, $S$ to the hop $w_{2}v_{3}$ and $H$ to a self-adjoint element commuting with $N$: number-conserving hopping on four modes with the same spectrum. So no property of the block as an element of the mode algebra makes $S$ number-violating; it is so with respect to $L$ and $N$, and number-conserving with respect to $N_{a} - N_{c}$.
\item[(iv)] \emph{(The block spectrum; proved at $K = 0$.)} At $K = 0$, $\mathrm{ad}_{H}^{4} - (M^{2} + 2m^{2})\,\mathrm{ad}_{H}^{2} + m^{4} = 0$ on the eight mode operators (for all real $m$, $M$ by the Cayley-Hamilton identity of an antisymmetric matrix with Pfaffian $-m^{2}$; checked at five rational pairs), so the mode energies are $|x_{\pm}|$ with $x^{2} - Mx - m^{2} = 0$: $x_{+} + x_{-} = M$, $x_{+}x_{-} = -m^{2}$, the light one equal to $m^{2}$ divided by the heavy one, with no expansion in $m/M$.
\end{enumerate}
\emph{Reading (argued).} The Majorana term of the neutral singlet is a pair term of the tower in the stored sense, but so is every Dirac mass, and the stored gap theorem, being at fixed charges, bears on neither; what marks the Majorana term is its charge under the number opposite on the two arrays, which is the stored statement that $T$ has $B - L$ charge $-2$ and nothing more. The stored tests of Theorem \claimref{synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content} use the count of arrays, which its clause (i) gives for every mass matrix, and the grading; since $[\Gamma, D] = [\Gamma, S] = 0$, a Majorana term does not change the verdict, and the number current, which it does not conserve, is not what those tests use. Scope: four modes (one momentum pair of two arrays), bilinear terms only; no statement about how a Majorana term forms or about its scale.

## technical
In the series' mode language a fermion mass couples the two modes of an array (momentum $k$ and $-k$) through a product of two annihilation operators, a pair term. A single mode has no such term, because the operators are null vectors. For two arrays there are two kinds: a cross term, which is a Dirac mass, and the self term of one array, which is its Majorana mass. Both lower the total number by two and both shift the two charges that the stored pairing-gap theorem holds fixed, so that theorem, which is about the quartic interaction, contains neither. The only charge that tells them apart is the one counted with opposite signs on the two arrays: the Dirac term conserves it and the Majorana term changes it by two. Even that is a matter of which charge one calls lepton number: exchanging creation and annihilation on the two $-k$ modes is a symmetry of the operator algebra, and it turns the whole block into ordinary hopping between four sites, with the same energies. Those energies solve $x^{2} - Mx - m^{2} = 0$ exactly, which is the seesaw.

## lay
There was a suggestion that the heavy mass of the right-handed neutrino might be explained by the series' results on pairing of modes. This entry checks it on the smallest example. The mass is indeed a pairing term, but so is every ordinary mass, so that does not single it out; and the stored pairing result concerns a different kind of term and says nothing about either. What distinguishes the special neutrino mass is only that it changes lepton number by two, which the series had already recorded. The small example does reproduce the standard seesaw relation between a heavy and a light mass exactly. Nothing here explains why the term exists or how large it is.

## one-liner
On four tower modes every mass term is a pair term and shifts the fixed charges of the stored gap theorem, which therefore contains none; the Majorana (self) term differs from the Dirac (cross) term only by its charge $2$ under the number opposite on the two arrays, an automorphism turns the block into number-conserving hopping, and at $K = 0$ its energies solve $x^{2} - Mx - m^{2} = 0$.
