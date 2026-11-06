---
id: synthesis.non-abelian-gauge-fixing-has-gribov-copies-and-the-weak-rotor-lattice-with-doublets-has-a-perimeter-law
kind: claim
version: 2
title: 'Gribov copies in the weak factor and a perimeter law with doublets'
status: proved
region: synthesis
subject: quantum-fields
tags: [gauge-fields, rotors-and-stabilisers, no-go, finite-models, recovers-known-physics]
proposed_by:
  kind: ai
  session: 2026-11-02-qft-full
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.field-theory.single-algebra-field
imported_from:
- citation: 'H. Neuberger, Nonperturbative BRS invariance and the Gribov problem, Phys. Lett. B 183 (1987), 337.'
  key: Neuberger1987
  locator: 'the statement (signed sum over lattice Gribov copies equals the Euler characteristic of the group, so lattice BRST expectation values are 0/0) read through the account of Kalloniatis, von Smekal and Williams; imported in Fact synthesis.imported-singer-gauge-slice-neuberger-lattice-brst-and-fradkin-shenker-complementarity (ii)'
- citation: 'A. C. Kalloniatis, L. von Smekal and A. G. Williams, Curci-Ferrari mass and the Neuberger problem, arXiv:hep-lat/0501016.'
  key: KalloniatisVonSmekalWilliams2005
  locator: 'Introduction and the one-link model (read in the arXiv text)'
- citation: 'E. Fradkin and S. H. Shenker, Phase diagrams of lattice gauge theories with Higgs fields, Phys. Rev. D 19 (1979), 3682.'
  key: FradkinShenker1979
  doi: 10.1103/PhysRevD.19.3682
  locator: 'for a Higgs field in the fundamental representation the Higgs and confinement regions are analytically connected; imported in Fact synthesis.imported-singer-gauge-slice-neuberger-lattice-brst-and-fradkin-shenker-complementarity (iii)'
- citation: 'I. M. Singer, Some remarks on the Gribov ambiguity, Commun. Math. Phys. 60 (1978), 7.'
  key: Singer1978
  locator: 'no continuous global gauge slice for a non-abelian group on the three-sphere or the four-sphere; imported in Fact synthesis.imported-singer-gauge-slice-neuberger-lattice-brst-and-fradkin-shenker-complementarity (i)'
derivations:
- name: main
  uses:
  - synthesis.weak-factor-rotor-lattice-strong-coupling-area-law@2
  - synthesis.imported-wilson-lattice-gauge-theory-and-strong-coupling-confinement@1
  - synthesis.imported-brst-kugo-ojima-strocchi-and-gribov@1
  - synthesis.imported-singer-gauge-slice-neuberger-lattice-brst-and-fradkin-shenker-complementarity@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_identity_rotor_map_is_a_coulomb_copy_of_zero_on_the_three_sphere
- kind: check
  ref: check.py::check_lattice_landau_gauge_has_a_copy_of_the_trivial_field_outside_the_gribov_region
- kind: check
  ref: check.py::check_signed_faddeev_popov_count_is_the_euler_characteristic_zero
- kind: check
  ref: check.py::check_doublet_wilson_loop_has_a_perimeter_law_at_beta_zero
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts
  - synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields
  - synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum
  - synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces
extraction:
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, by Leon''s list of routine imports of 2026-11-02: a uses edge to the new Fact synthesis.imported-singer-gauge-slice-neuberger-lattice-brst-and-fradkin-shenker-complementarity@1 (Singer 1978, Neuberger 1987, Fradkin-Shenker 1979, checked against sources), which replaces the citations from memory; the reading in this note brought into line with the formal level (a non-perturbative definition available to the series for the weak factor, proposed as a reading). Statement and check unchanged.'
  open_problem: op.qft-non-abelian-gauge-fields
  note: >-
    Bears on the problem's second attack line (confinement and the Gribov ambiguity beyond perturbation theory). What is computed is the Coulomb condition on a round spatial three-sphere and the lattice Landau condition, not the series' covariant flat-space gauge, for which the general statement is the imported Gribov and Singer results.
    Three standard facts, recomputed exactly in the rotors of the weak factor. (1) Gribov copies: the
    Maurer-Cartan form of the stereographic identity rotor map is a nonzero pure gauge field obeying the Coulomb
    condition of the round three-sphere (a polynomial identity), while an abelian pure gauge copy of zero there
    would need a nonconstant harmonic function; on a 4 x 2 rotor lattice the Landau gauge has a copy of the
    trivial field whose Faddeev-Popov form has two negative modes; the copy itself has a compact U(1) analogue, only its negative modes are non-abelian. (2) The signed count: on a two-site lattice the
    two copies have Faddeev-Popov signs +1 and -1, summing to the Euler characteristic of the three-sphere, zero;
    Neuberger's theorem (imported, synthesis.imported-singer-gauge-slice-neuberger-lattice-brst-and-fradkin-shenker-complementarity) gives zero for every compact group on every lattice, so lattice BRST expectation
    values are 0/0. (3) With a frozen fundamental doublet, the Wilson loop at beta = 0 is c(kappa)^P exactly,
    c = kappa/4 - kappa^3/96 + ..., a perimeter law, so with the series' two fundamental doublets (input, not derived) the stored
    strong-coupling area law is no confinement criterion for the weak factor (Fradkin-Shenker complementarity,
    imported in the same Fact). Reading: the Krein premise's BRST quantisation is a perturbative device; a non-perturbative definition
    available to the series for the weak factor, proposed here as a reading and adopted by no stored result, is the
    gauge-invariant rotor lattice, which needs no gauge fixing, no ghosts and no indefinite
    form, its positivity coming from reflection positivity (stored Fact). Pure-colour confinement in the
    continuum is the open Yang-Mills mass-gap question and is not addressed. Transport-absent.
---

## formal
Units and signature of the store. Rotors of the weak factor are $U = u_{0} + u_{1}B_{1} + u_{2}B_{2} + u_{3}B_{3}$ in the even subalgebra of $\Cl(3,0)$, $U\widetilde U = 1$, with $B_{1} = g_{2}g_{3}$, $B_{2} = g_{3}g_{1}$, $B_{3} = g_{1}g_{2}$ and the normalised Haar measure, as in Theorem \claimref{synthesis.weak-factor-rotor-lattice-strong-coupling-area-law}. A gauge transformation by a rotor field $g$ acts as $A \mapsto \widetilde gAg + \widetilde g\,dg$ on a bivector-valued field and as $U_{xy} \mapsto g_{x}U_{xy}\widetilde{g_{y}}$ on links.
\begin{enumerate}
\item[(i)] \emph{(A continuum Gribov copy; proved.)} Let $q(x) = \big((1 - r^{2}) + 2\sum_{k}x_{k}B_{k}\big)/(1 + r^{2})$ on $\mathbb{R}^{3}$, $r^{2} = \sum_{k}x_{k}^{2}$, the stereographic chart of the unit rotors, and $\Omega = 2/(1 + r^{2})$, so that $\Omega^{2}\delta_{ij}$ is the round metric of the three-sphere. Then $q\widetilde q = 1$, and $A_{i} = \widetilde q\,\partial_{i}q$, the gauge transform of the zero field by $q$, is nonzero ($A_{1}(0) = 2B_{1}$) and obeys $\sum_{i}\partial_{i}(\Omega A_{i}) = 0$, the Coulomb condition of the round three-sphere, but not the flat condition $\sum_{i}\partial_{i}A_{i} = 0$. The round three-sphere is here a compactified spatial slice, the setting of Gribov and Singer; the series' background is flat, where the copies are Gribov's large-field ones, not computed here. For an abelian field a pure gauge copy $A = d\theta$ of zero obeying the same condition has $\Delta\theta = 0$ on the compact three-sphere, so $\theta$ is constant and $A = 0$.
\item[(ii)] \emph{(A lattice copy outside the Gribov region; computed.)} On the periodic $4 \times 2$ square lattice let $F_{U}(g) = \sum_{\ell}\langle g_{x}U_{\ell}\widetilde{g_{y}}\rangle_{0}$, whose stationary points in $g$ are the configurations in lattice Landau gauge. The trivial field $U = 1$ and its transform by $g_{(x,y)} = B_{3}^{x}$, whose links are $-B_{3}$ along the first axis and $1$ along the second, are both in lattice Landau gauge, with $F = 16$ and $8$. The Faddeev-Popov form (minus the second variation of $F$ along $g_{x} = \exp(\epsilon w_{x})$) has signature $(21, 0, 3)$ at the trivial field (positive apart from the three global modes) and $(14, 2, 8)$ at the copy: two negative modes. The copy is generated by the abelian subgroup of $B_{3}$ and has a compact $U(1)$ analogue (links $-B_{3}$ in the group $a + bB_{3}$); its two negative Faddeev-Popov modes are non-abelian (they couple the $B_{1}$, $B_{2}$ components at neighbouring sites).
\item[(iii)] \emph{(The signed count; computed, with the general statement cited.)} On two sites joined by two links with $U_{1} = 1$, $U_{2} = \tfrac{7}{25} + \tfrac{24}{25}B_{3}$, and the rotor at the first site fixed, $F(g) = \langle gM\rangle_{0}$ with $M = \widetilde{U_{1}} + U_{2}$, $M\widetilde M = \tfrac{64}{25}$; its stationary points are exactly $g = \pm\tfrac58\widetilde M$, with Faddeev-Popov forms of signatures $(3,0,0)$ and $(0,3,0)$, so the signs of the Faddeev-Popov determinants are $+1$ and $-1$ and their sum is $0$, the Euler characteristic of the three-sphere. For every compact group, $U(1)$ included, and every finite lattice, the signed sum over lattice Gribov copies is the Euler characteristic of the group of gauge transformations, zero, so the BRST gauge-fixed lattice partition function vanishes and gauge-fixed expectation values are $0/0$ \cite{Neuberger1987, KalloniatisVonSmekalWilliams2005}.
\item[(iv)] \emph{(Perimeter law with a fundamental doublet; proved at $\beta = 0$.)} Add to the weight a frozen doublet, a unit rotor $\varphi_{x}$ at each site, with hopping term $\kappa\sum_{\ell}\langle\widetilde{\varphi_{x}}U_{\ell}\varphi_{y}\rangle_{0}$. At $\beta = 0$, for every closed path $C$ that uses $P$ distinct links once each, $\langle\langle U_{C}\rangle_{0}\rangle = c(\kappa)^{P}$ exactly, with $c(\kappa) = \int u_{0}e^{\kappa u_{0}}dU/\int e^{\kappa u_{0}}dU = \tfrac{\kappa}{4} - \tfrac{\kappa^{3}}{96} + O(\kappa^{5})$; at $\kappa = 0$ every such loop vanishes. So $\langle\langle U_{C}\rangle_{0}\rangle$ decreases as the exponential of the perimeter, not the area. For the two-link loop the expansion integrated over sites and links without gauge fixing is $\tfrac{\kappa^{2}}{16} - \tfrac{\kappa^{4}}{192} + O(\kappa^{6}) = c(\kappa)^{2}$ (computed).
\end{enumerate}
\emph{Reading (argued).} The covariant BRST quantisation that the Krein premise \claimref{synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields} licenses is a perturbative device: beyond perturbation theory the Coulomb and Landau conditions have copies ((i), (ii); in general Gribov, Fact \claimref{synthesis.imported-brst-kugo-ojima-strocchi-and-gribov}(iv), and Singer's theorem \cite{Singer1978}, Fact \claimref{synthesis.imported-singer-gauge-slice-neuberger-lattice-brst-and-fradkin-shenker-complementarity}(i)), and the lattice version of BRST gives $0/0$ (iii). A non-perturbative definition available to the series for the weak factor, proposed here as a reading and not adopted by any stored result, is the gauge-invariant rotor lattice, which needs no gauge fixing, no ghosts and no indefinite form: reflection positivity gives its positive Hilbert space (Fact \claimref{synthesis.imported-wilson-lattice-gauge-theory-and-strong-coupling-confinement}(ii)); no colour lattice is stored. The two fundamental doublets are input (\claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum}), not derived, and the frozen doublet of (iv) is the standard proxy for them. With them, Wilson loops have a perimeter law at strong coupling (iv), and the Higgs and confinement regions are analytically connected \cite{FradkinShenker1979} (Fact \claimref{synthesis.imported-singer-gauge-slice-neuberger-lattice-brst-and-fradkin-shenker-complementarity}(iii)). The stored area-law theorem already says its area law is not evidence of confinement; what is added is the perimeter law with the doublet. Whether pure colour confines in the continuum, with the asymptotic freedom computed in \claimref{synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces}, is not addressed.

## technical
Fixing a gauge for a non-abelian field is unique only in perturbation theory; for the covariant gauges of the series' BRST quantisation the general statement is Gribov's and Singer's, imported. In the rotors of the weak factor three standard facts are recomputed exactly, for the Coulomb condition on a round spatial three-sphere and the lattice Landau condition. First, the stereographic identity map from space to the unit rotors gives a nonzero pure gauge field that obeys the Coulomb condition of the round three-sphere, an exact polynomial identity; an abelian field has no such copy there. On a 4 x 2 rotor lattice the Landau gauge has a copy of the trivial field at which the Faddeev-Popov form has two negative modes, outside the Gribov region; the copy has a compact U(1) analogue, and only its negative modes are non-abelian. Second, on a two-site lattice the two copies carry Faddeev-Popov signs +1 and -1, summing to the Euler characteristic of the three-sphere, zero; Neuberger's theorem extends this to every compact group and lattice, so the lattice version of BRST gives 0/0. Third, with a frozen doublet in the fundamental representation the Wilson loop at infinite gauge coupling is c(kappa)^P exactly, a perimeter law, so with the series' two fundamental doublets, taken as input, the perimeter term overtakes the stored strong-coupling area law, which the store already does not count as evidence of confinement (Fradkin-Shenker). The reading: the indefinite form and the ghosts are a perturbative tool, while the gauge-invariant rotor lattice, which needs neither, is a non-perturbative definition available for the weak factor, positive by reflection positivity. Continuum confinement of pure colour is not addressed. Transport-absent.

## lay
To calculate with force fields such as the gluons and the W and Z, physicists usually pick one representative from each family of physically identical field configurations. For these fields the choice cannot be made cleanly: some families meet the selection rule more than once, and on a lattice the duplicates cancel each other exactly. This result shows both effects in the series' own rotation algebra. It also shows that, once the Higgs fields are included, the lattice test usually used for confinement, how a loop of field lines decays with its area, no longer applies to the weak force. The lattice formulation, which never picks representatives, needs neither the series' assumed indefinite form nor the auxiliary ghost fields.

## one-liner
In the rotors of the weak factor, for the Coulomb condition on a round spatial three-sphere and the lattice Landau condition (not the series' covariant flat-space gauge, for which Gribov and Singer are imported): the identity rotor map gives a Coulomb-gauge copy of zero (none for an abelian field); a lattice Landau-gauge copy of the trivial field, with a U(1) analogue, has two non-abelian negative Faddeev-Popov modes; on two sites the signed count of copies is $1 - 1 = 0$, the Euler characteristic, as Neuberger's theorem gives in general; with a frozen fundamental doublet (the two doublets are input) the Wilson loop at $\beta = 0$ is $c(\kappa)^{P}$, $c = \kappa/4 - \kappa^{3}/96 + \dots$, a perimeter law; BRST under the Krein premise is perturbative and the gauge-invariant lattice, a non-perturbative definition available for the weak factor, needs no Krein form; transport-absent.
