---
id: families.doublet-direction-module-georgi-jarlskog-clebsch
kind: claim
version: 6
title: The $126$ doublet direction in the module, and the Georgi-Jarlskog Clebsch
status: proved
region: families
subject: generations
tags: [flavour-and-mixing, representation-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
review: typed
derivations:
- name: main
  uses:
  - families.imported-decomposition-grade-dictionary@1
  - standard-model.hyp-s-slot-statistics@10
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_t_gj_pure_grade_five
- kind: check
  ref: check.py::check_georgi_jarlskog_entries
- kind: check
  ref: check.py::check_one_sided_weighting_antisymmetric
- kind: check
  ref: check.py::check_up_type_twin
- kind: proof
  derivation: main
locators:
  paper: T13
  number: Prop 8.1
  label: prop:126
  line: 900
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: T_GJ pure grade five in Cl(5,5) with its closed form and the 126bar half killing the sixteen; the Clebsch entries, symmetry and hypercharge of its form; the antisymmetric one-sided weighting; the up-type twin. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 5 -> 6.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'The grade-dictionary edge is a real premise and was kept; the Georgi-Jarlskog ratio in (ii)
      agrees with the standard 126 Clebsch (standard-model.imported-clebsch-structure-seesaw), but that
      import covers only the ratio and not the grade-five operator statement, so no standard-route derivation
      was added. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics added because its statement
      holds under Hypothesis (S) (clauses (ii) and (iv)). Levels pass: the lay level now states Hypothesis
      (S) for the species-level clauses, which it had dropped; the technical level carries (S) explicitly
      onto the up-type clause (iv).'
    added:
    - standard-model.hyp-s-slot-statistics
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Let $\chi := -(-1)^{N_{R}}$, which is $+1$ on the doublet sector $N_{R} = 1$ and $-1$ on the singlet sectors $N_{R} \in \{0, 2\}$, and let
\[
T_{\mathrm{GJ}} \;:=\; w_{4}\,(B - L)\,\chi .
\]
Then:
\begin{enumerate}
\item[(i)] $B - L = -\tfrac23\sum_{i \le 3} v_{i}\wedge w_{i}$ is pure grade two, $w_{4}\,\chi = w_{4}(1 - 2n_{5}) = -2\,w_{4}\,(v_{5}\wedge w_{5})$, and
\[
T_{\mathrm{GJ}} \;=\; \tfrac43\; w_{4}\wedge (v_{5}\wedge w_{5}) \wedge \Bigl(\sum_{i\le 3} v_{i}\wedge w_{i}\Bigr),
\]
a pure grade-five element of the Clifford algebra of the ten, with no grade-one and no grade-three component; hence, by Fact \claimref{families.imported-decomposition-grade-dictionary}, it has no $10$ and no $120$ component, and the mass form it induces on the sixteen is the $126$ component of $16 \otimes 16$, the $\overline{126}$ part of the grade-five space acting as zero on the sixteen;
\item[(ii)] under Hypothesis (S), which supplies the species names, $Y_{T_{\mathrm{GJ}}}$ is symmetric, conserves hypercharge, and is nonzero exactly on $(L, e^{c})$ with entries $-1$ and on $(Q, d^{c})$ with entries $\pm\tfrac13$, in the normalisation in which the $10$ form $Y_{w_{4}}$ has entries $\pm1$ on the same pairs; writing $y_{e}$, $y_{d}$ for the entries of $Y_{T_{\mathrm{GJ}}}$ on $(L, e^{c})$ and $(Q, d^{c})$, the ratio $|y_{e}/y_{d}| = 3$ is Georgi-Jarlskog's, and it is the ratio of the lepton doublet's to the quark doublet's $B - L$;
\item[(iii)] the one-sided weighting $w_{4}(B - L)$ without $\chi$ is antisymmetric on every coupled pair and contributes no one-family mass, because every Yukawa pair is $B - L$ neutral, $(B-L)(L) + (B-L)(e^{c}) = 0 = (B-L)(Q) + (B-L)(d^{c})$;
\item[(iv)] under Hypothesis (S) as in (ii), the up-type direction $v_{4}(B - L)\chi$ has a symmetric mass form coupling $(L, \nu^{c})$ with modulus $1$ and $(Q, u^{c})$ with modulus $\tfrac13$, so that $|m_{\nu}^{D}| = 3\,|m_{u}|$ on the $126$ direction; the signed entries are $+1$ on $(L, \nu^{c})$ and $\pm\tfrac13$ on $(Q, u^{c})$, the sign depending on the colour of the pair, so the relation is one of magnitudes.
\end{enumerate}

## technical
With $\chi = -(-1)^{N_{R}}$, equal to $+1$ on the doublet sector and $-1$ on the singlets, the operator $T_{\mathrm{GJ}} = w_{4}(B - L)\chi$ equals $\tfrac43\,w_{4} \wedge (v_{5} \wedge w_{5}) \wedge \sum_{i \le 3} v_{i} \wedge w_{i}$, a pure grade-five element of the Clifford algebra of the ten. By the grade dictionary it has no $10$ or $120$ component, so its mass form on the sixteen is the $126$ component of $16 \otimes 16$.

Under Hypothesis (S) for the species names the form is symmetric, conserves hypercharge, and is nonzero exactly on $(L, e^{c})$ with entries $-1$ and on $(Q, d^{c})$ with entries $\pm\tfrac13$, so $|y_{e}/y_{d}| = 3$, the Georgi-Jarlskog ratio, which is the ratio of the lepton doublet's to the quark doublet's $B - L$. Without $\chi$ the weighting $w_{4}(B - L)$ is antisymmetric on every coupled pair and gives no one-family mass, since every Yukawa pair is $B - L$ neutral. Under (S) likewise, the up-type twin $v_{4}(B - L)\chi$ gives $|m_{\nu}^{D}| = 3|m_{u}|$, a relation of magnitudes since the signs on $(Q, u^{c})$ depend on colour.

## lay
In the simplest unified theories the electron and the down quark come out with equal masses unless an extra ingredient supplies a factor of three, a well-known observation of Georgi and Jarlskog. This result finds, inside the paper's one-generation algebra, a specific operator that sits in the representation physicists already associate with that factor. Assuming Hypothesis (S), which lets the algebra's slots be read as named particles, the operator supplies exactly the factor of three between the electron and down-quark entries, and a simpler version without its sign factor gives no mass to a single family at all. Under the same hypothesis a companion operator gives the same factor of three between neutrino and up-quark masses, in size only.

## one-liner
The operator $w_{4}(B - L)\chi$ is pure grade five, so its mass form on the sixteen lies in the $126$, and under Hypothesis (S) it gives the Georgi-Jarlskog ratio $|y_{e}/y_{d}| = 3$.
