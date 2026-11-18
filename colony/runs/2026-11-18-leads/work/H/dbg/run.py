import sys,re,traceback
sys.path.insert(0,'/home/claude/phys-graph/lib')
import tp_premise; tp_premise.configure('/home/claude/phys-graph/store')
src=open(sys.argv[1]).read()
src=re.sub(r'^(\s*)ok = ok and (.*)$', r'\1assert \2', src, flags=re.M)
g={'__name__':'dbg'}
exec(compile(src,'dbg_check','exec'),g)
lines=src.split('\n')
for n in sorted(k for k in g if k.startswith('check_')):
    try:
        g[n](); print('ok',n)
    except AssertionError:
        tb=traceback.extract_tb(sys.exc_info()[2])[-1]
        print('ASSERT FAIL',n,'line',tb.lineno, lines[tb.lineno-1].strip()[:160])
    except Exception as e:
        tb=traceback.extract_tb(sys.exc_info()[2])[-1]
        print('ERR',n,repr(e)[:100],'line',tb.lineno, lines[tb.lineno-1].strip()[:160])
