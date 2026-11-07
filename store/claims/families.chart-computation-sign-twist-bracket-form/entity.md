---
id: families.chart-computation-sign-twist-bracket-form
kind: claim
version: 6
title: 'The chart computation: the sign twist, the bracket form, and the Fourier coordinates'
status: proved
region: families
subject: generations
tags:
- flavour-and-mixing
- representation-theory
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 6
  source: maintainer pass 2026-11-07 (GA units)
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T13.py
  tags:
  - label:prop:chart
- kind: check
  ref: check.py::check_sign_twist
- kind: check
  ref: check.py::check_bracket_form
- kind: check
  ref: check.py::check_fourier_coordinates_and_the_one_number
locators:
  paper: T13
  number: Prop 5.4
  label: prop:chart
  line: 752
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The Fourier unit in zeta = e^{2 pi i/3} and the phase of Gamma = |Gamma| e^{i delta} became I_4, with numbers (and the complexified doublet) read in span{1, I_4}, and the complex line C named span{1, I_4}; no bare i remains.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the sign twist and 3 x sgn = sgn + 2, the bracket form (Cauchy-Binet, Fourier null lines, 6ab), and the Fourier coordinates with |Gamma|^2/a^2 and delta on the lepton data. Version 3 -> 4. Fix round: the Fourier check asserts 2 v0 > v1 + v2 and v2 > v1 on the lepton bounds (delta in the first quadrant) and the sign relations at the samples. Version 4 -> 5.'
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - 'zeta = e^{2 pi i/3} and Gamma = |Gamma| e^{i delta}: roots of unity and a complex number parametrising
      the family doublet, numbers'
  env: proposition
  context_refs:
  - families.alignment-computed-thirteenth-refutation-democracy-one
  - families.imported-dictionary-exact-join
  - families.koide-nullity-condition-one-member-invariant
  eqrefs: 1
  typing:
    by: ai-typing-pass
    note: 'No edges: the proof is self-contained; the alignment, dictionary and nullity citations are
      comparison or disambiguation (the nullity family is only named, the invariant-tensor count is redone
      in the proof); the classic Koide parametrisation is recovered but no imported store claim carries
      it, so no standard route. Levels pass: lay now says the vector holds square roots of masses and
      that the bracket form is singled out only by excluding the all-ones tensor, which the paper does
      not supply.'
  source_title: 'The chart computation: the sign twist, the bracket form, and the Fourier coordinates'
  source_formal: 'Face space has a concrete realisation: the three $\omega$-spinors lie in the two-dimensional
    $S_{\omega}$, so the face vector of pairwise brackets $\Omega = ([\omega^{2}\omega^{3}], [\omega^{3}\omega^{1}],
    [\omega^{1}\omega^{2}])$ is the vector of $2 \times 2$ minors of a $3 \times 2$ array. Three consequences.

    \begin{enumerate}

    \item \emph{(The sign twist.)} Under an odd permutation of the twistor labels, $\Omega \mapsto -P\,\Omega$:
    the face vector transforms in $\mathbf{3} \otimes \mathrm{sgn} = \mathrm{sgn} \oplus \mathbf{2}$.
    The democratic direction is the sign representation, invariant as a line and odd as a vector, consistent
    with Proposition \claimref{families.alignment-computed-thirteenth-refutation-democracy-one}''s language
    (a direction, not a vector) and tying the line''s two orientations to the $S_{3}$-odd structure the
    ordering must break.

    \item \emph{(The bracket form, and what it selects.)} The complex-bilinear form on face space built
    from the symplectic $\varepsilon$ on the spinor slots and the Kronecker $\delta$ on the family slots
    is $C(\Omega) = \sum_{k}\Omega_{k}^{2}$ (the letter is the series'' for this form; it is not the Casimir
    $C$ of Fact \claimref{families.imported-dictionary-exact-join}), the Cauchy-Binet norm of the minors.
    It is $S_{3}$-invariant, and it is the member $\alpha = 1$, $\beta = -1$ of Proposition \claimref{families.koide-nullity-condition-one-member-invariant}''s
    family: on a real face vector $C(v) = s^{2} + |d|^{2} = |v|^{2}$, Euclidean, and $C(v_{\mathrm{lepton}})
    = \sum_{k} m_{k} = 1883$ MeV, not zero. The $S_{3}$-invariant tensors on the family indices are $\delta_{kl}$
    and the all-ones $J_{kl}$, so $C$ is singled out among the invariant forms only by excluding $J$,
    that is by requiring invariance under $O(3)$ on family indices rather than $S_{3}$, which nothing
    in the paper supplies. On the complexified doublet $C$ is nondegenerate, so, like every nondegenerate
    two-dimensional complex quadratic space, it is a hyperbolic plane: $C(f_{\pm}) = 0$ and $C(f_{+},
    f_{-}) = 3$ for the Fourier vectors $f_{\pm} = (1, \zeta^{\pm 1}, \zeta^{\mp 1})$, $\zeta = e^{2\pi
    i/3}$, and $C(af_{+} + bf_{-}) = 6ab$, so its null vectors are exactly the two Fourier lines. Those
    lines contain no nonzero real vector: $C$-nullity and the $q$-nullity of Proposition \claimref{families.koide-nullity-condition-one-member-invariant}
    share nothing but the word.

    \item \emph{(The Fourier coordinates, and the one number.)} The map $\Gamma \mapsto (\mathrm{Re}(\Gamma\zeta^{k}))_{k}$
    is an $\R$-linear bijection from $\C$ onto the real doublet plane $\{d : \sum_{k} d_{k} = 0\}$, so
    every real face vector has the form

    \begin{equation}

    \sqrt{m_{k}} \;=\; a + |\Gamma|\cos\!\Bigl(\delta + \frac{2\pi k}{3}\Bigr), \qquad \delta = \arg\Gamma,

    \end{equation}

    three real parameters for three components: the classic Koide parametrisation, with its $2\pi/3$ phase
    spacing, is the Fourier coordinate system on $\mathbb{Z}/3$ and carries no hypothesis. In these coordinates
    the relation''s entire content is one number: $Q_{\sqrt{m}} = \tfrac23 \iff |\Gamma|^{2} = 2a^{2}$,
    and the charged-lepton data give $|\Gamma|/a = 1.4142$ against $\sqrt{2} = 1.4142$ (the script certifies
    $|\Gamma|^{2}/a^{2} = 6Q_{\sqrt{m}} - 2$ inside $2 \pm 10^{-4}$), with $\delta = 0.222$ the free phase
    that encodes $m_{\mu}/m_{e}$, for the labelling $k = 0, 1, 2 = \tau, e, \mu$. The normalisation $|\Gamma|^{2}
    = 2a^{2}$, the one number, is Section \ref{sec:gaussian}''s question.

    \end{enumerate}'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: Only the twistor labels became spinor labels. The Fourier unit i in zeta = e^{2 pi i/3}, the
      complex doublet and the complex-bilinear form C are face-space (Z/3) structure, not twistor machinery,
      and are kept as written.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises:
    - families.koide-nullity-condition-one-member-invariant (motivated_by)
    added_dependants: []
    added_about: []
    verdict: connected
    note: Proof is self-contained, so no premise added; clause (2) answers the choice of member that the
      nullity proposition leaves open, recorded as lineage; the crossing proof's use of clause (3) was
      left removed, as the typing pass judged it a cross-check of a root already obtained.
lineage:
  motivated_by:
  - families.koide-nullity-condition-one-member-invariant
---

## formal
Face space has a concrete realisation: the three $\omega$-spinors lie in the two-dimensional $S_{\omega}$, so the face vector of pairwise brackets $\Omega = ([\omega^{2}\omega^{3}], [\omega^{3}\omega^{1}], [\omega^{1}\omega^{2}])$ is the vector of $2 \times 2$ minors of a $3 \times 2$ array. Three consequences.
\begin{enumerate}
\item \emph{(The sign twist.)} Under an odd permutation of the spinor labels, $\Omega \mapsto -P\,\Omega$: the face vector transforms in $\mathbf{3} \otimes \mathrm{sgn} = \mathrm{sgn} \oplus \mathbf{2}$. The democratic direction is the sign representation, invariant as a line and odd as a vector, consistent with Proposition \claimref{families.alignment-computed-thirteenth-refutation-democracy-one}'s language (a direction, not a vector) and tying the line's two orientations to the $S_{3}$-odd structure the ordering must break.
\item \emph{(The bracket form, and what it selects.)} The complex-bilinear form on face space built from the symplectic $\varepsilon$ on the spinor slots and the Kronecker $\delta$ on the family slots is $C(\Omega) = \sum_{k}\Omega_{k}^{2}$ (the letter is the series' for this form; it is not the Casimir $C$ of Fact \claimref{families.imported-dictionary-exact-join}), the Cauchy-Binet norm of the minors. It is $S_{3}$-invariant, and it is the member $\alpha = 1$, $\beta = -1$ of Proposition \claimref{families.koide-nullity-condition-one-member-invariant}'s family: on a real face vector $C(v) = s^{2} + |d|^{2} = |v|^{2}$, Euclidean, and $C(v_{\mathrm{lepton}}) = \sum_{k} m_{k} = 1883$ MeV, not zero. The $S_{3}$-invariant tensors on the family indices are $\delta_{kl}$ and the all-ones $J_{kl}$, so $C$ is singled out among the invariant forms only by excluding $J$, that is by requiring invariance under $O(3)$ on family indices rather than $S_{3}$, which nothing in the paper supplies. On the complexified doublet $C$ is nondegenerate, so, like every nondegenerate two-dimensional complex quadratic space, it is a hyperbolic plane: $C(f_{\pm}) = 0$ and $C(f_{+}, f_{-}) = 3$ for the Fourier vectors $f_{\pm} = (1, \zeta^{\pm 1}, \zeta^{\mp 1})$, $\zeta = e^{2\pi I_4/3}$ (numbers are read in $\mathrm{span}\{1, I_4\}$), and $C(af_{+} + bf_{-}) = 6ab$, so its null vectors are exactly the two Fourier lines. Those lines contain no nonzero real vector: $C$-nullity and the $q$-nullity of Proposition \claimref{families.koide-nullity-condition-one-member-invariant} share nothing but the word.
\item \emph{(The Fourier coordinates, and the one number.)} The map $\Gamma \mapsto (\mathrm{Re}(\Gamma\zeta^{k}))_{k}$ is an $\R$-linear bijection from $\mathrm{span}\{1, I_4\}$ onto the real doublet plane $\{d : \sum_{k} d_{k} = 0\}$, so every real face vector has the form
\begin{equation}
\sqrt{m_{k}} \;=\; a + |\Gamma|\cos\!\Bigl(\delta + \frac{2\pi k}{3}\Bigr), \qquad \delta = \arg\Gamma,
\end{equation}
three real parameters for three components: the classic Koide parametrisation, with its $2\pi/3$ phase spacing, is the Fourier coordinate system on $\mathbb{Z}/3$ and carries no hypothesis. In these coordinates the relation's entire content is one number: $Q_{\sqrt{m}} = \tfrac23 \iff |\Gamma|^{2} = 2a^{2}$, and the charged-lepton data give $|\Gamma|/a = 1.4142$ against $\sqrt{2} = 1.4142$ (the script certifies $|\Gamma|^{2}/a^{2} = 6Q_{\sqrt{m}} - 2$ inside $2 \pm 10^{-4}$), with $\delta = 0.222$ the free phase that encodes $m_{\mu}/m_{e}$, for the labelling $k = 0, 1, 2 = \tau, e, \mu$. The normalisation $|\Gamma|^{2} = 2a^{2}$, the one number, is Section \ref{sec:gaussian}'s question.
\end{enumerate}

## technical
The three $\omega$-spinors live in the two-dimensional $S_{\omega}$, so the face vector of pairwise brackets $\Omega = ([\omega^{2}\omega^{3}], [\omega^{3}\omega^{1}], [\omega^{1}\omega^{2}])$ is the vector of $2 \times 2$ minors of a $3 \times 2$ array. An odd permutation of the labels sends $\Omega \mapsto -P\,\Omega$, so face space carries $\mathbf{3} \otimes \mathrm{sgn} = \mathrm{sgn} \oplus \mathbf{2}$, and the democratic line is the sign representation: invariant as a line, odd as a vector.

The bilinear form built from $\varepsilon$ on the spinor slots and $\delta$ on the family slots is $C(\Omega) = \sum_{k}\Omega_{k}^{2}$, the Cauchy-Binet norm of the minors. On real face vectors it is the Euclidean form, the member $\alpha = 1$, $\beta = -1$ of the invariant family, and it does not vanish on the lepton vector; among $S_{3}$-invariant forms it is singled out only by excluding the all-ones tensor $J$. On the complexified doublet it is a hyperbolic plane whose null lines are the Fourier lines $f_{\pm} = (1, \zeta^{\pm 1}, \zeta^{\mp 1})$, $\zeta = e^{2\pi I_4/3}$ (numbers are read in $\mathrm{span}\{1, I_4\}$), which contain no nonzero real vector. Finally $\Gamma \mapsto (\mathrm{Re}(\Gamma\zeta^{k}))_{k}$ identifies $\mathrm{span}\{1, I_4\}$ with the real doublet plane, so $\sqrt{m_{k}} = a + |\Gamma|\cos(\delta + 2\pi k/3)$ with no hypothesis, and in these coordinates $Q_{\sqrt{m}} = \tfrac23$ if and only if $|\Gamma|^{2} = 2a^{2}$; the charged-lepton data give $|\Gamma|/a = 1.4142$.

## lay
The square roots of a family's three masses can be packaged as a vector with three components, and this result works out how that vector behaves when the labels are shuffled and how the construction's bracket form measures its length. That measure turns out to be ordinary length, singled out among the symmetric choices only by an extra symmetry requirement that nothing in the paper supplies, and it does not turn the Koide relation into a light-cone condition. The result also shows that the familiar way of writing the three masses with angles a third of a turn apart is just a coordinate system, with no physics assumed. In those coordinates the whole Koide relation is one number, a ratio equal to the square root of two, which the lepton masses match to four decimal places.

## one-liner
The face vector of brackets carries a sign twist, its bracket form is Euclidean on real vectors and null only on the Fourier lines, and in Fourier coordinates the Koide relation is the single condition $|\Gamma|^{2} = 2a^{2}$.
