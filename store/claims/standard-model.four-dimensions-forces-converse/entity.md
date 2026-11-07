---
id: standard-model.four-dimensions-forces-converse
kind: claim
version: 4
title: Four dimensions from the forces, and the converse
status: proved
region: standard-model
subject: standard-model
tags: [gauge-fields, forcing-and-uniqueness]
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
  - standard-model.gauge-algebra-minimal-massive-composite@4
  - standard-model.pair-count-dimension@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12.py
  tags:
  - label:prop:four
- kind: check
  ref: check.py::check_pair_count_and_even_dimensions
- kind: check
  ref: check.py::check_converse_two_by_three
locators:
  paper: T12
  number: Prop 4.3
  label: prop:four
  line: 1007
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the automorphism algebra of C^m x C^k computed as exact ranks for m, k <= 4 and the even dimensions n <= 8, with the pair count from a maximal isotropic subspace. Version 3 -> 4.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted the single twistor, the pair count per twistor and ''two twistors of three pairs'' to conformal spinors at every level; in dimension n the conformal spinor is that of the conformal algebra of dimension n. The proof had no twistor language.'
  source_title: |-
    Four dimensions from the forces, and the converse
  source_formal: |-
    (1) Let the spacetime dimension $n$ be even, and suppose that in dimension $n$, as in dimension four (Fact \claimref{mass.mass-symplectic-area-two-twistor-formula}), a single twistor is massless and mass first exists at two constituents. Then the pair count per twistor is $(n+2)/2$ (Lemma \claimref{standard-model.pair-count-dimension}), the minimal massive hierarchy is $\C^{2} \otimes \C^{(n+2)/2}$, and its automorphism algebra is $\su(2) \oplus \su((n+2)/2) \oplus \uu(1)$ by the argument of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}, which for $m \neq k$ uses the Segre lemma and the tensor factorisation only, and which at $n = 2$, where $m = k = 2$, still applies because an automorphism is defined as a map of the form $A \otimes B$, so that the swap of factors is excluded by definition, as in (2). This equals the Standard Model algebra if and only if $n = 4$. If, therefore, the gauge algebra of matter is the automorphism algebra of its minimal massive compositeness, four dimensions is a consequence: four is the dimension in which the pair count is three. The identification premise is Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}'s reading, the mass-begins-at-two hypothesis in dimension $n \neq 4$ is a hypothesis (the mass paper proves it in dimension four only), and both conditionalities are declared.

    (2) Conversely, with no hypothesis on $n$: for every two-factor hierarchy $\C^{m} \otimes \C^{k}$ with $m, k \ge 1$ the automorphism algebra is $\su(m) \oplus \su(k) \oplus \uu(1)$, of dimension $m^{2} + k^{2} - 1$, and it is isomorphic to the Standard Model algebra if and only if $\{m, k\} = \{2, 3\}$ as an unordered pair. So the gauge algebra, once identified, forces the hierarchy to be a two-by-three, and one further input orders it: given that mass begins at two constituents ($m = 2$), the pair count is three, hence four dimensions by Lemma \claimref{standard-model.pair-count-dimension}; given four dimensions ($k = 3$), the constituents number two. Under Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}'s reading, each of the two framework inputs is a consequence of the observed forces together with the other, not only consistent with them; the algebra alone does not distinguish two twistors of three pairs from three twistors of two.
  env: proposition
  context_refs:
  - mass.mass-symplectic-area-two-twistor-formula
  - standard-model.pair-count-dimension
  eqrefs: 1
  typing:
    by: ai-typing-pass
    added:
    - standard-model.pair-count-dimension
    note: 'Added the pair-count lemma, used for the pair count (n+2)/2; did not add the mass-as-area theorem,
      since in dimension n the mass-at-two condition is a declared hypothesis and the theorem is cited
      only as the four-dimensional case. Levels pass: the lay now keeps the mass-begins-at-two hypothesis
      (declared away from n = 4) on part (1); the one-liner keeps the even-dimension scope.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.pair-count-dimension
---

## formal
(1) Let the spacetime dimension $n$ be even, and suppose that in dimension $n$, as in dimension four (Fact \claimref{mass.mass-symplectic-area-two-twistor-formula}), a single conformal spinor (twistor) is massless and mass first exists at two constituents. Then the pair count per conformal spinor is $(n+2)/2$ (Lemma \claimref{standard-model.pair-count-dimension}), the minimal massive hierarchy is $\C^{2} \otimes \C^{(n+2)/2}$, and its automorphism algebra is $\su(2) \oplus \su((n+2)/2) \oplus \uu(1)$ by the argument of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}, which for $m \neq k$ uses the Segre lemma and the tensor factorisation only, and which at $n = 2$, where $m = k = 2$, still applies because an automorphism is defined as a map of the form $A \otimes B$, so that the swap of factors is excluded by definition, as in (2). This equals the Standard Model algebra if and only if $n = 4$. If, therefore, the gauge algebra of matter is the automorphism algebra of its minimal massive compositeness, four dimensions is a consequence: four is the dimension in which the pair count is three. The identification premise is Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}'s reading, the mass-begins-at-two hypothesis in dimension $n \neq 4$ is a hypothesis (the mass paper proves it in dimension four only), and both conditionalities are declared.

(2) Conversely, with no hypothesis on $n$: for every two-factor hierarchy $\C^{m} \otimes \C^{k}$ with $m, k \ge 1$ the automorphism algebra is $\su(m) \oplus \su(k) \oplus \uu(1)$, of dimension $m^{2} + k^{2} - 1$, and it is isomorphic to the Standard Model algebra if and only if $\{m, k\} = \{2, 3\}$ as an unordered pair. So the gauge algebra, once identified, forces the hierarchy to be a two-by-three, and one further input orders it: given that mass begins at two constituents ($m = 2$), the pair count is three, hence four dimensions by Lemma \claimref{standard-model.pair-count-dimension}; given four dimensions ($k = 3$), the constituents number two. Under Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}'s reading, each of the two framework inputs is a consequence of the observed forces together with the other, not only consistent with them; the algebra alone does not distinguish two conformal spinors of three pairs from three of two.

## technical
(1) In even dimension $n$, if a single conformal spinor is massless and mass first exists at two constituents, the pair count is $(n+2)/2$, the minimal massive hierarchy is $\C^{2} \otimes \C^{(n+2)/2}$, and its automorphism algebra $\su(2) \oplus \su((n+2)/2) \oplus \uu(1)$ is the Standard Model algebra exactly when $n = 4$. So if the gauge algebra of matter is the automorphism algebra of its minimal massive composite, four dimensions follows; that identification, and the mass-at-two hypothesis away from $n = 4$, are declared premises.

(2) Conversely, for any hierarchy $\C^{m} \otimes \C^{k}$ the algebra is $\su(m) \oplus \su(k) \oplus \uu(1)$, of dimension $m^{2} + k^{2} - 1$, which equals the Standard Model's twelve only for $\{m, k\} = \{2, 3\}$. Given $m = 2$ the pair count is three, hence $n = 4$; given $n = 4$ there are two constituents. The algebra alone does not distinguish two conformal spinors of three pairs from three of two.

## lay
If the forces of nature are the symmetries of the smallest composite of basic spinor states that can have mass, and if, as in four dimensions, mass first appears at two such states (a hypothesis in other dimensions), then spacetime must have four dimensions: in any other even dimension the symmetries come out wrong. Run backwards, the observed forces require a two-by-three structure, and either of the framework's two inputs, two constituents or four dimensions, then fixes the other. Both directions rest on identifying the forces with these symmetries, which is stated as a premise.

## one-liner
Under the reading that the gauge algebra is the automorphism algebra of the minimal massive composite, the Standard Model algebra forces four dimensions among the even dimensions given mass at two constituents, and in general forces a two-by-three hierarchy.
