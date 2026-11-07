---
id: angle.imported-theorems-deliver-their-hypotheses
kind: claim
version: 3
title: 'Imported: the theorems that deliver $2\pi$, and their hypotheses'
status: imported
region: angle
subject: thermality
tags: [classical-theorem, modular-theory, hawking-temperature]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-angle, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: 'unit resolution pass, the modular group written with the unit I_4 of span{1, I_4}'
  version: 3
  source: maintainer pass 2026-11-07 (resolve units)
review: typed
imported_from:
- citation: J. J. Bisognano and E. H. Wichmann, On the duality condition for a Hermitian scalar field,
    J. Math. Phys. 16 (1975), 985--1007.
  key: BW1975
- citation: J. J. Bisognano and E. H. Wichmann, On the duality condition for quantum fields, J. Math.
    Phys. 17 (1976), 303--321.
  key: BW1976
- citation: H.-J. Borchers, The CPT-theorem in two-dimensional theories of local observables, Commun.
    Math. Phys. 143 (1992), 315--332.
  key: Borchers1992
- citation: P. D. Hislop and R. Longo, Modular structure of the local algebras associated with the free
    massless scalar field theory, Commun. Math. Phys. 84 (1982), 71--85.
  key: HislopLongo1982
- citation: R. Brunetti, D. Guido and R. Longo, Modular structure and duality in conformal quantum field
    theory, Commun. Math. Phys. 156 (1993), 201--219.
  key: BGL1993
- citation: 'G. L. Sewell, Quantum fields on manifolds: PCT and gravitationally induced thermal states,
    Ann. Phys. 141 (1982), 201--224.'
  key: Sewell1982
- citation: B. S. Kay and R. M. Wald, Theorems on the uniqueness and thermal properties of stationary,
    nonsingular, quasifree states on spacetimes with a bifurcate Killing horizon, Phys. Rep. 207 (1991),
    49--136.
  key: KayWald1991
- citation: W. G. Unruh, Notes on black-hole evaporation, Phys. Rev. D 14 (1976), 870--892.
  key: Unruh1976
locators:
  paper: T05-angle
  number: Fact 1.3
  label: fact:BW
  line: 124
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U4 with U1: Borchers'' dilation relation for the modular group of an abstract von Neumann algebra on a complex Hilbert space is restated with the Hilbert space''s scalars read in span{1, I_4}, Delta^{I_4 t}; the sources write i for I_4, and the original formal level is kept in source_formal. Status stays imported; the declaration is removed.'
  source_formal: 'For a Wightman field theory in Minkowski space, the modular group of the algebra of a wedge with respect to the vacuum is the one-parameter group of boosts preserving the wedge, with modular parameter $t$ corresponding to rapidity $2\pi t$, and the modular conjugation is the CPT operator composed with the rotation by $\pi$ about the boost axis, which acts on spacetime as the wedge reflection $(x^{0}, x^{1}) \mapsto (-x^{0}, -x^{1})$; the hypotheses are the spectrum condition (positivity of the energy-momentum), Poincar\''e covariance and locality. The abstract form: if a von Neumann algebra $M$ with cyclic separating vector $\Omega$ carries a one-parameter unitary group $U(a)$ with positive generator, $U(a)\Omega = \Omega$ and $U(a)MU(a)^{*} \subseteq M$ for $a \geq 0$, then the modular group of $(M, \Omega)$ acts on the translations as the dilation $\Delta^{it}U(a)\Delta^{-it} = U(e^{-2\pi t}a)$. For the free massless field the modular groups of the wedge and double-cone algebras are geometric, and for a conformal net on the circle the modular group of an interval''s algebra is the M\"obius flow fixing the interval''s endpoints, again at $2\pi$. On a spacetime with a bifurcate Killing horizon the same mechanism gives the Hawking temperature for states regular across the horizon, and a stationary quasi-free state that is regular is unique and KMS at $\kappa/2\pi$. \emph{Provenance:} \cite{BW1975, BW1976}; \cite{Borchers1992}; \cite{HislopLongo1982, BGL1993}; \cite{Sewell1982, KayWald1991}; the Rindler case \cite{Unruh1976}.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (imported): Borchers'' theorem and the Bisognano-Wichmann modular groups Delta^{it} are quoted as their sources state them, on the Hilbert space of a general von Neumann algebra.'
  env: fact
  typing:
    by: ai-typing-pass
    note: Imported literature bundle; no edges to review.
---

## formal
For a Wightman field theory in Minkowski space, the modular group of the algebra of a wedge with respect to the vacuum is the one-parameter group of boosts preserving the wedge, with modular parameter $t$ corresponding to rapidity $2\pi t$, and the modular conjugation is the CPT operator composed with the rotation by $\pi$ about the boost axis, which acts on spacetime as the wedge reflection $(x^{0}, x^{1}) \mapsto (-x^{0}, -x^{1})$; the hypotheses are the spectrum condition (positivity of the energy-momentum), Poincar\'e covariance and locality. The abstract form: if a von Neumann algebra $M$ with cyclic separating vector $\Omega$ carries a one-parameter unitary group $U(a)$ with positive generator, $U(a)\Omega = \Omega$ and $U(a)MU(a)^{*} \subseteq M$ for $a \geq 0$, then the modular group of $(M, \Omega)$ acts on the translations as the dilation $\Delta^{I_{4}t}U(a)\Delta^{-I_{4}t} = U(e^{-2\pi t}a)$, numbers and the Hilbert space's complex structure being read in $\mathrm{span}\{1, I_{4}\}$ (the sources write $i$ for $I_{4}$). For the free massless field the modular groups of the wedge and double-cone algebras are geometric, and for a conformal net on the circle the modular group of an interval's algebra is the M\"obius flow fixing the interval's endpoints, again at $2\pi$. On a spacetime with a bifurcate Killing horizon the same mechanism gives the Hawking temperature for states regular across the horizon, and a stationary quasi-free state that is regular is unique and KMS at $\kappa/2\pi$. \emph{Provenance:} \cite{BW1975, BW1976}; \cite{Borchers1992}; \cite{HislopLongo1982, BGL1993}; \cite{Sewell1982, KayWald1991}; the Rindler case \cite{Unruh1976}.

## technical
The Bisognano-Wichmann theorem: for a Wightman field theory in Minkowski space, the modular group of the algebra of a wedge with respect to the vacuum is the group of boosts preserving the wedge, with modular parameter $t$ at rapidity $2\pi t$, and the modular conjugation acts on spacetime as the wedge reflection $(x^{0}, x^{1}) \mapsto (-x^{0}, -x^{1})$. Its hypotheses are the spectrum condition, Poincaré covariance and locality.

Borchers' abstract form: if a von Neumann algebra $M$ with cyclic separating vector $\Omega$ carries a unitary group $U(a)$ with positive generator, fixing $\Omega$ and with $U(a)MU(a)^{*} \subseteq M$ for $a \geq 0$, then $\Delta^{I_{4}t}U(a)\Delta^{-I_{4}t} = U(e^{-2\pi t}a)$, with the Hilbert space's complex unit read as $I_{4}$. The same factor $2\pi$ appears for the wedge and double-cone algebras of the free massless field, for interval algebras of a conformal net on the circle, and on spacetimes with a bifurcate Killing horizon, where a stationary quasi-free state that is regular is unique and KMS at $\kappa/2\pi$.

## lay
These are the standard theorems of quantum field theory that produce the factor $2\pi$ behind the Unruh and Hawking temperatures. They say that when energy is positive and the theory respects relativity and locality, the natural internal clock of the region on one side of a horizon is the horizon's boost, running at a fixed rate. The entry records their hypotheses, since those are what any attempt to use them must supply.

## one-liner
Under the spectrum condition, covariance and locality, the modular flow of a wedge or half-sided algebra is the boost at rate $2\pi$, and a regular stationary quasi-free state at a bifurcate Killing horizon is KMS at $\kappa/2\pi$.
