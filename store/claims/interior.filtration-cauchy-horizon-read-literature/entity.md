---
id: interior.filtration-cauchy-horizon-read-literature
kind: claim
version: 7
title: The filtration at the Cauchy horizon, read from the literature
status: proved
region: interior
subject: interior
tags: [kerr, horizons, obstruction-types]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
review: typed
about:
- obj.transport.obstruction-types
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - interior.imported-mass-inflation-stability@3
  - interior.stabilisers-flat-model@5
  - singularity.type-n-only-type-n@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_boost_weights_of_bivectors
- kind: check
  ref: check.py::check_parabolic_and_its_nilradical
- kind: check
  ref: check.py::check_extreme_weight_curvature_occupies_nilpotent_slots
locators:
  paper: T06
  number: Prop 6.11
  label: prop:ordering
  line: 896
extraction:
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 6 -> 7. Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: algebraic core of finding (3): boost-weight grading of bivectors, the parabolic of a null direction and its nilradical, extreme-weight Weyl maps landing in the nilpotent slots. Version 4 -> 5. check_extreme_weight_curvature_occupies_nilpotent_slots: asserts Weyl dimension 10 and that weight +2 images span the nilpotent slot (rank 2) (fix round 2026-10-23). Version 5 -> 6.'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Tractor wording completed by the lead: the tractor connection is named as the Cl(2,4) gauge field of the gravitational field, which carries the Schouten map in its n0 summand. Content unchanged.'
  typing:
    by: ai-typing-pass
    note: 'Kept all three uses (the type-N reading, the imports, the flat-model nilradical slot); the
      sheaf localised-transport and one-sided-completion results in context_refs enter only through the
      singularity paper''s type-N proposition and were not added. Levels pass: lay and one-liner now keep
      ''generically'' and that the connection-level failure is proved only in spherical symmetry and expected
      for Kerr.'
  env: proposition
  context_refs:
  - sheaf.localised-transport
  - sheaf.one-sided-completion
  eqrefs: 1
  flags:
  - 'beyond one flat chart: the Cauchy horizon of the maximal development and the extension across it'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement (MIXED): metric becomes the derived metric of the gravitational field on flat spacetime, the Levi-Civita connection is the rotation-gauge field Omega, and the divergent curvature components are components of the field strength; the Cauchy horizon and the extension across it are flagged beyond one flat chart (DICTIONARY.md section 14, item 3). Findings unchanged; tractor wording left to the lead. Proof: one opening sentence pointing to the GTG dictionary Fact.'
---

## formal
In the framework's language, Fact \claimref{interior.imported-mass-inflation-stability} yields three findings; each is a reading of the imported statements, and the one-step translation carrying each reading is proved below.
\begin{enumerate}
\item \emph{Obstruction type:} the degeneration at the perturbed Cauchy horizon is of type N (null kernel direction), in the degenerate-radical reading the series fixes at the Schwarzschild centre \cite[Prop.~3.1]{ButlerT5}, which extends T1's taxonomy \cite[Def.~3.1]{ButlerT1} to radical directions through \cite[Thm.~4.4, Cor.~4.5]{ButlerT4}: the same class as at the centre, realised on a null hypersurface rather than at a point.
\item \emph{Filtration by derivative level:} a $C^0$ derived metric $g(a,b) = \hb^{-1}(a) \cdot \hb^{-1}(b)$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) determines a $C^0$ conformal class (pointwise multiplication by a positive function preserves continuity, and the class map $g \mapsto [g]$ is continuous), so point-level structure, metric and conformal alike, extends continuously across the Cauchy horizon, while connection-level structure, the rotation-gauge field $\Omega$ (whose reading on $g$ is the Levi-Civita connection) and the tractor connection alike (on flat spacetime the $\Cl(2,4)$ gauge field of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}, whose $\nO$ summand carries the Schouten map, two derivatives of $g$), generically fails: proved in spherical symmetry by Fact \claimref{interior.imported-mass-inflation-stability}(ii$'$), expected for Kerr. The ordering is by derivative level; a strict separation of the conformal description from the metric one at fixed derivative level is not among the imports, and is exactly the open transport question of Section \ref{sec:scope}.
\item \emph{Filtration:} in a physical frame adapted to the horizon generators, the divergent components of the field strength $\mathcal{R}(B)$ are those of extreme boost weight, the top of the parabolic filtration attached to the null direction: the divergence occupies the nilpotent slots, as in every previous instance of the obstruction.
\end{enumerate}
\emph{Beyond one flat chart.} The Cauchy horizon, as the boundary of the maximal development, and the extension of the field across it are global and are not carried by a single gravitational field $(\hb, \Omega)$ on flat spacetime; the statements above that hold on the invertible region (the type and kernel of the degeneration, the regularity of the derived metric and of $\Omega$ along the approach, the boost weights of the divergent components) are in Gauge Theory Gravity, and the Cauchy horizon and the extension across it are read on the manifold assembled from the derived metric's charts.

## technical
Reading the imported results on mass inflation and $C^0$ stability in the framework's language gives three findings. First, the degeneration at the perturbed Cauchy horizon is of type N, with a null kernel direction, in the degenerate-radical reading fixed at the Schwarzschild centre: the same obstruction class, now realised on a null hypersurface. Second, survival is ordered by derivative level: a $C^0$ derived metric gives a $C^0$ conformal class, so point-level structure, metric and conformal alike, extends across the horizon, while connection-level structure, the rotation-gauge field $\Omega$ (the Levi-Civita connection) and the tractor connection alike, generically fails; this failure is proved in spherical symmetry and expected for Kerr.

No strict separation of the conformal and metric descriptions at fixed derivative level follows from the imports; that question stays open. Third, in a frame adapted to the horizon generators the divergent components of the field strength have extreme boost weight, the top of the parabolic filtration of the null direction, so the divergence occupies the nilpotent slots. Its Cauchy horizon and the extension across it are global: no single gravitational field on flat spacetime carries them, so that part is read on several charts of flat spacetime, each carrying its own gravitational field, glued on overlaps by displacement and rotation gauge transformations.

## lay
The inner horizon of a rotating black hole is known to be unstable: perturbations make the strength of the gravitational field blow up there, although the field itself stays continuous. This result translates those established findings into the series' language. It finds the same kind of breakdown as at the centre of a non-rotating black hole, one that generically hits the rules for comparing directions but not the field itself (proved in the spherically symmetric case and expected for rotating holes), and it places the divergence where the framework expects it.

## one-liner
Read through the imported Cauchy-horizon results, the perturbed Kerr Cauchy horizon is a type-N degeneration, with survival ordered by derivative level (point-level structure extends, connection-level structure generically fails, proved in spherical symmetry and expected for Kerr) and the divergence in the nilpotent slots.
