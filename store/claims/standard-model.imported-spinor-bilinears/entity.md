---
id: standard-model.imported-spinor-bilinears
kind: claim
version: 1
title: 'Imported: the spinor bilinears of $\mathrm{Spin}(10)$'
status: imported
region: standard-model
subject: standard-model
tags: [classical-theorem, representation-theory, flavour-and-mixing]
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
- citation: R. Slansky, Group theory for unified model building, Phys. Rep. 79 (1981) 1--128.
  key: Slansky1981
locators:
  paper: T12
  number: Fact 9.6
  label: fact:bilinears
  line: 1554
extraction:
  env: fact
  context_refs:
  - standard-model.yukawa-pattern-two-rung-module
  typing:
    by: ai-typing-pass
    note: 'Imported fact; levels only, no edges to review. Levels pass: no conditions to keep; the lay
      level now says the $10$ equates Dirac masses, not that it makes neutrinos as heavy as up quarks.'
---

## formal
$16 \otimes 16 = 10_{s} \oplus 120_{a} \oplus 126_{s}$, the subscripts giving the symmetry under exchange of the two factors; a Yukawa coupling of two generations of $16$s to a scalar in the $120$ is antisymmetric in the generation indices and vanishes for a single generation. Under $SU(5)$, $10_{v} = 5 \oplus \bar{5}$, $120 = 5 \oplus \bar{5} \oplus 10 \oplus \overline{10} \oplus 45 \oplus \overline{45}$, $126 = 1 \oplus \bar{5} \oplus 10 \oplus \overline{15} \oplus 45 \oplus \overline{50}$. A scalar in the $10$ coupled to two $16$s gives Dirac masses to up and down quarks, charged leptons and neutrinos with $m_{u} = m_{\nu}$ and $m_{d} = m_{e}$ at the scale of the coupling. \emph{Provenance:} \cite{Slansky1981}; assembly level. Theorem \claimref{standard-model.yukawa-pattern-two-rung-module} rederives the coupling pattern from the module and does not rely on this Fact for it.

## technical
In $\mathrm{Spin}(10)$, $16 \otimes 16 = 10_{s} \oplus 120_{a} \oplus 126_{s}$, so a Yukawa coupling of two generations to a scalar $120$ is antisymmetric in the generation indices and vanishes for a single generation. Under $SU(5)$, $10 = 5 \oplus \bar{5}$, $120 = 5 \oplus \bar{5} \oplus 10 \oplus \overline{10} \oplus 45 \oplus \overline{45}$ and $126 = 1 \oplus \bar{5} \oplus 10 \oplus \overline{15} \oplus 45 \oplus \overline{50}$.

A scalar $10$ coupled to two $16$s gives Dirac masses with $m_{u} = m_{\nu}$ and $m_{d} = m_{e}$ at the scale of the coupling. This is imported at assembly level from standard group theory; the module derivation of the coupling pattern does not rely on it.

## lay
In the $\mathrm{Spin}(10)$ grand unified theory a whole generation of matter sits in one sixteen-component family, and masses come from joining two such families through a scalar field. Only three kinds of scalar can do this, of sizes $10$, $120$ and $126$. The simplest, the $10$, gives up quarks and neutrinos the same Dirac mass, and down quarks and charged leptons the same mass, at the high scale. These are standard facts taken from the literature.

## one-liner
In $\mathrm{Spin}(10)$, $16 \otimes 16 = 10 \oplus 120 \oplus 126$, and a single scalar $10$ gives $m_{u} = m_{\nu}$ and $m_{d} = m_{e}$ at its scale.
