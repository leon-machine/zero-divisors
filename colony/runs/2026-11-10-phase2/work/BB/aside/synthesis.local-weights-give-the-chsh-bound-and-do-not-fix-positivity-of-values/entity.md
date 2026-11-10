---
id: synthesis.local-weights-give-the-chsh-bound-and-do-not-fix-positivity-of-values
kind: claim
version: 1
title: 'Local weights give the CHSH bound; they and the parity average do not give (P)'
status: proved
region: synthesis
subject: clifford-structure
tags: [entanglement, finite-models, classical-theorem, measurement-and-records]
proposed_by:
  kind: ai
  session: 2026-11-10-phase2
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase2
review: draft
derivations:
- name: main
  uses:
  - synthesis.signed-directions-and-the-integer-clifford-algebra@2
  - tower.commuting-copies@5
  - synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate@1
  - synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state@1
  - singularity.descent-parity-average@5
  - singularity.p-reduced-metric-level-reading-many@7
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_local_weights_bound_values_and_the_box_fails_them
- kind: check
  ref: check.py::check_local_values_do_not_fix_positivity
- kind: check
  ref: check.py::check_descents_mode_wise_gives_positivity_total_parity_does_not
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.premise-positivity-of-values
  - one-relation.recorded-sectors-superselected-premise
  - one-relation.measure-indifference-borns-rule-located
extraction:
  open_problem: op.positivity-of-values
  note: >-
    Adversarial test of two statements recorded with Premise (P), positivity of values
    (synthesis.premise-positivity-of-values): that positivity across settings is the part that cannot be dropped
    for the CHSH bound, and that (P) might be derived from the descent or from the record premises. Kill
    conditions registered before computing: the independence pair dies if the second functional is non-negative
    on every $xx^{\dagger}$ or differs from the first on a local product; the descent statements die if the
    mode-wise average of a non-positive functional stays non-positive or the total-parity average of the box
    becomes positive. None fired. What is proved: in the one-mode Klein-twisted realisation, non-negative
    weights at every pair of local directions already give the bound (the box functional has a negative weight
    at a pair outside its four); a one-parameter family of functionals has the same value on every product of
    local observables and satisfies (P) at exactly one parameter, so (P) is independent of the values of all
    local products, and of every premise that is a statement about those values; the mode-wise descent turns
    (P) into non-negativity of four weights, the total-parity average does not. What is argued and not proved:
    that the stored premises on recording, superselection of recorded sectors and supervenience are statements
    about recorded local values only (they are informal; no audit over the whole store was made). Scope: two
    modes, one mode per party with the twist, directions as observables; for general local algebras the
    statement that local positivity gives quantum correlations is the theorem of Barnum, Beigi, Boixo, Elliott
    and Wehner, Phys. Rev. Lett. 104 (2010) 140401 (existence checked on the web; proved there over the complex
    numbers, not checked here for the real algebras of the series), and the independent result of Acin et al.,
    Phys. Rev. Lett. 104 (2010) 140404 (from memory). That local values do not fix a state on a real algebra is
    the failure of local tomography in quantum theory over the reals (Wootters 1990; Hardy and Wootters 2012;
    both from memory). Classical mathematics placed in the series' algebra; transport-absent. The intended
    citation for the Born weights of a sharp state is the sibling result on states sharp on an atom, filed in
    the same run and not cited here because it is not yet stored.
---

## formal
Let $k$ be $\Q$ or a subfield of $\R$, and $\Cl_{k}(2,2)$ the algebra of two modes of Theorem \claimref{synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate}, clause (vii): generators $e_{j}$, $f_{j}$ with $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, $p_{j} = f_{j}e_{j}$, the adjoint $\dagger$ the linear extension of the inverse on blades, $\langle x\rangle_{0}$ the scalar part. Write
\[
X_{1} = e_{1}, \quad Z_{1} = p_{1}, \quad X_{2} = e_{2}p_{1}, \quad Z_{2} = p_{2}, \qquad U = X_{1}X_{2}, \quad V = Z_{1}Z_{2}, \quad K = e_{1}f_{2} .
\]
$X_{2}$ is the twisted generator of Theorem \claimref{tower.commuting-copies}. A \emph{direction} of party $1$ is $a = xX_{1} + zZ_{1}$ and of party $2$ is $b = x'X_{2} + z'Z_{2}$, with $x, z, x', z' \in k$, $x^{2} + z^{2} = x'^{2} + z'^{2} = 1$; directions are self-adjoint of square $1$, and those of party $1$ commute with those of party $2$. For directions $a_{1}, a_{2}, b_{1}, b_{2}$ let $C = a_{1}(b_{1} + b_{2}) + a_{2}(b_{1} - b_{2})$. The \emph{local products} are the elements of the span $L$ of the nine products $st$, $s \in \{1, X_{1}, Z_{1}\}$, $t \in \{1, X_{2}, Z_{2}\}$; $L$ contains every direction, every product $ab$ and every $C$. The \emph{weight} of the outcomes $(+,+)$ of a pair of directions is the value of $\tfrac14(1 + a)(1 + b)$; the other outcomes are the pairs $(\pm a, \pm b)$.

\emph{Hypothesis (L), non-negative local weights:} $\lambda : \Cl_{k}(2,2) \to k$ is $k$-linear with $\lambda(1) = 1$ and $\lambda\bigl(\tfrac14(1 + a)(1 + b)\bigr) \ge 0$ for every direction $a$ of party $1$ and $b$ of party $2$. (P) is Premise \claimref{synthesis.premise-positivity-of-values}. Neither is assumed here: the clauses compare them.
\begin{enumerate}
\item[(i)] \emph{((P) gives (L); proved.)} $\tfrac14(1 + a)(1 + b)$ is a self-adjoint idempotent $y = yy^{\dagger}$, so a functional satisfying (P) satisfies (L).
\item[(ii)] \emph{((L) gives the CHSH bound; proved.)} Under (L), $|\lambda(ab)| \le 1$ for all directions and $\lambda(C)^{2} \le 8$ for every $C$ built from directions; for $k = \Q$ the inequality is strict. No positivity on any other element is used, and not the reality clause.
\item[(iii)] \emph{(The box functional fails (L); proved.)} The functional $\lambda_{\mathrm{box}}(x) = \langle(1 + C_{0})x\rangle_{0}$, $C_{0}$ the element $C$ at $a_{1} = X_{1}$, $a_{2} = Z_{1}$, $b_{1} = X_{2}$, $b_{2} = Z_{2}$ (the functional of Theorem \claimref{synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state}, with value $4$ on $C_{0}$ and non-negative weights at its four pairs of settings), has $\lambda_{\mathrm{box}}(X_{1}b) = \tfrac75$ and the weight $\lambda_{\mathrm{box}}\bigl(\tfrac14(1 + X_{1})(1 - b)\bigr) = -\tfrac{1}{10}$ at the direction $b = \tfrac35X_{2} + \tfrac45Z_{2}$.
\item[(iv)] \emph{((L) and the values of all local products do not give (P); proved.)} $U$, $V$, $K$ are self-adjoint blades of square $1$, $UV = VU = -K$, and $K \notin L$. For $c \in k$ let $\lambda_{c}(x) = \langle(1 - U - V + cK)x\rangle_{0}$. Every $\lambda_{c}$ is linear with $\lambda_{c}(1) = 1$, $\lambda_{c}(x^{\dagger}) = \lambda_{c}(x)$, is even ($\lambda_{c}$ vanishes on odd elements), satisfies (L), and has on $L$ the values that do not depend on $c$: $\lambda_{c}(ab) = -(xx' + zz')$, $\lambda_{c}(a) = \lambda_{c}(b) = 0$, so every weight at a pair of directions is $\tfrac14(1 - xx' - zz')$ and every value $\lambda_{c}(C)$ is the same for all $c$. $\lambda_{c}(K) = c$. $\lambda_{c}$ satisfies (P) if and only if $c = -1$; $\lambda_{-1}(x) = 4\langle P_{s}x\rangle_{0}$ with $P_{s} = \tfrac14(1 - U)(1 - V)$ a self-adjoint idempotent with $P_{s}xP_{s} = 4\langle P_{s}x\rangle_{0}P_{s}$ for all $x$. For $c \ne -1$ a negative value occurs on a joint outcome of the commuting pair $U$, $V$: $\lambda_{c}\bigl(\tfrac14(1 + uU)(1 + vV)\bigr) = \tfrac14(1 - u - v - c\,uv)$ for $u, v = \pm 1$, which is $-\tfrac14(1 + c)$ at $(+,+)$ and $\tfrac14(1 + c)$ at $(+,-)$. So two functionals that agree on every local product, on every weight of a pair of directions and on every CHSH value of directions differ on (P); what separates them is the value of the one blade $K$, equivalently the weights of the joint outcomes of $U$ and $V$, a pair of commuting observables each of which is a product of local directions and whose joint outcome idempotents are not local products.
\item[(v)] \emph{(The two descents; proved.)} Let $E_{N}(x) = \tfrac14\sum_{g}gxg$, $g \in \{1, p_{1}, p_{2}, p_{1}p_{2}\}$, the composite of the mode-wise parity averages (Proposition \claimref{singularity.p-reduced-metric-level-reading-many}), and $E(x) = \tfrac12(x + \Gamma x\Gamma)$, $\Gamma = p_{1}p_{2}$, the total-parity average (Theorem \claimref{singularity.descent-parity-average} in its total-parity form). With $\Pi_{n} = \tfrac14(1 + n_{1}p_{1})(1 + n_{2}p_{2})$, $n_{1}, n_{2} = \pm 1$: $E_{N}(x) = \sum_{n}\Pi_{n}x\Pi_{n} = 4\sum_{n}\langle\Pi_{n}x\rangle_{0}\Pi_{n}$, so for every linear $\lambda$ with $\lambda(1) = 1$ the functional $\lambda \circ E_{N}$ is $x \mapsto 4\sum_{n}\lambda(\Pi_{n})\langle\Pi_{n}x\rangle_{0}$, and it satisfies (P) if and only if the four numbers $\lambda(\Pi_{n})$ are non-negative. $\lambda_{c} \circ E_{N}$ for every $c$ and $\lambda_{\mathrm{box}} \circ E_{N}$ are all the functional $\langle(1 - V)x\rangle_{0}$, which satisfies (P). For the total-parity average, $\lambda_{c} \circ E = \lambda_{c}$ for every $c$, and $\lambda_{\mathrm{box}} \circ E = \langle(1 + U - V)x\rangle_{0}$ has the value $-\tfrac14$ on the self-adjoint idempotent $\tfrac14(1 - U)(1 + V)$: the total-parity average of a functional that violates (P) can violate (P).
\end{enumerate}
\emph{Reading.} (P) implies (L), (L) implies the CHSH bound for directions, and neither implication reverses: the box functional satisfies neither, and $\lambda_{c}$, $c \ne -1$, satisfies (L) and not (P). In this realisation the bound therefore does not need positivity on elements that combine settings; it needs non-negative weights at every pair of local directions, not only at the four pairs of a configuration. What (P) adds to (L) is not visible in the values of local products. A premise that is a statement about recorded outcomes of local directions cannot distinguish $\lambda_{-1}$ from $\lambda_{c}$; that the stored premises on recording, on superselection of recorded sectors and on supervenience are of that kind is argued, not proved. Of the two stored readings of the descent on several modes, the mode-wise one reduces (P) to the non-negativity of the weights of the number sectors, and the total-parity one leaves (P) a separate condition.

## technical
Premise (P), positivity of values, asks that values be given by a linear functional that is non-negative on every $xx^{\dagger}$. For two parties, each with the directions of one mode of $\Cl(2,2)$ (the second mode twisted so that the parties commute), a weaker condition (L) asks only that the weights of the joint outcomes of every pair of local directions be non-negative. Three things are proved. First, (L) already gives the CHSH bound: the correlation of two directions is a bilinear form of their coordinates bounded by $1$ on unit vectors, which gives a squared CHSH value of at most $8$. The box functional of value $4$ has non-negative weights at its own four pairs of settings and a weight $-1/10$ at another rational pair, so it is excluded by (L) without (P). Second, (L) does not give (P): the functionals $\langle(1 - U - V + cK)x\rangle_{0}$, one for each number $c$, agree on every product of local directions, so on every local weight and every CHSH value, and only the one with $c = -1$ satisfies (P); the others give a negative weight to a joint outcome of the commuting products $U = X_{1}X_{2}$ and $V = Z_{1}Z_{2}$. The values of local products leave the value of the blade $K = e_{1}f_{2}$ free, and (P) fixes it. Third, the mode-wise parity average sends every one of these functionals, and the box, to the same functional, which satisfies (P) because after that average (P) is the non-negativity of the four weights of the number sectors; the total-parity average leaves the family unchanged and leaves the box functional in violation of (P). So (P) is independent of the values of all local products and is not produced by the total-parity descent; under the mode-wise descent it is the non-negativity of ordinary weights.

## lay
The series assumes that averages of measured quantities come from a rule that never gives a negative average to a quantity multiplied by its mirror image; this is assumption (P). One reason given for it was that without it two distant experimenters could be more strongly correlated than quantum theory allows. This result looks at what is really needed. If one only asks that every probability the two experimenters can obtain, for every choice of what each measures, is not negative, the quantum limit already follows, in the simplest setting of one mode each. The well-known rule that reaches the largest correlation fails this weaker request: it gives a negative probability for a choice of measurements it was not designed for. But the weaker request is not the same as (P). There is a family of rules that give exactly the same probabilities for everything the two experimenters can measure separately, and only one member of the family obeys (P); the others give a negative probability only for a joint measurement that neither experimenter can make alone. So (P) cannot be read off from separate measurements. The series' procedure of averaging over the parity of each mode makes all these rules equal and harmless; averaging only over the total parity does not.

## one-liner
In $\Cl_{k}(2,2)$ with one twisted mode per party, non-negative weights at every pair of local directions give $\lambda(C)^{2} \le 8$ without (P) and exclude the box functional (weight $-\tfrac{1}{10}$); the functionals $\langle(1 - U - V + cK)x\rangle_{0}$ agree on all local products and satisfy (P) only for $c = -1$; the mode-wise parity average reduces (P) to four non-negative weights, the total-parity average does not give it.
