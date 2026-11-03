---
id: note.correspondence.isomorphism-witt-pair
kind: note
version: 2
title: "The isomorphism on the Witt pair"
status: example
subject: conformal-spacetime
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
comments_on:
- correspondence.spinor-identification
- correspondence.chevalley-pairing
locators:
  paper: T09
  number: Ex 3.5
  label: ex:psi
  line: 416
extraction:
  source_title: "The isomorphism on the Witt pair"
  source_formal: |-
    Take $\nO := w_1$ and $\nInf := w_1'$, a Witt pair of $V_\C$ ($\ip{\nO}{\nInf} = 1$, both null); Section \ref{sec:incidence} arranges the real Witt pair of $V$ on this model. Then $c(w_1)$ maps the $\T'$-basis to $\sqrt2\,(w_{12}, w_{13})$ on $w_2, w_3$ and annihilates $w_1, w_{123}$; pairing through $B$ gives $G_{w_1}(w_3, w_2) = \sqrt2 = -G_{w_1}(w_2, w_3)$ and all other entries zero, so $\Psi(w_1) = -\sqrt2\,t_2\wedge t_3$: a simple bivector, whose plane is $\operatorname{span}(t_2, t_3) = \operatorname{span}(w_3\wedge w_1,\ w_1\wedge w_2)$, the even blades containing $w_1$. Likewise $c(w_1') = \sqrt2\,\iota_{w_1'}$ sends $w_1 \mapsto \sqrt2\cdot 1$ and $w_{123}\mapsto \sqrt2\,w_{23}$, giving $\Psi(w_1') = \sqrt2\,t_0\wedge t_1$ with plane $\operatorname{span}(1,\ w_2\wedge w_3)$. In both cases the plane of $\Psi(v)$ is the image $c(v)\T'$, equivalently the kernel of $c(v)|_\T$. This description of the line of a null vector is general: for nonzero null $v$ the antisymmetric form $G_v$ has rank $2$ (it is nonzero and simple), so $c(v)|_{\T'}$ has rank $2$ and its kernel $R_v$ is the radical of $G_v$; the plane of the bivector $\Psi(v) \in \Lambda^2\T \cong \Lambda^2(\T'^{\,*})$ is the annihilator of $R_v$, which contains $c(v)\T'$ (as $B(s, c(v)s_2) = B(c(v)s, s_2) = 0$ for $s \in R_v$) and has the same dimension $2$; and $c(v)\T' \subseteq \ker c(v)|_\T$ because $c(v)^2 = 0$, with equality since $c(v)|_\T$ is the $B$-transpose of $c(v)|_{\T'}$ (Lemma \claimref{correspondence.chevalley-pairing}(3)) and so also has rank $2$.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistor and dual twistor space to \\CS and \\CSm only; no other twistor wording."
---

## formal
Take $\nO := w_1$ and $\nInf := w_1'$, a Witt pair of $V_\C$ ($\ip{\nO}{\nInf} = 1$, both null); Section \ref{sec:incidence} arranges the real Witt pair of $V$ on this model. Then $c(w_1)$ maps the $\CSm$-basis to $\sqrt2\,(w_{12}, w_{13})$ on $w_2, w_3$ and annihilates $w_1, w_{123}$; pairing through $B$ gives $G_{w_1}(w_3, w_2) = \sqrt2 = -G_{w_1}(w_2, w_3)$ and all other entries zero, so $\Psi(w_1) = -\sqrt2\,t_2\wedge t_3$: a simple bivector, whose plane is $\operatorname{span}(t_2, t_3) = \operatorname{span}(w_3\wedge w_1,\ w_1\wedge w_2)$, the even blades containing $w_1$. Likewise $c(w_1') = \sqrt2\,\iota_{w_1'}$ sends $w_1 \mapsto \sqrt2\cdot 1$ and $w_{123}\mapsto \sqrt2\,w_{23}$, giving $\Psi(w_1') = \sqrt2\,t_0\wedge t_1$ with plane $\operatorname{span}(1,\ w_2\wedge w_3)$. In both cases the plane of $\Psi(v)$ is the image $c(v)\CSm$, equivalently the kernel of $c(v)|_\CS$. This description of the line of a null vector is general: for nonzero null $v$ the antisymmetric form $G_v$ has rank $2$ (it is nonzero and simple), so $c(v)|_{\CSm}$ has rank $2$ and its kernel $R_v$ is the radical of $G_v$; the plane of the bivector $\Psi(v) \in \Lambda^2\CS \cong \Lambda^2(\CSm^{\,*})$ is the annihilator of $R_v$, which contains $c(v)\CSm$ (as $B(s, c(v)s_2) = B(c(v)s, s_2) = 0$ for $s \in R_v$) and has the same dimension $2$; and $c(v)\CSm \subseteq \ker c(v)|_\CS$ because $c(v)^2 = 0$, with equality since $c(v)|_\CS$ is the $B$-transpose of $c(v)|_{\CSm}$ (Lemma \claimref{correspondence.chevalley-pairing}(3)) and so also has rank $2$.

## technical
pending

## lay
pending

## one-liner
pending
