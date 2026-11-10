---
id: note.synthesis.scope-of-the-quantum-field-theory-perturbative-on-a-classical-field
kind: note
version: 1
title: 'Scope of the quantum field theory: perturbative, on a classical gravitational field'
status: remark
subject: quantum-fields
proposed_by:
  kind: ai
  session: maintainer-2026-11-10
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction and the decision to record this note
- name: Claude Fable 5.2
  role: proposal and drafting
  source: maintainer pass of 2026-11-10
comments_on:
- synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants
- synthesis.one-loop-self-energy-and-vertex-extend-with-the-ward-identity-holding-at-a-common-cut-off-length
- synthesis.one-loop-qed-in-the-spacetime-algebra
- synthesis.two-loop-qed-in-the-spacetime-algebra-continued-in-dimension-gives-the-second-beta-coefficient
- synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off
- synthesis.weak-factor-rotor-lattice-strong-coupling-area-law
- synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields
- synthesis.imported-local-covariance-with-scaling-of-time-ordered-products
extraction:
  open_problem: op.qft-loops-and-renormalisation
  maintainer_pass_note:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Note added at Leon''s decision of 10 November 2026 (record the scope with neither a continuum interacting theory nor a cut-off theory with emergent covariance claimed; open no problem until one of the routes has a first computation). It changes no statement and no status. Scope: the matter and gauge sector on the classical gravitational field of Gauge Theory Gravity; the series'' position on the gravitational field itself is in the conventions, section "Gravity and the graviton". Prior art is named only where it was checked on the web on 10 November 2026: A. Jaffe, Constructive Quantum Field Theory (survey, read on the author''s site: the polynomial scalar theories in two dimensions and the quartic scalar theory in three are constructed, and the four-dimensional problem is unresolved); M. Aizenman and H. Duminil-Copin, arXiv:1912.07973, DOI 10.4007/annals.2021.194.1.3 (abstract: the scaling limit of the lattice-regulated quartic scalar field in four dimensions is Gaussian). Other constructive results, and the literature on chiral fermions on a lattice, were not checked and are not named.'
---

## formal
The quantum field theory of the series is perturbative and lives on a classical gravitational field. This note concerns the matter and gauge sector only; the gravitational gauge fields are classical throughout (conventions, section ``Gravity and the graviton''). What is stored: free Dirac and photon fields with the unit $I_{4}$ (\claimref{field-theory.second-quantisation}, \claimref{field-theory.fock-space-maxwell-modes}); tree-level exchange (\claimref{field-theory.coupled-system-tree-level}); one-loop electrodynamics with regulator fields under the Krein-form premise (\claimref{synthesis.one-loop-qed-in-the-spacetime-algebra}, \claimref{synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields}); the one-loop vacuum polarisation by extension of distributions with no regulator (\claimref{synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants}), and on the Euclidean section a pair of extensions of the one-loop self-energy and vertex obeying the Ward-Takahashi identity (\claimref{synthesis.one-loop-self-energy-and-vertex-extend-with-the-ward-identity-holding-at-a-common-cut-off-length}); the two-loop vacuum polarisation in dimensional regularisation (\claimref{synthesis.two-loop-qed-in-the-spacetime-algebra-continued-in-dimension-gives-the-second-beta-coefficient}); one S-matrix element (\claimref{synthesis.electron-positron-to-muon-pairs-in-the-spacetime-algebra-lsz-tree-cross-section-and-one-loop-unitarity}); the chiral anomaly and its cancellation per generation (\claimref{synthesis.triangle-anomaly-in-the-spacetime-algebra-is-the-pseudoscalar-part-of-the-field-square-and-cancels-per-generation}); and the imported framework of causal perturbation theory with local covariance on gravitational fields (\claimref{synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products}, \claimref{synthesis.imported-local-covariance-with-scaling-of-time-ordered-products}). Each is a coefficient of a formal power series in the couplings, with its scheme stated on it.

Nothing stored defines an interacting theory beyond that series. The series claims neither that a continuum interacting theory of its matter and gauge sector exists, nor that the physical theory is a cut-off theory in which covariance is emergent. The question should not be reopened without one of the following, none of which the store holds.
\begin{enumerate}
\item[(1)] \emph{A limit of a regulated theory.} The floors of the tower keep the charge and no boost (\claimref{synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off}). That excludes them as a covariant regulator. It does not exclude them as a cut-off whose limit is shown to be covariant. The limit and the proof of its covariance are missing.
\item[(2)] \emph{A continuum limit of the rotor lattice.} The store defines the weak factor on a lattice of rotors without gauge fixing and computes its strong-coupling expansion (\claimref{synthesis.weak-factor-rotor-lattice-strong-coupling-area-law}, \claimref{synthesis.non-abelian-gauge-fixing-has-gribov-copies-and-the-weak-rotor-lattice-with-doublets-has-a-perimeter-law}, \claimref{synthesis.a-finite-subgroup-of-colour-shares-its-strong-coupling-expansion-through-link-degree-three}). Missing: the weak-coupling limit; dynamical fermions with the series' chiral content (the stored lattice results have a frozen doublet only); the abelian factor and the scalar quartics, of which the store shows the quartics reaching strong coupling within a few TeV on one branch (\claimref{synthesis.rung-field-quartics-run-to-strong-coupling-within-a-few-tev-on-the-transmutation-branch}); the recovery of Lorentz and displacement-gauge covariance in the limit; and reflection positivity stated in the series' algebra.
\item[(3)] \emph{A positive state space beyond perturbation theory.} The Krein-form premise and the stored BRST construction are perturbative; only the gauge-invariant lattice avoids them, and it is at finite spacing.
\item[(4)] \emph{Control of the infrared.} Charged states, the adiabatic limit of causal perturbation theory, the on-shell normalisation of the electron field, and confinement in the continuum, which does not follow from the stored strong-coupling area law.
\item[(5)] \emph{Elementary or composite gauge bosons.} The tower gives anticommutation relations only (\claimref{field-theory.no-canonical-commutation-relations-tower}), and the photon is attached as an elementary Fock field; a theory built on the tower has to say which the gauge bosons are.
\end{enumerate}
Under these limits the stored loop results are to be read as the perturbative content of whatever theory exists. \emph{Prior art, as far as checked.} Interacting theories obeying the standard axioms have been constructed in two and three spacetime dimensions (the polynomial scalar theories in two, the quartic scalar theory in three), and the four-dimensional problem is unresolved (A. Jaffe, Constructive Quantum Field Theory, survey). The scaling limit of the lattice-regulated quartic scalar field in four dimensions is Gaussian (Aizenman and Duminil-Copin, arXiv:1912.07973). Both were checked on the web on 10 November 2026 at the level stated in the note of this entity; no other literature is relied on here.

## technical
pending

## lay
pending

## one-liner
The series' quantum field theory is perturbative, for matter and gauge fields on a classical gravitational field: each stored loop result is a coefficient of a formal power series with its scheme stated, and neither a continuum interacting theory nor a cut-off theory with emergent covariance is claimed; a limit of a regulated theory, a continuum limit of the rotor lattice, a positive state space beyond perturbation theory and control of the infrared are all missing.
