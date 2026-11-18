---
id: simulations.s3-mirror-cluster
kind: claim
version: 4
title: 'S3: the mirror in a cluster (model specification)'
status: postulate
region: simulations
subject: dark-matter
tags:
- halos-and-clusters
- mirror-sector
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14b, deposited version
- name: Claude Fable 5.2
  role: 'typed as model specification; the window of xi on which the helium composition is the stored estimate stated'
  version: 2
  source: maintainer pass of 2026-11-10
- name: Claude Fable 5.2
  role: 'the neutron-rich composition stated at the temperature ratio where it was computed, which is no longer the gravitational floor'
  version: 3
  source: 'maintainer pass of 2026-11-18 (run 2026-11-18-navigate)'
- name: Claude Fable 5.2
  role: 'the present gravitational floor named in the window clause (6.6e-4), after the floor was defined with the mean energy per creation event; then the neutron-rich composition stated at the present floor as well, from the rerun recorded in the composition Computation'
  version: 4
  source: 'maintainer pass of 2026-11-18 (run 2026-11-18-leads)'
amendments:
- version: 4
  kind: restatement
  defect: 'the window clause referred to the present floor without its value, and the record of version 3 gave that value as 5.2e-4, the floor at the convention of energy 3T per creation event; at the mean energy per event the present floor is 6.6e-4, now stated in the clause. Follow-up of the same day: the clause said the composition was not recomputed at the present floor; it is now, and the stored estimate gives a neutron-rich mirror there too (83 to 96 percent neutrons for L <= 0)'
- version: 3
  kind: restatement
  defect: 'two sentences placed the neutron-rich composition at the gravitational floor; it was computed at xi = 2.8 to 3.2e-4, the floor with the first imported coefficients, and is not recomputed at the present floor, 5.2e-4'
review: typed
locators:
  paper: T14b
  number: Premise 2.9
  label: prem:S3
  line: 138
extraction:
  maintainer_pass_2026_11_18_energy:
    by: maintainer-2026-11-18
    date: '2026-11-18'
    note: 'Version 3 -> 4, at Leon''s decision of 18 November 2026, 14:04 (adopt the computed mean energy per creation event in the gravitational floor). The formal level now names the present floor, 6.6e-4 (dark-matter.stored-asymmetry-charge-not-number (iii), version 13); the amendment of version 3 quotes 5.2e-4, the value on that pass. The model specification itself, its window of xi and the statement that the neutron-rich composition is computed only at xi = 2.8 to 3.2e-4 are unchanged. Follow-up, same day, version kept at 4: the window clause no longer says ''not recomputed at the present floor''; the stored estimate gives a neutron-rich mirror at 6.6e-4 as well (83 to 96 percent neutrons for L <= 0, against 96 to 100 at 2.8 to 3.2e-4; dark-tower-matter.mirrors-composition (i), version 5 as extended the same day). The window of the specification is unchanged. The figures at the present floor are decimal results of the supplementary scripts behind dark-tower-matter.mirrors-composition, run again on 18 November 2026 with 6.6e-4 added to their grids (that entity''s proof text and note give the details); the scripts are not in the store and no check is added.'
  maintainer_pass_2026_11_18:
    by: maintainer-2026-11-18
    date: '2026-11-18'
    note: 'Version raised by one: the neutron-rich composition is stated at xi = 2.8 to 3.2e-4, where it was computed.'
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 1 -> 2. Leon''s decision 10 of 10 November 2026: the six simulation premises (C, S1 to S5) are typed as model specification. The store has no entity type for a model specification, and an object cannot be the target of an assumes edge, so the entity keeps kind claim and status postulate (the assumes edges of simulations.halo-shapes and simulations.merger stand) and is marked in its title and at every level. S3 now states its window of xi (the stored composition estimate dark-tower-matter.mirrors-composition gives helium only there).'
  typing:
    by: ai-typing-pass
    note: Postulate; no edges.
  env: premise
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - simulations.merger
    - simulations.halo-shapes
    added_about: []
    verdict: connected
    note: Assumed by the merger and cluster-assembly runs (the cluster mirror model); the Galaxy model
      of Obs 9.1 uses its own semi-analytic model, so mirror-galaxy does not assume it.
---

## formal
Mirror matter in a cluster is a fully ionised helium plasma, $\gamma = 5/3$, cooling by bremsstrahlung alone (below about $10^{6}$ K He$^{+}$ line cooling would in reality dominate, so settling would come sooner; Cost K3). Gas that cools below about $7 \times 10^{4}$ K becomes collisionless (the settled phase). There is no mirror star formation and no feedback.

\emph{Type: model specification.} This is a clause of the specification of the numerical model of the cluster simulations (Premises S1 to S5 and C), not a hypothesis of the series about nature; it is kept with the premises so that the two simulation results show it among their conditions. Its window: the helium composition is the stored decimal estimate's only for a mirror temperature ratio $\xi = T'/T$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$ (Computation \claimref{dark-tower-matter.mirrors-composition}); at $\xi = 2.8$ to $3.2 \times 10^{-4}$ (the gravitational floor's value with the production coefficients first imported) and at the present floor, $6.6 \times 10^{-4}$, that estimate gives a neutron-rich mirror for a copied lepton number $L \leq 0$ ($96$ to $100$ and $83$ to $96$ percent neutrons) and towards the $\Neff$ cap a hydrogen-rich one, and outside the window S3 is not the stored composition. Nothing stored fixes $\xi$.

## technical
A modelling premise: mirror matter in a cluster is a fully ionised helium plasma with $\gamma = 5/3$, cooling by bremsstrahlung alone. Gas that cools below about $7 \times 10^{4}$ K becomes collisionless (the settled phase), and there is no mirror star formation and no feedback. Below about $10^{6}$ K, He$^{+}$ line cooling would in reality dominate and bring settling sooner, a cost the model records.

Type: model specification. S3 holds on the window of the mirror's temperature ratio where the stored estimate gives a helium mirror, $\xi$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$; outside it the stored composition is neutron-rich (at $\xi = 2.8$ to $3.2 \times 10^{-4}$, the floor's former value, and at the present floor, $6.6 \times 10^{-4}$) or hydrogen-rich (towards the cap), and nothing stored fixes $\xi$.

## lay
In the cluster simulations the mirror matter is a hot, fully ionised helium gas that loses heat only through the simplest radiation process. Gas that cools enough is treated as settled and no longer collides. The model has no mirror stars, so nothing heats the gas back up. It is part of the set-up of a computer model, not a claim of the theory about nature. The helium composition is what the series' own estimate gives only if the mirror world's temperature lies in a certain range, which nothing in the series fixes.

## one-liner
Model specification, valid on the window $\xi \approx 3 \times 10^{-3}$ to $2 \times 10^{-2}$ of the mirror's temperature ratio: mirror matter in clusters is modelled as a $\gamma = 5/3$ helium plasma cooling by bremsstrahlung, becoming collisionless below about $7 \times 10^{4}$ K, with no star formation and no feedback.
