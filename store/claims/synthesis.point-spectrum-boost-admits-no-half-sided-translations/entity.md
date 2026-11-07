---
id: synthesis.point-spectrum-boost-admits-no-half-sided-translations
kind: claim
version: 4
title: 'A point-spectrum boost admits no half-sided translations'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, car-algebra, boundary-modes, undetermined-input]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: unit pass, every imaginary unit resolved to the geometric-algebra unit it stands for
  version: 4
  source: maintainer pass 2026-11-07 (resolve units)
review: draft
about:
- obj.hawking.boundary-mode-algebra-windows-boost-dynamics
derivations:
- name: main
  uses:
  - hawking.imported-algebra-boundary-modes-car-algebra@5
  - hawking.modular-structure-completed-pair@3
  - angle.imported-theorems-deliver-their-hypotheses@3
  - singularity.modular-theory-matrix-factor-proved-outright@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_no_dilated_generator_on_windows
- kind: check
  ref: check.py::check_point_spectrum_and_recurrence
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - singularity.why-calibration-cannot-be-internal
  - singularity.rate-rigidity-temperature-not-algebra-intrinsic
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. The boundary-mode algebra and its GNS spaces have their numbers read in span{1, J}, J = e_2 e_3 the complex unit of the radial atom (U2; synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom, cited in the formal level), the source unit i read as J: the boost dynamics e^{-J omega_j t}, Ad(e^{JtK}) on the windows, [K, P] = JcP with P = X + JY in the proof, the modular unitaries Delta^{Js}, rho^{Js} and the periodicity phases e^{-2 pi J k}, e^{-J pi(2k+1)} are written with J, and the Borchers relation of the imported Fact angle.imported-theorems-deliver-their-hypotheses is read in the GNS space with that unit. The Definitions mode-set letter J is named once as such. No i remains; declaration removed. Mathematics, links and checks unchanged.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced, by Leon''s ruling R1 (7 November 2026): the boundary-mode algebra''s phase flow e^{-i omega_j t}, Ad(e^{itK}) on the windows, [K, P] = icP, the GNS unitaries and the modular group Delta^{is} keep i, since the boundary modes descend from T05''s atom, whose mode operators anticommute with I_4 (conventions, known limits 1 and 2). Declared (version and levels unchanged).'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Version 1 -> 2, note only, statement and proof unchanged. The parenthesis naming the bilateral weights kappa k as those of Premise (Q) refers to (Q) version 2. Premise (Q) version 3 (Leon''s decision of 23 October) takes kappa(k + 1/2), the second case of (iv), where the flow at time 2 pi/kappa is the parity automorphism. The theorem covers both offsets and its content is unchanged. Check maintenance: comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 2 -> 3.'
  open_problem: op.r-premises-external
  note: >-
    Answers part of the second success branch (what form any principle supplying (R) must
    take) for the Borchers and Bisognano-Wichmann route that note.singularity.cost-r-dictionary
    and note.angle.where-2-lives propose. The finite-window obstruction (no real-exponential
    eigenvector of a unitary flow) is extended to the whole countable mode space and to the GNS
    space of any boost-invariant state: a boost with point spectrum on a dense set dilates no
    strongly continuous translation group, so the half-sided translations whose dilation fixes
    2 pi are trivial there. The route therefore needs a one-particle space on which the boost
    has no eigenvectors, the continuum mode space, and cannot be run on windows, on the
    countable mode space, or on the array of Premise (Q), whose flow is even periodic.
    Filed alongside, synthesis.affine-cell-boost-spreads-without-scrambling exhibits the
    complementary case: the dilation on L^2(R_+), with continuous spectrum and a countable cell
    basis in which the boost is not diagonal.
    Transport-absent functional analysis; the series enters through its mode spaces.
---

## formal
Let $\mathfrak{A}$ be the boundary-mode algebra of Definition \claimref{obj.hawking.boundary-mode-algebra-windows-boost-dynamics} over a countable mode set (the set called $J$ in the Definition; below, $J$ is the unit) (Fact \claimref{hawking.imported-algebra-boundary-modes-car-algebra}), its numbers read in $\mathrm{span}\{1, J\}$ with $J = e_{2}e_{3}$ the complex unit of the boundary modes' radial atom (Theorem \claimref{synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom}), which commutes with the radial plane and with every vector orthogonal to spacetime, hence with every mode; it is also the unit of every GNS space below, and the imported theorem of (iii) is read with it, with window algebras $\mathfrak{A}_{F}$ and a quasi-free boost dynamics $\tau_{t}(a_{j}) = e^{-J\omega_{j}t}a_{j}$ with arbitrary real weights $\omega_{j}$ (positive, as in the Definition, or the bilateral weights $\omega_{k} = \kappa k$ of Premise \claimref{singularity.q-joint-quasi-freeness-s-wave}). The operative hypothesis is that the boost multiplies each generating mode by a phase, so that it has pure point spectrum on the windows; countability of the mode set alone would not suffice, since a one-particle space on which the boost has continuous spectrum also has countable bases, in which the boost is not diagonal. Then:
\begin{enumerate}
\item[(i)] every window is $\tau$-invariant and every element of $\bigcup_{F}\mathfrak{A}_{F}$ has a relatively compact $\tau$-orbit; on a window no nonzero $P$ satisfies $[K, P] = JcP$ with $c$ real and nonzero, $K = \sum_{j \in F}\omega_{j}N_{j}$;
\item[(ii)] if $(\gamma_{a})_{a \in \R}$ is a one-parameter group of $*$-automorphisms of $\mathfrak{A}$, strongly continuous ($a \mapsto \gamma_{a}(x)$ norm continuous for each $x$), with $\tau_{t}\circ\gamma_{a}\circ\tau_{-t} = \gamma_{e^{ct}a}$ for all $t, a$ and some real $c \neq 0$, then $\gamma_{a} = \id$ for every $a$;
\item[(iii)] let $\omega$ be a $\tau$-invariant state with GNS triple $(\mathcal{H}, \pi, \Omega)$ and $V_{t}$ the unitary group with $V_{t}\pi(x)\Omega = \pi(\tau_{t}(x))\Omega$. If $(U(a))_{a \in \R}$ is a strongly continuous unitary group on $\mathcal{H}$ with $V_{t}U(a)V_{-t} = U(e^{ct}a)$ for all $t, a$ and some real $c \neq 0$, then $U(a) = 1$ for every $a$. In particular, if the modular unitaries of $(\pi(\mathfrak{A})'', \Omega)$ act through the boost, $\Delta^{Js} = V_{-\beta s}$ for some $\beta \neq 0$, as they do when $\omega$ is a faithful $(\tau, \beta)$-KMS state, then every unitary group satisfying the hypotheses of the abstract theorem of Fact \claimref{angle.imported-theorems-deliver-their-hypotheses} (positive generator, $U(a)\Omega = \Omega$, half-sided inclusion) is trivial, since by that theorem it satisfies $\Delta^{Js}U(a)\Delta^{-Js} = U(e^{-2\pi s}a)$, which is the hypothesis of (iii) with $c = 2\pi/\beta$;
\item[(iv)] for the weights $\kappa k$ the flow is periodic, $\tau_{2\pi/\kappa} = \id$, so (i) to (iii) hold with every orbit periodic; for weights in $\kappa(\Z + \tfrac12)$, $\tau_{2\pi/\kappa}$ is the parity automorphism.
\end{enumerate}
Consequently the mechanism by which the Bisognano-Wichmann and Borchers theorems produce the factor $2\pi$ cannot be realised on the windows, on the countable mode space, or on the array of (Q): a principle deriving (R) along that route must be posed on a one-particle space on which the boost has no eigenvectors spanning the relevant vectors, such as the continuum mode space of Definition \claimref{obj.hawking.continuum-mode-space} with a Hamiltonian of continuous spectrum. This result does not show that the route succeeds there.

## technical
The series' best candidate for supplying the Hawking temperature from a principle stated in its own algebra is the Bisognano-Wichmann and Borchers mechanism: if the boost acts on a group of positive-energy translations by dilating them, the modular flow of the vacuum is that boost at exactly the rate $2\pi$, so the temperature would follow from positivity of energy instead of from the thermal premise (R). The store had already noted that a finite window cannot carry such translations. This result extends that to every setting the series uses for the boundary modes before the continuum: the whole countable mode space (with any real weights, including those of (Q)) and the Hilbert space of any boost-invariant state on it. The reason is that the boost there acts by phases on the modes, so it has pure point spectrum: every vector in a dense set moves on a compact orbit, and a translation group that the boost dilates is then forced to act trivially, by squeezing the translation parameter to zero along the orbit. So the half-sided translations that would fix $2\pi$ are trivial on these spaces, and a derivation of (R) along this route must use the continuum mode space, where the boost has continuous spectrum. Under (Q)'s weights the flow is even periodic, returning to the identity after exactly one modular period.

## lay
One hope for explaining the black-hole temperature without simply assuming it uses a celebrated theorem: if the time-stretching symmetry at a horizon acts on a family of positive-energy shifts by rescaling them, the temperature comes out automatically with the right value. This result shows that the discrete models the series uses for the horizon's quantum modes cannot host that mechanism: their time evolution only ever returns close to where it started, and a rescaling that never escapes a bounded region can only rescale shifts that do nothing. The mechanism needs a genuinely continuous spectrum of mode energies, so any derivation of the temperature along these lines has to be built on the series' continuum description of the modes.

## one-liner
A boost that acts by phases on a generating set of modes (pure point spectrum: windows, the countable mode space, the array of (Q)) dilates no strongly continuous translation group, even on the GNS space of a KMS state, so the Borchers and Bisognano-Wichmann route to (R) must be posed on the continuum mode space.
