d='proposals/synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state/'
BASE='synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate'
P=r"\emph{Hypothesis (P), positivity of values:} values are given by a \emph{state}, a $k$-linear $\omega : \Cl_{k}(p,q) \to k$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$ and $\omega(x^{\dagger}) = \omega(x)$ for all $x$; (P) is assumed, not derived."
C2=r"The adjoint is defined by the chosen generators. In definite signature it does not depend on the orthonormal frame; in indefinite signature it depends on the split into generators of square $1$ and of square $-1$, so observables, states and (P) are relative to that split, and each statement holds for every fixed split."
e=open(d+'entity.md').read()
head=e.split('\n## formal\n',1)[0]
head=head.replace("  - synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product@1","  - tower.commuting-copies@5\n  - "+BASE+"@1")
head=head.replace("- kind: check\n  ref: check.py::check_square_eight_on_a_state_with_nonzero_anticommutator\n","")
a=head.index("  note: >-")
head=head[:a]+r'''  note: >-
    Adversarial test of whether the CHSH bound on values follows from the algebra or needs a premise about
    values. A counter-model settles it: on the integer Clifford algebra, extended $\Q$-linearly, there is a
    normalised linear functional with $\lambda(x^{\dagger}) = \lambda(x)$ that assigns a non-negative,
    no-signalling probability table to every pair of settings and has CHSH value $4$. It is the Popescu-Rohrlich
    box (S. Popescu and D. Rohrlich, Found. Phys. 24 (1994) 379; verified by the referee) written as a functional
    on the algebra. The stored CHSH result has the functional, its value $4$ and its negative value at $t = 1$
    (clause (v)); what is recorded here is where the functional is non-negative (inside each setting pair), where
    it is negative (inertia $(12, 4, 0)$, with examples), and a pair of positivity conditions that suffices for
    the bound. What is proved: the algebra and linearity do not imply the bound. That no stored premise supplies
    positivity is argued, not audited over the whole store. The stored definition of a state (an element
    $\rho = \sum x_{r}x_{r}^{\dagger}$ of unit trace) already has positivity built in, so the gap is between
    functionals and stored states, and the maintainer decision is whether (P), or "values are given by stored
    states", is adopted as a premise. Hypothesis (P) is named in the formal level; it is to become an assumes
    edge to the postulate the maintainer creates after acceptance. The statement that anticommutation of a
    party's observables holds only on the state, with its three-mode example, was first drafted here and is now
    clause (ix) of the stored CHSH result; it is not part of this result (the id keeps its original wording, as
    ids are not renamed). That maximal CHSH value fixes the observables only on the support of the state is the
    content of self-testing (Summers and Werner 1987; Popescu and Rohrlich 1992; both from memory). Kill
    condition registered before computing: the identity forcing the bound for all normalised functionals (did
    not fire). Only the twist is used of the stored commuting-copies theorem. Classical mathematics;
    transport-absent.
---
'''
body=r'''## formal
Let $k$ be $\Q$ or an ordered field, and $\Cl_{k}(2,2)$ the algebra of two modes: generators $e_{j}$, $f_{j}$ with $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, $p_{j} = f_{j}e_{j}$, the integer algebra $\Cl_{\Z}(2,2)$ of Theorem \claimref{synthesis.signed-directions-and-the-integer-clifford-algebra} inside it. As in Theorem \claimref{BASE}, $\dagger$ is the linear extension of the inverse on blades, observables are self-adjoint elements of square $1$, and $C = A_{1}(B_{1} + B_{2}) + A_{2}(B_{1} - B_{2})$ for a configuration. C2TEXT

PTEXT

(P) extends the stored definition of a state as an element $\rho = \sum_{r}x_{r}x_{r}^{\dagger}$ of unit trace from elements to functionals. Throughout, the configuration is the blade configuration $A_{1} = p_{1}$, $A_{2} = e_{1}$, $B_{1} = p_{2}$, $B_{2} = e_{2}p_{1}$ (mode $1$ against the copy of mode $2$ twisted as in Theorem \claimref{tower.commuting-copies}; integer blades, commuting across the pairs, anticommuting within), with $C^{2} = 4 + 4K$, $K = -A_{1}A_{2}B_{1}B_{2}$, by clause (iv) of Theorem \claimref{BASE}. Let $\lambda(x) = \langle(1 + C)x\rangle_{0}$, the functional of clause (v) of that theorem: integer-valued on $\Cl_{\Z}(2,2)$, extended $\Q$-linearly, with $\lambda(1) = 1$, $\lambda(x^{\dagger}) = \lambda(x)$, $\lambda(C) = 4$. The element $1 + C$ is self-adjoint of unit scalar part and is not a stored state: it is not a sum of elements $xx^{\dagger}$, by (ii).
\begin{enumerate}
\item[(i)] \emph{(The box: a probability table at every setting pair; proved.)} $\lambda(A_{i}) = \lambda(B_{j}) = 0$, $\lambda(A_{1}B_{1}) = \lambda(A_{1}B_{2}) = \lambda(A_{2}B_{1}) = 1$, $\lambda(A_{2}B_{2}) = -1$. For each setting pair $(i,j)$ and outcomes $a, b = \pm 1$ the values $\lambda\bigl(\tfrac12(1 + aA_{i})\,\tfrac12(1 + bB_{j})\bigr) = \tfrac14(1 + ab\,\lambda(A_{i}B_{j}))$ on the four idempotents (elements of the algebra over $\Q$, not of the integer algebra) are $0$ or $\tfrac12$, they sum to $1$, and each party's marginal is $\tfrac12$ whatever the other party's setting. Moreover $\lambda(xx^{\dagger}) \ge 0$ for every $x$ in the algebra generated by one setting pair $A_{i}, B_{j}$: inside one setting pair $\lambda$ is a probability measure.
\item[(ii)] \emph{(Where the box is negative; proved.)} The symmetric form $(x, y) \mapsto \lambda(xy^{\dagger})$ on the $16$-dimensional algebra has inertia $(12, 4, 0)$: it is negative definite on a subspace of dimension $4$ and no larger. $\lambda((C - t)(C - t)^{\dagger}) = t^{2} - 8t + 4$, negative exactly for $4 - 2\sqrt{3} < t < 4 + 2\sqrt{3}$ (so for $t = 1, \dots, 7$; value $-12$ at $t = 4$). Negative values occur also on elements using only two setting pairs with a shared setting: $h = A_{1}(B_{1} + B_{2})$ has $\lambda((h - 2)^{2}) = -2$. All such elements combine different setting pairs; by (i) none lies in the algebra of one setting pair.
\item[(iii)] \emph{(A sufficient pair of positivity conditions, for this blade configuration; proved.)} Let $\varphi$ be $k$-linear with $\varphi(1) = 1$. If $\varphi((C - \varphi(C))^{2}) \ge 0$ and $\varphi((1 - K)^{2}) \ge 0$, then $\varphi(C)^{2} \le \varphi(C^{2}) = 4 + 4\varphi(K) \le 8$. Both elements combine different setting pairs. $\lambda$ satisfies the second condition ($\lambda((1 - K)^{2}) = 2$) and fails the first. The two conditions are sufficient; nothing here shows they are necessary, and other sufficient sets exist. Consequence: the stored identity for $C^{2}$, which $\lambda$ satisfies as an identity of elements, together with linearity, normalisation, reality and a probability table at every setting pair, does not imply the bound; the bound follows under (P), and (P) is not implied by the algebra.
\end{enumerate}

## technical
The identity $C^{2} = 4 - [A_{1},A_{2}][B_{1},B_{2}]$ holds already in the integer Clifford algebra, but it bounds no value by itself; the bound is a statement under Hypothesis (P), positivity of values (values are given by a state, a linear $\omega$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$, $\omega(x^{\dagger}) = \omega(x)$; assumed, not derived). On $\Cl_{\Z}(2,2)$, extended $\Q$-linearly, the stored functional $\lambda(x) = \langle(1 + C)x\rangle_{0}$ is normalised, real on self-adjoint elements, assigns to every pair of settings a non-negative no-signalling probability table, and has CHSH value $4$: the Popescu-Rohrlich box as a functional on the algebra. It is non-negative on $xx^{\dagger}$ for every $x$ in the algebra of one setting pair. It is negative on $(C - t)^{2}$ for $4 - 2\sqrt{3} < t < 4 + 2\sqrt{3}$ (about $0.54 < t < 7.46$) and on other elements that combine different setting pairs, for example $(A_{1}(B_{1} + B_{2}) - 2)^{2}$ with value $-2$, never inside one setting pair; the form $\lambda(xy^{\dagger})$ has inertia $(12, 4, 0)$. For this blade configuration the bound $\varphi(C)^{2} \le 8$ follows from positivity on $(C - \varphi(C))^{2}$ and $(1 - K)^{2}$; these two conditions are sufficient and are not claimed necessary. So the bound on values rests on (P), which the algebra does not supply. The stored definition of a state as an element $\sum x_{r}x_{r}^{\dagger}$ has positivity built in, and $1 + C$ is not such an element; the gap is between functionals and stored states. The adjoint, and with it (P), is relative to the split into generators of square $1$ and $-1$. Classical mathematics throughout.

## lay
The quantum limit $2\sqrt{2}$ on correlations between two parties is often derived from an algebraic identity. This result shows that the identity is not enough. Inside the same whole-number algebra there is a rule for assigning average values that gives sensible, non-negative probabilities for every experiment the two parties can actually perform, lets neither party signal to the other, and still reaches $4$, the largest value arithmetic allows. What rules it out is an extra requirement, Hypothesis (P): that averages of squares be non-negative even for combinations of measurements that can never be performed together. That requirement is an assumption about how values are assigned (assumed, not derived), not a consequence of the algebra. The rule that reaches $4$ breaks it only on such combinations, never within a single experiment.

## one-liner
On $\Cl_{\Z}(2,2)$, extended $\Q$-linearly, the functional $\langle(1 + C)x\rangle_{0}$ gives a non-negative no-signalling probability table at every setting pair and CHSH value $4$; it is negative on $(C - t)^{2}$ for $0.54 < t < 7.46$ and on other elements that combine different setting pairs, never inside one setting pair; the bound $\varphi(C)^{2} \le 8$ follows from positivity on $(C - \varphi(C))^{2}$ and $(1 - K)^{2}$, so it holds under (P), which the algebra does not imply.
'''
body=body.replace('C2TEXT',C2).replace('PTEXT',P.replace(r"\Cl_{k}(p,q)",r"\Cl_{k}(2,2)")).replace('BASE',BASE)
open(d+'entity.md','w').write(head+'\n'+body)
proof=r'''\emph{Preliminaries.} By Theorem \claimref{synthesis.signed-directions-and-the-integer-clifford-algebra} the integer algebra is free on the blades; the adjoint, observables and (P) are those of Theorem \claimref{BASE}, whose preliminaries give $\langle x^{\dagger}\rangle_{0} = \langle x\rangle_{0}$, $\langle ab\rangle_{0} = \langle ba\rangle_{0}$, that a self-adjoint blade has square $1$, and that the scalar part of a product of two blades is zero unless they are equal up to sign. \emph{The configuration.} $p_{1} = f_{1}e_{1}$ is self-adjoint of square $1$, anticommutes with $e_{1}$, $f_{1}$ and commutes with $e_{2}$, $f_{2}$; hence $e_{2}p_{1}$ has square $e_{2}^{2}p_{1}^{2} = 1$, is self-adjoint, commutes with $e_{1}$ ($e_{1}e_{2}p_{1} = -e_{2}e_{1}p_{1} = e_{2}p_{1}e_{1}$) and with $p_{1}$, and anticommutes with $p_{2}$ as $e_{2}$ does; this is the twisted generator of Theorem \claimref{tower.commuting-copies}. So the four blades are a configuration with anticommuting pairs, and clauses (iv), (v) of Theorem \claimref{BASE} give $C^{2} = 4 + 4K$, $K^{\dagger} = K$, $K^{2} = 1$, $\langle K\rangle_{0} = 0$, and for $\lambda$: $\lambda(1) = 1$, $\lambda(x^{\dagger}) = \lambda(x)$, $\lambda(C) = 4$, $\lambda((C - t)(C - t)^{\dagger}) = t^{2} - 8t + 4$.

\emph{(i).} The four products $A_{i}B_{j}$ are, up to sign, the blades $p_{1}p_{2}$, $p_{1}e_{2}p_{1} = e_{2}$, $e_{1}p_{2}$, $e_{1}e_{2}p_{1}$: distinct, not scalars, self-adjoint of square $1$, and none equals $\pm$ an $A_{i}$, a $B_{j}$ or $K$ (the check lists them). For a blade $b$ of square $1$, $\lambda(b)$ is the coefficient of $b$ in $1 + C$: this gives the values $1, 1, 1, -1$ on the products and $0$ on the $A_{i}$, the $B_{j}$ and $K$. Expanding, $\lambda(\tfrac14(1 + aA_{i})(1 + bB_{j})) = \tfrac14(1 + ab\,\lambda(A_{i}B_{j}))$, which is $\tfrac12$ or $0$; summing over $b$ gives $\tfrac12$, independent of $j$, and likewise over $a$. \emph{One setting pair.} $A_{i}$ and $B_{j}$ are commuting self-adjoint elements of square $1$, so the algebra they generate is spanned by $1, A_{i}, B_{j}, A_{i}B_{j}$, equivalently by the four idempotents $E_{ab} = \tfrac14(1 + aA_{i})(1 + bB_{j})$, which are self-adjoint, mutually orthogonal and sum to $1$. For $x = \sum x_{ab}E_{ab}$, $xx^{\dagger} = \sum x_{ab}^{2}E_{ab}$ and $\lambda(xx^{\dagger}) = \sum x_{ab}^{2}\lambda(E_{ab}) \ge 0$.

\emph{(ii).} The Gram matrix $\lambda(e_{S}e_{T}^{\dagger})$ on the sixteen blades is a rational symmetric matrix (symmetric because $\lambda(x^{\dagger}) = \lambda(x)$); exact congruence diagonalisation gives $12$ positive, $4$ negative and no zero diagonal entries (the check), and by the law of inertia this is the largest dimension of a subspace on which the form is negative definite. The quadratic $t^{2} - 8t + 4$ has roots $4 \pm 2\sqrt{3}$. For $h = A_{1}(B_{1} + B_{2})$: $h^{\dagger} = h$, $h^{2} = (B_{1} + B_{2})^{2} = 2 + B_{1}B_{2} + B_{2}B_{1} = 2$, $\lambda(h) = 2$, so $\lambda((h - 2)^{2}) = 2 - 8 + 4 = -2$. An element $x$ with $\lambda(xx^{\dagger}) < 0$ cannot lie in the algebra of one setting pair, by (i).

\emph{(iii).} $\varphi((C - t)^{2}) = \varphi(C^{2}) - 2t\varphi(C) + t^{2}$, which at $t = \varphi(C)$ is $\varphi(C^{2}) - \varphi(C)^{2}$; so the first condition is $\varphi(C)^{2} \le \varphi(C^{2})$. $(1 - K)^{2} = 2 - 2K$, so the second gives $\varphi(K) \le 1$ and $\varphi(C^{2}) = 4 + 4\varphi(K) \le 8$. $C$ contains all four products $A_{i}B_{j}$, and $K$ is, up to sign, $A_{1}B_{1} \cdot A_{2}B_{2}$. For $\lambda$: $\lambda((1 - K)^{2}) = 2 - 2\lambda(K) = 2$, and $\lambda((C - 4)^{2}) = -12$. Since $\lambda$ is a normalised linear functional on the algebra with $\lambda(x^{\dagger}) = \lambda(x)$, satisfies every identity of elements, and has $\lambda(C)^{2} = 16 > 8$, no argument from the algebra, linearity, normalisation and reality alone gives the bound; and since a sum of elements $xx^{\dagger}$ would make $\langle(1 + C)\,\cdot\,\rangle_{0}$ non-negative on every $yy^{\dagger}$ (as $\langle xx^{\dagger}yy^{\dagger}\rangle_{0} = \langle (y^{\dagger}x)^{\dagger}(y^{\dagger}x)\rangle_{0} \ge 0$), $1 + C$ is not such a sum.
'''.replace('BASE',BASE)
open(d+'proof-main.tex','w').write(proof)
ck=open(d+'check.py').read()
a=ck.index("def check_square_eight_on_a_state_with_nonzero_anticommutator")
ck=ck[:a].rstrip()+"\n"
ck=ck.replace('    premise("synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product")','    premise("tower.commuting-copies")\n    premise("'+BASE+'")')
ck=ck.replace('''    y = GA.sub(ONE, k)
    assert lam(prod(sq, y, dagger(y, sq))) == 2
''','''    y = GA.sub(ONE, k)
    assert lam(prod(sq, y, dagger(y, sq))) == 2
    # an element using two setting pairs with a shared setting
    h = prod(sq, a[0], GA.add(b[0], b[1]))
    hm = GA.sub(h, GA.sc(F(2)))
    assert dagger(h, sq) == h and prod(sq, h, h) == GA.sc(F(2)) and lam(prod(sq, hm, dagger(hm, sq))) == -2
    # non-negative inside each setting pair: x = sum of x_ab E_ab
    for i in range(2):
        for j in range(2):
            x = GA.add(GA.sc(F(3)), GA.scal(F(-5), a[i]), GA.scal(F(2), b[j]), GA.scal(F(7), prod(sq, a[i], b[j])))
            assert lam(prod(sq, x, dagger(x, sq))) >= 0
    # inertia of the form lam(x y^dagger) on the sixteen blades
    blades = [bb for n in range(5) for bb in combinations(range(4), n)]
    gram = [[lam(prod(sq, {s: F(1)}, dagger({t: F(1)}, sq))) for t in blades] for s in blades]
    assert all(gram[i][j] == gram[j][i] for i in range(16) for j in range(16))
    assert GA.congruence_signature(gram) == (12, 4, 0)
''')
ck=ck.replace("from fractions import Fraction as F\n","from fractions import Fraction as F\nfrom itertools import combinations\n")
ck=ck.replace('''(1) the box functional <(1 + C) x>_0: value 4 on C, non-negative no-signalling probabilities at every setting
    pair, and negative on (C - t)(C - t)^dagger; positivity on C - t and 1 - K alone gives the bound 8;
(2) a configuration with C^2 = 8 on a block and A1 A2 + A2 A1 = 1 - p_3, not zero.''','''The box functional <(1 + C) x>_0: value 4 on C, non-negative no-signalling probabilities at every setting pair,
non-negative inside each setting pair, negative on (C - t)(C - t)^dagger and on (A1(B1+B2) - 2)^2, inertia
(12, 4, 0); positivity on C - t and 1 - K suffices for the bound 8.''')
open(d+'check.py','w').write(ck)
open(d+'coverage.yaml','w').write('''functions:
  check_box_functional_has_value_four_and_fails_positivity_only_across_settings:
    kind: partial
    clauses: ["(i)", "(ii)", "(iii)"]
    omits: "complete for the values of the functional, all sixteen joint probabilities with the marginals, the value on (C - t)^2 for t = 0..8, the element A1(B1+B2) - 2 and the inertia of the form on the sixteen blades; non-negativity inside a setting pair is sampled on one element per pair and is otherwise the proof's; for clause (iii) the two conditions are evaluated on the box functional and on three states, and the implication is the proof's two lines"
''')
