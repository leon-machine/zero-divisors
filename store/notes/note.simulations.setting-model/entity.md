---
id: note.simulations.setting-model
kind: note
version: 1
title: The model
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
- simulations.mirror-galaxy
locators:
  paper: T14b
  number: Setting
  section: The mirror in the Galaxy
  line: 539
  subsection: The model
---

## formal
One Milky Way halo is shared by both sectors: the same growth, potential and spin. Its growth follows the Fakhouri-Ma-Boylan-Kolchin rate \cite{Fakhouri2010},
\[
\frac{dM}{dt} = A\Bigl(\frac{M}{10^{12}\Msun}\Bigr)^{1.1}(1 + bz)\sqrt{\Omega_{m}(1+z)^{3} + \Omega_{\Lambda}},
\]
with $(A, b) = (46.1\ \Msun/\mathrm{yr}, 1.11)$ (mean) or $(25.3, 1.65)$ (median). Each sector accretes its baryon share $f_{b}\,dM$ ($f_{b} = \Omega_{b}/\Omega_{m} = 0.1565$) into a hot halo, an isothermal sphere $\rho_{g}(r) = m_{\mathrm{hot}}/(4\pi Rr^{2})$ at the virial temperature $T = \mu m_{p}V^{2}/2k$ of its own composition. Following Croton et al.\ \cite{Croton2006}, with their parameter values, and with $R$ and $V$ the halo's virial radius and circular velocity, $m_{\mathrm{hot}}$ and $m_{\mathrm{cold}}$ the hot and cold gas masses, $r_{\mathrm{cool}}$ the radius at which the cooling time equals the reference time, and $\lambda$ the spin parameter:
\begin{align*}
t_{\mathrm{cool}}(r_{\mathrm{cool}}) &= t_{\mathrm{dyn}} = R/V \quad (\text{or the cosmic time}),\\
\dot m_{\mathrm{cool}} &= \tfrac{1}{2}m_{\mathrm{hot}}\frac{r_{\mathrm{cool}}}{R}\frac{V}{R} \quad (\text{all hot gas per } t_{\mathrm{dyn}} \text{ if } r_{\mathrm{cool}} > R),\\
\dot m_{*} &= \alpha\,\frac{m_{\mathrm{cold}} - m_{\mathrm{crit}}}{t_{\mathrm{disk}}}, \qquad
m_{\mathrm{crit}} = 3.8 \times 10^{9}\Msun\,\frac{V}{200\ \mathrm{km/s}}\,\frac{3R_{d}}{10\ \kpc},\\
\Delta m_{\mathrm{reheat}} &= \epsilon_{\mathrm{disk}}F\,\Delta m_{*}, \qquad
\Delta E = \tfrac{1}{2}\epsilon_{\mathrm{halo}}F\,\Delta m_{*}V_{\mathrm{SN}}^{2},\\
\Delta m_{\mathrm{eject}} &= \frac{\Delta E - \tfrac{1}{2}\Delta m_{\mathrm{reheat}}V^{2}}{\tfrac{1}{2}V^{2}}, \qquad
\dot m_{\mathrm{return}} = \gamma_{\mathrm{ej}}\,m_{\mathrm{ej}}/t_{\mathrm{dyn}},
\end{align*}
with $\alpha = 0.07$, $\epsilon_{\mathrm{disk}} = 3.5$, $\epsilon_{\mathrm{halo}} = 0.35$, $V_{\mathrm{SN}} = 630$ km/s, $\gamma_{\mathrm{ej}} = 0.5$, recycled fraction $0.43$, $R_{d} = \lambda R/\sqrt{2}$ and $t_{\mathrm{disk}} = 3R_{d}/V$. Metals are followed in each sector from a metal-free start: a yield $y = 0.03$ per unit of stars formed enters the cold gas and is carried by every flow, and each hot halo cools at its own metallicity. The feedback factor $F$ multiplies the supernova energy and mass loading per unit stellar mass; for our sector it is a calibrated number $F_{\mathrm{cal}}$, and the mirror's is $F$ times that.

## technical
pending

## lay
pending

## one-liner
pending
