# GA issues from reader R12 (tower, one-relation) for the GA rewriters

Owned entities in R12's list: one-relation.schr-odinger-slow-shadow, one-relation.dirac-current-conserved-density,
note.one-relation.setting-machine-verification, tower.compatibility-connecting-maps-transported. R12 did not edit them.

## one-relation.schr-odinger-slow-shadow
- Step (4) of the formal level writes the Pauli identity with a cross product,
  "$\mathbf{a}\mathbf{b} = \mathbf{a}\cdot\mathbf{b} + I_{3}\,\mathbf{a}\times\mathbf{b}$". The current tp check reports W222
  (a cross product) on this entity. GA form: $ab = a \cdot b + a \wedge b$ in $\Cl(3,0)$, with $a \wedge b = I_3(a \times b)$
  given only as a labelled reading if wanted. The proof's last sentence ("the Pauli identity on nine rational vector pairs")
  needs no change.
- Which unit acts where: step (3) calls Hestenes' right factor $I\sigma_3 = \gamma_2\gamma_1$ "the unit imaginary". The
  conventions name $I_4$ as the field theory's unit. Suggested sentence (R12 added the same one to
  one-relation.one-datum-not-two-imaginary-unit, technical level): the right unit $R_{I\sigma_3}$ is not $I_4$; on even spinors
  $L_{I_4} = -\Gamma R_{I\sigma_3}$ with $\Gamma\psi = I_4\psi I\sigma_3$
  (synthesis.massless-frequency-sign-relative-to-i4-is-not-the-chirality (ii)). I checked this exactly with lib/GA.py on every
  even blade of $\Cl(1,3)$.
- Checked: the Klein-Gordon square in the proof is correct: $\gamma_0 I\sigma_3\gamma_0 = I\sigma_3$ and
  $(I\sigma_3)^{-1} = -I\sigma_3$.

## one-relation.dirac-current-conserved-density
- The entity is declared `outside_ga: bridge` and is stated in a $4 \times 4$ matrix representation over
  $\mathrm{span}\{1, I_5\}$. A GA statement over the even spinors would remove the bridge: the constant real bilinears
  $\psi \Gamma \tilde\psi$, with conservation of $\psi\gamma_0\tilde\psi$ for solutions of $\nabla\psi I\sigma_3 = m\psi\gamma_0$.
  That is more than a change of notation, because the class of currents changes (sesquilinear complex against real-bilinear
  in the even algebra). It is for Leon to decide.
- Checked: the condition count $528 = 66 \cdot 4 \cdot 2$ and the "64 complex entries" are consistent. Nothing else found.

## note.one-relation.setting-machine-verification
- It was flagged for tensor notation ($\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}$, the Dirac representation in Part E). It
  describes legacy/verify_T16.py and matches that script: Part B second part lists the signatures $(1,0)$ to $(3,2)$ and
  $(0,3)$, and the "seven signatures up to $n = 5$" matches the legacy script. The store's check.py of the third-constant
  lemma tests five signatures; that is not an error in this note.
- The note also uses "twistor space" in passing (Part C). The store names that object $\CS$.

## tower.compatibility-connecting-maps-transported
- The formal level is matrix-heavy: $V_k$ is a $2 \times 2$ block matrix over $A \otimes \Mat_{2^k}(\R)$. I checked the
  mathematics against the proof and found it correct: the ground generators give $x \otimes \operatorname{diag}(-1, +1)$ on
  both sides, and the plane generators give $1 \otimes \operatorname{diag}(b, \overline\Omega_k b \overline\Omega_k^{-1})$.
  A GA restatement could give the corrector as an element of $T_{k+1}$. One candidate is the product of
  $u_A \otimes 1$ and $1 \otimes \overline\Omega_k$ with the outer plane's idempotents $vw$, $wv$, which are the matrix units
  $E_{11}$, $E_{22}$ of Fact transport.rule-1-morita-trivial. Any such restatement should keep the labelling clause.
- Its users tower.algebraic-limit-even-charge, tower.structure-tower-c-norms and synthesis.* quote $V_k$ and $W_k$. If the
  form of $V_k$ changes, their wording should follow.
