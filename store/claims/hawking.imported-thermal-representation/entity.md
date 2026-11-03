---
id: hawking.imported-thermal-representation
kind: claim
version: 2
title: 'Imported: the thermal representation'
status: imported
region: hawking
subject: thermality
tags: [classical-theorem, car-algebra, modular-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T07, deposited version
review: typed
imported_from:
- citation: H. Araki and W. Wyss, Representations of canonical anticommutation relations, Helv. Phys.
    Acta 37 (1964), 136--159.
  key: ArakiWyss1964
- citation: O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2, 2nd
    ed., Springer, Berlin (1997).
  key: BratteliRobinson1997
  locator: \S 5.3
about:
- obj.hawking.continuum-mode-space
locators:
  paper: T07
  number: Fact 4.3
  label: fact:arakiwyss
  line: 553
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: Imported literature result; no edges to review.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants: []
    added_about:
    - obj.hawking.continuum-mode-space
    verdict: standalone
    note: Literature import stated for orientation; only the remark on free-fermion thermal field theory
      and Israel's double draws on it, and no other paper cites it.
---

## formal
The GNS representation of $\CAR(\mathfrak{h})$ in the state $\omega_I$ is the Araki-Wyss representation: a doubled Fock space carrying two commuting copies of the CAR, with the GNS vector entangling them pairwise and the modular operator of the GNS vector implementing exactly the flow $\tau$ at inverse temperature $\beta$. \emph{Provenance:} Araki-Wyss \cite{ArakiWyss1964}; textbook form \cite[\S 5.3]{BratteliRobinson1997}.

## technical
The GNS representation of $\CAR(\mathfrak{h})$ in the I-state $\omega_{I}$ is the Araki-Wyss representation. It acts on a doubled Fock space carrying two commuting copies of the CAR, the GNS vector entangles the two copies pairwise, and the modular operator of that vector implements exactly the flow $\tau$ at inverse temperature $\beta$.

## lay
A thermal state of fermions can be represented as a single pure state of two copies of the system, entangled pair by pair. In that representation the state's natural internal time evolution is exactly the physical time evolution at the given temperature. This is a standard result of quantum statistical mechanics.

## one-liner
The GNS representation of the CAR algebra in the I-state is the Araki-Wyss doubled Fock representation, whose modular flow is $\tau$ at inverse temperature $\beta$.
