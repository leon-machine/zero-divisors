---
id: rule2.rule-2-kaluza-klein-algebra
kind: claim
version: 6
title: Rule 2 in the Kaluza-Klein algebra
status: proved
region: rule2
subject: completion
tags: [transport-algorithm, obstruction-types, finite-models, grading-and-parity]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T17-rule2, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: strengthened check and wording
  version: 6
  source: maintainer pass of 7 November 2026
outside_ga:
  kind: bridge
  why: 'the two ideals are compared with the five-dimensional Dirac (gamma-matrix) representations of the imported Fact, stated in that source''s language; the algebra itself is worked in GA'
review: typed
about:
- obj.transport.obstruction-types
derivations:
- name: main
  uses:
  - rule2.even-subalgebra-one-dimensional-extension@4
  - rule2.imported-classification-centre-type-c@3
  - rule2.imported-completion-spacetime-algebra-spinors@5
  - rule2.imported-gamma-matrices-odd-dimension@1
  - rule2.imported-rule-2-matrix-units-forgotten@3
  - rule2.where-obstruction-sits-commuting-square@5
  - std-algebra.orthogonal-anticommute@1
  - std-algebra.sta-matrix@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T17_rule2.py
  tags:
  - label:thm:KK
- kind: check
  ref: check.py::check_type_c_and_ideals
- kind: check
  ref: check.py::check_ideals_are_spacetime_algebra_two_dirac_reps
- kind: check
  ref: check.py::check_fifth_parity_is_outer
- kind: check
  ref: check.py::check_two_repairs_matrix_units_centre_r
- kind: check
  ref: check.py::check_parity_becomes_inner_boost_or_rotation
- kind: check
  ref: check.py::check_cl24_is_rule_one_ascent_of_spacetime
locators:
  paper: T17-rule2
  number: Thm 3.2
  label: thm:KK
  line: 197
extraction:
  maintainer_pass_warnings:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 6: check_fifth_parity_is_outer now also asserts that the reflection negates exactly 16 of the 32 basis blades (a hand-stated count the mutation test can perturb); outside_ga declared for the comparison with the Dirac representations of the imported gamma-matrix Fact.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.orthogonal-anticommute, std-algebra.sta-matrix where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: type C of Cl(1,4), the ideals as spacetime algebras with eps_pm e4 = -+eps_pm gamma, the outer fifth parity, the repairs Cl(2,4) and Cl(1,5) with matrix units and centre R, the parity made inner, and Cl(2,4) as the Rule 1 ascent. Version 3 -> 4.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'All six uses are premises of named items; the six-to-five-dimensional spinor reduction the
      discussion calls familiar is not an imported claim in the store, so no standard-route derivation;
      E204 is inherited from the spinor identification via the twistor Fact. Levels pass: conditions already
      kept.'
  source_title: 'Rule 2 in the Kaluza-Klein algebra'
  source_formal: |-
    In $A_5 = \Cl(1,4)$:
    \begin{enumerate}
    \item[(i)] the volume element $\omega = \gamma e_4$ is central with $\omega^2 = +1$; $A_5$ is type C, $A_5 = \varepsilon_+ A_5 \oplus \varepsilon_- A_5$;
    \item[(ii)] each ideal is a copy of the spacetime algebra: $a \mapsto \varepsilon_\pm a$ is an injective homomorphism $\Cl(1,3) \to \varepsilon_\pm A_5$ onto the ideal, and under it the fifth generator becomes minus or plus the spacetime pseudoscalar,
    \[
    \varepsilon_+ e_4 = -\,\varepsilon_+\gamma, \qquad \varepsilon_- e_4 = +\,\varepsilon_-\gamma :
    \]
    the two ideals are the two inequivalent five-dimensional Dirac representations of Fact \claimref{rule2.imported-gamma-matrices-odd-dimension}, $\Gamma^4 = \mp\,\Gamma^0\Gamma^1\Gamma^2\Gamma^3$, on the one Dirac spinor of $\Cl(1,3) \cong \Mat_2(\HH)$;
    \item[(iii)] the reflection of the fifth direction, $R: e_4 \mapsto -e_4$ with $e_0, \ldots, e_3$ fixed, extends to the automorphism $\hat{\cdot} \circ \Ad_{e_4}$ of $A_5$, sends $\omega \mapsto -\omega$, exchanges the ideals, and is outer: the five-dimensional parity is the exchange that Fact \claimref{rule2.imported-classification-centre-type-c} says no inner automorphism can perform;
    \item[(iv)] the Rule 2 repairs are $\Cl(2,4)$ ($\nu^2 = +1$) and $\Cl(1,5)$ ($\nu^2 = -1$), both $\cong \Mat_2(\Cl^0(1,4)) \cong \Mat_2(\Cl(1,3)) \cong \Mat_4(\HH)$, simple with centre $\R$, in which $\varepsilon_\pm$ are the diagonal matrix units;
    \item[(v)] in either repair $\Ad_\nu$ restricts to the grade involution of $A_5$ and $\Ad_{\nu e_4}$ restricts to the parity $R$: the outer exchange has become inner, and it is a boost, $(\nu e_4)^2 = +1$, in $\Cl(2,4)$ and a rotation, $(\nu e_4)^2 = -1$, in $\Cl(1,5)$;
    \item[(vi)] $\Cl(2,4)$ is the Rule 1 ascent of $\Cl(1,3)$, the conformal algebra of Minkowski space whose spinors carry twistor space (Fact \claimref{rule2.imported-completion-spacetime-algebra-spinors}): the pair $(\nu, e_4)$ is its hyperbolic plane and $f = \tfrac12(\nu + e_4)$, $f^* = \tfrac12(\nu - e_4)$ its ladder pair; $\Cl(1,5)$ is the same algebra at residue $4$ with a definite adjoined plane. The residues run $6 \to 5 \to 6$ or $6 \to 5 \to 4$.
    \end{enumerate}
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'One phrase in clause (vi) and one in the lay level converted (the spinors of $\Cl(2,4)$ carry the conformal spinor space $\CS$). The rest is already geometric algebra; the proof is unchanged.'
---

## formal
In $A_5 = \Cl(1,4)$:
\begin{enumerate}
\item[(i)] the volume element $\omega = \gamma e_4$ is central with $\omega^2 = +1$; $A_5$ is type C, $A_5 = \varepsilon_+ A_5 \oplus \varepsilon_- A_5$;
\item[(ii)] each ideal is a copy of the spacetime algebra: $a \mapsto \varepsilon_\pm a$ is an injective homomorphism $\Cl(1,3) \to \varepsilon_\pm A_5$ onto the ideal, and under it the fifth generator becomes minus or plus the spacetime pseudoscalar,
\[
\varepsilon_+ e_4 = -\,\varepsilon_+\gamma, \qquad \varepsilon_- e_4 = +\,\varepsilon_-\gamma :
\]
the two ideals are the two inequivalent five-dimensional Dirac representations of Fact \claimref{rule2.imported-gamma-matrices-odd-dimension}, $\Gamma^4 = \mp\,\Gamma^0\Gamma^1\Gamma^2\Gamma^3$, on the one Dirac spinor of $\Cl(1,3) \cong \Mat_2(\HH)$;
\item[(iii)] the reflection of the fifth direction, $R: e_4 \mapsto -e_4$ with $e_0, \ldots, e_3$ fixed, extends to the automorphism $\hat{\cdot} \circ \Ad_{e_4}$ of $A_5$, sends $\omega \mapsto -\omega$, exchanges the ideals, and is outer: the five-dimensional parity is the exchange that Fact \claimref{rule2.imported-classification-centre-type-c} says no inner automorphism can perform;
\item[(iv)] the Rule 2 repairs are $\Cl(2,4)$ ($\nu^2 = +1$) and $\Cl(1,5)$ ($\nu^2 = -1$), both $\cong \Mat_2(\Cl^0(1,4)) \cong \Mat_2(\Cl(1,3)) \cong \Mat_4(\HH)$, simple with centre $\R$, in which $\varepsilon_\pm$ are the diagonal matrix units;
\item[(v)] in either repair $\Ad_\nu$ restricts to the grade involution of $A_5$ and $\Ad_{\nu e_4}$ restricts to the parity $R$: the outer exchange has become inner, and it is a boost, $(\nu e_4)^2 = +1$, in $\Cl(2,4)$ and a rotation, $(\nu e_4)^2 = -1$, in $\Cl(1,5)$;
\item[(vi)] $\Cl(2,4)$ is the Rule 1 ascent of $\Cl(1,3)$, the conformal algebra of Minkowski space whose spinors carry the conformal spinor space $\CS$ (twistor space) (Fact \claimref{rule2.imported-completion-spacetime-algebra-spinors}): the pair $(\nu, e_4)$ is its hyperbolic plane and $f = \tfrac12(\nu + e_4)$, $f^* = \tfrac12(\nu - e_4)$ its ladder pair; $\Cl(1,5)$ is the same algebra at residue $4$ with a definite adjoined plane. The residues run $6 \to 5 \to 6$ or $6 \to 5 \to 4$.
\end{enumerate}

## technical
In $A_5 = \Cl(1,4)$ the volume element $\omega = \gamma e_4$, with $\gamma$ the spacetime pseudoscalar, is central with $\omega^2 = +1$, so $A_5 = \varepsilon_+A_5 \oplus \varepsilon_-A_5$ is of type C. Each ideal is a copy of $\Cl(1,3)$ through $a \mapsto \varepsilon_\pm a$, with $\varepsilon_\pm e_4 = \mp\varepsilon_\pm\gamma$, so the ideals are the two inequivalent five-dimensional Dirac representations $\Gamma^4 = \mp\Gamma^0\Gamma^1\Gamma^2\Gamma^3$ on the one Dirac spinor. The reflection $e_4 \mapsto -e_4$ is the automorphism $\hat{\cdot}\circ\mathrm{Ad}_{e_4}$; it exchanges the ideals and is outer.

The Rule 2 repairs are $\Cl(2,4)$, with $Q(\nu) = +1$, and $\Cl(1,5)$, with $Q(\nu) = -1$, both isomorphic to $\Mat_2(\Cl(1,3)) \cong \Mat_4(\HH)$ with $\varepsilon_\pm$ as diagonal matrix units. In either, conjugation by $\nu$ is the grade involution of $A_5$ and conjugation by $\nu e_4$ is the reflection, now inner: a boost in $\Cl(2,4)$, where $(\nu e_4)^2 = +1$, and a rotation in $\Cl(1,5)$, where $(\nu e_4)^2 = -1$. $\Cl(2,4)$ is the Rule 1 ascent of $\Cl(1,3)$, with $(\nu, e_4)$ its hyperbolic plane and $\tfrac12(\nu \pm e_4)$ its ladder pair; the residues run $6 \to 5 \to 6$ or $6 \to 5 \to 4$.

## lay
Adding a fifth dimension to spacetime, as in Kaluza-Klein theory, makes the geometric algebra split into two halves, which match the two inequivalent ways of writing a five-dimensional Dirac field. Reflecting the fifth direction swaps the halves, and nothing inside the algebra can perform that swap. Adding a sixth direction merges the halves and turns the reflection into an internal boost or rotation. With the sixth direction time-like, the merged algebra is the conformal algebra of spacetime, whose spinors are the four-dimensional spinors of conformal geometry.

## one-liner
$\Cl(1,4)$ is of type C with its two ideals the inequivalent five-dimensional Dirac representations, exchanged by the outer parity of the fifth direction, and its Rule 2 repairs $\Cl(2,4)$ and $\Cl(1,5)$, both $\Mat_4(\HH)$, make that parity inner, $\Cl(2,4)$ being the Rule 1 ascent of $\Cl(1,3)$.
