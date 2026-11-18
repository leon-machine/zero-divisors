import sys, json
d = json.load(sys.stdin)
keys = sys.argv[1:]
def show(d, ind=0):
    if isinstance(d, dict):
        for k, v in d.items():
            if isinstance(v, (dict, list)):
                print(' ' * ind + k + ':'); show(v, ind + 1)
            else:
                print(' ' * ind + k + ': ' + str(v))
    elif isinstance(d, list):
        for v in d:
            if isinstance(v, (dict, list)): show(v, ind + 1)
            else: print(' ' * ind + '- ' + str(v))
if keys:
    for k in keys:
        cur = d
        for part in k.split('.'):
            cur = cur[part]
        print('== ' + k); show(cur) if isinstance(cur, (dict, list)) else print(cur)
else:
    show(d)
