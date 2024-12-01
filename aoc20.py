def move(L, el):
    
    ix = 0

    for i, val in enumerate(L):
        if val[0] == el:
            ix = i
            break
    else:
        assert 0
    shift(L, ix)

def shift(L, ix):
    cpy = L[ix]
    
    if cpy[1] == 0:
        return

    sg = 1 if cpy[1] > 0 else -1
    s = (ix + cpy[1]) % len(L) 
    end = ix
    swap = L[s]

    while s != end:
        swap, L[s] = L[s], swap
        s = (s - sg) % len(L)
    L[end] = swap
    L[(ix + cpy[1]) % len(L)] = cpy

def grove_coords(L):
    for i, val in enumerate(L):
        if val[1] == 0:
            ix = i
            break
    else:
        assert 0
    v1 = L[(ix + 1000) % len(L)][1]
    v2 = L[(ix + 2000) % len(L)][1] 
    v3 = L[(ix + 3000) % len(L)][1]

    print(v1,v2,v3)
    return  v1 + v2 + v3 


arr = [(i,x * 811589153) for i,x in enumerate([int(y) for y in open("input20.txt").read().split('\n')])]
#print(arr)

for i = 0 to 10:
    for i in range(len(arr)):
        move(arr, i)


#print([x for (y,x) in arr])
print(grove_coords(arr))