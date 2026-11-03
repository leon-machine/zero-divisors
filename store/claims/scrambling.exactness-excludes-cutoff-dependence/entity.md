---
id: scrambling.exactness-excludes-cutoff-dependence
kind: claim
version: 4
title: Exactness excludes cutoff dependence
status: proved
region: scrambling
subject: entropy
tags: [mode-counting, entropy-premises]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T08, deposited version
review: typed
about:
- obj.scrambling.stretched-singularity
derivations:
- name: main
  proof: proof-main.tex
  uses:
  - scrambling.residue-each-convention@4
  - scrambling.scheme-robustness-cutoff@3
checked_by:
- kind: legacy
  script: verify_T08.py
  tags:
  - num:4.10
- kind: check
  ref: check.py::check_scheme_constants_differ
- kind: check
  ref: check.py::check_kretschmann_rationality
- kind: check
  ref: check.py::check_two_cutoff_free_scales
locators:
  paper: T08
  number: Prop 4.10
  label: prop:exactnorm
  line: 800
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: scheme constants solved, c_0^a pairwise distinct over a rational grid of a, 48^(a/6) rational iff a in 6Z, the two cutoff-free scales with residues 1/4 and 1. Version 3 -> 4.'
  env: proposition
  context_refs:
  - scrambling.residue-each-convention
  typing:
    by: ai-typing-pass
    added:
    - scrambling.residue-each-convention
    - scrambling.scheme-robustness-cutoff
    note: 'Added the residue proposition (context ref, quoted for the horizon residue of one quarter)
      and the scheme-robustness lemma, not cited by name but the source of the three scheme constants
      $c_0$ the proof computes with; the second addition is the judgement call. Levels pass: the lay now
      keeps the rational-monomial hypothesis on the count.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - scrambling.scheme-robustness-cutoff
    - scrambling.residue-each-convention
---

## formal
Suppose a calibration principle returns $N_{\mathrm{epoch}} = \SBH = 4\pi M^2$ exactly and its count is a monomial $c\,\pi^p M^m$ in the geometric data of the interior with $c$ rational. Then the count cannot depend on the stretched radius $r_c$: any dependence on $r_c$ through a power $r_c^a$, $a \neq 0$, carries the scheme constant $c_0^a$, which differs between the three schemes for every real $a \neq 0$ and, for rational $a$, is irrational for the Kretschmann scheme whenever $a \notin 6\mathbb{Z}$. The principle must therefore be normalised at a scale the interior fixes without a cutoff. Exactness does not choose that scale: the interior fixes the horizon $r_h = 2M$, at which the sphere carries $A = 4\,\SBH$ cells and the count is $\SBH$ with the residue $\tfrac14$ on the cells (Proposition \claimref{scrambling.residue-each-convention}(i)), and it fixes equally the rational multiple $r_* = M = r_h/2$, at which the sphere carries $4\pi M^2 = \SBH$ cells and the residue is $1$. Which of the two a principle should mean is not decided here.

## technical
Suppose a calibration principle returns exactly $N_{\mathrm{epoch}} = \SBH = 4\pi M^2$ as a monomial $c\,\pi^p M^m$ with rational $c$. Then it cannot depend on the stretched radius $r_c$: a factor $r_c^a$ with $a \neq 0$ carries the scheme constant $c_0^a$, which differs between the three cutoff schemes for every real $a \neq 0$ and, for rational $a$, is irrational in the Kretschmann scheme unless $a \in 6\mathbb{Z}$.

The principle must therefore be normalised at a radius the interior fixes without a cutoff. Exactness leaves two such radii: the horizon $r_h = 2M$, where the sphere carries $A = 4\,\SBH$ cells and the residue is $\tfrac14$, and $r_* = M$, where the sphere carries $\SBH$ cells and the residue is $1$. Which one a principle should use is not decided.

## lay
If a rule for counting boundary modes is to reproduce the black hole entropy exactly, with a count of the simple form a rational number times powers of $\pi$ and of the mass, it cannot depend on where one cuts off the interior geometry, because different reasonable cut-offs give incompatible answers. The rule must be tied to a size the black hole fixes by itself. Two such sizes remain, the horizon radius and half of it, and the result does not choose between them.

## one-liner
An exact rational-monomial count equal to $\SBH$ cannot depend on the cutoff radius $r_c$, so it must be normalised at a cutoff-free scale, $r_h = 2M$ or $r_* = M$, and exactness does not decide which.
