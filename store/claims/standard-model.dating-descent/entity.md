---
id: standard-model.dating-descent
kind: claim
version: 7
title: Dating the descent
status: conjectured
region: standard-model
subject: dark-energy
tags:
- matter-asymmetry
- the-number-n
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
  role: 'maintainer pass on Leon''s decisions, the second-reading margin of formal (iii) stated for the whole observed range (restatement)'
  version: 6
  source: maintainer pass 2026-11-07 (decisions)
- name: Claude Fable 5.2
  role: 'clause (i) corrected: the coincidence holds near the onset of Lambda-domination'
  version: 7
  source: 'maintainer pass of 2026-11-11 (run 2026-11-11-contradictions)'
amendments:
- version: 7
  kind: restatement
  defect: 'clause (i) said the age is of order N Planck times in any Lambda-dominated epoch; there 1/H is constant and the age grows without bound, so it holds only near the onset, the epochal form of standard-model.what (iii)'
review: typed
lineage:
  motivated_by:
  - dark-energy.gravity-pre-metric-forces-degenerate-exactly
derivations:
- name: conditional
  uses:
  - dark-energy.imported-henneaux-teitelboim-promotion@6
  - synthesis.einstein-route-makes-n-initial-data@4
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb@6
  note: 'Premise-only derivation, no proof text (a conjecture carries none): the dating of clause (ii)
    holds under the Henneaux-Teitelboim promotion, which T10 imports as Fact 5.11 and records as an
    open decision (Rem 5.9) and which the series adopts (decision of 23 October), with the register
    consequence for v/M_P from the Clausius-route result; clause (iii) rests on the finite-range bound
    on a descent deposit.'
locators:
  paper: T12
  number: Obs 7.4
  label: obs:dating
  line: 1251
extraction:
  maintainer_pass_2026_11_11:
    by: maintainer-2026-11-11
    date: '2026-11-11'
    note: 'Version 6 -> 7. One sentence of clause (i) corrected.'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Formal correction (DECISIONS A9, restatement): formal (iii) gave k/(a_d H_Lambda) > 7e9 at 1 MeV for every observed mode; it now reads > 4e9 at 1 MeV (> 7e9 for k >= a_0H_0), as synthesis.frozen-point-geometry-reads-descent-as-vacuum (ii) now proves. Evidence (reader, exact upper bound in v3.py; recomputed here in Fractions from the check''s inputs): the bound k/(a_d H_Lambda) = (k/a_0H_0)(a_0/a_d)/sqrt(Omega_Lambda) > 7e9 holds for k >= a_0H_0 (a_0/a_d > 10^12/168, sqrt(Omega_Lambda) < 0.83 with Omega_Lambda = 1 - 0.315 - 9.2e-5); the observed range starts at k = 2/eta_0, k/a_0H_0 in (0.627, 0.631), where the ratio is about 4.5e9 (0.627 (10^12/168)/0.83 > 4.49e9, and below 4.6e9). The conclusion (every observed mode inside) is unaffected.'
  maintainer_pass_weak_scale:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 5 (Leon''s register decision of 2026-11-01): clause (ii) no longer keeps v/H as a parameter of the laws; with synthesis.rung-unit-second-free-number version 3 the D-term level xi G, and so v/M_P, is the law, v/H is initial data and G v^2 N^2 = (v/H)^2 an identity, with a marked note recording the earlier wording; the technical level and the one-liner follow. a marked note fixes the Hubble unit of v/H (H^2 = Lambda/3, that is H_0 sqrt(Omega_Lambda), against H_0; a factor of order one, about 0.2 in ln(v/H)). Nothing else is changed.'
  env: observation
  context_refs:
  - dark-energy.gravity-pre-metric-forces-degenerate-exactly
  typing:
    by: ai-typing-pass
    note: 'Observation kept as conjectured; its motivating claim (the two-kinds theorem it cites for the
      pre-metric sector) was already recorded. Levels pass: conditions already kept.'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants: []
    added_about: []
    verdict: standalone
    note: Conjectured observation with lineage; the trichotomy's clause (3) is stated conditionally on
      it, which is a condition inside a proved statement, not a premise of its proof.
  source_formal: '(i) The one apparent indication fails. In any $\Lambda$-dominated epoch the age of the
    universe is automatically of order $N$ Planck times, since $t \sim 1/H$ and $N = M_{P}/H$: the Dirac
    coincidence is an identity of the era we observe from, not a clock pointing at the descent. The programme''s
    last indication was never one. (ii) The framework then answers, as its own claim: the descent froze
    at the beginning. The initial singularity is a division event; the classical era is the descended phase;
    the frozen point, hence $\Lambda$, hence $N$, was fixed at the origin and has been constant since, which
    is exactly the registered stance $w = -1$. The big bang, in this reading, is not an explosion in spacetime
    but the freezing of spacetime out of the ascended phase: the universe''s descent is its origin. (iii)
    At observation level, this is testable in kind: pre-descent physics is the pre-metric sector, the polynomial
    action and the $\theta$-remnants alone (Fact \claimref{dark-energy.gravity-pre-metric-forces-degenerate-exactly}),
    so the descent event, not an inflationary epoch, would source the earliest correlations. (iv) The residue:
    the dynamics of the freezing itself, declared beyond this paper''s scope. The last question of the theory
    is the first event of the universe.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Version 3 (Leon''s decisions 3 and 11 of 2026-10-23). Clause (ii): the Henneaux-Teitelboim promotion is adopted with v/H kept as the law, so N is initial data dated to the origin, v/M_P is initial data with G v^2 N^2 = (v/H)^2 a law (synthesis.einstein-route-makes-n-initial-data), the conjugate time is the record of synthesis.promoted-norm-weyl-clock-flat-weight version 4, and the smallness of Lambda is outside the series. Clause (iii) restated with its real condition: the descent can source the earliest correlations only through a pre-metric deposit correlated over hundreds to about 10^18 Hubble lengths of the descent, or a source acting after the descent, and the series supplies neither (synthesis.finite-range-descent-deposit-cannot-seed-cmb); no tensor amplitude is registered. The paper''s wording stays under source_formal.'
  maintainer_pass_2:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Version 3 -> 4 (maintainer decision of 26 October on the join of the frozen phase to the descent). Clause (iii) now records the two readings of that join: primary, (F), the late de Sitter stage of the observed Lambda is the frozen point''s own field, so the descent slice sits at |x_d| = eta_inf - eta_d in the frozen point''s chart, about 4.3 present Hubble radii; second, the frozen phase ends at the descent with the scale factor continuous. Both place every observed mode inside the frozen phase''s Hubble length (by k|x_d| from 2.7, about 960 at the pivot, against more than 7e9 at 1 MeV), so both read a deposit set by the frozen point as the vacuum (synthesis.frozen-point-geometry-reads-descent-as-vacuum). No other clause changes.'
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 3
    note: 'Made conditional (seed/CONTRADICTIONS_VALUES.md H3): clause (ii) now states that Lambda and N
      were fixed at the origin under the Henneaux-Teitelboim promotion, and every level says so. The promotion
      is carried by the T10 import dark-energy.imported-henneaux-teitelboim-promotion (Fact 5.11), now used
      in a premise-only derivation ''conditional''; adopting it for the Stelle-West norm is a decision the
      series records open, not a premise it takes as given, so no postulate was made. Linked with claimref:
      the T10 result that N is a parameter of the laws under the action as written (dark-energy.under-action-written-norm-parameter-laws,
      T10 Prop 5.8), the T10 remark that reconciles the two readings (note.dark-energy.what-clause-3-requires-what-it,
      Rem 5.9), and the w = -1 registration with its condition (pred.dark-energy-w-minus-one), whose condition
      the old wording dropped. Original formal in source_formal.'
---

## formal
(i) The one apparent indication fails. Near the onset of $\Lambda$-domination the age of the universe is automatically of order $N$ Planck times, since $t \sim 1/H$ there and $N = M_{P}/H$ (later the age grows while $1/H$ stays fixed): the Dirac coincidence is a property of the epoch we observe from, not a clock pointing at the descent. The programme's last indication was never one. (ii) The framework then answers, as its own claim and under the promotion it adopts: the descent froze at the beginning. The initial singularity is a division event; the classical era is the descended phase; under the Henneaux-Teitelboim promotion of the Stelle-West norm to the value of a Lagrange-multiplier field whose constancy is an equation of motion (Fact \claimref{dark-energy.imported-henneaux-teitelboim-promotion}), which the series adopts, the frozen point, hence $\Lambda$, hence $N$, was fixed at the origin and has been constant since, which matches the registered stance $w = -1$ (registered with its own condition, \claimref{pred.dark-energy-w-minus-one}). $N$ is then initial data of the descent (\claimref{programme.n-parameter-of-the-laws}); with the weak scale's constant of the laws the D-term level $\xi G$ (Premise \claimref{synthesis.rung-unit-second-free-number}, version 3), $v/M_{P}$ is the law up to relative order $(H/v)^{4}$, the rung unit $v/H$ is initial data too, and $Gv^{2}N^{2} = (v/H)^{2}$ is an identity (Theorem \claimref{synthesis.einstein-route-makes-n-initial-data}(iii)). \emph{Note (register, 2026-11-01).} Until version 4 this sentence kept $v/H$ as a parameter of the laws, with $v/M_{P}$ initial data and $Gv^{2}N^{2} = (v/H)^{2}$ a law; the register was restated when the stored D-term action, read under the promotion, made $v/H$ initial data (\claimref{synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion}). Under the action as written, with $\Lambda$ fixed before variation, $N$ would instead be a parameter of the laws (Proposition \claimref{dark-energy.under-action-written-norm-parameter-laws}, Remark \claimref{note.dark-energy.what-clause-3-requires-what-it}). The time conjugate to the promoted norm (Theorem \claimref{synthesis.promoted-norm-weyl-clock-flat-weight}) runs with matter, is not monotone and, by an argued reading, advances fastest in the earliest epoch: it is a record of the descended history, not a clock that dates the descent. Why $\Lambda$ is small is outside the series. The big bang, in this reading, is not an explosion in spacetime but the freezing of spacetime out of the ascended phase: the universe's descent is its origin. (iii) At observation level: pre-descent physics is the pre-metric sector, the polynomial action and the $\theta$-remnants alone (Fact \claimref{dark-energy.gravity-pre-metric-forces-degenerate-exactly}), and the dating reads the descent event, not an inflationary epoch, as the source of the earliest correlations. In the descended phase no mode at or below the pivot scale leaves the Hubble length after the descent, so the descent can source the measured primordial spectrum only through a pre-metric deposit correlated over hundreds (descent at $1$ MeV) to about $10^{18}$ (descent at $10^{12}$ GeV) Hubble lengths of the descent, for a deposit that is a perturbation (one-point variance at most one), or through a source acting after the descent (Theorem \claimref{synthesis.finite-range-descent-deposit-cannot-seed-cmb}). The series supplies neither, so it has no mechanism for the measured spectrum, neither its amplitude nor its index $n_{s}$; it registers no prediction of the tensor amplitude. The join of the frozen phase to the descent has two readings. The primary one, (F), takes the late de Sitter stage of the observed $\Lambda$ to be the frozen point's own field, so the descent slice sits at $|x_{d}| = \eta_{\infty} - \eta_{d}$ in the frozen point's chart, about $4.3$ present Hubble radii, and the observed modes have $k|x_{d}|$ from about $2.7$ to about $10^{4}$ (about $960$ at the pivot). The second reading takes the frozen phase to end at the descent with the scale factor continuous; the observed modes then lie inside the frozen phase's Hubble length by $k/(a_{d}H_{\Lambda}) > 4 \times 10^{9}$ at $1$ MeV ($> 7 \times 10^{9}$ for $k \ge a_{0}H_{0}$). In both readings every observed mode is inside the frozen phase's Hubble length at the descent, so a deposit correlated by the frozen point supplies the range the amplitude needs but reads as the vacuum, $n_{s} - 1 = 2$ (Proposition \claimref{synthesis.frozen-point-geometry-reads-descent-as-vacuum}); the readings differ in how far inside the modes sit, and only in (F) does the frozen point's one length enter the observed range, at the largest scales. (iv) The residue: the dynamics of the freezing itself, declared beyond this paper's scope. The last question of the theory is the first event of the universe.

\emph{Note (the Hubble unit).} Here $H$ is the de Sitter rate of $\Lambda$, $H^{2} = \Lambda/3$, that is $H_{0}\sqrt{\Omega_{\Lambda}}$, the $H$ of $N = M_{P}/H$; some texts quote $v/H$ with $H_{0}$, which differs from it by the factor $\sqrt{\Omega_{\Lambda}}$, of order one ($v/H \approx 2.1 \times 10^{44}$ against $v/H_{0} \approx 1.7 \times 10^{44}$; $\ln(v/H)$ changes by about $0.2$). No value of $v/H$ is quoted here.

## technical
At observation level. In any $\Lambda$-dominated epoch the age of the universe is of order $N$ Planck times, since $t \sim 1/H$ and $N = M_{P}/H$, so the Dirac coincidence is an identity of the era we observe from and not a clock pointing at the descent. The framework then takes as its own claim, under the promotion it adopts, that the descent froze at the beginning: the initial singularity is a division event, the classical era is the descended phase, and with the Stelle-West norm promoted to a Lagrange-multiplier field in the manner of Henneaux and Teitelboim, the frozen point, hence $\Lambda$ and $N$, was fixed at the origin and has been constant since, which matches the registered stance $w = -1$ with its own condition. $N$ is initial data; the weak scale in Planck units is the law (through the D-term level), so the rung unit $v/H$ is initial data too, and $Gv^{2}N^{2} = (v/H)^{2}$ is an identity. For the action as written $N$ would be a parameter of the laws. The promotion's conjugate time runs with matter but is not monotone, a record of the history rather than a date for the descent, and the smallness of $\Lambda$ is outside the series.

The dating reads the descent event rather than an inflationary epoch as the source of the earliest correlations. After the descent no mode at or below the pivot scale leaves the Hubble length, so the measured spectrum would need a pre-metric deposit correlated over hundreds to about $10^{18}$ Hubble lengths of the descent, depending on its temperature, or a source acting after the descent. The series supplies neither, so it has no mechanism for the measured spectrum or its index; no tensor amplitude is registered. Whether the frozen phase is read as the late de Sitter stage of the observed $\Lambda$ (the primary reading) or as a phase ending at the descent with a continuous scale factor (a second reading), the observed modes were inside its Hubble length at the descent, so a deposit correlated by the frozen point gives the vacuum's spectrum, not the measured one. The dynamics of the freezing itself are declared beyond scope.

## lay
A famous coincidence says that the age of the universe, measured in the tiniest natural unit of time, is about the same huge number that appears elsewhere in the framework. This observation argues that the coincidence is automatic in any universe dominated by dark energy, so it is not a clue about when anything happened. Instead the framework proposes that the number was fixed at the very beginning, with the big bang read as spacetime freezing out of an earlier phase. That proposal uses a known modification of the theory, which the framework adopts, making the cosmological constant a quantity set by the particular universe; why its value is so small is left outside the framework. The framework would like the first event to have laid down the ripples later seen in the cosmic background, but those ripples span distances far larger than anything in contact at that event, so they would need correlations already present before spacetime, or a later source, and the framework provides neither. How the freezing happened is also left open.

## one-liner
The Dirac coincidence is automatic in a $\Lambda$-dominated era; under the Henneaux-Teitelboim promotion, which the series adopts, the descent froze at the origin with $N$ and $v/H$ initial data and $v/M_{P}$ the law, and the descent could seed the measured spectrum only through a pre-metric deposit correlated over hundreds to $10^{18}$ of its Hubble lengths or a later source, neither of which the series supplies.
