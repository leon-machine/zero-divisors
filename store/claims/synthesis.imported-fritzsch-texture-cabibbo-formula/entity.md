---
id: synthesis.imported-fritzsch-texture-cabibbo-formula
kind: claim
version: 1
title: 'Imported: for nearest-neighbour (Fritzsch) quark textures each light-plane angle obeys tan^2 theta = m_light/m_heavy (Gatto, Sartori and Tonin 1968; Fritzsch 1978), and the Cabibbo element is sin theta_C = |R_u - R_d e^{-i psi}| with a phase psi near 90 degrees (Fritzsch and Xing 1999)'
status: imported
region: synthesis
subject: generations
tags: [flavour-and-mixing, confronted-with-data]
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
- citation: 'R. Gatto, G. Sartori and M. Tonin, Weak self-masses, Cabibbo angle, and broken SU(2) x SU(2), Phys. Lett. B 28 (1968), 128--130.'
  key: GST1968
- citation: 'H. Fritzsch, Weak-interaction mixing in the six-quark theory, Phys. Lett. B 73 (1978), 317.'
  key: Fritzsch1978
- citation: 'H. Fritzsch and Z.-z. Xing, The light quark sector, CP violation, and the unitarity triangle, Nucl. Phys. B 556 (1999), 49--75; arXiv:hep-ph/9904286.'
  key: FritzschXing1999
  locator: 'eqs. (3.8) to (3.10), Section 5.1'
  doi: 10.1016/S0550-3213(99)00337-5
extraction:
  note: >-
    Imported so that synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase
    can pin the formula it reads in the store's light-plane block. Checked on 2026-11-01 against
    arXiv:hep-ph/9904286 (abstract page and PDF): title, authors, DOI; eq. (3.8), sin theta_C = |R_u
    - R_d e^{-i psi}|; eq. (3.9), R_u = sqrt(m_u/(m_u + m_c)) sqrt(m_s/(m_d + m_s)), R_d =
    sqrt(m_c/(m_u + m_c)) sqrt(m_d/(m_d + m_s)); eq. (3.10), tan theta_u = sqrt(m_u/m_c), tan
    theta_d = sqrt(m_d/m_s); the phase about 79 degrees at central inputs, 38 to 115 degrees over
    the inputs, with "a good chance to be around 90 degrees", and phi_1 about 90 degrees from |V_us|
    in Section 5.1; the abstract's phase near 90 degrees in the light quark sector. The squared form
    is arithmetic on eqs. (3.8), (3.9). The journal volume and pages of Fritzsch and Xing, and the
    Gatto-Sartori-Tonin and Fritzsch 1978 papers (bibliographic data as in the references file), are
    cited from memory.
    The bare i is that of the imported complex quark mass matrices (an imported Hilbert-space and number convention).
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (Leon approved the import of the Fritzsch-Xing formula, with Gatto-Sartori-Tonin and Fritzsch 1978, as a routine Fact).'
---

## formal
For quark mass matrices whose light $2 \times 2$ block has the nearest-neighbour (Fritzsch) form, zero in the light-light entry and equal moduli off the diagonal, each sector's light-plane rotation angle obeys $\tan\theta_{u} = \sqrt{m_{u}/m_{c}}$, $\tan\theta_{d} = \sqrt{m_{d}/m_{s}}$ (the Gatto-Sartori-Tonin relation for the texture of Fritzsch), and with $\psi$ the relative phase of the two sectors' off-diagonal entries the Cabibbo element is
\[
\sin\theta_{C} = |R_{u} - R_{d}\,e^{-i\psi}|,\qquad
R_{u} = \sqrt{\tfrac{m_{u}}{m_{u} + m_{c}}}\sqrt{\tfrac{m_{s}}{m_{d} + m_{s}}},\quad
R_{d} = \sqrt{\tfrac{m_{c}}{m_{u} + m_{c}}}\sqrt{\tfrac{m_{d}}{m_{d} + m_{s}}},
\]
in the limit where the heavy family decouples; equivalently, with $x = m_{u}/m_{c}$ and $y = m_{d}/m_{s}$, $\sin^{2}\theta_{C} = (x + y - 2\sqrt{xy}\cos\psi)/((1 + x)(1 + y))$. The measured $|V_{us}|$ with the light-quark mass ratios selects $\psi$ near $90^{\circ}$ (about $79^{\circ}$ at the central inputs of 1999, $38^{\circ}$ to $115^{\circ}$ over them). Here $i$ is the unit of the imported complex mass matrices. \emph{Provenance:} \cite{GST1968}, \cite{Fritzsch1978}, \cite{FritzschXing1999} (eqs. (3.8) to (3.10), Section 5.1).

## technical
The oldest successful quark-mass relation says that the Cabibbo angle is about the square root of the down to strange mass ratio. In the nearest-neighbour textures of Fritzsch it holds sector by sector, and the Cabibbo angle is the modulus of the difference of the up-sector and down-sector contributions, which depends on one relative phase. Fritzsch and Xing showed that the data put that phase near a right angle, which also makes the unitarity triangle nearly rectangular.

## lay
A classic observation in particle physics links how strongly quarks of different families mix to the ratios of their masses. In one well-known family of models the mixing comes out as the difference of two such square-root ratios, offset by a phase, and the measured mixing wants that phase to be close to a right angle.

## one-liner
For Fritzsch textures $\tan^{2}\theta = m_{\mathrm{light}}/m_{\mathrm{heavy}}$ in each sector and $\sin\theta_{C} = |R_{u} - R_{d}e^{-i\psi}|$, with $\psi$ near $90^{\circ}$ fitted to $|V_{us}|$ (Fritzsch and Xing 1999).
