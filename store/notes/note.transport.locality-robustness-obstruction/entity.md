---
id: note.transport.locality-robustness-obstruction
kind: note
version: 1
title: Locality and robustness of the obstruction
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
- transport.no-go-level-elements
locators:
  paper: T01
  number: Rem 4.3
  label: rem:local
  line: 755
---

## formal
The proof consumes far less than the theorem's hypotheses offer, and it is worth recording what it actually uses, since the surplus rules out the obvious weakenings.

\emph{It is local.} Only the stabiliser of a \emph{single} null vector enters. The sharp statement proved above is therefore: \emph{for one null vector $v$ there is no $\sigma \in \Cl(\mathbb{V}')$ with $v\sigma v = v$ that is invariant under the null rotations fixing $v$.} No global rule, no coherence across the cone, and no regularity of $\sigma$ (continuity, measurability, genericity) is assumed or would help; the theorem as stated follows at once.

\emph{It survives equivariance up to scale.} The natural first weakening is to ask only that $\sigma(v)$ be canonical projectively, $\tau_R(\sigma(v)) = \lambda\,\sigma(v)$ for some $\lambda \neq 0$. This fails too. In the normal form of Step 1 the $w_0$-coefficient is $\gamma = 1$, and Step 3 shows it is unchanged by conjugation; comparing $w_0$-components forces $\lambda = 1$, whereupon the $\Cl(U')$-comparison gives the same contradiction $u = 0$.

## technical
pending

## lay
pending

## one-liner
pending
