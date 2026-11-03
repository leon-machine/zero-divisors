---
id: note.tower.setting-introduction
kind: note
version: 1
title: Introduction
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
- tower.volume-elements-planes
locators:
  paper: T03
  number: Setting
  section: Introduction
  line: 142
---

## formal
The root paper of the series \cite{ButlerT1} repairs the failure of division at the null cone of $\Cl(p,q)$ by the minimal Witt completion $\Cl(p,q) \to \Cl(p{+}1,q{+}1)$, shows this is one of exactly two transport rules, classifies what each adjoins, and proves that the completed algebra is the matrix amplification $\Mat_2(\Cl(p,q))$ with the base embedded as a twisted diagonal. The completed algebra, being a Clifford algebra of mixed signature, has a null cone of its own. The question this paper answers is the evident one: what happens when the transport is iterated? Three specific forms of the question: does the ascended algebra's own singular behaviour force a further ascent, without end; does the mod-8 periodicity of the real Clifford classification make the climb circulate; and what is the limit object?

The answers are more specific than the questions. The tower $\Cl(p{+}k,q{+}k)$ is canonically $\Mat_{2^k}(\Cl(p,q))$, so the climb never leaves the ground floor's Morita class: the clock is frozen, not circulating, and the eight clock positions classify eight parallel towers, one per transport charge $p - q \bmod 8$, rather than eight stages of one tower. What the iteration accumulates is capacity, not algebraic type: each rung adjoins one hyperbolic plane whose ladder pair satisfies the canonical anticommutation relations exactly, the Fock module doubles, and the Witt index, the algebra's count of independent fermionic modes, increases by exactly one. The limit is then the object the physical reading requires: the ground algebra tensored with the CAR algebra of a free fermionic field. Iterated transport is second quantisation, one mode per rung.

The mathematical content of the limit statement requires operator-algebraic care, which it receives here. The connecting embeddings are twisted diagonals $a \mapsto \operatorname{diag}(a, \hat a)$, with $\hat a$ the grade involution; whether the twist can be removed decides whether the limit is a plain tensor product. For even transport charge the ground algebra is central simple, the involution is inner by the Skolem-Noether theorem, and the twist conjugates away rung by rung: the algebraic limit is exactly $\Cl(p,q) \otimes \Mat_{2^\infty}$, and its completed complexification is $\Cl(p,q)_\C \otimes \CAR$. For odd charge the grade involution acts nontrivially on the centre and is outer; the even-charge argument does not apply, and rather than assert the unproved standard expectation we delimit the boundary and pose the odd case precisely.

## technical
pending

## lay
pending

## one-liner
pending
