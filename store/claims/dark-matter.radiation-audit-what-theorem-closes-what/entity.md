---
id: dark-matter.radiation-audit-what-theorem-closes-what
kind: claim
version: 7
title: 'The radiation audit: what the type-by-residue theorem closes, and what stays open'
status: proved
region: dark-matter
subject: dark-matter
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
  source: authorship disclosure of T14, deposited version
review: typed
derivations:
- name: main
  uses:
  - dark-matter.imported-eight-towers-mod-8-clock@4
  - dark-matter.mirror-tower-copy-one@8
  - dark-matter.open-channels-their-costs@5
  - dark-matter.projection-every-towers-content-dilutes-ones@3
  - dark-matter.seeding-gravity-floor-dark-towers-temperature@4
  - dark-matter.stored-asymmetry-charge-not-number@8
  - dark-matter.type-residue-what-each-tower-can@5
  - dark-matter.ceiling-valued-inherited-success@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:prop:audit
- kind: check
  ref: check.py::check_one_photon_like_species_breaks_the_cap
- kind: check
  ref: check.py::check_ground_level_and_vector_like_odd_towers
- kind: check
  ref: check.py::check_closing_margins_on_the_interval
- kind: check
  ref: check.py::check_mirror_atomic_cross_section
locators:
  paper: T14
  number: Prop 6.2
  label: prop:audit
  line: 554
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: one photon-like species 4.40-4.41 and five 22-22.1; intrinsic U(1) exactly at r = 3, 7; no chirality grading in odd dimension; closing margins on the interval (12, 8 and 7.3-7.4 orders); atomic cross-sections. Version 5 -> 6. Check strengthened: closing margins, the 7.4 rounding and the atomic cross-sections pinned to five or more figures; inputs moved to module level. Version 6 -> 7.'
  superseded_in_part_by:
  - dark-tower-matter.three-dimensional-phases
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: [1, 8]
    note: 'Decision 1: superseded in part by T14c Prop 9.1 (dark-tower-matter.three-dimensional-phases).
      Clause (2) said every compact U(1) in three dimensions confines by monopoles, with parity something
      to be imposed; T14c Prop 6.5(i) (dark-tower-matter.anomalies) forces half-integral bare Chern-Simons
      levels, and with them confinement holds in phase (C) only, phase (T) being topologically massive.
      Clause (2) and the conclusion are narrowed: the channel is closed in both phases, by confinement
      or by topological mass. A caveat also cites T14c Prop 8.2 (dark-tower-matter.mirrors-temperature-p2):
      the cold mirror the stance needs is an exception to P2. Decision 8: Hypothesis (U) enters only
      through the rung scale valued in the ceiling proposition, so the assumes edge to (U) is replaced
      by uses of dark-matter.ceiling-valued-inherited-success (cited in the proof at clause (4)); (U)
      still reaches this result through that proposition. Original in source_formal and orig-proof-main.tex.'
  source_formal: |-
    The cosmic microwave background caps extra relativistic energy at $\Delta\Neff \lesssim 0.3$ \cite{Planck2018}, and one massless photon-like species (two polarisations) at the visible temperature contributes $\Delta\Neff = (8/7)(11/4)^{4/3} \approx 4.4$, so five democratically filled sectors with such photons would contribute of order twenty. The audit proceeds tower by tower, at two levels fixed by Theorem \claimref{dark-matter.type-residue-what-each-tower-can} and Remark \ref{rem:flaglives}: the \emph{ground} level, where the type decides whether the tower's spinors carry an intrinsic $U(1)$ (exactly at the complex member of each odd pair, $r = 3, 7$ in the paper's convention), and the \emph{rung} level, where every flagged tower carries abelian charges from its ladder pairs.
    \begin{enumerate}
    \item \emph{(The mirror tower, $r = 2$.)} Open, by theorem: the mirror's derived content is a copy of ours (Theorem \claimref{dark-matter.mirror-tower-copy-one}), so it has a massless mirror photon and three light mirror neutrinos. The ground level is closed for the real member of the pair $\{2, 6\}$ (intrinsic group $\mathbb{Z}_{2}$, Theorem \claimref{dark-matter.type-residue-what-each-tower-can}(i); which member depends on the labelling convention, Proposition \claimref{dark-matter.towers-are-residues-single-clock-filter}) and irrelevant, since the content is not at that level. This is the mirror-matter situation of the literature, costed in Proposition \claimref{dark-matter.open-channels-their-costs}.
    \item \emph{(The three-dimensional towers, $r = 1, 7$.)} Closed at both levels, by Polyakov: vector-like (no chirality in odd dimension), so Dirac masses are unforbidden and, absent an imposed parity, generic; with no massless charged matter left, every compact $U(1)$ in three dimensions, the intrinsic one of the complex member of $\{1, 7\}$ (Theorem \claimref{dark-matter.type-residue-what-each-tower-can}(ii)) and the rung-level ones of both, confines by monopoles \cite{Polyakov1977}, and the non-abelian factors confine likewise.
    \item \emph{(The five-dimensional towers, $r = 3, 5$.)} Open at both levels: the complex member of the pair $\{3, 5\}$ carries an intrinsic $U(1)$ by theorem (Theorem \claimref{dark-matter.type-residue-what-each-tower-can}(ii); which member depends on the convention), both carry rung-level ones, no Polyakov mechanism exists in five dimensions, and by Lemma \claimref{dark-matter.projection-every-towers-content-dilutes-ones} a surviving photon dilutes as $a^{-4}$, exactly as ours.
    \item \emph{(The Goldstone exposure.)} Confining dark sectors with chiral breaking could leave massless dark pions. The framework supplies its own gap: any tower's accidental global symmetries are broken by its own tower's higher rungs (Fact \claimref{dark-matter.imported-eight-towers-mod-8-clock}), so the Goldstones are pseudo-Goldstones with masses of order $\Lambda_{\mathrm{conf}}^{2}/M_{\mathrm{rung}}$, the existence input a theorem and the mass estimate dimensional analysis.
    \end{enumerate}
    Conclusion: the three-dimensional towers are closed by theorem plus Polyakov; the mirror tower is open by theorem, with a known relativistic content, and closes only if it is cold; the five-dimensional towers are open with a content this paper does not derive. By Appendix \ref{app:seeding} (proved given the imported rate) every dark tower's temperature is bounded below by gravitational heating at a few parts in ten thousand of the visible temperature at the top of the ceiling range, and above by whatever energy the descent deposited, which the $\Neff$ cap limits to $0.448$ for the mirror and the paper's hot-deposit estimate puts near $4 \times 10^{-3}$ (Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}); across that interval both the mirror's channel and the five-dimensional towers' close by eight orders or more (twelve at the floor; the one case below eight is a nine-vector tower at the hot end, at $7.4$). $\Delta\Neff \approx 0$ is therefore a conditional stance, conditional on the open channels closing by one of the routes of Proposition \claimref{dark-matter.open-channels-their-costs} and on the deposit being no hotter than the estimate; so registered, and stated with that cost.

    On self-interaction: in the three-dimensional towers it is at composite strength if their matter is the confined charged matter the closure leaves, which the series does not establish (Section \ref{subsec:simulated}); in the five-dimensional ones it is undetermined; and for the mirror the composite figure is the wrong one, since mirror matter recombines at a visible temperature of order a keV (Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}) and enters structure formation as neutral mirror atoms, with an elastic cross-section per mass of order $2 \times 10^{8}$ (hydrogen) or $5 \times 10^{7}$ (helium) $\mathrm{cm^{2}\,g^{-1}}$, and as a plasma once ionised inside a halo: collisional and dissipative like our gas, tested by the collisional-fraction and dark-disk bounds of refutation item 6. The rung-breaking scale of channel (4) is valued in Proposition \claimref{dark-matter.ceiling-valued-inherited-success}.
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.open-channels-their-costs
    - dark-matter.seeding-gravity-floor-dark-towers-temperature
    - dark-matter.stored-asymmetry-charge-not-number
    - dark-matter.hyp-u-equal-rank-one-eigenvalues
    note: 'The four itemised clauses rest on the existing edges, but the conclusion''s temperature interval
      and conditional stance rest on the seeding floor (cited as the appendix), the hot-deposit estimate
      and the open-channel routes, so those three were added; the ceiling valuation and the residue-labelling
      proposition are context; the title still carries a LaTeX reference but is not a bare locator, so
      it was left. Hypothesis pass: assumes dark-matter.hyp-u-equal-rank-one-eigenvalues added because
      the paper names Hypothesis (U) as a condition of this result (the rung scale of channel (4), as
      the ceiling proposition states). Levels pass: all three levels now name Hypothesis (U) for the rung
      scale, and the lay and one-liner state both conditions of the stance (the open channels closing
      by a listed route, the deposit no hotter than the estimate).'
  env: proposition
  context_refs:
  - dark-matter.ceiling-valued-inherited-success
  - dark-matter.open-channels-their-costs
  - dark-matter.stored-asymmetry-charge-not-number
  - dark-matter.towers-are-residues-single-clock-filter
  unresolved_refs:
  - rem:flaglives
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.open-channels-their-costs
    - dark-matter.seeding-gravity-floor-dark-towers-temperature
    - dark-matter.stored-asymmetry-charge-not-number
    - dark-matter.hyp-u-equal-rank-one-eigenvalues
about:
- obj.dark-matter.spinor-module-type
---

## formal
The cosmic microwave background caps extra relativistic energy at $\Delta\Neff \lesssim 0.3$ \cite{Planck2018}, and one massless photon-like species (two polarisations) at the visible temperature contributes $\Delta\Neff = (8/7)(11/4)^{4/3} \approx 4.4$, so five democratically filled sectors with such photons would contribute of order twenty. The audit proceeds tower by tower, at two levels fixed by Theorem \claimref{dark-matter.type-residue-what-each-tower-can} and Remark \ref{rem:flaglives}: the \emph{ground} level, where the type decides whether the tower's spinors carry an intrinsic $U(1)$ (exactly at the complex member of each odd pair, $r = 3, 7$ in the paper's convention), and the \emph{rung} level, where every flagged tower carries abelian charges from its ladder pairs.
\begin{enumerate}
\item \emph{(The mirror tower, $r = 2$.)} Open, by theorem: the mirror's derived content is a copy of ours (Theorem \claimref{dark-matter.mirror-tower-copy-one}), so it has a massless mirror photon and three light mirror neutrinos. The ground level is closed for the real member of the pair $\{2, 6\}$ (intrinsic group $\mathbb{Z}_{2}$, Theorem \claimref{dark-matter.type-residue-what-each-tower-can}(i); which member depends on the labelling convention, Proposition \claimref{dark-matter.towers-are-residues-single-clock-filter}) and irrelevant, since the content is not at that level. This is the mirror-matter situation of the literature, costed in Proposition \claimref{dark-matter.open-channels-their-costs}.
\item \emph{(The three-dimensional towers, $r = 1, 7$.)} Closed at both levels: vector-like (no chirality in odd dimension), so Dirac masses are unforbidden and generic; with no massless charged matter left, each compact $U(1)$ in three dimensions, the intrinsic one of the complex member of $\{1, 7\}$ (Theorem \claimref{dark-matter.type-residue-what-each-tower-can}(ii)) and the rung-level ones of both, leaves no massless photon. The paper states that every such $U(1)$ confines by monopoles \cite{Polyakov1977}; with the half-integral bare Chern-Simons level that the parity anomaly forces (Proposition \claimref{dark-tower-matter.anomalies}(i)), that holds in the confining phase (C) only, and in phase (T) the photon is instead topologically massive (Proposition \claimref{dark-tower-matter.three-dimensional-phases}); both phases close the channel. The non-abelian factors confine.
\item \emph{(The five-dimensional towers, $r = 3, 5$.)} Open at both levels: the complex member of the pair $\{3, 5\}$ carries an intrinsic $U(1)$ by theorem (Theorem \claimref{dark-matter.type-residue-what-each-tower-can}(ii); which member depends on the convention), both carry rung-level ones, no Polyakov mechanism exists in five dimensions, and by Lemma \claimref{dark-matter.projection-every-towers-content-dilutes-ones} a surviving photon dilutes as $a^{-4}$, exactly as ours.
\item \emph{(The Goldstone exposure.)} Confining dark sectors with chiral breaking could leave massless dark pions. The framework supplies its own gap: any tower's accidental global symmetries are broken by its own tower's higher rungs (Fact \claimref{dark-matter.imported-eight-towers-mod-8-clock}), so the Goldstones are pseudo-Goldstones with masses of order $\Lambda_{\mathrm{conf}}^{2}/M_{\mathrm{rung}}$, the existence input a theorem and the mass estimate dimensional analysis.
\end{enumerate}
Conclusion: the three-dimensional towers are closed by theorem plus Polyakov confinement or, in phase (T), topological mass; the mirror tower is open by theorem, with a known relativistic content, and closes only if it is cold, which by Proposition \claimref{dark-tower-matter.mirrors-temperature-p2} is an exception to P2 (applied with the reach of Theorem \claimref{dark-matter.mirror-tower-copy-one}(iv), (v), P2 gives $\xi = 1$ and $\Delta\Neff = 7.45$); the five-dimensional towers are open with a content this paper does not derive. By Appendix \ref{app:seeding} (proved given the imported rate) every dark tower's temperature is bounded below by gravitational heating at a few parts in ten thousand of the visible temperature at the top of the ceiling range, and above by whatever energy the descent deposited, which the $\Neff$ cap limits to $0.448$ for the mirror and the paper's hot-deposit estimate puts near $4 \times 10^{-3}$ (Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}); across that interval both the mirror's channel and the five-dimensional towers' close by eight orders or more (twelve at the floor; the one case below eight is a nine-vector tower at the hot end, at $7.4$). $\Delta\Neff \approx 0$ is therefore a conditional stance, conditional on the open channels closing by one of the routes of Proposition \claimref{dark-matter.open-channels-their-costs} and on the deposit being no hotter than the estimate; so registered, and stated with that cost.

On self-interaction: in the three-dimensional towers it is at composite strength if their matter is the confined charged matter the closure leaves, which the series does not establish (Section \ref{subsec:simulated}); in the five-dimensional ones it is undetermined; and for the mirror the composite figure is the wrong one, since mirror matter recombines at a visible temperature of order a keV (Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}) and enters structure formation as neutral mirror atoms, with an elastic cross-section per mass of order $2 \times 10^{8}$ (hydrogen) or $5 \times 10^{7}$ (helium) $\mathrm{cm^{2}\,g^{-1}}$, and as a plasma once ionised inside a halo: collisional and dissipative like our gas, tested by the collisional-fraction and dark-disk bounds of refutation item 6. The rung-breaking scale of channel (4) is valued in Proposition \claimref{dark-matter.ceiling-valued-inherited-success}.

## technical
The microwave background caps extra relativistic energy at $\Delta N_{\mathrm{eff}} \lesssim 0.3$, while one two-polarisation photon-like species at the visible temperature contributes $\frac{8}{7}\left(\frac{11}{4}\right)^{4/3} \approx 4.4$. The audit runs tower by tower at the ground level, where an intrinsic $U(1)$ sits exactly at the complex member of each odd pair, and at the rung level, where every flagged tower carries abelian ladder charges. The mirror tower is open by theorem, its content copying ours; the three-dimensional towers are closed at both levels, since Dirac masses are unforbidden and each compact $U(1)$ then either confines by Polyakov's monopole mechanism or, in the topologically massive phase that the forced half-integral Chern-Simons level allows, has a gapped photon (the T14c note, Proposition \claimref{dark-tower-matter.three-dimensional-phases}, which corrects the paper's "every compact $U(1)$ confines" to phase (C)); the five-dimensional towers are open, a surviving photon diluting as $a^{-4}$; and any dark Goldstones are lifted by higher rungs to masses of order $\Lambda_{\mathrm{conf}}^{2}/M_{\mathrm{rung}}$, the rung scale being the ceiling proposition's, valued under Hypothesis (U).

Every dark tower's temperature lies between the gravitational heating floor, a few parts in ten thousand of ours at the top of the ceiling range, and the deposit, estimated near $4 \times 10^{-3}$; across that interval the open channels close by eight orders or more. So $\Delta N_{\mathrm{eff}} \approx 0$ is a conditional stance, conditional on the open channels closing by one of the listed routes and on the deposit being no hotter than the estimate. Caveat (T14c): a mirror that cold is an unstated exception to indifference, which applied with the copy theorem's reach gives $\xi = 1$ and $\Delta N_{\mathrm{eff}} = 7.45$ (Proposition \claimref{dark-tower-matter.mirrors-temperature-p2}).

## lay
Each hidden sector could carry its own kind of light, and observations rule out much extra light in the early universe. This audit checks every sector: the three-dimensional ones lose their light either through a known confinement effect or, as a later note (T14c) shows for one of their two possible phases, because the force carrier gains a mass, while the mirror and five-dimensional ones could keep theirs. Any leftover massless particles in the confining sectors pick up small masses from those sectors' higher rungs, at a scale set under Hypothesis (U). The open sectors would still be harmless if they started out no hotter than the framework's estimate and their light is removed by one of the listed routes, for instance by their being cold enough; so the stance of no detectable extra radiation holds only under those conditions. The same later note points out that a cold mirror is an unstated exception to the paper's indifference principle.

## one-liner
The three-dimensional towers' radiation channels close (by Polyakov confinement, or by topological mass in T14c's phase (T)), while the mirror and five-dimensional channels stay open, so, with the rung scale of Hypothesis (U), $\Delta N_{\mathrm{eff}} \approx 0$ is a conditional stance: it needs those channels to close by a listed route and the deposit to be no hotter than the estimate.
