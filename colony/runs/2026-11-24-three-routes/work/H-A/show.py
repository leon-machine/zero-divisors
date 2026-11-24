import json,subprocess,sys
def call(tool,arg):
    out=subprocess.run(['python3','colony/labcli.py',tool,json.dumps(arg)],capture_output=True,text=True).stdout
    try:
        d=json.loads(out)
        if isinstance(d,str):
            try: d=json.loads(d)
            except Exception: pass
        return d
    except Exception:
        return out
def show(x,ind=0,skip=()):
    if isinstance(x,dict):
        for k,v in x.items():
            if k in skip: continue
            if isinstance(v,(dict,list)):
                print(' '*ind+str(k)+':'); show(v,ind+2,skip)
            else: print(' '*ind+str(k)+': '+str(v))
    elif isinstance(x,list):
        for v in x:
            if isinstance(v,(dict,list)):
                print(' '*ind+'-'); show(v,ind+2,skip)
            else: print(' '*ind+'- '+str(v))
    else: print(x)
if __name__=='__main__':
    tool=sys.argv[1]; arg=json.loads(sys.argv[2])
    skip=tuple(sys.argv[3].split(',')) if len(sys.argv)>3 else ()
    show(call(tool,arg),0,skip)
