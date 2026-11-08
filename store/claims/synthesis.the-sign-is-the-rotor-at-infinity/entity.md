---
id: synthesis.the-sign-is-the-rotor-at-infinity
kind: claim
version: 1
title: 'The sign is the rational rotor at infinity; the path to it has length $\pi$'
status: proved
region: synthesis
subject: clifford-structure
tags: [rotors-and-stabilisers, needs-continuum, limits]
proposed_by:
  kind: ai
  session: 2026-11-08-ga-deck
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal, proof and drafting
  source: run 2026-11-08-ga-deck
review: draft
founded_on:
- synthesis.continuum-completion-premise@2
lineage:
  motivated_by:
  - std-algebra.complex-numbers
  - std-algebra.spin-double-cover
  - std-algebra.bivector-exponential
derivations:
- name: main
  uses:
  - synthesis.division-gives-the-rationals@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_rational_rotors_are_rotors
- kind: check
  ref: check.py::check_composition_is_tangent_addition_with_infinity
- kind: check
  ref: check.py::check_bijection_onto_the_rational_rotor_circle
- kind: check
  ref: check.py::check_the_full_turn_is_the_sign_and_fixes_vectors
- kind: check
  ref: check.py::check_speed_and_half_circle
- kind: check
  ref: check.py::check_length_brackets_pi
- kind: proof
  derivation: main
extraction:
  note: >-
    From Leon's working document "From the Bit to the Numbers" (7 November 2026), Step 5: "Rational
    rotors compose rationally (t = (t1 + t2)/(1 - t1 t2) for t = tan(theta/2)) ... pi is the length of
    the path from the identity to the rotor -1, which is itself just the sign bit of Step 2. The sign
    is algebraic; the distance to it is transcendental." Proved here in the form the Zero Divisors
    site's "Why geometric algebra" deck cites: the rational rotors of a plane are parametrised by the
    projective line Q together with infinity, composition is tangent addition, and the sign -1 is the
    rotor at the point at infinity, the same completion the transport principle's first slides make
    for 1/0. Clauses (i) to (iii) use only the rational Clifford algebra (Premises (F1) to (F3) and
    division, synthesis.division-gives-the-rationals); clause (iv) uses Premise (F4). Not part of the
    claim, and classical (cited from memory): pi is irrational (Lambert, 1761) and transcendental
    (Lindemann, 1882), so the length of the path to the sign is not reached by the rational algebra.
    The rational parametrisation of the circle is classical (Diophantus; the Weierstrass substitution).
    Ledger: transport-absent.
---

## formal
Let $\Cl_{\Q}(2,0)$ be the rational Clifford algebra of the plane (Theorem \claimref{synthesis.division-gives-the-rationals}), $B = e_{1}e_{2}$, so $B^{2} = -1$, and $U_{\Q} = \{a + bB : a, b \in \Q,\ a^{2} + b^{2} = 1\}$. For $t \in \Q$, $1 + tB$ is invertible with $(1 + tB)^{-1} = (1 - tB)/(1 + t^{2})$; put
\[
R_{t} = (1 - tB)(1 + tB)^{-1} = \frac{(1 - t^{2}) - 2t\,B}{1 + t^{2}}, \qquad R_{\infty} = -1 .
\]
\begin{enumerate}
\item[(i)] \emph{(Rational rotors.)} Each $R_{t}$ lies in $U_{\Q}$, so $R_{t}\widetilde{R_{t}} = 1$, and $v \mapsto R_{t}v\widetilde{R_{t}}$ maps the rational vectors $V_{\Q}$ to themselves preserving $Q$. $R_{0} = 1$, $R_{1} = -B$ (the half turn, $v \mapsto -v$), $R_{\infty} = -1$.
\item[(ii)] \emph{(Composition is tangent addition.)} $R_{s}R_{t} = R_{s \oplus t}$ on $\Q \cup \{\infty\}$, where $s \oplus t = (s + t)/(1 - st)$ for $st \ne 1$, $s \oplus t = \infty$ for $st = 1$, $\infty \oplus t = t \oplus \infty = -1/t$ for $t \ne 0, \infty$, $\infty \oplus 0 = \infty$ and $\infty \oplus \infty = 0$.
\item[(iii)] \emph{(The sign is the rotor at infinity.)} $t \mapsto R_{t}$ is a group isomorphism from $(\Q \cup \{\infty\}, \oplus)$ onto $U_{\Q}$, with inverse $a + bB \mapsto -b/(1 + a)$ for $a \ne -1$ and $-1 \mapsto \infty$. The sign $-1$, the residue of two distinctions passing each other (Premise (F2)), is the rotor at the point at infinity of the parameter line. As a map of vectors it is the full turn, $R_{\infty}v\widetilde{R_{\infty}} = v$, while the rotor itself is $-1$.
\item[(iv)] \emph{(The path to the sign has length $\pi$.)} Over $\R$ (Premise (F4)), with $|a + bB|^{2} = \langle (a + bB)(a + bB)^{\sim}\rangle_{0} = a^{2} + b^{2}$ on the even part, the curve $t \mapsto R_{t}$, $t \in [0, \infty)$, closed by $R_{\infty}$, traces the half of the unit circle of the even part with $b \le 0$ exactly once, from $1$ to $-1$, with speed $|dR_{t}/dt| = 2/(1 + t^{2})$. Its length is therefore half the length of the unit circle, $\pi$, and $\pi = \int_{0}^{\infty} 2\,dt/(1 + t^{2})$.
\end{enumerate}

## technical
In the rational algebra of the plane, the unit bivector $B$ squares to $-1$, and the Cayley form $R_{t} = (1 - tB)/(1 + tB)$ gives a rotor for every rational $t$, with rational coefficients. Every rational rotor arises this way, composition is the tangent addition law $(s + t)/(1 - st)$, and the parameter needs one extra point, $t = \infty$, which gives the rotor $-1$. So the sign bit of the foundation is the rotor at the point at infinity of a projective line, completed exactly as the transport principle completes the line for $1/0$. Acting on vectors that rotor is a full turn, which does nothing, while the rotor itself is $-1$: the spinor sign. The sign is reached algebraically, but the distance to it is not: over the reals the path of rotors from $1$ to $-1$ is half the unit circle, of length $\pi$, and $\pi$ is irrational (classical, not proved here). The continuum enters at exactly that step.

## lay
Turning something round in a plane can be done entirely with fractions: every rotation by a "rational" amount is described by one fraction $t$, and doing two rotations one after the other combines their fractions by a simple rule. One rotor is missing from the fractions, the one that turns everything by a full circle, and it sits at "$t$ = infinity", the same point at infinity that makes $1/0$ meaningful elsewhere on this site. That rotor is $-1$: a full turn leaves every arrow where it was, yet the algebra remembers it as minus one, the sign that electrons and other spinning particles are known to pick up. Getting to it is algebraic; measuring how far it is takes $\pi$, which no fraction equals.

## one-liner
In $\Cl_{\Q}(2,0)$ the rotors $R_{t} = (1 - tB)/(1 + tB)$, $t \in \Q$, with $R_{\infty} = -1$, are exactly the rational rotors, compose by $s \oplus t = (s + t)/(1 - st)$, and put the sign $-1$ (the full turn) at the point at infinity of the parameter; over $\R$ the path from $1$ to $-1$ is half the unit circle, of length $\pi = \int_{0}^{\infty} 2\,dt/(1 + t^{2})$.
