---
id: synthesis.collar-kms-extension-completion-locus
kind: claim
version: 4
title: 'Under (E), the horizon''s KMS state reads $6\pi$ at the exceptional set'
status: proved
region: synthesis
subject: thermality
tags: [modular-theory, schwarzschild, kasner, boundary-modes]
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
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: 'unit resolution pass, the holonomy phase flows written with the transverse unit J'
  version: 3
  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Opus 5.5
  role: GA rewrite (Killing bivector from the synchronous gauge field)
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - singularity.imported-interior-collar-kasner-form@6
  - singularity.imported-one-sided-completion-singularity@5
  - singularity.modular-flow-boundary-modes-holonomy-universal@2
  - singularity.modular-structure-completed-pair@5
  - singularity.kms-uniqueness-factor@6
  - singularity.rate-rigidity-temperature-not-algebra-intrinsic@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_killing_bivector_parallel_carry
- kind: check
  ref: check.py::check_one_atom_kms_every_slice
- kind: proof
  derivation: main
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Forms and Christoffel symbols to GA in the proof of (i): the (tau, t) block is the synchronous field hb^{-1}(e_tau) = e_0, hb^{-1}(e_t) = a e_1 with Omega(e_tau) = 0, Omega(hb(e_1)) = -(a''/a) B_1, so e_0, e_1 and B_1 are D-parallel along the tau-lines, and the Killing vector K = a e_1 has A . DK = A . F_K with F_K = (D ^ K)/2 = a'' B_1 (dictionary clause (vi)); the Christoffel symbol and the two-form d(xi_flat) stay as a labelled component reading. A notation change: the two frame derivatives are one-line GA computations ((e_0 . D)K = a'' e_1, (e_1 . D)K = -a'' (e_0 ^ e_1) . e_1 = a'' e_0), equal to the stored component values. Statement unchanged.'
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U2: the holonomy phase flows on the CAR algebra of the completed-pair atoms at P are written Ad(e^{J s f(r) K_P}) with J = e_2 e_3, the atoms'' complex unit (synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom, cited as a mention); hypothesis (E) is otherwise unchanged. Declaration removed: no bare i remains.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (complex-analysis): the holonomy phase flows Ad(e^{is f(r) K_P}), K_p = sigma_p/2, act on the CAR algebra of the atoms, whose modes anticommute with I_4 (conventions, known limit 1), so I_4 is not their unit.'
  open_problem: op.collar-kms-extension
  flow_note: phase; every flow here is the phase flow Ad(e^{isfK}) of the stated rate f (see synthesis.phase-flow-is-time-rotor-flow-kms-continuation).
  note: >-
    Decides op.collar-kms-extension under hypothesis (E), the reading in which the collar has no
    boundary modes of its own: the completion's ladder pair exists exactly over E (Fact
    singularity.imported-one-sided-completion-singularity), and (E) reads every collar slice on the
    E-atoms by carrying them along the tau-lines, along which the synchronous frame is parallel. Under
    (E) the extension exists, is unique, and its Hubble-normalised inverse temperature at the
    exceptional set is 6 pi, so the conditional of
    singularity.modular-flow-boundary-modes-holonomy-universal (ii) holds. The stored
    synthesis.collar-kms-extension-three-flows decides the opposite under its slice-product hypothesis
    (C), which gives each slice an independent atom; (C) and (E) are different hypotheses about the
    collar algebra and the store derives neither. Argued, not proved here: (C) needs atoms at collar
    points, which the completion does not supply, so (E) is the reading the completion favours; any
    Killing-equivariant carry inside the (t, r) surfaces (which are totally geodesic, with tangent
    bivector B1) gives the same generators. The problem should become decided under (E), with the
    choice between (C) and (E) recorded as its residue. The KMS machinery is standard
    (transport-absent); the identification of the slice generators is transport-essential, resting on
    the parallelism of B1 along the tau-lines. The sphere holonomies B2, B3 are not treated. Filed alongside,
    synthesis.collar-isotropy-selects-t-boost, which works pointwise on the frame atom Cl(1,3) at a point and
    agrees on selecting B1; it says nothing about the r-direction, which is what (C) and (E) decide.
---

## formal
Work in units $2M = 1$ on the collar of Fact \claimref{singularity.imported-interior-collar-kasner-form}, with $\kappa = \tfrac12$, $A = 1/r - 1$, and the rates of Proposition \claimref{singularity.modular-flow-boundary-modes-holonomy-universal}: $\rho(r) = 1/(2r^{2})$ per unit Killing time and, for $r < 1$, $\rho_{\mathrm{H}}(r) = \tfrac13 S(r)(1-r)^{-1/2} = \tfrac13 + \tfrac{4}{15}r + \cdots$ per unit Hubble-normalised parameter. By Fact \claimref{singularity.imported-one-sided-completion-singularity} the ladder pair of the completion exists exactly over the exceptional set $E = \{\tau = 0\}\times\R_{t}\times S^{2}$, and each line of constant $(t, \theta, \varphi)$ in the collar is a $\tau$-line ending at the point $(t, \theta, \varphi)$ of $E$. Assume:
\begin{enumerate}
\item[(E)] the boundary-mode atom read at a collar point is the atom (the completed pair of Theorem \claimref{singularity.modular-structure-completed-pair}) of the point of $E$ on its $\tau$-line, carried along that line by the parallel transport of the synchronous frame; on a finite set $P \subset E$ the algebra is the CAR algebra of the atoms at $P$, a matrix factor; and the $t$-line holonomy flow of the slice $r$ acts on it as the phase flow $\operatorname{Ad}(e^{Jsf(r)K_{P}})$ with $K_{P} = \sum_{p \in P}K_{p}$, $K_{p} = \sigma_{p}/2$, written with the boundary modes' complex unit $J = e_{2}e_{3}$, which commutes with the atoms (\claimref{synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom}), where $f = \rho$ (the Killing parametrisation) or $f = \rho_{\mathrm{H}}$ (the Hubble parametrisation, $r < 1$).
\end{enumerate}
Then:
\begin{enumerate}
\item[(i)] the Killing bivector of $\partial_{t}$ at a collar point of the slice $r$ is $\rho(r)B_{1}$ with $B_{1} = e_{0}\wedge e_{1}$, and $B_{1}$ is parallel along $\partial_{\tau}$; so every slice carries to $E$ a positive multiple of the one generator $K_{P}$, with a factor that depends on $r$ only;
\item[(ii)] the product state $\omega_{P}$ with density $\bigotimes_{p}e^{-2\pi K_{p}}/\Tr(\cdot)$, the completed pair's state of rapidity period $2\pi$ at every point of $P$, is for every slice $r$ the unique KMS state of that slice's Killing flow at $\beta = 2\pi/\rho(r) = 4\pi r^{2}$ and of its Hubble flow at $\beta_{\mathrm{H}}(r) = 2\pi/\rho_{\mathrm{H}}(r) = 6\pi\sqrt{1-r}/S(r) = 6\pi(1 - \tfrac45 r + O(r^{2}))$; a state KMS for one slice's flow at some $\beta \neq 0$ is KMS for every other slice's flow at the rescaled inverse temperature; in Killing time the same state has $\beta = 4\pi r^{2} \to 0$ at the exceptional set (infinite Killing-time temperature there), so $6\pi$ is the value in Hubble-normalised time;
\item[(iii)] at the exceptional set the Hubble-normalised holonomy flow has rate $|p_{1}| = \tfrac13$, and $\omega_{P}$ is its unique KMS state at $\beta_{\mathrm{H}} = 6\pi$; in particular the horizon's KMS state extends, uniquely, to a KMS state of the $t$-line holonomy flow at the exceptional set, and the conditional sentence of Proposition \claimref{singularity.modular-flow-boundary-modes-holonomy-universal}(ii) holds under (E);
\item[(iv)] the running $\rho_{\mathrm{H}}(r) = \tfrac13 + \tfrac{4}{15}r + \cdots$ of the rate is under (E) a slice-dependent reparametrisation of one flow and obstructs nothing; by contrast, if two slices $r_{1} \neq r_{2}$ carried independent atoms (the slice-product reading), the product of period-$2\pi$ states would be KMS for no Killing-parametrised flow $\rho(r_{1})K_{1} + \rho(r_{2})K_{2}$ at any $\beta \neq 0$, since $\rho(r_{1}) \neq \rho(r_{2})$.
\end{enumerate}
Clause (i) is the evidence for the flow form assumed in (E); given that form, (ii) and (iii) are reparametrisation. So whether the extension exists is decided by the collar algebra: on the exceptional set's own modes, carried along the $\tau$-lines, it exists and gives $6\pi$; on independent slice atoms it does not.

## technical
The completion attaches its ladder pair only over the exceptional set $E$; the collar has no boundary modes of its own. Read each collar slice on the modes of $E$ by carrying them along the lines of constant $(t, \theta, \varphi)$, the $\tau$-lines, along which the synchronous frame is exactly parallel. The Killing bivector of $\partial_{t}$ at radius $r$ is $\rho(r)B_{1}$, $\rho = 1/(2r^{2})$ in units $2M = 1$, and $B_{1}$ is parallel along $\tau$, so every slice's $t$-line holonomy flow acts on the same atoms through one generator $K = \sigma/2$, at a rate that depends only on $r$: $\rho(r)$ in Killing time, $\rho_{\mathrm{H}}(r) = \tfrac13 + \tfrac{4}{15}r + \cdots$ in Hubble-normalised time.

A KMS state of a flow is a KMS state of every constant reparametrisation of it, at the rescaled inverse temperature. So the horizon's state, rapidity period $2\pi$, is the unique KMS state of every slice's Killing flow at $4\pi r^{2}$ and of every slice's Hubble flow at $2\pi/\rho_{\mathrm{H}}(r) = 6\pi(1 - \tfrac45 r + \cdots)$, and at the exceptional set, where the Hubble rate is $\tfrac13$, it is KMS at exactly $6\pi$. In Killing time the same state reads $4\pi r^{2}$, which tends to zero there: $6\pi$ is a Hubble-time value. The stored conditional holds on this reading. The geometric computation (the Killing bivector and its parallelism) is what supports the flow form that (E) assumes; once (E) is granted the KMS statements are reparametrisation.

The earlier result that the extension fails assumed instead that each slice carries its own independent atom; then the varying rate makes the slice flows non-proportional and no state is KMS for two of them. The two readings are different hypotheses about the collar algebra; the completion, which supplies modes only on $E$, supports the first.

## lay
A black hole's horizon has a temperature, and earlier work found that a natural clock at the central singularity would read a universal temperature, $6\pi$ in suitable units, if the horizon's thermal state could be continued inward. Whether it can depends on what the quantum modes inside are. Suppose, as the construction suggests but does not prove, that the modes live only at the singularity and that every point inside is read by following a straight-in path to the singularity, along which the relevant direction is carried without turning. Then every layer of the interior sees the same modes, ticking at a different rate, and the horizon's thermal state is thermal for all of them, reading $6\pi$ at the singularity in the clock natural there. An earlier result reached the opposite answer by assuming instead that each layer has its own independent modes; which assumption is right is not decided.

## one-liner
Under hypothesis (E), that the collar's boundary modes are those of the exceptional set carried along the parallel $\tau$-lines, every slice's $t$-line holonomy flow is a reparametrisation of one flow, so the horizon's KMS state is KMS for all of them and reads $\beta_{\mathrm{H}} = 6\pi$ in Hubble time at the exceptional set (Killing-time $\beta = 4\pi r^{2} \to 0$), opposite to the verdict under independent slice atoms.
