---
id: synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field
kind: claim
version: 3
title: 'Imported: the Dirac CAR algebra on a gravitational field (Dimock 1982)'
status: imported
region: synthesis
subject: quantum-fields
tags: [car-algebra, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-01
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle
  version: 3
  source: maintainer pass 2026-11-07 (resolve units)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'J. Dimock, Dirac quantum fields on a manifold, Trans. Amer. Math. Soc. 269 (1982), 133--147.'
  key: Dimock1982
  doi: 10.1090/S0002-9947-1982-0637032-8
  locator: 'Sec. II.A (S = S+ - S-, after Thm. 2.1); Sec. II.B (Prop. 2.2, Thm. 2.3, Prop. 2.4(b)-(d)); Sec. III.A (the inner product on Cauchy data); Sec. III.B and Thm. 3.1 (the anticommutator)'
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3. Restated by U4: the factor -i of Dimock''s normalisation u = -i S p'' gamma u_0 is the Dirac field''s unit, I_4 on the (even) spinor values (U1, as in the Hadamard chain); the text now says that the source''s formula carries a factor -I_4 that the store''s normalisation of S removes, and the source''s form (the formal level as first stored) moves to extraction.source_formal; the source writes i for I_4. Status stays imported. Declaration removed.'
  source_formal: |-
    Let $(\hb, \Omega)$ be a gravitational field on four-dimensional flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric is globally hyperbolic, read on several charts where its global structure needs them, and consider the free Dirac field of mass $m_{0} \ge 0$ on it.
    \begin{enumerate}
    \item[(a)] \emph{(The field algebra.)} (Dimock) There are field operators $\psi(f)$ satisfying the Dirac equation with a causal anticommutator: $\{\psi(f), \psi(h)^{*}\}$ is the pairing given by the causal propagator of the Dirac operator and vanishes when the supports of $f$ and $h$ are spacelike separated. Formulated through the C$^{*}$-algebras of local observables (the CAR algebras of regions), the construction is free of ambiguity, and the net of these algebras satisfies a generalised form of the Haag-Kastler axioms (isotony, causality, covariance under the isometries of the field). No state is selected.
    \item[(b)] \emph{(Reproducing formula; Dimock, Prop.~2.4, Sec.~III, Thm.~3.1.)} Let $S_{\pm}$ be the retarded and advanced fundamental solutions of the Dirac operator and $S = S_{+} - S_{-}$ the causal propagator. For a Cauchy surface $\Sigma$ with future unit normal $n$, the inner product of solutions $(\Phi, \Phi')$, the polarisation of the flux $\int_{\Sigma}J_{\Phi}\cdot n\,d\Sigma$ of the conserved current $J_{\Phi} = \Phi e_{0}\tilde\Phi$, does not depend on $\Sigma$; every solution is reproduced from its Cauchy data by $S$, $\Phi(x) = \int_{\Sigma}S(x, x')\,n(x')\,\Phi(x')\,d\Sigma'$ (in the source's normalisation $u = -iSp'\gamma u_{0}$, with $p'$ the adjoint of the restriction to $\Sigma$; the store normalises $S$ so that no factor $-i$ appears); and the anticommutator pairing of (a) is the inner product of the solutions the test spinors define, $\{\psi(f), \psi(h)^{*}\} = (Sf, Sh)$, with $(Sf, \Phi) = \int f^{\dagger}\Phi$ for smooth solutions $\Phi$.
    \end{enumerate}
    \emph{Provenance:} \cite{Dimock1982}. \emph{Beyond one flat chart.} Global hyperbolicity and the Cauchy surfaces are global; the algebra of a region is read on one chart.
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the only i is in the source''s normalisation u = -iSp'' gamma u_0, quoted as Dimock states it, beside the store''s normalisation of S, in which no such factor appears. Declared imported (version and levels unchanged).'
  note: >-
    Imported so that the results on the field theory on a gravitational field can cite the existence of the
    Dirac field algebra, as distinct from a state on it, instead of citing it from memory. Checked on
    2026-11-01 against the publisher's record (author, title, Trans. Amer. Math. Soc. 269 (1982) 133-147, DOI)
    and its abstract: on globally hyperbolic Lorentzian manifolds field operators are constructed which satisfy
    the Dirac equation and have a causal anticommutator; ambiguities in the construction are removed by
    formulating the theory in terms of C*-algebras of local observables; a generalised form of the Haag-Kastler
    axioms is verified. Cited from memory, not checked: that the construction proceeds through the CAR algebra
    over the space of solutions with Cauchy data on a Cauchy surface. No state is part of this Fact.
    Clause (b), added in version 2 (2 November 2026), checked against the publisher's scanned text of the paper
    (symbols partly garbled in the text conversion; checked in substance): the propagator is S = S+ - S-, S+- the
    retarded and advanced fundamental solutions of the Dirac operator of Thm. 2.1(a), supported in J+-(supp f),
    with S* = -S (Sec. II.A); the solution of the Cauchy problem with data u0 on Sigma is u = -i S p' gamma u0,
    p' the adjoint of the restriction to Sigma and gamma the Dirac matrix contracted with the normal (Prop. 2.4(b)),
    with -i S p' gamma p S = S (Prop. 2.4(d)) and existence and uniqueness (Thm. 2.3); the inner product on
    Cauchy data is (f1, f2) = <f1, gamma_n f2> (Sec. III.A), its independence of the Cauchy surface following
    from the integral identity (1.7) (Prop. 1.2) with Prop. 2.4(c) (Sec. III.B); and {psi(h), psi+(f)} =
    -i (h, S f) = <gamma p S h, p S f> (Sec. III.B, Thm. 3.1), the form Dimock attributes to Lichnerowicz. The
    translation into the spacetime algebra (the Cauchy inner product as the flux of the current Phi e0 Phi~, and
    S normalised so that the reproducing formula carries no factor -i) is the store's reading.
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, at Leon''s decisions of 2 November 2026 (Hadamard scaling bound): clause (b) added, Dimock''s reproducing formula (the causal propagator reproduces a solution from its Cauchy data, and the anticommutator pairing is the conserved Cauchy inner product of the solutions), checked against the paper (Prop. 2.4, Sec. III, Thm. 3.1), so that the flux-contraction and generator-CAR results cite it as a Fact; what version 1 asserted is now clause (a), unchanged.'
  flags:
  - 'beyond one flat chart: global hyperbolicity and the Cauchy surface are global; the field algebra of a region is read on one chart'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on four-dimensional flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric is globally hyperbolic, read on several charts where its global structure needs them, and consider the free Dirac field of mass $m_{0} \ge 0$ on it.
\begin{enumerate}
\item[(a)] \emph{(The field algebra.)} (Dimock) There are field operators $\psi(f)$ satisfying the Dirac equation with a causal anticommutator: $\{\psi(f), \psi(h)^{*}\}$ is the pairing given by the causal propagator of the Dirac operator and vanishes when the supports of $f$ and $h$ are spacelike separated. Formulated through the C$^{*}$-algebras of local observables (the CAR algebras of regions), the construction is free of ambiguity, and the net of these algebras satisfies a generalised form of the Haag-Kastler axioms (isotony, causality, covariance under the isometries of the field). No state is selected.
\item[(b)] \emph{(Reproducing formula; Dimock, Prop.~2.4, Sec.~III, Thm.~3.1.)} Let $S_{\pm}$ be the retarded and advanced fundamental solutions of the Dirac operator and $S = S_{+} - S_{-}$ the causal propagator. For a Cauchy surface $\Sigma$ with future unit normal $n$, the inner product of solutions $(\Phi, \Phi')$, the polarisation of the flux $\int_{\Sigma}J_{\Phi}\cdot n\,d\Sigma$ of the conserved current $J_{\Phi} = \Phi e_{0}\tilde\Phi$, does not depend on $\Sigma$; every solution is reproduced from its Cauchy data by $S$, $\Phi(x) = \int_{\Sigma}S(x, x')\,n(x')\,\Phi(x')\,d\Sigma'$ (in the source's normalisation the formula carries a factor $-I_{4}$, $I_{4}$ the field's unit on the spinor values, with $p'$ the adjoint of the restriction to $\Sigma$; the store normalises $S$ so that no such factor appears); and the anticommutator pairing of (a) is the inner product of the solutions the test spinors define, $\{\psi(f), \psi(h)^{*}\} = (Sf, Sh)$, with $(Sf, \Phi) = \int f^{\dagger}\Phi$ for smooth solutions $\Phi$.
\end{enumerate}
\emph{Provenance:} \cite{Dimock1982}. \emph{Beyond one flat chart.} Global hyperbolicity and the Cauchy surfaces are global; the algebra of a region is read on one chart.

## technical
Before one can ask for a quantum state of the Dirac field in a gravitational field, the field itself, as an algebra of operators, has to exist. Dimock showed that on every spacetime with a well-posed initial-value problem (globally hyperbolic) the free Dirac field exists, with anticommutators that vanish at spacelike separation, and that its algebras of local observables satisfy the standard axioms of algebraic quantum field theory in a form adapted to curved backgrounds. In the store's language: on every gravitational field with a globally hyperbolic derived metric the Dirac CAR algebra exists; what is not fixed is a state, which is a separate datum. The same construction shows that the anticommutator of two smeared fields is the conserved inner product (the flux of the current through any instant) of the classical solutions they define, and that the causal propagator rebuilds every solution from its values at one instant.

## lay
The rules of quantum field theory for electrons and similar particles can be set up in any reasonable gravitational field: the field's operators exist and respect causality. Dimock proved this in 1982. What the construction does not provide is a choice of the quantum state, the analogue of empty space, which has to be supplied separately. This is taken from the literature.

## one-liner
On every gravitational field with a globally hyperbolic derived metric the free Dirac field exists, with a causal anticommutator and CAR algebras of local observables satisfying a generalised form of the Haag-Kastler axioms; the causal propagator reproduces every solution from its Cauchy data and the anticommutator pairing is the conserved Cauchy inner product of the solutions; no state is selected (Dimock 1982).
