import io
def edit(path, reps):
    s = open(path).read()
    for a, b in reps:
        assert s.count(a) == 1, (path, s.count(a), a[:70])
        s = s.replace(a, b)
    open(path, 'w').write(s)

P1 = 'proposals/synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product/'
P2 = 'proposals/synthesis.eviction-keeps-one-replica-saddle/'
P3 = 'proposals/synthesis.eviction-keeps-one-of-catalan-many-replica-saddles/'
AVG = r"x \mapsto \tfrac12(x + \Gamma x\Gamma)"

edit(P1 + 'entity.md', [
 # fix 1
 ("counterexample, the product rule (v), the proof that the Catalan limit is unchanged with the weight 4^g, the\n    bounds, and the mean entropy of a sector with its exact difference from the imported value. Prior art, cited",
  "counterexample, the product rule (v), the proof that the Catalan limit is unchanged with the weight 4^g, the\n    bounds, and, for the mean entropy, the rational difference Delta from the imported value with its bounds and\n    the comparison with the stored deficit bounds (the closed form of the sector mean entropy itself is not new,\n    see below). The lemma of clause (vi) stays inline for now and is to be cut to a citation of the\n    finite-averages result named above after acceptance. The result derives, in the algebra, the content of the\n    imported Fact descent-lift.imported-fermionic-operations-are-even-reduced for mode algebras (the reduced\n    state is the restriction to the subsystem's algebra, agrees with the partial trace for even states, products\n    with an even factor exist) and sharpens it (the reduction to A is a partial trace for every state; the other\n    reduction differs exactly on listed odd blades); whether its dependants drop the import is a maintainer\n    decision. The stored theorem singularity.descent-parity-average is stated for one mode; the uses edge is for\n    that one-mode case only, and the total-parity average used here is a definition. Prior art, cited"),
 ("and Wolf 2007; Friis, Lee and Bruschi 2013); the mean entanglement entropy of random fermionic states with a\n    conserved parity or number has been computed in the literature (Bianchi, Hackl, Kieburg, Rigol and Vidmar,\n    2022), where the closed form of (vii) may already appear; nothing is imported from these.",
  "and Wolf 2007; Friis, Lee and Bruschi 2013; Bravyi and Kitaev 2002 and Araki and Moriya 2003, the sources of\n    the imported Fact just named). Prior art checked on the web (first third of the paper read): Bianchi, Hackl,\n    Kieburg, Rigol and Vidmar, Volume-law entanglement entropy of typical pure quantum states, arXiv:2112.06959,\n    whose general direct-sum formula (equation (45) there) gives (vii) as its two-block case; rederived here\n    from Page's Fact. Nothing is imported from these."),
 # fix 2 formal
 (r"and \emph{even} if $\Gamma\rho = \rho\Gamma$, that is, if the parity average $\tfrac12(\rho + \Gamma\rho\Gamma)$ of Theorem \claimref{singularity.descent-parity-average} fixes it.",
  r"and \emph{even} if $\Gamma\rho = \rho\Gamma$, that is, if it is fixed by $" + AVG + r"$, the average of Theorem \claimref{singularity.descent-parity-average} with the total parity $\Gamma$ in place of the single-mode $\sigma$; that theorem is stated for one mode and the $\ell$-mode form is a definition here."),
 # fix 2 technical
 ("So for even states, the only ones left after the descent's parity average, both reductions",
  "So for even states, the states fixed by the total-parity average, both reductions"),
 # fix 3
 ("and the mean entropy is larger than Page's by a rational amount close to $1/(2mn)$.",
  "and the mean entropy is larger than Page's by a rational amount between $1/(2mn)$ and $1/(2mn) + 1/(2n^{2})$, about $3/(4m^{2})$ at the crossing."),
 # fix 5
 (r"($\tfrac12$ against $\tfrac13$ at $m = n = 2$; $\tfrac{271}{280}$ at $m = n = 4$)",
  r"(sector value $\tfrac12$ against the Fact's $\tfrac13$ at $m = n = 2$, $\Delta = \tfrac16$; sector value $\tfrac{271}{280}$ at $m = n = 4$, $\Delta = \tfrac{6553}{144144}$)"),
 # fix 6
 (r"mean entropy $\sum_{k=n/2+1}^{mn/2}1/k - (m-2)/(2n)$.",
  r"mean entropy $\sum_{k=n/2+1}^{mn/2}1/k - (m-2)/(2n)$ (moments from the imported all-moment Fact applied to a sector, entropy from Page's imported average on two blocks)."),
 ("and only small corrections change, by amounts given exactly.",
  "and only small corrections change, by amounts given exactly, using two textbook averages the collection holds as imports."),
 ("The mean entropy uses Page's Fact on the two blocks of a sector; the moment formula uses the imported all-moment Fact on the sector.",
  "The mean entropy uses Page's Fact on the two blocks of a sector and is the two-block case of a known formula for random states on a direct sum of tensor products; the moment formula uses the imported all-moment Fact on the sector. Both are conditional on those imports."),
 # fix 7
 (r"Hence the state of Theorem \claimref{singularity.eviction-window-thermal-product-radiation-entropy} is a pure even state, its window is",
  r"Reading the pairs of Theorem \claimref{singularity.eviction-window-thermal-product-radiation-entropy} as these pair states, its state is a pure even state, its window is"),
 # fix 8
 (r"Theorem \claimref{synthesis.eviction-keeps-one-replica-saddle}: (i), (ii), (v) unchanged;",
  r"Theorem \claimref{synthesis.eviction-keeps-one-replica-saddle} at version 3: (i), (ii), (v) unchanged;"),
 (r"Theorem \claimref{synthesis.eviction-keeps-one-of-catalan-many-replica-saddles}: (i), (ii) unchanged;",
  r"Theorem \claimref{synthesis.eviction-keeps-one-of-catalan-many-replica-saddles} at version 3: (i), (ii) unchanged;"),
])
edit(P1 + 'proof-main.tex', [
 (r"\emph{(iv).} Evenness is invariance under the parity average of Theorem \claimref{singularity.descent-parity-average}, taken with the involution $\Gamma$.",
  r"\emph{(iv).} Evenness is invariance under $" + AVG + r"$, the average of Theorem \claimref{singularity.descent-parity-average} with the total parity $\Gamma$ in place of the single-mode $\sigma$; that theorem is stated for one mode, and the $\ell$-mode form is a definition here (applied mode by mode it would erase the coherence of the pair state of (v), which is odd in one mode alone)."),
 (r"The state of Theorem \claimref{singularity.eviction-window-thermal-product-radiation-entropy} is the product of such pair states",
  r"Reading the pairs of Theorem \claimref{singularity.eviction-window-thermal-product-radiation-entropy} as these pair states, its state is the product of such pair states"),
 (r"the stated bounds on $\Delta$.",
  r"the stated bounds on $\Delta$ (the upper one is below $\tfrac{1}{2mn} + \tfrac{1}{2n^{2}}$). The closed form is the two-block case of a known formula for random states on a direct sum of tensor products (note); it is rederived here from the Fact."),
])

edit(P2 + 'entity.md', [
 ("    by: ai-2026-11-09-bridges\n", "    by: ai-contributor\n"),
 ("and the random-state value of clauses (iii), (iv) was the one for such a product; the modes are fermionic, the states left by the parity average are even and lie in one parity sector,",
  "and the random-state value of clauses (iii), (iv) was the one for such a product; the modes are fermionic, the states fixed by the total-parity average are even and lie in one parity sector,"),
 ("Leading terms and every eviction-side clause are unchanged.'",
  "Leading terms and every eviction-side clause are unchanged. The claimref to synthesis.imported-haar-average-purity is removed from the proof.'"),
 ("Version 3 -> 4, at Leon's request that the tensor product",
  "Version 3 -> 4, at Leon's request (his decision of 9 November 2026) that the tensor product"),
 ("Lubkin''s Haar purity at clause (iii) (synthesis.imported-haar-average-purity) and",
  "Lubkin''s Haar purity at clause (iii) (synthesis.imported-haar-average-purity; through version 3; removed at version 4) and"),
 ("and the Haar purity the\n    Fact synthesis.imported-haar-average-purity. The",
  "and the Haar purity the\n    Fact synthesis.imported-haar-average-purity (through version 3; removed at version 4). The"),
 (r"that is, they are fixed by the parity average of Theorem \claimref{singularity.descent-parity-average}.",
  r"that is, they are fixed by $" + AVG + r"$, the total-parity form of the single-mode average of Theorem \claimref{singularity.descent-parity-average}."),
 ("for the even states that survive the parity average the two give the same reduced states",
  "for the even states, those fixed by the total-parity average, the two give the same reduced states"),
])
edit(P2 + 'proof-main.tex', [
 (r"so it is a pure even state, fixed by the parity average of Theorem \claimref{singularity.descent-parity-average}.",
  r"so, reading the pairs of that theorem as these pair states, it is a pure even state, fixed by $" + AVG + r"$, the total-parity form of the single-mode average of Theorem \claimref{singularity.descent-parity-average}."),
 (r"the window state is the product of its members' thermal marginals, which on the split is",
  r"the window state is the product of its members' thermal marginals, which, reading the pairs of that theorem as the pair states of (e), is on the split"),
])

edit(P3 + 'entity.md', [
 ("    by: ai-2026-11-09-bridges\n", "    by: ai-contributor\n"),
 ("the states of the modes left by the parity average are even and lie in one parity sector,",
  "the even states (fixed by the total-parity average) lie in one parity sector,"),
 ("used only to name the index-two value, is dropped.'",
  "used only to name the index-two value, is dropped. The upper bound C_n d^{1-n} on the abstract average, stated without qualification at version 3, was proved there only in the form C_n d^{1-n} + (n! - C_n) d^{-n-1} and verified for n = 2, 3, 4, d = 2, 4, 8; the clause now says so.'"),
 ("Version 3 -> 4, at Leon's request that the tensor product",
  "Version 3 -> 4, at Leon's request (his decision of 9 November 2026) that the tensor product"),
 (r"lies strictly between $d^{1-n}$ and $C_{n}d^{1-n}$ ($n = 2, 3, 4$, $d = 2, 4, 8$ verified), and satisfies",
  r"exceeds $d^{1-n}$ and is below $C_{n}d^{1-n} + (n! - C_{n})d^{-n-1}$ (proved), is below $C_{n}d^{1-n}$ for $n = 2, 3, 4$, $d = 2, 4, 8$ (verified), and satisfies"),
 ("and the Haar average reproduces the planar value at large dimension.",
  "and the Haar average reproduces the planar value at large dimension, as does the average on a parity sector."),
])
edit(P3 + 'check.py', [
 ('''def check_parity_sector_moments_keep_the_catalan_limit():
''', '''def check_parity_sector_moments_keep_the_catalan_limit():
    """Partial: the sector trace count is enumerated at three cases only (n = 2 with d = 2, 4; n = 3 with
    d = 2); the count for every n is the proof's argument over F_2. The genus form, the Catalan limit and the
    bounds are evaluated for n = 2..6, d = 2..32."""
'''),
])
