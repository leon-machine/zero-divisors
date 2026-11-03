---
id: note.mass.setting-introduction
kind: note
version: 2
title: Introduction
status: setting
subject: einstein
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
comments_on:
- mass.imported-frozen-point-tractor-connection
locators:
  paper: T11
  number: Setting
  section: Introduction
  line: 372
extraction:
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
---

## formal
The action paper of this series builds the internal vector of gravity's MacDowell-Mansouri functional from the completion's frozen point, the parallel scale tractor $I$ whose squared norm is $\Lambda/3$: the Stelle-West vector is $V = X - (3/\Lambda)I$, made from $I$ and the canonical tractor $X$ \cite{ButlerT10}. That is the framework's account of what gravity is. This paper asks what mass is, and finds the same object at the centre of the answer twice: mass is the strength of a field's grip on the frozen point, measured once as a conformal weight read against the frozen point's length, and once as the length of a composite's momentum, which is the composite's grip on the same point. The paper proves each formula at the series' standard, computes the composite's mass in de Sitter space exactly, with the correction to the flat-space formula derived rather than estimated, and says precisely how the two readings meet: the flat formula is the squared pairing of the composite against the frozen point, and the dictionary then assigns the composite its weight.

The results come in three steps. \emph{The dictionary} (Section \ref{sec:dictionary}): a density of conformal weight $w$ coupled to the frozen point through the Thomas operator obeys the Klein-Gordon equation with
\[
m^{2} = -w(w+n-1)\,Q(I),
\]
in dimension four $m^{2} = -w(w+3)\Lambda/3$. With $H^{2} = \Lambda/3$ and $\Delta = -w$ this is the de Sitter mass formula $m^{2} = \Delta(3-\Delta)H^{2}$, and it carries its own classification: masslessness is $w \in \{0, -3\}$, the conformally coupled scalar $w = -1$ has $m^{2} = 2H^{2}$, a real weight gives $m^{2} \ge 0$ only for $w \in [-3, 0]$ and then $m \le 3H/2$, and every heavier field has complex weight $w = -\tfrac32 \pm i\nu$. Since $3H/2$ is about $10^{-33}\,\mathrm{eV}$, every known massive particle is of the last kind, with $\nu \approx m/H$, about $3 \times 10^{38}$ for the electron. The natural conjecture, that coupling to the frozen point explains the observed masses, fails: what the dictionary yields is the hierarchy problem restated as the size of an imaginary weight. \emph{The area} (Section \ref{sec:area}): a single twistor is massless; a two-twistor composite has $m^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$, the squared symplectic area between its constituents' spinor parts. \emph{The join} (Section \ref{sec:join}): the de Sitter scale in the flat conformal chart is $\sigma = 1 - \Lambda Q/12$, and its frozen point in the twistor chart is $I_{\Lambda} = n_{\infty} + (\Lambda/6)\,n_{0}$, derived rather than assumed. The composite's grip on it, the ambient vector $P = M(I_{\Lambda})$ built from the conformal moment map, is the de Sitter momentum, and its squared length is computed in closed form:
\[
m^{2} \;=\; 2\,|B_{\Lambda}|^{2} + Q(I_{\Lambda})\,C, \qquad B_{\Lambda} = \ip{I_{\Lambda}}{Z^{1}\wedge Z^{2}} = \br{\pi^{1}\pi^{2}} + \tfrac{\Lambda}{6}[\omega^{1}\omega^{2}],
\]
with $C$ the internal $\mathfrak{su}(2)$ Casimir of the two constituents. At $\Lambda = 0$ this is the area formula, now read as the squared pairing of the composite against the frozen point; for $\Lambda \neq 0$ the correction is a single term whose coefficient is the frozen point's norm. The composite's weight is then read off the dictionary: for every composite heavier than $3H/2$, $\mathrm{Re}\,w = -\tfrac32$ and $\mathrm{Im}\,w = m/H - \tfrac98 H/m + O((H/m)^{3})$. Section \ref{sec:gravity} assembles the results with the action paper, at declared levels: mass is coupling to the frozen point, gravity is the action of the frozen point, and the universality of free fall reads as the statement that the theory contains one scale-giving object.

## technical
pending

## lay
pending

## one-liner
pending
