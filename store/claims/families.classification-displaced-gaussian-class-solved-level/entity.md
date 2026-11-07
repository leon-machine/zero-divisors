---
id: families.classification-displaced-gaussian-class-solved-level
kind: claim
version: 3
title: 'The displaced-Gaussian class, at its weakest clause, derives no lepton spectrum'
status: proved
region: families
subject: generations
tags: [classification, flavour-and-mixing, pairing-and-bogoliubov]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
review: typed
derivations:
- name: main
  uses:
  - families.rigidity-pairing-sector-one-event@4
  - families.skeleton-rank-one-plus-ordering-shift@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_family_factor_doubly_degenerate
- kind: check
  ref: check.py::check_light_pair_exactly_degenerate
- kind: check
  ref: check.py::check_quoted_figures_consistent
- kind: proof
  derivation: main
locators:
  paper: T13
  number: Prop 6.4
  label: prop:classification
  line: 851
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: clause (1): G G^dagger spectrum {|a|^2, |a|^2, 0} and the exactly degenerate light pair of H for every pairing and depth, plus the consistency of the quoted factor 172. Version 1 -> 2. Sample inputs moved to module level; no change to what is tested (the quoted 206.77 and 1.2032 are module constants, and ''rounds to 172'' is written as round(ratio) == 172). Version 2 -> 3.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'Both edges are the premises of clause (1) and were kept; clauses (2)-(3) are preliminary computations
      not reproduced in the store, so the proved status rests on the paper''s level-of-weakest-clause
      convention, which is a doubt. Levels pass: lay now says the conclusion holds only at the level of
      the preliminary clauses; status left unchanged as the pass requires, though review item 5 flags
      it as below proof.'
---

## formal
The candidate inventory for the $S_{2} \to 1$ splitting within the displaced-Gaussian class of the six-mode face algebra has three entries, of which the first is closed by theorem and the other two by flagged preliminary computation:
\begin{enumerate}
\item \emph{(More pairing channels: closed by theorem.)} By Proposition \claimref{families.rigidity-pairing-sector-one-event} and Theorem \claimref{families.skeleton-rank-one-plus-ordering-shift}, every antisymmetric pairing is one fourfold-degenerate event with an exactly degenerate light pair. No pairing the descent can write splits the degenerate pair.
\item \emph{(The symmetric-spinor noise channel: preliminary computation.)} Preliminary computation by the methods of this section, in a displaced-Gaussian computation checked against exact Fock-space evaluation, indicates that the one pairing outside the $\varepsilon$-sector splits the pair but cannot reach the physical ratio pair $(m_{\mu}/m_{e}, m_{\tau}/m_{\mu}) = (206.77, 16.82)$: the best attainable point found is $(101, 19)$, far from Koide, with the deformation of $Q$ excluding the route along the way. The scan is not reproduced by this paper's script and the clause carries that level.
\item \emph{(The condensate means: preliminary computation.)} The same computation indicates that nonzero means with the flag-forced equal-amplitude form cap the split at $1.2032$, short of $206.77$ by a factor of $172$; and that with free amplitudes the physical spectrum is reachable exactly at every depth, with the solution itself showing why: the required leg asymmetry is $g_{1}/g_{2} \approx 207.5$, the muon-electron ratio relabelled, with sensitivity of the predicted split to the free parameter exactly $1$ and the heavy mass not responding at all. A mechanism whose parameters are the answer derives nothing. Same level as (2).
\end{enumerate}
The terminal statement, at the level of its weakest clause: the displaced-Gaussian class is solved; its entire output is the rank-one-plus-shift skeleton (rigidly one event, $S_{2}$-exact, by theorem), bounded Koide-incompatible perturbations of it, and free mean textures that are the mass data under another name. The physical charged-lepton spectrum lies in the class only as a relabelling of itself. The remaining route is named and constrained: a non-Gaussian frozen vacuum or a larger algebra, required to produce the number $207$ from caused structure, with the relabelling signature (unit sensitivity to a free parameter) as the refutation condition on every future candidate.

## technical
Within the displaced-Gaussian class of the six-mode face algebra the candidates for splitting the degenerate light pair ($S_{2} \to 1$) are three. Antisymmetric pairings are closed by theorem: by the rigidity of the pairing sector and the skeleton, every such pairing is one fourfold-degenerate event and the light eigenvalue $\cosh^{2}r$ stays doubly degenerate. The symmetric-spinor noise channel and nonzero condensate means are closed only by flagged preliminary computation: the noise channel splits the pair but its best point found is $(101, 19)$ against the physical $(206.77, 16.82)$; equal-amplitude means cap the split at $1.2032$, and free amplitudes reach the spectrum only with leg asymmetry $g_{1}/g_{2} \approx 207.5$, the muon-electron ratio relabelled, with unit sensitivity to that parameter.

The terminal statement holds at the level of its weakest clause: the class outputs the rank-one-plus-shift skeleton, bounded Koide-incompatible perturbations of it, and free textures that restate the data. The remaining route, a non-Gaussian frozen vacuum or a larger algebra, must produce $207$ from caused structure, with unit sensitivity to a free parameter as the refutation condition on any candidate.

## lay
The paper asks whether any version of its simplest class of vacuum states can explain why the electron and the muon have such different masses. One option is ruled out by proof; the other two are ruled out by preliminary calculations that the paper flags as such. They either cannot reach the observed mass ratios or reach them only by building the answer into a free parameter, which explains nothing. The conclusion, which is only as firm as those preliminary calculations, is that something beyond this class is needed, together with a test that any future proposal must pass.

## one-liner
At the level of its preliminary clauses, the displaced-Gaussian class yields only the unbreakable skeleton, bounded Koide-incompatible perturbations and textures that relabel the data, so the charged-lepton spectrum is not derived within it.
