---
id: synthesis.rotation-weights-of-pair-sources-fix-the-channel-weights-and-forbid-a-fermion-trace
kind: claim
version: 1
title: Rotation weights of pair sources fix the channel weights and forbid a fermion trace
status: proved
region: synthesis
subject: quantum-fields
tags: [quantum-gravity, scattering-amplitudes, recovers-known-physics]
proposed_by:
  kind: ai
  session: 2026-11-18-leads
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-18-leads
review: draft
derivations:
- name: main
  uses:
  - synthesis.gravitational-pair-production-from-the-operator-source-at-first-order@1
  - synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel@1
  - synthesis.electron-positron-to-muon-pairs-in-the-spacetime-algebra-lsz-tree-cross-section-and-one-loop-unitarity@4
  - synthesis.imported-maxwell-stress-spacetime-algebra@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_conserved_sources_split_and_rotation_invariants_are_one_line
- kind: check
  ref: check.py::check_pair_sources_have_rotation_weights_zero_one_and_two
- kind: check
  ref: check.py::check_channel_weights_follow_from_norms_and_traces
- kind: check
  ref: check.py::check_scalar_curvature_term_changes_only_the_trace_channel
lineage:
  motivated_by:
  - synthesis.gravitational-pair-production-from-the-operator-source-at-first-order
  - synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel
extraction:
  open_problem: op.graviton-rate-as-classical-field-process
  note: >-
    Filed against the item left by the rate theorem: the trace part of the fermion channel at the next
    order, which the stored remark on the trace anomaly (clause (v) of the first-order theorem) raised.
    Answer: there is none. The chiral pair's source has rotation weight one about the pair's axis and a
    trace needs weight zero, so the trace part vanishes by a selection rule and not by the tree-level form
    of the stress; and a term of the field equation built from the scalar curvature, which is the form the
    stored anomaly term takes at first order, changes only the product of the two traces. The same
    decomposition gives the nine channel weights of the rate theorem's clause (iv) from one norm and one
    trace per source, by one orthogonality relation, where that clause was computed by integration at
    sampled angles; the two routes agree, angle by angle for the fermion channels. Three things are argued
    and not proved, and are marked: that the two-quantum element of the full stress map of an interacting
    theory has the weight of the state; where a trace can first arise for vectors and mixed pairs; and the
    size of the anomaly coefficient. The literature behind them is quoted from memory and enters no proof
    step: the state-independence of the trace of the renormalised stress of a free field (R. M. Wald, 1978),
    the form of the stress trace in a gauge theory, and the numerical coefficient of the d'Alembertian of
    the scalar curvature in the trace for free fields. Transport-absent: kinematics of conserved sources
    in the spacetime algebra. Not done: the correction common to all channels from the trace-free part of
    the vacuum's response, which enters at the same order in the gravitational coupling.
---

## formal

Conventions of Theorem \claimref{synthesis.gravitational-pair-production-from-the-operator-source-at-first-order}: $\Cl(1,3)$, signature $(+,-,-,-)$; a \emph{source} at momentum $k$ is a symmetric linear map $\mathcal{T}$ of the vectors with $\mathcal{T}(k) = 0$; $\ip{\mathcal{T}_{1}}{\mathcal{T}_{2}} = \sum_{a} \mathcal{T}_{1}(e_{a}) \cdot \mathcal{T}_{2}(e^{a})$, $\tr\mathcal{T} = \sum_{a} e^{a} \cdot \mathcal{T}(e_{a})$, $B(\mathcal{T}_{1}, \mathcal{T}_{2}) = \ip{\mathcal{T}_{1}}{\mathcal{T}_{2}} - \tfrac12\tr\mathcal{T}_{1}\tr\mathcal{T}_{2}$. Fix $k$ with $Q(k) = s > 0$, let $P_{k}(a) = a - (a \cdot k)\,k/Q(k)$ be the projection onto the vectors orthogonal to $k$, and write $\mathcal{T}^{\circ} = \mathcal{T} - \tfrac13\tr\mathcal{T}\,P_{k}$. A rotor $R$ with $Rk\tilde{R} = k$ acts on sources by $(R \cdot \mathcal{T})(a) = R\,\mathcal{T}(\tilde{R}aR)\,\tilde{R}$, and a unit bivector $b$ of the space orthogonal to $k$ acts by $L_{b}\mathcal{T}(a) = b \times \mathcal{T}(a) - \mathcal{T}(b \times a)$, with $\times$ the commutator product. A source has \emph{weight zero} about $b$ if $L_{b}\mathcal{T} = 0$; a pair $(\mathcal{T}_{1}, \mathcal{T}_{2})$ has \emph{weight} $m \neq 0$ if $L_{b}\mathcal{T}_{1} = m\,\mathcal{T}_{2}$ and $L_{b}\mathcal{T}_{2} = -m\,\mathcal{T}_{1}$. For a pair of quanta of null momenta $p_{1}, p_{2}$ with $p_{1} + p_{2} = k$, $b$ is the unit bivector of the plane orthogonal to $p_{1}$ and $p_{2}$.
\begin{enumerate}
\item[(i)] \emph{(Decomposition; proved.)} The sources at $k$ form a space of dimension $6$ on which $\ip{\cdot}{\cdot}$ is positive definite; it is the orthogonal sum of the line of $P_{k}$, with $\tr P_{k} = \ip{P_{k}}{P_{k}} = 3$ and $\ip{\mathcal{T}}{P_{k}} = \tr\mathcal{T}$, and the five-dimensional space $V_{k}$ of trace-free sources. Hence
\[
B(\mathcal{T}_{1}, \mathcal{T}_{2}) \;=\; \ip{\mathcal{T}_{1}^{\circ}}{\mathcal{T}_{2}^{\circ}} - \tfrac16\,\tr\mathcal{T}_{1}\,\tr\mathcal{T}_{2} .
\]
\item[(ii)] \emph{(Orthogonality; proved.)} The rotors fixing $k$ leave no nonzero element of $V_{k}$ invariant, and their invariants in $V_{k} \otimes V_{k}$ form one line, spanned by the tensor of the pairing. Hence, for $A, A', C, C' \in V_{k}$, with $\langle\,\cdot\,\rangle_{R}$ the invariant mean over those rotors,
\[
\bigl\langle \ip{A}{R \cdot C}\,\ip{A'}{R \cdot C'} \bigr\rangle_{R} \;=\; \tfrac15\,\ip{A}{A'}\,\ip{C}{C'}, \qquad \bigl\langle \ip{A}{R \cdot C} \bigr\rangle_{R} \;=\; 0 .
\]
\item[(iii)] \emph{(Weights of the pair sources; proved, by a computation at one configuration and covariance.)} With the pair sources of clause (iii) of the stored theorem: the source of two quanta of a real scalar field with curvature coupling $\xi$ has weight zero, trace $(1 - 6\xi)s$ and $\ip{\mathcal{T}^{\circ}}{\mathcal{T}^{\circ}} = s^{2}/6$. The source of a particle and antiparticle of one massless chiral fermion has two real components $\mathcal{T}_{n}(a) = \tfrac14\bigl(j_{n}\,(a \cdot d) + d\,(a \cdot j_{n})\bigr)$, $d = p_{1} - p_{2}$, where $j_{1}, j_{2} = b \times j_{1}$ are orthogonal vectors in the plane of $b$ with $Q(j_{1}) = Q(j_{2}) = -s$ (the stored spin sum is $2\br{p_{2}wp_{1}w}_{0} = (j_{1} \cdot w)^{2} + (j_{2} \cdot w)^{2}$ for real $w$); they form a pair of weight one, are trace-free, orthogonal to each other and to $P_{k}$, and $\ip{\mathcal{T}_{1}}{\mathcal{T}_{1}} + \ip{\mathcal{T}_{2}}{\mathcal{T}_{2}} = s^{2}/4$. Of the four sources $-\tfrac12(F_{1}aF_{2} + F_{2}aF_{1})$ of two vector quanta with real transverse polarisations $\epsilon_{1}, \epsilon_{2}$ in the plane of $b$, the two combinations of weight zero vanish and the other two form a pair of weight two; all are trace-free and their norms sum to $2s^{2}$. The scalar part $\br{F_{1}F_{2}}_{0}$ is nonzero only on the weight-zero combination with equal polarisations, where the source vanishes.
\item[(iv)] \emph{(The channel weights; proved from (i) to (iii).)} For a pair of species $i$ let $N_{i}$ be the sum over its states of $\ip{\mathcal{T}^{\circ}}{\mathcal{T}^{\circ}}$, $\theta_{i}$ the sum of $(\tr\mathcal{T})^{2}$, and $\sigma_{i} = \tfrac12$ for identical quanta, $1$ otherwise. The integral over the sphere of $\sum B^{2}/s^{4}$ with these factors is
\[
W_{ij} \;=\; \sigma_{i}\sigma_{j}\,\frac{4\pi}{s^{4}}\left(\frac{N_{i}N_{j}}{5} + \frac{\theta_{i}\theta_{j}}{36}\right) \;=\; \frac{\pi}{180}\bigl(c_{i}c_{j} + 5\,\tau_{i}\tau_{j}\bigr), \qquad c_{i} = \frac{12\,\sigma_{i}N_{i}}{s^{2}}, \quad \tau_{i} = \frac{2\,\sigma_{i}\theta_{i}}{s^{2}} ,
\]
and by (iii) $c = 1, 3, 12$ and $\tau = (1 - 6\xi)^{2}, 0, 0$ for real scalars, chiral fermions and real massless vectors: clause (iv) of the stored theorem, for all nine channels, any two curvature couplings, and both relative helicities of fermion to fermion, with no angular integration.
\item[(v)] \emph{(Selection rule; proved.)} A pair of sources at $k$ of weight $m \neq 0$ about any $b$ is trace-free and orthogonal to $P_{k}$. So the source of the chiral pair has no trace part for any conserved stress map whose two-quantum element is a pair of weight one about the pair's axis, whatever its form.
\item[(vi)] \emph{(A scalar-curvature term; proved.)} A source at $k$ invariant under every rotor fixing $k$ is a multiple of $P_{k}$, and $(a \cdot k)\,k - Q(k)\,a = -Q(k)\,P_{k}(a)$ has trace $-3Q(k)$. Let the first-order field equation of clause (i) of the stored theorem carry such a term, $\mathcal{G}_{k}[h](a) + \mu\,\bigl((a \cdot k)\,k - Q(k)\,a\bigr)\,\mathcal{R}_{k}[h] = \lambda\,\mathcal{T}(a)$, with $\mathcal{R}_{k}[h]$ the first-order scalar curvature and $1 + 3\mu Q(k) \neq 0$. Its solution is, up to a displacement,
\[
h \;=\; \frac{2\lambda}{Q(k)}\Bigl[\mathcal{T}^{\circ} + \frac{\tr\mathcal{T}}{3\,(1 + 3\mu Q(k))}\bigl(P_{k} - \tfrac32\,\id\bigr)\Bigr],
\]
with scalar curvature $-\lambda\,\tr\mathcal{T}/(1 + 3\mu Q(k))$, and the interaction of two sources is $2\lambda/Q(k)$ times
\[
B_{\mu}(\mathcal{T}_{1}, \mathcal{T}_{2}) \;=\; \ip{\mathcal{T}_{1}^{\circ}}{\mathcal{T}_{2}^{\circ}} - \frac{\tr\mathcal{T}_{1}\,\tr\mathcal{T}_{2}}{6\,(1 + 3\mu Q(k))} ,
\]
equal to $B$ whenever one of the sources is trace-free. The weights become $(\pi/180)\bigl(c_{i}c_{j} + 5\tau_{i}\tau_{j}/(1 + 3\mu s)^{2}\bigr)$.
\end{enumerate}
\emph{Reading (argued).} The stored remark is that the quantum trace of the massless Dirac stress has a term proportional to the d'Alembertian of the scalar curvature, first order in the field. For free fields the trace of the renormalised stress is the same in every state (standard, quoted from memory), so it has no element between the vacuum and a pair: it is a response of the vacuum to the field, a conserved source built from the scalar curvature, hence by (vi) of the form $\mu\,((a \cdot k)k - Q(k)a)\mathcal{R}_{k}$ with $\mu$ of order $G$ times the scheme-dependent coefficient, reading the d'Alembertian as $-Q(k)$. By (vi) it changes no channel that contains a fermion or a vector pair, and it multiplies the trace term of scalars to scalars by $(1 + 3\mu s)^{-2}$, a relative change of order $s/\bar{M}_{P}^{2}$: third order in $G$ in the rate, $G^{3}T^{10}$, about $T^{2}/\bar{M}_{P}^{2} = 6 \times 10^{-8}$ at $T = 6 \times 10^{14}$ GeV times a coefficient that is small for the Standard Model's content (quoted from memory, not used). The stored rate is of order $G^{2}$ and nothing in the store uses the next order. So the correction to the chiral-fermion coefficient from the stored trace statement is zero, at the next order in $G$ as well. In an interacting theory the two-quantum element of the stress between the vacuum and a particle and antiparticle of one massless chiral species keeps weight one, because the state has helicity one about its axis; by (v) no order in couplings that keep the species massless gives the fermion channel a trace part. A trace needs a state of weight zero: scalar pairs at tree level; beyond tree level, a particle of one chiral species with the antiparticle of another of opposite chirality, through a Yukawa coupling, and vector pairs of equal helicity, through $\br{F_{1}F_{2}}_{0}$ (the stress trace of an interacting gauge theory is a multiple of the square of the field bivector, quoted from memory). At the same order $G^{3}$ the trace-free part of the vacuum's response rescales every $c_{i}c_{j}$ by one common factor; it is not a trace part and is not computed here.

## technical

Take a pair of massless quanta with total momentum $k$, $Q(k) = s > 0$. Its stress source is a symmetric map that kills $k$, so it lives on the three-dimensional space orthogonal to $k$: six components, one of them the trace (the projection $P_{k}$) and five trace-free. The bilinear of the rate theorem splits accordingly, $B = \ip{\mathcal{T}_{1}^{\circ}}{\mathcal{T}_{2}^{\circ}} - \tfrac16\tr\mathcal{T}_{1}\tr\mathcal{T}_{2}$.

Rotations about the pair's axis sort the sources by weight. A scalar pair has weight zero (norm $s^{2}/6$, trace $(1 - 6\xi)s$). A particle and antiparticle of one chiral fermion have weight one only (norm $s^{2}/4$). A vector pair has weight two only (norm $2s^{2}$): the two weight-zero combinations of polarisations carry no source at all.

Because the five trace-free components form one irreducible space under the rotations fixing $k$, the mean over rotations of a product of two pairings is one fifth of the product of the norms. That gives every channel weight at once: $W_{ij} = \sigma_{i}\sigma_{j}(4\pi/s^{4})(N_{i}N_{j}/5 + \theta_{i}\theta_{j}/36)$, which is $(\pi/180)(c_{i}c_{j} + 5\tau_{i}\tau_{j})$ with $c = 12\sigma N/s^{2} = 1, 3, 12$. The stored weights, computed there by integration at sampled angles, follow with no integration.

A trace is invariant under rotations, so a source of nonzero weight has none. The fermion pair's source is therefore trace-free by a selection rule, not by the tree-level form of its stress, and no correction that keeps the pair's weight can give it a trace.

If the field equation acquires a term built from the scalar curvature, $\mu((a \cdot k)k - Q(k)a)\mathcal{R}_{k}[h]$, only the product of traces changes: $B_{\mu} = \ip{\mathcal{T}_{1}^{\circ}}{\mathcal{T}_{2}^{\circ}} - \tr\mathcal{T}_{1}\tr\mathcal{T}_{2}/(6(1 + 3\mu Q(k)))$. The stored trace-anomaly term is of this form (argued), so it leaves the fermion and vector coefficients alone and changes the scalars' trace term at relative order $s/\bar{M}_{P}^{2}$, an order of the rate ($G^{3}T^{10}$) that the store does not use.

## lay

When two particles collide and gravity turns them into another pair, the strength of the process depends on how the pair's energy and momentum are arranged around its line of flight. This result sorts the three kinds of pair by how they turn under a rotation about that line: a pair of spinless particles does not turn, a matter particle with its antiparticle turns once, a pair of light-like force carriers turns twice. From that sorting alone the nine relative strengths of the stored production rate follow, the numbers 1, 3 and 12, with no integration over angles.

The same sorting answers a question the earlier work left open. One part of gravity's pull, the part that responds to a quantity called the trace, can only see pairs that do not turn. A matter particle with its antiparticle always turns once, so that part never sees it, however the calculation is refined. A known quantum effect that adds to the trace turns out to act only between pairs of spinless particles, and there it is smaller than anything the store uses by many orders of magnitude at the temperatures considered.

## one-liner

At a timelike momentum the conserved sources split as a trace line and five trace-free components, and pair sources have rotation weight $0$ (scalars), $1$ (a chiral fermion pair) and $2$ (vectors), so the stored channel weights $(\pi/180)(c_{i}c_{j} + 5\tau_{i}\tau_{j})$, $c = 1, 3, 12$, follow from norms $s^{2}/6$, $s^{2}/4$, $2s^{2}$ by one orthogonality relation, the fermion pair has no trace part by a selection rule, and a scalar-curvature term in the field equation, the form of the stored anomaly term (argued), changes only the scalars' trace term, by $(1 + 3\mu s)^{-2}$.
