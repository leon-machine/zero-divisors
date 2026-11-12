---
id: synthesis.tower-charge-sector-label-temperature-not
kind: claim
version: 5
title: 'The tower charge is a sector label; the temperature is not'
status: proved
region: synthesis
subject: dark-matter
tags: [mirror-sector, indifference, superselection, car-algebra, modular-theory, premises-p1-p5, needs-continuum]
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
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle
  version: 4
  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Opus 5.5
  role: 'pin review, the Reading and the proof''s reading now say that the scoping was first offered in the route-one proposition at its version 2 and is P2 at its version 2'
  version: 5
  source: maintainer pass 2026-11-07 (pin review)
review: draft
about:
- obj.hawking.boundary-mode-algebra-windows-boost-dynamics
derivations:
- name: main
  uses:
  - hawking.imported-quasi-free-states-car-algebra@2
  - hawking.i-state@4
  - dark-matter.superselected-hence-dark-exactly-stable@5
  - dark-matter.stored-asymmetry-charge-not-number@11
  - synthesis.cold-mirror-needs-non-equilibrium-descent@3
  - synthesis.mirror-asymmetry-route-one@4
  - dark-matter.mirror-tower-copy-one@11
  - synthesis.imported-powers-stormer-takesaki-disjointness@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_car_window
- kind: check
  ref: check.py::check_charge_is_sector_label
- kind: check
  ref: check.py::check_temperature_not_sector_label
- kind: check
  ref: check.py::check_mode_affinity
- kind: proof
  derivation: main
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-matter.stored-asymmetry-charge-not-number repinned 8 -> 9 after reviewing its G1 restatement (the cold mirror is an exception to P2 at its version-1 reach, P2 as scoped leaves xi free, and the cold mirror then needs a non-equilibrium descent; the charge reading and the numbers are unchanged); the use here holds as cited. Pin review: synthesis.mirror-asymmetry-route-one repinned 2 -> 3 after reviewing its G2 restatement (the scoping of P2 it offered without proof is now P2 at version 2, so clause (v) of the copy theorem has both routes); the Reading (formal) and the proof''s reading quoted the scoping as offered and not proved and now say that it was first offered there at its version 2 and is P2 at version 2; the result, which analyses that scoping, is unchanged. Pin review: dark-matter.mirror-tower-copy-one repinned 8 -> 9 after reviewing its C1 restatement (clause (iv): the common ceiling and coupling are now Premise synthesis.common-ceiling-coupling-premise, P2 equating labels and not couplings; the share of one rests also on that premise; the caveat is reworded for P2''s version-1 reach), clauses (i) to (iii) and (v) unchanged in content; the use here holds as cited. Version 4 -> 5. Pin review (second round): synthesis.mirror-asymmetry-route-one repinned 3 -> 4 after reviewing its restatement ((iii) scoped to what the tower-charge theorem proves (finite windows, or a convergent Powers-Stormer sum)); the Reading here quotes only its version-2 offering of the scoping, which stands, and the use here holds as cited.'
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. The charge rotations e^{i theta} act on the boundary-mode CAR algebra, so by U2 their unit is the transverse bivector J = e_2 e_3 of synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom (cited as a mention), written out as e_2 e_3 because J names the mode set in this entity: a_j -> e^{theta e_2 e_3} a_j, conjugation by e^{theta e_2 e_3 Q_F}, scalars span{1, e_2 e_3}. Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (complex-analysis): the charge rotations e^{i theta} act on the boundary-mode CAR algebra over l^2(J), defined over C, with windows End(Lambda C^F); the boundary modes are the atom''s ladder pairs, with whose mode operators I_4 anticommutes (conventions, known limit 1), so it is not their unit.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Maintainer pass: the Powers-Stormer criterion, cited from memory, and Takesaki''s disjointness theorem, cited in words, are now the imported Fact synthesis.imported-powers-stormer-takesaki-disjointness, added to uses and cited in the proof and check. Version 1 -> 2.'
  open_problem: op.no-dark-radiation-under-p2
  note: >-
    Tests the scoping of P2 offered and not proved in synthesis.mirror-asymmetry-route-one ("P2
    equates the superselected charges of the descent, which the temperature ratio is not"). The
    charge and the temperature are of different kinds on every finite window, so the scoping is
    well defined there and leaves xi free; on the infinite boundary-mode algebra the temperature
    is itself a superselection label whenever infinitely many modes share a frequency band, and
    then the same scoping reaches xi. Which case holds turns on whether the boundary-mode set is
    finite (the count of about pi N^2 / ln 2) or the countable J of the Definition: a decision for
    the series. Clause (iii) uses the Powers-Stormer criterion and agrees with Takesaki's theorem that KMS states at different temperatures are
    disjoint when the induced von Neumann algebra is of type III (M. Takesaki, Disjointness of the
    KMS-states of different temperatures, Comm. Math. Phys. 17 (1970) 33-41); both are the imported Fact
    synthesis.imported-powers-stormer-takesaki-disjointness. Thematically related to the reading of the phase-space count filed
    alongside, synthesis.promoted-norm-one-global-pair (when a thermal parameter is a sector label). The mathematics is standard operator algebra and transport-absent.
---

## formal
\emph{Hypothesis (B').} The reversal pair carries the joint boundary-mode algebra, the CAR algebra over $\ell^{2}(J) \oplus \ell^{2}(J')$ (Definition \claimref{obj.hawking.boundary-mode-algebra-windows-boost-dynamics} for each tower), and the superselection of the tower charge (Proposition \claimref{dark-matter.superselected-hence-dark-exactly-stable}) is represented by taking as observables the elements invariant under each tower's charge rotation $a_{j} \mapsto e^{\theta e_{2}e_{3}}a_{j}$ ($j \in J$), $a'_{j} \mapsto e^{\theta' e_{2}e_{3}}a'_{j}$ ($j \in J'$), with $\theta, \theta'$ independent. Here the complex unit of the boundary modes is the transverse bivector $e_{2}e_{3}$, which commutes with the radial-plane modes and squares to $-1$, and their scalars are $\mathrm{span}\{1, e_{2}e_{3}\}$ (\claimref{synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom}, where it is called $J$; it is written out here because $J$ names the mode set).
\begin{enumerate}
\item[(i)] \emph{(The charge is a sector label on windows.)} On every window $\mathfrak{A}_{F} \otimes \mathfrak{A}'_{F'}$ the observable algebra is the direct sum, over the joint charge values $(q, q')$, of the full matrix algebras of the joint charge eigenspaces; its centre is spanned by the joint charge projections, and window states of different charge are disjoint.
\item[(ii)] \emph{(The temperature is not, on windows.)} Every product of Gibbs states of the two towers' boost clocks at inverse temperatures $\beta, \beta'$, equal or not, has invertible density and gives positive weight to every joint charge sector; so any two of them have the same central support, $1$, and no central projection of the observable window algebra separates two values of $\xi = \beta/\beta'$.
\item[(iii)] \emph{(The temperature on the full algebra.)} For the I-states $\omega_{\beta}$, $\omega_{\beta'}$ of one tower (Theorem \claimref{hawking.i-state}) with $\beta \neq \beta'$, let $a_{j} = \sqrt{n_{j}n'_{j}} + \sqrt{(1 - n_{j})(1 - n'_{j})}$ be the Hellinger affinity of mode $j$; $a_{j} < 1$ for every mode of nonzero frequency, and $1 - a_{j} \le |n_{j} - n'_{j}|$. By the Powers-Stormer criterion the two states are quasi-equivalent if $\sum_{j}(1 - a_{j}) < \infty$ and disjoint otherwise. Hence if infinitely many frequencies $\omega_{j}$ lie in a compact subset of $(0, \infty)$ the two I-states are disjoint, and the temperature is a label of the full algebra in the disjointness sense, which on the full algebra is also the sense in which charge sectors are labels; if $\sum_{j}(n_{j} + n'_{j}) < \infty$ they are quasi-equivalent. The stored charge is a finite label (an eigenvalue of an element of the observable algebra) only on windows: a thermal state over infinitely many modes has no finite total charge, and there the charge too can be a label only in the disjointness sense, as a charge density. So the comparison of (i) with (iii) is between like and like exactly when the deposited mode set is finite, or when both are read as densities.
\end{enumerate}
\emph{Reading.} The scoping first offered, without proof, in Proposition \claimref{synthesis.mirror-asymmetry-route-one} at its version 2, and stated by P2 at its version 2 (labels, not states), under which P2 equates the superselection labels of the descent and not the state within the selected sector, is well defined and leaves $\xi$ free on every finite window, and on the full algebra exactly when the sum in (iii) converges; when infinitely many boundary modes share a frequency band, the same scoping reaches $\xi$ and gives $\xi = 1$, the value Proposition \claimref{synthesis.cold-mirror-needs-non-equilibrium-descent} reads as excluded under its hypothesis (M). Which case holds is decided by whether the deposited sector's mode set is finite, as the series' count of about $\pi N^{2}/\ln 2$ boundary modes for the cosmological horizon suggests (an observation-level count, not a premise here), or infinite, as the countable $J$ of the Definition allows. The scoping reaches the stored charge $Q = \epsilon N$ (Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}), but not the ceiling coupling, which is not a charge.

## technical
The question is whether the mirror's temperature is the same kind of quantity as the stored asymmetry, so that one rule could equate the second and not the first. In the boundary-mode model the asymmetry is a superselected charge: on every finite set of modes the observables split into blocks labelled by the two towers' charges, and states of different charge can be told apart by a central element. The temperatures are not labels of that kind: thermal states of the pair at any two temperatures give weight to every block, so no central element distinguishes them; within one block the temperature is a property of the state. On the infinite algebra the situation changes when infinitely many modes have frequencies in a bounded band away from zero: then, by the Powers-Stormer criterion, thermal states at different temperatures are disjoint, and the temperature becomes a label as well, in the same disjointness sense in which a charge density is one there (a thermal state over infinitely many modes has no finite total charge). A rule of indifference applied to labels of the descent and not to states can therefore free the mirror's temperature if the deposited sector has finitely many modes, as the series' mode count suggests, and cannot if it has infinitely many in a band. Such a rule reaches the asymmetry but not the ceiling coupling.

## lay
The framework's prediction of no extra radiation needs the mirror copy of our matter to be cold, while its indifference principle treats our world and the mirror alike. One way out is to say that the principle equalises only fixed labels of each world, like a conserved charge, and not the state each world happens to be in, like its temperature. This result checks whether that distinction is real in the mathematical model the framework uses. For any finite number of modes it is: the charge labels separate blocks of the theory, and temperature does not. With infinitely many modes at similar frequencies it fails, because temperature then becomes a label too. So the way out works only if the relevant number of modes is finite, which is something the framework has to decide.

## one-liner
Under (B'), in the boundary-mode model of a reversal pair, the stored tower charge is a superselection label on every finite window and the mirror's temperature is not, while on the infinite algebra the temperature is a label in the disjointness sense (the sense in which a charge density is one there) exactly when the Powers-Stormer sum diverges (for example, infinitely many modes in one frequency band); so a "labels, not states" scoping of P2 frees $\xi$ only if the deposited mode set is effectively finite.
