from copy import deepcopy

def expand(node, cache, arr):
    if node in cache:    
        return cache[node]
    
    val1 = expand(arr[node][0], cache, arr)
    val2 = expand(arr[node][2], cache, arr)

    out = 0
    if arr[node][1] == '+':
        out = val1 + val2
    elif arr[node][1] == '-':
        out = val1 - val2
    elif arr[node][1] == '*':
        out = val1 * val2
    elif arr[node][1] == '/':
        out = val1 // val2

    cache[node] = out
    return out


def find_humn(arr):

    cache = {}
    arr_set = {x[0][:-1]:x[1:] for x in arr}
    arr_set['root'][1] = '-'

    for a in arr:
        if len(a) == 2:
            cache[a[0][:-1]] = int(a[1])

    match = False

    i = 230000
    last_i = 0



    while True:
        arr_set['humn'] = i
        cache['humn'] = i

        match = expand('root', deepcopy(cache), arr_set)
        print(i, match)
        if match > 0:
            last_i = i
            i *= 2
        elif match < 0:
            break
        else:
            break

    piwo = 0
    while True:
        piwo = (last_i + i) // 2

        arr_set['humn'] = piwo
        cache['humn'] = piwo

        match = expand('root', deepcopy(cache), arr_set)
        if match > 0:
            last_i = piwo
        elif match < 0:
            i = piwo
        else:
            break


    print(piwo, match)
    arr_set['humn'] = piwo
    cache['humn'] = piwo

    print(expand('root', deepcopy(cache), arr_set))


with open("input21.txt") as f:
    arr = [y.split(' ') for y in f.read().split('\n')]
    find_humn(arr)

# expand("aaa", {})