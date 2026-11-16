---
id: synthesis.imported-physical-colour-angle-and-its-shift-under-quark-rephasing
kind: claim
version: 1
title: 'Imported: the physical colour angle and its shift under a rephasing of the quarks'
status: imported
region: synthesis
subject: standard-model
tags: [gauge-fields, hypercharge-and-anomalies, undetermined-input]
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
- citation: 'R. D. Peccei, The strong CP problem and axions, in Axions: Theory, Cosmology, and Experimental Searches, Lect. Notes Phys. 741, Springer (2008), 3--17; arXiv:hep-ph/0607268.'
  key: Peccei2008
  locator: 'arXiv version, equations (1), (2) and (17) to (20) with the text around them'
- citation: 'K. Fujikawa, Path-integral measure for gauge-invariant fermion theories, Phys. Rev. Lett. 42 (1979), 1195--1198.'
  key: Fujikawa1979
  doi: 10.1103/PhysRevLett.42.1195
  locator: 'abstract; equations (4), (15) and (21)'
- citation: 'J. Dragos, T. Luu, A. Shindler, J. de Vries and A. Yousif, Confirming the existence of the strong CP problem in lattice QCD with the gradient flow, Phys. Rev. C 103 (2021), 015202; arXiv:1902.03254.'
  key: Dragos2021
  doi: 10.1103/PhysRevC.103.015202
  locator: 'section 2 (the definition of the physical angle)'
- citation: 'D. Boer and J. K. Boomsma, Spontaneous CP-violation in the strong interaction at theta = pi, Phys. Rev. D 78 (2008), 054027; arXiv:0806.1669.'
  key: BoerBoomsma2008
  doi: 10.1103/PhysRevD.78.054027
  locator: 'abstract, introduction and section V'
extraction:
  note: >-
    Imported by Leon's decision D1 of 16 November 2026, so that the registration of the physical colour angle
    (synthesis.colour-angle-registered-free-input) and the two results it rests on cite a stored Fact for the
    definition of the physical angle instead of the literature from memory. What was read at source on
    16 November 2026, and what was not. Read: Peccei, arXiv:hep-ph/0607268 (the arXiv text, through its HTML
    rendering): equation (1), the divergence of the axial current with the coefficient g^2 N/(32 pi^2);
    equation (2), the rotation q_f -> exp(i alpha gamma_5/2) q_f; equation (17), the term
    theta (g^2/32 pi^2) F F-dual, with the sentence that it violates parity and time reversal and conserves
    charge conjugation, so violates CP; equation (18), exp(i alpha Q_5) taking the vacuum of angle theta to
    that of angle theta + alpha, with the sentence that chiral transformations, because of the anomaly, can
    change the vacuum angle; equation (19), the mass term with a general complex matrix M; the sentence that
    to reach a physical basis one diagonalises M by a chiral transformation which changes theta by
    Arg Det M; equation (20), theta-bar = theta + Arg Det M; and the sentence that the strong CP problem is
    why this angle is so small. The source rotates the quarks by alpha/2 in (2) and shifts the angle by alpha
    in (18) without relating the two normalisations for N flavours; clause (ii) reports both as printed and
    draws no factor from them. The book reference of that review (volume and pages) is cited from memory;
    the arXiv text carries no journal reference. Read: Fujikawa 1979, a scan of the published letter: the
    title, the abstract (the measure is not invariant under the gamma_5 transformation and the Jacobian
    gives an extra phase factor corresponding to the anomaly), the transformation (4) and the factor (15)
    with coefficient 1/(8 pi^2) on the integral of eta times Tr(*F F), N times it for N flavours in (21);
    the scan was not legible enough to check the sign of the exponent, which is therefore not stated here.
    Read: Dragos et al., arXiv:1902.03254, section 2: the phase of the quark mass matrix is absorbed in the
    physical parameter theta-bar = theta + arg det(M). Read: Boer and Boomsma, arXiv:0806.1669: only for
    theta = 0 modulo pi is the Lagrangian CP-conserving; at theta = pi spontaneous CP violation could arise
    (Dashen); in the two-flavour Nambu and Jona-Lasinio model in the mean-field approximation its occurrence
    depends on the strength of the 't Hooft determinant interaction, taking place above a critical value
    (about 0.008 for up and down masses of 6 MeV, in that paper's parametrisation). Not read at source and
    not used as a source here: 't Hooft 1976 (Phys. Rev. Lett. 37, 8; Phys. Rev. D 14, 3432), the original
    of the vacuum angle and of the anomalous non-conservation of the axial charge, and Dashen 1971, both
    cited from memory. Not imported: any statement that a physical angle of a half turn is excluded by the
    hadron spectrum.
  source_formal: >-
    Peccei: L_theta = theta (g^2/32 pi^2) F_a^{mu nu} F-dual_{a mu nu} (17); d_mu J_5^mu =
    (g^2 N/32 pi^2) F_a^{mu nu} F-dual_{a mu nu} (1) for q_f -> e^{i alpha gamma_5/2} q_f (2);
    e^{i alpha Q_5}|theta> = |theta + alpha> (18); L_Mass = qbar_{iR} M_{ij} q_{jL} + h.c. (19);
    theta-bar = theta + Arg Det M (20). Fujikawa: psi -> exp[i eta(x) gamma_5] psi (4), measure factor
    exp[(sign not checked) i int eta(x) (1/8 pi^2) Tr(*F^{mu nu} F_{mu nu}) d^4x] (15). The sources write i
    for I_4, and gamma_5 for the chirality element, whose two eigenspaces are the chiral halves named in
    the formal level.
  maintainer_pass_2026_11_16:
    by: maintainer-2026-11-16
    date: '2026-11-16'
    note: 'New imported Fact, created at Leon''s decision D1 of 16 November 2026 with the registration of the physical colour angle. Each clause says which source states it; the note says what was read at source and what is cited from memory.'
---

## formal
Numbers are read in $\mathrm{span}\{1, I_{4}\}$ (conventions U1; the sources write $i$ for $I_{4}$), $\operatorname{Arg}$ is the angle of a number in that plane and $\operatorname{Det}$ the determinant. The colour gauge field has coupling $g$, field-strength components $F_{a}^{\mu\nu}$ and dual $\tilde{F}_{a\mu\nu} = \tfrac12\epsilon_{\mu\nu\alpha\beta}F_{a}^{\alpha\beta}$; the two chiral halves of a quark field are its left-handed and right-handed parts $q_{L}$, $q_{R}$.
\begin{enumerate}
\item[(i)] \emph{(The angle term.)} The structure of the vacuum of the colour gauge theory adds to its Lagrangian the term
\[
L_{\theta} = \theta\,\frac{g^{2}}{32\pi^{2}}\,F_{a}^{\mu\nu}\tilde{F}_{a\mu\nu},
\]
with an angle $\theta$. The term is odd under space inversion and under time reversal and even under charge conjugation, so it is odd under their product CP \cite{Peccei2008}.
\item[(ii)] \emph{(Axial rotations move the angle.)} For $N$ quark flavours the axial rotation, which turns the two chiral halves of every quark field by the opposite phases $e^{\pm I_{4}\alpha/2}$, is not a symmetry of the quantum theory: its current $J_{5}^{\mu}$ has the divergence $\partial_{\mu}J_{5}^{\mu} = \frac{g^{2}N}{32\pi^{2}}F_{a}^{\mu\nu}\tilde{F}_{a\mu\nu}$ (the anomaly), and because of it chiral transformations change the vacuum angle: with $Q_{5}$ the axial charge, the source writes that $e^{I_{4}\alpha Q_{5}}$ takes the vacuum of angle $\theta$ to the vacuum of angle $\theta + \alpha$ \cite{Peccei2008}. In the functional integral the same fact is that the measure of the quark fields is not invariant under the axial rotation: under a rotation by a function $\eta(x)$ the measure of one flavour is multiplied by a phase factor whose exponent is $I_{4}\int\eta(x)\,\tfrac{1}{8\pi^{2}}\Tr({}^{*}F^{\mu\nu}F_{\mu\nu})\,d^{4}x$ up to a sign, in that source's normalisation (the coupling absorbed in $F$), and $N$ flavours give $N$ times the exponent; that factor is the anomaly \cite{Fujikawa1979}.
\item[(iii)] \emph{(The physical angle.)} With the weak interactions included, the quark mass matrix is a general matrix $M$ with entries in $\mathrm{span}\{1, I_{4}\}$, the mass term being $\bar{q}_{iR}M_{ij}q_{jL}$ plus its conjugate. Bringing $M$ to a physical basis, diagonal with real entries, takes a chiral transformation, which changes $\theta$ by $\operatorname{Arg}\operatorname{Det}M$. The coefficient of the term of (i) in the full theory is therefore
\[
\bar\theta = \theta + \operatorname{Arg}\operatorname{Det}M ,
\]
and the strong CP problem is the question why this angle is so small \cite{Peccei2008}. The same definition, the phase of the quark mass matrix absorbed in the physical parameter $\bar\theta = \theta + \arg\det(M)$, is the one used by the lattice conversion of the neutron dipole moment \cite{Dragos2021}.
\item[(iv)] \emph{(The half turn.)} The Lagrangian with the term of (i) conserves CP only for $\theta = 0$ modulo a half turn. At a half turn, $\theta = \pi$, CP can be broken spontaneously (Dashen's observation); in the two-flavour Nambu and Jona-Lasinio model in the mean-field approximation, whether it is broken depends on the strength of the instanton-induced determinant interaction, the breaking taking place above a critical strength \cite{BoerBoomsma2008}. So a half turn is not excluded by CP conservation of the Lagrangian, and whether the vacuum then breaks CP is model-dependent.
\end{enumerate}
\emph{In the store's variables (a translation of (iii); the sources do not write it so).} For the store's mass matrices $M_{u}$, $M_{d}$, $\operatorname{Arg}\operatorname{Det}M$ is the $I_{4}$ phase of $\det M_{u}\det M_{d}$. Clause (iii) applied to a matrix and to the same matrix after a rephasing of the quark fields gives the same coefficient in the full theory, so a rephasing moves $\theta$ and the phase of the determinant by opposite amounts and leaves $\bar\theta$. For one-parameter family rotations of the quark doublets and of the up-type and down-type singlets with anti-Hermitian generators $K_{Q}$, $K_{u}$, $K_{d}$, the determinant $\det M_{u}\det M_{d}$ turns through $(2\tr K_{Q} + \tr K_{u} + \tr K_{d})/I_{4}$ per unit parameter, so a rotation through $\phi$ shifts $\theta$ by $a_{3}\phi$ with $a_{3} = I_{4}^{-1}(2\tr K_{Q} + \tr K_{u} + \tr K_{d})$, the colour coefficient, up to a sign fixed by the convention for the rotation; only the magnitude is used in the store. The angle $\bar\theta$ is defined modulo a whole turn.

## technical
The colour gauge theory allows one extra term in its Lagrangian, the product of the field strength with its dual, multiplied by an angle. The term violates CP. Its coefficient is not physical on its own: because of the axial anomaly, turning the left-handed and right-handed halves of the quark fields by opposite phases is not a symmetry, and such a turn shifts the angle; in the functional integral this appears as a phase factor from the measure of the quark fields (Fujikawa). A general quark mass matrix has a determinant with a phase, and the rotation that makes the masses real moves that phase into the angle. What is physical is the sum, the coefficient of the term plus the phase of the determinant of the quark mass matrix; a rephasing of the quarks moves the two parts by opposite amounts and leaves the sum. In the store's variables the shift of the coefficient is the colour coefficient of the rotation times its angle. The Lagrangian conserves CP at an angle of zero and at a half turn; at a half turn CP may be broken spontaneously, and in the model study read here whether it is depends on the strength of the instanton-induced interaction.

## lay
The theory of the strong force permits a term whose strength is an angle. That angle is not meaningful by itself, because one can trade it against a phase in the quark masses by redefining the quark fields. What cannot be redefined away is the sum of the two, called the physical angle. The strong force respects the symmetry between matter and antimatter only if this physical angle is zero or exactly a half turn; at a half turn the symmetry can still break of its own accord, depending on details of the strong force that models treat differently.

## one-liner
The colour angle term $\theta\,\tfrac{g^{2}}{32\pi^{2}}F\tilde{F}$ is CP-odd; axial rotations of the quarks are anomalous and shift $\theta$; the physical angle is $\bar\theta = \theta + \operatorname{Arg}\operatorname{Det}M$, which a rephasing of the quarks leaves fixed (it shifts $\theta$ by the colour coefficient times the angle); CP is conserved by the Lagrangian only at $0$ and at a half turn, where its spontaneous breaking is model-dependent (Peccei 2008; Fujikawa 1979; Boer and Boomsma 2008).
