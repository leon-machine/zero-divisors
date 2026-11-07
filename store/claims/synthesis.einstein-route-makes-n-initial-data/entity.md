---
id: synthesis.einstein-route-makes-n-initial-data
kind: claim
version: 4
title: 'On the Clausius route, N is initial data without promotion'
status: proved
region: synthesis
subject: dark-energy
tags: [the-number-n, undetermined-input, cosmological-constant]
proposed_by:
  kind: ai
  session: 2026-10-23-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.dark-energy.four-ways-number-enters-theory-shape
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.einstein-equations-from-c-loc-and-clausius@7
  - mass.de-sitter-scale-frozen-point@6
  - dark-energy.under-action-written-norm-parameter-laws@4
  - synthesis.promoted-norm-one-global-pair@4
  - dark-energy.imported-henneaux-teitelboim-promotion@5
  - synthesis.smallness-monomials-exact-hierarchy-casimir@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_de_sitter_family_solves_route_equations
- kind: check
  ref: check.py::check_n_not_constant_on_route_solutions
- kind: check
  ref: check.py::check_de_sitter_lambda_constant_instance
- kind: check
  ref: check.py::check_rung_ratio_register
lineage:
  motivated_by:
  - programme.n-parameter-of-the-laws
  - standard-model.dating-descent
  - note.dark-energy.what-clause-3-requires-what-it
extraction:
  maintainer_pass_weak_scale:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 4 (Leon''s register decision of 2026-11-01): clause (iii) and the technical level no longer say that the registered premise holds v/H as the parameter; a marked note records that synthesis.rung-unit-second-free-number version 3 takes the second branch of (iii) (v/M_P, the level xi G, the law; v/H initial data; G v^2 N^2 = (v/H)^2 an identity), and the proof''s sentence on the premise names its version 2. a marked note fixes the Hubble unit of v/H (H^2 = Lambda/3, that is H_0 sqrt(Omega_Lambda), against H_0; a factor of order one, about 0.2 in ln(v/H)). The clauses and the proof''s argument are unchanged.'
  open_problem: op.henneaux-teitelboim-promotion
  note: 'Decision input. The comparison in the store sets the action as written (N a parameter of the laws) against the Henneaux-Teitelboim promotion (N initial data) as if the series had one dynamics. It has two: the frozen-point action, and the Clausius route that derives Einstein''s equations from (C_loc) and (H1), adopted as the series'' route to gravity. On that route Lambda is an integration constant, the solution set is the union over Lambda, which is the metric part of the promoted solution space, and N is initial data by the store''s own Definition read with the route''s equations as the laws. So the store does not force the decision: the route alone has the promoted solution space; rejecting the promotion means letting the action as written supply the law Lambda = Lambda_0 (the conjunction of route and action is consistent and has N of kind (P)), and adopting it adds a conjugate time and the Liouville density, which the route does not supply. The conjugate time is not one object: it depends on which action is promoted (for the frozen-point action it is the Weyl-squared integral in vacuum and the Euler-density excess with matter, synthesis.promoted-norm-weyl-clock-flat-weight; for an Einstein-Hilbert action it would be the four-volume), and the route by itself cannot choose. The Definition of the four kinds of number is stated for an action-indexed family; here it is applied beyond that scope, to an action-free theory with one solution space. Second, a consequence the comparison misses: with N initial data (on the route or under the promotion), the registered rung-unit premise (v/H a parameter of the laws) makes v/M_P initial data, with G v^2 N^2 = (v/H)^2 a law, and holding v/M_P as the law parameter instead makes v/H initial data and the premise false as worded. Under the action as written both can be parameters. Transport-absent (Jacobson-type and Henneaux-Teitelboim bookkeeping); the content is what it says about the series'' two dynamics and its register.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the route''s laws written G(a) + Lambda a = -8 pi G_cl T(a) in the store''s sign (DICTIONARY C6), the sphere-positive tensor form kept as a reading; the de Sitter solution g = sigma^{-2} eta named as the field hb(a) = sigma a on sigma != 0. Clauses (i)-(iii) unchanged; proof given a pointer. Check entries synced with check.py: +1, -1 (added check_de_sitter_lambda_constant_instance; removed check_promoted_solution_space_is_the_routes). Version 2 -> 3.'
---

## formal
Let the \emph{Clausius route} be the theory whose laws are the conclusions of Theorem \claimref{synthesis.einstein-equations-from-c-loc-and-clausius}: for a gravitational field $(\hb, \Omega)$ on a connected region of flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), $\mathcal{G}(a) + \Lambda a = -8\pi G_{\mathrm{cl}}T(a)$ in the store's sign (in the sphere-positive convention of the derived metric, $\Ric^{\circ} - \tfrac12R^{\circ}g - \Lambda g = 8\pi G_{\mathrm{cl}}T$ in signature $(1,3)$) with $\Lambda$ a constant that (C$_{\mathrm{loc}}$) and (H1) to (H4) leave free. Read Definition \claimref{obj.dark-energy.four-ways-number-enters-theory-shape}, which is stated for a family of action functionals, with these equations as the laws, so that $\Lambda$ indexes no law (an extension of its stated scope to an action-free theory with one solution space). Let $N = M_{P}\sqrt{3/\Lambda}$, $N = M_{P}/H$ on a de Sitter region (Proposition \claimref{synthesis.smallness-monomials-exact-hierarchy-casimir}).
\begin{enumerate}
\item[(i)] \emph{(N is initial data on the route.)} For every $\Lambda > 0$ the de Sitter field $\hb(a) = \sigma a$, $\sigma = 1 - \Lambda Q(x)/12$, on the invertible region $\sigma \neq 0$, whose derived metric is $g_{\Lambda} = \sigma^{-2}\eta$ of Lemma \claimref{mass.de-sitter-scale-frozen-point}, solves the route's equations with $T = 0$ and constant $\Lambda$, and $N$ is conserved along each solution. $N$ takes every positive value on the route's solution set, so in the sense of the Definition it is (I), initial data, and neither (P) nor (D), with no promotion.
\item[(ii)] \emph{(The route has the promoted solution space.)} The gravitational-field parts (with their derived metrics) of the solutions of the Henneaux-Teitelboim promoted equations (Fact \claimref{dark-energy.imported-henneaux-teitelboim-promotion}), Einstein's equations with $\Lambda$ a field and $d\Lambda = 0$, on a connected region, are the Einstein metrics with some constant $\Lambda$: the route's solution set, which is the union over $\Lambda$ of the solution spaces $\mathcal{S}_{\Lambda}$ of the action as written (Proposition \claimref{dark-energy.under-action-written-norm-parameter-laws}). What the promotion adds to the route is a conjugate variable $\tau$ and the Liouville density of the pair $(\Lambda, \tau)$ (Theorem \claimref{synthesis.promoted-norm-one-global-pair}(iii), (v)); both depend on which action is promoted (for the frozen-point action, $\tau$ advances by the integral of Theorem \claimref{synthesis.promoted-norm-weyl-clock-flat-weight}), and the route has no action and supplies neither. Keeping the route and rejecting the promotion requires the law $\Lambda = \Lambda_{0}$, which no premise of the route supplies and which the action as written supplies ($\Lambda$ fixed before variation, Proposition \claimref{dark-energy.under-action-written-norm-parameter-laws}); the conjunction of route and action is consistent and has $N$ of kind (P).
\item[(iii)] \emph{(The register under initial-data N.)} If $N$ is (I), two positive conserved quantities whose ratio is $N$ cannot both be constant on the solution space. With $v/M_{P} = (v/H)/N$: if $v/H$ is a parameter of the laws, as version 2 of the registered rung-unit premise stated, then $v/M_{P}$ is initial data and $Gv^{2}N^{2} = (v/H)^{2}$ holds as a law; if instead $v/M_{P}$ is held as the parameter, then $v/H = (v/M_{P})N$ is initial data and the rung-unit premise as worded fails. Under the action as written, where $N$ is (P), both can be parameters.
\end{enumerate}
\emph{Note (register, 2026-11-01).} The rung-unit premise, version 3 (\claimref{synthesis.rung-unit-second-free-number}), holds the D-term level $\xi G$, and so $v/M_{P}$ up to relative order $(H/v)^{4}$, as the law: the series is on the second branch of (iii), $v/H$ is initial data, and $Gv^{2}N^{2} = (v/H)^{2}$ is then an identity rather than a law (\claimref{synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion}). The clauses are unchanged.

\emph{Note (the Hubble unit).} Here $H$ is the de Sitter rate of $\Lambda$, $H^{2} = \Lambda/3$, that is $H_{0}\sqrt{\Omega_{\Lambda}}$, the $H$ of $N = M_{P}/H$; some texts quote $v/H$ with $H_{0}$, which differs from it by the factor $\sqrt{\Omega_{\Lambda}}$, of order one ($v/H \approx 2.1 \times 10^{44}$ against $v/H_{0} \approx 1.7 \times 10^{44}$; $\ln(v/H)$ changes by about $0.2$). No number here depends on the choice.

## technical
The series has two dynamics for the gravitational field on flat spacetime. Under the frozen-point action as written, $\Lambda$ is fixed before variation and $N$ is a parameter of the laws. On the Clausius route, which derives Einstein's equations from (C$_{\mathrm{loc}}$) and the Clausius hypothesis, $\Lambda$ is an integration constant: the de Sitter field $\hb(a) = \sigma a$ at every $\Lambda$ solves the route's equations (checked exactly at rational points for two values, with the Ricci map of the derived metric $\sigma^{-2}\eta$ computed from its conformal factor), so $N$ is not constant on the route's solutions and is initial data in the store's own Definition. That solution set is exactly the metric part of the Henneaux-Teitelboim promoted theory; the promotion adds a conjugate time and a Liouville density, both depending on which action is promoted, which the route, having no action, does not supply. Combined with the action as written, the route is restricted to one value of $\Lambda$ and $N$ is a parameter of the laws; the route on its own does not decide between the two kinds.

So the store does not force the decision, but the branches do not cost the same: rejecting the promotion while keeping the route needs an extra law fixing the integration constant. And once $N$ is initial data, the register of free numbers changes: $v/H$ and $v/M_{P}$ differ by the factor $N$, so at most one of them is a parameter. The rung-unit premise first registered $v/H$ as the parameter, which would make the weak scale in Planck units initial data tied to $N$ by $Gv^{2}N^{2} = (v/H)^{2}$; its version 3 holds $v/M_{P}$ (the D-term level) instead, so $v/H$ is initial data and that relation is an identity.

## lay
The theory has two ways of getting Einstein's gravity: from its own action, where the cosmological constant is fixed in advance, and from a thermodynamic argument about horizons, where it comes out as a constant of integration that can take any value. On the second route taken alone, the large number N built from the cosmological constant is a property of the particular universe, not of the laws. So the thermodynamic route on its own does not decide whether the constant should be promoted to a field: combined with the action it is a law, on its own it is a property of the universe. It also has a side effect: the ratio of the weak scale to the Hubble scale and its ratio to the Planck scale cannot both be fixed by the laws once N varies from universe to universe.

## one-liner
On the Clausius route $\Lambda$ is an integration constant, so on the route alone $N$ is initial data with no promotion and the route has the promoted solution space, while the action as written supplies the law $\Lambda = \Lambda_{0}$ and restores (P); and once $N$ is initial data, $v/H$ and $v/M_{P}$ cannot both be parameters of the laws.
