---
id: obj.transport.extension-quadratic-spaces
kind: object
version: 1
title: Extension of quadratic spaces
status: defined
region: transport
subject: completion
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
review: typed
locators:
  paper: T01
  number: Def 2.3
  label: def:extension
  line: 501
extraction:
  env: definition
  context_refs:
  - transport.no-go-level-elements
  typing:
    by: ai-typing-pass
    note: "Definition; levels explain it and its automatic orthogonal splitting."
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: [rungs.imported-totality-minimality-completion, transport.cohomological-form-no-go, transport.transport-principle, transport.type-p-self-repairing, rungs.fact-null-momenta-invite-one-rung]
    added_about: []
    verdict: connected
    note: 'About from the statements that quantify over every extension of the base quadratic space.'
---

## formal
An \emph{extension} of the nondegenerate quadratic space $(\mathbb{V}, Q)$ is a real quadratic space $(\mathbb{V}', Q')$ with $\mathbb{V} \subseteq \mathbb{V}'$ and $Q'|_{\mathbb{V}} = Q$. The form $Q'$ is not assumed nondegenerate. Because $Q$ is nondegenerate on $\mathbb{V}$, the extension splits orthogonally and automatically: $\mathbb{V}' = \mathbb{V} \perp \mathbb{V}^{\perp}$, where $\mathbb{V}^{\perp} = \{ a \in \mathbb{V}' : a \cdot x = 0 \ \forall x \in \mathbb{V}\}$ \cite{Lam2005}. Extensions in this sense are exactly the ``ascents'' quantified over in Theorem \claimref{transport.no-go-level-elements}.

## technical
An extension of a nondegenerate quadratic space $(\mathbb{V}, Q)$ is a real quadratic space $(\mathbb{V}', Q')$ with $\mathbb{V} \subseteq \mathbb{V}'$ and $Q'|_{\mathbb{V}} = Q$; the form $Q'$ may be degenerate. Because $Q$ is nondegenerate on $\mathbb{V}$, every extension splits orthogonally, $\mathbb{V}' = \mathbb{V} \perp \mathbb{V}^\perp$.

These extensions are exactly the ascents over which the element-level no-go result quantifies.

## lay
An extension places a space with a notion of length inside a larger space whose notion of length agrees with the original on the original vectors. The larger space is allowed to have directions of zero length. Because the original space is nondegenerate, the larger one always splits into the original plus a part perpendicular to it.

## one-liner
An extension of a nondegenerate quadratic space is any real quadratic space, possibly degenerate, that contains it with the same form on it, and it always splits as the original space plus its orthogonal complement.
