---
id: standard-model.imported-two-loop-gauge-coefficients
kind: claim
version: 1
title: 'Imported: the two-loop gauge coefficients'
status: imported
region: standard-model
subject: standard-model
tags: [classical-theorem, running-and-unification]
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
- citation: M. E. Machacek and M. T. Vaughn, Two-loop renormalization group equations in a general quantum
    field theory (I). Wave function renormalization, Nucl. Phys. B 222 (1983) 83--103.
  key: MachacekVaughn1983
- citation: S. P. Martin and M. T. Vaughn, Two-loop renormalization group equations for soft supersymmetry-breaking
    couplings, Phys. Rev. D 50 (1994) 2282--2292.
  key: MartinVaughn1994
- citation: S. Navas et al. (Particle Data Group), Review of particle physics, Phys. Rev. D 110 (2024),
    030001.
  key: PDG2024
locators:
  paper: T12
  number: Fact 8.18
  label: fact:twoloop
  line: 1467
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: Imported fact; levels only, no edges to review.
---

## formal
In $\beta(g_{i}) = \dfrac{g_{i}^{3}}{16\pi^{2}}\Bigl(b_{i} + \dfrac{1}{16\pi^{2}}\sum_{j} B_{ij}\,g_{j}^{2} - \dfrac{c_{i}\,y_{t}^{2}}{16\pi^{2}}\Bigr)$, the two-loop matrix for Weyl fermions in representations $R$ and complex scalars in representations $S$ of a product of simple factors and a $\mathrm{U}(1)$ is
\begin{align*}
B_{ij} \;=\; {}& \delta_{ij}\Bigl(-\tfrac{34}{3}C(G_{i})^{2} + \tfrac{10}{3}C(G_{i})\textstyle\sum_{R} T_{i}(R) + \tfrac{2}{3}C(G_{i})\sum_{S} T_{i}(S)\Bigr) \\
& + 2\textstyle\sum_{R} T_{i}(R)C_{j}(R) + 4\sum_{S} T_{i}(S)C_{j}(S),
\end{align*}
with $T_{i}$ the index weighted by the dimensions of the other factors and $C_{j}$ the quadratic Casimir ($\tfrac35 Y^{2}$ for the $\mathrm{U}(1)$), gauge Yukawas excluded; for a supersymmetric theory with chiral superfields $\Phi$ it is $B_{ij} = \delta_{ij}\bigl(-6C(G_{i})^{2} + 2C(G_{i})\sum_{\Phi} T_{i}\bigr) + 4\sum_{\Phi} T_{i}C_{j}$. The Standard Model's matrix is $\bigl[\begin{smallmatrix} 199/50 & 27/10 & 44/5 \\ 9/10 & 35/6 & 12 \\ 11/10 & 9/2 & -26 \end{smallmatrix}\bigr]$ and the minimal supersymmetric one $\bigl[\begin{smallmatrix} 199/25 & 27/5 & 88/5 \\ 9/5 & 25 & 24 \\ 11/5 & 9 & 14 \end{smallmatrix}\bigr]$; the top-Yukawa coefficients are $c = (\tfrac{17}{10}, \tfrac32, 2)$ and $(\tfrac{26}{5}, 6, 4)$, and $y_{t}$ runs at one loop with $\beta(y_{t}) = \dfrac{y_{t}}{16\pi^{2}}\bigl(\tfrac92 y_{t}^{2} - \tfrac{17}{20}g_{1}^{2} - \tfrac94 g_{2}^{2} - 8g_{3}^{2}\bigr)$ below and $\dfrac{y_{t}}{16\pi^{2}}\bigl(6y_{t}^{2} - \tfrac{13}{15}g_{1}^{2} - 3g_{2}^{2} - \tfrac{16}{3}g_{3}^{2}\bigr)$ above the threshold. \emph{Provenance:} \cite{MachacekVaughn1983, MartinVaughn1994}; the record's central values and uncertainties $\alpha^{-1}_{\mathrm{em}}(M_{Z}) = 127.951$, $\sin^{2}\theta_{W} = 0.23122 \pm 0.00004$, $\alpha_{s} = 0.1180 \pm 0.0009$ from \cite{PDG2024}.

## technical
With $\beta(g_{i}) = \tfrac{g_{i}^{3}}{16\pi^{2}}\bigl(b_{i} + \tfrac{1}{16\pi^{2}}\sum_{j}B_{ij}g_{j}^{2} - \tfrac{c_{i}y_{t}^{2}}{16\pi^{2}}\bigr)$, the two-loop matrix for Weyl fermions $R$ and complex scalars $S$ is $B_{ij} = \delta_{ij}\bigl(-\tfrac{34}{3}C(G_{i})^{2} + \tfrac{10}{3}C(G_{i})\sum_{R}T_{i}(R) + \tfrac23 C(G_{i})\sum_{S}T_{i}(S)\bigr) + 2\sum_{R}T_{i}(R)C_{j}(R) + 4\sum_{S}T_{i}(S)C_{j}(S)$, with gauge Yukawas excluded, and a corresponding formula holds for chiral superfields.

The fact records the resulting matrices for the Standard Model and its minimal supersymmetric extension, the top-Yukawa coefficients $c$, the one-loop running of $y_{t}$ below and above the threshold, and the record inputs $\alpha_{\mathrm{em}}^{-1}(M_{Z}) = 127.951$, $\sin^{2}\theta_{W} = 0.23122 \pm 0.00004$ and $\alpha_{s} = 0.1180 \pm 0.0009$. All of it is imported from the two-loop literature and the particle data record.

## lay
Beyond the first approximation, the way each force's strength changes with energy also depends on the strengths of the other forces and on the top quark's coupling to the Higgs field. This standard result gives the general formula for those corrections, the specific numbers for the Standard Model and its minimal supersymmetric extension, and the measured values the running starts from. It is taken from the literature.

## one-liner
The standard two-loop gauge coefficients $B_{ij}$, top-Yukawa corrections and record input values for the Standard Model and its minimal supersymmetric extension.
