---
id: odd-extensions.not-coupling-between-towers
kind: claim
version: 3
title: $\Lambda$ is not a coupling between towers
status: proved
region: odd-extensions
subject: dark-energy
tags: [towers-by-residue, superselection, cosmological-constant, no-go]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14a, deposited version
review: typed
derivations:
- name: main
  uses:
  - odd-extensions.are-ascents-pair-signed@4
  - odd-extensions.belongs-tower@5
  - odd-extensions.imported-copy-theorem-soldered-residue@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
locators:
  paper: T14a
  number: Cor 7.3
  label: cor:nocoupling
  line: 628
extraction:
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: corollary
  context_refs:
  - odd-extensions.are-ascents-pair-signed
  typing:
    by: ai-typing-pass
    added:
    - odd-extensions.are-ascents-pair-signed
    note: 'Added the pair theorem from context_refs because the statement''s first clause (Lambda is a
      datum of this tower''s ascent) rests on it, although the proof line cites only the belonging proposition
      (iii) and the copy Fact; both of those were kept. Levels pass: the lay now says the algebra coincidence
      is the positive-Lambda one, as the technical does.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - odd-extensions.are-ascents-pair-signed
---

## formal
The cosmological constant is a datum of this tower's ascent (Theorem \claimref{odd-extensions.are-ascents-pair-signed}), and its coincidence with the residue-$5$ tower's abstract algebra carries no structure across the superselection, since the dark-matter paper's exactness argument is precisely that isomorphisms between towers that do not respect the soldering carry nothing (Fact \claimref{odd-extensions.imported-copy-theorem-soldered-residue}). The coupling rule the dark-matter paper's odd towers need is not supplied by $\Lambda$.

## technical
The cosmological constant is a datum of this tower's ascent: the frozen point and the Stelle-West vector are the ascent's pair, signed by $\Lambda$. For $\Lambda > 0$ the algebra $\Cl(I^{\perp}) \cong \Cl(1,4)$ coincides with the residue-$5$ tower's abstract algebra, but the isomorphism is induced by an isometry of quadratic spaces and not by a map of soldered data.

The dark-matter paper's exactness argument is that isomorphisms between towers that do not respect the soldering carry no structure across the superselection. So the coincidence carries nothing, and the coupling rule the dark-matter paper's odd towers need is not supplied by $\Lambda$.

## lay
The framework has several towers, separate families of possible matter sectors, kept apart by a rule that only maps respecting how each algebra is tied to spacetime can carry anything between them. The cosmological constant belongs to our own tower. For a positive cosmological constant its algebra happens to look like that of one dark tower, but the match ignores that tie to spacetime, so it carries nothing across. The cosmological constant therefore cannot be the link that couples the dark towers to ours.

## one-liner
The cosmological constant is a datum of this tower's ascent, and its coincidence with the residue-$5$ tower's abstract algebra does not respect the soldering, so $\Lambda$ is not a coupling between towers.
