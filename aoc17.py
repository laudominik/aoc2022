def next_rock(el):
    els = '-+L|O-'
    for i in range(len(els)):
        if els[i] == el:
            return els[i+1]
    return 0

def position_ok(x,y,el,occupied):
    roccupied = rock_occupied(x,y,el)
    for (x,y) in roccupied:
        if x >= 7 or x < 0: #edges
            return False
    
        if y < 0:  #floor
            return False

    if len(occupied.intersection(roccupied)) != 0:
        return False

    return True

def rock_occupied(x,y,el):
    if el == '-':
        return set([(x,y),(x+1,y),(x+2,y),(x+3,y)]) #left edge
    if el == '+':
        return set([(x,y), (x+1,y), (x-1,y), (x,y+1), (x,y-1)]) #middle point
    if el == 'L':
        return set([(x,y), (x, y-1), (x, y-2), (x-1, y-2), (x-2,y-2)]) # top point
    if el == '|':
        return set([(x,y),(x, y-1), (x, y-2), (x, y-3)]) #top point
    if el == 'O':
        return set([(x,y), (x+1, y), (x, y-1), (x+1,y-1)]) #top left corner

def start_point(el, occupied):
     
    h_max = -1
    if len(occupied) != 0:
        h_max = max([y for (x,y) in occupied])
    if el == '-':
        return (2, h_max + 4)
    if el == '+':
        return (3, h_max + 5)
    if el == 'L':
        return (4, h_max + 6)
    if el =='|':
        return (2, h_max + 7)
    if el == 'O':
        return (2, h_max + 5)

def draw(occupied, current_falling):
    h_max = 0
    if len(occupied) != 0:
        h_max = max([y for (x,y) in occupied])
    if len(current_falling) != 0:
        h_max = max(h_max, max([y for (x,y) in current_falling]))

    for y in reversed(range(0, h_max + 4)):
        row = '|'

        for x in range(0, 7):
            if (x,y) in current_falling:
                row += '@'
            elif (x,y) in occupied:
                row += '#'
            else:
                row += '.'
        row += '|'
        print(row)
    print('+-------+') 
    input()

def mh(occupied):
    if len(occupied) == 0:
        return 0
    return max([y for (x,y) in occupied])



def simulate(wind, iters):
    el = '-'
    occupied = set()
    current = 0
    deltas = [0]
    heights = [0]

    rock_count = 0
    
    while rock_count < iters:
        xc,yc = start_point(el, occupied)

        while True:
            if wind[current] == '<' and position_ok(xc-1, yc, el, occupied):
                xc -= 1
            elif wind[current] == '>' and position_ok(xc+1, yc, el, occupied):
                xc += 1
            current = (current + 1)%len(wind)
            delta = mh(occupied) - heights[-1]

            if position_ok(xc, yc-1, el, occupied):
                yc -= 1
            else:
                break
        occupied = occupied.union(rock_occupied(xc, yc, el))
        heights.append(mh(occupied))
        deltas.append(delta)

        el = next_rock(el)  
        rock_count+=1
    h_max = max([y for (x,y) in occupied])
    print(h_max + 1)
    return deltas

def seq(deltas):
    size = 30
    for i in range(len(deltas) - size):
        sliced = deltas[i:i+size]
        repeats = [i]
        for t in range(i+size, len(deltas) - size):
            testslice = deltas[t:t+size]
            if sliced == testslice:
                repeats.append(t)
        if len(repeats) > 2: return repeats

with open("input17.txt") as f:
    wind = f.read()
    dts = simulate(wind, 2022)
    simulate(wind, 3000)
    #dts += simulate(f.read())
    s = seq(dts)
    lent = s[1] - s[0]
    it = 1000000000000 - s[0]
    rem = it % lent
    




