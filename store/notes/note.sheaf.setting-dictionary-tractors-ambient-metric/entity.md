---
id: note.sheaf.setting-dictionary-tractors-ambient-metric
kind: note
version: 1
title: 'Dictionary: tractors and the ambient metric'
status: setting
subject: singularity
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
comments_on:
- sheaf.gauge-field-cometric
locators:
  paper: T04
  number: Setting
  section: Dictionary, choices, and scope
  line: 841
  subsection: 'Dictionary: tractors and the ambient metric'
---

## formal
The following correspondences are assembly-level: precise at the level of the structures named, with the differences stated, and with no claim of subsumption either way.

\emph{Tractor calculus} \cite{BEG1994, CurryGover2018} attaches to an $n$-dimensional conformal manifold of signature $(p,q)$ the standard tractor bundle $\mathcal{T}$, of rank $n + 2$ and signature $(p{+}1, q{+}1)$, with a composition series whose successive quotients are the density bundles $\Lambda^0[1]$, $T^*M[1]$, $\Lambda^0[-1]$, and a canonical (normal) tractor connection. The correspondences: the ambient bundle $T = T^*M \oplus \underline{\R}^2$ matches the underlying filtered bundle, with $\nO, \nInf$ the two weight lines (the ``point at zero'' and ``point at infinity'' slots of the conformal sphere model); the ambient form $h$ matches the tractor metric; the completion's increment $(p,q) \to (p{+}1,q{+}1)$ is the tractor increment. The differences: tractor calculus starts from a \emph{conformal class} on all of $M$ and its bundle carries a canonical connection; the present construction starts from a single \emph{degenerating} cometric, carries no distinguished connection (none is needed for the algebra), and its coupling is supported near the wall, where conformal rescaling is precisely what fails. The natural meeting point, flagged as a question rather than claimed: at a conformally regularised wall (the CCC picture \cite{Penrose2010}), the conformal class extends across $\Sig$ while the metric degenerates, and there the ambient sheaf should be canonically the tractor bundle of the extended class, with the coupling the almost-Einstein scale tractor; making that precise is successor work.

\emph{The Fefferman-Graham ambient metric} \cite{FG1985, FG2012} realises the same $(+1,+1)$ increment as a nondegenerate metric of signature $(p{+}1,q{+}1)$ on a thickening $\widetilde{M} \subset \R_+ \times M \times \R$ of the metric cone. The correspondence: the FG cone directions (the dilation and the transversal) match the hyperbolic plane $(\nO, \nInf)$; the FG normalisation (Ricci-flatness to infinite or determined order) plays the role that the coupling's collar normalisation plays here. The difference is categorical: FG produces a manifold with metric, this paper produces a bundle with form; the Clifford functor applied to the FG tangent bundle along the cone's zero section reproduces the fibres of the ambient sheaf, but the sheaf exists without any thickened manifold, which is what permits the degenerate locus to be handled at all.

## technical
pending

## lay
pending

## one-liner
pending
