---
id: note.correspondence.setting-machine-verification
kind: note
version: 4
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle
  version: 4
  source: maintainer pass 2026-11-07 (resolve units)
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
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. The script''s scalars Q(i), the sample maps i x-hat, the i-multiples, the rescaling (3+4i)/5 and the +-i eigenvalues are in the scalar field of the complexified Fock model over V_C; by U3 its unit is I_7 = I_6 e of Cl(3,4) = Cl(2,4)_C, as in the results the note covers (std-algebra.complexification-is-the-odd-extension, cited as a mention): Q(I_7), I_7 x-hat, (3+4 I_7)/5, +-I_7. Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (other): the note describes a script that works over the Gaussian rationals Q(i) as the scalars of the complexified Fock model over V_C, where i must commute with the vectors; it records the script''s sample maps (i times a Hermitian matrix, the rescaling (3+4i)/5) in those scalars.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
---

## formal
Every computational identity asserted in this paper is verified by the deposited script \texttt{verify\_T09.py} \cite{ButlerVerifyT9}, which imports the series' shared exact-arithmetic library \texttt{GA.py} and runs entirely in exact arithmetic over the Gaussian rationals $\mathbb{Q}(I_7) = \mathrm{span}_{\mathbb{Q}}\{1, I_7\}$, with $I_7 = I_6e$ the central pseudoscalar of $\Cl(3,4) = \Cl(2,4)_\C$, the scalar unit of the complexified Fock model (\claimref{std-algebra.complexification-is-the-odd-extension}): no floating point appears anywhere, so every check is an identity, not an approximation. The script works with $C(v) = c(v)/\sqrt2$ (Section \ref{sec:setting}), so that $\{C(u), C(v)\} = \ip{u}{v}$ and $C(u)^2 = Q(u)/2$, and with the isotropic basis of Theorem \claimref{correspondence.fock-model-complexified-ascended-algebra}, which is Gaussian rational. Sixty-nine checks pass. Three reusable routines developed for this paper were promoted into \texttt{GA.py} per the series' practice, append-only and backward compatibly: an exact Gaussian-rational field class, generic-field linear algebra (rank, solve) usable over any exact field, and a kernel routine over any exact field.

The coverage, by section. \emph{The Fock model} (Theorem \claimref{correspondence.fock-model-complexified-ascended-algebra}): the CAR relations of the three wedge and contraction pairs $w_j\wedge$, $\iota_{w_j'}$ (Proposition \claimref{correspondence.clifford-side-ordering-shift}, there written $A_1$, $B_1$) and all anticommutators on the full state basis; $\{C(u), C(v)\} = \ip{u}{v}$ on all thirty-six basis pairs and $C(u)^2 = Q(u)/2$ on non-null, complex, and null instances; linear independence of the sixty-four ordered generator products in $\End(\Lambda^\bullet W)$ (rank $64$: simplicity, surjectivity and irreducibility at once); oddness of vectors; the even subalgebra of dimension exactly $32$. \emph{The Chevalley pairing} (Lemma \claimref{correspondence.chevalley-pairing}): parity vanishing, perfection of the $\T'\times\T$ block, antisymmetry on all sixty-four pairs, $B$-self-transposedness of all six basis vectors, and invariance under all fifteen antisymmetrised bivectors. \emph{The spinor identification} (Theorem \claimref{correspondence.spinor-identification}, Example \claimref{note.correspondence.isomorphism-witt-pair}): antisymmetry of $G_v$; rank six of $\Psi$; the norm correspondence on all twenty-one pairs with the computed constant ($-1$ for the $C$-normalised $\Psi$, i.e.\ $-2$ in the paper's normalisation); the exact values $\Psi_C(w_1) = -t_2\wedge t_3$, $\Psi_C(w_1') = t_0 \wedge t_1$ and their planes; the Pfaffian nullity criterion on null and non-null instances; equivariance $\Psi(\beta v) = \beta\cdot\Psi(v)$ for all fifteen bivectors on all six basis vectors (ninety identities). \emph{Incidence} (Proposition \claimref{correspondence.skew-lines-splittings-hyperbolic-planes-one}, Theorem \claimref{correspondence.incidence-relation-chart}, Proposition \claimref{correspondence.reality-conjugation-twistor-form-factor}): the hyperbolic pair; the expansion, norm identity, chart identification $P(A) = X(m(A))$ and simplicity for four sample maps $A$ (identity, Gaussian-rational, singular, and $I_7$ times a Hermitian matrix); the sign flip $-2\det(I_7\hat x) = +2\det\hat x$ on a sample map; the coverage pairing. \emph{Reality} (Proposition \claimref{correspondence.reality-conjugation-twistor-form-factor}): the real orthonormal basis and its relation to the isotropic one; the conjugation as the reflection in $b_4$ composed with coordinate conjugation; $\kappa\,C(v) = C(\bar v)\,\kappa$ on every basis state for the six basis vectors and their $I_7$-multiples; $\kappa^2 = -\tfrac12$ (the $C$-normalised $-1$) and the parity swap; the constant $\lambda_0 = \lambda = 1$ on the full basis, and the general relation $\Sigma(Z_2,Z_1) = \lambda\,\overline{\Sigma(Z_1,Z_2)}$ with its phase repair tested on $\kappa$ rescaled by $(3+4I_7)/5$, where $\lambda \neq 1$; $\Sigma$ Hermitian and of rank four; $\Som$ and $\Spi$ both $\Sigma$-null; the signature $(2,2)$ read off $\Sigma$ through its real form; all fifteen real bivectors $\Sigma$-anti-Hermitian; four $\sigma$-Hermitian $\hat x$ with $m(I_7\hat x)$ real and spanning $W_{1,3}$, and $m(\hat x)$ not real. \emph{Chiral planes and summands} (Lemma \claimref{correspondence.chiral-planes-summand-spaces}, Proposition \claimref{correspondence.local-twistor-transport-ascended-spinor-connection}(3)): each chirality factor annihilates exactly one of $\Som$, $\Spi$ and acts faithfully on the other, the two factors on different planes; the summand composite equals $C(e_a)C(\mathrm{P}(e_c))$, the $C$-form of $\tfrac12 c(e_a)c(\mathrm{P}(e_c))$, on $\Som$ for all sixteen pairs of mixed directions. \emph{Stabilisers and local twistors} (Fact \claimref{correspondence.imported-stabilisers-flat-model}, Proposition \claimref{correspondence.local-twistor-transport-ascended-spinor-connection}, Proposition \claimref{correspondence.clifford-side-ordering-shift}): the commutator identity $[\beta, C(w)] = C(\beta w)$ for all fifteen bivectors; trace-freeness and linear independence of the fifteen spinor actions (the $\mathfrak{sl}(\T)$ isomorphism); the stabiliser census $10 + 1 + 4$ of the infinity direction and the exact match with preservation of the plane $\Som$; both summand actions on all four mixed directions; the full eigenvalue table of $\rho(v\wedge v^*) = N - \tfrac12$. \emph{Twistors as states} (Theorem \claimref{correspondence.twistors-are-states-three-ladder-pairs}): the annihilator of the vacuum; purity (dimension three, total isotropy) of a generic even and a generic odd spinor; the joint-kernel line; generation of the whole module from a vacuum by its dual system; the CAR relations of the generic twistor's own pair system, built on its annihilator and the dual complement constructed in the proof. \emph{The palatial algebra} (Lemma \claimref{correspondence.symmetrised-quadratics-palatial-algebra}, Theorem \claimref{correspondence.shared-core-ordering-dictionary}): the relations $[Z^\alpha, \bar Z_\beta] = \hbar\delta$ in the realisation $\bar Z = -\hbar\,\partial$; the homogeneity identity $q(\mathrm{id}) = -(h+2)\hbar$ (the $-2s-2$ point of contact) on all monomials of degree $\le 3$; $[q(M), q(N)] = \hbar\,q([M,N])$ and the adjoint action for explicit Gaussian-rational $M, N$, checked on the determining monomial basis; the symmetric-versus-normal ordering shift. \emph{The chirality split} (Lemma \claimref{correspondence.lorentzian-duality-complex-structure}, Proposition \claimref{correspondence.chirality-split-ordering-insensitivity-asd-sector}): the full $\mathfrak{so}(1,3)$ bracket table, all fifteen brackets including the three vanishing $[R_i, B_i]$; closure and mutual commutation of the two chirality factors; $\ast^2 = -1$ on all six basis $2$-forms; and the $\pm I_7$ eigenvector property of the chirality generators $A^{(1)}_i, A^{(2)}_i$, with conjugate eigenvalues. The script exits nonzero on any failure and prints one line per check, tagged by the statement it certifies.

## technical
pending

## lay
pending

## one-liner
pending
