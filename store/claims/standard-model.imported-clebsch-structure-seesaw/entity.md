---
id: standard-model.imported-clebsch-structure-seesaw
kind: claim
version: 1
title: 'Imported: the Clebsch structure and the seesaw'
status: imported
region: standard-model
subject: generations
tags: [classical-theorem, seesaw-and-majorana, flavour-and-mixing]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
imported_from:
- citation: R. Slansky, Group theory for unified model building, Phys. Rep. 79 (1981) 1--128.
  key: Slansky1981
- citation: H. Georgi and C. Jarlskog, A new lepton-quark mass relation in a unified theory, Phys. Lett.
    B 86 (1979) 297--300.
  key: GeorgiJarlskog1979
locators:
  paper: T12
  number: Fact 11.1
  label: fact:clebsch
  line: 2027
extraction:
  env: fact
  context_refs:
  - families.doublet-direction-module-georgi-jarlskog-clebsch
  - standard-model.chain
  outside_pilot_cites:
  - ButlerT15
  typing:
    by: ai-typing-pass
    note: Levels only; imported claim with no derivations.
---

## formal
With Yukawa matrices $Y_{a}$ for the $10$s, $f$ for one $126$ and $h$ for one $120$, the Dirac mass matrices at $M_{I}$, where $\su(4)$ still relates quarks to leptons, are
\begin{align*}
M_{u} &= \textstyle\sum_{a} v^{a}_{u}Y_{a} + w_{u}f + c_{u}h, & M_{\nu} &= \textstyle\sum_{a} v^{a}_{u}Y_{a} - 3w_{u}f + c_{\nu}h, \\
M_{d} &= \textstyle\sum_{a} v^{a}_{d}Y_{a} + w_{d}f + c_{d}h, & M_{e} &= \textstyle\sum_{a} v^{a}_{d}Y_{a} - 3w_{d}f + c_{e}h,
\end{align*}
with complex vevs and the four coefficients of the $120$ independent (it carries two pairs of doublets, with lepton-to-quark Clebsches $1$ and $-3$). The right-handed neutrinos have the Majorana matrix $M_{R} = v_{R}f$, and the light neutrinos have $m_{\nu} = -M_{\nu}M_{R}^{-1}M_{\nu}^{T}$, the type-I seesaw. On the chain of Proposition \claimref{standard-model.chain} the $126$'s left triplet sits near $M_{U}$, so its contribution to $m_{\nu}$ is of order $v^{2}v_{R}/M_{U}^{2} \sim 10^{-9}$ eV and is dropped. \emph{Provenance:} \cite{Slansky1981} for the decomposition, the factor $-3$ being Georgi and Jarlskog's \cite{GeorgiJarlskog1979} and Fact \claimref{families.doublet-direction-module-georgi-jarlskog-clebsch}'s on the module; the seesaw as the neutrino paper T15 \cite{ButlerT15} uses it; assembly level.

## technical
With Yukawa matrices $Y_{a}$ for the $10$s, $f$ for one $126$ and $h$ for one $120$, the Dirac mass matrices at $M_{I}$, where $\su(4)$ still relates quarks to leptons, take the standard unified form, for example $M_{e} = \sum_{a} v^{a}_{d}Y_{a} - 3w_{d}f + c_{e}h$ against $M_{d} = \sum_{a} v^{a}_{d}Y_{a} + w_{d}f + c_{d}h$: the $10$s contribute equally to leptons and quarks, the $126$ with the Georgi-Jarlskog factor $-3$, and the $120$ with independent coefficients.

The right-handed neutrinos have the Majorana matrix $M_{R} = v_{R}f$, and the light neutrinos follow from the type-I seesaw $m_{\nu} = -M_{\nu}M_{R}^{-1}M_{\nu}^{T}$; on the chain the $126$'s left-triplet contribution, of order $10^{-9}$ eV, is dropped.

## lay
This is the standard bookkeeping from grand unified theories for how three kinds of Higgs field feed masses to quarks and leptons, including the factor of minus three that separates leptons from quarks for one of them. It also includes the seesaw, in which very heavy right-handed neutrinos make the ordinary neutrinos very light. The paper takes these formulas from the literature rather than deriving them.

## one-liner
Imported from the unified-theory literature: the $10$, $126$ and $120$ Clebsch structure of the Dirac mass matrices at $M_{I}$, with the type-I seesaw for the light neutrinos.
