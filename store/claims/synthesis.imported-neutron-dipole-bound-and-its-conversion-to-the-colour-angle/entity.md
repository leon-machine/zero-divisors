---
id: synthesis.imported-neutron-dipole-bound-and-its-conversion-to-the-colour-angle
kind: claim
version: 1
title: 'Imported: the neutron dipole bound and its conversion to the colour angle'
status: imported
region: synthesis
subject: standard-model
tags: [gauge-fields, confronted-with-data, undetermined-input]
proposed_by:
  kind: ai
  session: maintainer-2026-11-16
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction and decision
- name: Claude Fable 5.2
  role: drafting
  source: maintainer pass 2026-11-16 (anomaly)
review: draft
imported_from:
- citation: 'C. Abel et al., Measurement of the permanent electric dipole moment of the neutron, Phys. Rev. Lett. 124 (2020), 081803; arXiv:2001.11966.'
  key: Abel2020
  doi: 10.1103/PhysRevLett.124.081803
  locator: 'abstract; the final result and the sentence that follows it'
- citation: 'J. Dragos, T. Luu, A. Shindler, J. de Vries and A. Yousif, Confirming the existence of the strong CP problem in lattice QCD with the gradient flow, Phys. Rev. C 103 (2021), 015202; arXiv:1902.03254.'
  key: Dragos2021
  doi: 10.1103/PhysRevC.103.015202
  locator: 'abstract; section 2; equation (42); conclusions'
- citation: 'T. Bhattacharya, V. Cirigliano, R. Gupta, E. Mereghetti and B. Yoon, Contribution of the QCD Theta-term to the nucleon electric dipole moment, Phys. Rev. D 103 (2021), 114507; arXiv:2101.07230.'
  key: Bhattacharya2021
  doi: 10.1103/PhysRevD.103.114507
  locator: 'abstract'
- citation: 'L. J. Rosenberg, G. Rybka and B. Safdi, Axions and other similar particles, in Review of Particle Physics (Particle Data Group), review revised August 2023.'
  key: PDGAxions2023
  locator: 'section 90.2.1'
extraction:
  note: >-
    Imported by Leon's decision D1 of 16 November 2026, with the registration of the physical colour angle
    (synthesis.colour-angle-registered-free-input). A search of the store for an existing Fact holding the
    neutron bound found none: the bound is quoted, with the citation of Abel et al., inside clause (ii) of
    the proved result dark-matter.asymmetry-arrow-counted-fifteenth-refutation and in texts that follow it,
    and no imported Fact carried it; this Fact is therefore new and extends none. What was read at source on
    16 November 2026. Abel et al., arXiv:2001.11966, abstract and full text: the value
    (0.0 +- 1.1 stat +- 0.2 sys) x 10^-26 e cm; the sentence that the result may be interpreted as an upper
    limit |d_n| < 1.8 x 10^-26 e cm (90 percent C.L.); and that the neutron dipole moment alone stringently
    limits the angle, with no number given for the angle. Dragos et al., arXiv:1902.03254, abstract and full
    text: 2+1 flavours, pion masses 700, 570 and 410 MeV, three lattice spacings between 0.07 and 0.11 fm
    at one pion mass, two volumes; the assumption of continuum-like behaviour towards the chiral limit; the
    values d_n = -0.00152(71) theta-bar e fm and d_p = 0.0011(10) theta-bar e fm; the limit
    |theta-bar| < 1.98 x 10^-10 (90 percent CL) on the condition that the theta term is the only source of
    CP violation; in the body the experimental bound is quoted as d_n < 3.0 x 10^-26 e cm with two
    references (Baker et al. 2006; Pendlebury et al. 2015, neither read here), which is the limit before
    that of Abel et al.; the paper does not show how the limit on the angle is obtained from that bound or
    how the uncertainty of the coefficient enters it. Bhattacharya et al., arXiv:2101.07230, abstract: the
    conclusion that present lattice calculations do not provide a reliable estimate of the contribution of
    the Theta-term to the nucleon dipole moments; |d_n| below about 0.01 theta-bar e fm with the
    excited-state spectrum from fits to the two-point function, and possibly as large as 0.05 theta-bar e fm
    if the dominant excited state is the nucleon-pion state. The journal references of the two lattice
    papers are read from their DOIs. The Particle Data Group review, 2023 revision, section 90.2.1: the
    upper bounds |d_n| < 1.8 x 10^-26 e cm imply an effective angle of at most about 10^-10. Not read and
    not imported: the estimates of the conversion coefficient by current algebra, chiral perturbation
    theory and sum rules.
  maintainer_pass_2026_11_16:
    by: maintainer-2026-11-16
    date: '2026-11-16'
    note: 'New imported Fact, created at Leon''s decision D1 of 16 November 2026. The store held the neutron bound only as a quoted number inside a proved result; no existing Fact was extended. The closing paragraph of the formal level is arithmetic on the imported numbers and is marked as not a statement of any source.'
---

## formal
Let $d_{n}$ be the permanent electric dipole moment of the neutron, in units of the elementary charge $e$ times a length, and $\bar\theta$ the physical colour angle of Fact \claimref{synthesis.imported-physical-colour-angle-and-its-shift-under-quark-rephasing}(iii).
\begin{enumerate}
\item[(i)] \emph{(The measurement.)} Measured with ultracold neutrons at the Paul Scherrer Institute by Ramsey's method,
\[
d_{n} = (0.0 \pm 1.1_{\mathrm{stat}} \pm 0.2_{\mathrm{sys}}) \times 10^{-26}\ e\,\mathrm{cm},
\]
which the source reads as the upper limit $|d_{n}| < 1.8 \times 10^{-26}\ e\,\mathrm{cm}$ at $90$ percent confidence \cite{Abel2020}.
\item[(ii)] \emph{(The conversion, a lattice computation.)} A lattice computation of the dipole moments that the angle term induces, with $2 + 1$ dynamical flavours at pion masses of $700$, $570$ and $410$ MeV, three lattice spacings and two volumes, extrapolated to the physical pion mass, gives, on the assumption that the dipole moment behaves towards the chiral limit as in the continuum,
\[
d_{n} = -0.00152(71)\ \bar\theta\ e\,\mathrm{fm}, \qquad d_{p} = 0.0011(10)\ \bar\theta\ e\,\mathrm{fm},
\]
and the source states that, if the angle term is the only source of CP violation, the experimental bound on the neutron dipole moment limits $|\bar\theta| < 1.98 \times 10^{-10}$ at $90$ percent confidence. The experimental bound that source quotes is $d_{n} < 3.0 \times 10^{-26}\ e\,\mathrm{cm}$, the limit that preceded (i); it does not show how the limit on the angle is obtained from it, nor how the uncertainty of the coefficient enters \cite{Dragos2021}.
\item[(iii)] \emph{(The caveat.)} A later lattice study concludes that the lattice calculations of that time do not provide a reliable estimate of the contribution of the angle term to the nucleon dipole moments: with the excited-state spectrum taken from fits to the two-point function it finds $|d_{n}| \lesssim 0.01\ \bar\theta\ e\,\mathrm{fm}$, and if the dominant excited state is the nucleon-pion state the value could be as large as $0.05\ \bar\theta\ e\,\mathrm{fm}$ \cite{Bhattacharya2021}.
\item[(iv)] \emph{(The summary of the review.)} The Review of Particle Physics states that the upper bounds on the neutron dipole moment, $|d_{n}| < 1.8 \times 10^{-26}\ e\,\mathrm{cm}$, imply $|\bar\theta| \lesssim 10^{-10}$ \cite{PDGAxions2023}.
\end{enumerate}
\emph{Arithmetic on these numbers, not a statement of any of the sources.} A limit $|d_{n}| < L$ and a conversion $|d_{n}| = c\,|\bar\theta|$ give $|\bar\theta| < L/c$. With the central coefficient of (ii), $c = 0.00152\ e\,\mathrm{fm}$, the limit of (i), $L = 1.8 \times 10^{-13}\ e\,\mathrm{fm}$, gives $1.18 \times 10^{-10}$, and the earlier limit $3.0 \times 10^{-13}\ e\,\mathrm{fm}$ gives $1.97 \times 10^{-10}$, beside the source's $1.98 \times 10^{-10}$. With the coefficient one standard error below its central value, $0.00081\ e\,\mathrm{fm}$, the limit of (i) gives $2.2 \times 10^{-10}$. The values of (iii) are upper bounds on $c$ and so give no bound on the angle by themselves. The bound on the angle is thus of order $10^{-10}$, with an uncertainty of a factor of a few from the coefficient; it is a bound near $\bar\theta = 0$, where the conversion is linear, and it presumes that the angle term is the only source of the neutron's dipole moment.

## technical
The neutron's electric dipole moment has been measured to be zero within about $10^{-26}$ in units of the elementary charge times a centimetre; the 2020 result of the experiment at the Paul Scherrer Institute corresponds to an upper limit of $1.8 \times 10^{-26}$ at $90$ percent confidence. A nonzero physical colour angle would induce a dipole moment proportional to it, with a coefficient set by the strong interaction. A lattice computation gives the coefficient as $-0.00152(71)$ in units of the elementary charge times a femtometre, known to about half its value, and quotes from the earlier experimental limit the bound $|\bar\theta| < 1.98 \times 10^{-10}$, on the condition that the angle term is the only source of CP violation. A later lattice study finds that such computations are not yet reliable and gives only upper bounds on the coefficient. The Particle Data Group's review summarises the situation as $|\bar\theta| \lesssim 10^{-10}$. Dividing the 2020 limit by the central lattice coefficient gives $1.2 \times 10^{-10}$. The bound is linear in the angle near zero.

## lay
If the angle of the strong force were not tiny, the neutron would behave like a very small electric dipole, with its positive and negative charge slightly separated along its spin. Experiments have looked for this with great care and found nothing, down to a separation far smaller than the neutron itself. Turning that null result into a limit on the angle needs a calculation of how strongly the angle would polarise the neutron; the best calculations are still rough, but they agree that the angle must be smaller than about one part in ten billion.

## one-liner
$d_{n} = (0.0 \pm 1.1_{\mathrm{stat}} \pm 0.2_{\mathrm{sys}}) \times 10^{-26}\ e\,$cm, so $|d_{n}| < 1.8 \times 10^{-26}\ e\,$cm at $90$ percent confidence (Abel et al. 2020); a lattice conversion $d_{n} = -0.00152(71)\,\bar\theta\ e\,$fm gives $|\bar\theta| < 1.98 \times 10^{-10}$ from the earlier limit if the angle term is the only CP-odd source (Dragos et al. 2021), with the caveat that lattice values are not yet reliable (Bhattacharya et al. 2021); the bound is of order $10^{-10}$, good to a factor of a few.
