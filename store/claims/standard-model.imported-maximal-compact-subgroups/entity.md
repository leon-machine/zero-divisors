---
id: standard-model.imported-maximal-compact-subgroups
kind: claim
version: 1
title: 'Imported: maximal compact subgroups'
status: imported
region: standard-model
subject: standard-model
tags: [classical-theorem, rotors-and-stabilisers]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
imported_from:
- citation: S. Helgason, Differential Geometry, Lie Groups, and Symmetric Spaces, Academic Press (1978).
  key: Helgason1978
  locator: Ch.~VI, Thm.~2.1, and Ch.~X
locators:
  paper: T12
  number: Fact 9.19
  label: fact:compact
  line: 1669
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: Imported fact; levels only, no edges to review.
---

## formal
Every compact subgroup of a connected semisimple Lie group is conjugate into a maximal compact subgroup, and the maximal compact subgroup of $SO_{0}(2,4)$ is $SO(2) \times SO(4)$, of dimension $7$. \emph{Provenance:} \cite[Ch.~VI, Thm.~2.1, and Ch.~X]{Helgason1978}; standard.

## technical
In a connected semisimple Lie group every compact subgroup is conjugate into a maximal compact subgroup. For the identity component $SO_{0}(2,4)$ of the conformal group the maximal compact subgroup is $SO(2) \times SO(4)$, of dimension $1 + 6 = 7$. The result is imported from the standard theory of Lie groups and symmetric spaces.

## lay
Inside a large continuous symmetry group, every compact part, one that is closed and bounded, can be moved by a change of viewpoint into a single largest compact part. For the conformal symmetry group of spacetime that largest compact part combines a circle of rotations with the rotations of four dimensions, seven dimensions in all. It is a standard result taken from the literature.

## one-liner
Every compact subgroup of a connected semisimple Lie group is conjugate into a maximal compact one, and for $SO_{0}(2,4)$ that is the seven-dimensional $SO(2) \times SO(4)$.
