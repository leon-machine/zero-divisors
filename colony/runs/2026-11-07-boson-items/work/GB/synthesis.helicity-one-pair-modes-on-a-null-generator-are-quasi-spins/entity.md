---
id: synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins
kind: claim
version: 1
title: 'Helicity-one pair modes on a null generator are quasi-spins, not bosons'
status: proved
region: synthesis
subject: quantum-fields
tags: [bosonisation, car-algebra, gauge-fields, no-go]
proposed_by:
  kind: ai
  session: 2026-11-07-boson-items
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-07-boson-items
review: draft
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - tower.ladder-pairs-satisfy-car-vectors@4
  - std-algebra.orthogonal-anticommute@1
  - hawking.current-commutator-exactly-edge-split@4
  - field-theory.how-close-tower-comes-ccr@4
  - synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_window_commutator_identity
- kind: check
  ref: check.py::check_edge_clean_value_and_normality
- kind: check
  ref: check.py::check_helicity_one_is_nilpotent_and_not_normal
- kind: check
  ref: check.py::check_helicity_one_mode_is_a_quasi_spin
- kind: check
  ref: check.py::check_sea_annihilates_and_forms_are_nonnegative
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum
  - field-theory.fock-space-maxwell-modes
  - field-theory.composite-gauge-bosons-what-excluded
extraction:
  open_problem: bos.gauge-bosons
  note: >-
    Adversarial attack on the run target bos.gauge-bosons (what part of photon quantisation the tower gives).
    Answer, for pair modes on one null generator with any finite channel content: exact canonical pair modes are
    the normal ones, helicity-one modes are never normal, and they are quasi-spins with a finite number of
    quanta. New here: (i) the window identity for rho_q(M) with an arbitrary channel matrix M (entries in
    span{1, J}) over any finite channel set, and its edge-clean value q tr(M'*M) + rho_0([M, M'*]) (for two
    channels this is the level-one u(2) identity read on matrices); (ii) such a mode is a canonical boson on the edge-clean vectors if and only if
    M is normal; (iii) a mode of helicity +-1 about the generator ([W, M] = +-M for the channel weights W) is
    nilpotent, hence never normal, and its commutator carries the channel-number difference; no two commuting
    canonical pair modes rotate as a vector (linear polarisations), by the normal-and-nilpotent argument
    applied to M_1 -+ J M_2; (iv) on the chiral sea a helicity-one mode of momentum q is the quasi-spin of
    q rank(M) two-level sites, with |B^p Omega|^2 = (p!)^2 e_p strictly below the Bose value for p >= 2 and
    zero beyond q rank(M); (v) every annihilating pair mode of every tower state has a nonnegative form, so
    the timelike Gupta-Bleuler mode of (K1) is not a pair mode. Stored and cited, not refiled: the
    one-channel edge identity (hawking.current-commutator-exactly-edge-split), the quasi-spin ladder
    (field-theory.how-close-tower-comes-ccr, fluctuation-forms (ii)), the band density bosons of the null
    vacuum (fluctuation-forms (vi)), the chirality channels and their weights +-1/2 about the generator
    (light-ray-good-part (iii), (iv)), the composite-photon exclusions of Weinberg-Witten type
    (composite-gauge-bosons-what-excluded), which concern Lorentz-covariant currents and are a different
    obstruction. The window restriction of the null vacuum is the chiral sea used here (fluctuation-forms
    (vi)); that identification is context, not a premise, so the result does not hold given (N+). Premise
    (KF) is cited in (v) and in the reading, not used. The weights may be any real numbers, so the result
    covers any finite channel space per light ray (several species and flavours, and a finite set of
    transverse cells for modes of zero transverse momentum, with weights from spin only); the contraction
    reading (many transverse cells) is argued. Prior art, orientation only, cited from memory: level-one
    affine current algebras, in which the commutator of off-diagonal currents contains the Cartan current
    (Frenkel and Kac 1980, vertex operators; Pressley and Segal 1986); the Holstein-Primakoff and quasi-spin
    contractions. Ledger: transport-absent (finite CAR on tower planes; no transport completion used).
---

## formal
Let the modes on one null generator carry a generator momentum $k$ in the window $I = \{-N, \dots, N - 1\}$ and a channel $\alpha$ in a finite set; each mode $(k, \alpha)$ is a tower plane with $a_{k,\alpha}^{*} = v$, $a_{k,\alpha} = w$ (Theorem \claimref{tower.ladder-pairs-satisfy-car-vectors}), with the adjoint $*$ ($v^{*} = w$). Numbers are read in $\mathrm{span}\{1, J\}$, $J = g_{1}g_{2}$ the kernel bivector, which commutes with every mode, $J^{2} = -1$, $J^{*} = -J$. For a channel matrix $M$ with entries in $\mathrm{span}\{1, J\}$ ($M^{*}$ its conjugate transpose) and $q \ge 0$ let $\rho_{q}(M) = \sum_{k, k+q \in I}\sum_{\alpha,\beta}M_{\alpha\beta}a_{k,\alpha}^{*}a_{k+q,\beta}$. The transverse rotation by $\theta$ about the generator acts by $a_{k,\alpha} \mapsto e^{-\theta w_{\alpha}J}a_{k,\alpha}$ with real weights $w_{\alpha}$, $W = \mathrm{diag}(w_{\alpha})$; the two chirality channels of a Dirac species have $w = \pm\tfrac12$ (Theorem \claimref{synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays}(iv)). $\rho_{q}(M)$ has helicity $h$ if the rotation multiplies it by $e^{h\theta J}$. The chiral sea $\Omega$ has every channel filled for $k < 0$ and empty for $k \ge 0$; a vector is edge-clean at depth $q$ if the lowest $q$ momenta are filled and the highest $q$ empty in every channel.
\begin{enumerate}
\item[(i)] \emph{(Window identity.)} $[\rho_{q}(M), \rho_{q}(M')^{*}] = \sum_{k, k+q \in I}a_{k}^{*}MM'^{*}a_{k} - \sum_{k, k-q \in I}a_{k}^{*}M'^{*}Ma_{k}$ exactly, with $a_{k}^{*}Xa_{k} = \sum X_{\alpha\beta}a_{k,\alpha}^{*}a_{k,\beta}$; on edge-clean vectors it acts as $q\operatorname{tr}(M'^{*}M) + \rho_{0}([M, M'^{*}])$.
\item[(ii)] \emph{(Normality.)} For $N > q$, $[\rho_{q}(M), \rho_{q}(M')^{*}]$ is a scalar on the edge-clean vectors if and only if $[M, M'^{*}] = 0$; so $\rho_{q}(M)$ is a canonical boson there (value $q\operatorname{tr}(M^{*}M)$) if and only if $M$ is normal.
\item[(iii)] \emph{(Helicity.)} $\rho_{q}(M)$ has helicity $h$ if and only if $[W, M] = hM$. For $h \ne 0$ such an $M$ is nilpotent, hence, if nonzero, not normal: a pair mode of helicity $\pm1$ is never a canonical boson on the edge-clean vectors, its commutator there carrying the operator $\rho_{0}([M, M^{*}])$ (for $M = E_{+-}$ the difference of the channel numbers). If $\rho_{q}(M_{1}), \rho_{q}(M_{2})$ rotate as a vector ($J[W, M_{1}] = M_{2}$, $J[W, M_{2}] = -M_{1}$) and $[M_{i}, M_{j}^{*}] = 0$ for all $i, j$, then $M_{1} = M_{2} = 0$: no two pair modes with central mutual commutators form a rotation doublet. Normal helicity-zero modes (the channel densities among them) are canonical bosons.
\item[(iv)] \emph{(Quasi-spin.)} Let $M^{2} = 0$, $r = \operatorname{rank}M$, $N \ge q \ge 1$, $B = \rho_{q}(M)^{*}$. Then $|B^{p}\Omega|^{2} = (p!)^{2}e_{p}(x)$, $x$ the $qr$ numbers $\sigma_{s}^{2}$ (singular values of $M$, each repeated $q$ times), so $B^{p}\Omega = 0$ for $p > qr$ and $|B^{p}\Omega|^{2} < p!\,|B\Omega|^{2p}$ for $p \ge 2$. For $M = E_{+-}$: $|B^{p}\Omega|^{2} = (p!)^{2}\binom{q}{p}$ and $[\rho_{q}(M), B]B^{p}\Omega = (q - 2p)B^{p}\Omega$, the quasi-spin of $q$ sites.
\item[(v)] \emph{(Positivity.)} For every state $\omega$ of the tower and every $X$ with $\omega(X^{*}X) = 0$, $\omega([X, X^{*}]) = \omega(XX^{*}) \ge 0$. On the chiral sea every $\rho_{q}(M)$, $q \ge 1$, annihilates $\Omega$ and $\omega_{\Omega}([\rho_{q}(M), \rho_{q}(M)^{*}]) = q\operatorname{tr}(M^{*}M)$; on the reversed sea the value is $-q\operatorname{tr}(M^{*}M)$ and $\rho_{q}(M)^{*}$ annihilates. No pair mode of a tower state annihilates the state with a negative commutator, as the timelike polarisation of (K1) in Premise \claimref{synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields} would.
\end{enumerate}
Clauses (i) to (v) are proved. \emph{Reading (argued).} On the window restriction of the null vacuum, the chiral sea (Theorem \claimref{synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum}(vi)), the exact pair bosons are helicity-zero density waves; a helicity-one quantum about the generator built from pairs is a quasi-spin, canonical only in the contraction over many two-level sites (for instance many transverse cells), with the channel-number difference as the obstruction operator. So the tower gives the photon's canonical relations from pairs at most as a contraction, and the indefinite form of (KF) not at all; the stored elementary photon (\claimref{field-theory.fock-space-maxwell-modes}) and (KF) are unchanged.

## technical
Take the modes on one null generator, labelled by a generator momentum $k$ in the window $I = \{-N, \dots, N - 1\}$ and a channel in a finite set, each a tower plane, with numbers in $\mathrm{span}\{1, J\}$ ($J$ the kernel bivector, commuting with every mode). Pair modes are $\rho_{q}(M) = \sum_{k}a_{k}^{*}Ma_{k+q}$ for a channel matrix $M$; the rotation about the generator multiplies channel $\alpha$ by $e^{-\theta w_{\alpha}J}$, with weights $\pm\tfrac12$ for the two chirality channels of a Dirac species. (i) Exactly, $[\rho_{q}(M), \rho_{q}(M')^{*}]$ is the sum of $a_{k}^{*}MM'^{*}a_{k}$ over $k$ with $k + q$ in the window minus the sum of $a_{k}^{*}M'^{*}Ma_{k}$ over $k$ with $k - q$ in the window; on vectors whose lowest $q$ momenta are filled and highest $q$ empty it is $q\operatorname{tr}(M'^{*}M) + \rho_{0}([M, M'^{*}])$. (ii) With a bulk momentum present, that is a scalar exactly when $[M, M'^{*}] = 0$, so $\rho_{q}(M)$ is a canonical boson exactly when $M$ is normal. (iii) Helicity $h$ means $[W, M] = hM$; for $h = \pm1$ the matrix is nilpotent and so, if nonzero, not normal: the commutator keeps the channel-number difference. Two linear polarisations rotating into each other cannot both be canonical with central mutual commutators, since $M_{1} \mp JM_{2}$ would be normal and nilpotent. Normal helicity-zero modes, such as the channel densities, are exact bosons. (iv) On the chiral sea a nilpotent mode of rank $r$ at momentum $q$ is a quasi-spin of $qr$ two-level sites: $|B^{p}\Omega|^{2} = (p!)^{2}e_{p}$, strictly below the Bose value for $p \ge 2$ and zero beyond $qr$ quanta; for the flip $E_{+-}$ the normalised commutator on $p$ quanta is $1 - 2p/q$. (v) A mode that annihilates a positive state has a nonnegative commutator in it, so no pair mode is the timelike Gupta-Bleuler mode that the Krein premise (KF) uses. Reading (argued): the null vacuum's exact pair bosons are helicity-zero density waves; helicity-one pair quanta exist only as the contraction of a quasi-spin over many sites; the elementary photon and (KF) stay as stored.

## lay
The graph already shows that ripples in the density of the fermions filling a light ray behave exactly like bosons. This result asks whether such ripples could be photons, which spin about their direction of motion (helicity one). On a single light ray the answer is no: the ripples that are exactly bosons do not spin, and the ripples that do spin behave like a finite collection of two-state switches, which fill up after a few quanta and only approach boson behaviour when very many of them are pooled. The indefinite bookkeeping that standard photon quantisation uses for its unphysical time-like polarisation also cannot come from these ripples, because every state of the fermions has positive probabilities.

## one-liner
A fermion-pair mode on a null generator is a canonical boson on the window's edge-clean vectors iff its channel matrix is normal; helicity-one pair modes are nilpotent quasi-spins of q rank(M) sites, and no pair mode is a Gupta-Bleuler timelike mode.
