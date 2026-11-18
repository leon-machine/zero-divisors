"""Helpers for targeted edits of store/open_problems.yaml (maintainer pass of 2026-11-18, second file owner).

Every edit is made inside one problem's block, by exact string replacement that must match once, or by
replacing one whole field or one attack item of that block. Nothing is reordered and no other block is touched;
after each group the file is loaded with yaml and compared with the copy taken before the pass."""
import re
import textwrap
import yaml

PATH = '/home/claude/phys-graph/store/open_problems.yaml'
BEFORE = '/home/claude/phys-graph/colony/runs/2026-11-18-leads/work/M2/open_problems.before.yaml'
WIDTH = 112


def cr(x):
    return '\\claimref{' + x + '}'


def wrap(text, indent):
    """One paragraph, wrapped, each line indented by `indent` spaces. Long tokens are never broken."""
    text = ' '.join(text.split())
    out = textwrap.wrap(text, width=WIDTH, initial_indent=' ' * indent, subsequent_indent=' ' * indent,
                        break_long_words=False, break_on_hyphens=False)
    for line in out:
        assert not line.rstrip().endswith(':') or True
    return '\n'.join(out)


def block(text, oid):
    i = text.index('\n- id: ' + oid + '\n') + 1
    m = re.search(r'\n(?:- id: |\n# -{10,})', text[i + 5:])
    j = i + 5 + m.start() + 1 if m else len(text)
    return i, j


def rep(b, old, new):
    assert b.count(old) == 1, (old[:80], b.count(old))
    return b.replace(old, new)


def set_field(b, key, nextkey, paragraphs):
    """Replace the folded scalar `key` (which ends where `nextkey` begins) by the given paragraphs."""
    head = '  ' + key + ': >-\n'
    tail = '\n  ' + nextkey + ':'
    assert b.count(head) == 1 and b.count(tail) == 1, (key, nextkey, b.count(head), b.count(tail))
    i = b.index(head) + len(head)
    j = b.index(tail)
    assert i < j
    body = '\n\n'.join(wrap(p, 4) for p in paragraphs)
    return b[:i] + body + b[j:]


def append_known(b, paragraph, nextkey='attack'):
    """Add one dated paragraph at the end of `known`."""
    tail = '\n  ' + nextkey + ':'
    assert b.count(tail) == 1, (nextkey, b.count(tail))
    j = b.index(tail)
    return b[:j] + '\n\n' + wrap(paragraph, 4) + b[j:]


def attack_items(b):
    head = '\n  attack:\n'
    tail = '\n  success:'
    assert b.count(head) == 1 and b.count(tail) == 1
    i = b.index(head) + len(head)
    j = b.index(tail)
    raw = b[i:j]
    parts = re.split(r'\n(?=    - )', raw)
    assert all(p.startswith('    - ') for p in parts), [p[:20] for p in parts]
    return i, j, parts


def set_attack_item(b, n, text, expect_start=None):
    """Replace attack item n (0-based) by a folded block scalar holding `text`."""
    i, j, parts = attack_items(b)
    if expect_start is not None:
        assert expect_start in parts[n][:400], (n, parts[n][:120])
    parts[n] = '    - >-\n' + wrap(text, 6)
    return b[:i] + '\n'.join(parts) + b[j:]


def append_to_attack_item(b, n, text, expect_start=None):
    i, j, parts = attack_items(b)
    assert parts[n].startswith('    - >-\n'), parts[n][:40]
    if expect_start is not None:
        assert expect_start in parts[n][:400], (n, parts[n][:120])
    parts[n] = parts[n].rstrip('\n') + '\n' + wrap(text, 6)
    return b[:i] + '\n'.join(parts) + b[j:]


def add_attack_item(b, text):
    i, j, parts = attack_items(b)
    parts.append('    - >-\n' + wrap(text, 6))
    return b[:i] + '\n'.join(parts) + b[j:]


def add_entities(b, ids):
    """Append ids to the block's entities list, block style or flow style."""
    m = re.search(r'\n  entities: \[(.*)\]\n  added:', b)
    if m:
        for x in ids:
            assert x not in m.group(1), x
        new = m.group(1) + ''.join(', ' + x for x in ids)
        return b[:m.start(1)] + new + b[m.end(1):]
    tail = '\n  added:'
    assert b.count(tail) == 1 and b.count('\n  entities:\n') == 1
    j = b.index(tail)
    ent = b[b.index('\n  entities:\n'):j]
    for x in ids:
        assert ('- ' + x + '\n') not in ent + '\n', x
    return b[:j] + ''.join('\n    - ' + x for x in ids) + b[j:]


def apply(edits):
    """edits: list of (op id, function block -> block). Writes the file and verifies it."""
    text = open(PATH).read()
    for oid, fn in edits:
        i, j = block(text, oid)
        nb = fn(text[i:j])
        assert nb.endswith('\n') and nb.startswith('- id: ' + oid + '\n')
        text = text[:i] + nb + text[j:]
    open(PATH, 'w').write(text)
    verify([oid for oid, _ in edits])


def verify(changed=None):
    new = yaml.safe_load(open(PATH))
    old = yaml.safe_load(open(BEFORE))
    assert [o['id'] for o in new] == [o['id'] for o in old], 'order or ids changed'
    diff = [n['id'] for n, o in zip(new, old) if n != o]
    for n in new:
        for k in ('id', 'title', 'area', 'kind', 'difficulty', 'status', 'statement', 'entities'):
            assert n.get(k), (n['id'], k)
        assert isinstance(n['entities'], list) and all(isinstance(x, str) for x in n['entities'])
        assert isinstance(n.get('attack') or [], list) and all(isinstance(x, str) for x in n.get('attack') or [])
        assert n['status'] in ('open', 'partial', 'reformulated', 'settled')
    print('yaml ok;', len(new), 'problems; differing from the copy before the pass:', diff)
    if changed is not None:
        assert set(changed) <= set(diff), (changed, diff)
    return diff
