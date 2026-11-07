import sys; sys.path.insert(0,'/home/claude/phys-graph/lib')
exec(open('unit.py').read().split('# --- 1.')[0])
print("4. commutant of the whole transport (hyperbolic) subalgebra inside the tower level Cl(N, N+2)")
for N in (1,2):
    sq,K,planes=build(N); n=len(sq)
    hyp=[gen(i) for i in range(2,n)]
    blades=[b for k in range(n+1) for b in itertools.combinations(range(n),k)]
    commut=[b for b in blades if all(GA.commutes({b:F(1)},g,sq) for g in hyp)]
    Gam=sc(1)
    for (p,m) in planes: Gam=mul(Gam,mul(gen(p),gen(m),sq),sq)
    J=mul(gen(0),gen(1),sq); u1=mul(Gam,gen(0),sq); u2=mul(Gam,gen(1),sq)
    expect=sorted([(),(0,1)]+[list(u1.keys())[0],list(u2.keys())[0]])
    quat = all(eq(mul(x,x,sq),sc(-1)) for x in (J,u1,u2)) and eq(mul(J,u1,sq),u2) or eq(mul(J,u1,sq),neg(u2))
    even=[b for b in commut if len(b)%2==0]
    chk(f"N={N}: commutant blades {commut}; = span(1, J, Gamma g1, Gamma g2): {sorted(commut)==expect}; quaternion relations: {quat}; even part {even} = span(1, J)",
        sorted(commut)==expect and quat and even==[(),(0,1)])
print("ALL:", ok_all)
