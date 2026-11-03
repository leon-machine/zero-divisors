---
id: synthesis.imported-two-doublet-top-to-charged-higgs-width-ratio
kind: claim
version: 1
title: 'Imported: in a two-Higgs-doublet model at tree level, $\Gamma(t \to bH^{+})/\Gamma(t \to bW^{+}) = \cot^{2}\beta\,(1 - x)^{2}/((1 - y)^{2}(1 + 2y))$ with $x = m_{H^{\pm}}^{2}/m_{t}^{2}$, $y = M_{W}^{2}/m_{t}^{2}$, when the bottom-mass terms are neglected'
status: imported
region: synthesis
subject: standard-model
tags: [confronted-with-data, symmetry-breaking, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-01
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'H. E. Logan and D. MacLennan, Charged Higgs phenomenology in the flipped two Higgs doublet model, Phys. Rev. D 81 (2010), 075016, Appendix A, equations (A1) and (A2); arXiv:1002.4916.'
  key: LoganMacLennan2010
  doi: 10.1103/PhysRevD.81.075016
extraction:
  note: >-
    Imported so that the charged-pair result can pin the width ratio it uses instead of citing it from
    memory. Checked on 2026-11-01 against arXiv:1002.4916, Appendix A: equation (A1),
    Gamma(t -> W+ b) = G_F m_t/(8 sqrt2 pi) (m_t^2 + 2 M_W^2)(1 - M_W^2/m_t^2)^2, and equation (A2),
    Gamma(t -> H+ b) = G_F m_t/(8 sqrt2 pi) (m_t^2 cot^2 beta + m_b^2 tan^2 beta)(1 - M_H+^2/m_t^2)^2,
    stated at tree level with the final-state bottom mass neglected in the kinematics, for the type-II and
    flipped models; the DOI is that of the arXiv record. The ratio displayed here is those two formulas
    divided, with the m_b^2 term dropped. That in the type-I model the bottom coupling carries cot beta as
    well, so that the same ratio holds there with m_b neglected, is cited from memory and was not checked
    against the source.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (the two-doublet width ratio as a Fact, by Leon''s list of imports).'
---

## formal
In a two-Higgs-doublet model with ratio of vacuum values $\tan\beta$, in which the charged Higgs $H^{+}$ couples to $\bar{t}b$ through $m_{t}\cot\beta$ (the top Yukawa term) and $m_{b}\tan\beta$ (type II and flipped), at tree level and with the bottom mass neglected in the kinematics,
\[
\Gamma(t \to W^{+}b) = \frac{G_{F}m_{t}}{8\sqrt{2}\pi}\bigl(m_{t}^{2} + 2M_{W}^{2}\bigr)\Bigl(1 - \frac{M_{W}^{2}}{m_{t}^{2}}\Bigr)^{2}, \qquad
\Gamma(t \to H^{+}b) = \frac{G_{F}m_{t}}{8\sqrt{2}\pi}\bigl(m_{t}^{2}\cot^{2}\beta + m_{b}^{2}\tan^{2}\beta\bigr)\Bigl(1 - \frac{m_{H^{\pm}}^{2}}{m_{t}^{2}}\Bigr)^{2}.
\]
Dropping the $m_{b}^{2}$ term, which in type I carries $\cot^{2}\beta$ as well, the ratio is
\[
\frac{\Gamma(t \to bH^{+})}{\Gamma(t \to bW^{+})} = \cot^{2}\beta\,\frac{(1 - x)^{2}}{(1 - y)^{2}(1 + 2y)}, \qquad x = \frac{m_{H^{\pm}}^{2}}{m_{t}^{2}},\ y = \frac{M_{W}^{2}}{m_{t}^{2}},
\]
for $m_{H^{\pm}} < m_{t}$. \emph{Provenance:} \cite{LoganMacLennan2010} (equations (A1), (A2)).

## technical
A top quark decays almost always to a bottom quark and a $W$ boson. If a charged Higgs boson lighter than the top exists, the top can also decay to a bottom quark and the charged Higgs, at a rate set by the charged Higgs's coupling to the top and bottom. In a two-doublet model that coupling is the top's mass coupling times $\cot\beta$ (with a bottom-mass term that is negligible unless $\tan\beta$ is large), so the ratio of the two decay rates is $\cot^{2}\beta$ times a phase-space factor built from the masses of the top, the $W$ and the charged Higgs.

## lay
A top quark normally decays into a bottom quark and a W boson. If there were an electrically charged Higgs particle lighter than the top, some top quarks would decay into it instead. How often depends on how strongly the charged Higgs talks to the top and bottom quarks, and this formula gives the ratio of the two decay rates in the standard two-Higgs-field model.

## one-liner
Two-Higgs-doublet model, tree level, $m_{b}$ neglected: $\Gamma(t \to bH^{+})/\Gamma(t \to bW^{+}) = \cot^{2}\beta\,(1 - x)^{2}/((1 - y)^{2}(1 + 2y))$, $x = m_{H^{\pm}}^{2}/m_{t}^{2}$, $y = M_{W}^{2}/m_{t}^{2}$ (Logan and MacLennan, equations (A1), (A2)).
