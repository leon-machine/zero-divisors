import os,subprocess,sys
LAB='/home/claude/phys-graph'; W=LAB+'/colony/runs/2026-11-12-asymmetry/verify/work-R1'
P1='synthesis.exchange-of-set-and-clear-is-inner-and-fixed-by-no-integer-state'
P2='synthesis.baryon-number-centraliser-in-the-five-mode-algebra'
P3='synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them'
P4='synthesis.reversing-baryon-number-is-a-conjugation-and-reverses-the-jarlskog-invariant'
perts=[
 (P1,'base',None,None),
 (P1,'a_wrong_implementer','self.u = self.mul(*(self.e if m % 2 == 1 else self.f))','self.u = self.mul(*(self.e if m % 2 == 0 else self.f))'),
 (P1,'b_state_norm','return lambda x: 2 ** self.m * self.mul(p, x).get((), F(0))','return lambda x: 2 ** (self.m - 1) * self.mul(p, x).get((), F(0))'),
 (P1,'c_volume_sign','assert GA.eq(A.X(omega), GA.scal((-1) ** m, omega))','assert GA.eq(A.X(omega), GA.scal((-1) ** (m + 1), omega))'),
 (P1,'d_always_e_product','self.u = self.mul(*(self.e if m % 2 == 1 else self.f))','self.u = self.mul(*self.e)'),
 (P2,'base',None,None),
 (P2,'a_nb_sign_of_P','NB = GA.scal(F(1, 4), GA.sub(BL, P))','NB = GA.scal(F(1, 4), GA.add(BL, P))'),
 (P2,'b_bl_coefficient','BL = GA.sub(ONE, GA.scal(F(2, 3), K))','BL = GA.sub(ONE, GA.scal(F(1, 2), K))'),
 (P2,'c_T_four_modes','T = mul(*V)','T = mul(V[0], V[1], V[2], V[3])'),
 (P2,'d_pairs_are_two','PAIRS, SLOTS = (0, 1, 2), (3, 4)','PAIRS, SLOTS = (0, 1), (2, 3, 4)'),
 (P3,'base',None,None),
 (P3,'a_Y_slot_charge','Y, NB, NL, BML = vec(hyp, F(1, 2)), vec(n_b, 0), vec(n_l, 0), vec(bml, 0)','Y, NB, NL, BML = vec(hyp, F(0)), vec(n_b, 0), vec(n_l, 0), vec(bml, 0)'),
 (P3,'b_majorana_four_modes','top = [("v", i) for i in MODES]','top = [("v", i) for i in (1, 2, 3, 4)]'),
 (P3,'c_coefficient','c = F(28, 79)','c = F(8, 23)'),
 (P3,'d_chi_sign','return -(-1) ** jk(S)[0]','return (-1) ** jk(S)[0]'),
 (P3,'e_equilibrium_fixed_point_only','ok = final(0, -79) == 28 and final(79, 79) == 0 and final(28, -51) == 28','ok = final(79, 79) == 0'),
 (P4,'base',None,None),
 (P4,'a_nb_table','return [F(0), F(1, 3), F(-1, 3), F(0)][k_of(S)]','return [F(0), F(1, 3), F(1, 3), F(0)][k_of(S)]'),
 (P4,'b_no_conjugation','ok = ok and comm_det(conj(Hu), conj(Hd)) == QI(0) - D','ok = ok and comm_det(Hu, Hd) == QI(0) - D'),
 (P4,'c_drop_block_condition','blocks = (A & PAIR) in (frozenset(), PAIR) and (A & SLOT) in (frozenset(), SLOT)','blocks = True'),
 (P4,'d_hypercharge_formula','return F(j_of(S) - 1, 2) + bml(S) / 2','return F(j_of(S) - 1, 2) - bml(S) / 2'),
]
for pid,name,old,new in perts:
    src=open(f'{LAB}/proposals/{pid}/check.py').read()
    if old is not None:
        assert src.count(old)==1,(pid,name,src.count(old))
        src=src.replace(old,new)
    d=f'{W}/pert/{pid[:28]}_{name}'; os.makedirs(d,exist_ok=True)
    open(d+'/check.py','w').write(src)
    r=subprocess.run(['python3',LAB+'/colony/runcheck.py',d+'/check.py'],capture_output=True,text=True)
    lines=[l for l in r.stdout.splitlines() if l.startswith(('PASS','FAIL'))]
    print(pid[10:40],name,'exit',r.returncode)
    for l in lines: print('    ',l[:110])
