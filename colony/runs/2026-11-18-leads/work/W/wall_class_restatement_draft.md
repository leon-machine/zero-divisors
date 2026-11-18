# Draft restatement of sheaf.wall-class (version 3 -> 4), clauses (a) and (c)

Not filed: restating a conjecture is the maintainer's and Leon's decision. Grounds: the proposal
synthesis.eigenbundle-class-of-a-corank-one-wall-is-the-dying-line (if accepted, as restated in the fix round) and
the stored synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump. Clause (b) is unchanged.

Revised in the fix round to match the proposal as restated. What the proposal shows: compared across the collar,
the eigenbundle class of a wall is the dying line and carries the information of the pair (clock mismatch,
w_1(L)); two-sided completions carry its opposite on their exterior forms. What it does not show: that the pair is
natural, that it is conserved under wall induction (clause (b)), anything about the stored one-sided rung count,
or the class relative to the whole base (which can carry exterior information). So clause (c) is NOT recorded as
proved; the draft below only replaces its reference to the refuted conjecture by the statement that is conjectured
in its place, and says which part is proved.

## formal (replacement text for the clauses; the opening and closing sentences stay)
(a) its torsion part vanishes iff the wall admits a one-rung completion, a smooth symmetric form on the one-rung
bundle $T^*M \oplus \underline{\R}^2$, nondegenerate at every point of $M$, equal to $G \perp H$ outside a collar on
one side ($H$ the hyperbolic form on the added plane) and to $G$ plus a definite plane on the other, while its
coarse part, the signature jump $(1,-1)$ across the wall, whose residue is the clock mismatch $2$ of Theorem
\claimref{sheaf.conservation-degeneracy-absolute-form}, obstructs the strict two-sided completion and is nonzero on
every tame wall with two nonempty sides;

(c) it is the wall's instance of the eigenbundle class of clause (4) of Theorem
\claimref{synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump}, the class that every
completion nondegenerate at every point must carry, with the opposite sign, on the eigenbundles of its exterior
forms (transfer). This takes the place of the conservation-of-obstruction conjecture of
\cite[Conj.~7.9]{ButlerT1}, which is refuted as stated
(\claimref{transport.obstructions-are-moved-never-destroyed}). At the level of the Clifford sheaves the jump
across the wall depends on $\shL$ only through $\shL \oplus \shL$
(\claimref{synthesis.wall-rung-count-is-height-of-dying-line-class}, clause (4)), so the class refines the
sheaf-level jump.

Closing sentence, amended: "... the conjecture is that this pair, or a finer torsion-sensitive class that agrees
with it on one rung, is natural and satisfies (b) and (c). Towards (c): compared across a product collar of a
compact wall, the eigenbundles of the cometric differ by the dying line, whose rank is the signature jump and whose
isomorphism class is $w_{1}(\shL)$, and two-sided completions that are nondegenerate everywhere carry the opposite
on their exterior forms (\claimref{synthesis.eigenbundle-class-of-a-corank-one-wall-is-the-dying-line}); so
relative across the collar the class of (c) carries exactly the information of the pair $W(\Sig)$, with $w(\Sig)$
the clock mismatch. Not shown: the class relative to the whole base, naturality, and conservation under wall
induction."

## technical (clause (c))
(c) is the wall's instance of the eigenbundle class of the transfer clause, which every completion that is
nondegenerate everywhere carries with the opposite sign on its exterior forms; this replaces the reference to the
first paper's conservation conjecture, refuted as stated. Compared across the collar the class is the dying line
(proved for compact walls with a product collar); naturality and conservation remain conjectured.

## lay (last sentence)
"... carried unchanged from each wall to the next shadow wall, and to be the wall's share of the twist that every
repair of a degenerating geometry must carry, in mirror image, in what it adds. Compared across the wall the two
carry the same information; the rest is conjectured. The first paper's conservation conjecture, false as first
worded, survives in that form."

## one-liner
unchanged apart from "the clock mismatch with a torsion part" -> "the signature jump with a torsion part".
