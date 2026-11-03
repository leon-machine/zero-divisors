---
id: standard-model.one-number-explain
kind: claim
version: 4
title: One number to explain
status: conjectured
region: standard-model
subject: dark-energy
tags:
- refutation
- the-number-n
- cosmological-constant
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
lineage:
  motivated_by:
  - dark-energy.frozen-point-makes-stelle-west-vector
  - standard-model.imported-frozen-point-dictionary
locators:
  paper: T12
  number: Obs 7.1
  label: obs:N
  line: 1237
extraction:
  maintainer_pass_refines:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Cites synthesis.smallness-monomials-exact-hierarchy-casimir for the exact Casimir monomial of the hierarchy entry (the schema has no refines link).'
  maintainer_pass_2026_10_22:
    by: ai-maintainer-pass
    note: 'A5 largeness follow-up: N = M_P/H is about 1.0e61 (1.03e61), not of order 1e60; formal and
      lay corrected.'
  source_formal: 'The gravitational action of the action paper carries, in its curvature-squared presentation,
    a single dimensionless combination of scales, $G\Lambda$, the relative coefficient of its Einstein-Hilbert
    and Gauss-Bonnet terms (\cite[Thm.~3.1(2)]{ButlerT10}; reading that coefficient as \emph{the} dimensionless
    coupling is this paper''s, not the action paper''s). Let $N = M_{P}/H$, the number the dictionary
    of Fact \claimref{standard-model.imported-frozen-point-dictionary} attaches to the Planck mass, of
    order $10^{60}$. Then, as an exact exponent computation, the framework''s well-known smallness problems
    are all powers of $N$: the cosmological-constant problem is $G\Lambda = 3N^{-2}$; the weakness of
    gravity relative to a dimension-one matter coupling, evaluated at the Hubble scale, is $N^{-2}$; and
    the mass hierarchy is the statement that the imaginary weight of a mass $m$ is $\operatorname{Im}
    w = (m/M_{P})\,N$. The numerical layer of the programme therefore reduces to a single question: why
    is $N$ large? That question this framework does not answer; what it has done is ensure there is only
    one of it. The computation is exact and script-checked; the choice of $H$ as the comparison scale
    for gravity''s weakness, and the reading of the three problems as one, are conventions, which is why
    this is an Observation.'
  env: observation
  context_refs:
  - dark-energy.frozen-point-makes-stelle-west-vector
  - standard-model.imported-frozen-point-dictionary
  typing:
    by: ai-typing-pass
    note: Left as conjectured although the exponent computation is exact, because the paper itself keeps
      it an Observation on account of its conventions and its reading of three problems as one.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants: []
    added_about: []
    verdict: standalone
    note: Conjectured observation with lineage; it refutes the Dirac-coincidence row and is cited in the
      statement of what-derived-what-not as context, not as a premise.
  correction:
    by: ai-correction
    date: '2026-10-22'
    note: 'Adds the limit of the one-number reading, from the store''s own results: G Lambda = 3 N^-2
      and (H/M_P)^2 = N^-2 are one number by definition; Im w = (m/M_P) N carries m/M_P, which for the
      weak scale is v/M_P = 2.0165e-17 with N^-0.28 < v/M_P < N^-0.27 (exact interval arithmetic, v =
      246.22 GeV, N = 1.026e61), and which families.why-kinematic-attacks-had-fail (T13 Prop 7.5) shows
      is kinematically not a function of N at the level of its invariance premise. This is the refuter
      of refutation 10, whose corrected statement ("one number appearing in every smallness problem")
      therefore holds for two of the three problems only.'
  open_problem: op.t12-n-after-the-count
---

## formal
The gravitational action of the action paper carries, in its curvature-squared presentation, a single dimensionless combination of scales, $G\Lambda$, the relative coefficient of its Einstein-Hilbert and Gauss-Bonnet terms (\cite[Thm.~3.1(2)]{ButlerT10}; reading that coefficient as \emph{the} dimensionless coupling is this paper's, not the action paper's). Let $N = M_{P}/H$, the number the dictionary of Fact \claimref{standard-model.imported-frozen-point-dictionary} attaches to the Planck mass, about $1.0 \times 10^{61}$. Then, as an exact exponent computation, the framework's well-known smallness problems are all powers of $N$: the cosmological-constant problem is $G\Lambda = 3N^{-2}$; the weakness of gravity relative to a dimension-one matter coupling, evaluated at the Hubble scale, is $N^{-2}$; and the mass hierarchy is the statement that the imaginary weight of a mass $m$ is $\operatorname{Im} w = (m/M_{P})\,N$. The numerical layer of the programme therefore reduces to a single question: why is $N$ large? That question this framework does not answer; what it has done is ensure there is only one of it. The computation is exact and script-checked; the choice of $H$ as the comparison scale for gravity's weakness, and the reading of the three problems as one, are conventions, which is why this is an Observation. The reading has a limit the computation shows. The first two problems are one number by the definition of $N$: both are $(H/M_{P})^{2}$, the first times $3$. The third is not a power of $N$, and not exact as written: $\operatorname{Im} w = (m/M_{P})\,N$ holds to relative order $H^{2}/m^{2}$ for $m > 3H/2$ (exactly, the weight's Casimir is $-w(w+3) = (m/M_{P})^{2}N^{2}$, Proposition \claimref{synthesis.smallness-monomials-exact-hierarchy-casimir}), and it carries a second ratio, $m/M_{P}$, which for the weak scale is the rung unit $v/M_{P} \approx 2.0 \times 10^{-17}$, between $N^{-0.28}$ and $N^{-0.27}$; it is invariant under the rescaling of Proposition \claimref{standard-model.trichotomy-what-kind-number}(1) and so kinematically not a function of $N$ (Proposition \claimref{families.why-kinematic-attacks-had-fail}, at the level of its observation-level invariance premise). One number is to be explained for the cosmological-constant problem and gravity's weakness; the mass hierarchy adds the second continuous modulus that Proposition \claimref{standard-model.trichotomy-what-kind-number}(1) lists beside $N$, the weight spectrum.

## technical
The curvature-squared presentation of the gravitational action carries one dimensionless combination of scales, $G\Lambda$, the relative coefficient of its Einstein-Hilbert and Gauss-Bonnet terms; reading it as the dimensionless coupling is this paper's convention. With $N = M_{P}/H$ and $H^{2} = \Lambda/3$, an exact exponent computation gives $G\Lambda = 3N^{-2}$, the weakness of gravity against a dimension-one coupling at the Hubble scale as $N^{-2}$, and the imaginary weight of a mass $m$ as $\operatorname{Im} w = (m/M_{P})\,N$.

The paper reads the three problems as one question, why $N$ is large, which the framework does not answer. The computation is exact; the choice of $H$ as the comparison scale and the reading of the three problems as one are conventions, which is why this is an observation. The first two problems are the same number by the definition of $N$. The third carries a second ratio: $\operatorname{Im} w = N\,(m/M_{P})$ (to relative order $H^{2}/m^{2}$; exactly $-w(w+3) = (m/M_{P})^{2}N^{2}$), and for the weak scale $v/M_{P} \approx 2.0 \times 10^{-17}$ is, granting as Proposition \claimref{families.why-kinematic-attacks-had-fail} does that $m/M_{P}$ is invariant under the rescaling, a second modulus kinematically not a function of $N$, so the hierarchy needs $N$ and that second number.

## lay
Physics has several puzzles about why certain numbers are so extremely small, such as the tiny cosmological constant and the weakness of gravity. In this framework the cosmological constant and the weakness of gravity both turn out to be the same power of one number, about $10^{61}$, the ratio of the Planck mass to the expansion rate of the universe. The hierarchy of particle masses involves that number too, but also a second one, the weak scale measured against the Planck mass, which the framework does not tie to the first. The framework does not say why the first number is so large.

## one-liner
The cosmological-constant problem and the weakness of gravity are both $N^{-2}$ (up to $3$), with $N = M_{P}/H$, and the mass hierarchy enters as $\operatorname{Im} w = (m/M_{P})N$, which carries the second, rescaling-invariant ratio $m/M_{P}$; the numerical layer reduces to why $N$ is large and what fixes $v/M_{P}$.
