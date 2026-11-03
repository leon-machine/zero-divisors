---
id: note.correspondence.setting-machine-verification
kind: note
version: 2
title: Machine verification
status: setting
subject: conformal-spacetime
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
comments_on:
- correspondence.fock-model-complexified-ascended-algebra
- correspondence.clifford-side-ordering-shift
- correspondence.chevalley-pairing
- correspondence.spinor-identification
locators:
  paper: T09
  number: Setting
  section: Machine verification
  line: 892
extraction:
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
---

## formal
Every computational identity asserted in this paper is verified by the deposited script \texttt{verify\_T09.py} \cite{ButlerVerifyT9}, which imports the series' shared exact-arithmetic library \texttt{GA.py} and runs entirely in exact arithmetic over the Gaussian rationals $\mathbb{Q}(i)$: no floating point appears anywhere, so every check is an identity, not an approximation. The script works with $C(v) = c(v)/\sqrt2$ (Section \ref{sec:setting}), so that $\{C(u), C(v)\} = \ip{u}{v}$ and $C(u)^2 = Q(u)/2$, and with the isotropic basis of Theorem \claimref{correspondence.fock-model-complexified-ascended-algebra}, which is Gaussian rational. Sixty-nine checks pass. Three reusable routines developed for this paper were promoted into \texttt{GA.py} per the series' practice, append-only and backward compatibly: an exact Gaussian-rational field class, generic-field linear algebra (rank, solve) usable over any exact field, and a kernel routine over any exact field.

The coverage, by section. \emph{The Fock model} (Theorem \claimref{correspondence.fock-model-complexified-ascended-algebra}): the CAR relations of the three wedge and contraction pairs $w_j\wedge$, $\iota_{w_j'}$ (Proposition \claimref{correspondence.clifford-side-ordering-shift}, there written $A_1$, $B_1$) and all anticommutators on the full state basis; $\{C(u), C(v)\} = \ip{u}{v}$ on all thirty-six basis pairs and $C(u)^2 = Q(u)/2$ on non-null, complex, and null instances; linear independence of the sixty-four ordered generator products in $\End(\Lambda^\bullet W)$ (rank $64$: simplicity, surjectivity and irreducibility at once); oddness of vectors; the even subalgebra of dimension exactly $32$. \emph{The Chevalley pairing} (Lemma \claimref{correspondence.chevalley-pairing}): parity vanishing, perfection of the $\T'\times\T$ block, antisymmetry on all sixty-four pairs, $B$-self-transposedness of all six basis vectors, and invariance under all fifteen antisymmetrised bivectors. \emph{The spinor identification} (Theorem \claimref{correspondence.spinor-identification}, Example \claimref{note.correspondence.isomorphism-witt-pair}): antisymmetry of $G_v$; rank six of $\Psi$; the norm correspondence on all twenty-one pairs with the computed constant ($-1$ for the $C$-normalised $\Psi$, i.e.\ $-2$ in the paper's normalisation); the exact values $\Psi_C(w_1) = -t_2\wedge t_3$, $\Psi_C(w_1') = t_0 \wedge t_1$ and their planes; the Pfaffian nullity criterion on null and non-null instances; equivariance $\Psi(\beta v) = \beta\cdot\Psi(v)$ for all fifteen bivectors on all six basis vectors (ninety identities). \emph{Incidence} (Proposition \claimref{correspondence.skew-lines-splittings-hyperbolic-planes-one}, Theorem \claimref{correspondence.incidence-relation-chart}, Proposition \claimref{correspondence.reality-conjugation-twistor-form-factor}): the hyperbolic pair; the expansion, norm identity, chart identification $P(A) = X(m(A))$ and simplicity for four sample maps $A$ (identity, Gaussian-rational, singular, and $i$ times a Hermitian matrix); the sign flip $-2\det(i\hat x) = +2\det\hat x$ on a sample map; the coverage pairing. \emph{Reality} (Proposition \claimref{correspondence.reality-conjugation-twistor-form-factor}): the real orthonormal basis and its relation to the isotropic one; the conjugation as the reflection in $b_4$ composed with coordinate conjugation; $\kappa\,C(v) = C(\bar v)\,\kappa$ on every basis state for the six basis vectors and their $i$-multiples; $\kappa^2 = -\tfrac12$ (the $C$-normalised $-1$) and the parity swap; the constant $\lambda_0 = \lambda = 1$ on the full basis, and the general relation $\Sigma(Z_2,Z_1) = \lambda\,\overline{\Sigma(Z_1,Z_2)}$ with its phase repair tested on $\kappa$ rescaled by $(3+4i)/5$, where $\lambda \neq 1$; $\Sigma$ Hermitian and of rank four; $\Som$ and $\Spi$ both $\Sigma$-null; the signature $(2,2)$ read off $\Sigma$ through its real form; all fifteen real bivectors $\Sigma$-anti-Hermitian; four $\sigma$-Hermitian $\hat x$ with $m(i\hat x)$ real and spanning $W_{1,3}$, and $m(\hat x)$ not real. \emph{Chiral planes and summands} (Lemma \claimref{correspondence.chiral-planes-summand-spaces}, Proposition \claimref{correspondence.local-twistor-transport-ascended-spinor-connection}(3)): each chirality factor annihilates exactly one of $\Som$, $\Spi$ and acts faithfully on the other, the two factors on different planes; the summand composite equals $C(e_a)C(\mathrm{P}(e_c))$, the $C$-form of $\tfrac12 c(e_a)c(\mathrm{P}(e_c))$, on $\Som$ for all sixteen pairs of mixed directions. \emph{Stabilisers and local twistors} (Fact \claimref{correspondence.imported-stabilisers-flat-model}, Proposition \claimref{correspondence.local-twistor-transport-ascended-spinor-connection}, Proposition \claimref{correspondence.clifford-side-ordering-shift}): the commutator identity $[\beta, C(w)] = C(\beta w)$ for all fifteen bivectors; trace-freeness and linear independence of the fifteen spinor actions (the $\mathfrak{sl}(\T)$ isomorphism); the stabiliser census $10 + 1 + 4$ of the infinity direction and the exact match with preservation of the plane $\Som$; both summand actions on all four mixed directions; the full eigenvalue table of $\rho(v\wedge v^*) = N - \tfrac12$. \emph{Twistors as states} (Theorem \claimref{correspondence.twistors-are-states-three-ladder-pairs}): the annihilator of the vacuum; purity (dimension three, total isotropy) of a generic even and a generic odd spinor; the joint-kernel line; generation of the whole module from a vacuum by its dual system; the CAR relations of the generic twistor's own pair system, built on its annihilator and the dual complement constructed in the proof. \emph{The palatial algebra} (Lemma \claimref{correspondence.symmetrised-quadratics-palatial-algebra}, Theorem \claimref{correspondence.shared-core-ordering-dictionary}): the relations $[Z^\alpha, \bar Z_\beta] = \hbar\delta$ in the realisation $\bar Z = -\hbar\,\partial$; the homogeneity identity $q(\mathrm{id}) = -(h+2)\hbar$ (the $-2s-2$ point of contact) on all monomials of degree $\le 3$; $[q(M), q(N)] = \hbar\,q([M,N])$ and the adjoint action for explicit Gaussian-rational $M, N$, checked on the determining monomial basis; the symmetric-versus-normal ordering shift. \emph{The chirality split} (Lemma \claimref{correspondence.lorentzian-duality-complex-structure}, Proposition \claimref{correspondence.chirality-split-ordering-insensitivity-asd-sector}): the full $\mathfrak{so}(1,3)$ bracket table, all fifteen brackets including the three vanishing $[R_i, B_i]$; closure and mutual commutation of the two chirality factors; $\ast^2 = -1$ on all six basis $2$-forms; and the $\pm i$ eigenvector property of the chirality generators $A^{(1)}_i, A^{(2)}_i$, with conjugate eigenvalues. The script exits nonzero on any failure and prints one line per check, tagged by the statement it certifies.

## technical
pending

## lay
pending

## one-liner
pending
