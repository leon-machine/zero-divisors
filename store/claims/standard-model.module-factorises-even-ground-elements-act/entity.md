---
id: standard-model.module-factorises-even-ground-elements-act
kind: claim
version: 5
title: The module factorises, and even ground elements act on the pair factor
status: proved
region: standard-model
subject: standard-model
tags: [spinor-modules, ladder-pairs]
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
  - standard-model.imported-cauchy-decomposition-exterior-power@1
  - standard-model.imported-tower-commuting-copies-fock-module@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_module_irreducible_and_factorised
- kind: check
  ref: check.py::check_even_ground_elements_act_on_pairs_only
- kind: check
  ref: check.py::check_rung_vectors_twisted_and_commuting
locators:
  paper: T12
  number: Prop 9.9
  label: prop:factor
  line: 1569
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: irreducibility of the five CAR pairs, the block forms X_W (x) 1 and (-1)^N_W (x) y_R, and the commutation of so(V_C) with the rung algebra. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 4 -> 5.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Formal level and proof have no twistor language; only the lay level''s ''twistor part'' was reworded as the pair part. V_C, Cl^0(V_C) and the complexified two-rung algebra are kept: their complex unit must commute with vectors, which I6 does not.'
  source_title: |-
    The module factorises, and even ground elements act on the pair factor
  source_formal: |-
    $\Lambda^{\bullet}(W \oplus R_{2}) = \Lambda^{\bullet}W \otimes \Lambda^{\bullet}R_{2}$ as a module over the complexified two-rung algebra $T_{2} \otimes \C \cong \mathrm{M}_{32}(\C)$, irreducibly, and with the pair modes ordered before the rung modes:
    \begin{enumerate}
    \item[(1)] every vector of $V_{\C}$ acts as $x_{W} \otimes 1$, every product of two vectors of $V_{\C}$ as $X_{W} \otimes 1$, and hence every element of the even ground subalgebra $\Cl^{0}(V_{\C})$, in particular every generator of $\so(2,4)$, as an operator on $\Lambda^{\bullet}W$ tensored with the identity on $\Lambda^{\bullet}R_{2}$;
    \item[(2)] every vector of the rung plane acts as $\gamma \otimes y_{R}$ with $\gamma = (-1)^{N_{W}}$ the pair-number grading, so that vectors of $V_{\C}$ and of the rung plane anticommute, while products of two rung vectors act as $1 \otimes Y_{R}$;
    \item[(3)] consequently $\so(V_{\C})$ and $\so(R_{2} \oplus \overline{R}_{2})$ commute elementwise inside $\so(V_{\C} \oplus R_{2} \oplus \overline{R}_{2})$, and every element of $\so(V_{\C})$ commutes with the rung number $N_{R}$ and with the rung mixing $\uu(2) = \operatorname{span}\{v_{a}w_{b}\}_{a, b \in \{4, 5\}}$.
    \end{enumerate}
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - standard-model.imported-cauchy-decomposition-exterior-power
    note: Added the imported Cauchy fact because the proof uses its direct-sum formula for exterior algebras
      (cited there to the same Fulton-Harris locator); kept the tower Fock-module fact.
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.imported-cauchy-decomposition-exterior-power
---

## formal
$\Lambda^{\bullet}(W \oplus R_{2}) = \Lambda^{\bullet}W \otimes \Lambda^{\bullet}R_{2}$ as a module over the complexified two-rung algebra $T_{2} \otimes \C \cong \mathrm{M}_{32}(\C)$, irreducibly, and with the pair modes ordered before the rung modes:
\begin{enumerate}
\item[(1)] every vector of $V_{\C}$ acts as $x_{W} \otimes 1$, every product of two vectors of $V_{\C}$ as $X_{W} \otimes 1$, and hence every element of the even ground subalgebra $\Cl^{0}(V_{\C})$, in particular every generator of $\so(2,4)$, as an operator on $\Lambda^{\bullet}W$ tensored with the identity on $\Lambda^{\bullet}R_{2}$;
\item[(2)] every vector of the rung plane acts as $\gamma \otimes y_{R}$ with $\gamma = (-1)^{N_{W}}$ the pair-number grading, so that vectors of $V_{\C}$ and of the rung plane anticommute, while products of two rung vectors act as $1 \otimes Y_{R}$;
\item[(3)] consequently $\so(V_{\C})$ and $\so(R_{2} \oplus \overline{R}_{2})$ commute elementwise inside $\so(V_{\C} \oplus R_{2} \oplus \overline{R}_{2})$, and every element of $\so(V_{\C})$ commutes with the rung number $N_{R}$ and with the rung mixing $\uu(2) = \operatorname{span}\{v_{a}w_{b}\}_{a, b \in \{4, 5\}}$.
\end{enumerate}

## technical
The five-mode Fock module $\Lambda^{\bullet}(W \oplus R_{2}) = \Lambda^{\bullet}W \otimes \Lambda^{\bullet}R_{2}$ is the irreducible module of the complexified two-rung algebra $T_{2} \otimes \C \cong \mathrm{M}_{32}(\C)$. With the pair modes ordered before the rung modes, every vector of $V_{\C}$ acts as $x_{W} \otimes 1$, so every element of the even ground subalgebra, including every generator of $\so(2,4)$, acts on $\Lambda^{\bullet}W$ alone.

A rung vector acts as $(-1)^{N_{W}} \otimes y_{R}$, so ground and rung vectors anticommute while products of two rung vectors act as $1 \otimes Y_{R}$. Consequently $\so(V_{\C})$ and $\so(R_{2} \oplus \overline{R}_{2})$ commute elementwise, and $\so(V_{\C})$ commutes with the rung number $N_{R}$ and with the rung mixing $\uu(2)$.

## lay
The paper's state space for a composite is built from five modes: three from the internal pairs of the original conformal spinor and two added by later steps of the transport construction. This result shows that the space splits cleanly into a pair part and a rung part. The original conformal symmetries act on the pair part only, and the symmetries of the added rungs act on the rung part only, so the two sets of symmetries never interfere.

## one-liner
The two-rung Fock module factorises as $\Lambda^{\bullet}W \otimes \Lambda^{\bullet}R_{2}$, with the even ground algebra acting on the first factor only and commuting with the rung symmetries.
