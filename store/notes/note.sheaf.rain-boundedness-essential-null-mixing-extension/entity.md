---
id: note.sheaf.rain-boundedness-essential-null-mixing-extension
kind: note
version: 1
title: 'Rain-boundedness is essential: a null-mixing extension'
status: example
subject: walls
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
comments_on:
- obj.sheaf.extensions
- sheaf.uniqueness-weighted-module
locators:
  paper: T04
  number: Ex 8.19
  label: ex:nullmix
  line: 1065
---

## formal
Work on an angular chart and set $C := \tfrac12\sqrt{m^2 - u^2}$, $D := -\,m u^2/(2C)$, both $u$-smooth with $C(0) = m/2$. The module $\mathcal{M}'$ with frame
\[
\alpha = du + C\,d\theta, \qquad \beta = \dtPG + D\,d\theta, \qquad \gamma = u^4\,d\theta, \qquad \mu_2
\]
is a locally free rank-four extension in the sense of Definition \claimref{obj.sheaf.extensions}: its Gram extends smoothly to $E$, with
\[
\begin{gathered} G(\alpha,\alpha) = G(\alpha,\beta) = 0, \qquad G(\beta,\beta) = -\,\frac{u^2}{m^2 - u^2}, \\ G(\alpha,\gamma) = -C, \qquad G(\beta,\gamma) = -D, \qquad G(\gamma,\gamma) = -u^4 , \end{gathered}
\]
all exact. At the boundary the Gram has rank three with smooth radical spanned by $\beta$ (nonvanishing eigenvalues $\pm m/2$ from the $(\alpha,\gamma)$-pair and $-1$ from $\mu_2$), so (T2$\partial$) holds; and $\det G_{\mathcal{M}'} = -\,r/4$ exactly, so the dying eigenvalue is first-order in $r$ and (T3$\partial$) holds. Yet $\mathcal{M}' \neq \shW$: neither contains the other ($\alpha \notin \shW$, its rain component $\alpha(V) = -m/2u^2$ diverging; $\rho \notin \mathcal{M}'$). The mechanism is the null mixing of Remark \claimref{note.sheaf.bounded-norm-alone-does-not-characterise}, and it shows the rain-bounded hypothesis of Theorem \claimref{sheaf.uniqueness-weighted-module} is necessary, not technical. All displayed identities are verified exactly (Section \ref{sec:verification}).

## technical
pending

## lay
pending

## one-liner
pending
