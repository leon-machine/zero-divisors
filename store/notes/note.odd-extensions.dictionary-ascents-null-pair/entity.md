---
id: note.odd-extensions.dictionary-ascents-null-pair
kind: note
version: 2
title: the dictionary with the ascent's null pair
status: remark
subject: dark-energy
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14a, deposited version
comments_on:
- odd-extensions.cosmological-constant-undetermined-within-series
- odd-extensions.transport-constrains-frozen-point-only-through
- odd-extensions.are-ascents-pair-signed
- odd-extensions.boost-dilation-ratio-gauge
locators:
  paper: T14a
  number: Rem 8.4
  label: rem:nullpair
  line: 670
extraction:
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
---

## formal
The correspondence between the frozen point and the pair the transport adjoins, stated in the root paper's normalisation (which fixes the null basis up to the dilation, one hyperbolic plane being isometric to any other). The adjoined plane has the signed basis $e_{\pm}$ and the null basis $v = \tfrac12(e_{+} + e_{-})$, $v^{*} = \tfrac12(e_{+} - e_{-})$, with $v^{2} = v^{*2} = 0$ and $vv^{*} + v^{*}v = 1$, the pair the root paper adjoins and the tower paper reads as the one fermionic mode of the rung \cite[\S 2.2]{ButlerT1}, \cite[Prop.~4.1, Thm.~4.2]{ButlerT3}. The note's canonical frame is the same two null rays, $v = I_{0}$ and $v^{*} = \varphi/2$. Then: at $\Lambda = 0$ the frozen point is the null generator $v$ itself, the zero divisor of vector type, and the direction the completion adjoins is its partner $v^{*}$, canonical by Theorem \claimref{odd-extensions.transport-constrains-frozen-point-only-through}(i); the Stelle-West vector does not exist there. For $\Lambda \neq 0$ the frozen point is a combination of both null generators,
\[
I_{\Lambda} \;=\; \alpha\, v + \beta\, v^{*}, \qquad Q(I_{\Lambda}) = \alpha\beta = \Lambda/3 ,
\]
and the Stelle-West vector is the same two components with the relative sign reversed,
\[
V \;\propto\; \alpha\, v - \beta\, v^{*}, \qquad Q(V) \propto -\alpha\beta ,
\]
orthogonal to $I_{\Lambda}$ and to the Lorentz frame. So $I$ and $V$ are the sum and difference of one pair of null components, which is why they form the signed basis up to scale and a boost (Theorem \claimref{odd-extensions.are-ascents-pair-signed}(i)); the sign of $\Lambda$ is the relative sign of $\alpha$ and $\beta$, de Sitter when they agree and anti-de Sitter when they differ, and the wall is either of them vanishing. The dilation acts as $v \mapsto tv$, $v^{*} \mapsto v^{*}/t$, an automorphism of the relation $vv^{*} + v^{*}v = 1$, and $\alpha\beta$ is its invariant (Proposition \claimref{odd-extensions.boost-dilation-ratio-gauge}); in the frame of Theorem \claimref{odd-extensions.transport-constrains-frozen-point-only-through}, $\alpha = a$ and $\beta = 2b$. In the tower paper's reading of $v$ and $v^{*}$ as the annihilation and creation operators of the rung's mode, the frozen point of a $\Lambda = 0$ universe is a pure annihilator and a nonzero $\Lambda$ is a creation component, the product of the two coefficients being $\Lambda/3$; this is what that reading says verbatim; only the vanishing of the creation component is invariant, its size being the dilation gauge, and the note attaches no claim to the reading. The script verifies the null pair, its normalisation, the identification with the canonical frame, and the norms and orthogonality of $\alpha v \pm \beta v^{*}$ on instances of both signs and zero.

## technical
pending

## lay
pending

## one-liner
pending
