---
id: synthesis.massless-frequency-sign-relative-to-i4-is-not-the-chirality
kind: claim
version: 1
title: 'Massless frequency sign relative to $I_{4}$: helicity-locked, not the chirality'
status: proved
region: synthesis
subject: quantum-fields
tags: [chirality, pseudoscalar-and-centre, null-directions, thermal-premises]
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
derivations:
- name: main
  uses:
  - field-theory.fock-space-maxwell-modes@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_null_kernel_locks_helicity_to_the_frequency_sign
- kind: check
  ref: check.py::check_the_unit_is_minus_chirality_times_the_charge_rotation
- kind: check
  ref: check.py::check_lorentz_covariant_maps_are_right_multiplications
- kind: check
  ref: check.py::check_discrete_maps_flip_frequency_sign_and_chirality_independently
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.n-plus-null-ground-state
  - synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics
  - field-theory.fock-space-maxwell-modes
extraction:
  open_problem: op.r-premises-external
  note: >-
    Tests whether the orientation datum of (N+) (null vacuum versus filled sea, relative to the unit I4 and the
    time orientation) is the handedness of the doublets. Pre-registered kill condition: the identification
    dies if some kinematic map of the stated family flips the frequency sign and not the chirality, or the
    chirality and not the frequency sign. It dies: the spacetime-algebra charge conjugation psi -> psi sigma1
    flips the chirality only, a CP map flips the frequency sign only. Proved in general: on the null kernel
    S_k the boost bivector B_k = g0 n acts as -1 and the dual-plane bivector D_k = I4 B_k as -I4, so every
    massless even mode has helicity s/2 relative to I4 (restated for use: the same identities are
    synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays (iii)-(iv), there with the opposite sign
    convention B = n g0, and field-theory.where-each-lives (4); both are cited, not used, the first because it
    holds given several singularity premises); L_I4 = -Gamma R_{I sigma3}; the commutant of the left Lorentz action
    on Cl+(1,3) is the right action, so no pointwise Lorentz-covariant map changes the frequency sign; for the
    discrete maps a psi(Lambda^{-1} x) b the family keeping the massless equation is classified and
    s' = s (-1)^{|a|} sgn(g0 . Lambda k), flipping exactly for P and PT. The identity I4 B = D of
    synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics
    is re-derived in one line and cited, not used (field-theory.fock-space-maxwell-modes is used only for the
    chirality label e = -Gamma of its check's projectors): using it would import that result's premises, (N+) among
    them, into a result about (N+). Transport-absent. Literature: the name of Hestenes' charge conjugation
    psi -> psi sigma1, cited from memory as a name only; its action is computed here.
  flags:
  - 'the consequence for (N+) (Step 5) is argued: it shows that an identification of the orientation datum with the chirality Gamma is invariant under none of the maps that separate the two labels; it does not exclude a tie through some other structure of the series'
  - 'the identification of Gamma on Cl+(1,3) with the handedness of the series'' doublets (the sign of I6 relative to I4 on L_0, L_inf, field-theory.where-each-lives (3)) is assumed, not shown'
  - 'the family in (iv) is the maps psi(x) -> a psi(Lambda^{-1} x) b with a, b basis blades of the same parity and Lambda in {1, P, T, PT}; antilinear maps outside geometric algebra are not considered'
---

## formal
Work in $\Cl(1,3)$ with $\gamma_{0}^{2} = 1$, $\gamma_{1}^{2} = \gamma_{2}^{2} = \gamma_{3}^{2} = -1$, $I_{4} = \gamma_{0}\gamma_{1}\gamma_{2}\gamma_{3}$, $\sigma_{j} = \gamma_{j}\gamma_{0}$, $I\sigma_{3} = I_{4}\sigma_{3}$; spinors are even multivectors and the field theory's unit is $I_{4}$ (on spinors $L_{I_{4}} = R_{I_{4}}$, $L_{a}\psi = a\psi$, $R_{b}\psi = \psi b$). For future null $k = \omega(\gamma_{0} + n)$ ($\omega > 0$, $n \cdot \gamma_{0} = 0$, $Q(n) = -1$) put $B_{k} = \gamma_{0}n$ (minus the boost bivector $n\gamma_{0}$ of the generator in \claimref{synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays}; both fix the same $S_{k}$), $D_{k} = I_{4}B_{k}$ (for $k = \gamma_{0} + \gamma_{1}$, the wedge boost $\gamma_{0}\gamma_{1}$ and the dual plane $\gamma_{2}\gamma_{3}$ of \claimref{synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics}), $S_{k} = \{\psi \in \Cl^{+}(1,3) : k\psi = 0\}$, and call $\psi(x) = e^{-sI_{4}k\cdot x}\psi_{0}$, $\psi_{0} \in S_{k}$, $s = \pm 1$, a massless mode of frequency sign $s$. Let $\Gamma\psi = I_{4}\psi I\sigma_{3}$ be the chirality of massless even spinors (the projectors $\chi_{e} = \tfrac12(1 - e\Gamma)$ of the check of \claimref{field-theory.fock-space-maxwell-modes}, so its label is $e = -\Gamma$). Clauses (i) and (ii) restate, for use, identities already in the store: \claimref{synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays}(iii)-(iv) and \claimref{field-theory.where-each-lives}(4).
\begin{enumerate}
\item[(i)] \emph{(Helicity locked to the frequency sign; proved, restated.)} $\dim S_{k} = 4$, $L_{B_{k}} = -1$ and $L_{D_{k}} = -L_{I_{4}}$ on $S_{k}$. The rotation by $\theta$ about $n$, right-handed for $I_{3} = \gamma_{0}I_{4}$, is $\exp(\tfrac{\theta}{2}D_{k})$ and acts on $S_{k}$ as $e^{-I_{4}\theta/2}$; so a mode of frequency sign $s$ has energy $s\omega$, momentum direction $sn$ and helicity $s/2$ relative to $I_{4}$, for either chirality.
\item[(ii)] \emph{(The unit and the chirality; proved, restated.)} $\Gamma^{2} = 1$ and $L_{I_{4}} = -\Gamma R_{I\sigma_{3}}$ on $\Cl^{+}(1,3)$; $\Gamma$ commutes with the left rotor action and preserves $S_{k}$, with $2$-dimensional eigenspaces there. On a mode of chirality $\gamma$ the charge rotation $R_{I\sigma_{3}}$ equals $-\gamma L_{I_{4}}$, so the frequency sign relative to $I_{4}$ is $s = -\gamma s_{H}$, $s_{H}$ the frequency sign relative to the right unit $R_{I\sigma_{3}}$.
\item[(iii)] \emph{(Covariant maps are $I_{4}$-linear; proved.)} Every real-linear map of $\Cl^{+}(1,3)$ commuting with left multiplication by the Lorentz rotors is a right multiplication $R_{c}$, $c \in \Cl^{+}(1,3)$; hence it commutes with $L_{I_{4}}$ and preserves the frequency sign of every mode.
\item[(iv)] \emph{(Discrete maps; proved for the stated family.)} Let $\psi(x) \mapsto a\psi(\Lambda^{-1}x)b$, $a, b$ basis blades of the same parity, $\Lambda \in \{1, P, T, PT\}$ acting on vectors as $x$, $\gamma_{0}x\gamma_{0}$, $-\gamma_{0}x\gamma_{0}$, $-x$. It carries modes to modes with $s' = s(-1)^{|a|}\sgn(\gamma_{0}\cdot\Lambda k)$ and chirality $\gamma' = (-1)^{|a|}c(b)\gamma$, $c(b) = \pm 1$ as $b$ commutes or anticommutes with $I\sigma_{3}$. It keeps the massless equation exactly when $a \in \pm\{1, I_{4}\}$ for $\Lambda = 1, PT$ and $a \in \pm\{\gamma_{0}, \gamma_{0}I_{4}\}$ for $\Lambda = P, T$; within this family the frequency sign relative to $I_{4}$ flips exactly for $\Lambda \in \{P, PT\}$, the maps reversing the spatial orientation $I_{3}$. The charge conjugation $\psi \mapsto \psi\sigma_{1}$ flips the chirality and not the frequency sign; the CP map $\psi(x) \mapsto \gamma_{0}\psi(Px)\gamma_{0}\sigma_{1}$ flips the frequency sign and not the chirality; every pair $(s, \gamma)$ occurs on every $S_{k}$. The reversal under which Premise \claimref{synthesis.n-plus-null-ground-state} calls the filled sea the time reverse of the null vacuum is the $I_{4}$-linear one, $PT$ in this family, which flips $s$; the $I_{4}$-antilinear $T$ (odd $a$) keeps $s$.
\item[(v)] \emph{(Consequence; argued.)} The orientation datum of Premise \claimref{synthesis.n-plus-null-ground-state}, null vacuum versus filled sea relative to $I_{4}$ and the time orientation, is on massless modes the frequency sign relative to $I_{4}$: it is odd under spatial-orientation reversal and under CP, and even under charge conjugation, while the chirality $\Gamma$ of massless even spinors (the label $e = -\Gamma$) is odd under charge conjugation and even under CP. So the datum is not the chirality $\Gamma$; by (i) it can be read as a helicity orientation. Its identification with the handedness of the series' doublets, the sign of $I_{6}$ relative to $I_{4}$ on $L_{0}$, $L_{\infty}$ (\claimref{field-theory.where-each-lives}(3)), is assumed, not shown.
\end{enumerate}
Transport-absent.

## technical
The premise (N$_{+}$) leaves one orientation open: which of the two states with the same local data, the null vacuum or the filled sea, is the state of the light rays, a sign fixed only relative to the field unit $I_{4}$ and the direction of time. One might hope this sign is the handedness that the weak doublets already carry. For massless even spinors it is not. On the kernel of a null momentum the boost bivector acts as $-1$, so the rotation bivector of the dual plane acts as $-I_{4}$; every massless mode then has helicity equal to half its frequency sign relative to $I_{4}$, whatever its chirality (restated for use from \claimref{synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays}(iv) and \claimref{field-theory.where-each-lives}(4)). The field unit is minus the chirality times the charge rotation, $L_{I_{4}} = -\Gamma R_{I\sigma_{3}}$. The maps of spinors commuting with the Lorentz rotors are right multiplications, so they commute with $I_{4}$ and never change a frequency sign. Among the discrete maps $a\psi(\Lambda^{-1}x)b$ that keep the massless equation (classified here: $a$ is $1$ or $I_{4}$ for the identity and $PT$, $\gamma_{0}$ or $\gamma_{0}I_{4}$ for $P$ and $T$), the frequency sign flips exactly when the spatial orientation is reversed, while the chirality flips according to the parities of $a$ and $b$. Charge conjugation $\psi \mapsto \psi\sigma_{1}$ flips the chirality alone, CP flips the frequency sign alone. The reversal that (N$_{+}$) calls time reversal of the null vacuum is the $I_{4}$-linear $PT$, which flips the frequency sign; the antilinear $T$ of this family keeps it. So the (N$_{+}$) datum and the chirality $\Gamma$ are independent bits; the identification fails its pre-registered kill condition. The consequence for the premise, that the datum is not the chirality $\Gamma$, is argued from these transformation rules; that $\Gamma$ is the handedness of the series' doublets (\claimref{field-theory.where-each-lives}(3)) is assumed, not shown. The identity $I_{4}B = D$ of \claimref{synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics} is re-derived, not used; the result uses \claimref{field-theory.fock-space-maxwell-modes} only for the chirality label. Transport-absent.

## lay
The series assumes that the quantum modes on a horizon are in their lowest-energy state, but which of two mirror-image states that is depends on an orientation: how the field's imaginary unit, here the four-dimensional volume element of spacetime, is oriented relative to the direction of time. A natural guess is that this orientation is the same thing as the handedness (chirality) of the particles, the property the weak force is taken to act on. For massless particles it is not, although that the chirality computed here is the weak force's handedness is itself assumed. The orientation fixes the spin of each massless wave along its direction of motion, for left- and right-handed particles alike. Exchanging particles and antiparticles changes handedness without changing the orientation, and combining that with a mirror reflection changes the orientation without changing handedness, so the two cannot be one bit.

## one-liner
For massless even spinors with the field unit $I_{4}$, the frequency sign fixes the helicity, $\lambda = s/2$, for either chirality; pointwise Lorentz-covariant maps are right multiplications and keep it; among the discrete maps $a\psi(\Lambda^{-1}x)b$ keeping the massless equation it flips exactly under $P$ and $PT$, and charge conjugation $\psi\sigma_{1}$ flips the chirality alone while CP flips the frequency sign alone, so the orientation datum of (N$_{+}$) is not the chirality $\Gamma$ (argued; that $\Gamma$ is the doublets' handedness is assumed).
