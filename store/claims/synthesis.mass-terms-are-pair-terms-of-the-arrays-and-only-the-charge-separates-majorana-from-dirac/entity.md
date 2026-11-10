---
id: synthesis.mass-terms-are-pair-terms-of-the-arrays-and-only-the-charge-separates-majorana-from-dirac
kind: claim
version: 1
title: 'Mass terms as pair terms on four tower modes: the charge separating Majorana from Dirac'
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
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Cross-reference to the stored order-four result written with its id (the two results cite each other in words and neither is a premise of the other); no change of content. Version kept: the entity was accepted in the same pass.'
  note: >-
    Adversarial test of the suggestion that the Majorana mass of the neutral singlet is a pairing term of the
    tower and that the stored pairing gap is the heavy mass. Kill condition registered before computing: the
    stored pairing results hold only at fixed charges, where a number-violating term has no matrix elements. It
    fires, and more widely than expected: in the stored mode language every mass term, Dirac included, is a pair
    term and changes the fixed charges of the gap theorem, so an explicit mass term has vanishing compression on
    its sectors and is not part of its element; its clause (iii) ties the gap G n_b to the mean-field mass of the
    paired array, and nothing stored identifies that array with the neutral singlet or G with the Majorana scale. What the suggestion keeps: the
    bilinear block on two arrays has the seesaw quadratic exactly. What it loses: being a pair term does not
    single out the Majorana term; among the block's charges the difference from a Dirac term (besides array
    structure and rank) is its charge under the number that is
    opposite on the two arrays, the mode-level counterpart of [B - L, T] = -2T, and that difference is a choice of
    charge, not a property of the block, since an automorphism of the mode algebra turns the block into
    number-conserving hopping. The premise that the framework realises the Majorana term and fixes its scale
    (Premise (M) of the neutrino subject) is not used and not touched: nothing here produces the term or its
    scale. Also recorded: the grading commutes with every pair term, so the stored one-window and two-window
    tests, which use the count of arrays and the grading, are unchanged by any mass term; the earlier lead that
    the verdict on generations needs the number current is not supported by the stored statement. Cross-reference (neither result is a premise of the other): the opposite number is the mode-level
    image of B - L, and the Z4 parity of T in
    synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element is
    its reduction modulo 4; in that dictionary the total number corresponds to the order-four element and the
    opposite number to that element times the centre of su(2)_L (argued, from the stored grade dictionary: every
    mass form on the sixteen has odd Clifford grade). The K != 0 form of clause (iv) was verified by a second, independent computation (ad_H is K on creators, -K on annihilators,
    plus the antisymmetric part, and the cross terms cancel in the square). The seesaw
    quadratic for a symmetric two-by-two mass matrix is textbook; the Bogoliubov form of a fermion mass is
    Nambu and Jona-Lasinio's (cited from memory). Transport-absent: algebra of the canonical anticommutation
    relations on four modes.
---

## formal
Let $v_{j}, w_{j}$ ($j = 0, \dots, 3$) be tower modes, null vectors with $Q(v_{j}) = Q(w_{j}) = 0$ and $\{v_{j}, w_{k}\} = \delta_{jk}$ (Fact \claimref{field-theory.imported-tower-limit}); in $\Cl(4,4)$ with generators $e_{j}$, $f_{j}$, $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, they are $w_{j} = \tfrac12(e_{j} + f_{j})$, $v_{j} = \tfrac12(e_{j} - f_{j})$, and the adjoint is reversion composed with $f_{j} \mapsto -f_{j}$. Put $n_{j} = v_{j}w_{j}$. Modes $0, 1$ are the two modes $(a, c)$ of one array in a block of Proposition \claimref{field-theory.composite-scalars-mean-field-level}(1), whose mass term is $\mu w_{a}w_{c} + \mu^{*}v_{c}v_{a}$; modes $2, 3$ are the two modes $(a', c')$ of a second array. Let $D = w_{0}w_{3} + w_{2}w_{1}$ (the cross pair term), $S = w_{2}w_{3}$ (the self pair term of the second array), $H = K\sum_{j}n_{j} + m(D + D^{*}) + M(S + S^{*})$ with $K, m, M$ real, and the charges $N = \sum_{j}n_{j}$, $L = n_{0} + n_{1} - n_{2} - n_{3}$ (opposite on the two arrays), $N_{a} = n_{0} + n_{2}$, $N_{c} = n_{1} + n_{3}$, and the grading $\Gamma = \prod_{j}(1 - 2n_{j})$.
\begin{enumerate}
\item[(i)] \emph{(Mass terms are pair terms, and one mode has none; proved.)} Every $x$ in the span of the $w_{j}$ has $Q(x) = 0$, so $xx = 0$ and the pair terms $w_{j}w_{k}$, $j < k$, span a space of dimension $\binom{n}{2}$ on $n$ modes: none on one mode, six on four. The stored mass block is the pair term of the two modes of one array; a mass term of an array with itself needs both its modes and is its self pair term $S$; a mass term between two arrays is a cross pair term $D$. The stored one-array block is itself of the self kind: $[L, w_{0}w_{1}] = -2w_{0}w_{1}$ and $[N_{a} - N_{c}, w_{0}w_{1}] = 0$. So in the stored mode language every mass term is a pair term (for terms beyond the stored block this is the definition used here: a bilinear term changing the number by two).
\item[(ii)] \emph{(Charges; proved.)} $[N, X] = -2X$, $[N_{a}, X] = [N_{c}, X] = -X$, $[N_{a} - N_{c}, X] = 0$ and $[\Gamma, X] = 0$ for $X = D$ and $X = S$ alike; $[L, D] = 0$ and $[L, S] = 2S$. Hence on every sector of fixed $(N_{a}, N_{c})$, the setting of Theorem \claimref{synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy}(i), (ii), the compression of $D$, $S$ and their adjoints vanishes, and the element $H_{4}$ of that theorem contains no explicit bilinear term of either kind. Vanishing compression is not absence of effect: $H_{4}$ plus a mass term mixes the sectors. Clause (iii) of the same theorem relates its gap to the mean-field mass $\Delta$ of the paired array ($Gn_{b} = 2\sqrt{K^{2} + \Delta^{2}}$, twice it at $K = 0$), which by clause (3) of the stored block is $G$ times the condensate of a self pair term in the present vocabulary; nothing stored identifies that paired array with the neutral singlet or $G$ with a scale. $H$ commutes with $N_{a} - N_{c}$ and with $\Gamma$ for all $K, m, M$; with $L$ exactly when $M = 0$; with $N$, or with $N_{a}$, exactly when $m = M = 0$. Among the six charges listed, $L$ alone separates $S$ from $D$. In general a diagonal charge $\sum_{j}q_{j}n_{j}$ commutes with $D$ exactly when $q = (\alpha, \beta, -\beta, -\alpha)$, and then $[\,\cdot\,, S] = (\alpha + \beta)S$: $S$ is charged under every charge conserved by $D$ except the line $\alpha + \beta = 0$ ($N_{a} - N_{c}$ and its multiples). $L$ is the mode-level counterpart of $[B - L, T] = -2T$ of Proposition \claimref{standard-model.majorana-element}(2), up to the sign convention of the charge.
\item[(iii)] \emph{(The separation is a choice of charge; proved.)} The map $\theta$: $f_{1} \mapsto -f_{1}$, $f_{3} \mapsto -f_{3}$, the other generators fixed, is an automorphism of the algebra commuting with the adjoint; it exchanges $v_{j}$ and $w_{j}$ for $j = 1, 3$, carries $N_{a} - N_{c}$ to $N - 2$, $S$ to the hop $w_{2}v_{3}$ and $H$ to a self-adjoint element commuting with $N$: number-conserving hopping on four modes with the same spectrum. So no property of the block as an element of the mode algebra makes $S$ number-violating; it is so with respect to $L$ and $N$, and number-conserving with respect to $N_{a} - N_{c}$. This does not make $S$ and $D$ equivalent: they differ also by the array structure and by rank ($S$ alone gives a mass to two of the four modes, those of the second array; $D$ alone to all four), so no automorphism preserving the mode space carries one to the other.
\item[(iv)] \emph{(The block spectrum; proved.)} At $K = 0$, $\mathrm{ad}_{H}^{4} - (M^{2} + 2m^{2})\,\mathrm{ad}_{H}^{2} + m^{4} = 0$ on the eight mode operators (for all real $m$, $M$ by the Cayley-Hamilton identity of an antisymmetric matrix with Pfaffian $-m^{2}$; checked at five rational pairs), so the mode energies are $|x_{\pm}|$ with $x^{2} - Mx - m^{2} = 0$: $x_{+} + x_{-} = M$, $x_{+}x_{-} = -m^{2}$, the light one equal to $m^{2}$ divided by the heavy one, with no expansion in $m/M$. For every real $K$, $\mathrm{ad}_{H}^{2} = K^{2} + E^{2}$ on the mode operators with $E^{2}$ the same operator as at $K = 0$: $(\mathrm{ad}_{H}^{2} - K^{2})^{2} - (M^{2} + 2m^{2})(\mathrm{ad}_{H}^{2} - K^{2}) + m^{4} = 0$, the two-array form of the stored $\mathrm{ad}_{H}^{2} = K^{2} + |\mu|^{2}$, with mode energies $\sqrt{K^{2} + x_{\pm}^{2}}$.
\end{enumerate}
\emph{Reading (argued).} The Majorana term of the neutral singlet is a pair term of the tower in the stored sense, but so is every Dirac mass, and the stored gap theorem contains no explicit mass term of either kind, its clause (iii) relating the gap to the mean-field mass of whichever array is paired; what marks the Majorana term among the block's charges is its charge under the number opposite on the two arrays, the mode-level image of the stored statement that $T$ has $B - L$ charge $-2$. On the sixteen components every mass form has odd Clifford grade, so each is odd under an order-four element whose square is the grading (the pseudoscalar of the ten Majorana generators, \claimref{synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element}, clause (2)); this corresponds to the row $N$ ($-2$ on both terms), and the row $L$ to that element times the centre of $\su(2)_{L}$, under which a Dirac (doublet) form is even and $T$, which commutes with the gauge algebra, stays odd. So the charge-dependence of (iii) has an invariant form: the class of the order-four element modulo the unbroken gauge group (argued; the order-four element is not a stored entity). The stored tests of Theorem \claimref{synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content} use the count of arrays, which its clause (i) gives for every mass matrix, and the grading; since $[\Gamma, D] = [\Gamma, S] = 0$, a Majorana term does not change the verdict, and the number current, which it does not conserve, is not what those tests use. Scope: four modes (one momentum pair of two arrays), bilinear terms only, the six charges listed and the diagonal charges of (ii); no statement about how a Majorana term forms or about its scale.

## technical
In the series' mode language a fermion mass couples the two modes of an array (momentum $k$ and $-k$) through a product of two annihilation operators, a pair term. A single mode has no such term, because the operators are null vectors. For two arrays there are two kinds: a cross term, which is a Dirac mass, and the self term of one array, which is its Majorana mass. Both lower the total number by two and both shift the two charges that the stored pairing-gap theorem holds fixed, so that theorem's element, the quartic interaction, contains neither as an explicit term (its mean-field clause concerns the mass of whichever array is paired). Among the charges of the block, the one that tells them apart is the one counted with opposite signs on the two arrays: the Dirac term conserves it and the Majorana term changes it by two. Even that is a matter of which charge one calls lepton number: exchanging creation and annihilation on the two $-k$ modes is a symmetry of the operator algebra, and it turns the whole block into ordinary hopping between four sites, with the same energies. Those energies solve $x^{2} - Mx - m^{2} = 0$ exactly, which is the seesaw.

## lay
There was a suggestion that the heavy mass of the right-handed neutrino might be explained by the series' results on pairing of modes. This entry checks it on the smallest example. The mass is indeed a pairing term, but so is every ordinary mass, so that does not single it out; and the stored pairing result concerns a different kind of term and says nothing about either. What distinguishes the special neutrino mass is only that it changes lepton number by two, which the series had already recorded. The small example does reproduce the standard seesaw relation between a heavy and a light mass exactly. Nothing here explains why the term exists or how large it is.

## one-liner
On four tower modes every mass term is a pair term with vanishing compression on the fixed-charge sectors of the stored gap theorem, whose element contains no explicit one; the Majorana (self) term differs from the Dirac (cross) term, among the block's charges, by its charge $2$ under the number opposite on the two arrays (and by rank), an automorphism turns the block into number-conserving hopping, and its mode energies are $\sqrt{K^{2} + x^{2}}$ with $x^{2} - Mx - m^{2} = 0$.
