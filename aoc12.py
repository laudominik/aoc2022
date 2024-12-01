from math import inf


def vertex(y,x,width):
    return x + y * width

def dijkstra(m_g, height, width, start, end):

    traversed = set()
    distances = [inf for x in range(height * width)]
    distances[vertex(start[0],start[1], width)] = 0
   

    while len(traversed) != height * width:
        pick = (0,0)
        min_dist = inf
        for y in range(height):
            for x in range(width):
                if  distances[vertex(y,x,width)] <= min_dist and (y,x) not in traversed:
                    pick = (y,x)
                    min_dist = distances[vertex(y,x,width)]


        traversed.add(pick)
       
        for u in m_g[pick[0]][pick[1]]:
            if distances[vertex(u[0],u[1],width)] > min_dist + 1:
                distances[vertex(u[0],u[1],width)] = min_dist + 1


    print(traversed)
    print(distances)    

    return distances[vertex(end[0],end[1], width)], distances



def h(char):
    if char == 'S':
        return ord('a')
    elif char == 'E':
        return ord('z')
    else:
        return ord(char)


def to_graph(inp):
    spl = inp.split("\n")
    
    height = len(spl)
    width = len(spl[0])

    m_g = [[[] for x in range(width)] for y in range(height)]

    ass = []
    start = (0,0)
    end = (0,0)

    for y in range(height):
        for x in range(width):
            
            if spl[y][x] == 'S':
                start = (y,x)
            if spl[y][x] == 'a':
                ass.append((y,x))
            if spl[y][x] == 'E':
                end = (y,x)


            thresh = h(spl[y][x]) + 1

            if x > 0 and h(spl[y][x-1]) <= thresh:   
                m_g[y][x-1].append((y,x))  
                #m_g[y][x].append((y,x-1))
            if x < width - 1 and h(spl[y][x+1]) <= thresh:
                m_g[y][x+1].append((y,x)) 
                #m_g[y][x].append((y,x+1))
            if y > 0 and h(spl[y-1][x]) <= thresh:
                m_g[y-1][x].append((y,x)) 
                #m_g[y][x].append((y-1, x))
            if y < height - 1 and h(spl[y+1][x]) <= thresh:
                m_g[y+1][x].append((y,x))
                #m_g[y][x].append((y+1,x))
    return m_g, height, width, start, end, ass



with open("input12.txt", "r") as f:
    m_g, height, width, s, e, ass = to_graph(f.read())

    ds, dste = dijkstra(m_g, height, width, e, s)

    md = inf
    for a in ass:
        d = dste[vertex(a[0],a[1], width)]
        if  d < md:
            md = d
    print(md)



   