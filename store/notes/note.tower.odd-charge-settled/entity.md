---
id: note.tower.odd-charge-settled
kind: note
version: 1
title: The odd-charge limit is settled
status: remark
subject: tower
proposed_by:
  kind: ai
  session: maintainer-2026-11-07-decisions
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: drafting of the remark
  source: maintainer pass 2026-11-07 (decisions)
comments_on:
- q.tower.odd-charge
- synthesis.tower-limit-forgets-residue
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'New remark (DECISIONS G9, R12 item 3): T03''s running text (note.tower.abstract, note.tower.setting-scope, note.tower.setting-introduction, note.tower.setting-contribution, note.tower.what-completion-means-here-why-it) still calls the odd-charge limit open and says the real limit remembers strictly more; the paper text is left as written and this remark records the settlement by synthesis.tower-limit-forgets-residue.'
---

## formal
The odd-charge question of the tower paper (\claimref{q.tower.odd-charge}) is settled by Theorem \claimref{synthesis.tower-limit-forgets-residue}: for every $(p,q)$, with $p - q$ of either parity, the algebraic limit of the tower over $\Cl(p,q)$ is $\Cl(\R^{p,q} \perp H_{\infty}) \cong \Mat_{2^{\infty}}$; for $p - q$ odd it is $\Cl^{0}(p,q) \otimes \Mat_{2^{\infty}}$, again a plain tensor product, and not $\Cl(p,q) \otimes \Mat_{2^{\infty}}$. The limit determines neither $n = p + q$ nor the residue, so no invariant, real K-theoretic or other, of the limit algebra separates the cases. Where the paper's running text calls the odd-charge limit open, or says that the real limit remembers strictly more than the even case, it predates this theorem; the text is kept as the paper wrote it.

## technical
The tower paper left open what the infinite limit of the tower is when the transport charge is odd. The store now answers it: every tower's algebraic limit is the same algebra $\Mat_{2^{\infty}}$, for odd charge in the form $\Cl^{0}(p,q) \otimes \Mat_{2^{\infty}}$, so nothing in the limit algebra tells the towers apart. The paper's sentences calling the question open are kept as written and read with this settlement.

## lay
The paper on towers of algebras asked what the endless tower looks like when its starting charge is odd, and its text still calls that open. It has since been answered: every tower ends in the same infinite algebra, so the end point forgets which tower it came from.

## one-liner
The tower paper's open odd-charge limit is settled: every tower's algebraic limit is $\Mat_{2^{\infty}}$, for odd charge $\Cl^{0}(p,q) \otimes \Mat_{2^{\infty}}$, and no invariant of the limit separates the cases.
