# Run 2026-11-08-frozen-point-datum: report

Target: op.frozen-point-rational-datum (logged this run). Since the foundation postulates of 7 November place the series'
scalars in Q until the completion F4, a frozen-point construction that needs sqrt(Lambda/3) holds over Q only for special
Lambda. Method: agent S (theorem and store sweep), three restaters (stopped, see below), blind referee F, fixes, close-out.

## Accepted
- synthesis.frozen-point-datum-is-h (referee F: SOUND WITH FIXES; fixes applied). Over any field K of characteristic 0:
  everything rational in Lambda holds as written; the static boost's null eigen-directions and unit, R_h and kappa, the
  observer's horizon point, the isometry of I-perp with <1,-1,-1,-1,-1>, Cl(I-perp) = Cl(1,4) and the mirror's Cl(4,1) each
  hold exactly when Lambda/3 is a square in K, and all hold with Lambda = 3H^2, H in K; counterexamples over Q (Lambda = 7/3:
  no rational point on the bifurcation sphere, by descent; Lambda = 6); constructions with their own conditions (a sphere
  point iff d is a sum of three squares; a similarity onto the standard (1,4) space iff d is a sum of two squares; the
  mirror complexified iff -d is not a square; the sqrt|Lambda| rescaling needs sqrt 3; the anti-de Sitter side needs H'; the
  operator join needs sqrt 2). Its extraction note lists the stored results affected on a rational reading (42 needing H,
  five needing more, three physical magnitudes) and how the list was compiled.
- store/conventions.md, Notation: "The frozen point's datum": results are stated over R; on a rational reading the datum is
  H, Lambda = 3 eps H^2 (H' on the anti-de Sitter side).
- op.frozen-point-rational-datum moved to open_problems_settled.yaml.

## Leon's decisions (8 November)
1. The datum is H (Lambda = 3H^2); then, on the sweep: Lambda = 3 eps H^2; group labels by hypothesis; extra conditions stated;
   45 restatements plus 19 wording rewrites.
2. Revised after the restatement cost became clear ("choosing H as the datum is adding too much overhead"): keep every
   stored result as stated over R, record the dependence once (the theorem's note) and by one convention line, and rewrite
   nothing. The three restaters were stopped; their eight finished drafts are set aside outside the store and the proposal
   queue; the one maintainer restatement (the MacDowell-Mansouri import) was reverted. The sweep table
   (findings/sweep.md) stays in the run folder in case a full restatement is wanted later.

## Checks
Baseline (store at 12e45eb) 0 errors 0 warnings. The theorem: check4 exit 0 with no findings, validate ok. Final check 0 errors 0
warnings; build 0 errors (2287 entities, 7230 edges); layout, site, lock; 393 tests OK.

## Costs (approximate subagent tokens)
Agent S 417k, referee F 185k, restaters (stopped) not totalled.
