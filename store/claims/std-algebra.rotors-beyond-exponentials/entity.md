---
id: std-algebra.rotors-beyond-exponentials
kind: claim
version: 3
title: Rotors that are not plus or minus an exponential when min(p, q) >= 2
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
- name: Claude Opus 5.5
  role: 'consistency pass, the (2,2) volume element no longer written I_4'
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
review: draft
about:
- obj.std-algebra.rotor
- obj.std-algebra.pin-spin
derivations:
- name: main
  uses:
  - std-algebra.bivector-lie-algebra@1
  - std-algebra.bivector-exponential@4
  - std-algebra.orthogonal-anticommute@1
  - std-algebra.bivector-exponential-in-spin@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_split_rotor_has_simple_negative_eigenvalue
- kind: check
  ref: check.py::check_exponential_rotors_have_even_negative_multiplicity
- kind: check
  ref: check.py::check_low_dimensions
locators:
  sources:
  - key: Lounesto2001
    locator: Ch. 17 (spin groups; exponentials of bivectors)
  - key: DoranLasenby2003
    locator: 'Ch. 4 (foundations of geometric algebra: rotors, versors)'
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3. Unit-name clash: the proof of (ii) called e_1e_2e_3e_4 of a (2,2) block I_4, the store''s reserved name for the spacetime pseudoscalar gamma_0gamma_1gamma_2gamma_3 (square -1); this element squares to +1 (exact check in scratch). Renamed omega_4. Mathematics unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 2: a uses edge to std-algebra.bivector-exponential-in-spin@2, whose clause (ii) supplies the series identity Ad_{e^B} = exp(ad_B) on V that (i) rests on, and whose clause (iv) is the Lorentzian case of the closing remark; the text citations are now claimrefs. Content unchanged.'
  open_problem: op.bivector-exponential-spin
  note: 'Answers the clause "state when a rotor is an exponential" outside the Lorentzian case, in one direction: min(p, q) >= 2 is shown sufficient for a rotor that is not plus or minus an exponential. The converse (every rotor is plus or minus an exponential when min(p, q) <= 1) is not proved here; it is consistent with the Lorentzian case, std-algebra.bivector-exponential-in-spin clause (iv) and, cited from memory, with Nishikawa 1983 (exp onto SO_0(p, q) exactly when min(p, q) <= 1). The negative-eigenvalue lemma is the easy half of the criterion for a real matrix to have a real logarithm (Culver 1966, cited from memory; the half used is proved here). Literature cited from memory and not used in the proof: for definite Q and n >= 2 every rotor is an exponential (the exponential map of a compact connected Lie group is onto), and for min(p, q) = 1, n >= 3, every rotor is plus or minus an exponential (the exponential map of SO+(1, n) is onto, lifted through the kernel of the double cover).'
---

## formal
Let $(V, Q)$ be a nondegenerate real quadratic space of signature $(p, q)$, $n = p + q$, and write $\Ad_R(x) = R x R^{-1}$ for even $R$.
\begin{enumerate}
\item[(i)] For every bivector $B$, every negative real eigenvalue of $\Ad_{e^{B}}$ on $V$, and so of $\Ad_{-e^{B}} = \Ad_{e^{B}}$, has even algebraic multiplicity. (Here $\Ad_{e^{B}} = \exp(X)$ with $X = \operatorname{ad}_{B}|_{V}$ a real linear map of $V$, the series identity of \claimref{std-algebra.bivector-exponential-in-spin}(ii).)
\item[(ii)] (A sufficient condition.) If $p \ge 2$ and $q \ge 2$, let $e_1, e_2, e_3, e_4$ be orthonormal with $Q(e_1) = Q(e_2) = 1$ and $Q(e_3) = Q(e_4) = -1$, and
\begin{equation}
R \;=\; -\,e_1 e_2 e_3 e_4 \bigl(\tfrac54 + \tfrac34\, e_1 e_3\bigr) .
\end{equation}
Then $R$ is a rotor ($R$ is a product of six unit vectors and $R\tilde R = 1$), and $\Ad_R$ has the eigenvalues $-4$ and $-\tfrac14$ on $\operatorname{span}(e_1, e_3)$, $-1$ on $e_2$ and $e_4$, and $1$ on $\{e_1, \dots, e_4\}^{\perp}$. Since $-4$ is a simple eigenvalue, neither $R$ nor $-R$ is the exponential of any bivector. So for every signature with $\min(p, q) \ge 2$, among them the conformal algebra $\Cl(2,4)$ and the split algebras $\Cl(k,k)$ with $k \ge 2$, the rotors are not all of the form $\pm e^{B}$.
\item[(iii)] (Low dimensions.) For $n = 1$ there are no nonzero bivectors and $-1$ is a rotor; in $\Cl(1,1)$ the rotors are $a + b\,e_1e_2$ with $a^{2} - b^{2} = 1$, every exponential $e^{\lambda e_1 e_2} = \cosh\lambda + \sinh\lambda\, e_1 e_2$ has $a \ge 1$, and $-1$ is a rotor. In both cases $-1$ is a rotor that is not an exponential, although every rotor is $\pm e^{B}$.
\end{enumerate}

## technical
Conjugating a vector by the exponential of a bivector is the exponential of the bivector's commutator action on vectors, a real linear map. The exponential of a real matrix can have a negative eigenvalue only from a pair of complex conjugate eigenvalues of the exponent, so every negative eigenvalue of such a conjugation comes with even multiplicity. In any signature with at least two positive and two negative directions, the rotor $R = -e_1e_2e_3e_4(\tfrac54 + \tfrac34 e_1e_3)$ acts on vectors with the simple eigenvalue $-4$ (a boost by the factor $4$ composed with the reversal of a $(2,2)$-plane), so neither $R$ nor $-R$ is an exponential. In dimension one and in $\Cl(1,1)$ the rotor $-1$ is not an exponential, although every rotor is plus or minus an exponential. Only one direction is shown: two positive and two negative directions suffice for a rotor that is not plus or minus an exponential; that fewer never allow one is not proved here.

## lay
Every rotation or boost written as the exponential of a plane element is an allowed rotor, but the converse can fail. When the space has at least two time-like and two space-like directions, there are rotors that cannot be written as an exponential even after flipping their overall sign. One such rotor combines a boost with a half-turn of a four-dimensional block; the boost factor appears exactly once with a minus sign among the stretch factors, and an exponential can only produce such negative factors in pairs. The conformal algebra used for twistors, with two plus and four minus directions, is of this kind.

## one-liner
$\Ad_{e^{B}}$ has every negative eigenvalue with even multiplicity, so whenever $\min(p, q) \ge 2$ the rotor $-e_1e_2e_3e_4(\tfrac54 + \tfrac34 e_1e_3)$ is neither $e^{B}$ nor $-e^{B}$; in $n = 1$ and $\Cl(1,1)$ the rotor $-1$ is no exponential.
