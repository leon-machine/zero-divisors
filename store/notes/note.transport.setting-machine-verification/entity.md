---
id: note.transport.setting-machine-verification
kind: note
version: 1
title: Machine verification
status: setting
subject: zero-divisors
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
comments_on:
- transport.splitting-along-hyperbolic-plane
- transport.no-go-level-elements
- transport.totality
- transport.density
locators:
  paper: T01
  number: Setting
  section: Machine verification
  line: 1670
---

## formal
Every computational identity in this paper has been checked by computer in exact rational arithmetic. The consolidated script \texttt{verify\_T01.py} \cite{ButlerVerifyT01}, deposited alongside the series' shared exact-arithmetic library \texttt{GA.py}, runs one hundred and fifteen checks and reports each; no floating point is used anywhere except the Moore--Penrose comparisons of \S\ref{subsec:mp}, which are float and compared at machine precision, and the script exits nonzero on any failure.

The twenty-two checks inherited from the published deposit's script cover: the hyperbolic-pair and versor identities; Lemma \claimref{transport.splitting-along-hyperbolic-plane}, including over an extension carrying a degenerate direction, where the dimension count is the essential step; all three steps of the proof of Theorem \claimref{transport.no-go-level-elements} in $\Cl(2,1)$ and in $\Cl(3,2)$, the latter exercising the shear for \emph{every} $u$ in a three-dimensional $U$; the scale-robustness of Remark \claimref{note.transport.locality-robustness-obstruction}, the nilpotency data of Remark \claimref{note.transport.obstruction-parabolic}, and the partner parametrisation \eqref{eq:partners} with the simple transitivity on it; both branches of Theorem \claimref{transport.totality} and the limit paths of Lemma \claimref{transport.density} over bases of signature $(1,1)$ and $(2,1)$; Proposition \claimref{transport.swap-rescale-normal-form} with the fixed loci of Remark \claimref{note.transport.where-each-stratum-comes}, and Lemma \claimref{transport.descent-read-out-map}; and the two consistency checks of \S\ref{sec:checks}.

The eight checks of Section \ref{subsec:extension} cover: Theorem \claimref{transport.where-obstruction-lies-commuting-square}(a) on every even-dimensional $(p,q)$ with $2 \leq n \leq 6$, with Corollary \claimref{transport.which-residues-obstruct-which-way}'s two residue sets read off the grid, Corollary \claimref{transport.odd-lorentzian-dimension-exactly-one-real} in dimensions $3, 5, 7, 9, 11$, and Remark \claimref{note.transport.three-dimensions}'s three cases; Lemma \claimref{transport.even-subalgebra-one-dimensional-extension} on $(1,3)$ and $(2,0)$ with both signs of $\nu^2$; and Theorem \claimref{transport.where-obstruction-lies-commuting-square}(c), (d) on the whole grid, the repairs built from the signature tuple of the extension found to obstruct, with Proposition \claimref{transport.fusion-occurs-most-once} along the square (the centre of $\Cl(p{+}1,q{+}1)$ computed blade-wise and found trivial, so fusion occurs at most once).

The other eighty-five checks (the taxonomy, the type-N sharpenings, type C, type P, and the clock) cover: Lemmas \claimref{transport.centre} and \claimref{transport.sign} exhaustively over \emph{all} signatures with $n \leq 8$, blade-wise, following the proofs, with the type-C criterion where it applies; the taxonomy's examples and Lemma \claimref{transport.regularity-localises-zero-divisors-idempotents}; the full Rule-2 package for the three bases $\Cl(1,0)$, $\Cl(0,3)$, $\Cl(2,1)$ and \emph{both} ascents of each, the $\gamma$-independence of every check being the computational form of Theorem \claimref{transport.rule-2-ideal-fusion-sharp-form}(3); the full Rule-1 package of Theorem \claimref{transport.rule-1-morita-trivial} and Proposition \claimref{transport.pinching-kernel} over $\Cl(1,1)$ and, for its physical relevance, $\Cl(1,3) \to \Cl(2,4)$ in dimension $64$; the type-P orbit facts with both clauses of Remark \claimref{note.transport.moore-penrose-boundary-idempotent-side}; Theorem \claimref{transport.cohomological-form-no-go} instantiated in $\Cl(2,2)$, with the torsor translation of Proposition \claimref{transport.pseudo-inverse-torsor} tested modulo the left ideal $v\,\Cl(\mathbb{V}')$ by exact membership; and Lemma \claimref{transport.conformal-gram-matrix} over five signatures, confirmed by exact congruence diagonalisation against the model lift, with Example \claimref{note.transport.exotic-embedding-inertness} realised concretely over the Gaussian rationals.

A second layer of machine checking, of a different kind, is deposited alongside: \texttt{T01\_kernel.lean} \cite{ButlerKernelT01}, seventy-six theorems in Lean 4 checked against Mathlib, with no \texttt{sorry} and no axioms beyond Lean's own. The two layers prove different things and neither replaces the other. The script checks named identities in named signatures, exactly and exhaustively within the range it enumerates; the Lean file proves the quantified statements, for every associative ring, every element, every transport history, and every $(p,q)$. Where both apply, the second subsumes the first: Lemma \claimref{transport.sign}'s two expressions for $\omega^2$ are checked blade-wise for $n \leq 8$ by the script and proved for all $p,q$ in Lean, the bridge between them being the polynomial identity $n(n-1) + 2q = (p-q)(p-q-1) + 4pq$; and Proposition \claimref{transport.fusion-occurs-most-once} is confirmed on the square by the script and proved for transport histories of every length in Lean. The Lean file is not a formalisation of this paper: it contains no Clifford algebras, no quadratic forms and no signatures, and it takes as hypotheses what this paper takes from the literature, namely semisimplicity, the injectivity of a unital homomorphism out of a simple ring, and Theorem \claimref{transport.rule-1-morita-trivial}. Its header carries a concordance from each statement label used here to the theorems that carry it, and a list of what it does not cover.

## technical
pending

## lay
pending

## one-liner
pending
