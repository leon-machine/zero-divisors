---
id: note.transport.obstruction-parabolic
kind: note
version: 1
title: The obstruction is parabolic
status: remark
subject: zero-divisors
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
comments_on:
- transport.pseudo-inverse-torsor
- transport.no-go-level-elements
- obj.transport.extension-quadratic-spaces
- transport.splitting-along-hyperbolic-plane
locators:
  paper: T01
  number: Rem 4.4
  label: rem:parabolic
  line: 763
---

## formal
The stabiliser of a null direction in an indefinite orthogonal group is not \emph{reductive}: it contains a nontrivial normal subgroup of \emph{unipotent} elements, transformations $g$ for which $g - \mathrm{id}$ is nilpotent (here $(R-1)^2 = 0$ in the algebra, while on $\mathbb{V}$ the action satisfies $(\Ad_R - \mathrm{id})^3 = 0$, with $(\Ad_R - \mathrm{id})^2 w_0 = -2Q(u)\,v$ nonzero whenever $Q(u) \neq 0$), called its unipotent radical. (``Parabolic'' parallels the M\"obius classification: like a parabolic M\"obius map, a null rotation is unipotent and fixes the null direction $[v]$; for $n = 3$ it fixes no other direction at all, while for $n \geq 4$ it fixes in addition the subspace $U \cap u^{\perp}$, which may itself contain null directions.) Step 3 shows that this radical acts on the candidate partners by translating the $\Cl(U')$-coefficient $\alpha$ by $-u$, freely and without fixed point; Proposition \claimref{transport.pseudo-inverse-torsor} makes that action exact. Two consequences deserve emphasis. First, enlarging the algebra can never help: the shearing rotors $R = 1 + vu$ and the translation vectors $u$ lie inside $\Cl(\mathbb{V})$ and act the same way in every extension, which is why Theorem \claimref{transport.no-go-level-elements} quantifies over all ascents at once. The quantifier ranges over the Clifford algebra of an extension quadratic space (Definition \claimref{obj.transport.extension-quadratic-spaces}), which is what the splitting of Lemma \claimref{transport.splitting-along-hyperbolic-plane} requires; it extends verbatim to matrix algebras $M_k\bigl(\Cl(\mathbb{V}')\bigr)$ over such an algebra, since reading $v\sigma v = v$ entrywise, with $v$ embedded as $v\,I$, makes each diagonal entry of $\sigma$ an invariant pseudo-inverse in $\Cl(\mathbb{V}')$ and so contradicts the theorem. Second, the phenomenon is absent in definite signature, where there are no null vectors and stabilisers of directions are compact and reductive: it is a genuinely mixed-signature obstruction, present exactly where the null cone is.

## technical
pending

## lay
pending

## one-liner
pending
