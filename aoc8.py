import copy

def scoreAlongVector(trees, i, j, vec_x, vec_y):
    tree = trees[i][j]
    x0 = copy.deepcopy(i)
    y0 = copy.deepcopy(j)



    x0 += vec_x
    y0 += vec_y
    score = 1
    while x0 >= 0 and y0 >= 0 and x0 < len(trees) and y0 < len(trees[0]):
        if trees[x0][y0] >= tree:
            return score
        score += 1
        x0 += vec_x
        y0 += vec_y

    return score - 1

def score(trees, i, j):     
    return scoreAlongVector(trees, i, j, 0, 1) * \
            scoreAlongVector(trees, i, j, 1, 0) * \
            scoreAlongVector(trees, i, j, -1, 0) * \
            scoreAlongVector(trees, i, j, 0, -1)



def visibleTrees(trees):
    c = 0

    visibility_map = [[0 for x in y] for y in trees]
    mx = 0
    for i in range(len(trees)):
        for j in range(len(trees[i])):
            visibility_map[i][j] = score(trees, i, j)
            if visibility_map[i][j] > mx:
                mx = visibility_map[i][j]
    return mx

with open("input8.txt", "r") as f:
    print(visibleTrees([[int(y) for y in x] for x in f.read().split("\n")]))