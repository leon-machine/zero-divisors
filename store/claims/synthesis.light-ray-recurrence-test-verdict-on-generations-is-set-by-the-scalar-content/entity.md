---
id: synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content
kind: claim
version: 1
title: 'Light-ray recurrence test: with additive bosons, scalars and graviton set the verdict'
status: proved
region: synthesis
subject: quantum-fields
tags: [boundary-modes, mode-counting, counting-rules, undetermined-input, no-go]
proposed_by:
  kind: ai
  session: 2026-11-09-solvable
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-09-solvable
review: draft
derivations:
- name: main
  uses:
  - synthesis.slot-module-light-ray-arrays-are-weyl-components@3
  - synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators@1
  - synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays@5
  - standard-model.connection-forced@5
  - synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum@5
  - synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations@4
  - synthesis.null-ordering-of-counted-units-is-zeta-symmetric@4
  assumes:
  - singularity.q-joint-quasi-freeness-s-wave@3
  - synthesis.window-reading-array-killing-energy@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_scalar_null_data_carries_no_potential
- kind: check
  ref: check.py::check_content_count_and_gauge_vectors_drop_out
- kind: check
  ref: check.py::check_verdict_on_generations
- kind: check
  ref: check.py::check_neutral_singlet_and_the_per_generation_count
- kind: check
  ref: check.py::check_boson_fermion_balance_passes_every_generation_number
- kind: check
  ref: check.py::check_real_array_zero_point_and_the_j3_reading
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.null-ordering-of-counted-units-is-zeta-symmetric
  - synthesis.slot-module-light-ray-arrays-are-weyl-components
extraction:
  maintainer_pass:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'Leon approved the assumes edges named at acceptance: (Q) singularity.q-joint-quasi-freeness-s-wave@3 and the window reading synthesis.window-reading-array-killing-energy@1, under which the tests are posed, are now assumed directly and cited in the proof; the intended citation of the sibling one-window result is now a plain cross-reference; the sentence on the narrowing of J3 now follows its version 2 (the current-boson identification kept for every massless field, so vectors and scalars stay currents under J3); statement unchanged.'
  maintainer_pass_2026_11_09b:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'Note only: one sentence added on hawking.joint-j3-s-wave-reduction version 3 (even-parity spin 2 only, partial-wave wording, identification not injective); reading (2) and the statement are unchanged.'
  open_problem: op.counted-mode-energy
  note: >-
    Adversarial attack on the open question of op.counted-mode-energy "which fields form the light-ray sea" and,
    through it, on the generation number of op.qft-structural-inputs. The recorded argument (prose in the problem's
    known field) is that a one-window recurrence of fermion parity with the zeta ordering needs the sea's light-ray
    central charge c to be a multiple of 24, that the spin-1/2 content alone gives 16 n_g, and that adding the
    integer-weight fields gives 78 at n_g = 3. This result takes the test as given and asks what its verdict on
    n_g depends on, under two readings of the bosons. (1) The additive reading: the null data of the gauge vectors,
    the scalar doublets and (eps = 1) the graviton are counted as real arrays of their own, on top of the sixteen
    Weyl arrays per generation. This reading is outside the CAR scope of (N+) and of the window reading, and it is
    not the reading of the stored postulate J3 (hawking.joint-j3-s-wave-reduction, in the past cone through the
    null-ordering result and the collapse result), which identifies each channel of every four-dimensional massless
    field, the graviton included, with the current boson of the s-wave theory, the bosonised current of the arrays.
    Under it: each field's null data are counted for every mass matrix and potential (the scalar case is new here;
    the fermion and abelian vector cases are stored; the non-abelian vector count and the integer weight of scalar
    data are argued); the twelve gauge vectors contribute 24 and drop out; the verdict tracks the doublets
    (n_g = 0 mod 3 needs n_h = 0 mod 6 for one window, 0 mod 3 for two; the two doublets of the linear rung field
    pass n_g = 1, 4 and fail 3; one doublet passes n_g = 2 under the two-window test); and a graviton counted
    additively, as J3's species list would have it, makes every content fail. (2) J3's reading: the integer-weight
    channels are currents of the arrays and add nothing, c = 16 n_g, and both tests give 3 | n_g. Either way the
    title's condition matters: the scalar and graviton content set the verdict only under the additive reading.
    On 9 November J3 was restated (version 2): its channel-reduction clause is assumed for spin 2 only, since
    synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional derives it for spins 0, 1/2
    and 1, while its current-boson identification is kept for every massless field; so under J3 version 2 the
    vectors and scalars are still read as currents of the arrays, and reading (2) is unchanged. J3 version 3 (same
    day) keeps the channel-reduction clause for even-parity spin 2 only, words the reduction per partial-wave
    channel, l >= |s|, and records that the identification is not one array tower per helicity channel; reading (2),
    in which the integer-weight channels add no array, is again unchanged, and is the reading J3 version 3 states.
    The modulus 3 appears because 16 is 2^4 and 24 = 8 * 3: any per-generation count of 8 or 16
    mod 24 gives it. Under boson-fermion balance, the vanishing of the stored quartic Sakharov coefficient, c = 48
    n_g and the test is blind to n_g. The two-window test (the evolution over two windows equal to 1, equivalently
    the one-window evolution equal to the grading up to sign) is included because it is the weakest operator-level
    recurrence; the one-window form adds one sign, the grading being normalised to +1 on the sea. The unit: on the
    arrays of (Q) the phase is written with the boundary-mode unit J (the boundary-mode algebra keeps its own complex
    unit, whose modes anticommute with I_4); on the continuum light ray it is I_4; the condition on c is the same.
    See synthesis.one-window-parity-recurrence-of-the-light-ray-sea-needs-twenty-four-arrays, whose clause (iv)
    derives the -kappa/24 of a real integer-weight component and whose one-window theorem is the form
    U = e^{2 pi J c/24} P assumed here; the zeta value used here is re-derived in the proof. The fifteen-component
    case of (iv) repeats that result's count as one instance of the general rule. What is not claimed: which
    fields form the sea, and anything fixing three rather than six or nine. Argued, not part of the statement:
    under spontaneous breaking the null-data count is unchanged (three Goldstone components become three
    longitudinal data, 2 * 9 + 3 * 3 + 1 = 28 = 24 + 4); and the recurrence cannot be posed on the whole Hamiltonian
    of a hole, whose label constant M gives the window phase L M = 8 pi M^2 = A/2 = 2S, so recurrence would put S in
    pi(Z + c/24), against S = (ln 2)/2 per array of (Q) version 3, since ln 2/pi is irrational (Gelfond: e^pi is
    transcendental; cited from memory). Prior art (literature, not premises; web-verified on 9 November 2026 unless
    marked): J. Wang, arXiv:2312.14928 (2023), the framing anomaly c_- = 0 mod 24 with c_- = 8 per family of 16
    Weyl fermions read as Majorana-Weyl fermions on a domain wall: the conclusion 3 | n_g is prior art (Wang's
    arithmetic is 8 n_g = 0 mod 24, c = 1/2 per Weyl fermion, not 1 per complex array; the fifteen-component cases
    differ); I. Garcia-Etxebarria and M. Montero, JHEP 08 (2019) 003, arXiv:1808.00009, the Z16 Dai-Freed anomaly
    and sixteen per generation, and, in the same paper, a mod-9 Dai-Freed anomaly of baryon triality that cancels
    only when the number of generations is a multiple of 3, direct prior art for 3 | n_g; Z. Wan, J. Wang and
    S.-T. Yau, arXiv:2605.26202 (2026; abstract read), which cancels the mixed (B+L)-gauge-gravitational anomaly of
    a Standard Model without right-handed neutrinos by a Z_3 gauge TQFT, with N = N_c = N_f = 3 the minimal solution;
    E. Witten, Commun. Math. Phys. 121 (1989) 351 (framing anomaly, cited from memory). There c_- is the net chiral
    central charge, blind to bosons and to vector-like pairs; the additive light-ray count counts every field's null
    data with the same sign, so it agrees with theirs on fermion-only content (clause (iv)) and differs as soon as
    bosons or vector-like fermions enter. Transport-absent: two-dimensional central-charge bookkeeping on the
    series' recorded content.
---

## formal
Units $\hbar = c = 1$. On a generator of a horizon in the scope of Premise (N$_{+}$), a \emph{complex array} is an array of Premise \claimref{singularity.q-joint-quasi-freeness-s-wave} version 3, weights $\kappa(k + \tfrac12)$, and a \emph{real array} the modes of one real chiral boson at integer weights $\kappa k$, which carries $-\kappa/24$ over a window $2\pi/\kappa$ in the zeta-regularised symmetric ordering ($\tfrac{\kappa}{2}\zeta(-1) = -\kappa/24$, as each complex array does, Theorem \claimref{synthesis.null-ordering-of-counted-units-is-zeta-symmetric}(ii)). For a content with $f$ complex and $b$ real arrays per generator put $c = f + b$, and call the \emph{one-window test} the condition $24 \mid c$ and the \emph{two-window test} the condition $12 \mid c$. They are the conditions for $e^{2\pi Jc/24} = 1$ and $e^{2\pi Jc/12} = 1$ ($J$ the unit of the boundary-mode arrays; on the continuum light ray the unit is $I_{4}$ and the conditions are the same), that is, for a window evolution of the form $e^{2\pi Jc/24}P$, with $P$ the grading normalised to $+1$ on the sea, to be $P$, respectively to be $\pm P$, equivalently the evolution over two windows to be $1$. That form is the reading under which the tests are posed; nothing below uses it. Call the \emph{additive reading} the reading in which the light-ray sea contains, besides the sixteen Weyl arrays per generation and in addition to them, one real array per real component of the null data of the gauge vectors, of the scalar doublets and, if $\epsilon = 1$, of the graviton. It lies outside the CAR scope of (N$_{+}$) and of the window reading, and it is not the reading of Premise \claimref{hawking.joint-j3-s-wave-reduction} (J3), which identifies every channel of each four-dimensional massless field with the current boson of the s-wave theory, a current of the arrays. Then:
\begin{enumerate}
\item[(i)] \emph{(Null data of each field, under the additive reading.)} On a null plane $N_{k}$ of $\Cl(1,3)$, $k = \gamma_{0} + \gamma_{3}$, $m = \gamma_{0} - \gamma_{3}$, $Q(k) = Q(m) = 0$, $\ip{k}{m} = 2$: every Weyl component gives one complex array for every mass matrix (Theorem \claimref{synthesis.slot-module-light-ray-arrays-are-weyl-components}(i)); every abelian gauge vector gives two real fields per generator (Theorem \claimref{synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators}(ii)), at integer boost weight (Theorem \claimref{synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays}(vi)), and the same count for each component of a non-abelian vector is argued, not proved; and every real scalar component gives one real field per generator for every potential $V$: for linearised solutions $\phi_{1}, \phi_{2}$ of $\nabla^{2}\phi + V'(\phi) = 0$ the current $\omega = \phi_{1}\nabla\phi_{2} - \phi_{2}\nabla\phi_{1}$ has $\nabla\cdot\omega = \phi_{1}\nabla^{2}\phi_{2} - \phi_{2}\nabla^{2}\phi_{1} = 0$, its flux through $N_{k}$ is $k\cdot\omega = \phi_{1}(k\cdot\nabla)\phi_{2} - \phi_{2}(k\cdot\nabla)\phi_{1}$, which contains neither $V$ nor a transverse derivative, and $\nabla^{2} = (k\cdot\nabla)(m\cdot\nabla) - \partial_{1}^{2} - \partial_{2}^{2}$, so the field equation fixes $(m\cdot\nabla)\phi$ on $N_{k}$ from $\phi$ there and one boundary value per generator (that these data carry integer weight, so form a real array, is argued). Hence, under the additive reading, a content of $n_{g}$ generations of the slot module (sixteen Weyl components each, Theorem \claimref{synthesis.slot-module-light-ray-arrays-are-weyl-components}(ii)), $n_{V}$ gauge vectors, $n_{s}$ real scalar components and, if a graviton's two helicities are counted, $\epsilon = 1$ ($\epsilon = 0$ otherwise) has
\[
c = 16n_{g} + 2n_{V} + n_{s} + 2\epsilon ,
\]
for every mass matrix and every scalar potential.
\item[(ii)] \emph{(The gauge vectors drop out, additive reading.)} With the connection-forced algebra $\su(3) \oplus \su(2) \oplus \uu(1)$ (Theorem \claimref{standard-model.connection-forced}), $n_{V} = 12$ and the vectors contribute $24$, so they change neither test. A gauge algebra of dimension $d$ drops out of the one-window test if and only if $12 \mid d$, and of the two-window test if and only if $6 \mid d$.
\item[(iii)] \emph{(The verdict on generations, additive reading.)} With $n_{V} = 12$ and $n_{s} = 4n_{h}$ ($n_{h}$ doublets), the one-window test holds if and only if $\epsilon = 0$ and $n_{h} \equiv 2n_{g} \pmod 6$, and the two-window test if and only if $\epsilon = 0$ and $n_{g} + n_{h} \equiv 0 \pmod 3$. So: with no scalar counted both hold exactly when $3 \mid n_{g}$; with one doublet the one-window test fails for every $n_{g}$ and the two-window test holds exactly when $n_{g} \equiv 2 \pmod 3$ ($c = 60$ at $n_{g} = 2$, where the window evolution is $-P$); with the eight real components of the linear rung field (Theorem \claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum}), $n_{h} = 2$, both hold exactly when $n_{g} \equiv 1 \pmod 3$, so $n_{g} = 1$ and $4$ pass and $n_{g} = 3$ fails ($c = 80$); with $\epsilon = 1$ (the graviton counted additively, as J3's species, every massless field, would include it) neither holds for any $n_{g}$, $n_{h}$ ($c \equiv 2 \pmod 4$). The content $n_{h} = 1$, $\epsilon = 1$ gives $c = 78$ at $n_{g} = 3$.
\item[(iv)] \emph{(The per-generation count.)} With $f$ Weyl components per generation and nothing else, the one-window test holds if and only if $24/\gcd(24, f)$ divides $n_{g}$ (the two-window test likewise with $12$), and the one-window modulus is $3$ exactly when $f \equiv 8$ or $16 \pmod{24}$. Fifteen components per generation (no neutral singlet, not a CPT halving of the slot module) give $8 \mid n_{g}$ and $4 \mid n_{g}$; sixteen components and the count of eight Majorana-Weyl units per generation give the same modulus $3$.
\item[(v)] \emph{(Boson-fermion balance, additive reading.)} If $b = 2f$, the balance of on-shell degrees of freedom at which the quartic coefficient $2N_{V} + N_{S} - 2N_{W}$ of the attachment's Sakharov sum vanishes (Theorem \claimref{synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations}(iv), here with $\epsilon = 0$), then $c = 3f = 48n_{g}$ and both tests hold for every $n_{g}$; at $n_{g} = 3$, $N_{V} = 12$ this is that theorem's $N_{S} = 72$, with $c = 144$.
\item[(vi)] \emph{(J3's reading.)} If the integer-weight channels are read as J3 reads them, currents of the arrays, they add no array, $c = 16n_{g}$, and both tests hold exactly when $3 \mid n_{g}$.
\end{enumerate}
So the scalar and graviton content set the verdict only under the additive reading: there the tests single out $n_{g} \equiv 0 \pmod 3$ only with no graviton and a number of doublets divisible by $6$ (one window) or $3$ (two windows), and with the graviton counted no content passes; under J3's reading the verdict is $3 \mid n_{g}$. Which reading holds, and so which fields form the sea, is not decided here, and neither test distinguishes three generations from six or nine.

## technical
The recorded recurrence test asks that the evolution of the light-ray sea over one window of Killing time be exactly the fermion grading, which needs the light-ray central charge $c$ to be a multiple of $24$; the weaker requirement, the grading up to sign or two windows giving the identity, needs a multiple of $12$. This result reads off both verdicts under two readings of the bosons. In the additive reading the null data of the vectors, the scalars and possibly the graviton are counted as real arrays of their own on top of the sixteen Weyl arrays per generation; this reading lies outside the CAR scope of (N$_{+}$) and of the window reading and is not that of the stored channel postulate J3, which reads every massless field's channels as currents of the arrays. Null data are mass-blind: a Weyl component gives one complex array for every mass matrix and an abelian vector two real fields (both stored), and a real scalar one real field for every potential, since the symplectic flux through the null plane is $\phi_{1}(k\cdot\nabla)\phi_{2} - \phi_{2}(k\cdot\nabla)\phi_{1}$ and the potential enters only the constraint; the non-abelian vector count and the integer weight of scalar data are argued. So $c = 16n_{g} + 2n_{V} + n_{s} + 2\epsilon$. The twelve gauge vectors give exactly $24$ and drop out; the recorded failure at $78$ comes from the doublet's $4$ and the graviton's $2$. With $n_{h}$ doublets, one window needs $n_{h} \equiv 2n_{g} \pmod 6$ and two windows $n_{g} + n_{h} \equiv 0 \pmod 3$; a graviton, which J3's species list includes, makes both fail always. On the two doublets of the store's linear rung field the test passes at one and four generations and fails at three; with one doublet the two-window test passes at two. At the boson-fermion balance where the stored quartic Sakharov coefficient vanishes, $c = 48n_{g}$ and the test does not see $n_{g}$. Under J3's own reading the bosons add nothing, $c = 16n_{g}$, and both tests give $3 \mid n_{g}$; the modulus $3$ comes from $24 = 8 \cdot 3$ against the power of two $16$, and the Majorana-Weyl count $8$ of the literature gives the same.

## lay
An earlier argument suggested that a timing condition on the sea of particles running along a black hole's horizon (after one cycle the sea should return to itself exactly, up to the sign that distinguishes fermions) would require the number of particle generations to be a multiple of three, provided only the matter particles form that sea. Whether the force carriers, the Higgs field and the graviton add to that sea depends on a reading the series has not settled: its own rule for these fields treats them as built from the matter sea, in which case they add nothing and the multiple-of-three answer stands. If instead they are counted as extra members of the sea, the force carriers add exactly a harmless amount, while the Higgs field and a graviton shift the answer: with one Higgs doublet the strict condition can never be met and a slightly weaker form picks two generations; with the series' two Higgs doublets it picks one or four and rules out three; with a graviton it can never be met. In no reading can the condition tell three generations from six.

## one-liner
For the one-window ($24 \mid c$) and two-window ($12 \mid c$) recurrence tests of the light-ray sea: if the null data of vectors, scalars and ($\epsilon = 1$) the graviton are counted additively, as real arrays beside the sixteen Weyl arrays per generation (a reading outside (N$_{+}$), the window reading and J3), then $c = 16n_{g} + 2n_{V} + n_{s} + 2\epsilon$, the twelve vectors drop out, the verdict is $n_{h} \equiv 2n_{g} \pmod 6$, resp. $n_{g} + n_{h} \equiv 0 \pmod 3$, and never with a graviton; under J3's reading, bosons as currents of the arrays, $c = 16n_{g}$ and the verdict is $3 \mid n_{g}$.
