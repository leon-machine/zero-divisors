---
id: synthesis.c-loc-modular-clause-moves-no-nested-patch
kind: claim
version: 2
title: 'The modular clause of (C$_{\mathrm{loc}}$) moves no nested patch'
status: proved
region: synthesis
subject: einstein
tags: [modular-theory, boundary-modes, horizons, no-go, thermal-premises]
proposed_by:
  kind: ai
  session: 2026-10-22-cloc
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
review: draft
about:
- obj.hawking.boundary-mode-algebra-windows-boost-dynamics
derivations:
- name: main
  uses:
  - synthesis.point-spectrum-boost-admits-no-half-sided-translations@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_window_flow_acts_by_phases
- kind: check
  ref: check.py::check_recurrence_without_period
- kind: check
  ref: check.py::check_shift_contrast
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.c-loc-local-horizon-premise
  - synthesis.point-spectrum-boost-admits-no-half-sided-translations
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The phases of the boundary-mode boost dynamics and of its GNS unitaries, the modular group Delta^{I_4 s}, and the check''s Gaussian-rational step z = (3 + 4I_4)/5 with unique factorisation in Z[I_4] now use the field theory''s unit I_4 (the boundary-mode CAR algebra''s complex unit, numbers read in span{1, I_4}); no bare i remains.'
  open_problem: op.derive-c-loc
  note: >-
    Consistency test of clause (iii) of the local-horizon premise against its clause (i). Clause (i) places
    on each local horizon the boundary-mode algebra of the cited Definition, whose boost acts by phases
    (pure point spectrum). Clause (iii) can be read two ways: as the boost dynamics acting on the patch's
    mode algebra as a whole (as at a Killing horizon, where the modes sit on the fixed locus of the flow),
    or as a geometric flow that moves the algebras of sub-patches, as the Bisognano-Wichmann and
    Hislop-Longo flows move the null-plane and sub-diamond algebras of a quantum field. The second reading
    is inconsistent with clause (i) as worded whenever the sub-patch algebras are properly nested, at the
    C*-level and in the GNS representation of any boost-invariant state; the first is consistent, and for a
    faithful state it is the KMS clause again (the window version is proved in Theorem \claimref{synthesis.local-boost-temperature-is-local-regularity}, part (ii)). The proof is direct (almost periodicity), and does not need Wiesbrock's theorem
    on half-sided modular inclusions (Wiesbrock 1993, with the correction of Araki and Zsido 2005, cited
    from memory), which would route the same conclusion through the stored no-go on half-sided
    translations. Transport-absent: operator algebra applied to the premise's wording.
---

## formal
Let $\mathfrak{A}$ be the boundary-mode algebra of Definition \claimref{obj.hawking.boundary-mode-algebra-windows-boost-dynamics}, the CAR algebra over a countable mode set with window algebras $\mathfrak{A}_{F}$, and let $(\tau_{t})_{t \in \R}$ be any one-parameter group of $*$-automorphisms that multiplies each generating mode by a phase, $\tau_{t}(a_{j}) = e^{-I_4\omega_{j}t}a_{j}$ with real $\omega_{j}$, as the Definition's boost dynamics does (the mode algebra's complex unit is the field theory's unit $I_4$, and numbers are read in $\mathrm{span}\{1, I_4\}$).
\begin{enumerate}
\item[(i)] \emph{(Recurrence.)} Every $x \in \mathfrak{A}$ has a relatively compact $\tau$-orbit, and for every $\varepsilon > 0$ and $S > 0$ there are $T \ge S$ and $T' \le -S$ with $\|\tau_{T}(x) - x\| < \varepsilon$ and $\|\tau_{T'}(x) - x\| < \varepsilon$.
\item[(ii)] \emph{(No proper semigroup invariance.)} If $\mathcal{B} \subseteq \mathfrak{A}$ is a norm-closed subspace with $\tau_{t}(\mathcal{B}) \subseteq \mathcal{B}$ for all $t \ge 0$, or for all $t \le 0$, then $\tau_{t}(\mathcal{B}) = \mathcal{B}$ for every $t \in \R$. The same holds in the GNS representation $(\mathcal{H}, \pi, \Omega)$ of any $\tau$-invariant state, with $V_{t}$ the unitaries implementing $\tau$: $V_{t}$ has pure point spectrum, and every $\sigma$-weakly closed subspace $\mathcal{B}$ of $\pi(\mathfrak{A})''$ with $V_{t}\mathcal{B}V_{t}^{*} \subseteq \mathcal{B}$ for all $t$ of one sign satisfies $V_{t}\mathcal{B}V_{t}^{*} = \mathcal{B}$ for all $t$.
\item[(iii)] \emph{(Consequence for the local-horizon premise.)} Let $\mathcal{H}$ be a local Rindler horizon carrying $\mathfrak{A}$ as clause (i) of Premise \claimref{synthesis.c-loc-local-horizon-premise} asserts, with affine parameter $\lambda$ on its generators and bifurcation cut at $\lambda = 0$, and let $\mathcal{N}_{c} = \{\lambda > c\}$, $c > 0$. Assume (P): the local boost acts on the patch's modes as the Definition's boost dynamics, so that the modular flow, which clause (iii) identifies with the local boost, is $\tau$ up to a nonzero rescaling of its parameter (clause (i) cites the algebra; that its phase dynamics is the local boost is this hypothesis). Consider the geometric reading (G) of clause (iii): the modes on $\mathcal{N}_{c}$ generate C$^{*}$-subalgebras $\mathfrak{A}_{c} \subseteq \mathfrak{A}$ (or von Neumann subalgebras of $\pi(\mathfrak{A})''$ in the GNS representation of the selected state) with $\mathfrak{A}_{c} \subseteq \mathfrak{A}_{c'}$ for $c \ge c'$, and the modular flow carries $\mathfrak{A}_{c}$ onto $\mathfrak{A}_{e^{\mp 2\pi s}c}$ at modular parameter $s$, the way the boost moves $\mathcal{N}_{c}$. Then, under (P), $\mathfrak{A}_{c} = \mathfrak{A}_{c'}$ for all $c, c' > 0$. So (G) with properly nested sub-patch algebras contradicts clause (i) as worded, given (P); the same holds for nested diamonds sharing a tip, moved monotonically by the conformal Killing flow of the larger one.
\end{enumerate}
Hence, given (P), clause (iii) is consistent with clause (i) only as a statement about the boost dynamics acting on the patch's mode algebra as a whole, which is how the flow acts at a Killing horizon, where the modes sit on the fixed locus of the boost; for a faithful state this is the KMS condition of clause (ii) restated (on windows, part (ii) of Theorem \claimref{synthesis.local-boost-temperature-is-local-regularity}). The geometric reading, the one the Bisognano-Wichmann and Hislop-Longo flows realise for a quantum field and the one the small-diamond route uses, needs a mode space on which the boost has continuous spectrum, such as Definition \claimref{obj.hawking.continuum-mode-space}, which clause (i) does not cite.

## technical
Clause (i) of the local-horizon premise puts on every local horizon the series' boundary-mode algebra, on which the boost multiplies each mode by a phase. Such a flow is almost periodic: every orbit is relatively compact, so every element returns arbitrarily close to itself at arbitrarily late and early times. It follows that a closed subspace mapped into itself by the flow for all positive times (or all negative times) is mapped onto itself for all times: the flow cannot push a subalgebra properly inside itself. The same holds for weakly closed subalgebras in the GNS representation of any boost-invariant state, since the implementing unitaries have pure point spectrum and generate a compact group, in which a closed semigroup is a group. A boost acting geometrically does exactly that to the algebras of the future parts of the generators, $\lambda > c$, which it carries to $\lambda > e^{\mp 2\pi s}c$; this is the half-sided structure behind the Bisognano-Wichmann and Hislop-Longo theorems, and the stored no-go on half-sided translations is its translation-side counterpart. So, if the local boost acts on the patch's modes as the cited boost dynamics, clause (iii) cannot mean that the modular flow moves nested sub-patch algebras, unless those algebras all coincide. Read as the boost dynamics acting on the patch's algebra as a whole, as at a Killing horizon where the modes sit on the fixed locus, clause (iii) is consistent, and for a faithful state it says no more than the KMS condition of clause (ii). The exact checks illustrate the theorem and do not test (ii) or (iii), which are proved in the proof text: they verify the canonical anticommutation relations and the phase action on a two-mode window with the non-periodic phase $(3 + 4I_4)/5$, that this phase is no root of unity up to order $200$ while returning within $10^{-3}$ of $1$ (squared distance) at order $61$, and, in contrast, that the bilateral shift never returns and maps its half-space properly into itself.

## lay
The new assumption needed for Einstein's equations has three parts: small horizons carry the series' quantum modes, those modes are at the right temperature, and their natural time flow is the geometric flow of the horizon. This result shows that the third part can only be meant in a weak sense. The series' modes evolve by simple rotations of phases, and such an evolution always comes back close to where it started. A genuinely geometric flow would instead push the modes of a smaller piece of horizon ever deeper into a larger piece, never returning. The two cannot both hold. So the third part must be read as a statement about the modes of the whole patch, where it adds nothing beyond the temperature part; the stronger geometric reading would need a continuous family of modes, which the assumption does not name.

## one-liner
A phase-acting boost is almost periodic, so it maps no closed subspace properly into itself; hence, if the local boost acts on the patch's modes as the cited boost dynamics, clause (iii) of (C$_{\mathrm{loc}}$) cannot move properly nested C$^{*}$- or von Neumann sub-patch algebras of the mode algebra its clause (i) cites, and is consistent only as the boost dynamics on the whole patch, where for a faithful state it restates clause (ii).
