from itertools import count


inp = [i[1:-1] for i in open("input24.txt").read().split('\n')[1:-1]]
print(inp)
width = len(inp[0])
height = len(inp)


def in_blizzard(t, x, y):
    return inp[y%height][(x+t)%width] == '<' or \
           inp[y%height][(x-t)%width] == '>' or \
           inp[(y+t)%height][x%width] == '^' or \
           inp[(y-t)%height][x%width] == 'v'

def bfs(st, et,t0):
    moves = {st}
    for i in count(t0):
        new_moves = set()
        for x,y in moves:
            if 0<=y < height and in_blizzard(i-1,x,y) or \
            not (0 <= x < width and \
            0 <= y < height or ((x,y) == (0,-1) or (x,y) == (width-1, height))):
                continue
            for dx, dy in [(-1,0), (1, 0), (0,0), (0,-1), (0,1)]:
                new_moves.add((x+dx,y+dy))

        moves = new_moves
        if et in moves:
            return i

s = (0,-1)
e = (width-1, height)

j1 = bfs(s,e,1)
j2 = bfs(e,s, j1)
j3 = bfs(s,e,j2)
print(j3)


