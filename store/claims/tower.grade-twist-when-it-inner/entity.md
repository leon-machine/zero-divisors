---
id: tower.grade-twist-when-it-inner
kind: claim
version: 4
title: The grade twist, and when it is inner
status: proved
region: tower
subject: tower
tags: [grading-and-parity, pseudoscalar-and-centre]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T03, deposited version
review: typed
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - transport.rule-1-morita-trivial@5
  - std-algebra.pseudoscalar-commutation@1
  - primer.centre@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T03.py
  tags:
  - num:5.1
- kind: check
  ref: check.py::check_embedding_is_twisted_diagonal
- kind: check
  ref: check.py::check_even_charge_volume_element_implements_twist
- kind: check
  ref: check.py::check_inner_exactly_for_even_charge
locators:
  paper: T03
  number: Lem 5.1
  label: lem:twist
  line: 344
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.pseudoscalar-commutation, primer.centre where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the tower embedding as the twisted diagonal in the corner identification, Ad_u = grade involution for even n, and innerness exactly for even n (implementing kernel R u or 0; centre moved for odd n). Version 2 -> 3. Wording fix (Leon 2026-10-23): diag(a, a^) is stated to hold in the corner identification of Fact transport.rule-1-morita-trivial, reading diag(a^, a) in the twisted coordinates with E11 = vw (formal and technical).'
  env: lemma
  context_refs:
  - tower.commuting-copies
  - tower.compatibility-connecting-maps-transported
  typing:
    by: ai-typing-pass
    note: 'Kept the Rule 1 edge, which gives the matrix form of the embedding; did not add the commuting-copies
      context_ref, since the proof uses only Rule 1 with base T_k and that theorem already cites this
      lemma for its compatibility clause, so the edge would be framing only and would close a cycle. Levels
      pass: conditions already kept.'
---

## formal
Under the isomorphism of Theorem \claimref{tower.commuting-copies}, the tower embedding $\iota_k$ becomes the twisted diagonal $a \mapsto \operatorname{diag}(a, \hat a)$ of \cite[Thm.~7.1]{ButlerT1} (in the corner identification of Fact \claimref{transport.rule-1-morita-trivial}; in the twisted coordinates with $E_{11} = vw$ it reads $\operatorname{diag}(\hat a, a)$). If $p - q$ is even, $\Cl(p,q)$ is central simple over $\R$, the grade involution is an $\R$-algebra automorphism fixing the centre, and it is inner, implemented by the ground volume element $u$ (which anticommutes with vectors precisely when $n$ is even): $\hat a = u a u^{-1}$. Consequently $\operatorname{diag}(a, \hat a) = U \operatorname{diag}(a, a)\, U^{-1}$ with $U = \operatorname{diag}(1, u)$: the twist conjugates away at the level of the single step. (How the correction transports through the identifications of Theorem \claimref{tower.commuting-copies}, which is what the limit theorem needs, is Lemma \claimref{tower.compatibility-connecting-maps-transported}; the stagewise corrector is \emph{not} simply this $U$.) If $p - q$ is odd the grade involution acts nontrivially on the centre ($\R \oplus \R$ or $\C$) and is outer; no inner correction exists.

## technical
Under the commuting-copies isomorphism, the tower embedding $\iota_k$ is the twisted diagonal $a \mapsto \operatorname{diag}(a, \hat a)$ (in the corner identification of Fact \claimref{transport.rule-1-morita-trivial}; in the twisted coordinates with $E_{11} = vw$ it reads $\operatorname{diag}(\hat a, a)$), with $\hat a$ the grade involution. When $p - q$ is even, $\Cl(p,q)$ is central simple over $\R$ and the grade involution is inner: it is conjugation by the ground volume element $u$, which then anticommutes with every vector, so $\hat a = u a u^{-1}$. Hence $\operatorname{diag}(a, \hat a) = U \operatorname{diag}(a, a)\, U^{-1}$ with $U = \operatorname{diag}(1, u)$, and the twist conjugates away at a single step.

This single-step corrector is not the stagewise corrector the limit needs, which is handled by a separate compatibility lemma. When $p - q$ is odd, the centre is $\R \oplus \R$ or $\C$, the grade involution acts nontrivially on it, and so it is outer: no inner correction exists.

## lay
Each step up the tower places the previous algebra inside the next one with a small twist, built from the operation that flips the sign of every vector. When the numbers of positive and negative directions differ by an even amount, the twist is only a change of viewpoint at each step: conjugating by a single element, the volume element of the ground algebra, undoes it. When they differ by an odd amount, the twist moves the centre of the algebra and cannot be undone in this way.

## one-liner
The tower embedding is a diagonal twisted by the grade involution, which is inner, implemented by the ground volume element, when $p - q$ is even, and outer when $p - q$ is odd.
