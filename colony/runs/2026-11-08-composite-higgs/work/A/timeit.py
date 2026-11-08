import sys, time, importlib.util
sys.path.insert(0,'/home/claude/phys-graph/lib')
import tp_premise, GA
tp_premise.configure('/home/claude/phys-graph/store')
spec=importlib.util.spec_from_file_location('chk',sys.argv[1]); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
for name in sorted(n for n in dir(m) if n.startswith('check_')):
    if len(sys.argv)>2 and name not in sys.argv[2:]: continue
    t=time.time(); nf=len(GA.FAILURES)
    try: r=getattr(m,name)()
    except Exception as e: r=repr(e)
    print(name, r, len(GA.FAILURES)-nf, round(time.time()-t,1), flush=True)
