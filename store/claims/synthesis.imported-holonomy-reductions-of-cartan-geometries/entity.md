---
id: synthesis.imported-holonomy-reductions-of-cartan-geometries
kind: claim
version: 1
title: 'Imported: holonomy reductions of Cartan geometries (Cap, Gover and Hammerl)'
status: imported
region: synthesis
subject: einstein
tags: [tractors, rotors-and-stabilisers, conformal-model, classical-theorem]
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
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'A. Cap, A. R. Gover and M. Hammerl, Holonomy reductions of Cartan geometries and curved orbit decompositions, Duke Math. J. 163 (2014), 1035--1070.'
  key: CapGoverHammerl2014
  doi: 10.1215/00127094-2644793
  locator: Definition 2.2, Lemma 2.3 and Section 2.3, Theorem 2.6, Theorem 3.5 (arXiv:1103.4497)
extraction:
  note: >-
    Imported so that the field-space premise of the gravitational action can be stated in invariant form,
    as a holonomy reduction of the varied Cl(2,4) connection to the stabiliser of the frozen point, and so
    that the results reading the premise in that form cite a source instead of memory. Checked on
    2026-11-01: the bibliographic data (authors, title, Duke Math. J. 163 (2014), no. 5, 1035-1070, DOI
    10.1215/00127094-2644793) against the ANU research portal record of the paper; against the arXiv text
    (arXiv:1103.4497), through a text-extraction tool, so the wording was summarised and only short
    phrases quoted: Definition 2.2 (a holonomy reduction of G-type O is a parallel section of the bundle
    with fibre the homogeneous space O), Lemma 2.3 and Section 2.3 (on a connected manifold a parallel
    section has values in one G-orbit, and a parallel tractor section of one G-type is a holonomy reduction
    of that type), Theorem 2.6 (the curved orbit decomposition into initial submanifolds, each with a
    canonical induced Cartan geometry, torsion-free when the original is), all stated for general Cartan
    geometries with no normality assumption; and Theorem 3.5 (the conformal case: for the normal conformal
    Cartan connection and a parallel standard tractor of nonzero norm, the zero locus of its scale splits the
    manifold into two open curved orbits, on which the metric sigma^-2 g of the conformal class is Einstein,
    and a hypersurface curved orbit). Cited from memory, not checked against the source: the exact form of
    the structure groups of the induced geometries, which the reading below computes for the series' case,
    and the source's sign convention for the Einstein constant, which is not used. The reading in the
    series' chart is the store's, not part of the import.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created at Leon''s decision of 2026-11-01 to import the Cap-Gover-Hammerl theory of holonomy reductions of Cartan connections as a Fact, for the invariant form of the field-space premise; partly verified (see note).'
---

## formal
Let $(\mathcal{G} \to M, \omega)$ be a Cartan geometry of type $(G, P)$ on a connected manifold $M$ (a Cartan connection, so its soldering part is nondegenerate; it need not be normal), and $\mathcal{O}$ a homogeneous space of $G$.
\begin{enumerate}
\item[(a)] \emph{(Holonomy reductions.)} A holonomy reduction of $G$-type $\mathcal{O}$ is a parallel section of $\mathcal{G} \times_{P} \mathcal{O}$. For a representation $\mathbb{V}$ of $G$ with tractor bundle $\mathcal{G} \times_{P} \mathbb{V}$ and its tractor connection, a parallel section has values in a single $G$-orbit $\mathcal{O} \subset \mathbb{V}$, and is a holonomy reduction of $G$-type $\mathcal{O}$; choosing a point of $\mathcal{O}$ with isotropy group $H$, $\mathcal{O} = G/H$.
\item[(b)] \emph{(Curved orbit decomposition.)} Given a holonomy reduction of $G$-type $\mathcal{O} = G/H$, $M$ is the disjoint union of curved orbits $M_{i}$, one for each $P$-type, that is each $P$-orbit in $\mathcal{O}$ met by the section (on the homogeneous model $G/P$ these are the $H$-orbits); each $M_{i}$ is an initial submanifold and carries a canonical Cartan geometry modelled on the corresponding $H$-orbit of the model, torsion-free if $\omega$ is.
\item[(c)] \emph{(The conformal case.)} For a normal conformal Cartan connection (the normal tractor connection of a conformal structure of signature $(p, q)$) and a parallel section $s$ of the standard tractor bundle with nonzero norm, $M = M_{+} \cup M_{0} \cup M_{-}$ with $M_{0}$ the zero locus of the scale $\sigma$ of $s$, a hypersurface curved orbit with an induced conformal structure of signature $(p - 1, q)$ or $(p, q - 1)$, and on the open curved orbits $M_{\pm}$ the metric $\sigma^{-2}g$ of the conformal class is Einstein, with the sign of its Einstein constant fixed by the norm of $s$.
\end{enumerate}
\emph{Provenance:} \cite{CapGoverHammerl2014}, Definition 2.2, Lemma 2.3 and Section 2.3 for (a), Theorem 2.6 for (b), Theorem 3.5 for (c).

\emph{Reading in the series' chart (not part of the import).} With $G$ the group of $\Cl(2,4)$ rotors acting on the vectors of $\Cl(2,4)$ (the standard tractors), $P$ the stabiliser of the line of the canonical tractor $X = \nO$ and $\omega$ a $\Cl(2,4)$ gauge field on flat spacetime with nondegenerate soldering $a \mapsto A(a) \times X$, a tractor $I$ parallel for $A$ has constant $Q(I) = 2\rho$ and is, by (a), a holonomy reduction of $G$-type the level set $Q = 2\rho$, with $H$ the stabiliser of $I$ (of de Sitter type for $\rho > 0$, anti-de Sitter type for $\rho < 0$ and Poincar\'e type for $\rho = 0$). Where $\ip{X}{I} \neq 0$ the points lie on one open curved orbit, and a rotor fixing $I$ and the line of $X$ fixes $X$ (the pairing $\ip{X}{I}$ is preserved), so the induced geometry there is modelled on the stabiliser of $I$ with structure group the stabiliser of $I$ and $X$, the Lorentz group of the complement of the plane of $X$ and $I$. Clause (c) concerns the normal connection, for which a parallel scale tractor is the Einstein condition (Theorem \claimref{interior.scale-tractor-leaves-cone}); (a) and (b) do not assume normality.

## technical
Cap, Gover and Hammerl develop holonomy reductions for general Cartan geometries. A Cartan geometry of type $(G, P)$ is a manifold modelled on the homogeneous space $G/P$ by a Cartan connection; a parallel section of an associated bundle whose fibre is a homogeneous space of $G$ is a holonomy reduction. For a tractor bundle (associated with a representation of $G$), a parallel section takes values in one $G$-orbit, so it is a holonomy reduction of that orbit type, with structure group reduced to the isotropy group $H$ of a point. Given such a reduction the manifold splits into curved orbits, one for each $P$-orbit in the $G$-orbit, which are initial submanifolds, each carrying an induced Cartan geometry modelled on the matching $H$-orbit of $G/P$, torsion-free when the original is. None of this assumes the Cartan connection is normal. In conformal geometry, with the normal tractor connection and a parallel standard tractor of nonzero norm, the zero set of its scale is a hypersurface separating two open curved orbits, on which the rescaled metric $\sigma^{-2}g$ is Einstein.

In the series' chart the standard tractors are the vectors of $\Cl(2,4)$, $P$ is the stabiliser of the line of the canonical tractor $X$, and a parallel tractor $I$ of norm $2\rho$ reduces a $\Cl(2,4)$ gauge field with nondegenerate soldering to the stabiliser of $I$ (de Sitter, anti-de Sitter or Poincar\'e type); where $\ip{X}{I} \neq 0$ the induced geometry has the Lorentz group as structure group. For the normal connection the parallel scale tractor is the Einstein condition; for a connection that is not required to be normal it is a reduction of the field.

## lay
A Cartan geometry describes a curved space by comparing it, point by point, with a simple symmetric model space. Cap, Gover and Hammerl showed that whenever such a geometry carries a quantity that stays fixed as it is transported around, the space breaks into pieces, each with its own simpler geometry of the same kind, and that this works whether or not the geometry obeys the usual normalisation. For the conformal geometry of spacetime with its standard normalisation, if a fixed quantity of this kind has nonzero length, it singles out a metric solving Einstein's equations on the parts where its scale is nonzero. This is a result taken from the mathematical literature.

## one-liner
A parallel section of a tractor bundle of any Cartan geometry is a holonomy reduction to the isotropy group of one orbit, and the manifold splits into curved orbits, each with an induced Cartan geometry (no normality assumed); for the normal conformal connection with a parallel standard tractor of nonzero norm the open curved orbits carry Einstein metrics $\sigma^{-2}g$ (Cap, Gover and Hammerl 2014).
