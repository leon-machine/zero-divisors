---
id: synthesis.imported-einstein-cartan-matter-coupling
kind: claim
version: 1
title: 'Imported: the Einstein-Cartan matter coupling, in Gauge Theory Gravity form'
status: imported
region: synthesis
subject: einstein
tags: [gauge-fields, curvature-and-field-equations, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-31
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'T. W. B. Kibble, Lorentz invariance and the gravitational field, J. Math. Phys. 2 (1961), 212--221.'
  key: Kibble1961
  doi: 10.1063/1.1703702
- citation: 'D. W. Sciama, The physical structure of general relativity, Rev. Mod. Phys. 36 (1964), 463--469.'
  key: Sciama1964
- citation: 'F. W. Hehl, P. von der Heyde, G. D. Kerlick and J. M. Nester, General relativity with spin and torsion: foundations and prospects, Rev. Mod. Phys. 48 (1976), 393--416.'
  key: HehlEtAl1976
  doi: 10.1103/RevModPhys.48.393
- citation: 'A. N. Lasenby, C. J. L. Doran and S. F. Gull, Gravity, gauge theories and geometric algebra, Phil. Trans. R. Soc. Lond. A 356 (1998), 487--582.'
  key: LasenbyDoranGull1998
  doi: 10.1098/rsta.1998.0178
extraction:
  note: >-
    Imported so that synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part can pin the matter coupling
    it cited from memory. Checked: Kibble 1961 (title, journal, volume 2, issue 2, pages 212-221, DOI) against a
    bibliographic record; Hehl, von der Heyde, Kerlick and Nester 1976 (journal, volume, first page, year, DOI)
    against the publisher's listing, whose abstract states that the spin of matter couples to torsion and that the
    theory arises as a local gauge theory of the Poincare group; Lasenby, Doran and Gull 1998 (journal, volume,
    pages, year) against the authors' publication page and the DOI against the arXiv listing (gr-qc/0405033),
    whose abstract states that consistency with minimal coupling singles out a unique form of spin-torsion
    interaction. Cited from memory, not checked against the sources: Sciama 1964's last page; the statement of
    the field equations in the form given here, including the factor 8 pi G and the store's sign, which is the
    form clause (7) of synthesis.einstein-condition-is-infinity-vacuum-incidence takes.
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Created at Leon''s decision of 2026-10-31 to import the Einstein-Cartan matter coupling as a Fact (with the settlement of op.scale-selection-principle given the imported MacDowell-Mansouri action); partly verified (see note).'
---

## formal
Units $\hbar = c = 1$; store sign (Fact \claimref{synthesis.imported-gtg-dictionary}): signature $(+,-,-,-)$ on the physical vectors, de Sitter curvature $\mathcal{R}(B) = \tfrac{\Lambda}{3}B$. Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), with $\hb$ (the frame) and $\Omega$ (the rotation gauge field, equivalently the spin connection) varied independently, and let the gravitational functional be the Einstein-Cartan functional with cosmological term, normalised by Newton's constant $G$. Add a matter functional $S_{m}[\hb, \Omega, \psi]$ coupled minimally (through the covariant derivative built from $\hb$ and $\Omega$).
\begin{enumerate}
\item[(a)] (Frame equation.) The frame variation of $S_{m}$ defines the energy-momentum map $T(a)$ of the matter, and the frame equation is $\mathcal{G}(a) + \Lambda a + 8\pi G\,T(a) = 0$, with $\mathcal{G}$ the Einstein map of the field strength.
\item[(b)] (Connection equation.) The variation of $\Omega$ fixes the torsion algebraically in terms of the spin density of the matter: it vanishes where the spin density vanishes, and for a Dirac field minimal coupling gives a unique spin-torsion interaction, its spin trivector sourcing a totally antisymmetric torsion.
\item[(c)] (Torsion-free case.) For matter with no spin density (a perfect fluid, a minimally coupled scalar) the connection is the torsion-free one and (a) is Einstein's equation with cosmological constant and source $T$, the symmetric energy-momentum map.
\end{enumerate}
\emph{Provenance:} \cite{Kibble1961, Sciama1964, HehlEtAl1976, LasenbyDoranGull1998}.

## technical
When the gravitational field is treated as a gauge field, as in the Einstein-Cartan theory of Kibble and Sciama and in Gauge Theory Gravity, the frame and the connection are independent fields. Matter is coupled by putting the connection into its derivatives. Varying the frame then gives Einstein's equations with the matter's energy-momentum as source and Newton's constant as the overall normalisation; varying the connection ties the torsion to the matter's spin density, so torsion is absent where matter carries no spin, and for a Dirac field minimal coupling fixes the form of the spin-torsion interaction. Hehl, von der Heyde, Kerlick and Nester review the theory as a gauge theory of the Poincare group; Lasenby, Doran and Gull give it in geometric algebra on flat spacetime. Taken from the literature, with the field equation written in the store's sign.

## lay
Einstein's theory says how matter curves spacetime. When gravity is described as a gauge field, like the fields of particle physics, there is a standard way to let matter act as its source: the matter's energy and momentum appear in Einstein's equations, and the matter's spin produces a tiny extra twisting of spacetime, called torsion, that vanishes where there is no spin. This is the standard coupling, taken from the literature.

## one-liner
With frame and connection varied independently and matter coupled minimally, the frame equation is $\mathcal{G}(a) + \Lambda a + 8\pi G\,T(a) = 0$ with $T$ the matter's energy-momentum, and the connection equation ties the torsion algebraically to the matter's spin density, vanishing without spin (Kibble 1961, Sciama 1964, Hehl et al. 1976; in Gauge Theory Gravity Lasenby, Doran and Gull 1998).
