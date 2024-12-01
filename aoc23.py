
def prop(elf, elves, direction):
    x,y = elf
    if direction == 'N':
        if (x, y-1) in elves:
            return False
        if (x-1, y-1) in elves:
            return False
        if (x+1, y-1) in elves:
            return False
        return (x, y-1)
    if direction == 'S':
        if (x, y+1) in elves:
            return False
        if (x-1, y+1) in elves:
            return False
        if (x+1, y+1) in elves:
            return False
        return (x, y+1)
    if direction == 'E':
        if (x+1, y) in elves:
            return False
        if (x+1, y-1) in elves:
            return False
        if (x+1, y+1) in elves:
            return False
        return (x+1, y)
    if direction == 'W':
        if (x-1, y) in elves:
            return False
        if (x-1, y-1) in elves:
            return False
        if (x-1, y+1) in elves:
            return False
        return (x-1, y)
    assert 0


def should_move(elf, elves):
    x,y = elf

    return (x+1, y) in elves \
        or (x-1, y) in elves \
        or (x+1, y+1) in elves \
        or (x+1, y-1) in elves \
        or (x-1, y-1) in elves \
        or (x-1, y+1) in elves \
        or (x, y-1) in elves \
        or (x, y+1) in elves
        


def simulate(elves):

    state = "NSWE"

    change = True
    rounds = 0
    while change:
        print(rounds)
        rounds += 1
        next_moves = []
        change = False

        #first part
        for elf in elves:
            if should_move(elf, elves):
                dst = prop(elf, elves, state[0])    
                if dst:
                    next_moves.append((elf, dst))
                    continue
                dst = prop(elf, elves, state[1])
                if dst:
                    next_moves.append((elf,dst))
                    continue
                dst = prop(elf, elves, state[2])
                if dst:
                    next_moves.append((elf,dst))
                    continue
                dst = prop(elf, elves, state[3])
                if dst:
                    next_moves.append((elf,dst))
                    continue
            next_moves.append((elf, elf))

        #second part
        next_elves = []
        for elf, dst in next_moves:
            if len([1 for a, d in next_moves if d == dst]) == 1:
                next_elves.append(dst)
                if dst != elf:
                    change = True

            else:
                next_elves.append(elf)
        state = state[1:] + state[0]
        elves = next_elves
    print(rounds)
    return elves

def area(elves):
    min_x = min([x for x,y in elves])
    min_y = min([y for x,y in elves])
    max_x = max([x for x,y in elves])
    max_y = max([y for x,y in elves])

    cnt = 0
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x,y) not in elves:
                cnt+=1
    return cnt


elves = []

with open("input23.txt") as f:
    inp = f.read().split('\n')
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] == '#':
                elves.append((x,y))


simulate(elves)


