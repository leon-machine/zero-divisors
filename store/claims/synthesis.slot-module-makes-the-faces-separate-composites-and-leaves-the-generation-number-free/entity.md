---
id: synthesis.slot-module-makes-the-faces-separate-composites-and-leaves-the-generation-number-free
kind: claim
version: 2
title: 'Slot module: the faces are separate composites, generation number free'
status: proved
region: synthesis
subject: generations
tags: [face-identification, hypercharge-and-anomalies, spinor-modules, no-go]
proposed_by:
  kind: ai
  session: 2026-11-02-qft-full
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
  - synthesis.cpt-closure-forces-slot-module-and-chirality@1
  - standard-model.imported-anomaly-coefficients@1
  - synthesis.faces-of-one-slot-space-are-not-three-generations-under-one-gauge-group@2
  - families.three-identical-families-mixing-shared-slots@8
  - synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces@3
  - standard-model.gauge-algebra-minimal-massive-composite@4
  - synthesis.imported-witten-global-su2-anomaly@1
  assumes:
  - standard-model.slot-module-hypothesis@4
  - synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_degree_one_slot_space_is_the_doublet
- kind: check
  ref: check.py::check_shared_space_breaks_the_slot_module_for_one_face
- kind: check
  ref: check.py::check_separate_copies_are_anomaly_free_for_every_number
- kind: check
  ref: check.py::check_asymptotic_freedom_bounds_the_number
- kind: check
  ref: check.py::check_face_space_is_the_dual_triplet
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.faces-of-one-slot-space-are-not-three-generations-under-one-gauge-group
  - families.three-generations-faces-maximal-composite
  - families.hyp-face-identification
extraction:
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, by Leon''s decisions of 2 November 2026: an assumes edge to the slot-module hypothesis standard-model.slot-module-hypothesis@4, on which the formal statement is conditional (clauses (1) and (2) are about state spaces satisfying it); an assumes edge to the Krein premise synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@2, which clause (4) states as its hypothesis (''Under the Krein premise'', the condition of the stored running coefficients it specialises); a uses edge to the new imported Fact synthesis.imported-witten-global-su2-anomaly@1, which replaces the citation from memory in clause (3) and its proof. The check touches the slot-module hypothesis (clause (1)) and the Witten Fact (clause (3)); the Krein premise is excused in coverage. Pin of families.three-identical-families-mixing-shared-slots moved to @8 (dated note on the generation number, content unchanged). Statement unchanged; n_g free and three not derived, as before.'
  open_problem: op.qft-structural-inputs
  note: >-
    The generation count asked in two forms: derive from the slot module that the faces are three composites
    with separate slots and pair modes, or fix the number otherwise. Kill conditions registered before
    computing: a degree-one polynomial U(2)-module of odd dimension, or (G) admitting more than two slots; an
    anomaly sum depending on the number of copies other than through a per-copy zero. Neither fired. Clause (1)
    restates clause (G); clause (2) complements the stored faces theorem (its part (3)) by showing that the
    shared space fails the premise's own refutation signature even for one face; clause (3) is an independence
    result. Standard content: per-generation anomaly cancellation (3) and the asymptotic-freedom bounds (4),
    the latter the stored one-loop condition specialised. The count three is not derived. Transport-absent.
---

## formal
Let $V = F \otimes \Lambda^{\bullet}W$ be a composite's state space of the form assumed by Premise \claimref{standard-model.slot-module-hypothesis}, in the setting of Theorem \claimref{synthesis.cpt-closure-forces-slot-module-and-chirality}, with slot number $n$, pair number $k$ and $Y = (3n - 2k)/6$; the statements below hold for state spaces satisfying the premise's clauses named in them, and are conditional on the premise where they are applied to the series' composites.
\begin{enumerate}
\item \emph{(Two slots per composite; clause (G) restated.)} If $F$ is graded as in clause (a), the one-slot space $F_{1}$ is a polynomial representation of the slot mixing $U(2)$ on which $\mu I_{2}$ acts as $\mu$; the polynomial irreducible representations of degree one are the doublet alone, so $F_{1}$ is a sum of doublets, of even dimension. If moreover $F$ is generated as in (G), $F_{1}$ is the image of $\C^{2} \otimes F_{0}$ with $\dim F_{0} = 1$, so $F_{1} \cong \C^{2}$ (or $F_{1} = 0$), as the premise itself states. No action of $U(2)$ makes a three-dimensional slot space the one-slot space of a composite.
\item \emph{(The shared space is no slot module, even for one face.)} Let $S = \C^{3}$ be the slot space of the three-spinor composite, $W = \C^{3}$, and read $\Lambda^{\bullet}(S \oplus W)$ with the gauge group $S(U(2) \times U(3))$ of one face $S_{F}$ ($U(2)$ on $S_{F}$, trivial on the remaining slot $s_{o}$). If the slot number counts all three slots, the centre of $U(2)$ acts trivially on $s_{o}$, of slot number one, against (a). If it counts the face's slots only, $F_{0} = \mathrm{span}\{1, s_{o}\}$ has dimension two, against (G): every weight occurs exactly twice, $\Lambda^{\bullet}(S \oplus W) \cong \Lambda^{\bullet}(S_{F} \oplus W) \otimes \Lambda^{\bullet}(\C s_{o})$, which is the premise's own refutation signature (two copies of each species), and the half of even mode number carries the face's particle half once and its antiparticle half once, so it is vectorlike. This complements Theorem \claimref{synthesis.faces-of-one-slot-space-are-not-three-generations-under-one-gauge-group}(3), which already gives that, with shared slots, the faces are three generations only as separate composites: the shared space fails the premise even before a second face is considered, so if each generation satisfies the premise under one gauge group, the faces of Theorem \claimref{families.three-identical-families-mixing-shared-slots} are three separate composites $\Lambda^{\bullet}(\C^{2} \oplus W_{F})$, each with its own two slots and its own pair system.
\item \emph{(The number is free; standard.)} For every $n \ge 1$, if one composite satisfies the premise then $n$ separate copies satisfy every clause of it, each for itself, and their particle halves, $16n$ states, satisfy the four anomaly conditions of Fact \claimref{standard-model.imported-anomaly-coefficients} and the colour cubic condition, each sum being $n$ times its value $0$ for one copy; the number of weak doublets is $4n$, even, as Witten's global anomaly requires (Fact \claimref{synthesis.imported-witten-global-su2-anomaly}). So the number of generations is independent of the slot-module premise and of anomaly freedom.
\item \emph{(Asymptotic freedom bounds it, if required; standard.)} Under the Krein premise (\claimref{synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields}), with the coefficients of Theorem \claimref{synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces}, one copy's Dynkin sums are $2$ for $\su(2)$ and $2$ for $\su(3)$, so $b_{3} = -11 + \tfrac43 n$ and $b_{2} = -\tfrac{22}{3} + \tfrac43 n + \tfrac{n_{h}}{6}$: colour is asymptotically free exactly for $n \le 8$, and weak isospin exactly for $n \le 5$ when $n_{h} = 1$ or $2$ (the stored condition $8n_{g} + n_{h} < 44$ at these $n_{h}$). So if both non-abelian factors are to be asymptotically free, $1 \le n \le 5$; nothing in the store requires the weak factor to be.
\item \emph{(The face count; argued reading.)} Every bivector of a three-dimensional slot space is a blade, so the face planes are exactly the lines of $\Lambda^{2}S$, of dimension $3$, and $(Xa) \wedge (Xb)$ is $\det(X)X^{-\mathsf T}$ applied to $a \wedge b$ through the dual: $\Lambda^{2}S \cong S^{*} \otimes \det$ as a $GL(S)$-module, the dual triplet of the slot space twisted by the determinant; $\binom{N}{2} = N$ only for $N = 3$. \emph{Reading (argued, under a further hypothesis):} if the generation labels are taken to be the face space of the maximal composite, with the slot $\su(3)$ of the maximal hierarchy acting on them as a family symmetry, which neither the premise nor (2) implies (separate composites need no labels from the maximal composite), then the number of generations is $\dim\Lambda^{2}\C^{3} = 3$. This rests on that hypothesis and on the three-spinor bound, imported at observation level (Fact \claimref{families.imported-face-valued-bracket-quantum-numbers}); the count three is not derived.
\end{enumerate}

## technical
The slot-module hypothesis says a composite's slot states are built from one vacuum by one doublet of slot creation operators. Clause (1) restates clause (G) in representation-theoretic form: clause (a) makes the one-slot space a sum of doublets, and (G) makes it exactly one, so every composite has two slots and the three-spinor composite's three slots cannot be one composite's slot space. Clause (2) complements the stored theorem that, with shared slots, the faces are three generations under one gauge group only as separate composites (Theorem \claimref{synthesis.faces-of-one-slot-space-are-not-three-generations-under-one-gauge-group}(3)). Viewed with the gauge group of a single face, the shared space already fails the premise. Either it has a slot the centre does not count, or it has two slot vacua, which doubles every species, the premise's own refutation signature. Its chirality half is one generation together with its conjugate, a vectorlike pair. The number of separate composites is fixed neither by the premise nor by anomaly cancellation, which holds copy by copy for any number (standard per-generation cancellation). If both non-abelian factors are to be asymptotically free, the stored one-loop condition allows one to five (standard). On the data side, the stored count of light neutrino species from the $Z$ resonance (Fact \claimref{synthesis.imported-two-doublet-scalon-sum-rule-and-lep-neutrino-count}) bounds light neutrinos, not generations. Three appears only in a reading: the face space of three slots has dimension three and is the dual triplet of the slot space twisted by the determinant. Taking it as the generation label space, with the slot $\su(3)$ acting on the labels, is a further family-symmetry hypothesis, and the three-spinor bound that supplies three slots is imported at observation level.

## lay
The framework's account of a particle family builds it from two internal ingredients called slots. Its standing assumption about how a family's states are organised already allows exactly two slots per particle, never three. This result shows that the old idea of the three families as the three pairs chosen from one three-slot object fails that assumption even when only one pair is looked at. In the shared space every particle would appear twice, and the left-right asymmetry of the weak force would cancel out. This adds to an earlier result that the families must be three separate objects. The same assumption, and the requirement that the theory be free of anomalies, are satisfied by any number of separate families, which is standard. If the strengths of both nuclear-type forces are to weaken at high energy, at most five families are allowed. That there are three is not derived: it is only a reading that rests on a separate, observation-level bound that the largest object has three slots, which can be paired in three ways.

## one-liner
The slot-module premise gives every composite two slots (clause (G) restated); the shared three-slot space of the faces fails it even for one face (two slot vacua, a vectorlike half), complementing the stored separate-composites result. The premise and anomaly freedom hold for any number of composites, and asymptotic freedom, if required, allows at most five (both standard). Three is only an argued reading on the imported observation-level three-spinor bound, whose face space is the dual triplet.
