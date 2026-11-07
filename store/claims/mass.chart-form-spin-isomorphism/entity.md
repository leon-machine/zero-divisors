---
id: mass.chart-form-spin-isomorphism
kind: claim
version: 6
title: "The chart form of the spin isomorphism"
status: proved
region: mass
subject: conformal-spacetime
tags: [conformal-spinors, rotors-and-stabilisers]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
- name: Claude Opus 5.5
  role: GA rewrite (matrices as linear maps on the chart frame)
  version: 6
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - mass.imported-flat-model-twistor-chart-infinity@7
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T11.py
  tags:
  - label:lem:chartiso
- kind: check
  ref: check.py::check_grading_element
- kind: check
  ref: check.py::check_translations_block
- kind: check
  ref: check.py::check_special_conformal_block
locators:
  paper: T11
  number: Lem 5.3
  label: lem:chartiso
  line: 634
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 5 -> 6. The three block matrices are written as the linear maps they are on the chart frame (the grading element as -1/2 on S- and +1/2 on S+, the translations as b_x: S+ -> S-, the special conformal generators as c_x: S- -> S+), acting on Lambda^2 S as derivations of the outer product; the block matrices stay as a labelled reading. Pure notation: each map is the displayed matrix read column by column, so no equivalence needed computing. The spinor components x^{aa''} and epsilon_{ab} stay (components, which the conventions allow). Found in passing: the front matter carries two source_formal keys, the first empty.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the traceless spin preimages of n_inf ^ n0, x ^ n_inf, x ^ n0 solved exactly and compared with the displayed grading, b_x and c_x blocks built from the formulas. Version 4 -> 5.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: lemma
  unresolved_refs:
  - rem:nullity
  typing:
    by: ai-typing-pass
    added:
    - mass.imported-flat-model-twistor-chart-infinity
    note: 'The proof starts from the spin isomorphism and the chart normalisation recorded in the flat-model fact, so that fact was added as the premise; the remark on nullity it also cites is not in the store.'
  source_title: "The chart form of the spin isomorphism"
  source_formal: |-
    For $x = x^{aa'}e_{a}\wedge e_{a'}$ in the $x$-slot:
    \begin{enumerate}
    \item $A(n_{\infty}\wedge n_{0}) = \operatorname{diag}(-\tfrac12, -\tfrac12, \tfrac12, \tfrac12)$, the grading element;
    \item $A(x \wedge n_{\infty}) = \begin{pmatrix} 0 & b_{x} \\ 0 & 0 \end{pmatrix}$ with $b_{x}: \Sc' \to \Sc$, $(b_{x}\pi)^{a} = x^{aa'}\varepsilon_{a'b'}\pi^{b'}$: the translations;
    \item $A(x \wedge n_{0}) = \begin{pmatrix} 0 & 0 \\ c_{x} & 0 \end{pmatrix}$ with $c_{x}: \Sc \to \Sc'$, $(c_{x}\omega)^{a'} = -x^{ba'}\varepsilon_{ba}\omega^{a}$: the special conformal generators.
    \end{enumerate}
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Wrote the chart halves as $\\Som$, $\\Spi$ (they were $\\Sc$, $\\Sc'$) in all levels and the proof, and converted the plain levels' twistor wording; the computation is unchanged."
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - mass.imported-flat-model-twistor-chart-infinity
---

## formal
Let $A(U)$ be the traceless linear map of $\CS = \Som \oplus \Spi$ (frame $e_{1}, e_{2}$ of $\Som$ and $e_{3}, e_{4}$ of $\Spi$) that acts on $\Lambda^{2}\CS$ as the derivation $A\cdot(u \wedge v) = Au \wedge v + u \wedge Av$ of the outer product by which $U$ acts. For $x = x^{aa'}e_{a}\wedge e_{a'}$ in the $x$-slot:
\begin{enumerate}
\item $A(n_{\infty}\wedge n_{0})$: $e_{a} \mapsto -\tfrac12 e_{a}$, $e_{a'} \mapsto \tfrac12 e_{a'}$, the grading element;
\item $A(x \wedge n_{\infty})$ is zero on $\Som$ and is $b_{x}: \Spi \to \Som$, $b_{x}(e_{b'}) = x^{aa'}\varepsilon_{a'b'}e_{a}$, that is $(b_{x}\pi)^{a} = x^{aa'}\varepsilon_{a'b'}\pi^{b'}$: the translations;
\item $A(x \wedge n_{0})$ is zero on $\Spi$ and is $c_{x}: \Som \to \Spi$, $c_{x}(e_{a}) = -x^{ba'}\varepsilon_{ba}e_{a'}$, that is $(c_{x}\omega)^{a'} = -x^{ba'}\varepsilon_{ba}\omega^{a}$: the special conformal generators.
\end{enumerate}
(As matrices in the frame $(e_{1}, \dots, e_{4})$, a labelled reading: $\operatorname{diag}(-\tfrac12, -\tfrac12, \tfrac12, \tfrac12)$, $\begin{psmallmatrix} 0 & b_{x} \\ 0 & 0 \end{psmallmatrix}$ and $\begin{psmallmatrix} 0 & 0 \\ c_{x} & 0 \end{psmallmatrix}$.)

## technical
Write $\CS = \Som \oplus \Spi$ with $n_\infty = e_1 \wedge e_2$, $n_0 = e_3 \wedge e_4$, and the $x$-slot spanned by the mixed bivectors $e_a \wedge e_{a'}$. Under the isomorphism $\mathfrak{sl}(\CS) \to \so(\Lambda^2\CS, \varepsilon)$, the bivector $n_\infty \wedge n_0$ corresponds to the grading element, $-\tfrac12$ on $\Som$ and $+\tfrac12$ on $\Spi$ (the matrix $\operatorname{diag}(-\tfrac12, -\tfrac12, \tfrac12, \tfrac12)$ in the chart frame).

The translations $x \wedge n_\infty$ correspond to the map $b_x : \Spi \to \Som$ (zero on $\Som$), $(b_x\pi)^a = x^{aa'}\varepsilon_{a'b'}\pi^{b'}$, and the special conformal generators $x \wedge n_0$ to the map $c_x : \Som \to \Spi$ (zero on $\Spi$), $(c_x\omega)^{a'} = -x^{ba'}\varepsilon_{ba}\omega^a$. The proof checks on each basis bivector that the displayed map, acting as a derivation of the outer product, acts as the named rotation.

## lay
The conformal symmetries of spacetime can be written either as rotations of a six-dimensional space or as linear maps of the four-component spinors of the conformal algebra. This lemma writes that translation out explicitly in the chart used for spacetime points. Dilations become a scaling of the two spinor halves in opposite senses, translations a map from one half into the other, and special conformal transformations a map back.

## one-liner
In the conformal spinor chart, the dilation, the translations and the special conformal generators correspond to the grading element and to the maps $b_x: \Spi \to \Som$ and $c_x: \Som \to \Spi$ between the chiral halves.
