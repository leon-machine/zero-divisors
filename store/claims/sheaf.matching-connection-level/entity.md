---
id: sheaf.matching-connection-level
kind: claim
version: 8
title: The matching at connection level
status: proved
region: sheaf
subject: interior
tags: [schwarzschild, kasner, limits]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
- name: Claude Opus 5.5
  role: 'consistency pass, citations of the weighted-limit Fact corrected'
  version: 8
  source: maintainer pass 2026-11-07 (consistency)
review: typed
about:
- obj.interior.weighted-blow-up-hubble-normalisation-admissible
- obj.sheaf.weighted-coframe-module
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - sheaf.matching-fibre@5
  - sheaf.schwarzschild-degeneration-boundary-tame@6
  - sheaf.weighted-limit@6
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_adapted_coframe_is_exceptional
- kind: check
  ref: check.py::check_rates_by_exact_series
- kind: check
  ref: check.py::check_matching_values_generate_so13
locators:
  paper: T04
  number: Thm 8.27
  label: thm:connweld
  line: 1143
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Formal clauses (preamble, (2), (3)) and the proof cited the adapted coframe, the rate series, the weighted-limit connection and its holonomy clause as Fact obj.interior.weighted-blow-up-hubble-normalisation-admissible, which is a Definition holding none of them; they are the Fact sheaf.weighted-limit (already in uses); wording only.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: frames from the PG gauge field cometric: the rationalised identities, orthonormality and the boost to the rain frame; rates by exact series and the trace rule; B_w unit and the values generate so(1,3). Version 5 -> 6. check_adapted_coframe_is_exceptional: wall coincidence computed from the boost formula at r = 0 with an approach bound, replacing a literal comparison (fix round 2026-10-23). Version 6 -> 7.'
  typing:
    by: ai-typing-pass
    note: 'Repair edge to the weighted-limit fact reviewed and kept: the statement''s references to the
      weighted limit (extracted as the definition) are to this fact, whose display and fullness argument
      the proof uses. Levels pass: the lay now restricts the statement to the Schwarzschild interior.'
  env: theorem
  repair:
    added:
    - sheaf.weighted-limit
    note: premise newly extracted after the typing pass (fact previously merged into a definition); not
      yet reviewed
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - sheaf.weighted-limit
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the adapted orthonormal coframe is the physical-vector map hb^{-1} of the Schwarzschild interior gravitational field in an adapted orthonormal frame; the static-to-rain boost is a rotation-gauge transformation; the connection is the rotation-gauge field. Identities, rates and matching unchanged. Proof: one opening sentence pointing to the GTG dictionary Fact. Fix (Leon 2026-10-23, referee GR1): displayed connection values re-signed to the GTG sign of the definition, D_a = a.nabla + Omega(a) x (Cartan forms omega^i_0 = sigma_i theta^i assemble to -sigma_i B_i; Hubble-normalised Kasner model -sum_i p_i B_i, DICTIONARY C10); content unchanged.'
---

## formal
For the Schwarzschild interior gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), write $(d\tau, \theta^1, \theta^2, \theta^3)$ for the adapted orthonormal coframe of Fact \claimref{sheaf.weighted-limit} (synchronous time, normalised Killing direction, sphere directions): the components $\theta^a(v) = \gamma^a \cdot \hb^{-1}(v)$ of the physical-vector map in the adapted orthonormal frame. Then:
\begin{enumerate}
\item \emph{(Frames.)} The adapted coframe consists of exceptional-module sections, exactly: $\sqrt{m^2 - r}\;d\tau = \rho$ and
\[
\sqrt{m^2 - r}\;\theta^1 \;=\; -\sqrt r\,\dtPG \,+\, m\,(k/\sqrt r),
\]
with $\theta^2 = \mu_1$, $\theta^3 = \mu_2$ exactly (the first identity uses the transition of Theorem \claimref{sheaf.schwarzschild-degeneration-boundary-tame}(4)). The static and rain frames of $\shW_{\mathrm{exc}}$ are related by the rotation-gauge boost of rapidity $\chi$ with $(\sinh\chi, \cosh\chi) = (-\sqrt r, m)/\sqrt{m^2-r}$, unit-normalised exactly and vanishing on the exceptional boundary: the two frames coincide at the wall, future orientations matched.
\item \emph{(Rates.)} In this common frame the Hubble-normalised rotation-gauge field is $-\sum_i (\tau\sigma_i)B_i \otimes \hat\theta^i$ (in the sign of the Definition) plus a sphere term of normalised size $\tau/r = \tfrac23\sqrt r + O(r^{3/2}) \to 0$, with the exact series of Fact \claimref{sheaf.weighted-limit} re-derived here independently by exact power series in $\sqrt r$, agreeing coefficient by coefficient, and the trace rule $\tau(\sigma_1 + 2\sigma_2) \to 1$ realising the first Kasner relation as a rate statement.
\item \emph{(The matching.)} Consequently the weighted-limit connection of Fact \claimref{sheaf.weighted-limit} is a connection datum on the exceptional bundle of this section: its boundary value is minus the weight one-form of the exceptional coframe, $-\sum_i p_i B_i \otimes \hat\nu^i$, its total element is $-B_w$, minus the unit boost $B_w$ of Proposition \claimref{sheaf.matching-fibre}, and its values, nonzero multiples of the three boosts, generate the full bivector algebra, so the holonomy theorem of \cite{ButlerT6} is the statement that the boundary holonomy of the exceptional bundle, in the values-level sense of \cite[Def.~5.5]{ButlerT6}, is all of $\mathfrak{so}(1,3)$; the matching uses exactly those values. The two black-hole routes are one structure: the weighted limit transports the exceptional fibre, the completion Clifford-multiplies it, and the ladder boost is the transverse $\mathfrak{so}(1,1)$.
\end{enumerate}

## technical
For the Schwarzschild interior gravitational field on flat spacetime, the adapted orthonormal coframe $(d\tau, \theta^1, \theta^2, \theta^3)$, the components of the physical-vector map $\hb^{-1}$ in an adapted frame, consists exactly of exceptional-module sections: $\sqrt{m^2 - r}\,d\tau = \rho$, $\sqrt{m^2 - r}\,\theta^1 = -\sqrt r\,\dtPG + m(k/\sqrt r)$, and $\theta^2 = \mu_1$, $\theta^3 = \mu_2$. The static and rain frames are related by a boost of rapidity $\chi$ with $(\sinh\chi, \cosh\chi) = (-\sqrt r, m)/\sqrt{m^2 - r}$, which vanishes on the exceptional boundary, so the two frames coincide at the wall. In this frame the Hubble-normalised connection is $-\sum_i (\tau\sigma_i)B_i \otimes \hat\theta^i$ plus a sphere term of size $\tau/r \to 0$, the rate series being re-derived independently, and the trace rule $\tau(\sigma_1 + 2\sigma_2) \to 1$ realises the first Kasner relation as a rate statement.

Consequently the weighted-limit connection is a connection datum on the exceptional bundle: its boundary value is minus the weight one-form, $-\sum_i p_i B_i \otimes \hat\nu^i$, its total element is $-B_w$, minus the unit boost $B_w$, and its values generate the full $\mathfrak{so}(1,3)$, so the values-level boundary holonomy of the exceptional bundle is all of $\mathfrak{so}(1,3)$. The weighted limit transports the exceptional fibre, the completion Clifford-multiplies it, and the ladder boost is the transverse $\mathfrak{so}(1,1)$.

## lay
The series has two separate descriptions of the centre of a non-rotating (Schwarzschild) black hole: one from the gravitational field, as a limit of the rules for carrying directions, and one from its algebraic completion. This result shows that they fit together exactly. The natural directions of the field picture are exactly building blocks of the algebraic one, and the limiting rules of the field picture become a structure on the algebraic one, so the two routes describe a single object.

## one-liner
The adapted coframe of the Schwarzschild interior consists exactly of exceptional-module sections, and the weighted-limit connection becomes a connection datum on the exceptional bundle, with boundary value minus the weight one-form and total element $-B_w$, minus the unit boost $B_w$.
