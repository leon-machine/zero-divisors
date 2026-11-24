---
id: synthesis.under-rp-record-weights-bound-the-chsh-sum-of-correlators-on-two-modes
kind: claim
version: 1
title: 'Under Hypothesis (RP): record weights bound the CHSH sum of correlators on two modes'
status: proved
region: synthesis
subject: clifford-structure
tags: [entanglement, measurement-and-records, finite-models]
proposed_by:
  kind: ai
  session: 2026-11-24-three-routes
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-24-three-routes
review: draft
outside_ga:
  kind: other
  why: "The elements, their products, the projectors and the functionals are computed with the Clifford product of Cl(2,2). Two steps are elementary algebra outside it: the greatest common divisor of two rational polynomials satisfied by one element, and the irrationality of the square root of 8."
derivations:
- name: main
  uses:
  - synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear@1
  - synthesis.signed-directions-and-the-integer-clifford-algebra@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_chsh_element_is_a_combination_of_four_rational_projectors_in_two_commuting_pairs
- kind: check
  ref: check.py::check_chsh_element_has_no_decomposition_into_commuting_rational_projectors
- kind: check
  ref: check.py::check_sum_of_correlators_is_the_linear_value_bounded_for_states_and_four_for_the_box
lineage:
  motivated_by:
  - synthesis.premise-positivity-of-values
  - synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate
  - synthesis.local-weights-give-the-chsh-bound-and-do-not-fix-positivity-of-values
  - one-relation.measure-indifference-borns-rule-located
extraction:
  maintainer_pass_2026_11_24_three_routes:
    by: maintainer-2026-11-24
    date: '2026-11-24'
    note: 'Maintainer edit before first acceptance, version kept at 1. After Leon''s decisions of 24 November 2026. The Reading now cites by reference the stored result on local records (its clauses (iv) to (vi): why (RP) must include projectors that are not products of local outcomes), with the sentence the note already had, and the note''s ''filed alongside'' citation is a reference; the note''s ''one party holds two modes'' is corrected to ''two or more modes'', as that result is stored. A dated sentence records Leon''s decision that (RP) stays a named hypothesis of this result, neither adopted nor rejected and written into no premise. The sentence that the extension to more modes is not carried out or checked here stays. No mathematics, link or check changed; no uses edge is added.'
  open_problem: op.positivity-of-values
  note: >-
    Conditional on Hypothesis (RP), which is a reading and not a stored premise: no assumes edge is drawn, and
    the premise of positivity of values (P) is not used (the identities needed for the bound are rederived in
    the proof so that the result does not rest on a result that assumes (P)). It answers the open problem's
    item on which projectors can label a record, on its first reading, and the question what of (P) is then
    still assumed. Kill condition registered before computing: the CHSH element at the stored settings is not a
    rational combination of rational self-adjoint projectors, or its value is not fixed by weights on
    projectors without additivity across summands that do not commute. Outcome, in two parts. The first part
    did not fire: clause (i). The second fired in its literal form: clause (ii) shows that every decomposition
    of the element into rational projectors uses projectors that do not commute, so no record has the element
    as its mean, and that the linear value is its value remains a convention or a part of (P). It did not fire
    for the quantity that a CHSH test reports, which is a sum of four correlators recorded separately: by
    clauses (iii) and (iv) that sum is bounded under (RP) with no assumption on the value of the element. What
    is new against the stored results: the core of clause (iv) is one line, (RP) gives a state by the stored
    theorem for two modes and a state gives the bound; the stored bound from local weights
    (synthesis.local-weights-give-the-chsh-bound-and-do-not-fix-positivity-of-values) assumes a linear
    functional, and here linearity is not assumed, it comes from additivity on orthogonal projectors. Separate
    content is clause (ii) and the reading of what of (P) is then a convention. That (RP) must include
    projectors that are not products of local outcomes is essential and not a matter of convenience: the
    result \claimref{synthesis.local-records-give-the-chsh-bound-without-positivity-and-reversal-on-one-party-keeps-them},
    clauses (iv) to (vi), shows that the reversal on one party of a state keeps the weights of every sequence of
    local records while it need not be a state, so weights on products of local outcomes alone do not
    separate a state from its reversal; that result obtains the bound from a weaker condition on one party's
    records, in a setting where one party holds two or more modes, which does not cover the two modes treated here.
    What is not new: clause (v) restates stored computations for comparison. Candour
    on the weight of the hypothesis: (RP) asks for non-negative weights, independent of the context, on
    projectors that are not products of local outcomes, and by the theorem for two modes that is equivalent to
    (P) on the projectors; the result trades the linearity of (P) across elements that do not commute for
    additivity on orthogonal projectors plus the reading (RP), and derives neither (P) nor (RP). More than two
    modes: by the stored theorem for every size from four,
    synthesis.additive-weights-on-the-rational-projectors-are-linear-in-every-size-from-four, an
    additive function on the projectors of any number $\ell \ge 2$ of modes is the restriction of a linear
    functional, and with non-negativity and normalisation of a state. With it the arguments of clauses (iii)
    and (iv) extend to commuting pairs of self-adjoint elements of square one with rational coefficients in
    the algebra of any number of modes (the bound then follows from the identity $C^{2} = 4 - XY$ of the
    stored certificate and positivity, in place of $C^{2} = 4 + 4K$). That extension is not carried out or
    checked here: this result is stated, proved and checked for two modes and the stored settings only, and
    no derivation here uses the theorem for larger sizes. Literature (from memory): the bound is
    Tsirelson's (B. S. Cirel'son, Lett. Math. Phys. 4 (1980) 93); the sum of four correlators is that of
    Clauser, Horne, Shimony and Holt (1969); the functional of value $4$ is the Popescu-Rohrlich box (1994);
    that additivity across observables that do not commute is an assumption and not a consequence of the
    values of commuting ones is Bell's criticism of von Neumann's argument (J. S. Bell, Rev. Mod. Phys. 38
    (1966) 447). Ledger: transport-absent (a statement about the rational matrix algebra of size four and a
    reading of records).
---

## formal
Let $\Cl_{\Q}(2,2)$ be the algebra of two modes with generators $e_{j}$, $f_{j}$, $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, and the adjoint $\dagger$ the linear extension of the inverse on blades. A \emph{projector} is a self-adjoint idempotent. Let $A_{1} = e_{1}$, $A_{2} = f_{1}e_{1}$, $B'_{1} = e_{2}f_{1}e_{1}$, $B'_{2} = f_{2}e_{2}$ (the stored settings), $T_{ij} = A_{i}B'_{j}$, $E_{ij} = \tfrac12(1 + T_{ij})$, $C = T_{11} + T_{12} + T_{21} - T_{22}$ and $K = e_{1}f_{2}$. A \emph{record weight} is a function $\mu$ from the projectors to $\Q$ with $\mu(E + E') = \mu(E) + \mu(E')$ whenever $EE' = 0$, $\mu(E) \ge 0$ and $\mu(1) = 1$. \emph{Hypothesis (RP)} (a reading of the residual postulate that weights exist and add, \claimref{one-relation.measure-indifference-borns-rule-located}; a hypothesis of this result, not a premise of the series): every projector can label a record, and the frequencies of records are a record weight; in particular the weight of a projector does not depend on the other projectors recorded with it. For a self-adjoint $T$ with $T^{2} = 1$ the \emph{correlator} is $\kappa_{\mu}(T) = \mu(\tfrac12(1 + T)) - \mu(\tfrac12(1 - T))$, and $S(\mu) = \kappa_{\mu}(T_{11}) + \kappa_{\mu}(T_{12}) + \kappa_{\mu}(T_{21}) - \kappa_{\mu}(T_{22})$.
\begin{enumerate}
\item[(i)] \emph{(The element is a combination of four projectors; computed.)} Each $T_{ij}$ is self-adjoint of square one, each $E_{ij}$ is a projector with $\langle E_{ij}\rangle_{0} = \tfrac12$, and $C = 2(E_{11} + E_{12} + E_{21} - E_{22}) - 2$. $T_{11}$ commutes with $T_{22}$ and $T_{12}$ with $T_{21}$; the other four pairs anticommute. So $C = D_{1} + D_{2}$ with $D_{1} = T_{11} - T_{22}$, $D_{2} = T_{12} + T_{21}$, each a rational combination of commuting projectors, $D_{k}^{2} = 2 + 2K$, $D_{k}^{3} = 4D_{k}$, and $D_{1}D_{2} \ne D_{2}D_{1}$.
\item[(ii)] \emph{(No decomposition into commuting projectors; proved.)} $C^{2} = 4 + 4K$, $C^{3} = 8C$, and $C$ is not a rational combination of pairwise commuting projectors. The only spectral projector of a single eigenvalue of $C$ with rational coefficients is that of its kernel, $1 - \tfrac18C^{2} = \tfrac12(1 - K)$; with its complement $\tfrac18C^{2} = \tfrac12(1 + K)$, the projector of the pair of eigenvalues $\pm 2\sqrt{2}$, these are the only spectral projectors of $C$ with rational coefficients besides $0$ and $1$.
\item[(iii)] \emph{(The sum of correlators is the linear value; proved, given the theorem for two modes; the sign is not used.)} For a function $\mu$ on the projectors that adds on orthogonal ones, let $L$ be the linear functional of \claimref{synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear}. If $x = \sum_{i}c_{i}E_{i}$ with rational $c_{i}$ and projectors $E_{i}$, commuting or not, then $\sum_{i}c_{i}\mu(E_{i}) = L(x)$: the number does not depend on the decomposition. In particular $\kappa_{\mu}(T) = L(T)$ and $S(\mu) = L(C)$.
\item[(iv)] \emph{(The bound; proved.)} For every record weight $\mu$: $S(\mu)^{2} \le 4 + 4L(K) \le 8$ and $S(\mu)^{2} \ne 8$, so $S(\mu)^{2} < 8$. The value $S = \tfrac{14}{5}$ occurs.
\item[(v)] \emph{(Without the sign on projectors that are not joint local outcomes; computed, restating stored results.)} $\lambda(x) = \langle(1 + C)x\rangle_{0}$ restricted to the projectors adds on orthogonal ones, has $\lambda(1) = 1$, takes the values $0$ and $\tfrac12$ on the sixteen joint outcomes $\tfrac12(1 \pm A_{i})\tfrac12(1 \pm B'_{j})$, has $S = 4$, and $\lambda = -\tfrac14$ on one atom.
\end{enumerate}
\emph{Reading (argued).} Under (RP) on two modes, of what the premise of positivity of values (P) asserts: (a) linearity of the weights of projectors is derived (the theorem for two modes); (b) the sign is supplied by the reading, since a frequency is not negative, and by (v) it is needed on projectors that are not among the sixteen joint outcomes of the four settings; (c) the mean of a record of an element that is a rational combination of commuting projectors is $L$ of it, by the definition of a mean; (d) for the CHSH element no record has it as its mean, by (ii), and that $L(C)$ is its value is a convention, or the part of (P) that (RP) does not give: additivity of values across the two summands $D_{1}$, $D_{2}$ that do not commute; (e) the reality clause of (P) only fixes the extension of $L$ to elements that are not self-adjoint. The quantity of a CHSH test is the sum of four correlators recorded separately, and for it (iii) and (iv) give the bound with no use of (d). So under (RP) the bound on the correlations is not assumed, and what (RP) itself assumes is stated in the note: it is close to (P) on projectors. More modes: by \claimref{synthesis.additive-weights-on-the-rational-projectors-are-linear-in-every-size-from-four} additive functions on the projectors of any number $\ell \ge 2$ of modes are restrictions of linear functionals, so the arguments of (iii) and (iv) extend to commuting pairs of self-adjoint elements of square one with rational coefficients on any number of modes; that extension is not carried out or checked here, and the clauses above are for two modes and the stored settings. That (RP) must include projectors that are not products of local outcomes is essential (argued from clauses (iv) to (vi) of Theorem \claimref{synthesis.local-records-give-the-chsh-bound-without-positivity-and-reversal-on-one-party-keeps-them}): the reversal on one party of a state keeps the weight of every sequence of local records and need not be a state, so weights on products of local outcomes alone do not separate a state from its reversal; that theorem obtains the bound from a weaker condition, on one party's records given the other's outcomes, for a party of two or more modes, which does not cover the two modes treated here. \emph{Note (24 November 2026).} By Leon's decision of that date (RP) stays a named hypothesis of this result: it is neither adopted nor rejected, it is written into no premise, and (P) stays the postulate.

## technical
The stored theorem on additive weights says that on two modes over the rationals a function on the self-adjoint idempotents that adds on orthogonal pairs is the restriction of a linear functional $L$. This result draws the consequence for the CHSH element at the stored settings and settles what the reading (RP), every rational projector can label a record with a non-negative weight that does not depend on the context, leaves of the premise (P). The element is $C = 2(E_{11} + E_{12} + E_{21} - E_{22}) - 2$ with four rational projectors of rank two, which fall into two commuting pairs; it satisfies $C^{3} = 8C$ with $C^{2} = 4 + 4K \ne 8$, so it has the eigenvalues $0$ and $\pm 2\sqrt{2}$ and cannot be written with commuting rational projectors at all. Hence no record over the rationals has $C$ as its mean, and the value of $C$ as an element is not given by weights without adding values across summands that do not commute. But the number a CHSH test reports is the sum $S$ of four correlators, each a difference of two weights of orthogonal projectors recorded in its own context, and by linearity of the weights $S = L(C)$ whatever is said about the value of $C$. With non-negative weights $L$ is a state, and $L(C)^{2} \le L(C^{2}) = 4 + 4L(K) \le 8$, with strict inequality because $S$ is rational. The identities are rederived here so that nothing rests on (P). The stored functional of value $4$ shows where the sign is needed: it is additive, normalised and non-negative on all sixteen joint outcomes of the four settings, and negative on an atom that is not among them. The stored bound from local weights assumed a linear functional; here linearity is a consequence of additivity on orthogonal projectors. The hypothesis is strong: by the theorem for two modes it is equivalent to (P) on projectors, so this is a relocation of (P) into a statement about records, not a derivation of it.

## lay
The CHSH test adds up four measured correlations, each taken in a different arrangement of the two detectors. Quantum theory says the total cannot exceed about 2.83, while other imaginable rules reach 4. In the series this limit has so far rested on an assumed premise about values. This result shows what happens if one instead reads every yes-or-no question that can be written with rational numbers as something that can be recorded, with a frequency that is never negative and does not depend on what else is recorded with it. Then the earlier theorem on two modes forces the frequencies to follow one linear rule, and the total of the four correlations is below 2.83 with nothing assumed beyond that reading. The single algebraic object that stands for the total cannot itself be recorded with rational numbers, and its value stays a matter of convention; the measured total does not need it. The reading itself is an assumption of about the same strength as the premise it replaces, stated in terms of records.

## one-liner
Under Hypothesis (RP) (a reading, not a premise: every self-adjoint idempotent of $\Cl_{\Q}(2,2)$ with rational coefficients can label a record, with non-negative weights that do not depend on the context and add on orthogonal projectors), the CHSH sum of four correlators at the stored settings equals $L(C)$ for the linear functional of the theorem on additive weights and satisfies $S^{2} < 8$, with no assumption on the value of the element $C = 2(E_{11} + E_{12} + E_{21} - E_{22}) - 2$, which is a combination of four rational projectors but of no commuting ones ($C^{3} = 8C$); that $L(C)$ is the value of $C$ itself stays a convention or part of (P), and the stored functional of value $4$ is excluded only by the sign on projectors that are not joint local outcomes.
