"""Group 1: op.eigenbundle-class-of-degenerations, op.wall-class-invariant, op.kerr-ring."""
from oplib import *

C3 = 'synthesis.position-vector-eigenbundle-in-codimension-three-has-a-class-of-order-two'
BALL = 'synthesis.fixed-form-completion-over-a-ball-exists-iff-the-eigenbundle-is-stably-trivial'
WALL = 'synthesis.eigenbundle-class-of-a-corank-one-wall-is-the-dying-line'
STRICT = 'synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump'
PLANE = r'$\begin{psmallmatrix} x & y \\ y & -x\end{psmallmatrix}$'
PLANE2 = r'$\begin{psmallmatrix} x^{2} - y^{2} & 2xy \\ 2xy & y^{2} - x^{2}\end{psmallmatrix}$'


def eigenbundle(b):
    b = rep(b, '  status: open\n', '  status: reformulated\n')
    b = rep(b, "(the conjecture refuted as stated; this problem for what is still open)\"\n",
            "(the conjecture refuted as stated; this problem for what is still open); the three results on the "
            "class accepted 18 November (codimension three, sufficiency over a ball, corank-one walls) and Leon's "
            "decisions of that day (the wall-class conjecture restated around the transfer class; the periodicity "
            "theorem not imported)\"\n")
    b = set_field(b, 'statement', 'why', [
        r"Restated 18 November. For a continuous family $G$ of symmetric forms degenerating on a closed set "
        r"$\Sigma$, every completion that is nondegenerate everywhere carries on its complement, outside a "
        r"neighbourhood $U$ of $\Sigma$, the opposite of the class of the positive and negative eigenbundles of "
        r"$G$ relative to the base (" + cr(STRICT) + r", clause (4)). Three of the four questions first asked are "
        r"answered. For a degeneration confined to a ball of $\R^{m}$, a completion with a fixed exterior form "
        r"exists exactly when the positive eigenbundle is stably trivial on the bounding sphere, flat directions "
        r"being added. For the position vector in codimension three on the least module the class has order two. "
        r"Across the collar of a compact corank-one wall the class is the dying line, with exactly the "
        r"information of the stored pair $W(\Sigma)$. What is open: the class of an isolated degeneration in "
        r"codimension five and beyond, where the store cites the classical periodicity and proves nothing, and "
        r"whether the stored clock of period eight governs it; the class relative to the whole base, which can "
        r"carry information from the exterior that the comparison across a collar does not see; and whether the "
        r"two-sided number of rungs of a wall, bounded below through the transfer, equals the stored one-sided "
        r"count $k(\Sigma)$."])
    b = append_known(b,
        r"(18 November, second pass.) Three results, all proved. Codimension three (" + cr(C3) + r"): for the "
        r"position vector of $\R^{3}$ on $k$ copies of the least module of $\Cl(3,0)$ the clutching function of "
        r"the positive eigenbundle over the two-sphere is one full turn in $k$ planes, and its lift to rotors ends "
        r"at $(-1)^{k}$. For $k$ odd the eigenbundles are not stably trivial and no completion with a fixed "
        r"exterior form, with any added directions, is nondegenerate everywhere; for $k$ even the fourth "
        r"generator of $\Cl(4,0)$ repairs the family with no added direction. So in the group of stable classes "
        r"of real vector bundles over the two-sphere the class on the least module has order exactly two, and it "
        r"is a class of degree two, not seen on any circle. No characteristic class is imported: the proof lifts a "
        r"contracted loop of rotations through the stored double cover (its clause (L)). With the stored cases "
        r"this proves that the degeneration cannot be removed on the least modules for $m = 1, 2, 3$; the "
        r"residues $m \equiv 1, 2, 3, 5 \pmod 8$ beyond $m = 3$ stay cited (the periodicity theorem, from memory; "
        r"by the decision of 18 November it is not imported). Sufficiency (" + cr(BALL) + r"): for a family over "
        r"$\R^{m}$ whose degeneration set lies in an open ball, a completion with some fixed exterior form, "
        r"standard outside the ball and nondegenerate everywhere, exists if and only if the positive eigenbundle "
        r"is stably trivial on the bounding sphere (the negative one then is too). For such families the transfer "
        r"clause is an equivalence and the stable class on the sphere is the whole obstruction. The completion is "
        r"explicit and continuous, does not restrict to the family inside the ball, and uses a number of added "
        r"directions that is an upper bound, not claimed least. The added directions are needed: for " + PLANE2 +
        r" the eigenlines are trivial on every circle about the origin, no completion on the same bundle of rank "
        r"two exists, and one added direction gives one; so triviality of the eigenbundles together with those of "
        r"a given exterior form does not suffice for that form. Not treated: bases other than $\R^{m}$, "
        r"neighbourhoods that are not balls (a ring with a solid torus around it), completions that restrict to "
        r"the family inside the ball. Corank-one walls (" + cr(WALL) + r"): for a compact wall with a product "
        r"collar, corank one on the wall and signatures $(p,q)$ and $(p-1,q+1)$ on the two sides (every wall under "
        r"the hypotheses of the one-rung theorem, with the collar thin enough; the first-order clause of tameness "
        r"and smoothness are not used), the positive eigenbundle loses and the negative one gains exactly the "
        r"dying line $\mathcal L$ across the wall. Relative across the collar the class is $\mathcal L$: its rank "
        r"is the signature jump, whose residue is the clock mismatch $2$, and its isomorphism class is "
        r"$w_{1}(\mathcal L)$, so it carries exactly the information of the stored pair $W(\Sigma)$ with "
        r"$w(\Sigma)$ read as the clock mismatch, neither finer nor coarser. Every two-sided completion that is "
        r"nondegenerate everywhere, with no condition along the wall, carries the opposite on its exterior forms; "
        r"with $k$ hyperbolic planes on the physical side the far form's negative eigenbundle $N$, of rank "
        r"$k - 1$, satisfies $\overline G_{-} \oplus \mathcal L \oplus N \cong \overline G_{-} \oplus "
        r"\underline{\R}^{k}$, with $\overline G_{-}$ the negative eigenbundle of the form induced on the wall: a "
        r"necessary condition of the same form as the stored one-sided necessity clause of the rung count. That "
        r"clause concerns one-sided completions that restrict to $G$ along the wall and have no far form; neither "
        r"statement is derived from the other, and whether the two-sided count equals $k(\Sigma)$ is not decided. "
        r"On the twisted wall of the cylinder one rung, with a constant hyperbolic plane, fails and an explicit "
        r"two-rung form is nondegenerate everywhere. Not shown: the class relative to the whole base, naturality, "
        r"and conservation under wall induction. By Leon's decision of 18 November Conjecture " +
        cr('sheaf.wall-class') + r" is restated around the transfer class (its clauses (a) and (c)) and stays "
        r"conjectured. The Kerr ring (a reading computed in a working file; not stored, not refereed): in the "
        r"stored normal coordinate $w$ of the ring, with $z^{2} = w$, the plane family " + PLANE + r" in the "
        r"coordinates $(\operatorname{Re} w, \operatorname{Im} w)$ has positive eigenline $\R z$, the stored "
        r"double cover is the orientation cover of that eigenline, and the Kerr-Schild potential is linear in the "
        r"unit eigenvector, hence odd under the deck map. So the forced cover is the class of degree one of the "
        r"plane example pulled back by $w$; a punctured plane has one nontrivial double cover, so parity alone "
        r"forces that identification. The winding number three is the degree of the field strength in the ring "
        r"coordinate, and only its parity, the stored holonomy $-1$, is a class of a degenerating form (argued on "
        r"stored statements). No completion statement applies, because the Kerr cometric does not degenerate at "
        r"the ring.")
    b = set_attack_item(b, 0,
        r"Answered (18 November; " + cr(C3) + r"). The item asked for the case $m = 3$ on the least module "
        r"(dimension four): to show in the store's cell model that the positive eigenbundle of the position vector "
        r"over the two-sphere is not stably trivial (a class of degree two), or to import the statement as one "
        r"Fact. It is proved in the store's own terms, by the rotor lift of the clutching function and with no "
        r"import: the class has order two, and the family is repaired exactly on the even multiples of the least "
        r"module. What remains: codimension five and beyond ($m \equiv 1, 2, 3, 5 \pmod 8$, $m \ge 5$). In "
        r"codimension five the class is of infinite order (classical, from memory), and a proof in these terms "
        r"needs an integer invariant of a three-sphere of rotations that the store does not hold; the periodicity "
        r"theorem is not imported.",
        expect_start='The case $m = 3$')
    b = set_attack_item(b, 1,
        r"Answered (18 November; " + cr(WALL) + r"): agreement, for two-sided completions only. The item asked to "
        r"compute the relative class of the eigenbundles of a tame corank-one wall, to compare it with the pair "
        r"$(w(\Sigma), w_{1}(L))$ of Theorem " + cr('synthesis.wall-class-one-rung-obstruction') + r", and if they "
        r"agree to restate Conjecture " + cr('sheaf.wall-class') + r" around the transfer clause. Relative across "
        r"the collar the class is the dying line and carries exactly the information of the pair, with "
        r"$w(\Sigma)$ read as the clock mismatch; the conjecture is restated (Leon's decision of 18 November, "
        r"clauses (a) and (c); it stays conjectured). The transfer gives a necessary condition on two-sided "
        r"completions of the same form as the stored one-sided necessity clause, and lower bounds on the two-sided "
        r"number of rungs of the same form as the stored ones; the stored one-sided rung counts are not rederived "
        r"and no new rung count is obtained. What remains: whether the two-sided count equals the one-sided "
        r"$k(\Sigma)$; the class relative to the whole base; naturality and conservation under wall induction.",
        expect_start='Tame walls:')
    b = set_attack_item(b, 2,
        r"Closed negatively as posed (18 November; computed, not stored). The item asked whether the forced "
        r"double cover of " + cr('synthesis.kerr-ring-double-cover-data') + r" is the class of degree one found "
        r"here, and whether the winding number three is an invariant of the completion or only of the family of "
        r"rank two. The cover is the class of degree one of the plane example pulled back by the ring's normal "
        r"coordinate, an identification that parity alone forces. The winding number three is the degree of the "
        r"field strength in the ring coordinate; only its parity is a class of a degenerating form, and three is "
        r"an invariant neither of the cover nor of a completion (argued on stored statements). No completion "
        r"statement applies, since the Kerr cometric does not degenerate at the ring. There is no stored result; "
        r"what is left of the ring is with op.kerr-ring.",
        expect_start='The Kerr ring:')
    b = set_attack_item(b, 3,
        r"Answered (18 November; " + cr(BALL) + r"). The item asked: for a contractible base and an isolated "
        r"degeneration, is a completion with a fixed exterior form available whenever the class of the "
        r"eigenbundles on the surrounding sphere vanishes after adding the form's eigenspaces? Over $\R^{m}$ with "
        r"the degeneration set in a ball: yes once flat directions are added, and not in general for the given "
        r"form on the given bundle (the family whose eigenline winds twice). What remains: bases other than "
        r"$\R^{m}$, neighbourhoods that are not balls, completions that restrict to the family inside the ball, "
        r"and the least number of added directions.",
        expect_start='Sufficiency:')
    b = set_field(b, 'success', 'entities', [
        r"The class identified and computed for isolated degenerations in every codimension, with the stored "
        r"clock of period eight derived for it or shown not to govern it (done for codimension three; open from "
        r"codimension five). On tame walls the comparison across the collar is done (agreement with the stored "
        r"wall class); what would complete it is the class relative to the whole base, and the two-sided number "
        r"of rungs shown equal to the stored one-sided count or shown to differ."])
    b = add_entities(b, [C3, BALL, WALL])
    return b


def wall_class(b):
    b = rep(b, "the imported Steenrod Fact and the tameness edges, by Leon's decisions of 9 November\"\n",
            "the imported Steenrod Fact and the tameness edges, by Leon's decisions of 9 November; the "
            "eigenbundle-class result on corank-one walls accepted 18 November and Leon's decision of that day "
            "(the wall-class conjecture restated, clauses (a) and (c))\"\n")
    b = append_known(b,
        r"(18 November, second pass.) The comparison left with op.eigenbundle-class-of-degenerations is made (" +
        cr(WALL) + r", proved). What it says of tame walls: for a compact wall with a product collar under the "
        r"hypotheses of the one-rung theorem, the class of the cometric's eigenbundles relative across the collar "
        r"is the dying line, with rank the signature jump and isomorphism class $w_{1}(\mathcal L)$, exactly the "
        r"information of $W(\Sigma)$ with $w(\Sigma)$ read as the clock mismatch; every two-sided completion that "
        r"is nondegenerate everywhere, with no condition along the wall, carries the opposite on its exterior "
        r"forms; and with $k$ rungs on the physical side that gives lower bounds on the two-sided number of rungs "
        r"of the same form as the stored ones ($w_{1}(\mathcal L)^{j} = 0$ for $j \ge k$; for two rungs, "
        r"$\mathcal L \oplus \mathcal L$ trivial after adding the negative eigenbundle of the form induced on the "
        r"wall). What it does not say: anything about the one-sided count $k(\Sigma)$ asked for here (the "
        r"one-sided necessity clause, the sufficiency clauses, the twisted-rung clause and the lens-space counts "
        r"do not follow from it, and no new rung count is obtained); whether the two-sided count equals "
        r"$k(\Sigma)$; the class relative to the whole base; naturality and conservation under wall induction, "
        r"clauses (b) and (c) of the conjecture. By Leon's decision of 18 November Conjecture " +
        cr('sheaf.wall-class') + r" is restated: in clause (a) the coarse part is the signature jump $(1,-1)$, "
        r"whose residue is the clock mismatch $2$, and clause (c) refers to the eigenbundle class of the transfer "
        r"clause in place of the refuted conjecture of the first paper. It stays conjectured; the comparison "
        r"across the collar is its proved part.")
    b = add_entities(b, [WALL])
    return b


def kerr(b):
    b = append_to_attack_item(b, 0,
        r"(18 November; a reading computed in a working file, not stored and not refereed.) The same negative "
        r"reading as in op.eigenbundle-class-of-degenerations. The forced double cover is the class of degree one "
        r"of the plane family " + PLANE + r" pulled back by the ring's normal coordinate $w$: it is the "
        r"orientation cover of that family's eigenline, and the Kerr-Schild potential is linear in the unit "
        r"eigenvector. The winding number three is the degree of the field strength in the ring coordinate, and "
        r"only its parity, the stored holonomy $-1$, is a class of a degenerating form (argued on stored "
        r"statements); so three is an invariant neither of the cover nor of a completion, and no completion "
        r"statement applies, the Kerr cometric not degenerating at the ring. This does not decide the item, which "
        r"concerns the connection's limit algebra, to which the eigenbundle class does not speak. A first step: "
        r"decide whether the conjecture's ``winding number three as an invariant'' is to be restated as the "
        r"parity together with the degree of the field.",
        expect_start='Decide whether the limiting values of')
    return b


if __name__ == '__main__':
    apply([('op.eigenbundle-class-of-degenerations', eigenbundle),
           ('op.wall-class-invariant', wall_class),
           ('op.kerr-ring', kerr)])
