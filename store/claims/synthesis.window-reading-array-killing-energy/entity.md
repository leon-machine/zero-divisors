---
id: synthesis.window-reading-array-killing-energy
kind: claim
version: 2
title: 'The window reading of an array''s Killing energy'
status: postulate
region: synthesis
subject: thermality
tags: [thermal-premises, boundary-modes, mode-counting]
proposed_by:
  kind: ai
  session: maintainer-2026-10-31
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Fable 5.2
  role: 'scope sentence at Leon''s decision of 10 November 2026: the reading equates mean Killing energy only'
  version: 2
  source: maintainer pass of 2026-11-10
review: draft
about:
- obj.hawking.continuum-mode-space
lineage:
  motivated_by:
  - synthesis.null-ordering-of-counted-units-is-zeta-symmetric
  - synthesis.counted-unit-energy-at-half-offset
  - synthesis.positive-null-energy-gives-r-premises
  - synthesis.n-plus-null-ground-state
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 1 -> 2. Scope sentence added at Leon''s decision of 10 November 2026: the reading equates the mean Killing energy only. The array''s entropy (1/2) ln 2 and the continuum''s entropy rate times the window, pi/6 per complex component, are different objects and the reading does not equate them; the variance of the energy differs too. The reading itself and its refutation conditions are unchanged. Which object''s entropy the count compares with A/4 is an attack item of op.residue-killing-weights.'
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: >-
      New adopted reading, registered by Leon's decision of 2026-10-31 to adopt the window reading of an array's
      Killing energy (the hypothesis of clause (iv) of synthesis.null-ordering-of-counted-units-is-zeta-symmetric),
      at the tier of the store's other premises: taken as given, with a refutation condition. Given it, the half
      offset of (Q) version 3 is singled out by (N+), the counted units carry zero mean Killing energy and the
      ground-energy label carries all of M. It does not fix the count unit or the label's energy function. An
      assumes edge from the null-ordering result is added with it.
---

## formal
\emph{The window reading (adopted).} Units $\hbar = c = 1$. On a half-generator of a horizon in the scope of Premise \claimref{synthesis.n-plus-null-ground-state}, with surface gravity $\kappa$, Killing time $\tau$ and affine parameter $u = e^{\kappa\tau}$, let an array be an evenly spaced set of modes with weights $\omega_{k} = \kappa(k + \delta)$, $k \in \Z$, $0 \le \delta < 1$ (an s-wave array of Premise \claimref{singularity.q-joint-quasi-freeness-s-wave}, whose version 3 has $\delta = \tfrac12$). The array is read as one chiral complex component of the continuum of that light ray on a window of Killing time of length $2\pi/\kappa$ (its real-time recurrence window), and its Killing energy, in every state, is the Killing energy of the continuum over that window measured from the null ground state that (N$_{+}$) selects, that is, in the normal ordering at that state, in which $\langle T_{uu}\rangle = 0$.

\emph{Scope (mean energy only).} The reading equates the mean Killing energy of an array with that of the continuum over one window, and nothing else. The array's entropy at the Hawking temperature, $\tfrac12\ln 2$ (Theorem \claimref{synthesis.half-integer-weight-array-carries-half-ln2}), and the continuum's entropy rate times the window, $\pi/6$ per complex component, are different objects, and the reading does not equate them; the variance of the energy differs too. The count of the series uses the array's entropy.

\emph{What it is for.} It is the hypothesis of clause (iv) of Theorem \claimref{synthesis.null-ordering-of-counted-units-is-zeta-symmetric}, which with it decides the ordering question left open by Theorem \claimref{synthesis.counted-unit-energy-at-half-offset}: the boost ground state carries $-\kappa/24$ per complex component over one window measured from the null ground state, and an array's zeta-regularised symmetric sea energy $\tfrac{\kappa}{2}B_{2}(\delta)$ takes that value exactly at $\delta = \tfrac12$. Given the reading, (i) the half offset of (Q) version 3 is singled out by (N$_{+}$), being the only offset at which an array's own sea is consistent with the null ordering window by window; (ii) at that offset the zeta-regularised symmetric ordering is the physical ordering of the sea's energy; (iii) a counted unit of two arrays carries mean Killing energy $0$ at the Hawking temperature, the equality case of clause (v) of Theorem \claimref{synthesis.residue-from-mode-entropy}; (iv) the constant of the hole's Hamiltonian in Theorem \claimref{synthesis.hole-mass-is-ground-energy-label}(iii) is all of $M$, so the ground-energy label carries all of $M$ and the counted units none. It does not fix the count unit (two arrays per registered unit remains a decision), the label's energy function, or which fields form the sea.

\emph{What it costs.} It is a reading of the arrays, not a consequence of (N$_{+}$): (N$_{+}$) cannot be posed on point-spectrum mode sets (Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}(iv)), and the reading applies that theorem's discretisation reading, by which the point-spectrum wordings of the thermal premises are discretisations of the continuum statements, to energy. It also identifies the spectrum of an array, of spacing $\kappa$, with a twisted identification of real Killing time over one window, which the continuum does not supply. The numbers it relates are equalities proved without it; without it the ordering is not decided.

\emph{Refutation condition.} The reading is false if any of the following is established: (a) a derivation, from the series' premises, of the Killing energy of an array (for example from a construction of the arrays out of the continuum modes of a light ray) that differs from the continuum's window energy measured from the null ground state; (b) a derivation that the arrays' offset is not $\tfrac12$, since under the reading no other offset is consistent with the null ordering window by window (at $\delta = 0$ the symmetric sea is $+\kappa/12$, not $-\kappa/24$); (c) a derivation, from the series' premises, that the counted units carry a nonzero mean Killing energy, or that the hole's energy $M$ is shared between the label and the counted units.

## technical
The series counts a black hole's entropy in units of two arrays, evenly spaced sets of modes on each light ray of the horizon, and the energy those units carry depends on where the zero of energy is put. The null ground-state premise (N$_{+}$) puts the zero of null energy at the state of the light rays it selects, but it is a statement about the continuum of each light ray and cannot be posed on an array. This reading bridges the two: an array is one stretch of a light ray's continuum, one recurrence window of Killing time $2\pi/\kappa$ long, and its Killing energy is the continuum's energy over that window, measured from the null ground state. With it, the stored equality of numbers becomes a decision of the ordering: the half offset of (Q) version 3 is the only offset at which an array's zeta-regularised sea takes the null ground state's window value, the symmetric ordering is the physical one, the counted units carry no mean Killing energy, and the whole of the hole's mass sits in the ground-energy label. The reading equates mean Killing energy only: it does not equate the array's entropy, $\tfrac12\ln 2$, with the continuum's entropy rate times the window, $\pi/6$ per complex component, nor the variances of the energy. It is adopted, not derived, and would be refuted by a derivation of an array's energy that disagrees, by a forced offset other than one half, or by a derivation that the counted units carry part of the mass.

## lay
The series counts a black hole's entropy in small units on its horizon, and whether those units carry energy depends on where the zero of energy is placed. The series' premise about the state on the horizon's light rays places it, but only for the light rays as a whole, not for the counted units. This assumption connects the two: a unit's energy is the energy of the stretch of light ray it stands for. With it, the units carry no energy on average and the hole's mass sits in a single overall constant. It is a statement about average energy only, not about entropy. It is an assumption of the series, stated so that it can be refuted.

## one-liner
Adopted reading: an array of (Q) is one chiral component of a light ray's continuum on a Killing-time window $2\pi/\kappa$, and its Killing energy is the continuum's over that window measured from the null ground state of (N$_{+}$); given it, the half offset is singled out by (N$_{+}$), the counted units carry zero mean Killing energy and the ground-energy label carries all of $M$; the reading equates mean Killing energy only, not entropy.
