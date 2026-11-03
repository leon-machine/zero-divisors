---
id: correspondence.one-statement-three-languages
kind: claim
version: 5
title: "One statement in three languages"
status: proved
region: correspondence
subject: conformal-spacetime
tags: [frozen-point, curvature-and-field-equations, dictionaries, cosmological-constant]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
review: typed
derivations:
- name: main
  uses:
  - correspondence.imported-vacuum-equations-scale-tractor@6
  - correspondence.spinor-identification@7
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_infinity_bivector_norm_is_lambda_over_three
- kind: check
  ref: check.py::check_infinity_bivector_simple_iff_lambda_zero
- kind: check
  ref: check.py::check_constancy_in_three_languages
locators:
  paper: T09
  number: Cor 4.8
  label: cor:threelang
  line: 566
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the infinity bivector as an equivariant I6-bilinear form on CS: Pfaffian proportional to Q, eps(I ^ I) = Lambda/3, simple exactly at Lambda = 0 with plane ker(ninf), and constancy equivalent to tractor parallelism. Version 3 -> 4. Check strengthened: invariance of the spinor form tested on every ordered pair of basis spinors (was j < k); sample vectors, directions, Lambda and Lorentz bivector moved to module level. Version 4 -> 5.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the region of invertibility is that of a gravitational field on flat spacetime and covariant constancy is for the tractor gauge field and its spin form; the three languages and the claim unchanged.'
  env: corollary
  typing:
    by: ai-typing-pass
    removed:
    - correspondence.local-twistor-transport-ascended-spinor-connection
    note: 'Removed the local-twistor edge: the proof only takes the spin bundle and its induced connection
      as set up there, not the proposition''s identification; the paper calls the simplicity criterion
      classical, but no imported claim stating it is in the store, so no standard route.'
  source_title: "One statement in three languages"
  source_formal: |-
    Define the \emph{infinity twistor} of a scale $g$ as $I_{\alpha\beta} := \Psi(I_g) \in \Lambda^2\T$, with $I_g = (1,0,\rho_g)$ the scale tractor of Fact \claimref{correspondence.imported-vacuum-equations-scale-tractor}. Then, on the region of invertibility:
    \begin{enumerate}
    \item vacuum with $\Lambda = 0$ holds if and only if the infinity twistor is covariantly constant and \emph{simple} (a line of $\PT$: the infinity line);
    \item the Einstein condition with $\Lambda \neq 0$ holds if and only if the infinity twistor is covariantly constant with $\varepsilon(I\wedge I) = \Lambda/3 \neq 0$: a non-simple bivector, which is no line at all.
    \end{enumerate}
    Field equations, tractor parallelism, and infinity-twistor constancy are one statement in three languages, and the classical twistor fact that the infinity twistor is simple precisely when $\Lambda = 0$ is the transport principle's nullity criterion (Theorem \claimref{correspondence.spinor-identification}(2)) applied to Fact \claimref{correspondence.imported-vacuum-equations-scale-tractor}.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistor space to the conformal spinor space (\\CS, \\PCS, \\CS M) and Penrose's infinity twistor to the infinity bivector of \\CS, named once; the classical fact is still credited to twistor theory as its source."
---

## formal
Define the \emph{infinity bivector} of a scale $g$ (Penrose's infinity twistor) as $I_{\alpha\beta} := \Psi(I_g) \in \Lambda^2\CS$, a bivector of the conformal spinor space, with $I_g = (1,0,\rho_g)$ the scale tractor of Fact \claimref{correspondence.imported-vacuum-equations-scale-tractor}. Then, on the region of invertibility of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), with covariant constancy taken for the tractor gauge field of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection} and its action on $\CS$:
\begin{enumerate}
\item vacuum with $\Lambda = 0$ holds if and only if the infinity bivector is covariantly constant and \emph{simple} (a line of $\PCS$: the infinity line);
\item the Einstein condition with $\Lambda \neq 0$ holds if and only if the infinity bivector is covariantly constant with $\varepsilon(I\wedge I) = \Lambda/3 \neq 0$: a non-simple bivector, which is no line at all.
\end{enumerate}
Field equations, tractor parallelism, and infinity-bivector constancy are one statement in three languages, and the classical fact of twistor theory that the infinity bivector is simple precisely when $\Lambda = 0$ is the transport principle's nullity criterion (Theorem \claimref{correspondence.spinor-identification}(2)) applied to Fact \claimref{correspondence.imported-vacuum-equations-scale-tractor}.

## technical
For a gravitational field on flat spacetime, the infinity bivector of a scale $g$ of its derived metric (Penrose's infinity twistor) is $I_{\alpha\beta} = \Psi(I_g) \in \Lambda^2\CS$, the image under the spinor identification of the scale tractor $I_g = (1, 0, \rho_g)$. On the region of invertibility, vacuum with $\Lambda = 0$ holds if and only if the infinity bivector is covariantly constant for the tractor gauge field $\Omega_{T}$ acting on conformal spinors and simple, a line of $\PCS$ (the infinity line); the Einstein condition with $\Lambda \neq 0$ holds if and only if it is covariantly constant with $\varepsilon(I\wedge I) = \Lambda/3 \neq 0$, a non-simple bivector that is no line at all.

So field equations, tractor parallelism and infinity-bivector constancy are one statement in three languages, and the classical fact that the infinity bivector is simple exactly when $\Lambda = 0$ is the nullity criterion of the spinor identification (null vectors are simple bivectors) applied to the scale tractor.

## lay
In this series gravity is a pair of fields on flat spacetime, and Einstein's vacuum equations can be phrased as the statement that one vector of the six-dimensional conformal model, the scale tractor, is constant as those fields carry it around. Translating that object into the spinors of the conformal algebra gives a bivector of that spinor space, the infinity bivector. This result shows that the three formulations say the same thing, and that the familiar fact that this bivector is a genuine line exactly when the cosmological constant vanishes is the same rule that matches lightlike vectors with lines.

## one-liner
On the invertible region of a gravitational field on flat spacetime, the vacuum and Einstein equations are equivalent to covariant constancy of the infinity bivector of the conformal spinor space, which is simple exactly when the cosmological constant vanishes.
