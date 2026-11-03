---
id: synthesis.slot-count-not-from-constituent-fock-space
kind: claim
version: 1
title: The slot count of Hypothesis (S) is not an SL(4)-equivariant constituent count, whatever the statistics
status: proved
region: synthesis
subject: standard-model
tags: [hypotheses-s-r-c, no-go, mode-counting, conformal-spinors]
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
review: draft
derivations:
- name: main
  uses:
  - field-theory.twistor-attachment@6
  - rungs.two-twistor-bivector-null-invites-one@4
  - standard-model.under-s-composites-state-space-spinor@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_slot_count_not_from_constituent_fock_space
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.hyp-s-slot-statistics
extraction:
  open_problem: op.hypothesis-s
  note: 'Bears on the count half of Hypothesis (S), not on its statistics. Second quantisation over the twistor attachment, with K slot labels and an internal conformal spinor, gives a Fock space over C^K (x) CS, in which every constituent carries its own copy of the twistor label; (S) instead has one pair system per composite. The theorem shows the two cannot be matched equivariantly for the twistor group SL(4) when K is even, for any statistics (fermionic, bosonic, or any Fock-type space generated from an invariant vacuum by equivariant creation operators, parafermions included); the unmatched sectors are exactly the SU(2)-singlet species. Under the gauge group U(2) x U(3) alone the obstruction disappears, since the central element -1 of SL(4) is not a gauge transformation (for K = 2 fermions with CS restricted to U(3) as Lambda^0 W + Lambda^2 W, the d^c-type component of the two-slot sector does occur in Lambda^2(C^2 (x) CS)). Clause (3) records that the parity argument is needed: for K = 3 the bosonic Fock space does contain a singlet copy of the dual twistor. The shape (S) needs, slot Fock space tensor one pair Fock space on which the slot group acts trivially, is the shape of the tower module, ground module tensor rung module (standard-model.imported-tower-commuting-copies-fock-module), which favours the T12 outcome that restates (S) as a hypothesis about the transport tower (slots as rung modes) over any derivation from constituents; that is a reading, argued, not part of the theorem. General K for the fermionic case in clause (3) uses skew Howe duality for GL(K) x GL(4) on the exterior algebra of C^K (x) C^4 (R. Howe, Remarks on classical invariant theory, Trans. AMS 313 (1989) 539, cited from memory); only K = 3, 4 are computed. Transport-absent as a statement about representations; its bearing is on which T12 outcome survives.'
---

## formal
Let $\CS = \Lambda^{\mathrm{even}}W$ be the conformal spinor space as a module of $\mathrm{Spin}(6) \cong SL(4)$ (complexified), $\CSm = \Lambda^{\mathrm{odd}}W$ its dual, and let $U$ be $\CS$, $\CSm$ or $\CS \oplus \CSm$. For $K \ge 1$ let $F$ be a Fock-type space over the one-particle space $\C^{K} \otimes U$ (slot label times internal twistor label): a representation of $SL(K) \times SL(4)$ spanned by vectors $a^{\dagger}(u_{1})\cdots a^{\dagger}(u_{n})\Omega$, $u_{r} \in \C^{K} \otimes U$, with $\Omega$ invariant and $a^{\dagger}$ linear and equivariant (the exterior and symmetric algebras, and parastatistics Fock spaces, are examples). Let $\mathcal{S} = \Lambda^{\bullet}(\C^{2} \oplus W)$ be the state space of Hypothesis (S), with $SL(2)$ acting on the slot modes and $SL(4)$ on $\Lambda^{\bullet}W$, and $\mathcal{S}_{j} = \Lambda^{j}\C^{2} \otimes \Lambda^{\bullet}W$ its slot-number sectors.
\begin{enumerate}
\item \emph{(Even slot number.)} If $K$ is even, $F$ has no nonzero $SL(K)$-invariant vector in an $SL(4)$-isotypic component of type $\CS$ or $\CSm$.
\item \emph{(The (S) sectors that cannot be matched.)} In $\mathcal{S}$ the sectors $\mathcal{S}_{0}$ and $\mathcal{S}_{2}$ are $SL(2)$-invariant and each is $\CS \oplus \CSm$ under $SL(4)$; they hold the singlet species $\nu^{c}, u^{c}$ ($j = 0$) and $e^{c}, d^{c}$ ($j = 2$) of Theorem \claimref{standard-model.under-s-composites-state-space-spinor} and their conjugates. Hence for $K = 2$ every $SL(2) \times SL(4)$-equivariant linear map $\mathcal{S} \to F$ vanishes on $\mathcal{S}_{0} \oplus \mathcal{S}_{2}$, every equivariant map $F \to \mathcal{S}$ has image in $\mathcal{S}_{1}$, and $\mathcal{S}$ is not an $SL(2) \times SL(4)$-equivariant subquotient of any such $F$, whatever the statistics. Equivariance for the twistor group $SL(4)$ is needed: under the gauge group $U(2) \times U(3)$ alone the obstruction disappears, the central element $-1 \in SL(4)$ not being a gauge transformation.
\item \emph{(Odd $K$ is different.)} For $K = 3$ and $U = \CS$: the exterior algebra has no $SL(3)$-singlet copy of $\CS$ or $\CSm$ (computed, all degrees), while the symmetric algebra contains exactly one copy of $\det \otimes \CSm$ in degree three and none of $\CS$ in degree nine (computed). For $K = 4$ there is none in either algebra.
\end{enumerate}

## technical
Second quantising composites over the twistor attachment, with a label for each slot and the twistor as internal label, puts one copy of the twistor label on every constituent. Hypothesis (S) instead puts one pair system on the whole composite, beside the slot modes, so that a state with no slot occupied, or with both, still carries a full twistor or dual twistor. Central elements decide the matter: in any Fock-type space built from creation operators carrying a slot index and a twistor index, $-1$ in the slot group and $-1$ in the twistor group act by the same sign $(-1)^{n}$ on $n$-particle states. For an even number of slots an invariant of the slot group therefore has even particle number and is fixed by $-1$ in the twistor group, which acts as $-1$ on twistors and dual twistors. In the space of (S) the slot-invariant sectors, no slot or both slots occupied, are twistors and dual twistors, and they hold exactly the four singlet species $\nu^{c}$, $u^{c}$, $e^{c}$, $d^{c}$. So the count of (S) cannot come from constituents by any construction that respects the twistor group $SL(4)$, with any statistics; only the doublet sector can be matched. Under the gauge group $U(2) \times U(3)$ alone the obstruction disappears: the central element $-1 \in SL(4)$ is not a gauge transformation. The argument needs the even count: three bosonic constituents do produce one invariant dual twistor, their antisymmetrised product.

## lay
The series' Hypothesis (S) says a composite particle has two places for its twistors plus one shared set of three internal modes. A natural way to derive such a space is to treat each twistor as a particle and build the many-particle space, each particle carrying its own internal label. This result shows that route cannot work for two twistors, whatever rule for identical particles one uses: a sign coming from the twistor symmetry, which both descriptions must agree on if the twistor symmetry is to be respected, comes out differently, and the states that disagree are exactly the four kinds of particle with no weak charge (the right-handed neutrino, up quark, electron and down quark). The shared internal modes must come from something attached to the composite as a whole.

## one-liner
For an even number $K$ of slot labels and maps equivariant for the twistor group $SL(4)$, no Fock-type space over $\C^{K} \otimes U$ ($U = \CS$, $\CSm$ or both, any statistics) holds a slot-invariant twistor or dual twistor, while the (S) space holds them in its no-slot and two-slot sectors ($\nu^{c}, u^{c}, e^{c}, d^{c}$), so the (S) count is not an $SL(4)$-equivariant constituent count; under $U(2) \times U(3)$ alone the obstruction disappears, and for $K = 3$ bosons it fails, with one invariant dual twistor.
