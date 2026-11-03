---
id: obj.standard-model.one-threshold-spectrum-admissible
kind: object
version: 1
title: One-threshold spectrum; admissible
status: defined
region: standard-model
subject: standard-model
tags:
- running-and-unification
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
locators:
  paper: T12
  number: Def 8.4
  label: def:spectrum
  line: 1294
extraction:
  typing:
    by: ai-typing-pass
    note: Definition; no edges to type.
  env: definition
  context_refs:
  - standard-model.hypercharge-global-form-pair-counting-consistency
  - standard-model.imported-coefficient-sum-indices
  eqrefs: 1
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - standard-model.one-threshold-exact-criterion (about)
    - standard-model.table-exact (about)
    - standard-model.two-threshold-criterion (about)
    - standard-model.chain (about)
    - standard-model.direction-demanded-content-doublet-heavy (about)
    - standard-model.supersymmetric-row-two-loops (about)
    - refuted.the-desert-the-derived-content-alone-connects-th (about)
    added_about: []
    verdict: connected
    note: Added about from the six T12 results stated in terms of one-threshold spectra, admissibility
      and the threshold fraction, and from the refuted desert.
---

## formal
A \emph{one-threshold spectrum} consists of the derived content with one Higgs doublet, coefficients $b = (b_{1}, b_{2}, b_{3})$ (under Hypothesis (S) the content of Theorem \claimref{standard-model.hypercharge-global-form-pair-counting-consistency} with its lepton doublet, $b = (\tfrac{41}{10}, -\tfrac{19}{6}, -7)$, the value used throughout this section), active from $M_{Z}$ upward, together with further content, coefficient shifts $\Dl = (\Dl_{1}, \Dl_{2}, \Dl_{3})$ by Fact \claimref{standard-model.imported-coefficient-sum-indices}, active from a threshold $M_{I}$ upward. Write $x = \ln(M_{U}/M_{Z})/2\pi$ and $y = \ln(M_{U}/M_{I})/2\pi$, so that the one-loop equations read
\begin{equation}
a_{i}(M_{Z}) \;=\; a_{U} + b_{i}\,x + \Dl_{i}\,y, \qquad i = 1, 2, 3,
\end{equation}
with $a_{U}$ the common inverse coupling at $M_{U}$. The spectrum is \emph{admissible} for given record values $a_{i}(M_{Z})$ if \eqref{eq:run} has a solution with $x > 0$, $0 \le y \le x$ and $a_{U} > 0$: the couplings meet at one scale above $M_{Z}$, the threshold lies between $M_{Z}$ and $M_{U}$, and the unified coupling is positive. The \emph{threshold fraction} is $f = y/x = \ln(M_{U}/M_{I})/\ln(M_{U}/M_{Z})$. Write $b_{12} = b_{1} - b_{2}$, $b_{23} = b_{2} - b_{3}$, $\Dl_{12} = \Dl_{1} - \Dl_{2}$, $\Dl_{23} = \Dl_{2} - \Dl_{3}$, $D_{12} = a_{1} - a_{2}$ and $D_{23} = a_{2} - a_{3}$ at $M_{Z}$, and
\[
R \;=\; \frac{D_{12}}{D_{23}}, \qquad r_{0} \;=\; \frac{b_{12}}{b_{23}}, \qquad r_{\Dl} \;=\; \frac{b_{12} + \Dl_{12}}{b_{23} + \Dl_{23}}.
\]
$R$ is the record's ratio, $r_{0}$ the Standard Model's, $r_{\Dl}$ the ratio of the whole spectrum as if it were active from $M_{Z}$.

## technical
A one-threshold spectrum is the derived content with one Higgs doublet, with one-loop coefficients $b = (b_{1}, b_{2}, b_{3})$ active from $M_{Z}$ upward (under Hypothesis (S), $b = (\tfrac{41}{10}, -\tfrac{19}{6}, -7)$), plus further content that shifts the coefficients by $\Dl = (\Dl_{1}, \Dl_{2}, \Dl_{3})$ from a threshold $M_{I}$ upward. With $x = \ln(M_{U}/M_{Z})/2\pi$ and $y = \ln(M_{U}/M_{I})/2\pi$ the inverse couplings obey $a_{i}(M_{Z}) = a_{U} + b_{i}\,x + \Dl_{i}\,y$.

The spectrum is admissible for given record values $a_{i}(M_{Z})$ if these equations have a solution with $x > 0$, $0 \le y \le x$ and $a_{U} > 0$. The threshold fraction is $f = y/x$, and the ratios $R = D_{12}/D_{23}$ of the record, $r_{0} = b_{12}/b_{23}$ of the Standard Model and $r_{\Dl} = (b_{12} + \Dl_{12})/(b_{23} + \Dl_{23})$ of the whole spectrum as if active from $M_{Z}$ compare data with running.

## lay
This definition sets up a simple model of how the strengths of the three forces change with energy: the known particles act from low energy upward, and some extra particles join in above one threshold. The model counts as admissible if the three strengths meet at a single higher energy, with the threshold between the two scales and a positive common strength. A few ratios are defined to compare the measured couplings with what the running gives.

## one-liner
A one-threshold spectrum adds content at one threshold to the derived content's one-loop running, and is admissible when the couplings meet above $M_{Z}$ with the threshold in between and $a_{U} > 0$.
