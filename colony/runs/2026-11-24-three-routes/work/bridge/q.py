import json, subprocess, sys, textwrap
LAB='/home/claude/leon-machine/zero-divisors'
def call(tool, arg):
    r = subprocess.run(['python3','colony/labcli.py',tool,json.dumps(arg)],cwd=LAB,capture_output=True,text=True)
    try: return json.loads(r.stdout)
    except Exception: return {'_raw': r.stdout[:3000], '_err': r.stderr[:1000]}
def show(o, keys=None, maxlen=6000, indent=0):
    if isinstance(o, dict):
        for k,v in o.items():
            if keys and indent==0 and k not in keys: continue
            if isinstance(v,(dict,list)):
                print(' '*indent+f'[{k}]'); show(v,None,maxlen,indent+1)
            else:
                s=str(v)
                print(' '*indent+f'{k}: {s[:maxlen]}')
    elif isinstance(o, list):
        for x in o:
            if isinstance(x,(dict,list)): show(x,None,maxlen,indent+1); print(' '*indent+'-')
            else: print(' '*indent+'- '+str(x)[:maxlen])
if __name__=='__main__':
    tool=sys.argv[1]; arg=json.loads(sys.argv[2]); keys=sys.argv[3].split(',') if len(sys.argv)>3 else None
    maxlen=int(sys.argv[4]) if len(sys.argv)>4 else 6000
    show(call(tool,arg),keys,maxlen)
