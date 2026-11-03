---
id: note.tower.setting-machine-verification
kind: note
version: 2
title: Machine verification
status: setting
subject: tower
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T03, deposited version
comments_on:
- tower.compatibility-connecting-maps-transported
- tower.structure-tower-c-norms
- tower.grade-twist-when-it-inner
locators:
  paper: T03
  number: Setting
  section: Machine verification
  line: 492
extraction:
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
---

## formal
Every computational identity in this paper has been checked by computer, in exact rational arithmetic over the shared library's basis-blade Clifford product, in the manner of the verifications deposited with \cite{ButlerT1, ButlerT4}. The script \texttt{verify\_T03.py}, deposited with this paper alongside the series' shared exact-arithmetic library \texttt{GA.py}, \cite{ButlerVerifyT03}, performs its checks and reports each. The coverage: the volume-element lemma in full on the two-rung floor over $\Cl(1,3)$ (squares, own-plane anticommutation, all cross commutations, and the $\Omega_2$ properties); the commuting-copies theorem at $k = 2$, where the twisted generators are verified to satisfy the ground relations, all sixteen generator pairs of $A_2$ against $B_2$ commute, and the $256$ products of $A$-blades with $B$-blades are checked to be $256$ \emph{distinct} basis blades of $\Cl(3,5)$, an exact generation-and-dimension count; the frozen clock on floors $0$, $1$, $2$ of the physical tower by exhaustive blade-wise commutant (valid for diagonal forms, where an element is central exactly when each blade of its support is), each centre coming out $\operatorname{span}\{1\}$, so no checked floor hosts a central idempotent; the twenty-seven CAR relations of three ladder pairs in $\Cl(3,3)$ as vector identities; the Fock module on $\Lambda^\bullet W_3$ (the anticommutators on all eight states, $c(\alpha)^2 = Q(\alpha)\,\mathrm{id}$ for a general rational vector, the vacuum clause, and irreducibility by the exact rank of the sixty-four blade actions inside $\End(\Lambda^\bullet W_3)$); capacity instances in $\Cl(2,4)$ and on the floor $\Cl(3,5)$, with the isotropy and independence (exact rank) of the creation span verified in both algebras, as in the theorem's own argument; the grade twist: $\Ad_u$ equal to the grade involution on all blades of $\Cl(1,3)$ and $\Cl(2,4)$, the block conjugation $U \operatorname{diag}(a,a)\,U^{-1} = \operatorname{diag}(a, \hat a)$ in $\Mat_2(\Cl(1,3))$, and the odd-charge outerness witnessed in $\Cl(1,0)$ (commutative, yet the involution swaps its central idempotents); the compatibility lemma in full at one stage over the ground algebra $\Cl(1,1)$, where the transported connecting map is checked against $\Ad(V_k) \circ \theta_k$ with the \emph{split} corrector of Lemma \claimref{tower.compatibility-connecting-maps-transported}, generator by generator inside $\Cl(3,3)$, and the naive corrector $\operatorname{diag}(1, u_{T_1})$ is checked to fail, so the split is necessary; the *-structure of Lemma \claimref{tower.structure-tower-c-norms} on $\Cl(2,2)$ (antimultiplicativity on sampled products, unitarity of all generators and of the volume elements, and $v^* = w$ for the ladder pair); and the single-step corrector identity of Lemma \claimref{tower.grade-twist-when-it-inner} rearranged as one commuting square, on a sample element. Thirty-one checks in all. No floating point is used anywhere; the script exits nonzero on any failure, and all checks pass.

## technical
pending

## lay
pending

## one-liner
pending
