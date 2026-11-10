---
id: synthesis.chsh-with-parity-even-observables-needs-two-modes-per-party-and-no-klein-twist
kind: claim
version: 1
title: 'CHSH with parity-even observables: two modes per party, and no Klein twist'
status: proved
region: synthesis
subject: clifford-structure
tags: [entanglement, grading-and-parity, car-algebra, classical-theorem]
proposed_by:
  kind: ai
  session: 2026-11-10-phase1
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase1
review: draft
derivations:
- name: main
  uses:
  - tower.commuting-copies@5
  - singularity.descent-parity-average@5
  - synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_even_observables_commute_without_twist_and_one_mode_has_only_the_parity
- kind: check
  ref: check.py::check_two_modes_per_party_reach_square_eight_with_even_observables_and_even_states
- kind: check
  ref: check.py::check_twisted_one_mode_split_exceeds_two_only_through_odd_observables
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product
  - singularity.imported-univalence-superselection-rule
extraction:
  note: >-
    Adversarial test of whether the Klein-twisted split is the right notion of two parties for a CHSH statement
    in the Clifford algebra of modes. Two settings are recorded side by side and neither is called the physical
    one. Setting E: a party's observables are parity-even. Then no twist is needed, one mode per party never
    exceeds $2$, and two modes per party reach every value $8r$ with $8r^{2} \le 1$. Setting O: parity-odd elements
    count as observables. Then one mode against the Klein-twisted other mode exceeds $2$ (the realisation of the
    stored CHSH result, its clause (vii)). Kill condition registered before computing: a pair of non-commuting
    even self-adjoint elements of square one in one mode, or no even configuration of two modes per party with
    $C^{2} = 4 + 4K$ (neither fired). Hypothesis (P) is stated in the formal level as a named hypothesis; it is to
    become an assumes edge to the postulate the maintainer creates after acceptance. The identity, the bound and
    the blade lemma with its functionals are cited from the stored CHSH result (clauses (i), (iii), (iv)). Only
    the twist is used of the stored commuting-copies theorem; the pair state of clause (iv) is written out and
    verified in the proof, so the stored theorem on the mode split (where it is the pair state at equal weights,
    $r = 0$, $cs = \tfrac12$) is not pinned. Prior art: Dasenbrook, Bowles, Bohr Brask, Hofer, Flindt and Brunner,
    New J. Phys. 18 (2016) 043036, obtain a Bell violation from two copies of a single-electron mode-entangled
    state, because the single-copy measurements needed are not diagonal in occupation number, and conclude that
    the state is entangled and nonlocal; they state no no-go result. Debarba, Iemini, Giedke and Friis, Phys. Rev.
    A 101 (2020) 052326, state that under parity superselection two copies must be processed jointly to violate a
    Bell inequality (both checked on the web). The superselection rule is Wick, Wightman and Wigner (1952), and
    mode subsystems under it are discussed by Banuls, Cirac and Wolf, Phys. Rev. A 76 (2007) 022311 and Friis, Lee
    and Bruschi, Phys. Rev. A 87 (2013) 022338 (these three from memory). The mathematics is classical; what is
    recorded is the statement in the series' algebra and its relation to the stored twist and parity average.
    Transport-absent. A sequence of rational values on the twisted split belongs to a sibling result of the same
    run (not used); one example, $\tfrac{14}{5}$, is kept here.
---

## formal
Let $k$ be $\Q$ or any ordered field and $\Cl_{k}(\ell,\ell)$ the algebra of $\ell$ modes: generators $e_{j}$, $f_{j}$ with $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, mode parities $p_{j} = f_{j}e_{j}$, $\Gamma_{X} = \prod_{j \in X}p_{j}$ for a set $X$ of modes, total parity $\Gamma$. As in Theorem \claimref{synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate}, $\dagger$ is the linear extension of the inverse on blades (it fixes each $e_{j}$ and negates each $f_{j}$), an \emph{observable} is an $x$ with $x^{\dagger} = x$, $x^{2} = 1$, a \emph{configuration} is four observables with $A_{i}B_{j} = B_{j}A_{i}$, and $C = A_{1}(B_{1} + B_{2}) + A_{2}(B_{1} - B_{2})$. The adjoint is defined by the chosen generators. In definite signature it does not depend on the orthonormal frame; in indefinite signature it depends on the split into generators of square $1$ and of square $-1$, so observables, states and (P) are relative to that split, and each statement holds for every fixed split.

\emph{Hypothesis (P), positivity of values:} values are given by a \emph{state}, a $k$-linear $\omega : \Cl_{k}(\ell,\ell) \to k$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$ and $\omega(x^{\dagger}) = \omega(x)$ for all $x$; (P) is assumed, not derived.

(P) extends the stored definition of a state as an element $\rho = \sum_{r}x_{r}x_{r}^{\dagger}$ of unit trace from elements to functionals. An element is \emph{even} if it commutes with $\Gamma$; a state is even if $\omega(\Gamma x\Gamma) = \omega(x)$. For disjoint sets of modes $A$, $B$ let $\Cl(A)$, $\Cl(B)$ be the subalgebras generated by their generators and $B'$ the copy of $\Cl(B)$ twisted by $\Gamma_{A}$ as in Theorem \claimref{tower.commuting-copies} (generators $y\Gamma_{A}$). Two settings are recorded side by side, and neither is singled out as the physical one: \emph{setting E}, in which a party's observables are even; \emph{setting O}, in which parity-odd elements also count as observables. Clauses (i) to (iii) are in setting E, clause (iv) is in setting O and compares, clause (v) is the untwisted split.
\begin{enumerate}
\item[(i)] \emph{(Setting E: even observables need no twist; proved.)} Even elements of $\Cl(A)$ and of $\Cl(B)$ commute; $(y\Gamma_{A})(y'\Gamma_{A}) = yy'$ for generators $y, y'$ of $\Cl(B)$, so the even part of $B'$ is the even part of $\Cl(B)$. For even observables the graded split and the Klein-twisted split are the same split, and any even observables $A_{i} \in \Cl(A)$, $B_{j} \in \Cl(B)$ form a configuration.
\item[(ii)] \emph{(Setting E: a party whose two observables are even elements of the algebra of one mode, or of its twisted copy; proved; the value bound under (P).)} The self-adjoint elements of the algebra of one mode $j$ are $s + tp_{j} + ue_{j}$; its observables are $\pm 1$ and $tp_{j} + ue_{j}$ with $t^{2} + u^{2} = 1$; its even observables are $\pm 1$ and $\pm p_{j}$, which commute (for the twisted copy: $\pm 1$, $\pm p_{j}$ again). Hence for such a party $C^{2} = 4$ and, under (P), $\omega(C)^{2} \le 4$ for every state, whatever the other party.
\item[(iii)] \emph{(Setting E: two modes per party; proved; values under (P).)} For $\ell = 4$, $A = \{1,2\}$, $B = \{3,4\}$, the elements $A_{1} = p_{1}$, $A_{2} = e_{1}f_{2}$, $B_{1} = p_{3}$, $B_{2} = e_{3}f_{4}$ are even observables, blades with $A_{1}A_{2} = -A_{2}A_{1}$, $B_{1}B_{2} = -B_{2}B_{1}$, forming a configuration. By the blade lemma (clause (iv) of Theorem \claimref{synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate}) $C^{2} = 4 + 4K$ with $K = -f_{1}f_{2}f_{3}f_{4}$, and for $8r^{2} \le 1$ the functional $\omega_{r}(x) = \langle(1 + K)(1 + rC)x\rangle_{0}$ satisfies (P) with $\omega_{r}(C) = 8r$; it is an even state. So in setting E one mode per party never exceeds $2$ and two modes per party give every rational value of square below $8$, with supremum $2\sqrt{2}$ not attained over $\Q$.
\item[(iv)] \emph{(Setting O: one mode against the twisted other mode; proved; values under (P).)} For $\ell = 2$, $A = \{1\}$, $B = \{2\}$, the observables $p_{1}, e_{1}$ of $\Cl(A)$ and $p_{2}, e_{2}p_{1}$ of $B'$ commute across the parties and anticommute within each (the realisation of clause (vii) of Theorem \claimref{synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate}). Let $\rho = \tfrac14(1 + p_{1}p_{2} - e_{1}f_{2} - f_{1}e_{2})$, the stored pair state at $r = 0$, $cs = \tfrac12$ (equal weights); it is a self-adjoint idempotent commuting with $\Gamma$, and $\omega(x) = 4\langle\rho x\rangle_{0}$ is an even state. Then $\omega(p_{1}p_{2}) = \omega(e_{1}\,e_{2}p_{1}) = 1$, $\omega(p_{1}\,e_{2}p_{1}) = \omega(e_{1}p_{2}) = 0$, and with directions $B_{\pm} = zp_{2} \pm x\,e_{2}p_{1}$, $x^{2} + z^{2} = 1$, the configuration $(p_{1}, e_{1}; B_{+}, B_{-})$ has value $\omega(C) = 2(z + x)$, above $2$ for $x, z > 0$: for example $\tfrac{14}{5}$ at $(x, z) = (\tfrac45, \tfrac35)$ on this state with these directions. On the pair state with amplitudes $(c, s)$, $c^{2} + s^{2} = 1$, $\rho_{c,s} = \tfrac14(1 + p_{1}p_{2})(1 + (c^{2} - s^{2})p_{1}) - \tfrac12cs\,(e_{1}f_{2} + f_{1}e_{2})$, the value is $2(z + 2cs\,x)$, whose supremum over these directions is $2\sqrt{1 + 4c^{2}s^{2}}$; this is $2(z + x)$ only at equal weights. The observables $e_{1}$ and $e_{2}p_{1}$ anticommute with $\Gamma$, and the parity average $E(x) = \tfrac12(x + \Gamma x\Gamma)$ of Theorem \claimref{singularity.descent-parity-average} (in its total-parity form) sends them to $0$; with every observable replaced by its parity average the value is $2z \le 2$. By (ii) no other choice of observables changes this: on one mode per party a value above $2$ exists in setting O and not in setting E.
\item[(v)] \emph{(Without the twist; proved; values under (P).)} $e_{1}$ and $e_{2}$ anticommute and $e_{1}e_{2}$ is anti-self-adjoint, so $\omega(e_{1}e_{2}) = 0$ for every state (by the reality clause of (P)). The self-adjoint part of the untwisted element $e_{1}e_{2} + e_{1}p_{2} + p_{1}e_{2} - p_{1}p_{2}$ is $H = e_{1}p_{2} + p_{1}e_{2} - p_{1}p_{2}$, with $H^{2} = 3$, so $\omega(H)^{2} \le 3 < 4$ for every state.
\end{enumerate}

## technical
In the Clifford algebra of fermionic modes, odd elements of two disjoint sets of modes anticommute, and the stored Klein twist is what makes them commute. This result records two settings side by side, without calling either the physical one, with values taken under Hypothesis (P), positivity of values (values are given by a state, a linear $\omega$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$, $\omega(x^{\dagger}) = \omega(x)$; assumed, not derived). In the setting where a party's observables are parity-even, the twist is idle: even elements of disjoint mode sets already commute and the twisted and untwisted even algebras coincide; a party holding one mode has only the parity itself, so every CHSH value is at most $2$; with two modes each there are even blade observables to which the stored blade lemma applies, giving even states with every rational value of square below $8$. In the setting where parity-odd elements are observables, one mode against the twisted other mode gives $2(z + x)$ on the stored pair state at equal weights with directions $zp_{2} \pm x\,e_{2}p_{1}$ (for example $\tfrac{14}{5}$), and $2\sqrt{1 + 4c^{2}s^{2}}$ at most for amplitudes $(c, s)$; the observables $e_{1}$ and $e_{2}p_{1}$ that this uses anticommute with the parity, and the stored parity average sends them to zero. Without the twist the odd-odd product has value zero and the self-adjoint part of the CHSH expression has square $3$. The adjoint, and with it observables and states, is relative to the split into generators of square $1$ and $-1$. Classical mathematics (fermion parity superselection; two copies of a mode-entangled state); the statement in the series' algebra is what is recorded.

## lay
Two parties share particles of the kind that obey the exclusion principle, described by slots that are either empty or full. Average values are assumed to be non-negative on squares (Hypothesis (P), an assumption, not something derived). Two possible rules for what counts as a measurement are set side by side, and this result does not say which one nature uses. Under the first rule, a measurement may not change the number of particles from even to odd. Then one shared slot each is not enough to exceed the everyday limit of $2$: each party has only one such measurement, "is my slot full". Two slots each are enough, and nothing special is needed to make the two parties' measurements compatible. Under the second rule, measurements that change even to odd are allowed; a stored device called the Klein twist makes those of the two parties compatible, and then one slot each does exceed $2$. The mathematics is known; it is recorded here inside the series' algebra.

## one-liner
Under (P), in the Clifford algebra of modes: with parity-even observables no Klein twist is needed, a one-mode party gives $C^{2} = 4$ (value at most $2$) and two modes per party give every rational value of square below $8$; with parity-odd observables allowed, one mode against the twisted other mode reaches $2(z + x)$ on the equal-weight pair state; the two settings are recorded side by side.
