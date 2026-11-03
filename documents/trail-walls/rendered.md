# Degenerate metrics and walls

**Abstract.** Geometry can degenerate: along a wall, one direction can lose its length. This trail follows what then happens to the Clifford algebra attached to each point, assuming the degeneration is tame, the mildest controlled kind.

The algebras keep the same size everywhere, so degeneration shows up in their structure rather than in a count of dimensions. On the wall the dying direction $k$ generates a square-zero ideal of the algebra.

Adjoining a hyperbolic plane coupled to the dying direction repairs the geometry on one side, the wall included. The degeneracy is not destroyed, though: it reappears at a shadow wall further away, and for a compact wall with good couplings the process repeats forever.

After the standing assumption, the walk goes from the algebra on a degenerate wall, to its repair, to what the repair reveals about the wall, and finally to the shadow walls the repair creates.

## What we assume

**Postulate 1 (Tameness).** This is the standing assumption on how a geometry is allowed to degenerate. The places where it degenerates must form a smooth closed wall, exactly one direction must lose its length at each point of the wall, and these directions must vary smoothly along it. In addition, the length must vanish at a linear rate as the wall is reached, not to higher order.

## Degenerate metrics and walls

Each step either describes the wall, repairs it, or follows the consequences of the repair.

We begin before any wall is singled out.

Gluing together the Clifford algebras of a cometric $G$ at all points gives a sheaf $\shA$ that is locally free of constant rank $2^n$, degenerate or not, with structure functions polynomial in $G$. So degeneration cannot be detected by counting dimensions; it has to show up in the structure of the algebra.

**Theorem 2 (Local freeness at constant rank).** Gluing together the Clifford algebras at all points of a space gives a smoothly varying family of algebras. This result shows that the family has the same size everywhere, even where the geometry degenerates. So degeneration cannot be detected by counting dimensions; it has to show up in the structure of the algebra instead.

*Rests on:* sheaf.blade-basis-degenerate-forms-included

This step finds that structure, for a tame corank-one degeneration: one direction losing its length, transversally, along a smooth wall $\Sig$.

At a wall point $x$ the radical line, spanned by $k$, generates a two-sided ideal with \[ J(x) = A(x)\,k, \qquad J(x)^2 = 0, \qquad \dim_\R J(x) = 2^{n-1} \] The quotient is the Clifford algebra of the induced nondegenerate form, and these ideals assemble into a sheaf supported exactly on the wall.

**Theorem 3 (The degeneration sheaf).** Where the geometry degenerates along a wall, assuming it does so in the controlled way the paper calls tame (one direction losing its length, transversally, along a smooth wall), the algebra attached to each point changes character. Away from the wall it is an ordinary Clifford algebra. On the wall, the direction that has lost its length generates a part of the algebra whose products all vanish, an infinitesimal part of exactly half the size, and removing it leaves a smaller ordinary Clifford algebra. These parts fit together smoothly along the wall into a well-behaved algebraic object living only on the wall.

*Rests on:* sheaf.blade-basis-degenerate-forms-included, sheaf.imported-classification-values, std-algebra.vector-squares, primer.commutation-rule, std-algebra.existence-uniqueness, std-algebra.radical-ideal-and-quotient, sheaf.tameness

The wall can also be approached from outside rather than examined in place.

Along a transversal with parameter $t$, rescaling the dying direction as $k \mapsto k/\sqrt{t}$ gives a nondegenerate limit form \[ \hat G = G_0|_{V_1} \perp \dot G(k,k) \] in which the dying direction re-enters with its rate of degeneration as its coefficient. Its Clifford algebra, the exceptional algebra, is canonically independent of the choices made to build it.

**Theorem 4 (The exceptional algebra: deformation to the normal cone).** Assume the wall is tame, so that at the wall one direction of the geometry loses its length at a nonzero rate. If that direction is stretched at exactly the right rate as the wall is approached, the geometry has a well-behaved, non-degenerate limit. The algebra of this limit, the exceptional algebra, depends only on the wall point and not on the choices made to build it.

*Rests on:* sheaf.blade-basis-degenerate-forms-included, sheaf.degeneration-sheaf, sheaf.tameness

The repair begins by adjoining a hyperbolic plane $(\nO, \nInf)$ and coupling it to the dying direction with constants $\mu$ and $\nu$.

On the wall the surviving directions split off, and the coupled block has Gram matrix \[ \begin{pmatrix} 0 & \nu & \mu \\ \nu & 0 & -1 \\ \mu & -1 & 0 \end{pmatrix}, \qquad \det = -2\mu\nu \] which is nondegenerate for every nonzero $\mu, \nu$. The sign of $\mu\nu$ decides the signature: $(p{+}1, q{+}1)$ when $\mu\nu > 0$, $(p, q{+}2)$ when $\mu\nu < 0$.

**Theorem 5 (The wall Gram).** On the wall, the enlarged geometry splits into two independent pieces: the ordinary directions that survive the degeneration, and a three-dimensional block made of the dying direction and the two added ones. A direct calculation shows that this block is never degenerate, whatever non-zero coupling strengths are used. The sign of the product of the two coupling constants decides how many directions of each sign the repaired geometry has.

*Rests on:* sheaf.degeneration-sheaf, std-algebra.sylvester-inertia

The block shows that the repair works on the wall; this step extends it to the whole physical side.

Assuming tameness, $p \geq 1$ on the physical side, and a trivial radical line bundle, the coupling gives an ambient form of constant signature $(p{+}1, q{+}1)$ on the whole physical side, wall included. In the physical case every fibre of the completed sheaf is \[ \Cl(2,4) \cong \Mat_4(\HH) \]

**Theorem 6 (One-sided completion).** Assume a geometry degenerates along a wall in the tame way, with at least one positive direction on the physical side and with the dying direction's line consistently orientable along the wall. Then it can be repaired on that side by adding two extra dimensions and coupling them to the direction that is dying. This result shows that the coupling can be chosen so that the enlarged geometry is non-degenerate, with the same signature everywhere on the physical side, the wall itself included. The resulting family of algebras is then uniform: in the physical case every member is the algebra of four-by-four quaternion matrices.

*Rests on:* sheaf.determinant-identity-blow-up-expansion, sheaf.local-freeness-constant-rank, sheaf.wall-gram, sheaf.tameness

Next comes what the repair does to the original degenerate algebra.

It sits inside the completed algebra unchanged, but on the wall the radical covector $k$ acquires a partner $k^*$ built from the coupling: \[ k k^* + k^* k = 1, \qquad k^2 = (k^*)^2 = 0 \] The two form a fermionic ladder pair, and this pairing exists exactly over the wall.

**Theorem 7 (Localised transport).** When the degenerate algebra is placed inside the larger completed algebra, it sits there unchanged. What changes is its surroundings: on the wall, a direction of zero length that was a dead end in the small algebra finds a partner in the large one, and together they behave like the creation and annihilation operators of a single fermion. This pairing happens only on the wall, so the fermion-like structure lives exactly where the geometry is singular.

*Rests on:* sheaf.blade-basis-degenerate-forms-included, sheaf.degeneration-sheaf, sheaf.determinant-identity-blow-up-expansion, sheaf.resolution-ideal-theoretically, sheaf.wall-gram, sheaf.one-sided-completion, std-algebra.existence-uniqueness, std-algebra.sylvester-inertia

The repair also says something about the geometry of the wall itself.

Near a tame wall the physical metric, the inverse cometric, has a canonical simple pole whose residue is the inverse of the transversality datum. That residue pairs the conormal line with the dying line twice over, \[ N^*\Sig \cong \shL^{\otimes 2} \] so the completion's partner line is a square root of the normal bundle.

**Theorem 8 (The metric's residue, and the square-root twist).** Near a degenerate wall of the well-behaved kind the series assumes (a tame wall, where the degeneration is transverse), the ordinary metric blows up like one over the distance to the wall. The coefficient of this blow-up turns out to be the inverse of the canonical rate at which the geometry degenerates. It shows that the direction across the wall is, in a precise sense, the square of the direction that dies, so the extra direction added in the repair is a square root of the direction across the wall.

*Rests on:* sheaf.invariant-form-t3, sheaf.localised-transport, sheaf.tameness

That square-root relation has a topological consequence.

A real line bundle may twist like a band with a half twist, but two twists cancel, so the square of any line bundle is untwisted. Hence \[ w_1(N^*\Sig) = 2\,w_1(\shL) = 0 \] and every tame wall is two-sided, so a physical side always exists.

**Theorem 9 (Tame walls are two-sided).** Some surfaces, like a M\"obius band, have only one side. This result shows that, if a geometry degenerates along a wall in the tame way, as the tameness hypothesis requires, the wall can never be one-sided. So it always makes sense to speak of the physical side of the wall and the other side.

*Rests on:* sheaf.imported-real-line-bundles, sheaf.metrics-residue-square-root-twist, sheaf.tameness

Having two sides matters, because the repair is one-sided.

With $\mu\nu > 0$ the ambient form degenerates again exactly where \[ F = 1 + 2\mu\nu\beta^2 s \] vanishes, a shadow wall on the far side across which the signature passes from $(p{+}1,q{+}1)$ to $(p,q{+}2)$. Reversing the sign only moves the shadow wall to the other side; it never removes it.

**Theorem 10 (Conservation of degeneracy, located).** The one-sided repair of a degenerating geometry works on one side of the wall, but the degeneracy reappears as a new shadow wall further away. This result locates that shadow wall exactly, as the zero set of an explicit function, and says how the signature changes across it. Flipping the sign of the coupling moves the shadow wall to the other side but never removes it.

*Rests on:* sheaf.determinant-identity-blow-up-expansion, sheaf.wall-gram

A shadow wall invites the same repair again.

For a compact tame wall and a gentle enough coupling, the shadow wall is just as tame as the original. Repeating the repair gives an infinite sequence of walls whose fibres ascend the Witt tower, \[ \Cl(p,q) \to \Cl(p{+}1,q{+}1) \to \Cl(p{+}2,q{+}2) \to \cdots \] one rung per wall. The degeneracy is pushed further from the physical region at every step but never destroyed.

**Theorem 11 (The infinite wall sequence).** Provided the wall is compact and each repair is done gently enough (a good coupling at every stage), repairing a degenerate wall on one side creates a new wall a little further away, and that wall can be repaired in the same way. Repeating this forever gives an infinite chain of walls, each carrying an algebra built on two more dimensions than the last. The degeneracy is never destroyed, only pushed further from the physical region at each step.

*Rests on:* sheaf.one-sided-completion, sheaf.tame-wall-induction

## Results cited, not shown

**Fact (imported) 12 (The commutation rule).** In a Clifford algebra two perpendicular directions anticommute: swapping their order flips the sign. This rule extends that to anything built from directions perpendicular to a given one. Moving the given direction past such an element flips the sign of its odd part and leaves its even part alone.

*Provenance:* Transport Lab claim primer.commutation-rule, version 2 (T00 Lem 9.1).

**Fact (imported) 13 (Blade basis, degenerate forms included).** A Clifford algebra is built from a space of directions together with a rule for multiplying lengths. This result says that the standard basis of the algebra, made from products of basis directions, still works when the rule is degenerate, so that some directions have zero length against everything, and even when the chosen directions are not perpendicular. The multiplication table depends polynomially, and so smoothly, on the rule.

*Provenance:* Transport Lab claim sheaf.blade-basis-degenerate-forms-included, version 4 (T04 Lem 2.6).

**Fact (imported) 14 (The determinant identity, and the blow-up expansion).** The enlarged geometry built around a degenerating wall has a determinant that factorises exactly into the original determinant times a simple correction factor. The correction involves a quantity that blows up as the wall is approached, like one over the vanishing eigenvalue, with opposite signs on the two sides. Knowing exactly how it blows up is what lets one control where the enlarged geometry stays non-degenerate.

*Provenance:* Transport Lab claim sheaf.determinant-identity-blow-up-expansion, version 3 (T04 Lem 4.3).

**Fact (imported) 15 (Imported: classification values).** The Clifford algebra of any non-degenerate geometry is, up to relabelling, a familiar algebra of matrices. This imported fact lists five such identifications; for example, the algebra of four-dimensional spacetime is the algebra of two-by-two matrices of quaternions. They come from the standard classification of real Clifford algebras.

*Provenance:* Transport Lab claim sheaf.imported-classification-values, version 4 (T04 Fact 2.9).

**Fact (imported) 16 (Imported: real line bundles and $w_1$).** A line bundle attaches a line to every point of a space, and it may twist like a M\"obius band. A single invariant, the first Stiefel-Whitney class, detects whether it twists. Two twists cancel, so the square of any line bundle is untwisted, and a surface inside a space has two distinct sides exactly when its normal lines do not twist.

*Provenance:* J. W. Milnor and J. D. Stasheff, Characteristic Classes, Annals of Mathematics Studies 76, Princeton University Press (1974)., \S 4.

**Fact (imported) 17 (The invariant form of (T3)).** Suppose a geometry degenerates along a smooth wall, losing exactly one direction there in a smooth way (the first two tameness conditions). That direction loses its length as one crosses the wall, and how fast it does so can be measured without arbitrary choices, giving a canonical quantity on the wall. Asking that this quantity never vanish, so that the degeneration is first order, is the same as asking that the square of the dying direction match the direction across the wall.

*Provenance:* Transport Lab claim sheaf.invariant-form-t3, version 2 (T04 Lem 2.2).

**Fact (imported) 18 (Resolution, ideal-theoretically).** On the wall, the zero-length direction generates only an infinitesimal part of the algebra, one whose products all vanish. Once the geometry is enlarged to a non-degenerate one, in any way at all, that same direction finds a partner, and together they produce the number one. So the infinitesimal turns into a genuine new dimension.

*Provenance:* Transport Lab claim sheaf.resolution-ideal-theoretically, version 4 (T04 Prop 3.4).

**Fact (imported) 19 (Tame wall induction).** Repairing a degenerate wall on one side creates a new shadow wall on the other. This result shows that, for a compact original wall that degenerates in the well-behaved (tame) way, if the repair is done gently enough, the shadow wall is just as well behaved as the original. So the same repair can be applied to it, and the process can be repeated.

*Provenance:* Transport Lab claim sheaf.tame-wall-induction, version 5 (T04 Lem 5.3).

**Fact (imported) 20 (The Clifford algebra exists and is unique).** The rule "an arrow squared is a number" can always be realised by an actual algebra, and in essentially one way only. One explicit construction lets arrows act on oriented areas and volumes by adding a direction or removing one.

*Provenance:* Transport Lab claim std-algebra.existence-uniqueness, version 1.

**Fact (imported) 21 (The radical ideal of a degenerate Clifford algebra and its quotient).** When some directions of a space have zero length and are perpendicular to everything, their algebra picks up a layer of elements that vanish when multiplied by themselves enough times. Removing that layer leaves exactly the ordinary algebra of the remaining, healthy directions, and that layer is the largest part of the algebra that both vanishes on repeated multiplication and is closed under multiplication by the whole algebra.

*Provenance:* Transport Lab claim std-algebra.radical-ideal-and-quotient, version 1.

**Fact (imported) 22 (Orthogonal bases and the law of inertia).** However you choose perpendicular unit directions in a space, you always find the same number of "space-like", "time-like" and "zero" directions. These three counts are the space's signature, and they are all there is to know about it.

*Provenance:* T. Y. Lam, Introduction to Quadratic Forms over Fields, AMS (2005)., the diagonalisation of forms and Sylvester's law of inertia (real case).

**Fact (imported) 23 (The product of two vectors).** Multiplying two arrows gives a number plus something new. The number is their ordinary dot product. The new part changes sign when the order is swapped, and turns out to be the oriented plane the two arrows span.

*Provenance:* Transport Lab claim std-algebra.vector-squares, version 1.

The thread runs from an algebra that keeps its size but changes its structure on a wall, through a repair that gives the dying direction a partner, to shadow walls the repair can push away but never remove.

Everything rests on the tameness postulate in What we assume: the degeneracy forms a smooth closed wall, exactly one direction loses its length at each of its points, these directions vary smoothly, and the length vanishes at a linear rate. The one-sided repair also needs a positive direction on the physical side and a radical line that can be oriented consistently along the wall.

The endless sequence of walls further needs a compact wall and good couplings at every stage.
