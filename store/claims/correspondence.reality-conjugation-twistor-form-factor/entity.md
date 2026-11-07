---
id: correspondence.reality-conjugation-twistor-form-factor
kind: claim
version: 8
title: "Reality: the conjugation, the invariant Hermitian form, and the factor $I_6$"
status: proved
region: correspondence
subject: conformal-spacetime
tags: [conformal-spinors, pseudoscalar-and-centre, conformal-model]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 7
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle
  version: 8
  source: maintainer pass 2026-11-07 (resolve units)
review: typed
derivations:
- name: main
  uses:
  - correspondence.chevalley-pairing@4
  - correspondence.incidence-relation-chart@7
  - correspondence.fock-model-complexified-ascended-algebra@9
  - std-algebra.inverse-of-vector@1
  - std-algebra.reflection@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T09.py
  tags:
  - label:prop:reality
- kind: check
  ref: check.py::check_conjugation_intertwines_and_is_unique
- kind: check
  ref: check.py::check_twistor_form_hermitian_invariant
- kind: check
  ref: check.py::check_null_planes_and_signature
- kind: check
  ref: check.py::check_real_chart_three_ways
locators:
  paper: T09
  number: Prop 4.5
  label: prop:reality
  line: 495
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 7 -> 8. The Fock module''s scalar, the last bare i (b_3 - i b_4, b_4 = -(i/2)(w_3 + 2w_3''), the phases e^{i theta}, the rescaling (3+4i)/5, the i-multiples, m(i x-hat)), is the central pseudoscalar I_7 = I_6 e of Cl(3,4) = Cl(2,4)_C by U3 (std-algebra.complexification-is-the-odd-extension, cited as a mention in clause (5) and its proof); I_6 stays the factor of the incidence relation, acting by left multiplication, and clause (5) says that on CS it equals +-I_7, related there and not identified. Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (other): the proof works in the complex Fock module over V_C (b_4 = -(i/2)(w_3 + 2w_3''), the phases e^{i theta} of the Hermitian form, the rescaling by (3+4i)/5), whose scalar must commute with the vector actions c(v) and is +-I_6 only on CS.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.inverse-of-vector, std-algebra.reflection where the proof uses them. Version 5 -> 6.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: kappa = Gamma c(e5) J intertwines and is unique up to a scalar (computed kernel), kappa^2 = -1, Sigma Hermitian and invariant with lambda = 1, null planes, signature (2,2), and the three descriptions of the real chart as equal 4-dimensional real subspaces. Version 4 -> 5.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: proposition
  context_refs:
  - correspondence.fock-model-complexified-ascended-algebra
  unresolved_refs:
  - ex:psi
  - rem:factori
  typing:
    by: ai-typing-pass
    added:
    - correspondence.fock-model-complexified-ascended-algebra
    note: Added the Fock model because the conjugation is built on its monomial basis and uniqueness uses
      its irreducibility; the incidence edge is a real premise for clause (5) and was kept, the reverse
      edge having been removed from the incidence theorem.
  source_title: "Reality: the conjugation, the twistor form, and the factor $i$"
  source_formal: |-
    Write $v \mapsto \bar v$ for the real structure of $V_\C$ with real points $V$, and $J$ for the antilinear map on $\Lambda^\bullet W$ that conjugates coefficients in the monomial basis built on the isotropic basis of Theorem \claimref{correspondence.fock-model-complexified-ascended-algebra}.
    \begin{enumerate}
    \item (\emph{The conjugation.}) With $\Gamma$ the parity operator ($+1$ on $\T$, $-1$ on $\T'$) and $b_4$ the fourth negative basis vector of Section \ref{sec:setting},
    \[
    \kappa := \Gamma\, c(b_4)\, J
    \]
    is an antilinear bijection of $\Lambda^\bullet W$ with $\kappa\, c(v) = c(\bar v)\, \kappa$ for all $v \in V_\C$; every antilinear map with this property is a complex multiple of $\kappa$; $\kappa$ swaps the chiralities, $\kappa(\T) = \T'$; and $\kappa^2 = -\id$.
    \item (\emph{The twistor form.}) $\Sigma(Z_1, Z_2) := B(\kappa Z_1, Z_2)$ is a nondegenerate sesquilinear form on $\T$ with $\Sigma(Z_2, Z_1) = \lambda\,\overline{\Sigma(Z_1, Z_2)}$ for a constant $\lambda$ of modulus one, so that a rescaling of $\kappa$ by a phase makes $\Sigma$ Hermitian; for the $\kappa$ of (1), $\lambda = 1$ and $\Sigma$ is Hermitian as it stands. The real bivectors act $\Sigma$-anti-Hermitianly, so $\Sigma$ is $\mathrm{Spin}(2,4)$-invariant.
    \item (\emph{Null planes.}) For every real null vector $v$ the plane of $\Psi(v)$ is $\Sigma$-null. In particular $\Som$ and $\Spi$ are $\Sigma$-null.
    \item (\emph{Signature.}) $\Sigma$ has signature $(2,2)$.
    \item (\emph{Reality of the chart, and the factor $i$.}) Let $\sigma(\omega, \pi) := \Sigma(\omega, \pi)$ be the resulting perfect pairing $\Som\times\Spi \to \C$, and call $\hat x: \Spi\to\Som$ \emph{$\sigma$-Hermitian} if $\sigma(\hat x\pi, \pi') = \overline{\sigma(\hat x\pi', \pi)}$ for all $\pi, \pi' \in \Spi$. For $A \in \operatorname{Hom}(\Spi, \Som)$ the following are equivalent: (a) the chart point $m(A)$ of Theorem \claimref{correspondence.incidence-relation-chart} is real, $m(A) \in W_{1,3}$; (b) the line $L_A$ is $\Sigma$-null; (c) $A = i\hat x$ with $\hat x$ $\sigma$-Hermitian. Consequently the real points of the affine chart are exactly the $\Sigma$-null lines skew to $L_\infty$, the incidence relation of a real point reads $\omega = i\hat x\pi$ with $\hat x$ $\sigma$-Hermitian, and on real points the chart norm is $\ip{m}{m} = -2\det A = 2\det\hat x$ in the bases of Theorem \claimref{correspondence.incidence-relation-chart}.
    \end{enumerate}
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistor space to the conformal spinor space (\\CS, \\CSm), called $\\Sigma$ the invariant Hermitian form (the twistor form, matched by the dictionary to the reversion form), and converted the factor $i$ of clause (5) and its proof to $I_6$, which acts on \\CS as the scalar $\\pm i$ (TWGA E1.3d); clause (5) holds for either sign. The construction of $\\kappa$ and the phase argument in (1) and (2) are kept with the Fock model's scalar $i$, which the dictionary does not cover ($V_\\C$ is not complexified by $I_6$)."
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - "the factor $i$ of the incidence relation, already $I_6$ (the conformal spinors unit, set by the earlier pass)"
    - "the Fock model scalar $i$ on $\\Lambda^\\bullet W$ over $V_\\C$: a complexified space"
    - "the phases $e^{i\\theta}$, $e^{-i\\theta/2}$ and $(3+4i)/5$ rescaling $\\kappa$: complex numbers used as numbers"
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - correspondence.fock-model-complexified-ascended-algebra
---

## formal
Write $v \mapsto \bar v$ for the real structure of $V_\C$ with real points $V$, and $J$ for the antilinear map on $\Lambda^\bullet W$ that conjugates coefficients in the monomial basis built on the isotropic basis of Theorem \claimref{correspondence.fock-model-complexified-ascended-algebra}.
\begin{enumerate}
\item (\emph{The conjugation.}) With $\Gamma$ the parity operator ($+1$ on $\CS$, $-1$ on $\CSm$) and $b_4$ the fourth negative basis vector of Section \ref{sec:setting},
\[
\kappa := \Gamma\, c(b_4)\, J
\]
is an antilinear bijection of $\Lambda^\bullet W$ with $\kappa\, c(v) = c(\bar v)\, \kappa$ for all $v \in V_\C$; every antilinear map with this property is a complex multiple of $\kappa$; $\kappa$ swaps the chiralities, $\kappa(\CS) = \CSm$; and $\kappa^2 = -\id$.
\item (\emph{The invariant Hermitian form.}) $\Sigma(Z_1, Z_2) := B(\kappa Z_1, Z_2)$ (the twistor form; on the conformal spinor space $\CS$ it corresponds to the reversion form) is a nondegenerate sesquilinear form on $\CS$ with $\Sigma(Z_2, Z_1) = \lambda\,\overline{\Sigma(Z_1, Z_2)}$ for a constant $\lambda$ of modulus one, so that a rescaling of $\kappa$ by a phase makes $\Sigma$ Hermitian; for the $\kappa$ of (1), $\lambda = 1$ and $\Sigma$ is Hermitian as it stands. The real bivectors act $\Sigma$-anti-Hermitianly, so $\Sigma$ is $\mathrm{Spin}(2,4)$-invariant.
\item (\emph{Null planes.}) For every real null vector $v$ the plane of $\Psi(v)$ is $\Sigma$-null. In particular $\Som$ and $\Spi$ are $\Sigma$-null.
\item (\emph{Signature.}) $\Sigma$ has signature $(2,2)$.
\item (\emph{Reality of the chart, and the factor $I_6$.}) The conformal pseudoscalar $I_6$ acts on $\CS$ as its complex unit (the factor Penrose writes as his imaginary unit). The scalars of the module are $\mathrm{span}\{1, I_7\}$, $I_7 = I_6e$ the central pseudoscalar of the odd extension $\Cl(3,4) = \Cl(2,4)_\C$, with $V_\C = V \oplus I_7V$ (\claimref{std-algebra.complexification-is-the-odd-extension}); on $\CS$, $I_6$ acting by left multiplication equals $\pm I_7$, the two being related there and not identified. Let $\sigma(\omega, \pi) := \Sigma(\omega, \pi)$ be the resulting perfect pairing $\Som\times\Spi \to \C$, and call $\hat x: \Spi\to\Som$ \emph{$\sigma$-Hermitian} if $\sigma(\hat x\pi, \pi') = \overline{\sigma(\hat x\pi', \pi)}$ for all $\pi, \pi' \in \Spi$. For $A \in \operatorname{Hom}(\Spi, \Som)$ the following are equivalent: (a) the chart point $m(A)$ of Theorem \claimref{correspondence.incidence-relation-chart} is real, $m(A) \in W_{1,3}$; (b) the line $L_A$ is $\Sigma$-null; (c) $A = I_6\hat x$ with $\hat x$ $\sigma$-Hermitian. Consequently the real points of the affine chart are exactly the $\Sigma$-null lines skew to $L_\infty$, the incidence relation of a real point reads $\omega = I_6\hat x\pi$ with $\hat x$ $\sigma$-Hermitian, and on real points the chart norm is $Q(m) = -2\det A = 2\det\hat x$ in the bases of Theorem \claimref{correspondence.incidence-relation-chart}.
\end{enumerate}

## technical
There is an antilinear bijection $\kappa = \Gamma\,c(b_4)\,J$ of the Fock module with $\kappa\,c(v) = c(\bar v)\,\kappa$ for all $v \in V_\C$, unique up to a complex multiple; it swaps the chiralities, $\kappa(\CS) = \CSm$, and $\kappa^2 = -\id$. With the Chevalley pairing it gives the invariant Hermitian form $\Sigma(Z_1, Z_2) = B(\kappa Z_1, Z_2)$ on the conformal spinor space $\CS$ (the twistor form, matched to the reversion form): nondegenerate and sesquilinear, Hermitian for this $\kappa$ (and after a phase for any multiple), $\Spin(2,4)$-invariant, and of signature $(2,2)$. For every real null vector $v$ the plane of $\Psi(v)$ is $\Sigma$-null; in particular $\Som$ and $\Spi$ are.

For $A \in \operatorname{Hom}(\Spi, \Som)$ the following are equivalent: the chart point $m(A)$ is real; the line $L_A$ is $\Sigma$-null; and $A = I_6\hat x$, with $I_6$ the complex unit of $\CS$, and $\hat x$ Hermitian for the induced pairing $\sigma$ of $\Som$ with $\Spi$. So the real points of the affine chart are the $\Sigma$-null lines skew to $L_\infty$, the incidence relation of a real point reads $\omega = I_6\hat x\pi$, and there $Q(m) = -2\det A = 2\det\hat x$.

## lay
The spinor space of the conformal algebra, as built here, is a complex space, and real spacetime has to be recovered from it by a reality condition. This result builds that condition from the completion itself: a conjugation operation and, from it, a Hermitian form on the spinor space with two positive and two negative directions. Real spacetime points are exactly the lines of spinors on which this form vanishes, and the complex unit in Penrose's incidence relation, here the conformal pseudoscalar, is forced by this reality condition.

## one-liner
The completion carries an antilinear conjugation, unique up to scale, whose invariant form on the conformal spinor space is Hermitian of signature $(2,2)$, and the real chart points are exactly the null lines of that form skew to the infinity line, with incidence relation $\omega = I_6\hat x\pi$ for Hermitian $\hat x$.
