# Items for AP2 (from AP1)

Entities AP2 claimed in claimed-apply.txt on which AP1 has a decided item (DECISIONS.md; Leon's answer 1: apply all
of A, G, H). Apply in your version bump and record each in your maintainer_pass_decisions note.

## A10. sheaf.wall-class, clause (b) (formal and technical; Leon's answer 7 "fix the clock wording")
- Defect: (b) says each iteration transfers the invariant "while shifting both clock coordinates by the rung" (formal
  statement paragraph and the "Conjecture:" paragraph of the technical level: "with both clock coordinates shifted by the
  rung"). The rung (+1,+1) leaves d = p - q mod 8 unchanged ((p+1) - (q+1) = p - q); tower.rigidity-clock-frozen and
  synthesis.wall-class-one-rung-obstruction say the same.
- Fix: formal (b) "... each iteration transferring it to the next shadow wall, the rung shifting both signatures by (1,1)
  and leaving both clock positions unchanged"; technical (b) "... passing to each shadow wall, the rung shifting both
  signatures by (1,1) and leaving both clock positions unchanged". AP1 has added the dated bracket to
  note.sheaf.wall-class-posed (v2), which points to "Conjecture sheaf.wall-class (b) now states".

## H5 (notation, routine). synthesis.normality-on-the-closed-generator-gives-the-vacuum-folium-not-the-ground-state
- Defect (ga-issues-R02 item 2): proof (i) names the composite inversion rotor `J` and uses `nu` for the vector with
  nInf = nu + e_-; in this subject J is the boundary-mode unit (U2) and J_a the modular conjugations, nu the null
  translations.
- Fix: rename the rotor (for example $R_{\mathrm{inv}}$) and the vector (for example $e_{+}$ if that is what it is), or
  add one sentence saying what J and nu denote in this proof. No content change.
