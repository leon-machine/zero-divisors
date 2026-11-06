---
id: synthesis.conjugate-reading-up-down-split-is-t3r-odd-or-cp-odd
kind: claim
version: 1
title: 'Under the conjugate reading, the up-down split is $T_{3R}$-odd or CP-odd'
status: proved
region: synthesis
subject: standard-model
tags: [flavour-and-mixing, mass-generation, no-go, representation-theory]
proposed_by:
  kind: ai
  session: 2026-11-01-weak-scale
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
derivations:
- name: main
  uses:
  - standard-model.one-vev-vector-relations-breaking-pattern@7
  - standard-model.invariant-pairing-five-modes@5
  - standard-model.yukawa-pattern-two-rung-module@5
  - standard-model.hyp-s-slot-statistics@9
  - standard-model.generation-ten-under-pati-salam@7
  - standard-model.automorphisms-preserve-slot-pair-split-are@6
  - synthesis.georgi-jarlskog-majorana-moment-map@3
  - synthesis.up-down-split-under-conjugate-reading-needs-su2r-odd-weighting@3
  - standard-model.imported-clebsch-structure-seesaw@1
  - standard-model.imported-spinor-bilinears@1
  - synthesis.second-doublet-of-one-family-coupling-gives-no-quark-mixing@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_symmetric_and_antisymmetric_entries_are_e_plus_o_and_e_minus_o
- kind: check
  ref: check.py::check_one_rung_vector_gives_proportional_mass_matrices
- kind: check
  ref: check.py::check_relatively_real_family_matrices_give_conjugate_squares
- kind: check
  ref: check.py::check_trace_law_two_channels
- kind: check
  ref: check.py::check_ten_plus_120_keeps_the_trace_and_splits_the_determinant
- kind: check
  ref: check.py::check_second_ten_splits_only_through_the_cp_channel
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.up-down-split-under-conjugate-reading-needs-su2r-odd-weighting
  - synthesis.second-doublet-of-one-family-coupling-gives-no-quark-mixing
extraction:
  open_problem: op.rung-unit
  note: >-
    The problem's fourth line of attack (a second 10 with its own Yukawa, or the 126 and an S2-odd 120)
    under the per-sector reading of up-type masses through the conjugate c* (down entries from the
    composite c_k g_k, up entries from c_k^* g_k, one family matrix per composite). That reading is not
    su(2)_R covariant: it sees only the beta half of each rung vector; its su(2)_R-covariant completion
    (Y on c and Yt on c* as wholes) is the subject of the result synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix, and the per-sector reading
    is that completion's leading mass reading. The stored results say one family
    matrix gives M_u = r M_d (any number of vevs) and that T3R-even weightings of one composite keep
    m_u = m_d. This result treats any number of composites c_k g_k of rung-4 vectors with diagonal
    weightings h_k(T3R, B - L), each with its own family matrix and its own rung vector, and finds exactly what can split up from down. Extending the stored parity argument to
    the antisymmetric (120-type) entries, every composite enters with real weights e + o (down) and e - o
    (up). Three consequences. Composites of ONE rung vector with T3R-even weightings (the 10, the
    Georgi-Jarlskog composite of the 126 route, and the 120-type entries of B - L, chi and mu_P), each with
    an independent complex family matrix, still give b M_u = conj(b) M_d: equal masses and V = 1, so under
    the per-sector reading an independent second family matrix on the same rung vector is not enough. (Under
    the covariant completion it is: the coupling Yt to c* of the same rung vector gives
    tr H_u - tr H_d = 2 m (|Y|^2 - |Yt|^2), odd under the mirror m -> -m, the T3R-odd channel below in
    another guise; synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix.) With several rung vectors and family matrices that are
    real up to one common phase, H_u is the complex conjugate of H_d: equal masses again, although the
    mixing can be nontrivial (the exact instance has det[H_u, H_d] != 0). The trace law splits the
    difference tr H_u - tr H_d into a T3R-odd channel and a CP channel, the product of two CP-odd relative
    phases (that of two rung vectors' frame coefficients, spontaneous, and that of their family matrices,
    explicit), a product that is itself CP-even; since a
    symmetric and an antisymmetric family matrix are trace-orthogonal, one 10 with one 120 keeps
    sum m_u^2 = sum m_d^2 for all complex data, against the record (m_t much larger than m_b at every
    scale, cited from memory), while their determinants split by a product of two CP-odd phases. A second 10 with its own
    rung vector does split up from down (exact instance), but only through the CP channel. So under the
    per-sector conjugate reading the split needs either a T3R-odd weighting (the stored Majorana-square route) or
    spontaneous and explicit CP phases together; the relative phase of two rung vectors is not fixed by
    the stored D-term action, which depends on each field's norm and moment map only (argued). The reading
    of several composites, each through its own c*, is the stored per-sector reading extended, stated as such.
    Transport-absent.
---

## formal
Under Hypothesis (S), on the sixteen (the particle half of Proposition \claimref{standard-model.hyp-s-slot-statistics}) with the pairing $B$ of Lemma \claimref{standard-model.invariant-pairing-five-modes}, let the sources $k = 1, \ldots, n$ be composites $c_{k}g_{k}$ of rung-$4$ vectors $c_{k} = a_{k}v_{4} + b_{k}w_{4}$ with diagonal weightings $g_{k} = h_{k}(T_{3R}, B - L)$, each paired with a complex family matrix $Y_{k}$, symmetric for the symmetric part of the mass form ($10$ and $126$ type) or antisymmetric for its antisymmetric part ($120$ type, Fact \claimref{standard-model.imported-spinor-bilinears}), and read as in Corollary \claimref{standard-model.one-vev-vector-relations-breaking-pattern} under the per-sector conjugate reading (one family matrix per composite feeding both sectors; this reading sees only the $b_{k}$ half of each rung vector and is not $\su(2)_{R}$ covariant): down-type and charged-lepton entries from $b_{k}w_{4}g_{k}$, up-type and Dirac-neutrino entries from $\bar{b}_{k}v_{4}g_{k}$, relative to the $10$ forms of $w_{4}$ and $v_{4}$ (Theorem \claimref{standard-model.yukawa-pattern-two-rung-module}). Write $H_{q} = M_{q}M_{q}^{\dagger}$.
\begin{enumerate}
\item[(i)] \emph{(Weights.)} On each sector, both the symmetric and the antisymmetric weight of a source are $d_{k} = e_{k} + o_{k}$ (down-type) and $u_{k} = e_{k} - o_{k}$ (up-type), $e_{k}$ and $o_{k}$ real and coming from the parts of $h_{k}$ even and odd in $T_{3R}$. So $M_{d} = \sum_{k} b_{k}d_{k}Y_{k}$ and $M_{u} = \sum_{k}\bar{b}_{k}u_{k}Y_{k}$ (lepton weights for $M_{e}$, $M_{\nu}$), the form of Fact \claimref{standard-model.imported-clebsch-structure-seesaw} with each up-type vev the conjugate of its down-type partner for $T_{3R}$-even sources. The antisymmetric weights of $B - L$, $\chi$ and $\mu_{P}$ (lepton, quark) are $(1, -\tfrac13)$, $(-1, -1)$ and $(-\tfrac{3}{16}, \tfrac{1}{16})$ in both sectors; $\mu_{R}$ and $X_{4}$ are odd in both parts.
\item[(ii)] \emph{(One rung vector.)} If every $o_{k} = 0$ and every $b_{k}$ is a real multiple of one $b$, then $bM_{u} = \bar{b}M_{d}$ and $bM_{\nu} = \bar{b}M_{e}$ whatever the family matrices: $m_{u_{i}} = m_{d_{i}}$, $m_{\nu_{i}}^{D} = m_{e_{i}}$ and $V = 1$.
\item[(iii)] \emph{(Relatively real family matrices.)} If every $o_{k} = 0$ and $Y_{k} = \omega R_{k}$ with $R_{k}$ real and one complex $\omega$, then $\bar{\omega}M_{u} = \omega\overline{M_{d}}$ for all frame coefficients, so $H_{u} = \overline{H_{d}}$ and the masses are equal family by family; the mixing need not be trivial.
\item[(iv)] \emph{(Trace law.)} With $t_{kl} = \tr(Y_{k}Y_{l}^{\dagger})$ and $p_{kl} = b_{k}\bar{b}_{l}$,
\[
\tr H_{u} - \tr H_{d} = -2\sum_{k,l}(e_{k}o_{l} + o_{k}e_{l})\operatorname{Re}t_{kl}\operatorname{Re}p_{kl} + 2\sum_{k,l}(e_{k}e_{l} + o_{k}o_{l})\operatorname{Im}t_{kl}\operatorname{Im}p_{kl},
\]
a $T_{3R}$-odd channel and a CP channel, the latter the product of two CP-odd relative phases, itself CP-even; $t_{kl} = 0$ when one of $Y_{k}$, $Y_{l}$ is symmetric and the other antisymmetric.
\item[(v)] \emph{(A $10$ with a $120$.)} For one symmetric source $S$ and one antisymmetric source $A$, $A_{ij} = \varepsilon_{ijk}a_{k}$, both $T_{3R}$-even with frame coefficients $b$ and $\gamma$ (weights absorbed in $S$ and $A$), $\tr H_{u} = \tr H_{d}$ for all complex data, while $\det H_{u} - \det H_{d} = -4|b|^{2}\operatorname{Im}(\det S\,\overline{a^{\mathsf T}Sa})\operatorname{Im}((\bar{b}\gamma)^{2})$.
\item[(vi)] \emph{(A second $10$; computed.)} Two $10$ sources with independent complex family matrices and frame coefficients of different phase give different spectra of $H_{u}$ and $H_{d}$ and $\det[H_{u}, H_{d}] \ne 0$ in an exact instance.
\end{enumerate}
So under the per-sector conjugate reading the up-down split needs a $T_{3R}$-odd weighting or the CP channel, which needs two rung vectors with a relative phase and family matrices with a relative phase of the same symmetry type; a second family matrix on the same rung vector, the Georgi-Jarlskog composite and the $120$ do not supply it, and a $10$ with one $120$ keeps $\sum m_{u}^{2} = \sum m_{d}^{2}$. Under the $\su(2)_{R}$-covariant completion, with $Y$ on $c$ and $\tilde{Y}$ on $c^{*}$ as wholes (\claimref{synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix}), one rung vector does split them, by $2m(c)(\|Y\|^{2} - \|\tilde{Y}\|^{2})$.

## technical
The series reads up-type masses through the conjugate of the rung vector; read sector by sector (down-type masses from the vector, up-type masses from its conjugate, one family matrix per coupling), one coupling makes up and down quarks equally heavy. This sector-by-sector reading is the leading mass reading of a left-right covariant coupling, and it is the one used here. The open question is which additions split them. Every dressing of a rung vector enters the down-type and up-type mass matrices with real weights $e + o$ and $e - o$, where $o$ is the part of the dressing that changes sign with the right-handed isospin; this holds for the symmetric couplings of the $10$ and $126$ type and, shown here, for the antisymmetric couplings of the $120$ type. From that one structure: dressings of a single rung vector that do not see the sign of right-handed isospin give an up-type matrix proportional to the down-type one, however many independent family matrices they carry, so equal masses and no mixing. With several rung vectors and family matrices sharing one complex phase, the up-type matrix is the complex conjugate of the down-type one and the masses are again equal. In general the difference of the summed squared masses is an exact two-term law: a term from isospin-odd dressings and a CP term, the product of two CP-odd relative phases, one of two rung vectors and one of their family matrices (the product itself is CP-even). A symmetric and an antisymmetric family matrix never interfere in it, so a $10$ with a single $120$ cannot make the summed squared up-type masses differ from the down-type ones. A second $10$ with its own rung vector can split them, but only through the CP term. The left-right covariant coupling, with its own family matrix on the conjugate of the same rung vector, does split them; that is \claimref{synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix}.

## lay
In this framework one coupling gives up-type quarks (up, charm, top) and down-type quarks (down, strange, bottom) the same masses, against the large measured top-bottom ratio, so something must be added. This result sorts every addition of the usual kinds, with the masses read sector by sector as the series does (a reading that is not left-right symmetric). Read that way, adding more couplings to the same underlying field never helps. Adding a second field helps only if both the fields and the couplings carry complex phases, the kind of phases that also produce matter-antimatter asymmetry in quark decays; otherwise the only source is a piece that distinguishes right-handed up from right-handed down, which the square of the heavy-neutrino object supplies. A popular combination, one coupling of each of two standard types, provably cannot make the up-type quarks heavier on average. A left-right symmetric coupling to the field's mirror image, with its own strength, does split them.

## one-liner
Under the per-sector $c^{*}$ reading (not $\su(2)_{R}$ covariant), every composite of a rung-$4$ vector with a diagonal weighting $h(T_{3R}, B - L)$ enters with weights $e \pm o$ (symmetric and $120$-type entries alike), so $T_{3R}$-even composites of one rung vector give $bM_{u} = \bar{b}M_{d}$ whatever their family matrices, relatively real family matrices give $H_{u} = \overline{H_{d}}$, $\tr H_{u} - \tr H_{d}$ is a $T_{3R}$-odd channel plus a CP channel $\propto \operatorname{Im}t_{kl}\operatorname{Im}(b_{k}\bar{b}_{l})$ (two CP-odd phases, a CP-even product), and a $10$ with one $120$ keeps $\tr H_{u} = \tr H_{d}$.
