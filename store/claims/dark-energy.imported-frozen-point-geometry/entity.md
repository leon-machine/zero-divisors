---
id: dark-energy.imported-frozen-point-geometry
kind: claim
version: 7
title: 'Imported: the frozen point and its geometry'
status: proved
region: dark-energy
subject: dark-energy
tags: [frozen-point, tractors, curvature-and-field-equations, rotors-and-stabilisers]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T10, deposited version
- name: Claude Opus 5.5
  role: 'the sentence naming the tractor gauge-field theorem made a text-only remark, at Leon''s second-round decisions'
  version: 7
  source: maintainer pass 2026-11-07 (decisions, second round)
review: typed
derivations:
- name: main
  uses:
  - dark-energy.imported-frozen-point-geometry-external@1
  - interior.covariant-form-vacuum-equations@5
  - interior.imported-tractor-connection@3
  - interior.non-null-stabilisers-section-they-act@5
  - interior.scale-tractor-leaves-cone@8
  - interior.sign-fixed-internally@5
  - interior.stabiliser-rotates-parabolic-reductive@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T10.py
  tags:
  - label:fact:frozen
- kind: check
  ref: check.py::check_tractor_gauge_field_reproduces_connection
- kind: check
  ref: check.py::check_vacuum_iff_null_scale_tractor_parallel
- kind: check
  ref: check.py::check_stabilisers_reductive_and_parabolic
locators:
  paper: T10
  number: Fact 2.1
  label: fact:frozen
  line: 625
extraction:
  maintainer_pass_decisions_2:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 6 -> 7. Leon''s second-round answer 6 (fix-F1.md For Leon item 2): the formal''s sentence naming Theorem synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection (the tractor connection as the flat-space gauge field D^T_a = a . nabla + Omega_T(a) x) is moved out of the Fact''s statement into a marked text-only remark after the provenance, because that theorem rests on this Fact through dark-energy.stelle-west-vector-frozen-point; the technical level, the proof''s opening, the lay ("the rule, the tractor connection") and the one-liner ("parallel for the tractor connection") follow. The Fact now states the connection only in its scale-g display. No edge existed or changes; check_tractor_gauge_field_reproduces_connection still compares the gauge field with the display (it tests the remark''s content against the Fact''s display, and its coverage clauses name the display).'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the tractor gauge field reproducing the connection on Kasner, matter and de Sitter fields, vacuum iff ninf parallel, and the reductive and parabolic stabilisers. Version 4 -> 5. Sample inputs moved to module level; no change to what is tested. Version 5 -> 6.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the invertible region is that of a gravitational field on flat spacetime, g its derived metric, the fibre the Cl(2,4) vectors and the connection the tractor gauge field (index display kept as its reading).'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  typing:
    by: ai-typing-pass
    note: 'A restatement of the geometry paper''s results; kept all six series premises and the external Gover entry, each matching a cited locator.'
  env: fact
  context_refs:
  - interior.covariant-form-vacuum-equations
  - interior.imported-tractor-connection
  - interior.non-null-stabilisers-section-they-act
  - interior.scale-tractor-leaves-cone
  - interior.sign-fixed-internally
  - interior.stabiliser-rotates-parabolic-reductive
  eqrefs: 1
  flags:
  - 'fact restating several series results: derived from them'
---

## formal
Let $g$ be the derived metric of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}). On the invertible region: the vacuum equations are exactly the covariant constancy of the null scale tractor $\nInf$; for the Einstein condition with $\Lambda \neq 0$ the parallel tractor has squared norm $Q(I) = \Lambda/3$, its stabiliser is the reductive de Sitter group $SO(1,4)$ (for $\Lambda > 0$; anti-de Sitter for $\Lambda < 0$), and the parabolic-to-reductive rotation of the stabiliser is proved with the sign fixed internally. The stabiliser of a non-null fibre vector of $\Cl(2,4)$ has dimension ten, with the orthogonal complement of the vector carrying the induced form of signature $(1,4)$ or $(2,3)$. In the scale $g$ the tractor connection is
\begin{equation}
\nabla_a(\sigma, \mu_b, \rho) \;=\; \bigl(\nabla_a\sigma - \mu_a,\;\; \nabla_a\mu_b + g_{ab}\,\rho - P_{ab}\,\sigma,\;\; \nabla_a\rho + P_a{}^{b}\mu_b\bigr),
\end{equation}
with $P_{ab}$ the Schouten tensor, $P_{ab} = (\Lambda/6)\,g_{ab}$ on the Einstein region, and it preserves \eqref{eq:tractormetric}. \emph{Provenance:} \cite[Fact~4.1, Thms.~4.5, 4.7, Props.~4.4, 4.10, Lem.~4.8]{ButlerT6}; the tractor connection and the almost-Einstein scale tractor are Gover's technology \cite{Gover2010}, as the geometry paper's Fact 4.1 records.

\emph{Remark (text only, not part of the Fact).} On flat spacetime this tractor connection is the gauge field $D^{T}_{a} = a \cdot \nabla + \Omega_{T}(a)\times$ of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}. That theorem rests on this Fact, through Lemma \claimref{dark-energy.stelle-west-vector-frozen-point}, so the Fact does not use it, and a result citing the Fact cannot take the gauge-field form from it.

## technical
On the invertible region of a gravitational field on flat spacetime the vacuum equations are exactly the covariant constancy of the null scale tractor. For the Einstein condition with $\Lambda\neq 0$ the parallel tractor $I$ has $Q(I) = \Lambda/3$ and stabiliser the reductive de Sitter group $SO(1,4)$ for $\Lambda > 0$, anti-de Sitter for $\Lambda < 0$, the parabolic-to-reductive rotation of the stabiliser being proved with the sign fixed internally. The stabiliser of a non-null fibre vector has dimension ten, and its orthogonal complement carries a form of signature $(1,4)$ or $(2,3)$.

The tractor connection reads in the scale $g$ as $\nabla_a(\sigma,\mu_b,\rho) = (\nabla_a\sigma - \mu_a,\ \nabla_a\mu_b + g_{ab}\rho - P_{ab}\sigma,\ \nabla_a\rho + P_a{}^b\mu_b)$, with Schouten tensor $P_{ab} = (\Lambda/6)g_{ab}$ on the Einstein region, and it preserves the tractor metric. The fact restates results of the geometry paper, with Gover's tractor technology as the external input. A remark, not part of the fact: on flat spacetime this connection is the $\Cl(2,4)$ gauge field $\Omega_{T}$ of the tractor gauge-field theorem, which itself rests on this fact.

## lay
This fact collects earlier results about the frozen point, a fixed direction in the six-dimensional conformal model attached to flat spacetime. Einstein's vacuum equations amount to this direction staying constant as the gravitational gauge fields carry it from place to place, and its length is set by the cosmological constant. The symmetries that leave it alone form the de Sitter group, or the anti-de Sitter group when the cosmological constant is negative. The fact also writes down the rule, the tractor connection, that says what constant means here.

## one-liner
On the invertible region of a gravitational field on flat spacetime the Einstein condition makes the scale tractor parallel for the tractor connection, with $Q(I) = \Lambda/3$, stabiliser $SO(1,4)$ or $SO(2,3)$, and $P_{ab} = (\Lambda/6)g_{ab}$.
