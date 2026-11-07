---
id: odd-extensions.imported-frozen-point
kind: claim
version: 8
title: 'Imported: the frozen point'
status: proved
region: odd-extensions
subject: dark-energy
tags: [frozen-point, rotors-and-stabilisers, tractors]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14a, deposited version
- name: Claude Opus 5.5
  role: 'consistency pass, notation clash in the soldering form resolved'
  version: 7
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: consistency pass, the sign of l^2 named on the anti-de Sitter branch
  version: 8
  source: maintainer pass 2026-11-07 (consistency, small items)
review: typed
derivations:
- name: main
  uses:
  - dark-energy.frozen-point-makes-stelle-west-vector@7
  - dark-energy.imported-frozen-point-geometry@7
  - odd-extensions.imported-frozen-point-external@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_frozen_point_norm_complement_stabiliser_both_signs
- kind: check
  ref: check.py::check_stelle_west_vector_and_lorentz_stabiliser
- kind: check
  ref: check.py::check_soldering_form_and_reduced_connection
locators:
  paper: T14a
  number: Fact 1.5
  label: fact:frozen
  line: 423
extraction:
  maintainer_pass_small_items:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'l^2 = -Q(V) = 3/Lambda with its sign named (negative for Lambda < 0) in formal and technical. Store reading. Version 7 -> 8.'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review (second round): dark-energy.imported-frozen-point-geometry repinned 6 -> 7 after reviewing its restatement (the sentence naming the tractor gauge-field theorem moved to a text-only remark); the parts cited here (parallel frozen point, Q(I) = Lambda/3, the stabilisers, the scale-g display and the Schouten tensor) are unchanged, and the use here holds as cited.'
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The soldering form was written e^mu = hb^{-1}(e^mu), one symbol for two objects (the physical frame and the background frame); it is now the map a -> hb^{-1}(a) and the translation part hb^{-1}(a) ^ V/Q(V), as in dark-energy.imported-macdowell-mansouri-theorem-stelle-west; notation only.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Translation part corrected to e^mu ^ V/Q(V) = -e^mu ^ V/l^2 (was e^mu ^ V/l; checked exactly at four values of Lambda, and as clause (v) of the GTG tractor result); also own exact check added: Q(I) = Lambda/3 with I^perp (1,4) or (2,3) and its stabiliser, the Stelle-West vector with Q(V) = -3/Lambda and Lorentz stabiliser of {I,V}^perp, D^T V = hb^{-1}(a), and the reduced connection Omega(a) - hb^{-1}(a) ^ V/l^2. Version 4 -> 5. check.py docstring: deleted stale note about e^mu ^ V/l (fix round 2026-10-23). Version 5 -> 6.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the invertible region is that of a gravitational field on flat spacetime, the tractor metric the square of Cl(2,4), and the soldering form the physical frame hb^{-1}(a), so that the reduced connection is Omega(a) - hb^{-1}(a) ^ V/l^2 in the store normalisation; content unchanged.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: fact
  context_refs:
  - dark-energy.frozen-point-makes-stelle-west-vector
  - dark-energy.imported-frozen-point-geometry
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'Fact restating the dark-energy paper''s Fact 2.1 and Theorem 3.1 (both premises, kept) with
      the external MacDowell-Mansouri and Stelle-West ingredients; no standard-route derivation, since
      the external construction is already a premise of the main derivation. Levels pass: the lay said
      the cosmological constant is the frozen point''s squared length, but $Q(I) = \Lambda/3$, so it now
      says a third, and it and the one-liner keep the invertible-region and nonzero-Lambda conditions.'
---

## formal
On the invertible region of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) with $\Lambda \neq 0$, the parallel scale tractor $I$ has squared norm $Q(I) = \Lambda/3$ in the tractor metric of signature $(2,4)$, the square of $\Cl(2,4)$; its orthogonal complement $I^{\perp}$ is a rank-five bundle carrying the induced form of signature $(1,4)$ for $\Lambda > 0$ and $(2,3)$ for $\Lambda < 0$, with stabiliser $SO(1,4)$ or $SO(2,3)$; the Stelle-West vector $V$ is a section of $I^{\perp}$ of squared norm $-3/\Lambda$, its stabiliser is the Lorentz group of $\{I, V\}^{\perp}$, of signature $(1,3)$, and its covariant derivative is the soldering form, the physical frame $a \mapsto \hb^{-1}(a)$ of the gravitational field, so that in the gauge where $V$ is constant the reduced connection splits as a Lorentz connection, the rotation-gauge field $\Omega$, plus the translation part $\hb^{-1}(a)\wedge V/Q(V) = -\hb^{-1}(a)\wedge V/\ell^{2}$ ($\ell^{2} = -Q(V) = 3/\Lambda$, negative for $\Lambda < 0$). \emph{Provenance:} \cite[Fact~2.1, Thm.~3.1]{ButlerT10}; the construction is MacDowell and Mansouri's \cite{MacDowellMansouri1977} in Stelle and West's form \cite{StelleWest1980}.

## technical
On the invertible region of a gravitational field on flat spacetime with $\Lambda \neq 0$ the parallel scale tractor $I$ satisfies $Q(I) = \Lambda/3$ in the tractor metric of signature $(2,4)$. Its orthogonal complement $I^{\perp}$ is a rank-five bundle of signature $(1,4)$ when $\Lambda > 0$ and $(2,3)$ when $\Lambda < 0$, with stabiliser $SO(1,4)$ or $SO(2,3)$.

The Stelle-West vector $V$ is a section of $I^{\perp}$ with $Q(V) = -3/\Lambda$; its stabiliser is the Lorentz group of $\{I,V\}^{\perp}$, of signature $(1,3)$, and its covariant derivative is the soldering form, the physical frame of the gravitational field. In the gauge where $V$ is constant the reduced connection splits as the rotation-gauge field $\Omega$ plus the translation part $\hb^{-1}(a)\wedge V/Q(V) = -\hb^{-1}(a)\wedge V/\ell^{2}$ ($\ell^{2} = -Q(V) = 3/\Lambda$, negative for $\Lambda < 0$). The construction is MacDowell and Mansouri's in Stelle and West's form, as established in the series' dark-energy paper.

## lay
Where the cosmological constant is nonzero, and on the region where the gravitational field on flat spacetime can be inverted, a third of it is the squared length of a fixed reference vector called the frozen point. Fixing that vector cuts the theory's larger symmetry down to a de Sitter or anti-de Sitter symmetry, depending on the sign. A second vector built alongside it, the Stelle-West vector, cuts it down further to the ordinary Lorentz symmetry and splits the gauge field into a rotation part, gravity's own rotation field, and a translation part, its frame. This is a known construction, imported here from earlier work.

## one-liner
On the invertible region with $\Lambda \neq 0$ the frozen point $I$, with $Q(I) = \Lambda/3$, and the Stelle-West vector $V$, with $Q(V) = -3/\Lambda$, reduce the $(2,4)$ tractor geometry to de Sitter or anti-de Sitter and then to Lorentz symmetry, splitting the tractor gauge field into $\Omega$ and the frame part $\hb^{-1}(a)\wedge V/Q(V) = -\hb^{-1}(a)\wedge V/\ell^{2}$ ($\ell^{2} = -Q(V) = 3/\Lambda$, negative for $\Lambda < 0$).
