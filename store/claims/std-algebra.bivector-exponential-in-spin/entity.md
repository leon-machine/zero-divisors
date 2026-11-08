---
id: std-algebra.bivector-exponential-in-spin
kind: claim
version: 2
title: 'Exponentials of bivectors are rotors; the Lorentzian exceptions'
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- rotors-and-stabilisers
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.std-algebra.rotor
- obj.std-algebra.pin-spin
- obj.std-algebra.clifford-group
derivations:
- name: main
  uses:
  - std-algebra.involution-properties@1
  - std-algebra.bivector-lie-algebra@1
  - std-algebra.cartan-dieudonne@2
  - primer.twisted-adjoint-action@4
  - primer.centre@3
  - primer.sign@3
  - std-algebra.spin-double-cover@1
  - std-algebra.bivector-exponential@4
  - std-algebra.inverse-of-vector@1
  - std-algebra.complex-clifford-algebra@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_series_identities_for_general_bivectors
- kind: check
  ref: check.py::check_series_identities_over_the_complex_numbers
- kind: check
  ref: check.py::check_terminating_exponentials_are_spin_plus
- kind: check
  ref: check.py::check_lorentzian_rotors_and_the_non_exponential
- kind: check
  ref: check.py::check_degenerate_exponential_is_not_a_versor
locators:
  sources:
  - key: Lounesto2001
    locator: Ch. 17 (spin groups; exponentials of bivectors)
  - key: DoranLasenby2003
    locator: 'Ch. 4 (foundations of geometric algebra: rotors, versors)'
  - key: HestenesSobczyk1984
    locator: Ch. 3 (versors, rotors and the bivector algebra)
extraction:
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 2: a uses edge to std-algebra.complex-clifford-algebra@1 for the complex clause of (ii), whose proof needs the Clifford algebra over C and its blade basis (part (i) there), now cited by claimref; content unchanged.'
  open_problem: op.bivector-exponential-spin
---

## formal
Let $(V, Q)$ be a quadratic space over $\R$ or over $\C$ (any signature; (i) and (ii) include degenerate forms, (iii) needs a nondegenerate real form), $B \in \Cl^{2}(V, Q)$ any bivector, and $e^{B} = \sum_{k \ge 0} B^{k}/k!$, which converges absolutely in the finite-dimensional algebra. Write $\operatorname{ad}_B(y) = By - yB = 2\, B \times y$.
\begin{enumerate}
\item[(i)] $e^{B}$ is even, $(e^{B})^{\sim} = e^{-B}$ and $e^{B} e^{-B} = 1$; so $e^{B} (e^{B})^{\sim} = 1$, and $e^{sB} e^{tB} = e^{(s+t)B}$.
\item[(ii)] For every vector $x$, $e^{B} x e^{-B} = \sum_{k \ge 0} \operatorname{ad}_B^{k}(x)/k! \in V$, and $x \mapsto e^{B} x e^{-B}$ is an isometry of $(V, Q)$.
\item[(iii)] If the field is $\R$ and $Q$ is nondegenerate, then $e^{B} = u_1 \cdots u_{2j}$ with $Q(u_i) = \pm 1$ and $\prod_i Q(u_i) = +1$: $e^{B}$ is a rotor (\claimref{obj.std-algebra.rotor}), $e^{B} \in \Spin^{+}(V, Q)$, and $x \mapsto e^{B} x e^{-B}$ lies in $\mathrm{SO}^{+}(V, Q)$. For degenerate $Q$, $e^{B}$ need not be a versor: in $\Cl(0,0,2)$ every vector is null, so the only versor is $1$, while $e^{f_1 f_2} = 1 + f_1 f_2$.
\item[(iv)] (Lorentzian case.) In $\Cl(1,3)$ with pseudoscalar $I$, the even scalars $\C_I = \operatorname{span}\{1, I\}$ form a field isomorphic to $\C$, central in $\Cl^{+}$, every bivector has $B^{2} \in \C_I$, and every element of $\Cl^{+}$ with $R\tilde R = 1$ is $R = s + F$ with $s \in \C_I$, $F \in \Cl^{2}$, $s^{2} - F^{2} = 1$. Such an $R$ is the exponential of a bivector if and only if it is not of the form $-(1 + N)$ with $N$ a nonzero bivector of square $0$. Hence every rotor of $\Cl(1,3)$ is $e^{B}$ or $-e^{B}$, and $-(1 + (\gamma_0 + \gamma_1)\gamma_2)$ is a rotor that is not an exponential.
\end{enumerate}

## technical
The exponential of an arbitrary bivector, not only one whose square is a number, is a rotor in every nondegenerate real signature. Its reverse is its inverse because reversion negates bivectors, and conjugating a vector by it gives the exponential of the bivector's commutator action, which keeps vectors vectors because that action maps vectors to vectors. The resulting isometry factors into reflections, and comparing the exponential with the product of the reflecting vectors leaves only a scalar, fixed by the norm. The first two statements hold over the complex numbers and for degenerate forms as well. For the spacetime algebra the exponential map misses exactly the rotors minus one plus a null bivector, so every rotor is plus or minus an exponential there.

## lay
Every rotation, boost or combination of them generated smoothly from the identity is a rotor, however tangled the plane of motion. In spacetime one family of rotors, a null rotation combined with a full turn, is not the exponential of any plane element (it lies on no one-parameter subgroup), although its negative is. When some directions are null and orthogonal to everything, the exponential can fail to be a product of reflections at all.

## one-liner
For every bivector $B$, $(e^{B})^{\sim} = e^{-B}$ and $e^{B} x e^{-B} = e^{\operatorname{ad}_B}x \in V$; for nondegenerate real $Q$, $e^{B} \in \Spin^{+}$ is a rotor; in $\Cl(1,3)$ a rotor is an exponential iff it is not $-(1 + N)$, $N^{2} = 0 \ne N$.
