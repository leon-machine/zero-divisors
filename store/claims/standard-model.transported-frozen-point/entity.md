---
id: standard-model.transported-frozen-point
kind: claim
version: 6
title: The transported frozen point
status: proved
region: standard-model
subject: mass
tags: [frozen-point, transport-algorithm, null-directions]
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
- name: Claude Opus 5.5
  role: consistency pass, notation, Q(I) for the square of a vector in the proof
  version: 6
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - standard-model.imported-frozen-point-grip-thirteenth-refutation@6
  - transport.totality@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_mode_vectors
- kind: check
  ref: check.py::check_lift_and_its_rung_component
- kind: check
  ref: check.py::check_reciprocal_lift
- kind: check
  ref: check.py::check_third_rung_adds_minus_w5
- kind: check
  ref: check.py::check_normalisation_scaling_and_conjugate_directions
- kind: check
  ref: check.py::check_hypercharges_of_the_components
- kind: proof
  derivation: main
locators:
  paper: T12
  number: Prop 9.27
  label: prop:lift
  line: 1768
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 5 -> 6. In the proof the square of the vector I, written as the inner product of I with itself, is now Q(I) (house style); no change of content.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: lift, normalised reciprocal and third-rung lift of sampled frozen points with their rung components and norms, the normalisation and lambda^2 scaling, conjugate directions, and the hypercharges. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 4 -> 5.'
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - standard-model.imported-frozen-point-grip-thirteenth-refutation
    note: 'Added the frozen-point Fact, which supplies Q(I) = Lambda/3 used in every computation of the
      proof although context_refs did not list it; kept the transport totality edge. Levels pass: conditions
      already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.imported-frozen-point-grip-thirteenth-refutation
---

## formal
Carry $I$ into the two-rung completion by the constructions of Fact \claimref{transport.totality}, with $(\nO', \nInf')$ and $(\nO'', \nInf'')$ the null pairs of the second and third rungs and $v = \tfrac12\nInf$, $w = -\nO$ the corresponding mode vectors ($v \cdot w = \tfrac12$, $v^{*} = w$). Then:
\begin{enumerate}
\item[(i)] The lift $X(I) = \nO' + I + \tfrac{\Lambda}{6}\nInf'$ is null, and its second-rung component is $\nO' + \tfrac{\Lambda}{6}\nInf' = -w_{4} + \tfrac{\Lambda}{3}v_{4}$, of norm $-\Lambda/3$: a vector of the hypercharge $-\tfrac12$ doublet with an admixture of order $\Lambda$ of the conjugate.
\item[(ii)] The lift of the reciprocal, normalised to ground component $I$, is $\tfrac{\Lambda}{3}\nO' + I + \tfrac12\nInf'$, null, with second-rung component $\tfrac{\Lambda}{3}\nO' + \tfrac12\nInf' = v_{4} - \tfrac{\Lambda}{3}w_{4}$, of norm $-\Lambda/3$: the conjugate direction, hypercharge $+\tfrac12$; at $\Lambda = 0$ it is exactly $\tfrac12\nInf' = v_{4}$, the root paper's ideal point $x_{0} + \tfrac12\nInf$.
\item[(iii)] Lifting the null $X(I)$ to the third rung adds the component $\nO'' = -w_{5}$ and nothing else: the doubly lifted frozen point has rung components $(-w_{4} + \tfrac{\Lambda}{3}v_{4},\; -w_{5})$, the direction $(1,1)$ of the hypercharge $-\tfrac12$ doublet.
\end{enumerate}
The coefficient one of $-w_{4}$ in (i) and of $v_{4}$ in (ii) is the lift's normalisation, not a property of $I$: $X(x)$ carries $\nO'$ with coefficient one for every $x$, and the reciprocal's lift carries $\tfrac12\nInf'$ with coefficient one for every invertible $x$, so the $H_{d}$ direction is where every lift lands and the $H_{u}$ direction where every reciprocal's lift lands. What is specific to $I$ is the admixture of order $\Lambda$, and its size relative to the unit is not invariant: under $I \to \lambda I$ it scales as $\lambda^{2}$, and it is the normalisation $\sigma = 1$ of the scale slot that fixes $\lambda$. The two constructions land on conjugate null directions of the rung plane.

## technical
Carry the frozen point $I$ into the two-rung completion by the transport construction $X(x) = \nO' + x + \tfrac12 Q(x)\nInf'$, with mode vectors $v = \tfrac12\nInf$ and $w = -\nO$ for each rung. Since $Q(I) = \Lambda/3$, the lift $X(I) = \nO' + I + \tfrac{\Lambda}{6}\nInf'$ is null, with second-rung component $-w_{4} + \tfrac{\Lambda}{3}v_{4}$ of norm $-\Lambda/3$: a vector of the hypercharge $-\tfrac12$ doublet with an admixture of order $\Lambda$ of the conjugate. The reciprocal's lift, normalised to ground component $I$, has second-rung component $v_{4} - \tfrac{\Lambda}{3}w_{4}$, the conjugate direction with hypercharge $+\tfrac12$, and equals $v_{4}$ at $\Lambda = 0$. Lifting $X(I)$ to the third rung adds only $-w_{5}$.

The unit coefficients are the lift's normalisation, so every lift lands in the $H_{d}$ direction and every reciprocal's lift in the $H_{u}$ direction. What is specific to $I$ is the admixture of order $\Lambda$, whose relative size scales as $\lambda^{2}$ under $I \to \lambda I$ and is fixed by the normalisation $\sigma = 1$ of the scale slot.

## lay
The frozen point, the series' reference point for mass, can be carried up into a larger structure by the same construction that founds the series. When it is, it picks up new components pointing in the directions that carry the Higgs doublet's charges, plus a small piece proportional to the cosmological constant. The main components come from the construction itself, not from the frozen point; only the small piece is specific to it.

## one-liner
Transporting the frozen point into the two-rung completion gives null vectors whose rung components lie along conjugate doublet directions, with only the admixture of order $\Lambda$ specific to the frozen point.
