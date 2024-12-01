def dm(x0,y0,x1,y1):
    return abs(x0-x1) + abs(y0-y1)



def covered(scanners, x, y):
    for scanner in scanners:
        xs = scanner[0]
        ys = scanner[1]
        radius = scanner[2]
        if dm(xs,ys,x,y) <= radius:
            return True
    return False



def cpoint(scanners):
    for scanner in scanners:
        xs = scanner[0]
        ys = scanner[1]
        radius = scanner[2]
        print(xs,ys)
        for dy in range(radius + 1):
            dx = radius - dy + 1
            for p in [-1, 1]:
                for q in [-1, 1]:
                    xp = xs + dx * p
                    yp = ys + dy * q
                    

                    if not covered(scanners, xp, yp) and xp >= 0 and xp <= 4000000 and yp >= 0 and yp <= 4000000:
                        return (xp, yp)
    return (-1,-1)




def coverage(scanners):
    #scanner[0] = scanner pos x
    #scanner[1] = scanner pos y
    #scanner[2] = scanner "radius"

    #beams - set
    cover = set()
    for scanner in scanners:
        x = scanner[0]
        y = scanner[1]
        radius = scanner[2]
        print(radius)
        yc = y - radius
        yc = 2000000
        #while yc != y + radius + 1:
        while True:
            xc = x - radius
            while xc != x + radius + 1:
                if dm(xc,yc, x,y) <= radius:
                    cover.add((xc,yc))
                xc+=1
            yc+=1
            break
        
    return cover

def count_covered(cover, scanners, beams):
    count = 0
    for c in cover:
        if c not in scanners and c not in beams:
            count+=1

    return count

beams = []
scanners = []
scanners_r = []



with open("input15.txt") as f:
    for row in f.read().split("\n"):
        rarr = row.split(' ')
        x = int(rarr[2][2:-1])
        y = int(rarr[3][2:-1])
        xb = int(rarr[8][2:-1])
        yb = int(rarr[9][2:])
        scanners.append((x,y))
        beams.append((xb,yb))
        scanners_r.append((x,y,dm(x,y,xb,yb)))


#cover = coverage(scanners_r)
print(cpoint(scanners_r))
#print(count_covered(cover, scanners, beams))
# print(cover)

# cover = coverage([(8,7,dm(8,7,2,10))])

# print(cover)

# print(count_covered(cover, [(8,7)], [(2,10)]))
# print(count_covered(cover, scanners, beams))

# print(count_covered(cover, [(8,7)], [(2,10)]))

# for y in range(-2,22):
#     row = ""

#     for x in range(-2,25):
#         if (x,y) in beams:
#             row += 'B'
#         elif (x,y) in scanners:
#             row += 'S'
#         elif (x,y) in cover:
#             row += '#'
#         else:
#             row += '.'
#     print(row)








