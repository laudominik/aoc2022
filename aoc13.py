def tokenize(s):
    s = s.replace('[','[,')
    s = s.replace(']', ',]')
    tokens = list(filter(lambda x: x != '',s.split(',')))
    return tokens

def parse(tokens, i):
    out = []
    while i < len(tokens):
        tok = tokens[i]
        if tok == '[':
            inner, i = parse(tokens, i+1)
            out.append(inner)
            continue
        if tok == ']':
            i+=1
            break
        else:
            out.append(int(tok))
            i+=1
    return out, i

def parseLine(line):
    return parse(tokenize(line),1)[0]

def lex_cmp(l1, l2): # l1 op l2

    state = 'EQUAL'

    if len(l1) == 0 and len(l2) == 0:
        return 'EQUAL'
    if len(l1) == 0:
        return 'SMALLER'
    if len(l2) == 0:
        return 'BIGGER'

    if isinstance(l1[0],list) and isinstance(l2[0], list):
        state = lex_cmp(l1[0], l2[0])
    elif isinstance(l1[0], list):
        state = lex_cmp(l1[0], [l2[0]]) 
    elif isinstance(l2[0], list):
        state = lex_cmp([l1[0]], l2[0])
    else:
        if l1[0] == l2[0]:
            state = 'EQUAL'
        elif l1[0] > l2[0]:
            state = 'BIGGER'
        else:
            state = 'SMALLER'

    if state == 'EQUAL':
        return lex_cmp(l1[1:],l2[1:])

    return state

        
def lex_order(l1,l2):
    out = lex_cmp(l1,l2)
    if out == 'SMALLER':
        return -1
    elif out == 'BIGGER':
        return 1
    return 0


with open("input13.txt", "r") as f:
    from functools import cmp_to_key

    s = [parseLine(x) for x in f.read().replace('\n\n','\n').split('\n')]
    s.append([[2]])
    s.append([[6]])

    ix0 = 0
    ix1 = 0
    ix = 1

    for y in sorted(s, key=cmp_to_key(lex_order)):
        if y == [[2]]:
            ix0 = ix
        if y == [[6]]:
            ix1 = ix

        ix+=1
    print(ix0, ix1, ix0 * ix1)



