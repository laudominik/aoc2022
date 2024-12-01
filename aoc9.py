def hmove(head, mt):
   
    if mt == 'R':
        head[0] += 1
    elif mt == 'U':
        head[1] += 1
    elif mt == 'L':
        head[0] -= 1
    elif mt == 'D':
        head[1] -= 1
    
    return head

def tmove(head, tail):
    if head[0] - tail[0] == 0:
        if head[1] - tail[1] == 2:
            tail = (tail[0], tail[1] + 1)
        elif head[1] - tail[1] == -2:
            tail = (tail[0], tail[1] - 1)
    elif head[1] - tail[1] == 0:
        if head[0] - tail[0] == 2:
            tail = (tail[0] + 1, tail[1])
        elif head[0] - tail[0] == -2:
            tail = (tail[0] - 1, tail[1])
    else:
        if head[0] - tail[0] == 2 and head[1] - tail[1] == 1:
            tail = (tail[0] + 1, tail[1] + 1)
        elif head[0] - tail[0] == 2 and head[1] - tail[1] == -1:
            tail = (tail[0] + 1, tail[1] - 1)
        elif head[0] - tail[0] == -2 and head[1] - tail[1] == 1:
            tail = (tail[0] - 1, tail[1] + 1)
        elif head[0] - tail[0] == -2 and head[1] - tail[1] == -1:
            tail = (tail[0] - 1, tail[1] - 1)
        elif head[0] - tail[0] == 1 and head[1] - tail[1] == 2:
            tail = (tail[0] + 1, tail[1] + 1)
        elif head[0] - tail[0] == 1 and head[1] - tail[1] == -2:
            tail = (tail[0] + 1, tail[1] - 1)
        elif head[0] - tail[0] == -1 and head[1] - tail[1] == 2:
            tail = (tail[0] - 1, tail[1] + 1)
        elif head[0] - tail[0] == -1 and head[1] - tail[1] == -2:
            tail = (tail[0] - 1, tail[1] - 1)
        elif head[0] - tail[0] == 2 and head[1] - tail[1] == 2:
            tail = (tail[0] + 1, tail[1] + 1)
        elif head[0] - tail[0] == -2 and head[1] - tail[1] == 2:
            tail = (tail[0] - 1, tail[1] + 1)
        elif head[0] - tail[0] == 2 and head[1] - tail[1] == -2:
            tail = (tail[0] + 1, tail[1] - 1)
        elif head[0] - tail[0] == -2 and head[1] - tail[1] == -2:
            tail = (tail[0] - 1, tail[1] - 1)
    return tail

def simulate(moves):
    head = [0,0]
    
    knots = [(0,0) for x in range(9)]
    visited = set()
    
    for m in moves:
        mv = m.split(' ')
        for i in range(int(mv[1])):
            visited.add(knots[8])
            head = hmove(head,mv[0])
            knots[0] = tmove(head, knots[0])
            for i in range(1,len(knots)):
                knots[i] = tmove(knots[i-1], knots[i])
            visited.add(knots[8])
    print(head, knots)
    print(visited)
    print(len(visited))

with open("input9.txt", "r") as f:
    simulate(f.read().split('\n'))