import functools
min_length = []
G = {}
W = {}

def dijkstra(G, v):

    from math import inf
    n = len(G)

    traversed = set()
    distances = {v:inf for v in G}
    distances[v] = 0
   

    while len(traversed) != n:
        pick = 0
        min_dist = inf
        
        for u in G:
            if  distances[u] <= min_dist and u not in traversed:
                pick = u
                min_dist = distances[u]

        traversed.add(pick)
       
        for u in G[pick]:
            if distances[u] > min_dist + 1:
                distances[u] = min_dist + 1

    return  distances

def map_dijkstra(G):
    return {v:dijkstra(G,v) for v in G}

# v - current vertex
@functools.cache
def match(time, v,  opened, elephant):
    if time <= 0 and not elephant:
        return 0
    if time <= 0 and elephant:
        return match(26, 'AA', opened, elephant = False)

    maximal = 0
    for u in G[v]:
        maximal = max(maximal, match(time-1, u, opened, elephant))

    if v not in opened and W[v] > 0 and time > 0:
        opened = set(opened)
        opened.add(v)
        time -= 1
        rho = time * W[v]

        for u in G[v]:
            maximal = max(maximal, rho + match(time-1, u, frozenset(opened), elephant))

    return maximal




t = 30

with open("input16.txt") as f:
    for row in f.read().split('\n'):
        tokens = row.split(' ')
        name = tokens[1]
        rate = int(tokens[4][5:-1])
        neighborhood = [x.replace(',','') for x in tokens[9:]]

        G[name] = neighborhood
        W[name] = rate

min_length = map_dijkstra(G)


print(match(26, 'AA', frozenset(),elephant = True))



