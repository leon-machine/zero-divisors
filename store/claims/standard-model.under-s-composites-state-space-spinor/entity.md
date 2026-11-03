---
id: standard-model.under-s-composites-state-space-spinor
kind: claim
version: 6
title: 'Under (S): the composite''s state space is the $\mathrm{Spin}(10)$ spinor, and the derived generation
  is its even half'
status: proved
region: standard-model
subject: standard-model
tags: [spinor-modules, representation-theory, hypercharge-and-anomalies]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
derivations:
- name: main
  uses:
  - standard-model.chirality-two-halves-spinor-module-conjugation@6
  - standard-model.hypercharge-global-form-pair-counting-consistency@5
  - standard-model.imported-anomaly-coefficients@1
  - standard-model.imported-cauchy-decomposition-exterior-power@1
  - standard-model.imported-fock-representation-clifford-algebra-bogoliubov@1
  - standard-model.mass-bracket-charged-singlet@4
  - standard-model.hyp-s-slot-statistics@9
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12.py
  tags:
  - label:prop:sixteen
- kind: check
  ref: check.py::check_even_part_is_the_generation
- kind: check
  ref: check.py::check_fock_space_is_the_cl10_spinor
- kind: check
  ref: check.py::check_number_and_split_preserving_bivectors
- kind: check
  ref: check.py::check_abelian_generators_anomalies
- kind: check
  ref: check.py::check_spin10_action_anomaly_free
locators:
  paper: T12
  number: Prop 5.8
  label: prop:sixteen
  line: 1160
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the even and odd parts as the generation and its conjugate, the Cl(10) Fock module with its u(5) and u(2) + u(3) bivectors, and the anomaly sums of the abelian generators in both actions. Version 4 -> 5. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 5 -> 6.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted the empty-twistor doublet and the twistor slots to the empty conformal spinor''s doublet and the conformal-spinor slots in the formal level; no other level or the proof had twistor language.'
  source_title: |-
    Under (S): the composite's state space is the $\mathrm{Spin}(10)$ spinor, and the derived generation is its even half
  source_formal: |-
    Assume Hypothesis (S). Let $S(U(2) \times U(3))$ act on $\Lambda^{\bullet}(\C^{2} \oplus \C^{3})$ through $\Lambda^{\bullet}(A \oplus B)$, so that on the component $\Lambda^{j}\C^{2} \otimes \Lambda^{k}\C^{3}$ the abelian factor $\lambda$ acts by $\lambda^{3j - 2k}$. Then:
    \begin{enumerate}
    \item The one-generation spectrum of Theorem \claimref{standard-model.hypercharge-global-form-pair-counting-consistency},
    \[
    Q \oplus L \oplus u^{c} \oplus d^{c} \oplus e^{c} \oplus \nu^{c}
    \;=\; (2,3)_{1/6} \oplus (2,1)_{-1/2} \oplus (1,\bar{3})_{-2/3} \oplus (1,\bar{3})_{1/3} \oplus (1,1)_{1} \oplus (1,1)_{0},
    \]
    is exactly the even part $\Lambda^{\mathrm{even}}(\C^{2} \oplus \C^{3})$, sixteen-dimensional, with $\nu^{c}$, $u^{c}$, $Q$, $L$, $e^{c}$, $d^{c}$ at $(j, k) = (0,0), (0,2), (1,1), (1,3), (2,0), (2,2)$; and the odd part $\Lambda^{\mathrm{odd}}(\C^{2} \oplus \C^{3})$ is its dual, the antiparticles, with the empty-twistor doublet $(2,1)_{1/2}$ at $(1,0)$. The mass bracket's slot factor $\Lambda^{2}\C^{2}$, $(1,1)_{1}$, is the even component $(2,0)$, the same representation as $e^{c}$.
    \item The five-mode Fock space $\Lambda^{\bullet}(\C^{2} \oplus \C^{3}) = \Lambda^{\bullet}\C^{5}$ is the spinor module of $\Cl(10)$, its two parities are the two half-spinor representations of $\mathrm{Spin}(10)$, and the automorphisms of the five-mode state space's canonical anticommutation relations induced by orthogonal maps of its ten Majorana generators form $O(10)$, implemented on the Fock space by $\mathrm{Pin}(10)$, with the connected part $SO(10)$ implemented by $\mathrm{Spin}(10)$ (Fact \claimref{standard-model.imported-fock-representation-clifford-algebra-bogoliubov}). The derived generation is therefore the half-spinor $16$ of $\mathrm{Spin}(10)$ restricted to $S(U(2) \times U(3))$, with the twistor slots as two of the five modes and the pairs as the other three; the automorphisms preserving in addition the mode number form $U(5)$, and those preserving the slot-pair split as well form $U(2) \times U(3)$, of which Theorem \claimref{standard-model.global-form-quotient-determined}'s group is the determinant-one part. (The number-preserving subgroup of $\mathrm{Spin}(10)$ is a double cover of $U(5)$ acting as $\Lambda^{\bullet} \otimes \det^{-1/2}$, the "determinant phase" of Fact \claimref{standard-model.imported-fock-representation-clifford-algebra-bogoliubov}; the action $\Lambda^{\bullet}(A \oplus B)$ declared above is that of $U(2) \times U(3) \subset SO(10)$, and the two agree on the determinant-one subgroup, where every hypercharge of this paper is computed.)
    \item Among the abelian generators of the split-and-number-preserving algebra, acting on the component $(j,k)$ by $\alpha j + \beta k$ with $\alpha, \beta$ real (hypercharge being $(\alpha, \beta) = (\tfrac12, -\tfrac13)$, the pair $(3,-2)$ divided by six):
    \begin{enumerate}
    \item[(a)] in the action $\Lambda^{\bullet}(A \oplus B)$ declared above, the $[SU(3)]^{2}U(1)$, $[SU(2)]^{2}U(1)$ and gravitational sums of Fact \claimref{standard-model.imported-anomaly-coefficients} over the derived generation are $2(2\alpha + 3\beta)$, $2(2\alpha + 3\beta)$ and $8(2\alpha + 3\beta)$, and the cubic sum is a cubic form in $(\alpha, \beta)$ vanishing at $(3,-2)$; so the three linear conditions hold if and only if the generator is a multiple of hypercharge, the total mode number $j + k$ having sums $(10, 10, 40, 400)$ and $j - k$ having $(-2, -2, -8, -32)$;
    \item[(b)] in the action the state space carries, that of $\mathrm{Spin}(10)$ through $\Lambda^{\bullet} \otimes \det^{-1/2}$ in (2), the generator acts by $\alpha j + \beta k - \tfrac12(2\alpha + 3\beta)$, and all four sums, together with the mixed sums $Y^{2}X$ and $YX^{2}$ with hypercharge, vanish for every $(\alpha, \beta)$.
    \end{enumerate}
    The thirteenth generator of the five-mode state space's automorphism algebra is therefore anomaly-free in the action the generation carries. It is
    \[
    X \;=\; j + k - \tfrac52 \;=\; 2Y - \tfrac52\,(B - L), \qquad B - L \;:=\; 1 - \tfrac23\,k,
    \]
    the pair-number form of the operator $B - L$ of Fact \claimref{families.doublet-direction-module-georgi-jarlskog-clebsch}, and it takes the values $-\tfrac52$ on $\nu^{c}$, $-\tfrac12$ on $Q$, $u^{c}$, $e^{c}$ and $\tfrac32$ on $L$, $d^{c}$: the $U(1)_{X}$ of $\mathrm{Spin}(10)$. The automorphism rule of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}, read with anomaly cancellation, returns thirteen generators. The thirteenth is broken by the right-handed neutrino's Majorana bilinear $\nu^{c}\nu^{c}$, which carries $X = -5$ and $B - L = 2$ (Proposition \claimref{standard-model.majorana-element}), and the twelve are what survives below that scale.
    \end{enumerate}
    Without (S) the first statement is a theorem about a spectrum and an exterior algebra that happen to coincide, with the exterior algebra an object the paper never built; the second is Fact \claimref{standard-model.imported-fock-representation-clifford-algebra-bogoliubov} instantiated and is not available; the third is a computation on the table of components and is not needed.
  env: proposition
  context_refs:
  - families.doublet-direction-module-georgi-jarlskog-clebsch
  - standard-model.gauge-algebra-minimal-massive-composite
  - standard-model.global-form-quotient-determined
  - standard-model.majorana-element
  typing:
    by: ai-typing-pass
    note: 'All six edges are premises cited in the proof; the Majorana-element proposition was not added
      because it depends on this claim through the Pati-Salam split. The paper calls the anomaly freedom
      the standard statement that SO(10) has no cubic invariant, but no such imported claim is in the
      store, so no standard-route derivation. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S). Levels pass: conditions already kept.'
    added:
    - standard-model.hyp-s-slot-statistics
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Assume Hypothesis (S). Let $S(U(2) \times U(3))$ act on $\Lambda^{\bullet}(\C^{2} \oplus \C^{3})$ through $\Lambda^{\bullet}(A \oplus B)$, so that on the component $\Lambda^{j}\C^{2} \otimes \Lambda^{k}\C^{3}$ the abelian factor $\lambda$ acts by $\lambda^{3j - 2k}$. Then:
\begin{enumerate}
\item The one-generation spectrum of Theorem \claimref{standard-model.hypercharge-global-form-pair-counting-consistency},
\[
Q \oplus L \oplus u^{c} \oplus d^{c} \oplus e^{c} \oplus \nu^{c}
\;=\; (2,3)_{1/6} \oplus (2,1)_{-1/2} \oplus (1,\bar{3})_{-2/3} \oplus (1,\bar{3})_{1/3} \oplus (1,1)_{1} \oplus (1,1)_{0},
\]
is exactly the even part $\Lambda^{\mathrm{even}}(\C^{2} \oplus \C^{3})$, sixteen-dimensional, with $\nu^{c}$, $u^{c}$, $Q$, $L$, $e^{c}$, $d^{c}$ at $(j, k) = (0,0), (0,2), (1,1), (1,3), (2,0), (2,2)$; and the odd part $\Lambda^{\mathrm{odd}}(\C^{2} \oplus \C^{3})$ is its dual, the antiparticles, with the doublet of the empty conformal spinor (the empty-twistor doublet) $(2,1)_{1/2}$ at $(1,0)$. The mass bracket's slot factor $\Lambda^{2}\C^{2}$, $(1,1)_{1}$, is the even component $(2,0)$, the same representation as $e^{c}$.
\item The five-mode Fock space $\Lambda^{\bullet}(\C^{2} \oplus \C^{3}) = \Lambda^{\bullet}\C^{5}$ is the spinor module of $\Cl(10)$, its two parities are the two half-spinor representations of $\mathrm{Spin}(10)$, and the automorphisms of the five-mode state space's canonical anticommutation relations induced by orthogonal maps of its ten Majorana generators form $O(10)$, implemented on the Fock space by $\mathrm{Pin}(10)$, with the connected part $SO(10)$ implemented by $\mathrm{Spin}(10)$ (Fact \claimref{standard-model.imported-fock-representation-clifford-algebra-bogoliubov}). The derived generation is therefore the half-spinor $16$ of $\mathrm{Spin}(10)$ restricted to $S(U(2) \times U(3))$, with the slots of the conformal spinors as two of the five modes and the pairs as the other three; the automorphisms preserving in addition the mode number form $U(5)$, and those preserving the slot-pair split as well form $U(2) \times U(3)$, of which Theorem \claimref{standard-model.global-form-quotient-determined}'s group is the determinant-one part. (The number-preserving subgroup of $\mathrm{Spin}(10)$ is a double cover of $U(5)$ acting as $\Lambda^{\bullet} \otimes \det^{-1/2}$, the "determinant phase" of Fact \claimref{standard-model.imported-fock-representation-clifford-algebra-bogoliubov}; the action $\Lambda^{\bullet}(A \oplus B)$ declared above is that of $U(2) \times U(3) \subset SO(10)$, and the two agree on the determinant-one subgroup, where every hypercharge of this paper is computed.)
\item Among the abelian generators of the split-and-number-preserving algebra, acting on the component $(j,k)$ by $\alpha j + \beta k$ with $\alpha, \beta$ real (hypercharge being $(\alpha, \beta) = (\tfrac12, -\tfrac13)$, the pair $(3,-2)$ divided by six):
\begin{enumerate}
\item[(a)] in the action $\Lambda^{\bullet}(A \oplus B)$ declared above, the $[SU(3)]^{2}U(1)$, $[SU(2)]^{2}U(1)$ and gravitational sums of Fact \claimref{standard-model.imported-anomaly-coefficients} over the derived generation are $2(2\alpha + 3\beta)$, $2(2\alpha + 3\beta)$ and $8(2\alpha + 3\beta)$, and the cubic sum is a cubic form in $(\alpha, \beta)$ vanishing at $(3,-2)$; so the three linear conditions hold if and only if the generator is a multiple of hypercharge, the total mode number $j + k$ having sums $(10, 10, 40, 400)$ and $j - k$ having $(-2, -2, -8, -32)$;
\item[(b)] in the action the state space carries, that of $\mathrm{Spin}(10)$ through $\Lambda^{\bullet} \otimes \det^{-1/2}$ in (2), the generator acts by $\alpha j + \beta k - \tfrac12(2\alpha + 3\beta)$, and all four sums, together with the mixed sums $Y^{2}X$ and $YX^{2}$ with hypercharge, vanish for every $(\alpha, \beta)$.
\end{enumerate}
The thirteenth generator of the five-mode state space's automorphism algebra is therefore anomaly-free in the action the generation carries. It is
\[
X \;=\; j + k - \tfrac52 \;=\; 2Y - \tfrac52\,(B - L), \qquad B - L \;:=\; 1 - \tfrac23\,k,
\]
the pair-number form of the operator $B - L$ of Fact \claimref{families.doublet-direction-module-georgi-jarlskog-clebsch}, and it takes the values $-\tfrac52$ on $\nu^{c}$, $-\tfrac12$ on $Q$, $u^{c}$, $e^{c}$ and $\tfrac32$ on $L$, $d^{c}$: the $U(1)_{X}$ of $\mathrm{Spin}(10)$. The automorphism rule of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}, read with anomaly cancellation, returns thirteen generators. The thirteenth is broken by the right-handed neutrino's Majorana bilinear $\nu^{c}\nu^{c}$, which carries $X = -5$ and $B - L = 2$ (Proposition \claimref{standard-model.majorana-element}), and the twelve are what survives below that scale.
\end{enumerate}
Without (S) the first statement is a theorem about a spectrum and an exterior algebra that happen to coincide, with the exterior algebra an object the paper never built; the second is Fact \claimref{standard-model.imported-fock-representation-clifford-algebra-bogoliubov} instantiated and is not available; the third is a computation on the table of components and is not needed.

## technical
Under Hypothesis (S), the composite's state space is $\Lambda^{\bullet}(\C^{2} \oplus \C^{3})$, the abelian factor acting on $\Lambda^{j}\C^{2} \otimes \Lambda^{k}\C^{3}$ by $\lambda^{3j-2k}$, so $Y = (3j - 2k)/6$. Its even part is exactly the derived generation $Q \oplus L \oplus u^{c} \oplus d^{c} \oplus e^{c} \oplus \nu^{c}$, sixteen states, and its odd part is the dual. As the Fock space of five modes it is the spinor module of $\Cl(10)$, so the generation is the half-spinor $16$ of $\mathrm{Spin}(10)$ restricted to $S(U(2) \times U(3))$, with the slots as two modes and the pairs as three.

Among the abelian generators $\alpha j + \beta k$, the linear anomaly sums in the declared action vanish only for multiples of hypercharge, while in the action the state space carries, through $\Lambda^{\bullet} \otimes \det^{-1/2}$, all the sums vanish for every $(\alpha, \beta)$. The thirteenth generator is $X = j + k - \tfrac52 = 2Y - \tfrac52(B - L)$, the $U(1)_{X}$ of $\mathrm{Spin}(10)$, anomaly-free and broken by the right-handed neutrino's Majorana bilinear, leaving twelve below that scale.

## lay
If the slots of a composite are assumed to behave as fermionic modes just like its pairs, the composite has five modes and 32 states. Half of them, those with an even number of filled modes, turn out to be exactly one generation of quarks and leptons with the right charges, including a right-handed neutrino, and the other half are the antiparticles. This is the 16 of the unified group Spin(10), arising from the framework's own modes. One extra symmetry appears; it causes no inconsistency and is broken by the neutrino's mass.

## one-liner
Under Hypothesis (S), the composite's state space $\Lambda^{\bullet}(\C^{2} \oplus \C^{3})$ is the $\mathrm{Spin}(10)$ spinor, its even half is the derived generation, and the extra generator $U(1)_{X}$ is anomaly-free in the action it carries.
