---
id: synthesis.imported-anomalous-weak-process-changes-b-plus-l-and-keeps-b-minus-l
kind: claim
version: 1
title: 'Imported: the anomalous weak process changes $B + L$ and keeps $B - L$'
status: imported
region: synthesis
subject: dark-matter
tags: [matter-asymmetry, hypercharge-and-anomalies, classical-theorem]
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
- citation: 'G. ''t Hooft, Symmetry breaking through Bell-Jackiw anomalies, Phys. Rev. Lett. 37 (1976), 8.'
  key: tHooft1976
  doi: 10.1103/PhysRevLett.37.8
- citation: 'V. A. Kuzmin, V. A. Rubakov and M. E. Shaposhnikov, On anomalous electroweak baryon-number non-conservation in the early universe, Phys. Lett. B 155 (1985), 36--42.'
  key: KuzminRubakovShaposhnikov1985
  doi: 10.1016/0370-2693(85)91028-7
- citation: 'V. A. Rubakov and M. E. Shaposhnikov, Electroweak baryon number non-conservation in the early universe and in high energy collisions, arXiv:hep-ph/9603208 (for Usp. Fiz. Nauk 166, no. 5, 1996).'
  key: RubakovShaposhnikov1996
  locator: 'equations (2.2) to (2.5); section 3'
extraction:
  note: >-
    Imported by Leon's decision D3 of 16 November 2026, so that the conditional inheritance of B - L
    (synthesis.conditional-inheritance-of-b-minus-l-and-the-conversion-coefficient-as-a-gram-ratio, hypothesis
    (A)), the registered asymmetry premise and clauses (v), (vi) of
    synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them can pin the process instead of citing
    it from memory. Read at source on 16 November 2026: the abstract of 't Hooft's letter on the publisher's page
    (DOI 10.1103/PhysRevLett.37.8, received 22 March 1976): Bell-Jackiw anomalies violate certain
    current-conservation laws in models of fermions coupled to gauge fields; in perturbation theory the total
    charge still seems conserved; nonperturbative effects give interactions that violate it; one consequence is
    baryon and lepton number nonconservation in gauge theories with charm. The review of Rubakov and Shaposhnikov,
    arXiv:hep-ph/9603208 (CERN-TH/96-13, INR-913/96, 1 March 1996; its abstract says it is to appear in Usp. Fiz.
    Nauk 166, no. 5, May 1996; page numbers not checked): equations (2.2) to (2.5) as stated in the formal level,
    the count of twelve doublets for three families, the sentence that B - L is conserved while B + L is
    violated, and in section 3 the estimate of the rate in the unbroken phase (a constant of order one times
    (alpha_W T)^4, its references [74, 75]) against the expansion rate (of order 0.1 T^2/M_Pl), the range
    T_c < T < 0.1 M_Pl alpha_W^4 ~ 10^12 GeV, the conclusion that the reactions are fast there, and the
    Boltzmann suppression exp(-E_sph(T)/T) below T_c; its reference list gives [20] 't Hooft, Phys. Rev. Lett. 37
    (1976) 8, [21] 't Hooft, Phys. Rev. D 14 (1976) 3432, [25] Kuzmin, Rubakov and Shaposhnikov, Phys. Lett. 155B
    (1985) 36, and its introduction attributes to [20, 21] the violation of baryon number in the electroweak
    theory and to [25] that baryon number is rapidly violated at high temperatures. The bibliographic data of
    Kuzmin, Rubakov and Shaposhnikov (title, Phys. Lett. B 155, issue 1-2, pages 36-42, 1 May 1985, DOI) from two
    index records. NOT read at source: the text and the abstract of Kuzmin, Rubakov and Shaposhnikov 1985 (the
    publisher's page was not reached and the open records carry no abstract), so clause (b) is stated as the
    review of two of its authors states it and attributes it; and 't Hooft's Phys. Rev. D 14, 3432, which is
    not cited here. A second attribution read at source, not used in the statement: Arnold and McLerran,
    Fermilab-Pub-87/34-T (1987), introduction: Kuzmin, Rubakov and Shaposhnikov argued that the violation is
    unsuppressed at temperatures of about 1 TeV; B - L has no anomaly; each transition changes B by the number
    of families. The reading in the series' chart is an identification of formulas, checked by hand.
  maintainer_pass_2026_11_16:
    by: maintainer-2026-11-16
    date: '2026-11-16'
    note: 'Created by the maintainer pass of 2026-11-16 at Leon''s decision D3 (the anomalous weak process as a Fact, checked at source). The colour process of the same kind is not part of this Fact.'
---

## formal
The setting is the Standard Model with $n_{f}$ generations, in the index notation of the sources; nothing here is derived in the store.
\begin{enumerate}
\item[(a)] \emph{(The anomaly and the selection rule.)} For each left-handed weak doublet $i$ (for three generations there are twelve: nine quark doublets, one for each colour and generation, and three lepton doublets) the fermion-number current $J^{(i)}_{\mu}$ is not conserved,
\[
\partial_{\mu}J^{(i)}_{\mu} = \frac{1}{32\pi^{2}}\,\mathrm{Tr}\bigl(F_{\mu\nu}\tilde{F}_{\mu\nu}\bigr),
\]
$F$ the field strength of the weak field and $\tilde{F}$ its dual; the right-hand side is, in the source's normalisation, the weak field's four-form, the pseudoscalar part of the square of the field strength. In a process in which the weak field has $N[A] = \frac{1}{32\pi^{2}}\int d^{4}x\,\mathrm{Tr}(F_{\mu\nu}\tilde{F}_{\mu\nu}) \neq 0$ the fermion number of every doublet changes by the same amount, $\Delta N^{(i)}_{F} = N[A]$. Hence for three generations $\Delta N_{e} = \Delta N_{\mu} = \Delta N_{\tau} = N[A]$ and $\Delta B = \tfrac13 \cdot 3 \cdot 3\,N[A] = 3N[A]$: baryon number and lepton number change by equal amounts, so $B - L$ is conserved and $B + L$ is violated \cite[eqs.~(2.2) to (2.5)]{RubakovShaposhnikov1996}. That the anomaly, through nonperturbative effects, gives interactions that violate baryon and lepton number, although in perturbation theory the total charge still seems conserved, is 't Hooft's result \cite{tHooft1976}.
\item[(b)] \emph{(Fast above the weak transition.)} In the phase of unbroken weak symmetry the rate of these processes is much higher than the expansion rate of the universe for temperatures $T_{c} < T < 0.1\,M_{\mathrm{Pl}}\alpha_{W}^{4} \sim 10^{12}$ GeV, $T_{c}$ the temperature of the weak transition and $\alpha_{W}$ the weak coupling: the reactions that violate baryon number are fast at these temperatures. Below $T_{c}$ the rate is suppressed by a Boltzmann factor $\exp(-E_{\mathrm{sph}}(T)/T)$, $E_{\mathrm{sph}}(T)$ proportional to $m_{W}(T)/\alpha_{W}$ \cite[section 3]{RubakovShaposhnikov1996}. That baryon number is rapidly violated at high temperatures is attributed there to \cite{KuzminRubakovShaposhnikov1985}.
\end{enumerate}
\emph{Provenance:} (a) \cite{tHooft1976} (abstract), in the form of \cite{RubakovShaposhnikov1996}; (b) \cite{KuzminRubakovShaposhnikov1985}, as stated and attributed in \cite{RubakovShaposhnikov1996}; the text of the 1985 letter was not read.

\emph{Reading in the series' chart (identification of formulas, not part of the import).} A charge $X$ of one generation that is constant on weak doublets, with value $x_{Q}$ on the quark doublet and $x_{L}$ on the lepton doublet, changes in such a process by $(3x_{Q} + x_{L})\,N[A] = \tfrac12A_{2}(X)\,N[A]$ per generation, with $A_{2}(X) = 6x_{Q} + 2x_{L}$ the mixed weak coefficient of the stored classification of the abelian charges of the sixteen: $A_{2}(n_{B}) = A_{2}(n_{L}) = 2$ gives $\Delta B = \Delta L = N[A]$ per generation, and $A_{2}(B - L) = 0$. The statement is about the weak field only; the process of the same kind driven by the colour field's four-form is not part of this Fact.

## technical
In the Standard Model the baryon and lepton currents are conserved classically and seem conserved in perturbation theory, but each left-handed weak doublet contributes the same anomaly to its fermion-number current, proportional to the weak field strength contracted with its dual. A change of the topological number of the weak field therefore changes the fermion number of every doublet by one unit: three units of baryon number and three of lepton number for three generations. The difference $B - L$ is untouched and the sum $B + L$ is not conserved. At zero temperature the process is a tunnelling event and is negligible; in the hot early universe it proceeds by thermal fluctuation, and above the weak transition, up to about $10^{12}$ GeV, it is faster than the expansion.

## lay
Baryon number (which counts protons and neutrons) and lepton number (which counts electrons and neutrinos) look conserved in the Standard Model, but a subtle quantum effect of the weak force breaks both, by exactly the same amount. So their difference is still conserved, while their sum is not. Today the effect is far too slow to notice. In the heat of the early universe it was fast, and it could freely trade baryons against leptons as long as the difference stayed fixed. The series takes this from the literature.

## one-liner
The weak anomaly changes the fermion number of every left-handed doublet by $N[A]$, so $\Delta B = \Delta L = 3N[A]$ for three generations ($B - L$ conserved, $B + L$ violated; 't Hooft 1976), and above the weak transition, up to about $10^{12}$ GeV, the process is faster than the expansion (Kuzmin, Rubakov and Shaposhnikov 1985, as stated in Rubakov and Shaposhnikov 1996).
