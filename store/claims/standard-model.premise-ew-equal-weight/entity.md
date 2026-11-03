---
id: standard-model.premise-ew-equal-weight
kind: claim
version: 1
title: 'Premise (EW): equal weight on the heavy direction'
status: postulate
region: standard-model
subject: neutrinos
tags: [neutrino-premises, seesaw-and-majorana]
proposed_by:
  kind: human
  author: leon (stated in the paper); entered by the build
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
locators:
  paper: T12
  number: Premise (EW)
  label: ''
  line: 2062
extraction:
  env: hypothesis
  typing:
    by: ai-typing-pass
    note: Stated inside the remark that equal weight is a premise; formal text is the premise sentence
      and the scope sentence after it, verbatim (the remark has no store entity).
---

## formal
\emph{Premise (EW):} in a family basis in which the symmetric part of $M_{u}$ is diagonal with $(M_{u})_{33} = m_{t}$, $(M_{\nu})_{33} = 0$; since $h$ has no diagonal, this is $4w_{u}f_{33} = m_{t}$. Applied in every family direction the premise would make $M_{u}$ proportional to $f$ and every light neutrino massless, so it cannot hold beyond the heavy direction.

## technical
Premise (EW) fixes the neutrino's Dirac entry along the heavy family direction only: in a family basis in which the symmetric part of $M_{u}$ is diagonal with $(M_{u})_{33} = m_{t}$, it sets $(M_{\nu})_{33} = 0$, which, since $h$ has no diagonal, reads $4w_{u}f_{33} = m_{t}$.

It is declared as a premise because it is not derived: saying that the Dirac elements commute with the condensate says no more than that the condensate removes the neutrino's Dirac entry. Applied in every family direction it would make $M_{u}$ proportional to $f$ and every light neutrino massless, so it cannot hold beyond the heavy direction.

## lay
This is an assumption, not a result: in the heaviest family, one contribution to the neutrino's mass is taken to vanish exactly, which ties a coupling to the top quark's mass. The framework's other statements do not imply it. Applied to every family it would make all neutrinos massless, so it is used only for the heaviest.

## one-liner
Premise (EW): along the heavy family direction the neutrino's Dirac entry vanishes, $(M_{\nu})_{33} = 0$, that is $4w_{u}f_{33} = m_{t}$.
