---
id: transport.rule-2-ideal-fusion-sharp-form
kind: claim
version: 4
title: 'Rule 2: ideal fusion, sharp form'
status: proved
region: transport
subject: completion
tags: [transport-algorithm, obstruction-types, idempotents]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
review: typed
about:
- obj.transport.obstruction-types
derivations:
- name: main
  uses:
  - transport.ascent-renders-grade-involution-inner@3
  - transport.centre@4
  - transport.classification-real-clifford-algebras@3
  - transport.corner-even-subalgebra@4
  - transport.matrix-units-peirce-isomorphism@3
  - std-algebra.morita-amplification@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_matrix_units_and_corner
- kind: check
  ref: check.py::check_fused_algebra_simple_centre_r
- kind: check
  ref: check.py::check_eps_exchanged_by_ad_nu
- kind: check
  ref: check.py::check_two_ascents_isomorphic_fixing_corner
locators:
  paper: T01
  number: Thm 5.5
  label: thm:fusion
  line: 1204
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.morita-amplification where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: matrix units and corner giving Mat_2(Cl^0), centre R, eps exchanged by Ad_nu, and the two ascents isomorphic fixing the corner. Version 2 -> 3.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'Kept all five premises, each used in the proof; the existing pins to the centre lemma and the classification are at version 1 although both are now at version 2, and were left as extracted.'
---

## formal
Let $p - q \equiv 1 \pmod 4$ and $\gamma = \pm 1$. Then
\[
B_\gamma \;=\; \Cl(p{+}1,q) \ \text{or}\ \Cl(p,q{+}1) \;\cong\; \Mat_2\bigl(\Cl^0(p,q)\bigr),
\]
by the matrix units of Lemma \claimref{transport.matrix-units-peirce-isomorphism} and the corner identification of Lemma \claimref{transport.corner-even-subalgebra}. Consequently:
\begin{enumerate}
\item $B_\gamma$ is simple, and its centre is $\R$: the fusion does not reintroduce a central splitting, and $B_\gamma$ carries no type-C obstruction.
\item The images of $\varepsilon_\pm$ in $B_\gamma$ are a conjugate pair of non-central idempotents, the diagonal matrix units of the fused algebra, exchanged by the inner automorphism $\mathrm{Ad}_\nu$, which restricts on $A$ to the grade involution (Proposition \claimref{transport.ascent-renders-grade-involution-inner}).
\item The two ascents are isomorphic as algebras: $\Cl(p{+}1,q) \cong \Cl(p,q{+}1)$, both canonically $\Mat_2(\Cl^0(p,q))$, with an isomorphism through the matrix units that fixes the corner.
\end{enumerate}

## technical
For $p - q \equiv 1 \pmod 4$ and an adjoined generator $\nu$ with $Q(\nu) = \gamma = \pm 1$, the one-generator ascent $B_\gamma = \Cl(p{+}1,q)$ or $\Cl(p,q{+}1)$ is isomorphic to $\Mat_2(\Cl^0(p,q))$, through the matrix units built from $\varepsilon_\pm$ and $\nu$ and the identification of the corner with the even subalgebra. Consequently $B_\gamma$ is simple with centre $\R$: the fusion reintroduces no central splitting and carries no type-C obstruction.

The images of $\varepsilon_\pm$ are a conjugate pair of non-central idempotents, the diagonal matrix units, exchanged by the inner automorphism $\mathrm{Ad}_\nu$, which restricts on $A$ to the grade involution. The two ascents are isomorphic as algebras, $\Cl(p{+}1,q) \cong \Cl(p,q{+}1)$, both canonically $\Mat_2(\Cl^0(p,q))$, by an isomorphism through the matrix units that fixes the corner.

## lay
Some Clifford algebras split into two independent halves. Adding one new direction, of either sign, fuses the halves into a single algebra of two-by-two matrices whose entries come from the algebra's even part. The fused algebra has no split of its own, and the two choices of sign give the same algebra.

## one-liner
For $p - q \equiv 1 \pmod 4$, adjoining one generator $\nu$ with $Q(\nu) = \pm 1$ gives the simple algebra $\Mat_2(\Cl^0(p,q))$ with centre $\R$, the same for either sign.
