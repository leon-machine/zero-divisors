---
id: synthesis.circulant-charged-leptons-excluded-with-real-neutrino-sectors
kind: claim
version: 3
title: 'The Koide circulant as charged-lepton matrix against the global fit'
status: proved
region: synthesis
subject: neutrinos
tags: [flavour-and-mixing, no-go, confronted-with-data, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-01-five-fronts
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
review: draft
derivations:
- name: main
  uses:
  - synthesis.koide-channel-phase-is-no-symmetry-angle@3
  - synthesis.series-family-structures-give-no-lopsided-second-stage@3
  - synthesis.theta23-at-s3-s2-direction@3
  - neutrino.breaking-relation@3
  - synthesis.residual-s2-decouples-first-family-from-ckm-and-pmns@2
  - synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix@3
  - synthesis.imported-nufit-6-oscillation-parameter-ranges@1
  - synthesis.imported-harrison-scott-mu-tau-reflection@1
  - synthesis.imported-takagi-factorisation@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_circulants_are_diagonal_in_the_fourier_basis
- kind: check
  ref: check.py::check_real_neutrino_frames_give_equal_conjugate_rows
- kind: check
  ref: check.py::check_odd_state_column_for_s2_invariant_neutrino_sectors
- kind: check
  ref: check.py::check_assignments_against_the_global_fit
- kind: check
  ref: check.py::check_every_placement_excluded_for_p12_invariant_sectors
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.koide-channel-phase-is-no-symmetry-angle
  - synthesis.theta23-at-s3-s2-direction
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The cube root of unity omega, the circulant phase b = |b| e^{I_4 delta}, the Hermitian-circulant decomposition, the overall neutrino phase and the Takagi phases are written with I_4 (numbers read in span{1, I_4}); nothing stays.'
  open_problem: op.second-order-breaking
  note: 'Answers the attack line that asks to reconcile the two charged-lepton structures in the store, the circulant reading of the Koide parametrisation and the texture c(J + delta_c E) of the neutrino paper, or to decide which one the second stage acts on; the same line appears in op.non-gaussian-completion (its third attack line). The decision is made by computing what each structure does to the lepton mixing matrix with the series neutrino sector. The stored textures have real coefficients; under the su(2)_R-covariant completion (synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix) the Dirac neutrino matrix alpha Y + conj(beta) Ytilde and M_R = v_R f are complex for generic frame coefficients and family matrices (real only on relatively real sub-branches), so the real-sector clauses do not reach that branch; the residual-S2 clause does, real or complex. The key identity is elementary: the Fourier vectors f_1 and f_2 are complex conjugates, so their overlaps with any real vector have equal moduli. A circulant charged-lepton matrix together with a real neutrino mass matrix therefore gives mu-tau reflection symmetry when the electron sits on the democratic line; this is the pattern of Harrison and Scott (hep-ph/0210197, imported as the Fact synthesis.imported-harrison-scott-mu-tau-reflection: mu-tau reflection, |U_mu i| = |U_tau i|; they attribute the circulant-basis case to an earlier paper, not checked). Clause (i) restates clauses (i) and (ii) of synthesis.series-family-structures-give-no-lopsided-second-stage (there S e_j = e_{j+1}; here (Sx)_i = x_{i+1}, the transpose, so A here is minus the stored A, the same line). The new content is (ii) to (iv), applied to the store: the stored representative of the circulant reading puts the tau on the democratic line, which the global fit excludes for every real neutrino sector; the other two placements are treated too. Placement of a charged lepton on the democratic line is physical once the family basis is shared with the neutrino sector: permutations of the families fix f_0, so the shift of the channel phase by 2 pi/3, which the circulant-reading result counts among relabellings of the square-root-mass vector, here changes the matrix. The NuFIT 6.0 three-sigma ranges (arXiv:2410.05380, Table 1) are imported as the Fact synthesis.imported-nufit-6-oscillation-parameter-ranges, and the Takagi factorisation as synthesis.imported-takagi-factorisation; the result uses the union of its four data sets, and combines one-dimensional ranges, which is conservative for an exclusion. Free numbers: none; look-elsewhere count: three placements. Transport-absent (flavour linear algebra and data).'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: the NuFIT 6.0 ranges, the Harrison-Scott mu-tau reflection pattern and the Takagi factorisation now cite imported Facts (uses edges added, claimrefs in the formal statement, the technical level and the proof; Harrison-Scott added to the references); the pins to synthesis.series-family-structures-give-no-lopsided-second-stage and synthesis.koide-channel-phase-is-no-symmetry-angle moved to their versions 2 (pointer notes added there). No clause changed.'
---

## formal
Work in the family basis of the textures of Proposition \claimref{synthesis.theta23-at-s3-s2-direction}, with $S$ the cyclic shift $(Sx)_{i} = x_{i+1}$ (the transpose of the shift of Proposition \claimref{synthesis.series-family-structures-give-no-lopsided-second-stage}), $P_{12}$ the exchange of the first two families, $u' = (1, 1, 1)$, $A = S - S^{\mathsf{T}}$ (minus the $A$ of that Proposition, the same sign line), $\omega = e^{2\pi I_{4}/3}$ (numbers are read in $\mathrm{span}\{1, I_{4}\}$) and $f_{k} = (1, \omega^{k}, \omega^{2k})/\sqrt3$. Read the projected coherent vector as the $\sqrt{m}$ vector of a circulant $C = a\mathbb{1} + bS + \bar{b}S^{\mathsf{T}}$ acting on that basis (the circulant reading of Proposition \claimref{synthesis.koide-channel-phase-is-no-symmetry-angle}), whose eigenvalue on $f_{k}$ is $p_{k}$; the stored representative there ($0 < \delta < \tfrac{\pi}{12}$, $p_{1} < p_{2} < p_{0}$) puts the tau on the democratic line $f_{0}$. For a complex symmetric neutrino mass matrix $m_{\nu}$ with Takagi vectors $\nu_{j}$ (Fact \claimref{synthesis.imported-takagi-factorisation}), let $U_{\alpha j} = \langle f_{k(\alpha)}, \nu_{j}\rangle$, $k(\alpha)$ the Fourier line of the charged lepton $\alpha$.
\begin{enumerate}
\item[(i)] \emph{(The two charged-lepton structures; this restates clauses (i) and (ii) of Proposition \claimref{synthesis.series-family-structures-give-no-lopsided-second-stage}.)} Every circulant, and so $CC^{\dagger}$, is diagonal on the $f_{k}$ for every channel phase. Under conjugation by $S_{3}$ the circulants span the trivial lines $\mathbb{1}$, $\J$ and the sign line $A$; every $P_{12}$-invariant matrix, in particular $c^{2}(\J + \delta_{c}E)^{2}$, has no component on $A$. So a Hermitian circulant is $P_{12}$-invariant exactly when it lies in $\mathrm{span}\{\mathbb{1}, \J\}$, and $(\J + \delta_{c}E)^{2}$ with $\delta_{c} \ne 0$ is not a circulant: the two structures share the democratic term and nothing else.
\item[(ii)] \emph{(Real neutrino sectors.)} If $m_{\nu}$ is real up to an overall phase, then $|U_{f_{1}j}| = |U_{f_{2}j}|$ for $j = 1, 2, 3$, and $|U_{f_{0}j}| = |\nu_{j}\cdot u'|/\sqrt3$ with $\nu_{j}$ chosen real.
\item[(iii)] \emph{(Residual $S_{2}$, real or complex.)} If $P_{12}m_{\nu}P_{12} = m_{\nu}$, with $m_{\nu}$ real or complex (the textures of Proposition \claimref{synthesis.theta23-at-s3-s2-direction} at the $S_{3} \to S_{2}$ direction; equally the seesaw built from the Dirac matrix $\alpha Y + \bar{\beta}\tilde{Y}$ of Theorem \claimref{synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix} with complex $P_{12}$-invariant $Y$, $\tilde{Y}$ and a complex $P_{12}$-invariant $M_{R}$), then $(1, -1, 0)/\sqrt2$ is, up to a phase, a Takagi vector, and its column has squared moduli $(0, \tfrac12, \tfrac12)$ on $(f_{0}, f_{1}, f_{2})$.
\item[(iv)] \emph{(Against the global fit.)} The three-sigma ranges of \cite{NuFIT2024} (Fact \claimref{synthesis.imported-nufit-6-oscillation-parameter-ranges}; union of its four data sets: $\sin^{2}\theta_{13} \in [0.02023, 0.02409]$, $\sin^{2}\theta_{23} \in [0.430, 0.597]$, $\sin^{2}\theta_{12} \in [0.275, 0.345]$) give $|U_{e1}|^{2} \in [0.639, 0.711]$, $|U_{e2}|^{2} \in [0.268, 0.339]$, $|U_{e3}|^{2} \le 0.0241 < 0.393 < |U_{\tau 3}|^{2}$ and $0.419 < |U_{\mu 3}|^{2}$. Hence: (a) for every $P_{12}$-invariant neutrino sector, real or complex, every placement is excluded, since by (iii) the electron row holds $0$ (electron on $f_{0}$) or $\tfrac12$ (electron on $f_{1}$ or $f_{2}$), in none of the ranges; (b) for $m_{\nu}$ real up to a phase, the tau or the muon on $f_{0}$ is excluded at every order of the breaking, since by (ii) $|U_{e3}|$ would equal $|U_{\mu 3}|$ or $|U_{\tau 3}|$; (c) the electron on $f_{0}$ with a real $P_{12}$-breaking $m_{\nu}$ gives $|U_{\mu j}| = |U_{\tau j}|$ for all $j$, hence $\sin^{2}\theta_{23} = \tfrac12$ and, when $s_{12}c_{12}s_{13} \ne 0$, $\cos\delta_{CP} = 0$; (d) for a complex $P_{12}$-breaking $m_{\nu}$ there is no statement.
\end{enumerate}
So on the real-neutrino branch (the stored textures) the Koide circulant at its stored placement is not the charged-lepton matrix in the neutrino textures' family basis. On the complex branch that the $\su(2)_{R}$-covariant completion gives for generic couplings, it is excluded while the neutrino sector keeps $P_{12}$ and undecided once $P_{12}$ is broken there.

## technical
The store holds two descriptions of the charged leptons. One reads the Koide parametrisation as a circulant matrix of square-root masses, with a channel phase $\delta$ that encodes $m_{\mu}/m_{e}$; the other is the neutrino paper's texture $c(\J + \delta_{c}E)$, which keeps the exchange of the first two families. This result asks what the circulant does to lepton mixing when it is taken as the charged-lepton matrix in the same family basis as the neutrino textures. A circulant is diagonal on the Fourier vectors $f_{0} = u'/\sqrt3$, $f_{1}$, $f_{2}$ for every phase and, as the stored sign-line result already shows, shares only the democratic term with the exchange-invariant texture. Two facts decide the mixing. If the neutrino sector keeps the exchange, real or complex, the odd neutrino state has overlaps $0$, $\tfrac12$, $\tfrac12$ with the three Fourier lines, so the electron row would hold $0$ or $\tfrac12$; the global fit allows neither, whichever lepton sits where. If the neutrino mass matrix is real, as in the stored textures, the conjugate lines $f_{1}$ and $f_{2}$ give equal moduli in their two rows; the fit forbids $|U_{e3}| = |U_{\mu 3}|$ and $|U_{e3}| = |U_{\tau 3}|$, so the stored placement (tau on the democratic line) and the muon placement fail at every order. With the electron there and a real exchange-breaking neutrino sector the result is the mu-tau reflection pattern of Harrison and Scott (hep-ph/0210197; Fact \claimref{synthesis.imported-harrison-scott-mu-tau-reflection}): maximal $\theta_{23}$ and $\delta_{CP} = \pm 90^{\circ}$. The $\su(2)_{R}$-covariant completion makes the Dirac neutrino matrix and the Majorana matrix complex for generic couplings; there the exclusion holds only while the neutrino sector keeps the exchange. No number is fitted.

## lay
The theory has two different descriptions of how the electron, muon and tau masses arise. One arranges the square roots of the three masses in a pattern that repeats when the three families are cycled; the other, used for neutrinos, singles out one family. This result checks what the first description would do to the way neutrinos mix with the charged leptons, if both live in the same set of family directions. If the neutrino masses still single out that family, every arrangement fails against the measured mixing. If the neutrino masses carry no complex phase (as in the neutrino paper's textures; the newer two-coupling completion generally gives complex ones), two of the charged leptons must mix with each neutrino by the same amount; in the arrangement the theory currently uses those two are the electron and the muon, which measurements say mix very differently. The cyclic description survives only with complex neutrino masses that do not single out a family, or with the electron as the special family member and real neutrino masses, in which case the muon and tau mix equally and two measurable angles are fixed: one at 45 degrees and the matter-antimatter phase at plus or minus 90 degrees.

## one-liner
Taken as the charged-lepton matrix in the neutrino textures' family basis, the Koide circulant is excluded by the global fit at every placement for every $P_{12}$-invariant neutrino sector, real or complex, and, for a real neutrino mass matrix (as stored), at the stored placement (tau on the democratic line) and the muon placement at every order; the electron placement with a real $P_{12}$-breaking sector gives mu-tau reflection ($\sin^{2}\theta_{23} = \tfrac12$, $\cos\delta_{CP} = 0$), and a complex $P_{12}$-breaking sector, generic under the $\su(2)_{R}$-covariant completion, is left open.
