---
id: synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free
kind: claim
version: 2
title: Capacity and induced-gravity readings do not fix the generation number
status: proved
region: synthesis
subject: quantum-fields
tags: [boundary-modes, mode-counting, counting-rules, undetermined-input, no-go]
proposed_by:
  kind: ai
  session: 2026-11-09-three
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-09-three
- name: Claude Fable 5.2
  role: 'clause (iv) restated: under clause (K1) of the Krein premise the gauge parameter is one, so the zeros reached by moving it are not admissible; the stored tree-level reading of the doublets'' curvature coupling recorded'
  version: 2
  source: maintainer pass of 2026-11-10
review: draft
derivations:
- name: main
  uses:
  - synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins@1
  - synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays@5
  - synthesis.array-ln2-is-zero-mode-doublet-one-tower@6
  - synthesis.slot-module-light-ray-arrays-are-weyl-components@3
  - standard-model.connection-forced@5
  - synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum@5
  - hawking.helicity-lift-joints-itemised@7
  - synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations@4
  - synthesis.krein-quartet-drops-from-the-induced-einstein-hilbert-coefficient-only-under-a-regulator-that-treats-it-alike@3
  - synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off@2
  - synthesis.slot-module-makes-the-faces-separate-composites-and-leaves-the-generation-number-free@2
  - synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_pair_currents_have_helicity_at_most_one_and_only_helicity_zero_is_canonical
- kind: check
  ref: check.py::check_capacity_inequality_passes_two_generations_on_recorded_contents
- kind: check
  ref: check.py::check_sakharov_coefficient_has_zeros_at_every_generation_number
- kind: check
  ref: check.py::check_the_pin_is_recurrence_with_asymptotic_freedom_and_the_tally_of_rules
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.slot-module-makes-the-faces-separate-composites-and-leaves-the-generation-number-free
  - synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 1 -> 2, by decisions 7 and 10 of 9 November 2026: clause (iv) now says that under clause (K1) of the Krein premise the gauge parameter is one, so the zeros of B obtained by moving the gauge parameter are arithmetic only and not admissible (the one at gauge parameter one, at three generations, is the stored cancellation), and records that at the stored tree-level reading xi_R = 0 of the rung doublets B = 16 n_g - 40 vanishes at no integer; clause (v) says that none of the eleven variants uses a moved gauge parameter, so the tally stands; the technical and lay levels, the proof of (iv), the independence paragraph and one check label follow. Clauses (i) to (iii), the conclusion and the premises are unchanged.'
  maintainer_pass:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'After acceptance (decisions of 9 November 2026): the intended citation of the spin-2 horizon-channel result is now a plain cross-reference to its stored id, and the sentences on joint J3 follow its version 3, which keeps the channel-reduction clause as premise for even-parity spin 2 only and records that its identification is not one array tower per helicity channel, so the capacity inequality is a reading and not a consequence of J3; clauses (i) to (v), premises and check unchanged.'
  open_problem: op.qft-structural-inputs
  note: >-
    Adversarial test of two leads on the generation number recorded on 9 November. Lead (a), the capacity rule: if
    every massless helicity channel on a light ray must be registered by its own array, then
    2 n_V + n_s + 2 eps <= 16 n_g, which on twelve vectors, eight rung components and a graviton reads 34 <= 16 n_g
    and gives n_g >= 3. Lead (b): the stored cancellation of the induced quadratic coefficient at three generations.
    Neither is required by the stored results cited (argued: the slot-module premise and anomaly freedom are audited through the stored independence clause, the other postulates of the cone are not), and neither fixes three. The registration rule cannot be met in the
    exact sense for any content with a vector or a graviton, because pair currents of spin-1/2 arrays have helicity
    0 or +-1 only and the helicity +-1 ones are not canonical; as bare arithmetic the inequality passes two
    generations unless the graviton is counted with both doublets (34 against a capacity of 32). The quadratic
    coefficient vanishes at three generations only at conformal coupling in the Feynman gauge with sixteen
    components and no graviton; with the curvature coupling free (an open datum of the store) it has a zero at every
    n_g from 1 to 5, the graviton's helicity states move the zero to four, and the leading (quartic) coefficient of
    the same sum vanishes on the recorded content at one generation. None of the cited results requires either coefficient
    to vanish: the stored reading of the cancellation is that the induced-gravity route supplies no Newton coupling,
    and the stored matching clause needs a positive coefficient. The only conjunction of the candidate rules that
    gives three is the recurrence test in the currents reading with asymptotic freedom of weak isospin, neither of
    which is a premise; the capacity inequality adds nothing to it. The answer three was known in advance, so the
    tally of rule variants is recorded as a look-elsewhere count, not as a probability. Status proved covers clauses (i) to (v); the independence
    paragraph and the reading are argued, and the tag no-go is meant in that sense only. The store has no graviton
    field or dynamics; the graviton occurs in J1 (kinematics) and in J3's channel-reduction clause (premise for
    even-parity spin 2 since J3 version 3). Gauge parameter and curvature coupling (10 November 2026, decisions 7
    and 10 of 9 November): for every statement about the coefficient B the gauge parameter is fixed at one by
    clause (K1) of synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields, so the zeros in the
    gauge parameter of clause (iv) are recorded as arithmetic and are not admissible; and the stored reading of
    the rung doublets' curvature coupling is the tree-level value xi_R = 0
    (synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point, clause (ii)), at which
    B = 8 on the recorded content at three generations, the zero at xi_R = 1/6 being a property of the
    attachment modules (synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations).
    The phrases "with the curvature coupling free (an open datum of the store)" above and "a bookkeeping choice"
    for the gauge parameter describe the state before those decisions; the conclusion does not depend on them. J3 with clause (iv) of synthesis.array-ln2-is-zero-mode-doublet-one-tower,
    read injectively, would be the capacity inequality with eps = 1; by decision of 9 November 2026 J3 (version 3)
    records that its identification is not injective, not one array tower per helicity channel, so the inequality
    is a reading and not a consequence of J3. See
    synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional, which derives the
    odd-parity half of the spin-2 channel clause and reaches the even-parity half in one direction (two graviton
    channels per (omega, l, m), l >= 2). Transport-absent: counting and one-loop arithmetic on the series' content.
---

## formal
Let a content have $n_{g}$ generations of sixteen Weyl components (\claimref{synthesis.slot-module-light-ray-arrays-are-weyl-components}), $n_{V}$ gauge vectors, $n_{s}$ real scalar components and $\epsilon \in \{0, 1\}$ gravitons; the recorded content has $n_{V} = 12$ (\claimref{standard-model.connection-forced}) and $n_{s} = 8$ (\claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum}), and the store holds no graviton field or dynamics: the graviton occurs in joint J1 (kinematics) and in the channel-reduction clause of joint J3, which is premise for the even-parity channels of spin $2$ (\claimref{hawking.helicity-lift-joints-itemised}; the odd-parity channels are derived in \claimref{synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional}), so $\epsilon = 1$ is the reading of J3's species list and $\epsilon = 0$ that of the stored field content. On a generator of a horizon the arrays are the $n = 16n_{g}$ chirality channels, with rotation weights $w_{\alpha} = \pm\tfrac12$ about the generator (\claimref{synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays}(iv)), and a pair current is $\rho_{q}(M)$ for a channel matrix $M$ with entries in $\mathrm{span}\{1, J\}$, as in \claimref{synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins}. The \emph{capacity rule} is the candidate requirement that every massless helicity channel on a light ray be registered by the current of an array of its own; the \emph{capacity inequality} is its arithmetic consequence $2n_{V} + n_{s} + 2\epsilon \le 16n_{g}$.
\begin{enumerate}
\item[(i)] \emph{(Helicities of pair currents; proved, a corollary of clauses (ii) and (iii) of the quasi-spin theorem; new here are the absence of helicity $\pm 2$ and the bound $n$.)} $\rho_{q}(M)$ has helicity $h$ exactly when $[W, M] = hM$, $W = \mathrm{diag}(w_{\alpha})$, and the eigenvalues of $M \mapsto [W, M]$ are the differences $w_{\alpha} - w_{\beta} \in \{-1, 0, 1\}$. So no pair current of the arrays has helicity $\pm 2$; a pair current of helicity $\pm 1$ has $M^{2} = 0$ and $[M, M^{*}] \neq 0$ and is not a canonical boson on the edge-clean vectors; the current of a single array has helicity $0$. A linearly independent (over $\mathrm{span}\{1, J\}$) family of normal channel matrices with $[M, M'^{*}] = 0$ for all pairs has at most $n$ members; a member with a definite helicity has helicity $0$, and the diagonal units attain $n$ with helicity $0$. (A member need not have a definite helicity: on two channels of weights $\tfrac12, -\tfrac12$ the normal matrix $E_{+-} + E_{-+}$ commutes with $1$ and has none.)
\item[(ii)] \emph{(The capacity rule cannot be met; proved from (i).)} In the exact sense of (i) (a canonical boson of the channel's helicity) the capacity rule holds for scalar channels only: for every $n_{g}$ it fails for a content with a gauge vector or a graviton, whose channels have helicity $\pm 1$, $\pm 2$ about the generator. Restricted to the scalars it reads $n_{s} \le 16n_{g}$ and holds at $n_{g} = 1$ for $n_{s} = 8$.
\item[(iii)] \emph{(The inequality as arithmetic; computed.)} The load $2n_{V} + n_{s} + 2\epsilon$ is $34$ for $(n_{V}, n_{s}, \epsilon) = (12, 8, 1)$, $32$ for $(12, 8, 0)$ and $30$ for $(12, 4, 1)$. So the inequality gives $n_{g} \ge 3$ only if both doublets and the graviton are counted, and $n_{g} \ge 2$ otherwise, with equality $32 = 32$ at two generations for the recorded content without a graviton.
\item[(iv)] \emph{(The quadratic coefficient; computed from the stored weights.)} In units of one minimally coupled real scalar the induced quadratic coefficient of a content with gauge parameter $\alpha$ and scalar curvature coupling $\xi_{R}$ is $B = 16n_{g} + n_{s}(1 - 6\xi_{R}) + n_{V}(\alpha - 5)$ under the heat-kernel cut-off of \claimref{synthesis.krein-quartet-drops-from-the-induced-einstein-hilbert-coefficient-only-under-a-regulator-that-treats-it-alike}(ii), (iv), and the same with $\alpha = 1$ under the energy cut-off. For $n_{V} = 12$, $n_{s} = 8$: at $\alpha = 1$ it vanishes exactly at $\xi_{R} = \tfrac16 + \tfrac{n_{g} - 3}{3}$, that is $-\tfrac12, -\tfrac16, \tfrac16, \tfrac12, \tfrac56$ for $n_{g} = 1, \dots, 5$; at $\xi_{R} = \tfrac16$ it vanishes, as arithmetic in $\alpha$, exactly at $\alpha = 5 - \tfrac43 n_{g}$, which is positive for $n_{g} = 1, 2, 3$ ($\tfrac{11}{3}$, $\tfrac73$, $1$). Under clause (K1) of Premise \claimref{synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields} the one-particle form of the polarisations is $-u\cdot w$, the form of gauge parameter one, so $\alpha = 1$ in every statement about $B$ and the zeros obtained by moving the gauge parameter are not admissible: of the three only $\alpha = 1$ at $n_{g} = 3$ remains, which is the stored cancellation. At $\alpha = 1$ and the stored tree-level reading $\xi_{R} = 0$ of the rung doublets (\claimref{synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point}(ii)), $B = 16n_{g} - 40$: $8$ at $n_{g} = 3$, and zero at no integer $n_{g}$. With fifteen components per generation it never vanishes at $\xi_{R} = \tfrac16$, $\alpha = 1$. If the graviton's two helicity states are added by the rule of \claimref{synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations}(iii), (iv) ($s^{2}$ per helicity state), the $L^{2}$ coefficient is $-(n_{V} + 4\epsilon - 4n_{g})\int_{0}^{1}xf$ and vanishes at $n_{g} = 4$ for $\epsilon = 1$. The $L^{4}$ coefficient of the same regulated sum, proportional to $2n_{V} + n_{s} - 32n_{g}$, vanishes on the recorded content exactly at $n_{g} = 1$.
\item[(v)] \emph{(The conjunctions; computed.)} With weak isospin asymptotically free ($n_{g} \le 5$, \claimref{synthesis.slot-module-makes-the-faces-separate-composites-and-leaves-the-generation-number-free}(4)): the one-window recurrence test in the currents reading ($3 \mid n_{g}$, \claimref{synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content}(vi)) gives $n_{g} = 3$ with or without the capacity inequality; the capacity inequality without the recurrence test gives $\{3, 4, 5\}$ with the graviton and $\{2, 3, 4, 5\}$ without. Of eleven variants of the candidate rules tabulated in the proof, two single out three, two more contain it and seven exclude it; every $n_{g}$ from $1$ to $5$ is selected by some variant. None of the eleven uses a zero obtained by moving the gauge parameter (the three variants of the quadratic coefficient are taken at $\alpha = 1$), so the tally is the same under (K1).
\end{enumerate}
\emph{Reading (argued).} Neither rule is required by the stored results cited here; the remaining premises of the store were not audited one by one. On the capacity rule the store has the upper bound per array: one array can register at most one helicity channel of the lift, and two helicities need two arrays (\claimref{synthesis.array-ln2-is-zero-mode-doublet-one-tower}(iv)); and joint J3 identifies every channel of every massless field, the graviton included, with a current boson of the arrays. Read injectively, onto distinct array towers, J3 with that clause would be the capacity inequality with $\epsilon = 1$; J3 states that its identification is not one array tower per helicity channel, so the inequality is a reading and not a consequence of that premise. Either way the inequality is a lower bound ($n_{g} \ge 3$ at $(12, 8, 1)$, $\{3, 4, 5\}$ with asymptotic freedom), not the value three, and by (i) the identification cannot be exact for helicity $\pm 1$, $\pm 2$ about the generator (the stored reading of the photon is a contraction over many sites). None of the cited results asks that the induced quadratic coefficient vanish: the stored reading of the cancellation is that the induced-gravity route supplies no Newton coupling, and \claimref{synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off}(iv) needs $B > 0$ for that route to give the observed coupling. With the stored independence of $n_{g}$ from the slot-module premise and anomaly freedom, these two readings do not fix the generation number (argued; it is not claimed that nothing can): the one conjunction that gives three, recurrence in the currents reading with asymptotic freedom, uses two requirements that are not premises of the store. Transport-absent.

## technical
Two leads on the number of generations are tested. The capacity lead asks that each massless helicity channel on a light ray have an array of its own, so that the boson channels (two per vector, one per scalar component, two for a graviton) cannot outnumber the sixteen arrays per generation. In the stored light-ray setting the currents of spin-$\tfrac12$ arrays have helicity $0$ or $\pm 1$ about the generator, never $\pm 2$, and only the helicity-zero ones are exact bosons, so the rule cannot be met for vectors or a graviton at any generation number; as bare arithmetic it gives three only when both doublets and the graviton are counted ($34$ against $32$). The induced-gravity lead is the vanishing of the quadratic Sakharov coefficient at three generations. That zero moves with the scalars' curvature coupling, and as arithmetic with the gauge parameter, which clause (K1) of the Krein premise fixes at one so that those zeros are not admissible; at the stored tree-level coupling of the doublets, zero, the coefficient vanishes at no generation number; the zero sits at four generations if the graviton is counted by the same helicity rule, and the leading coefficient of the same sum vanishes at one generation; none of the stored results cited requires any of these to vanish (argued; the store's other premises were not audited). The stored channel postulate J3, read as one array tower per helicity channel, would give the capacity inequality as a lower bound, three or more, not three; J3 says that it is not to be read so. The result is a no-go for both leads as derivations of three, and a table of what each variant selects.

## lay
Two numerical coincidences seemed to point at three families of matter particles. The first said the force carriers and the Higgs field need enough matter channels on a light ray to register them, and with the graviton included the count just exceeds what two families supply. The second said a certain quantum correction to the strength of gravity cancels with exactly three families. Looked at closely, neither holds up as a derivation. The registering rule cannot be satisfied in the exact sense for light or gravity whatever the number of families, and as a plain count it allows two families unless one counts the graviton and both Higgs doublets. The cancellation depends on a property of the Higgs field, its coupling to curvature, and on the collection's own tree-level value of that coupling there is no cancellation at any number of families; a bookkeeping choice for the force fields would move it too, but the collection's premise on those fields fixes that choice. Other values of the coupling and other ways of counting pick one, two or four families, and nothing found in the series' results on the matter requires the cancellation in the first place. As far as these two ideas go, the number of families remains something the series takes from observation.

## one-liner
Pair currents of the light-ray arrays have helicity $0$ or $\pm 1$, never $\pm 2$, and only helicity-zero ones are canonical, so the one-array-per-helicity-channel rule, read exactly, fails for vectors and gravitons at every $n_{g}$ and its inequality $2n_{V} + n_{s} + 2\epsilon \le 16n_{g}$ gives $n_{g} \ge 3$ only at $(12, 8, 1)$; the induced quadratic coefficient $16n_{g} + n_{s}(1 - 6\xi_{R}) + n_{V}(\alpha - 5)$ has a zero in $\xi_{R}$ at every $n_{g}$; neither rule is required by the stored results cited (argued). Under clause K1 of the Krein premise the gauge parameter is one, so zeros reached by moving it are not admissible.

