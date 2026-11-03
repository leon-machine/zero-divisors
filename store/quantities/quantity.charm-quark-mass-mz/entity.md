---
id: quantity.charm-quark-mass-mz
kind: quantity
version: 1
title: Running mass of the charm quark at the Z mass
status: measured
subject: standard-quantities
programme: standard
proposed_by:
  kind: ai
  session: maintainer-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
quantity:
  symbol: m_{c}(M_{Z})
  value: '0.619'
  uncertainty: '0.084'
  units: 'GeV'
  dimension: mass
  source:
    citation: Z.-z. Xing, H. Zhang and S. Zhou, Updated values of running quark and lepton masses, Phys.
      Rev. D 77 (2008) 113016
    key: XingZhangZhou2008
    doi: 10.1103/PhysRevD.77.113016
    locator: 'Table II, running quark masses at mu = M_Z'
  date: '2008'
  note: 'Running MS-bar mass at mu = M_Z, Table II of the source (one set of six, shared by every result that quotes running quark masses at M_Z). Value, uncertainty and table checked against arXiv:0712.1419v3 on 2026-10-26; the journal reference is that of the DOI.'
---

## formal
$m_{c}(M_{Z}) = 0.619 \pm 0.084$ GeV, the $\overline{\mathrm{MS}}$ charm-quark mass run to $\mu = M_{Z}$ \cite{XingZhangZhou2008}.

## technical
pending

## lay
The mass of the charm quark as it appears at the energy of the Z boson, after the running of quark masses with energy.

## one-liner
$m_{c}(M_{Z}) = 0.619$ GeV.
