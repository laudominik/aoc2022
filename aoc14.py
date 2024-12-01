def add_chains(s, arr):

    for chain in arr:
        
        i = 1
        x = chain[0][0]
        y = chain[0][1]
       
        while i != len(chain):
            s.add((x,y))
            
            xp = chain[i][0]
            yp = chain[i][1]
            
            if (xp - x) == 0 and (yp - y) == 0:
                i+=1
            elif xp - x == 0:
                if yp - y > 0:
                    y += 1
                else:
                    y -= 1
            elif yp - y == 0:
                if xp - x > 0:
                    x += 1
                else:
                    x -= 1

def simulate_sand(chains, floor_y):
    xs = 500
    ys = 0
    sand_set = set()
    while True:
        if (xs, ys+1) not in sand_set and (xs, ys+1) not in chains  and ys+1 != floor_y:
            ys+=1
        elif (xs-1,ys+1) not in sand_set and (xs-1, ys+1) not in chains and ys+1 != floor_y:
            xs -= 1
            ys += 1
        elif (xs+1, ys+1) not in sand_set and (xs+1, ys+1) not in chains and ys+1 != floor_y:
            xs += 1
            ys += 1
        else:
            sand_set.add((xs,ys))
            if xs == 500 and ys == 0:
                break
           
            xs = 500
            ys = 0

    print(len(sand_set))









with open("input14.txt") as f:
    inp = [[[int(z) for z in y.split(',')] for y in x.split(' -> ')] for x in f.read().split('\n')]
    s = set()
    add_chains(s, inp)
    floor_y = max([el[1] for el in s]) + 2
  
    simulate_sand(s, floor_y)
  