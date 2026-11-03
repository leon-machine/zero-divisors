---
id: mass.imported-frozen-point-tractor-connection
kind: claim
version: 6
title: 'Imported: the frozen point and the tractor connection'
status: proved
region: mass
subject: einstein
tags: [frozen-point, tractors, cosmological-constant]
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
review: typed
derivations:
- name: main
  uses:
  - interior.covariant-form-vacuum-equations@5
  - interior.imported-tractor-connection@2
  - interior.non-null-stabilisers-section-they-act@4
  - interior.scale-tractor-leaves-cone@7
  - interior.sign-fixed-internally@4
  - interior.stabiliser-rotates-parabolic-reductive@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T11.py
  tags:
  - label:fact:frozen
- kind: check
  ref: check.py::check_displayed_connection_slots
- kind: check
  ref: check.py::check_frozen_point_parallel_with_rho_j_over_n
- kind: check
  ref: check.py::check_stabiliser_de_sitter_group_and_sign
- kind: check
  ref: check.py::check_general_n_rho_is_j_over_n
locators:
  paper: T11
  number: Fact 2.1
  label: fact:frozen
  line: 402
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: displayed slots of the Cl(2,4) gauge field; on GTG Einstein fields P = (Lambda/6) id, J = 2 Lambda/3, I = ninf + (J/4) n0 parallel with Q = Lambda/3; stabiliser dimension 10, I-perp (1,4), opposite sign gives (2,3); general n: rho = J/n for n = 3..6. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the background is the derived metric of a gravitational field on flat spacetime, the ambient bundle the Cl(2,4) vectors sigma ninf + mu + rho n0, and the connection the tractor gauge field (index display kept as its reading); content unchanged, including the general-n remark.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  typing:
    by: ai-typing-pass
    note: All six uses are the interior-paper results this fact restates; the sign lemma was kept because
      the fact restates its content (that the Schouten sign is fixed internally), which is the least clear-cut
      of the six.
  env: fact
  context_refs:
  - interior.covariant-form-vacuum-equations
  - interior.imported-tractor-connection
  - interior.non-null-stabilisers-section-they-act
  - interior.scale-tractor-leaves-cone
  - interior.sign-fixed-internally
  - interior.stabiliser-rotates-parabolic-reductive
  eqrefs: 4
  outside_pilot_cites:
  - ButlerT6
  flags:
  - 'fact restating several series results: derived from them'
---

## formal
Let $g$ be the derived metric of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}). The ambient bundle, whose fibre is the vector space of $\Cl(2,4)$ with tractors $\sigma\nInf + \mu + \rho\nO$, carries the canonical connection, which in Gauge Theory Gravity is the $\Cl(2,4)$ rotation-gauge field $D^{T}_{a} = a \cdot \nabla + \Omega_{T}(a)\times$, $\Omega_{T}(a) = \Omega(a) - \nInf \wedge \hb^{-1}(a) + \nO \wedge \Sch(\hb^{-1}(a))$, acting on tractors $\sigma\nInf + \mu + \rho\nO$ (Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}), whose expression in the scale $g$ is
\begin{equation}
\nabla_{a}(\sigma, \mu_{b}, \rho) = \bigl(\nabla_{a}\sigma - \mu_{a},\;\; \nabla_{a}\mu_{b} + g_{ab}\,\rho - P_{ab}\,\sigma,\;\; \nabla_{a}\rho + P_{a}{}^{b}\mu_{b}\bigr),
\end{equation}
and it preserves \eqref{eq:tractormetric}. On a vacuum Einstein field with cosmological constant $\Lambda$ (field strength $\mathcal{R}(a) = \Lambda a$), in these conventions $P_{ab} = (\Lambda/6)\,g_{ab}$ and $J = 2\Lambda/3$, the bundle carries a distinguished parallel section $I$, the frozen point: in its own scale $I = (1, 0, \rho_{I}) = \nInf + \rho_{I}\nO$ with vanishing middle slot, $\nabla I = 0$ is equivalent to the vacuum equations, and
\[
\rho_{I} = \frac{J}{n} = \frac{\Lambda}{6}, \qquad Q(I) = \frac{2J}{n} = \frac{\Lambda}{3}.
\]
(The geometry paper is four-dimensional; the general-$n$ form of $\rho_{I}$ is the middle slot of \eqref{eq:tractorconn} for the section $(1, 0, \rho_{I})$, $g_{ab}\rho_{I} = P_{ab}$, traced.) $I$ is null exactly when $\Lambda = 0$; for $\Lambda > 0$ its stabiliser is $SO(1,4)$ and the induced form on $I^{\perp}$ has signature $(1,4)$. \emph{Provenance:} \cite[Fact~4.1, Prop.~4.4, Thm.~4.5, Thm.~4.7, Prop.~4.10]{ButlerT6} (Prop.~4.4 for the stabiliser algebra and the signature of $I^{\perp}$, Prop.~4.10 for the group). The sign of the norm is the series' convention, fixed there and machine-verified; \cite[Rem.~4.9]{ButlerT6} records why that sign is not free: a norm of the opposite sign could not carry the de Sitter stabiliser the same paper establishes. The relative sign of the Schouten slots in \eqref{eq:tractorconn} against the literature is convention-dependent and is fixed internally in the geometry paper \cite[Lem.~4.8]{ButlerT6}; every formula of this paper is written in the convention of \eqref{eq:tractorconn}.

## technical
For a gravitational field on flat spacetime with derived metric $g$, the ambient bundle, the vectors $\sigma\nInf + \mu + \rho\nO$ of $\Cl(2,4)$, carries the canonical connection, on flat spacetime the $\Cl(2,4)$ gauge field $\Omega_{T}$, which reads $\nabla_a(\sigma, \mu_b, \rho) = (\nabla_a\sigma - \mu_a,\ \nabla_a\mu_b + g_{ab}\rho - P_{ab}\sigma,\ \nabla_a\rho + P_a{}^b\mu_b)$ in the scale $g$ and preserves the tractor metric. On a vacuum Einstein field with cosmological constant $\Lambda$, $P_{ab} = (\Lambda/6)\,g_{ab}$ and $J = 2\Lambda/3$, and the bundle carries a parallel section $I = (1, 0, \rho_I)$, the frozen point, whose parallelism is equivalent to the vacuum equations.

Here $\rho_I = J/n = \Lambda/6$ and $Q(I) = 2J/n = \Lambda/3$, so $I$ is null exactly when $\Lambda = 0$; for $\Lambda > 0$ its stabiliser is $SO(1,4)$ and $I^\perp$ has signature $(1,4)$. The sign of the norm and the relative sign of the Schouten slots are the series' conventions, fixed internally and shown not to be free.

## lay
In the series' language, a gravitational field on flat spacetime that describes empty space with a cosmological constant carries one distinguished vector of the six-dimensional conformal model, the frozen point, which stays fixed as the gravitational gauge fields carry it around. Its squared length is a third of the cosmological constant. When the constant is positive, the symmetries fixing the frozen point are those of de Sitter space. These facts are restated from earlier in the series.

## one-liner
For a vacuum Einstein field on flat spacetime the tractor gauge field has a parallel frozen point $I = \nInf + \tfrac{\Lambda}{6}\nO$ of squared norm $\Lambda/3$, with stabiliser $SO(1,4)$ for $\Lambda > 0$.
