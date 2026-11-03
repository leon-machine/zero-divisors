---
id: synthesis.imported-dimensional-regularisation-and-the-bmhv-gamma5
kind: claim
version: 2
title: 'Imported: dimensional regularisation (''t Hooft and Veltman 1972) and its treatment of $\gamma_{5}$ (Breitenlohner and Maison 1977): the metric and the Dirac matrices split into four-dimensional and evanescent parts, $\{\gamma_{5}, \bar\gamma^{\mu}\} = 0$, $[\gamma_{5}, \hat\gamma^{\mu}] = 0$, which breaks the BRST symmetry of chiral gauge theories and needs finite symmetry-restoring counterterms (at one and at two loops in the abelian case); and the $d$-dimensional integral rules: translation invariance, vanishing scale-free integrals, integration by parts (Chetyrkin and Tkachov 1981), the radial integral, symmetric integration, the massless bubble $G(a_{1}, a_{2})$ and the two-loop benchmark $6\zeta_{3}$'
status: imported
region: synthesis
subject: quantum-fields
tags: [chirality, gauge-fields, classical-theorem, pseudoscalar-and-centre]
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
- citation: 'G. ''t Hooft and M. Veltman, Regularization and renormalization of gauge fields, Nucl. Phys. B 44 (1972), 189--213.'
  key: tHooftVeltman1972
  doi: 10.1016/0550-3213(72)90279-9
- citation: 'P. Breitenlohner and D. Maison, Dimensional renormalization and the action principle, Commun. Math. Phys. 52 (1977), 11--38.'
  key: BreitenlohnerMaison1977
  doi: 10.1007/BF01609069
- citation: 'H. Belusca-Maito, A. Ilakovac, M. Madjor-Bozinovic and D. Stoeckinger, Dimensional regularization and Breitenlohner-Maison/''t Hooft-Veltman scheme for gamma_5 applied to chiral YM theories: full one-loop counterterm and RGE structure, J. High Energy Phys. 08 (2020), 024, arXiv:2004.14398, equations (2.1), (2.6) and (2.10).'
  key: BeluscaMaito2020
  doi: 10.1007/JHEP08(2020)024
- citation: 'H. Belusca-Maito, A. Ilakovac, P. Kuehler, M. Madjor-Bozinovic and D. Stoeckinger, Two-loop application of the Breitenlohner-Maison/''t Hooft-Veltman scheme with non-anticommuting gamma_5: full renormalization and symmetry-restoring counterterms in an abelian chiral gauge theory, J. High Energy Phys. 11 (2021), 159; arXiv:2109.11042.'
  key: BeluscaMaito2021
  locator: 'abstract; eqs. (6.4) and (6.5) (the one-loop breaking and the one-loop finite symmetry-restoring counterterms of the abelian theory with right-handed fermions, Tr Y_R^3 = 0 imposed)'
  doi: 10.1007/JHEP11(2021)159
- citation: 'K. G. Chetyrkin and F. V. Tkachov, Integration by parts: the algorithm to calculate beta-functions in 4 loops, Nucl. Phys. B 192 (1981), 159--204.'
  key: ChetyrkinTkachov1981
  doi: 10.1016/0550-3213(81)90199-1
- citation: 'A. Grozin, Lectures on multiloop calculations, lectures at the Calc-03 school, Dubna (2003); arXiv:hep-ph/0307297.'
  key: Grozin2003
  locator: 'eq. (2.1) (normalisation), eq. (2.5) (the bubble G(n1, n2)), eq. (2.12) (a triangle relation), Sec. 2.1 (scale-free integrals vanish)'
- citation: 'A. V. Kotikov and S. Teber, Multi-loop techniques for massless Feynman diagram calculations, arXiv:1805.05109.'
  key: KotikovTeber2018
  locator: 'eq. (2.14) (scale-free integrals vanish), eq. (2.19) (the bubble), the rule of triangles attributed to Chetyrkin and Tkachov, eqs. (3.42), (3.43) (the two-loop diagram with five unit lines, 6 zeta3 + O(eps))'
- citation: 'S. Weinzierl, Introduction to Feynman integrals, arXiv:1005.1855.'
  key: Weinzierl2010
  locator: 'eq. (39) (translation invariance), eq. (64) (the angular integral 2 pi^{D/2}/Gamma(D/2)), eq. (76) (a radial integral)'
extraction:
  note: >-
    Imported so that the result on the unit I4 can pin the regularisation literature it compares with instead of
    citing it from memory. Checked on 2026-11-01: the bibliographic data of 't Hooft-Veltman (Nucl. Phys. B 44,
    189-213, 1972, DOI) and Breitenlohner-Maison (Commun. Math. Phys. 52, 11-38, 1977, DOI) against their INSPIRE
    records; the scheme equations of (ii) against arXiv:2004.14398: the metric split g = gbar + ghat (2.1), the Dirac
    matrices split into four-dimensional gammabar and evanescent gammahat with {gammabar, gammahat} = 0 (2.6), and
    {gamma_5, gammabar^mu} = 0, [gamma_5, gammahat^mu] = 0 (2.10); and, from that paper's abstract, that the scheme
    breaks BRST invariance of chiral gauge theories, needs singular and evanescent counterterms that are not gauge
    invariant and finite counterterms that restore BRST invariance, and leaves the one-loop renormalisation group
    equations unchanged. Cited from memory, not checked against the sources: the content of 't Hooft and Veltman
    beyond the title, and the obstruction stated in (iii).
  maintainer_pass_2026_11_02:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, by Leon''s list of routine imports of 2026-11-02: clause (iv), the d-dimensional integral rules (translation invariance, vanishing scale-free integrals and total derivatives, integration by parts after Chetyrkin and Tkachov, the radial integral, symmetric integration, the massless bubble G(a1, a2), the two-loop benchmark 6 zeta3), and clause (v), the two-loop abelian BMHV counterterms (Belusca-Maito et al. 2021), added so that the two-loop vacuum polarisation and the chiral abelian loops pin them instead of citing them from memory. Clauses (i) to (iii) unchanged. Checked on 2026-11-02: the bubble formula and its normalisation against Grozin eqs. (2.1), (2.5) and Kotikov-Teber eq. (2.19); vanishing scale-free integrals against Grozin Sec. 2.1 and Kotikov-Teber eq. (2.14); translation invariance and the angular integral against Weinzierl eqs. (39), (64); the triangle rule as an integration-by-parts identity and its attribution to Chetyrkin and Tkachov against Kotikov-Teber (the rule of triangles) and the form against Grozin eq. (2.12); the title and DOI of Chetyrkin-Tkachov against the DOI record; the five-line value 6 zeta3 + O(eps) against Kotikov-Teber eqs. (3.42), (3.43); Belusca-Maito et al. 2021, authors, title and DOI against arXiv:2109.11042 and its eqs. (6.4), (6.5) against the arXiv text. Cited from memory, not checked against a source: the general radial integral with a power Q(l)^r in the numerator, and the symmetric-integration rule for 2r indices (both follow from rotation invariance and the Beta integral).'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (dimensional regularisation and the BMHV gamma_5 as a Fact, by Leon''s list of imports; the Clifford classification facts are cited from the stored primer results, not imported).'
---

## formal
\begin{enumerate}
\item[(i)] \emph{(Dimensional regularisation.)} Loop integrals are continued in the spacetime dimension $D$ and their divergences appear as poles at $D = 4$; the continuation preserves Lorentz invariance and, for vector-like gauge theories, gauge invariance \cite{tHooftVeltman1972}.
\item[(ii)] \emph{(The BMHV $\gamma_{5}$.)} In the scheme of 't Hooft and Veltman and of Breitenlohner and Maison the $D$-dimensional metric splits as $g = \bar g + \hat g$ into a four-dimensional and a $(D-4)$-dimensional (evanescent) part, the Dirac matrices correspondingly as $\gamma^{\mu} = \bar\gamma^{\mu} + \hat\gamma^{\mu}$ with $\{\bar\gamma^{\mu}, \hat\gamma^{\nu}\} = 0$, and $\gamma_{5}$, the four-dimensional product, satisfies $\{\gamma_{5}, \bar\gamma^{\mu}\} = 0$ and $[\gamma_{5}, \hat\gamma^{\mu}] = 0$. In chiral gauge theories this breaks BRST invariance; the singular and evanescent counterterms are not gauge invariant, and finite counterterms restore the symmetry; at one loop the renormalisation group equations are unchanged \cite{BreitenlohnerMaison1977, BeluscaMaito2020}.
\item[(iii)] \emph{(The obstruction.)} No $\gamma_{5}$ anticommuting with every $\gamma^{\mu}$ in $D \neq 4$ is compatible with a cyclic trace and $\mathrm{Tr}(\gamma_{5}\gamma^{\mu}\gamma^{\nu}\gamma^{\rho}\gamma^{\sigma}) \neq 0$ \cite{BreitenlohnerMaison1977}.
\item[(iv)] \emph{(The $d$-dimensional integral rules.)} On the Euclidean section, with measure $d^{d}\ell/\pi^{d/2}$, $d = 4 - 2\epsilon$: integrals are invariant under shifts of the loop momentum, $\int d^{d}\ell\,f(\ell + p) = \int d^{d}\ell\,f(\ell)$ \cite{Weinzierl2010}; scale-free integrals vanish, $\int d^{d}\ell\,Q(\ell)^{-a} = 0$, and so do integrals of total derivatives, which gives the integration-by-parts identities, among them the triangle rule \cite{ChetyrkinTkachov1981, Grozin2003, KotikovTeber2018}; the radial integral is $\int\frac{d^{d}\ell}{\pi^{d/2}}\,\frac{Q(\ell)^{r}}{(Q(\ell) + \Delta)^{N}} = \frac{\Gamma(r + d/2)\,\Gamma(N - r - d/2)}{\Gamma(d/2)\,\Gamma(N)}\,\Delta^{d/2 + r - N}$, and under the integral $\ell^{\alpha_{1}}\cdots\ell^{\alpha_{2r}} \to Q(\ell)^{r}\{\delta^{r}\}/(d(d+2)\cdots(d + 2r - 2))$, $\{\delta^{r}\}$ the sum over the pairings of the indices (symmetric integration); the Minkowski forms follow by the Wick rotation. The massless one-loop bubble is
\[
\int\frac{d^{d}k}{\pi^{d/2}}\,\frac{1}{Q(k)^{a_{1}}\,Q(k - q)^{a_{2}}} = G(a_{1}, a_{2})\,Q(q)^{d/2 - a_{1} - a_{2}}, \qquad G(a_{1}, a_{2}) = \frac{\Gamma(a_{1} + a_{2} - d/2)\,\Gamma(d/2 - a_{1})\,\Gamma(d/2 - a_{2})}{\Gamma(a_{1})\,\Gamma(a_{2})\,\Gamma(d - a_{1} - a_{2})}
\]
\cite{Grozin2003, KotikovTeber2018}, and the two-loop massless self-energy integral with five lines of unit index, $\int\int\frac{d^{d}k\,d^{d}l}{\pi^{d}}\,\frac{1}{Q(k)Q(k - q)Q(l)Q(l - q)Q(k - l)}$, equals $6\zeta_{3}/Q(q) + O(\epsilon)$ \cite{ChetyrkinTkachov1981, KotikovTeber2018}.
\item[(v)] \emph{(Two loops in the abelian chiral theory.)} For an abelian gauge theory with right-handed fermions of charges $\mathcal{Y}_{R}$ and $\mathrm{Tr}\,\mathcal{Y}_{R}^{3} = 0$, the BMHV scheme is consistent at two loops: the finite symmetry-restoring counterterms through two loops have the same form as at one loop, restoring the Ward identities, the one-loop ones being $\frac{\hbar}{16\pi^{2}}\int\bigl[-\frac{e^{2}}{6}\mathrm{Tr}(\mathcal{Y}_{R}^{2})\,\bar A\cdot\bar\partial^{2}\bar A + \frac{e^{4}}{12}\mathrm{Tr}(\mathcal{Y}_{R}^{4})\,(\bar A^{2})^{2} + (\text{a fermion term proportional to } 5 + \xi)\bigr]$; ultraviolet-divergent evanescent counterterms are needed in addition \cite{BeluscaMaito2021}.
\end{enumerate}

## technical
Dimensional regularisation continues loop integrals to a non-integer number of dimensions, so divergences become poles at four dimensions; it keeps Lorentz and vector-like gauge invariance. The chirality matrix $\gamma_{5}$ is intrinsically four-dimensional, and no continuation keeps it anticommuting with every Dirac matrix while traces stay cyclic and the four-dimensional epsilon trace survives. The standard consistent choice, due to 't Hooft and Veltman and to Breitenlohner and Maison, splits the Dirac matrices into a four-dimensional part, with which $\gamma_{5}$ anticommutes, and an evanescent part, with which it commutes. In chiral gauge theories this breaks the BRST symmetry, and finite counterterms are needed to restore it; for an abelian theory with right-handed fermions their form at two loops is the same as at one loop (Belusca-Maito and collaborators, 2021).

The rules that make dimensionally continued integrals computable are also standard. Integrals do not change when the loop momentum is shifted, integrals with no scale and integrals of total derivatives vanish, and the last gives the integration-by-parts identities of Chetyrkin and Tkachov, which reduce massless multi-loop integrals to a few masters. The one-loop radial integral and the massless bubble are ratios of Gamma functions; under the integral, products of loop momenta are replaced by symmetric combinations of the metric over $d(d+2)\cdots$; and the two-loop self-energy integral with five unit lines is $6\zeta_{3}$ at four dimensions.

## lay
One standard way of taming the infinities of quantum corrections pretends that spacetime has a slightly non-integer number of dimensions. The quantity that distinguishes left-handed from right-handed particles exists only in four dimensions, so the method has to give up one of its properties; the standard choice keeps it consistent at the cost of extra corrections in theories, like the weak force, that treat left and right differently. The method comes with a small set of rules for doing the resulting integrals, which reduce complicated calculations to a few standard ones.

## one-liner
Dimensional regularisation ('t Hooft-Veltman) with the Breitenlohner-Maison $\gamma_{5}$: $\gamma^{\mu} = \bar\gamma^{\mu} + \hat\gamma^{\mu}$, $\{\gamma_{5}, \bar\gamma^{\mu}\} = 0$, $[\gamma_{5}, \hat\gamma^{\mu}] = 0$; no anticommuting $\gamma_{5}$ in $D \neq 4$ with a cyclic trace and nonzero epsilon trace; BRST of chiral theories broken and restored by finite counterterms, of one-loop form also at two loops in the abelian case; the $d$-dimensional rules (shift invariance, vanishing scale-free integrals, integration by parts, the bubble $G(a_{1}, a_{2})$, symmetric integration, the benchmark $6\zeta_{3}$).
