---
id: synthesis.z-adapted-witt-flags-energy-sign-follows-the-flag-bit
kind: claim
version: 1
title: 'Energy sign and family of the $Z$-adapted Witt flags'
status: proved
region: synthesis
subject: conformal-spacetime
tags: [conformal-spinors, pseudoscalar-and-centre, grading-and-parity, thermal-premises]
proposed_by:
  kind: ai
  session: 2026-11-07-ga-units
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-07-ga-units
review: draft
about:
- obj.dark-matter.witt-flag
- obj.dark-matter.null-blades-fock-ideal-chirality
derivations:
- name: main
  uses:
  - synthesis.positive-conformal-energy-gives-positive-null-translations@7
  - dark-matter.two-families-are-two-chiralities@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_the_flag_operators_are_isotropic_with_an_eight_dimensional_kernel
- kind: check
  ref: check.py::check_the_conformal_energy_is_minus_s0_times_the_unit
- kind: check
  ref: check.py::check_the_family_is_the_orientation_and_flips_with_the_energy_sign_on_conjugate_pairs
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - dark-matter.premise-flag-as-datum
  - synthesis.n-plus-null-ground-state
  - synthesis.attachment-conformal-energy-is-generated-by-z
  - one-relation.arrow-frequency-are-one-bit-level
extraction:
  open_problem: op.r-premises-external
  note: >-
    Asks whether the orientation datum of (N+), read as the conformal-energy sign of a flag's Fock vacuum, is
    the stored flag bit. Pre-registered kill condition for the identification: both energy signs occur within
    one family. Over the eight orthogonal complex structures J_s preserving the planes (e0, nu), (e1, e2),
    (e3, e-) that happens (each (energy sign, family) pair occurs twice), but only across complex structures
    that are not conjugate; the stored bit of dark-matter.premise-flag-as-datum ranges over a conjugate pair,
    J against -J, and there the energy sign and the family flip together, s0 times the family being -s1 s2,
    a sign fixed with J up to J -> -J. So the kill condition as registered fires, while the datum, read this
    way, is the stored bit up to the kinematic sign s1 s2: the first version of this proposal read the count
    as two independent bits for the datum, which was overstated (referee, 7 November), and this version is
    restated to the weaker statement. Consistent with one-relation.arrow-frequency-are-one-bit-level and
    one-relation.imported-flag-arrow-superselection ("spent once, read twice"), cited, not used. The flag is
    written on the module with the conformal spinors' unit R_{I6} (w_a = L_{x_a} - s_a L_{y_a} R_{I6}), so no
    complexified vector space and no bare imaginary unit is needed. Signs in the store's normalisation
    (I6 = I4 E, E = nu e-): Z psi = -s0 psi I6 and I6 psi = omega psi I6 with omega = -s0 s1 s2 the
    orientation of J_s relative to I6 (the standard chirality of a pure spinor, Cartan and Chevalley, cited from
    memory). The positive-plane statement identifies the unit of
    synthesis.attachment-conformal-energy-is-generated-by-z with +R_{I6}, a convention; that result is cited,
    not used, since it holds given (N+). The conjugate-flag clause restates
    synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation (2)-(3) and
    dark-matter.two-families-are-two-chiralities (iii). The algebra is transport-absent; the derived ledger
    label essential is inherited from synthesis.positive-conformal-energy-gives-positive-null-translations,
    used only for the frame and Z.
  flags:
  - 'scope: only the eight Z-adapted flags; whether the descent''s flag (dark-matter.imported-derived-generation-flag) is among them, and what fixes its sign s1 s2, is open'
  - 'the reading of the (N+) datum as the conformal-energy sign of a flag''s vacuum (clause (v)) is argued, through the stored implication from positive conformal energy to positive null translations, with the attachment''s unit identified as +R_{I6}'
  - 'restated after an OVERSTATED verdict: the earlier reading (the datum a second orientation bit, independent of the stored one) is withdrawn'
---

## formal
Work in $\Cl(2,4)$ with the frame of Proposition \claimref{synthesis.positive-conformal-energy-gives-positive-null-translations}: $e_{0}^{2} = \nu^{2} = 1$, $e_{1}^{2} = e_{2}^{2} = e_{3}^{2} = e_{-}^{2} = -1$, $Z = e_{0}\nu$ (the conformal energy, $Z = P_{e_{0}} + e_{0}\nO$), $I_{4} = e_{0}e_{1}e_{2}e_{3}$, $E = \nu e_{-}$, $I_{6} = I_{4}E$; the conformal spinors' unit is right multiplication $R_{I_{6}}$, which commutes with every left multiplication. For $s = (s_{0}, s_{1}, s_{2}) \in \{1, -1\}^{3}$ let $J_{s}$ be the orthogonal complex structure $J_{s}e_{0} = s_{0}\nu$, $J_{s}e_{1} = s_{1}e_{2}$, $J_{s}e_{3} = s_{2}e_{-}$ ($J_{s}^{2} = -1$); these are the eight orthogonal complex structures preserving the planes $(e_{0}, \nu)$, $(e_{1}, e_{2})$, $(e_{3}, e_{-})$, and $J_{-s} = -J_{s}$. Their Witt flags $W_{s}$ (Definition \claimref{obj.dark-matter.witt-flag}) act on the module through the unit as $w_{1} = L_{e_{0}} - s_{0}L_{\nu}R_{I_{6}}$, $w_{2} = L_{e_{1}} - s_{1}L_{e_{2}}R_{I_{6}}$, $w_{3} = L_{e_{3}} - s_{2}L_{e_{-}}R_{I_{6}}$, and a pure spinor (Fock vacuum) of $W_{s}$ is a nonzero $\psi \in \Cl(2,4)$ with $w_{a}\psi = 0$ for all $a$, equivalently $v\psi = (J_{s}v)\psi I_{6}$ for every vector $v$.
\begin{enumerate}
\item[(i)] \emph{(The flags; proved.)} The $w_{a}$ are nilpotent and pairwise anticommute; the pure spinors of $W_{s}$ span an $8$-dimensional real space, generated by any one of them under right multiplication by $\Cl^{+}(2,4)$; in $\CS = \Cl^{+}(2,4)P$ (respectively its odd counterpart) the pure spinor is unique up to $\mathrm{span}\{1, I_{6}\}$.
\item[(ii)] \emph{(The conformal energy sees $s_{0}$; proved.)} $Z\psi = -s_{0}\,\psi I_{6}$ on every pure spinor of $W_{s}$; $s_{0}$ is the orientation of $J_{s}$ on the plane of $Z$, $e_{0}\wedge J_{s}e_{0} = s_{0}Z$. With the unit of \claimref{synthesis.attachment-conformal-energy-is-generated-by-z}(i) identified as $+R_{I_{6}}$ (a convention; with $-R_{I_{6}}$, $T_{+}$ and $T_{-}$ exchange), the vacuum lies in the positive plane $T_{+}$ of the twistor form exactly when $s_{0} = 1$.
\item[(iii)] \emph{(The family is the orientation; proved.)} $I_{6}\psi = \omega(J_{s})\,\psi I_{6}$ on every pure spinor of $W_{s}$, where $\omega(J_{s}) = -s_{0}s_{1}s_{2}$ is the orientation of $J_{s}$ relative to $I_{6}$, $e_{0}\wedge J_{s}e_{0}\wedge e_{1}\wedge J_{s}e_{1}\wedge e_{3}\wedge J_{s}e_{3} = \omega(J_{s})I_{6}$: the vacuum lies in $\CS$ when $\omega = 1$ and in $\CSm$ when $\omega = -1$, so $\omega$ is the family of $W_{s}$ (Proposition \claimref{dark-matter.two-families-are-two-chiralities}). With the opposite orientation of $I_{6}$ the family reads $+s_{0}s_{1}s_{2}$ for the same $s$, and (ii) is unchanged. The orientation of $J_{s}$ on the four-space orthogonal to $Z$ is $s_{1}s_{2}$; the conjugate flag $W_{-s}$ lies in the other family (as in \claimref{synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation}(2)-(3)).
\item[(iv)] \emph{(Conjugate pairs; proved.)} As functions on the eight flags, $s_{0}$ and the family are independent: each of the four pairs occurs for exactly two flags. On each conjugate pair $\{W_{s}, W_{-s}\}$, the two values of the orientation bit of Premise \claimref{dark-matter.premise-flag-as-datum} ($J$ against $-J$), both flip, and $s_{0}\,\omega(J_{s}) = -s_{1}s_{2}$ is the same on both.
\item[(v)] \emph{(Reading; argued.)} So, read as the energy sign of the flag's vacuum (through \claimref{synthesis.positive-conformal-energy-gives-positive-null-translations}(ii), with the attachment's unit identified as $+R_{I_{6}}$), the orientation datum of Premise \claimref{synthesis.n-plus-null-ground-state} is the stored flag bit up to the sign $s_{1}s_{2}$ of the descent's complex structure on the four-space orthogonal to $Z$, a kinematic sign fixed with $J$ up to $J \mapsto -J$; this is consistent with \claimref{one-relation.arrow-frequency-are-one-bit-level}. Whether the descent's flag is $Z$-adapted is open.
\end{enumerate}
The algebra is transport-absent; the ledger label essential is inherited from the frame's source.

## technical
The descent plants a Witt flag, a choice of which half of each null pair annihilates the Fock vacuum, and its family, the chirality of that vacuum, is the stored orientation bit: the sign of the flag's complex structure $J$ against $-J$. The premise (N$_{+}$) leaves a sign open that decides the direction of the null translations, and positive conformal energy $Z = e_{0}\nu$ gives positive null translations, so one may ask how the energy sign of a flag's vacuum relates to its family. For the eight flags adapted to the three planes $(e_{0}, \nu)$, $(e_{1}, e_{2})$, $(e_{3}, e_{-})$, written on the module with the conformal spinors' unit $R_{I_{6}}$ as three anticommuting nilpotent operators $L_{x} - sL_{y}R_{I_{6}}$, the vacuum satisfies $v\psi = (J_{s}v)\psi I_{6}$. The conformal energy acts on it as $-s_{0}R_{I_{6}}$, set by the orientation of the flag on the plane of $Z$, while left multiplication by $I_{6} = I_{4}E$ acts as $\omega(J_{s})R_{I_{6}}$, $\omega = -s_{0}s_{1}s_{2}$ the orientation of $J_{s}$ relative to $I_{6}$, which is the family. Across all eight flags the two signs are independent, but that compares complex structures that are not conjugate. The stored bit ranges over a conjugate pair, $J$ and $-J$, and there both signs flip together with $s_{0}\omega = -s_{1}s_{2}$ fixed. So, read as the energy sign of the flag's vacuum (with the attachment's unit taken as $+R_{I_{6}}$, a convention), the (N$_{+}$) datum is the stored flag bit up to the descent's sign $s_{1}s_{2}$ on the four-space orthogonal to $Z$, in line with the stored statement that the arrow and the frequency sign are one bit (\claimref{one-relation.arrow-frequency-are-one-bit-level}). This reading is argued; whether the descent's flag is of this kind is open. The algebra is transport-absent; the ledger label essential is inherited from the source of the frame.

## lay
The series makes one orientation choice when the theory descends to spacetime: for every pair of directions at once, which half of each pair empties the vacuum. Its overall handedness is stored as a single bit, and flipping the bit flips every half. A different-looking sign decides which way energy runs along light rays near a horizon. For a natural family of eight such choices, the energy sign is set by one of the three pairs and the stored handedness by all three together, so across the family they look unrelated. But flipping the stored bit flips both at once: once the descent's choice is fixed up to that flip, the energy sign is the stored bit read a second way, up to one fixed sign of the other two pairs.

## one-liner
For the eight Witt flags adapted to the planes $(e_{0}, \nu)$, $(e_{1}, e_{2})$, $(e_{3}, e_{-})$, written with the unit $R_{I_{6}}$, the conformal energy acts on the flag's vacuum as $-s_{0}R_{I_{6}}$ and $I_{6} = I_{4}E$ as $\omega R_{I_{6}}$, $\omega = -s_{0}s_{1}s_{2}$ the orientation of $J_{s}$; across the eight they are independent, but on each conjugate pair (the stored bit, $J$ against $-J$) they flip together, so the energy-sign reading of the (N$_{+}$) datum is the stored flag bit up to the kinematic sign $s_{1}s_{2}$ (argued).
