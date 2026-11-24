import sys,json,subprocess
lab='/home/claude/leon-machine/zero-divisors'
lvl=sys.argv[1]; n=int(sys.argv[2])
for id in sys.argv[3:]:
    out=subprocess.run(['python3',lab+'/colony/labcli.py','get_claim',json.dumps({'id':id})],capture_output=True,text=True).stdout
    try: d=json.loads(out)
    except Exception as e: print(id,'ERR',out[:300]); continue
    fm=d.get('front_matter',{}); lv=d.get('levels',{})
    print('###',id,'| v',fm.get('version'),'|',fm.get('status'),'|',fm.get('title'))
    for l in lvl.split(','):
        print('['+l+']',(lv.get(l) or '')[:n])
    print()
