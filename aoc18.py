import sys
from collections import deque
sys.setrecursionlimit(100000)

def surface(cubes):
    sf = 0
    for (x,y,z) in cubes:
        if (x+1, y, z) not in cubes:
            sf += 1
        if (x-1, y, z) not in cubes:
            sf += 1
        if(x, y+1, z) not in cubes:
            sf += 1
        if (x, y-1, z) not in cubes:
            sf += 1
        if (x, y, z + 1) not in cubes:
            sf += 1
        if (x,y,z-1) not in cubes:
            sf += 1
    return sf


def dip(cubes):
    sf = 0
    traversal = deque([(0,0,0)])
    seen = set()
    while traversal:
        print(traversal)
        (x,y,z) = traversal.popleft()
        seen.add((x,y,z))
        if (x+1, y, z) in cubes:
            sf += 1
            seen.add((x+1,y,z))
        if (x-1, y, z) in cubes:
            sf += 1
            seen.add((x-1,y,z))
        if(x, y+1, z) in cubes:
            sf += 1
            seen.add((x,y+1,z))
        if (x, y-1, z) in cubes:
            sf += 1
            seen.add((x,y-1,z))
        if (x, y, z + 1) in cubes:
            sf += 1
            seen.add((x,y,z+1))
        if (x,y,z-1) in cubes:
            sf += 1
            seen.add((x,y,z-1))
        if x > -2 and (x-1, y, z) not in seen:
            traversal.append((x-1,y,z))
            seen.add((x-1,y,z))
        if x < 25 and (x+1,y,z) not in seen:
            traversal.append((x+1,y,z))
            seen.add((x+1,y,z))
        if y > -2 and (x,y-1, z) not in seen:
            traversal.append((x,y-1,z))
            seen.add((x,y-1,z))
        if y < 25 and ((x, y+1, z)) not in seen:
            traversal.append((x,y+1,z))
            seen.add((x,y+1,z))
        if z > -2 and ((x,y,z-1)) not in seen:
            traversal.append((x,y,z-1))
            seen.add((x,y,z-1))
        if z < 25 and (x,y,z+1) not in seen:
            traversal.append((x,y,z+1))
            seen.add((x,y,z+1))
    return sf


with open("input18.txt") as f:
    cubes = [tuple([int(y) for y in x.split(',')]) for x in f.read().split('\n')]
    print(surface(cubes))

    print(dip(cubes))

    #print(len(cubes))

