import sys,json,subprocess
def show(id, levels=('formal',), maxc=7000):
    out=subprocess.run(['python3','colony/labcli.py','get_claim',json.dumps({'id':id})],capture_output=True,text=True).stdout
    d=json.loads(out)
    fm=d['front_matter']
    print('###',fm.get('id'),'v',fm.get('version'),'status',fm.get('status'),'kind',fm.get('kind'))
    print('title:',fm.get('title'))
    for l in levels:
        t=d['levels'].get(l)
        if t: print('--',l,':\n',t[:maxc])
    print()
if __name__=='__main__':
    lv=('formal',)
    args=sys.argv[1:]
    if args[0].startswith('-l'):
        lv=tuple(args[0][2:].split(',')); args=args[1:]
    for a in args: show(a,lv)
