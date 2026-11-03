---
id: note.primer.rotation-exactly
kind: note
version: 1
title: A rotation, exactly
status: example
subject: clifford-structure
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T00, deposited version
comments_on:
- primer.commutation-rule
locators:
  paper: T00
  number: Ex 6.1
  label: ex:rotor
  line: 378
---

## formal
In the Euclidean plane of Example \claimref{note.primer.euclidean-plane}, take $R = a - b\,e_1 e_2$ with $a, b$ real, not both zero (a rotor once normalised by $\sqrt{a^2 + b^2}$; the conjugation below ignores the scale). Its reverse is $\tilde{R} = a + b\, e_1 e_2$ and $R\tilde{R} = a^{2} + b^{2}$, so $R^{-1} = \tilde{R}/(a^2 + b^2)$. Conjugating $e_1$:
\[
R\, e_1\, R^{-1} \;=\; \frac{a^{2} - b^{2}}{a^{2} + b^{2}}\, e_1 \;+\; \frac{2ab}{a^{2} + b^{2}}\, e_2 .
\]
The coefficients are the cosine and sine of the double angle of the point $(a,b)$: the rotor rotates $e_1$ towards $e_2$ by $2\arctan(b/a)$, and with $a, b$ rational every entry is exactly rational. (The sign in $R$ is the usual half-angle convention, $R = \cos\tfrac{\theta}{2} - \sin\tfrac{\theta}{2}\, e_1 e_2$; the sign is easy to get wrong, and the machine check below verifies it.) This is the half-angle representation of rotations, and it is why rotors, like quaternions, cover the rotation group twice: $R$ and $-R$ rotate identically.

## technical
pending

## lay
pending

## one-liner
pending
