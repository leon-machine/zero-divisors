---
id: note.simulations.setting-smoothed-particle-hydrodynamics
kind: note
version: 1
title: Smoothed-particle hydrodynamics
status: setting
subject: dark-matter
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14b, deposited version
comments_on:
- simulations.averaged-pair-operator
locators:
  paper: T14b
  number: Setting
  section: The simulation code
  line: 269
  subsection: Smoothed-particle hydrodynamics
---

## formal
Each fluid species has its own tree. The kernel is the cubic spline of support $2h$ \cite{MonaghanLattanzio1985},
\[
W(r, h) = \frac{1}{\pi h^{3}}
\begin{cases}
1 - \tfrac{3}{2}q^{2} + \tfrac{3}{4}q^{3}, & 0 \le q < 1,\\[2pt]
\tfrac{1}{4}(2 - q)^{3}, & 1 \le q < 2,\\[2pt]
0, & q \ge 2,
\end{cases}
\qquad q = r/h ,
\]
normalised so that $\int W\,d^{3}r = 1$. Density is gathered at each particle's own smoothing length, $\rho_{i} = \sum_{j} m_{j}W(r_{ij}, h_{i})$; pressure and sound speed are $P_{i} = (\gamma - 1)\rho_{i}u_{i}$ and $c_{i} = \sqrt{\gamma(\gamma - 1)u_{i}}$. The next smoothing length is
\[
h_{i} = \tfrac{1}{2}\Bigl(\frac{3N_{\mathrm{ngb}}m_{i}}{4\pi\rho_{i}}\Bigr)^{1/3}, \qquad N_{\mathrm{ngb}} = 40,
\]
limited to a change between $0.8$ and $1.25$ per step, floored at $h_{\min} = 10\ \kpc$, and cut to $0.7h_{i}$ if a particle's neighbour list reaches its cap of $2000$.

The equations of motion are the symmetric form \cite{Monaghan1992},
\begin{align*}
\frac{d\mathbf{v}_{i}}{dt} &= -\sum_{j} m_{j}\Bigl(\frac{P_{i}}{\rho_{i}^{2}} + \frac{P_{j}}{\rho_{j}^{2}} + \Pi_{ij}\Bigr)\,\mathbf{g}_{ij},
\\
\frac{du_{i}}{dt} &= \sum_{j} m_{j}\Bigl(\frac{P_{i}}{\rho_{i}^{2}} + \tfrac{1}{2}\Pi_{ij}\Bigr)\,\mathbf{v}_{ij}\cdot\mathbf{g}_{ij},
\end{align*}
with the kernel gradient averaged over the two smoothing lengths, $\mathbf{g}_{ij} = \tfrac{1}{2}\bigl(\nabla_{i}W(r_{ij}, h_{i}) + \nabla_{i}W(r_{ij}, h_{j})\bigr)$, and $\mathbf{v}_{ij} = \mathbf{v}_{i} - \mathbf{v}_{j}$. The artificial viscosity acts on approaching pairs \cite{MonaghanGingold1983}:
\[
\Pi_{ij} = \frac{-\alpha\,\bar{c}_{ij}\mu_{ij} + \beta\mu_{ij}^{2}}{\bar{\rho}_{ij}}, \qquad
\mu_{ij} = \frac{\bar{h}_{ij}\,\mathbf{v}_{ij}\cdot\mathbf{r}_{ij}}{r_{ij}^{2} + 0.01\bar{h}_{ij}^{2}} \quad (\mathbf{v}_{ij}\cdot\mathbf{r}_{ij} < 0),
\]
with $\alpha = 1$, $\beta = 2$ and bars denoting pair means. Internal energy is floored at $u_{\mathrm{floor}} = u(10^{4}\ \mathrm{K})$ for mean particle mass $0.6\,m_{p}$.

## technical
pending

## lay
pending

## one-liner
pending
