from copy import deepcopy
from functools import cache
from frozendict import frozendict


def expand(blueprint, t, robots, materials, cache, max_spend):
    if t == 0:
        return materials[3]

    key = tuple([*robots, *materials, t])

    if key in cache:
        return cache[key]

    max_geode = materials[3] + robots[3] * t 

    for bp, bp_res in enumerate(blueprint):
        if bp != 3 and robots[bp] >= max_spend[bp]:
            continue

        wait = 0
        
        for rp, ramt in enumerate(bp_res):
            if robots[rp] == 0:               
                break
            wait = max(wait, -(-(ramt - materials[rp]) // robots[rp]))
        else:
        
            remtime = t - wait - 1
            if remtime <= 0:
                continue
            robots_ = robots[:]
            materials_ = [x + y * (wait + 1) for x, y in zip(materials, robots)]
            for rp, ramt in enumerate(bp_res):
                materials_[rp] -= ramt
            robots_[bp] += 1
            for i in range(3):
                materials_[i] = min(materials_[i], max_spend[i] * remtime)
            max_geode = max(max_geode, expand(blueprint, remtime, robots_, materials_, cache, max_spend))
    
    
    cache[key] = max_geode
 
    return max_geode


with open("input19.txt") as f:
    
    blueprints = []

    #[(ore,clay, obsidian, geode)]
    for y in [x.split("Each ") for x in f.read().split("\n")]:
        ore = [int(y[1].split(' ')[3])]
        clay = [int(y[2].split(' ')[3])]
        obsidian = [int(y[3].split(' ')[3]), int(y[3].split(' ')[6])]
        geode = [int(y[4].split(' ')[3]), 0, int(y[4].split(' ')[6])]

        max_spend = [0,0,0]
        max_spend[0] = max([int(y[1].split(' ')[3]),int(y[2].split(' ')[3]), int(y[3].split(' ')[3]), int(y[4].split(' ')[3])])
        max_spend[1] = int(y[3].split(' ')[6])
        max_spend[2] = int(y[4].split(' ')[6])
        blueprints.append(([ore, clay, obsidian, geode], max_spend))

    s = 0
    i = 1
    mult = 1

    for blueprint in blueprints[:3]:
        exu = expand(blueprint[0], 32,[1,0,0,0], [0,0,0,0], {}, blueprint[1])
        print(exu)
        s += i * exu
        if i <= 3:
            print(exu)
            mult *= exu

        i+= 1

    print(s)
    print(mult)
   

