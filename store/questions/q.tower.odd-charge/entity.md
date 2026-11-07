---
id: q.tower.odd-charge
kind: question
version: 3
title: Odd charge
status: settled
region: tower
subject: tower
tags:
- open-problem
- towers-by-residue
- limits
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
lineage:
  motivated_by:
  - tower.grade-twist-when-it-inner
  - tower.algebraic-limit-even-charge
locators:
  paper: T03
  number: Question 5.8
  label: q:oddcharge
  line: 450
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Lay level and one-liner updated to the settled status (settled_by synthesis.tower-limit-forgets-residue: the odd-charge limit is Cl^0(p,q) (x) Mat_{2^infinity}, isomorphic to Mat_{2^infinity}, and no invariant separates the cases); the formal and technical levels keep the question as posed. No version bump (lay and one-liner only).'
  env: question
  context_refs:
  - tower.grade-twist-when-it-inner
  typing:
    by: ai-typing-pass
    note: Question; levels only.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants: []
    added_about:
    - obj.tower.tower
    verdict: standalone
    note: 'Open question: it asks for the odd-charge analogue of the even-charge limit theorem and arises where
      the grade-twist lemma fails (both recorded as lineage); nothing in the store settles it.'
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 5
    note: 'Settled by the accepted synthesis result: every tower''s algebraic limit, odd charge included, is the
      same CAR algebra Cl(H_infinity); for p - q odd it is Cl^0(p,q) tensored with Mat_{2^infinity}, not Cl(p,q)
      tensored with it.'
settled_by:
- synthesis.tower-limit-forgets-residue
---

## formal
For $p - q$ odd the connecting twist is outer on the centre and Lemma \claimref{tower.grade-twist-when-it-inner} fails; the limit is still an AF-style object (an increasing union of finite-dimensional semisimple algebras), but its identification is sensitive to how the twist moves the two central idempotents (split case) or conjugates the complex structure (complex case). Identify $\varinjlim T_k$ for odd charge; in particular decide whether it is again a plain tensor product with $\Mat_{2^\infty}$, and what real K-theoretic invariant separates the cases if not.

## technical
For odd transport charge $p - q$ the connecting twist acts as an outer automorphism on the centre, so the lemma that makes the grade twist inner in the even case fails. The direct limit $\varinjlim T_k$ is still an increasing union of finite-dimensional semisimple algebras, but identifying it depends on how the twist moves the two central idempotents (split case) or conjugates the complex structure (complex case).

The question asks for that limit: is it again a plain tensor product with $\Mat_{2^\infty}$, and if not, which real K-theoretic invariant separates the cases?

## lay
For towers of even charge the series knows exactly what the infinite limit of the ladder of algebras is. For odd charge each step twists the centre of the algebra in a way that blocks the same argument. The question was what the limit is in that case, and whether some invariant from K-theory is needed to tell the possibilities apart. It is settled: the limit is again a plain tensor product, now of the even half of the starting algebra, and it is the same algebra for every tower, so no invariant tells the cases apart.

## one-liner
Settled question: the direct limit of the tower for odd transport charge is $\Cl^{0}(p,q) \otimes \Mat_{2^\infty} \cong \Mat_{2^\infty}$, a plain tensor product, and no invariant, real K-theoretic or other, separates the cases.
