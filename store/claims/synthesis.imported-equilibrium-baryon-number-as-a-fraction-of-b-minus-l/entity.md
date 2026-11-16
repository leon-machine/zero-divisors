---
id: synthesis.imported-equilibrium-baryon-number-as-a-fraction-of-b-minus-l
kind: claim
version: 1
title: 'Imported: equilibrium baryon number as a fraction of $B - L$'
status: imported
region: synthesis
subject: dark-matter
tags: [matter-asymmetry, hypercharge-and-anomalies]
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
- citation: 'J. A. Harvey and M. S. Turner, Cosmological baryon and lepton number in the presence of electroweak fermion-number violation, Phys. Rev. D 42 (1990), 3344.'
  key: HarveyTurner1990
  doi: 10.1103/PhysRevD.42.3344
- citation: 'S. Yu. Khlebnikov and M. E. Shaposhnikov, Melting of the Higgs vacuum: conserved numbers at high temperature, Phys. Lett. B 387 (1996), 817; arXiv:hep-ph/9607386.'
  key: KhlebnikovShaposhnikov1996
  doi: 10.1016/0370-2693(96)01116-1
  locator: 'equations (6), (12), (14), (16) to (19) and the paragraph after (19)'
extraction:
  note: >-
    Imported by Leon's decision D3 of 16 November 2026, so that the conversion coefficient of
    synthesis.conditional-inheritance-of-b-minus-l-and-the-conversion-coefficient-as-a-gram-ratio (clauses (v),
    (vii)), the registered asymmetry premise and clause (vi) of
    synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them can pin the literature's closed forms.
    Read at source on 16 November 2026. Khlebnikov and Shaposhnikov, the arXiv text of hep-ph/9607386
    (PURD-TH-96-05, CERN-TH/96-167, July 1996): equations (12), (14), (16), (17), (18), (19), the rule for the
    coefficients (1/6 per helicity state of a boson pair, 1/12 per helicity state of a fermion pair, multiplying
    -T^2 mu^2 in the one-loop effective action), the conserved numbers B/n_f - L_i with the asymmetries taken
    equal in flavour, the paragraph on the use of the relation at the freeze-out, and the attributions: for phi
    much less than T "the same result as in the symmetric phase [7]", [7] Khlebnikov and Shaposhnikov, Nucl.
    Phys. B 308 (1988) 885; equation (19) coincides with the result of its references [4, 5, 6, 8], which are
    Harvey and Turner, Phys. Rev. D 42 (1990) 3344, Dolgov, Phys. Rep. 222 (1992) 309, Dreiner and Ross, Nucl.
    Phys. B 410 (1993) 188, Nelson and Barr, Phys. Lett. B 246 (1990) 141. The source prints no number for
    n_f = 3, n_s = 1; the three values in (c) are arithmetic on its formulas. Its journal data (Phys. Lett. B
    387 (1996) 817) are from the reference list of Buchmuller, arXiv:hep-ph/0101102, and the DOI from the arXiv
    record. Harvey and Turner: the abstract, on the publisher's page (DOI 10.1103/PhysRevD.42.3344, received 25 May
    1990) and in the index record of the report FERMILAB-PUB-90/49-A, EFI-90-33, and the scanned preprint of
    March 1990, sections on the equilibrium relations: the conditions (2a) to (2f), the
    condition (3) of the anomalous process, neutrality Q = 0 with Q_3 = 0 above the transition and a vanishing
    chemical potential of the neutral Higgs field below it, masses neglected. The scan is poor: as far as it can be read the
    preprint treats all species with one statistics, and its equation (9) reads B = (16N + 4m)/(44N + 13m) (B - L) above
    the transition (consistent with its equation (8)); that is the closed form of (d) with one per boson state
    in place of two (the same Gram ratio with that weight gives (16N + 4m)/(44N + 13m) and
    (16N + 4(m + 2))/(48N + 13(m + 2)), computed in this pass in exact arithmetic), so the preprint's form is not
    the closed form the literature quotes from the published article. NOT read at source: the body of the published article of Harvey and Turner (only
    its abstract page was reached). Its closed forms are
    stated in (d) as three sources read in this pass quote them: Khlebnikov and Shaposhnikov as above;
    Kartavtsev, arXiv:hep-ph/0511059, equation (13a), B = (8N + 4m c_-)/(22N + 13m c_-) (B - L), attributed there
    to Harvey and Turner and to Dreiner and Ross, where c_- is a mass factor of the charged Higgs field equal to
    one in the massless limit; Buchmuller, arXiv:hep-ph/0101102, equation (10) with a = 28/79 attributed to
    Harvey and Turner and equation (53), (8N + 4)/(22N + 13), attributed to Khlebnikov and Shaposhnikov 1988.
    The reading in the series' chart is an
    identification of formulas, checked in exact arithmetic on n_f = 1 to 6, n_s = 0 to 6.
  maintainer_pass_2026_11_16:
    by: maintainer-2026-11-16
    date: '2026-11-16'
    note: 'Created by the maintainer pass of 2026-11-16 at Leon''s decision D3 (the equilibrium relation between baryon number and B - L as a Fact, checked at source; of the published article of Harvey and Turner only the abstract was reached, and its closed forms are quoted through three sources that were read).'
---

## formal
The setting, as in the sources, is the hot plasma of the Standard Model with $n_{f}$ generations and $n_{s}$ Higgs doublets at temperature $T$: the chemical potentials are small against $T$; the masses are small against $T$, so that the high-temperature spectrum applies; the gauge charges are neutral; the asymmetries are equal in the lepton flavours, so that $B - L$ is the one conserved number; and the anomalous weak process is in equilibrium, $\mu_{B} + \mu_{L} = 0$. Let $\phi$ be the expectation value of the Higgs field, $g$ the weak coupling, $m_{W}(\phi) = \tfrac12g\phi$, and $m_{D}^{2} = \bigl(\tfrac23 + \tfrac{n_{s}}{6} + \tfrac{n_{f}}{3}\bigr)g^{2}T^{2}$ the Debye mass of the weak field. Nothing here is derived in the store.
\begin{enumerate}
\item[(a)] \emph{(The relation.)} The equilibrium baryon number at fixed $B - L$ is
\[
B_{0} = \frac{4(2n_{f} + n_{s})\,m_{D}^{2} + 8(2 + 2n_{f} + n_{s})\,m_{W}(\phi)^{2}}{(22n_{f} + 13n_{s})\,m_{D}^{2} + 2(26 + 24n_{f} + 13n_{s})\,m_{W}(\phi)^{2}}\,(B - L)
\]
\cite[eq.~(17)]{KhlebnikovShaposhnikov1996}.
\item[(b)] \emph{(The two limits.)} In the symmetric phase, and in the Higgs phase for $\phi \ll T$,
\[
B_{0} = \frac{4(2n_{f} + n_{s})}{22n_{f} + 13n_{s}}\,(B - L),
\]
and for $\phi \gg T$
\[
B_{0} = \frac{4(2 + 2n_{f} + n_{s})}{26 + 24n_{f} + 13n_{s}}\,(B - L)
\]
\cite[eqs.~(18), (19)]{KhlebnikovShaposhnikov1996}. What decides between them is $\phi$ against $T$, not $T$ against the transition temperature; the source states that the earlier derivations, which equate chemical potentials using the zero-temperature spectrum, are wrong for $\phi \lesssim T$.
\item[(c)] \emph{(Three generations, one doublet; arithmetic on (a), (b).)} For $n_{f} = 3$, $n_{s} = 1$ the two limits are $\tfrac{28}{79}$ and $\tfrac{12}{37}$, $m_{D}^{2} = \tfrac{11}{6}g^{2}T^{2}$, and (a) reads $B_{0} = (28m_{D}^{2} + 72m_{W}^{2})/(79m_{D}^{2} + 222m_{W}^{2})\,(B - L)$.
\item[(d)] \emph{(The closed forms of Harvey and Turner.)} With $N$ generations and $m$ Higgs doublets, the fast interactions (gauge, Higgs and the anomalous weak process) in equilibrium, masses neglected, and the plasma electrically neutral (with the third component of weak isospin also neutral above the transition, and the chemical potential of the neutral Higgs field zero below it),
\[
B = \frac{8N + 4m}{22N + 13m}\,(B - L) \ \text{ above the weak transition}, \qquad B = \frac{8N + 4(m + 2)}{24N + 13(m + 2)}\,(B - L) \ \text{ below it}
\]
\cite{HarveyTurner1990}, as quoted in the literature read: these are the two limits of (b) with $n_{f} = N$, $n_{s} = m$. Without particles beyond the usual quarks and leptons, a nonzero $B - L$ before the epoch of rapid fermion-number violation is needed for baryon and lepton asymmetries to survive it, and a nonzero $B + L$ then persists after it \cite{HarveyTurner1990} (abstract).
\item[(e)] \emph{(The counting.)} In the source's one-loop effective action a species enters through $-T^{2}\eta\mu^{2}$ with $\eta = \tfrac16$ for each helicity state of a bosonic particle-antiparticle pair and $\eta = \tfrac{1}{12}$ for each helicity state of a fermionic pair: a boson state counts twice a fermion state \cite[eq.~(6)]{KhlebnikovShaposhnikov1996}.
\item[(f)] \emph{(Where the relation is taken.)} The relation is to be taken at the moment the anomalous weak processes freeze out. For a strongly first-order transition, after which $\phi/T$ exceeds about $1.2$ to $1.5$, the freeze-out coincides with the transition and the symmetric-phase limit of (b) is accurate enough; for a weakly first-order or second-order transition or a crossover, (a) is to be used at $\phi/T \approx 1.2$ to $1.5$, that is $m_{W}^{2}(\phi)/m_{D}^{2} \approx 0.2$ to $0.3$, where the equilibrium baryon number lies roughly midway between its two limits \cite{KhlebnikovShaposhnikov1996} (the paragraph after eq. (19)).
\end{enumerate}
\emph{Provenance:} (a), (b), (e), (f) \cite{KhlebnikovShaposhnikov1996}; (d) \cite{HarveyTurner1990}, whose published text was not read: the closed forms are as quoted by \cite{KhlebnikovShaposhnikov1996} and by two further sources named in the record of this entity.

\emph{Reading in the series' chart (identification of formulas, not part of the import).} With $n_{f} = N_{f}$ and $n_{s} = N_{H}$, the two limits of (b) are the Gram ratios $c_{\mathrm{sym}} = (8N_{f} + 4N_{H})/(22N_{f} + 13N_{H})$ and $c_{\mathrm{br}} = (8N_{f} + 4(N_{H} + 2))/(24N_{f} + 13(N_{H} + 2))$ of the susceptibility form on the stored charges of the fifteen, under these conventions: one per fermion state and two per complex boson state, as in (e), all massless; in the symmetric phase the neutral gauge charge is the hypercharge and the bosons in the form are the components of the $N_{H}$ doublets; in the other limit it is the electric charge and the bosons are the weak boson of charge one with two helicities and the charged component of each doublet. The relation (a) is the mediant of the two limits with weights $m_{D}^{2}$ and $2m_{W}^{2}$, so it lies between them.

## technical
When the anomalous weak process is in equilibrium, baryon number is no longer free: with the conserved quantity $B - L$ fixed and the plasma neutral, the chemical potentials are determined, and the baryon number is a fixed fraction of $B - L$. Harvey and Turner computed the fraction by equating chemical potentials: $(8N + 4m)/(22N + 13m)$ above the weak transition and $(8N + 4(m + 2))/(24N + 13(m + 2))$ below it, for $N$ generations and $m$ Higgs doublets, $28/79$ and $12/37$ in the Standard Model. Khlebnikov and Shaposhnikov rederived the relation from the high-temperature effective action and found that the fraction depends continuously on the ratio of the Higgs expectation value to the temperature, through the Debye mass and the mass the Higgs field gives the weak boson: the two older values are its limits for a small and a large expectation value, and the transition temperature as such plays no role. The relation is to be evaluated when the process freezes out.

## lay
In the hot early universe a weak-force process could turn baryons into leptons and back, keeping only their difference fixed. Once that process has run to equilibrium, the number of baryons is a definite fraction of the conserved difference: about a third. The exact fraction depends on how many kinds of particles are present and on how far the Higgs field has switched on when the process stops: it is 28/79 if the Higgs field is still off and 12/37 if it is fully on, for the known particles. The series takes these formulas from the literature.

## one-liner
With the anomalous weak process in equilibrium, $B_{0} = \bigl[4(2n_{f} + n_{s})m_{D}^{2} + 8(2 + 2n_{f} + n_{s})m_{W}^{2}\bigr]/\bigl[(22n_{f} + 13n_{s})m_{D}^{2} + 2(26 + 24n_{f} + 13n_{s})m_{W}^{2}\bigr](B - L)$ (Khlebnikov and Shaposhnikov 1996), with limits $(8n_{f} + 4n_{s})/(22n_{f} + 13n_{s})$ for $\phi \ll T$ and $(8n_{f} + 4(n_{s} + 2))/(24n_{f} + 13(n_{s} + 2))$ for $\phi \gg T$ (Harvey and Turner 1990): $\tfrac{28}{79}$ and $\tfrac{12}{37}$ for three generations and one doublet.
