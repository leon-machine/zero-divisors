---
id: standard-model.trichotomy-what-kind-number
kind: claim
version: 10
title: 'The trichotomy: what kind of number $N$ is'
status: proved
region: standard-model
subject: dark-energy
tags: [needs-continuum]
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
  - standard-model.four-dimensions-forces-converse@4
  - standard-model.gauge-algebra-minimal-massive-composite@4
  - standard-model.global-form-quotient-determined@3
  - standard-model.hypercharge-global-form-pair-counting-consistency@5
  - standard-model.imported-frozen-point-dictionary@7
  - standard-model.imported-norm-frozen-point-not-field@5
  - standard-model.pair-count-dimension@3
  - standard-model.quarks-leptons-two-level-fermion-content@5
  - standard-model.weak-angle-over-derived-generation@5
  - dark-energy.imported-henneaux-teitelboim-promotion@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12.py
  tags:
  - label:prop:trichotomy
- kind: check
  ref: check.py::check_rescaling_kinematics
- kind: check
  ref: check.py::check_n_varies_across_lambda
- kind: check
  ref: check.py::check_units_statement_numbers
locators:
  paper: T12
  number: Prop 7.6
  label: prop:trichotomy
  line: 1259
extraction:
  maintainer_pass_weak_scale:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 10: a marked note fixes the Hubble unit of v/H (H^2 = Lambda/3, that is H_0 sqrt(Omega_Lambda), against H_0; a factor of order one, about 0.2 in ln(v/H)), and records that the numbers for N use H^2 = Lambda/3. The register decision of 2026-10-23 recorded in an earlier note (v/H kept as the law) was restated on 2026-11-01: the D-term level xi G, and so v/M_P, is the law and v/H initial data (synthesis.rung-unit-second-free-number version 3); no clause here depends on which. Nothing else is changed.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: H -> sH and N -> N/s under Lambda -> s^2 Lambda on the chart frozen point with the dilation rotor, d(N^2)/dLambda = -3/Lambda^2, and the units-statement numbers (about 4.8e122 qubits, log2 about 407, R about 405) with certified bounds on pi and ln 2. Version 6 -> 7. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 7 -> 8. Check strengthened: pi and ln 2 brackets pinned to their known digits by truncation, and the base-two exponents written as floor(log2 C) = 407, floor(log2 N^2) = 405 at both bracket ends; quoted C range moved to module level. Version 8 -> 9.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'The Henneaux-Teitelboim promotion was adopted on 2026-10-23 (v/H kept as the law), so N is initial data under the promoted action (programme.n-parameter-of-the-laws version 3); where this text treats the promotion as an open decision, read it as adopted. Version 5 -> 6.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: proposition
  context_refs:
  - dark-energy.frozen-point-makes-stelle-west-vector
  - dark-energy.under-action-written-norm-parameter-laws
  - standard-model.dating-descent
  outside_pilot_cites:
  - ButlerT10
  typing:
    by: ai-typing-pass
    note: 'Kept all nine uses (the invariants the kinematic clause inspects and the two imported Facts);
      did not add the dark-energy parameter-of-the-laws proposition behind clause (4) because it itself
      uses this claim (its not-kinematic clause imports clause (1)), so the edge would close a cycle,
      and did not add the dating observation because clause (3) is stated as conditional on it. Levels
      pass: lay and one-liner no longer present not-kinematic as proved (only the rescaling invariance
      is proved; the rest is an observation-level reading), and technical adds that reading.'
  source_title: 'The trichotomy: what kind of number $N$ is'
  source_formal: 'The question the paper ends by pointing at can itself be classified. The classification
    has four parts, of which the first contains a proved statement and a reading, the second is an import,
    the third is conditional on the first two, on Observation \claimref{standard-model.dating-descent}
    and on a decision the fourth names, and the fourth is imported from the action paper; the levels are
    marked clause by clause.

    \begin{enumerate}

    \item \emph{(Kinematic.)} Proved: under $\Lambda \to s^{2}\Lambda$ at fixed $M_{P}$, that is $I \to
    sI$ on the frozen point with the conformal class unchanged, $H \to sH$ and $N \to N/s$, while every
    discrete invariant this paper derives (the algebra and its dimension twelve, the global form and its
    $\mathbb{Z}_{6}$, the dimension four, the content and the hypercharges, and under (S) the ratio $3/8$)
    is unchanged, since each is computed from the conformal class, the pair structure and the group alone,
    none of which the rescaling affects. Reading, at observation level: since the conformal class and
    the pair structure carry no scale, no construction from them alone can fix $N$, which lies in the
    ratio of the frozen point''s norm to the Planck scale; on this reading the kinematic layer determines
    all discrete invariants and no continuous modulus, and $N$ and the weight spectrum are its only continuous
    moduli.

    \item \emph{(Non-dynamical, imported.)} $\Lambda$ is the norm of the frozen point, and the norm is
    not a field: it is fixed by a constraint, the fluctuations of the frozen point are pure gauge, and
    the action carries no equation of motion for it (Fact \claimref{standard-model.imported-norm-frozen-point-not-field}).

    \item \emph{(Initial data, conditional.)} If the alternatives kinematic, dynamical and initial-data
    are exhaustive, then by (1) and (2) $N$ is initial data, and Observation \claimref{standard-model.dating-descent}(ii)
    locates the boundary that carries it at the origin. The exhaustiveness is not proved here, and the
    location is an Observation; the clause is conditional on both, and clause (4) says what the exhaustiveness
    costs.

    \item \emph{(Parameter of the laws, imported.)} The three alternatives are not exhaustive: a conserved
    quantity that is constant on every solution of a theory but varies across a family of theories indexed
    by a parameter is a parameter of the laws, and the action paper proves that under the action as written,
    with $\Lambda$ the value of the Stelle-West constraints fixed before variation, $N$ is exactly that:
    constant on each solution space $\mathcal{S}_{\Lambda}$ by the rigidity of (2), varying across $\Lambda$,
    so neither dynamically fixed nor initial data \cite[Prop.~5.8]{ButlerT10}. Clause (3) therefore holds
    only if the norm is promoted from a fixed number to the value of a Lagrange-multiplier field whose
    constancy is an equation of motion, the Henneaux-Teitelboim mechanism, which makes $\Lambda$ a label
    of the solution rather than of the theory; that promotion is a decision for the series, recorded open
    with both branches stated \cite[Rem.~5.9]{ButlerT10}, and the entropic and null-endpoint effects named
    below act on a measure over theories or on a measure within one theory according to it.

    \end{enumerate}

    At observation level, two competing effects are then named without being balanced: an entropic weighting
    of the freezing by $\exp(S_{\mathrm{modes}}) = \exp(N^{2})$ favours large $N$ overwhelmingly (the
    well-known entropic argument for small $\Lambda$, inherited with every one of its known objections,
    listed as inherited and not solved), while at the endpoint $\Lambda = 0$ the frozen point is null
    and the curvature-squared presentation of the action, whose prefactor is $3/\Lambda$, does not exist;
    the action paper is explicit that this is a boundary of the presentation and not of the action, the
    Einstein-Cartan functional remaining \cite[Thm.~3.1, Rem.~3.2]{ButlerT10}, so what is lost at $\Lambda
    = 0$ is the reductive structure and the frozen point''s length, not gravity. Large because large boundary
    mode spaces dominate the measure; nonzero because the descent selects a frozen point of nonzero length;
    the value is the balance point, and the balance point awaits the descent measure, the one object this
    framework does not possess. Last, a statement of units only, flagged as such: in the boundary modes''
    own units the number is $R = \log_{2} N^{2} \approx 400$ rungs, some fifty turns of the mod-8 clock,
    which is the question in the framework''s own coordinates, not an answer to it.'
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: Only the proof named a twistor notion (the flat twistor chart, now the flat chart of the conformal
      model). The formal level and the other levels have no twistor language and are unchanged.
  correction:
    by: ai-correction
    date: '2026-10-22'
    note: 'Observation-level paragraph only; the four clauses and the proof are unchanged. (a) The entropic
      weight exp(N^2) becomes exp(pi N^2), the performed area-law entropy (synthesis.de-sitter-entropy-pi-n-squared).
      (b) The units statement R = log2 N^2 ~ 400 rungs, fifty turns of the mod-8 clock: with one qubit
      per rung (T3 Thm 4.2) the horizon capacity pi N^2 nats is pi N^2/ln 2 ~ 4.77e122 qubits, and 2^407
      < pi N^2/ln 2 < 2^408 while 2^405 < N^2 < 2^406 (exact interval arithmetic on H0 = 67.4, Omega_Lambda
      = 0.685, M_P = 1.221e19 GeV); log2 N^2 is the rung count of a module of dimension N^2, not of the
      horizon mode space; and the residue p - q mod 8 is fixed by every rung (T1 Thm 7.1, T3 Cor 6.2(2)),
      so "turns of the mod-8 clock" contradicts proved results. Original text in source_formal.'
  open_problem: op.t12-n-after-the-count
about:
- obj.dark-energy.four-ways-number-enters-theory-shape
---

## formal
The question the paper ends by pointing at can itself be classified. The classification has four parts, of which the first contains a proved statement and a reading, the second is an import, the third is conditional on the first two, on Observation \claimref{standard-model.dating-descent} and on a decision the fourth names, and the fourth is imported from the action paper; the levels are marked clause by clause.
\begin{enumerate}
\item \emph{(Kinematic.)} Proved: under $\Lambda \to s^{2}\Lambda$ at fixed $M_{P}$, that is $I \to sI$ on the frozen point with the conformal class unchanged, $H \to sH$ and $N \to N/s$, while every discrete invariant this paper derives (the algebra and its dimension twelve, the global form and its $\mathbb{Z}_{6}$, the dimension four, the content and the hypercharges, and under (S) the ratio $3/8$) is unchanged, since each is computed from the conformal class, the pair structure and the group alone, none of which the rescaling affects. Reading, at observation level: since the conformal class and the pair structure carry no scale, no construction from them alone can fix $N$, which lies in the ratio of the frozen point's norm to the Planck scale; on this reading the kinematic layer determines all discrete invariants and no continuous modulus, and $N$ and the weight spectrum are its only continuous moduli.
\item \emph{(Non-dynamical, imported.)} $\Lambda$ is the norm of the frozen point, and the norm is not a field: it is fixed by a constraint, the fluctuations of the frozen point are pure gauge, and the action carries no equation of motion for it (Fact \claimref{standard-model.imported-norm-frozen-point-not-field}).
\item \emph{(Initial data, conditional.)} If the alternatives kinematic, dynamical and initial-data are exhaustive, then by (1) and (2) $N$ is initial data, and Observation \claimref{standard-model.dating-descent}(ii) locates the boundary that carries it at the origin. The exhaustiveness is not proved here, and the location is an Observation; the clause is conditional on both, and clause (4) says what the exhaustiveness costs.
\item \emph{(Parameter of the laws, imported.)} The three alternatives are not exhaustive: a conserved quantity that is constant on every solution of a theory but varies across a family of theories indexed by a parameter is a parameter of the laws, and the action paper proves that under the action as written, with $\Lambda$ the value of the Stelle-West constraints fixed before variation, $N$ is exactly that: constant on each solution space $\mathcal{S}_{\Lambda}$ by the rigidity of (2), varying across $\Lambda$, so neither dynamically fixed nor initial data \cite[Prop.~5.8]{ButlerT10}. Clause (3) therefore holds only if the norm is promoted from a fixed number to the value of a Lagrange-multiplier field whose constancy is an equation of motion, the Henneaux-Teitelboim mechanism, which makes $\Lambda$ a label of the solution rather than of the theory; that promotion is a decision for the series, recorded open with both branches stated \cite[Rem.~5.9]{ButlerT10}, and the entropic and null-endpoint effects named below act on a measure over theories or on a measure within one theory according to it.
\end{enumerate}
At observation level, two competing effects are then named without being balanced: an entropic weighting of the freezing by $\exp(S_{\Lambda}) = \exp(\pi N^{2})$, with $S_{\Lambda} = \pi N^{2}$ the cosmological horizon's area-law entropy (Theorem \claimref{synthesis.de-sitter-entropy-pi-n-squared}), favours large $N$ overwhelmingly (the well-known entropic argument for small $\Lambda$, inherited with every one of its known objections, listed as inherited and not solved), while at the endpoint $\Lambda = 0$ the frozen point is null and the curvature-squared presentation of the action, whose prefactor is $3/\Lambda$, does not exist; the action paper is explicit that this is a boundary of the presentation and not of the action, the Einstein-Cartan functional remaining \cite[Thm.~3.1, Rem.~3.2]{ButlerT10}, so what is lost at $\Lambda = 0$ is the reductive structure and the frozen point's length, not gravity. Large because large boundary mode spaces dominate the measure; nonzero because the descent selects a frozen point of nonzero length; the value is the balance point, and the balance point awaits the descent measure, the one object this framework does not possess. Last, a statement of units only, flagged as such: in the boundary modes' own units, qubits, one per rung of the Fock module (Theorem \claimref{tower.fock-module-one-qubit-per-rung}), the horizon's capacity $S_{\Lambda} = \pi N^{2}$ is $\pi N^{2}/\ln 2$, about $4.8 \times 10^{122}$ qubits (the mode count of Theorem \claimref{synthesis.de-sitter-mode-count} under the black hole's counting rule), whose base-two logarithm is about $407$; the paper's $R = \log_{2} N^{2} \approx 405$ counts the rungs of a module of dimension $N^{2}$, whose capacity is only $\ln N^{2} = 2\ln N$ nats, not the horizon's. Neither number is a count of turns of the mod-8 clock, which no rung moves: each rung preserves the residue $p - q \pmod 8$ (Theorem \claimref{transport.rule-1-morita-trivial}). This is the question in the framework's own coordinates, not an answer to it.

\emph{Note (the Hubble unit).} The numbers for $N = M_{P}/H$ here use $H^{2} = \Lambda/3$, that is $H_{0}\sqrt{\Omega_{\Lambda}}$ (with $H_{0} = 67.4$ km/s/Mpc and $\Omega_{\Lambda} = 0.685$), the $H$ in which the register states the rung unit $v/H$; some texts quote $v/H$ with $H_{0}$, which differs by the factor $\sqrt{\Omega_{\Lambda}}$, of order one ($\ln(v/H)$ changes by about $0.2$). No value of $v/H$ is quoted here.

## technical
The classification of $N = M_{P}/H$ has four clauses at different levels. Proved: under $\Lambda \to s^{2}\Lambda$ at fixed $M_{P}$, that is $I \to sI$ with the conformal class unchanged, $H \to sH$ and $N \to N/s$, while every discrete invariant the paper derives (the gauge algebra, its global form, the dimension four, the content and the hypercharges, and under (S) the ratio $3/8$) is unchanged; on the observation-level reading, no construction from the conformal class and pair structure alone can fix $N$. Imported: the norm of the frozen point is not a field, being fixed by a constraint with pure-gauge fluctuations.

Conditional: if kinematic, dynamical and initial data were exhaustive, $N$ would be initial data located at the origin. Imported: they are not exhaustive, since under the action as written, with $\Lambda$ fixed before variation, $N$ is a parameter of the laws, constant on each solution space and varying across $\Lambda$; the conditional clause holds only if the norm is promoted to the value of a Lagrange-multiplier field, a decision the series records open. The entropic and null-endpoint effects are named at observation level, the entropic weight being $\exp(\pi N^{2})$ for the area-law entropy $\pi N^{2}$. In units of qubits, one per rung, the horizon holds about $\pi N^{2}/\ln 2 \approx 4.8 \times 10^{122}$; the paper's $R = \log_{2}N^{2} \approx 405$ counts the rungs of a module of dimension $N^{2}$, not the horizon's mode space (whose base-two logarithm is about $407$), and no rung turns the mod-8 clock.

## lay
The framework's one large number, $N$, could in principle be fixed by the structure of the theory, by its equations, or by the starting conditions of the universe. This result proves that rescaling it changes nothing else the theory derives, reads that, at observation level, as showing that the structure alone cannot fix it, and imports the fact that no equation governs it. With the action as currently written $N$ turns out to be a fixed parameter of the laws; it would count as a starting condition only if the theory were modified in a specific way that the series leaves as an open choice.

## one-liner
The number $N = M_{P}/H$ rescales while every derived discrete invariant stays fixed (proved), which is read at observation level as $N$ not being kinematic; it is imported as not dynamical, and under the action as written it is a parameter of the laws, becoming initial data only if the norm is promoted to a field.
