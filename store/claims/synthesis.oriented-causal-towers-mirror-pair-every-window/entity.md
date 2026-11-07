---
id: synthesis.oriented-causal-towers-mirror-pair-every-window
kind: claim
version: 2
title: In every dimension the oriented causal towers are the mirror pair of residues 2 and 6
status: proved
region: synthesis
subject: dark-matter
tags: [towers-by-residue, chirality, pseudoscalar-and-centre, obstruction-types]
proposed_by:
  kind: ai
  session: synthesis-bridges-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
derivations:
- name: main
  uses:
  - dark-matter.two-families-are-two-chiralities@7
  - transport.sign@3
  - odd-extensions.imported-conformal-completion@5
  - rule2.where-obstruction-sits-commuting-square@6
  - field-theory.where-each-lives@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_oriented_causal
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - dark-matter.which-towers-can-carry-arrow
  - dark-matter.towers-are-residues-single-clock-filter
  - dark-matter.flag-bit-exists-exactly-tower-dimension
extraction:
  review_fixes:
    by: ai-review-fix
    date: 2026-10-21
    note: 'Referee fix: the count of oriented causal signatures per dimension n = 0 mod 4 is restricted to n >= 4.'
  proof_restored:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'proof-main.tex was lost in an earlier sync; reconstructed from the formal statement and its premises'
  check_restored:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'check.py, named by checked_by but lost in the same sync, rewritten in exact arithmetic (enumeration to n = 10, GA.py products at n = 4 and 8).'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Version 1 -> 2 only because the restored proof text and check file enter the substantive hash (validator E206); the statement and the premises are unchanged.'
---

## formal
Let a tower representative have signature $(p,q)$, dimension $n = p + q$ and residue $r = p - q \pmod 8$, with conformal ambient of signature $(p+1, q+1)$ (Fact \claimref{odd-extensions.imported-conformal-completion}). Call it \emph{oriented} if a Witt pair $W, W'$ of the complexified ambient lies in opposite families, which by Proposition \claimref{dark-matter.two-families-are-two-chiralities}(iii) happens exactly when $m = (n+2)/2$ is odd, that is $n \equiv 0 \pmod 4$; and \emph{causal} if $\min(p,q) = 1$. Then, in every dimension and with no choice of representatives or window:
\begin{enumerate}
\item[(i)] a tower that is both oriented and causal has residue $2$ or $6$. In each dimension $n \equiv 0 \pmod 4$, $n \ge 4$, there are exactly two such signatures, $(1, n-1)$ and $(n-1, 1)$, with residues $2 - n$ and $n - 2$, which are $\{2, 6\}$ as a set: a mirror pair $r \leftrightarrow -r$;
\item[(ii)] the self-mirror even residues $0$ and $4$, the fixed points of $r \mapsto -r$, contain no oriented causal tower in any dimension, and every signature of residue $0$ or $4$ has pseudoscalar square $\omega^{2} = +1$ (Lemma \claimref{transport.sign}): no tower of these residues has a pseudoscalar imaginary unit, and when $n$ is even $\tfrac12(1 \pm \omega)$ are central idempotents of its even subalgebra, so chirality there is a real splitting;
\item[(iii)] every oriented causal tower has $\omega_{n}^{2} = -1$ and conformal pseudoscalar $\omega_{n+2}^{2} = -1$; $\omega_{n}$ anticommutes with the tower's vectors, commutes with the ascended plane and is central in the even subalgebra, the properties of the field theory's unit $I_{4}$ at $n = 4$ (Proposition \claimref{field-theory.where-each-lives}); and its spacelike extension $\Cl(p, q+1)$ carries the type-C obstruction, with central idempotents $\tfrac12(1 \pm \omega_{n+1})$ (Theorem \claimref{rule2.where-obstruction-sits-commuting-square}(a)).
\end{enumerate}
Consequently the conclusion of Corollary \claimref{dark-matter.which-towers-can-carry-arrow} that the towers both oriented and causal are this one and the mirror holds as a statement about residues in every window: Premise P3 fixes which dimension the other residues' representatives have, but no window makes a tower of residue $0$, $4$ or an odd residue both oriented and causal.

## technical
Orientation of a tower, in the sense of the Witt flag, is the condition that the two halves of a Witt pair of its complexified conformal ambient lie in opposite families, which holds exactly when the tower dimension $n$ is divisible by four. Causality is $\min(p,q) = 1$. In dimension $n \equiv 0 \pmod 4$, $n \ge 4$, the only causal signatures are $(1, n-1)$ and $(n-1, 1)$, of residues $\pm(n-2)$, and $n - 2 \equiv 2 \pmod 4$ makes these $2$ and $6$ modulo $8$ whatever $n$ is. So orientation and causality together select the mirror pair $\{2, 6\}$ in every window, not only at the dimension-four representatives of Premise P3. The two self-mirror even residues $0$ and $4$ never host an oriented causal tower, and their pseudoscalars always square to $+1$, so they never carry a pseudoscalar unit. The selected pair always does: tower and conformal pseudoscalars square to $-1$, the tower one commutes with the ascended plane as the field theory's $I_{4}$ does, and the spacelike one-dimensional extension of either member is the type-C obstruction of the root paper.

## lay
The series sorts its eight towers by a number from zero to seven. Two properties matter for whether a tower can hold matter like ours: whether it has a single direction of time, and whether its spinors carry an orientation bit that can record a matter-antimatter asymmetry. The dark-matter paper found that only our tower and its mirror have both, but only after assuming every tower lives in four dimensions. This result removes that assumption: in any number of dimensions, having both properties forces the tower number to be 2 or 6, our tower and its mirror, and those two always come with a built-in imaginary unit, while towers 0 and 4 never do.

## one-liner
Oriented ($n \equiv 0 \pmod 4$) and causal ($\min(p,q) = 1$) together force residue $2$ or $6$ in every dimension, a mirror pair with $\omega^{2} = -1$ and a type-C spacelike extension, so the oriented causal towers are this one and the mirror without Premise P3.
