---
id: synthesis.residual-s2-decouples-first-family-from-ckm-and-pmns
kind: claim
version: 1
title: Couplings that respect the residual $S_{2}$ share the odd eigenvector $(1,-1,0)$ in every mass matrix, quark and lepton, so one row and one column of each mixing matrix are trivial; when that state is the lightest in both sectors of a pair, as the stored textures make it for the leptons, $V_{us} = V_{ub} = V_{cd} = V_{td} = 0$ and $\theta_{12} = \theta_{13} = 0$; a second stage must break $S_{2}$ in the charged-fermion couplings, and the single residual-$S_{2}$ $120$ cannot supply it
status: proved
region: synthesis
subject: neutrinos
tags: [flavour-and-mixing, symmetry-breaking, no-go, seesaw-and-majorana]
proposed_by:
  kind: ai
  session: 2026-10-24-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
derivations:
- name: main
  uses:
  - synthesis.residual-s2-fixes-120-family-form@1
  - neutrino.breaking-relation@3
  - neutrino.invariant-symmetric-matrices@2
  - standard-model.imported-clebsch-structure-seesaw@1
  - standard-model.imported-spinor-bilinears@1
  - synthesis.solar-angle-light-plane-sum-rule@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_s2_invariant_matrices_share_the_odd_eigenvector
- kind: check
  ref: check.py::check_pati_salam_textures_with_s2_couplings_decouple_first_family
- kind: check
  ref: check.py::check_stored_s3_to_s2_textures_are_s2_invariant_with_a_null
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.residual-s2-fixes-120-family-form
  - synthesis.theta23-at-s3-s2-direction
extraction:
  open_problem: op.second-order-breaking
  note: >-
    One statement of the residual-S2 lemma for both mixing matrices, with the seesaw included so
    that the lepton side is covered; the quark side is the same algebra, and the companion result on
    a second doublet of one family coupling (filed alongside, synthesis.second-doublet-of-one-family-coupling-gives-no-quark-mixing)
    cites it for the common-eigenvector step. At the S3 -> S2 direction both neutrino kernels are
    (1,-1,0), which is this lemma at leading order. What it does to the open problem: its second
    line of attack, "with one 120, whose single family matrix is fixed by
    synthesis.residual-s2-fixes-120-family-form, fit the lopsided second stage once and compute all
    three PMNS angles and the CKM numbers", cannot work as phrased, because that 120 respects the
    residual S2 and every S2-respecting set of couplings leaves one family unmixed in both matrices;
    the 120's family form is fixed only at the S2 stage, and the second stage must carry S2-odd
    entries in the charged-fermion couplings themselves. With the stored sum rule, at the order of
    the breaking lemma and under Premise (H), this makes the second stage S2-odd and lopsided. Which
    mass eigenstate the odd direction is (the lightest, for the stored lepton textures) is an input
    to the labels, not to the lemma. Linear algebra on 3 x 3 family matrices; transport-absent.
---
## formal
Let $P$ be the exchange of $e_{1}$ and $e_{2}$, the residual $S_{2}$ of the $S_{3} \to S_{2}$ direction $e_{3}e_{3}^{\mathsf T}$ of Lemma \claimref{neutrino.breaking-relation}, acting on family matrices by $X \mapsto PXP$, and let $a = (1,-1,0)$ span its odd line and $b_{1} = (1,1,0)$, $b_{2} = e_{3}$ its even plane, as in Proposition \claimref{synthesis.residual-s2-fixes-120-family-form}. Call a matrix $S_{2}$-invariant when $PXP = X$.
\begin{enumerate}
\item[(i)] \emph{(The odd eigenvector.)} The $S_{2}$-invariant complex matrices form a five-dimensional algebra, closed under products, adjoints, transposes and inverses, and every member has $a$ as an eigenvector, $Xa = (X_{11} - X_{12})\,a$, with no coupling between $a$ and the even plane. Hence if the Yukawa matrices of the $10$s, the $126$ and the $120$ are $S_{2}$-invariant, then for arbitrary complex vevs and $120$ coefficients the Dirac matrices $M_{u}, M_{d}, M_{e}, M_{\nu}$ and the Majorana matrix $M_{R}$ of Fact \claimref{standard-model.imported-clebsch-structure-seesaw}, the Hermitian squares $M M^{\dagger}$ and the seesaw matrix $m_{\nu} = -M_{\nu}M_{R}^{-1}M_{\nu}^{\mathsf T}$ are all $S_{2}$-invariant and have $a$ as a common eigenvector.
\item[(ii)] \emph{(Both mixing matrices.)} When the eigenvalue of $a$ is simple in each Hermitian square (the generic case once the second stage has lifted the degeneracies; at a degenerate eigenvalue the mixing is undetermined, the leading-order situation), every diagonalising unitary has $a$ as a column up to phase, so the CKM and the PMNS matrix each have one entry of modulus one with its row and column otherwise zero, and vanishing Jarlskog invariant: one row and one column of each mixing matrix are trivial. Which row and column is an extra input, the position of $a$ in each mass ordering; its eigenvalue $X_{11} - X_{12}$ need not be the smallest. When $a$ is the lightest state in both sectors of a pair, which it is for the leptons at the $S_{2}$ stage ($a$ is a null vector of $M_{D}$ and of $M_{e}$ there, Proposition \claimref{synthesis.residual-s2-fixes-120-family-form}(ii)), the trivial row and column are the first: $U_{e2} = U_{e3} = U_{\mu 1} = U_{\tau 1} = 0$, that is $\theta_{12} = \theta_{13} = 0$, and with the same ordering for the quarks $V_{us} = V_{ub} = V_{cd} = V_{td} = 0$, with the $2$-$3$ mixing free in each; any other position of $a$ puts the zeros in another row and column, equally excluded by the record.
\item[(iii)] \emph{(What the second stage must do.)} A second stage $S_{2} \to 1$ whose charged-fermion and neutrino couplings all respect $S_{2}$ produces neither the Cabibbo angle nor $\theta_{12}$, $\theta_{13}$. The $120$ whose family form is fixed by Proposition \claimref{synthesis.residual-s2-fixes-120-family-form}(ii), the line $(e_{1} + e_{2})\wedge e_{3}$, is $S_{2}$-invariant and annihilates $a$, so it is not a second stage: the family form is fixed only at the $S_{2}$ stage, and the second stage must carry $S_{2}$-odd entries in the charged-fermion couplings themselves (an $S_{2}$-odd Majorana sector with $S_{2}$-invariant Dirac couplings, $w_{u} = w_{d} = 0$ for the $126$, changes $m_{\nu}$ and no charged square). Since one-type $S_{2}$-odd stages are excluded by the solar sum rule at the order of Lemma \claimref{neutrino.breaking-relation} and under Premise (H) (Proposition \claimref{synthesis.solar-angle-light-plane-sum-rule}), under those two conditions the second stage must be $S_{2}$-odd and lopsided.
\item[(iv)] \emph{(Instances; computed, exact.)} For $S_{2}$-invariant complex Yukawas with generic complex vevs and $120$ coefficients, all nine matrices of (i) commute with $P$, have $a$ as an eigenvector with no coupling to the even plane, and the eigenvalue of $a$ is simple in $H_{u}, H_{d}, H_{e}, m_{\nu}$ and $m_{\nu}m_{\nu}^{\dagger}$ ($H_{e}a = 205\,a$ in the instance); adding one $S_{2}$-odd entry $\tfrac13\,e_{1}\wedge e_{3}$ to the $120$ couples $a$ to the even plane in $H_{e}$, $H_{d}$ and $m_{\nu}$. The stored textures $M_{D} = d(\J + \delta\,e_{3}e_{3}^{\mathsf T})$, $M_{R} = \alpha\Pi + M_{3}\J/3 + \varepsilon\,e_{3}e_{3}^{\mathsf T}$, $M_{e} = \J + \delta_{c}\,e_{3}e_{3}^{\mathsf T}$ are $S_{2}$-invariant, with $a$ a null vector of $M_{D}$, $M_{e}$ and $m_{\nu}$ and $M_{R}a = \alpha a$.
\end{enumerate}

## technical
The neutrino paper breaks the family symmetry in two stages, $S_{3} \to S_{2} \to 1$, and the store fixes the family form of the $120$ coupling at the first stage: the one antisymmetric matrix invariant under the residual exchange of the first two families, which couples the second and third and leaves the first alone. This lemma says what every coupling that respects that exchange has in common: the odd direction $(1,-1,0)$ is an eigenvector of each of them, and the property survives products, adjoints, inverses and the seesaw. So if the $10$s, the $126$ and the $120$ all respect the residual $S_{2}$, that direction is an exact mass eigenstate in every sector at once, up quarks, down quarks, charged leptons and light neutrinos, and it cannot mix: one row and one column of the CKM matrix and of the PMNS matrix are trivial, and only a $2 \times 2$ mixing remains in each. Where the odd direction sits in the mass ordering is a separate input; for the leptons the stored textures make it the lightest, so the Cabibbo angle, $V_{ub}$, $\theta_{12}$ and $\theta_{13}$ are the entries that vanish. The quark half of the statement is the same algebra; at the $S_{3} \to S_{2}$ direction the lepton half is the observation that both neutrino kernels are $(1,-1,0)$. For the open problem the consequence is sharp: the second stage of breaking cannot be the $S_{2}$-respecting $120$ with its fixed family form; it must put $S_{2}$-odd entries into the charged-fermion couplings, and the solar sum rule, at the breaking lemma's order and under Premise (H), then makes it lopsided.

## lay
The series builds the pattern of quark and lepton masses by breaking a symmetry among the three families in two steps. After the first step one symmetry is left, swapping the first two families, and the framework's preferred new ingredient respects it. This result shows that if the couplings in every sector respect that swap, they leave one combination of families, "first minus second", exactly unmixed with the other two: the swap picks it out, and every product and inverse that enters, including the seesaw that gives the light neutrinos their masses, preserves it. For the leptons the stored textures make that combination the lightest family, so the Cabibbo angle and two of the three neutrino mixing angles would be exactly zero, which they are not. The second step must therefore break the swap itself in the couplings of the quarks and charged leptons; the preferred ingredient, as fixed by the first step, is not that second step.

## one-liner
The $S_{2}$-invariant family matrices form an algebra closed under products, adjoints, inverses and the seesaw in which $(1,-1,0)$ is a common eigenvector, so $S_{2}$-respecting $10$, $126$ and $120$ couplings leave one row and one column of the CKM and of the PMNS matrix trivial and $J = 0$; with that state the lightest in both sectors, as the stored lepton textures make it, $V_{us} = V_{ub} = V_{cd} = V_{td} = 0$ and $\theta_{12} = \theta_{13} = 0$; the residual-$S_{2}$ $120$ is therefore not a second stage, which must carry $S_{2}$-odd charged-fermion couplings, lopsided by the solar sum rule at the breaking lemma's order and under Premise (H).
