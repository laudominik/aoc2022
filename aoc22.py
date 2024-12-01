
'''

   111222
   111222
   111222
   333
   333
   333
555444
555444
555444
666
666
666

 3
542
 6

'''



def next_tile(y,x, board, facing):
    if facing == 'up':
        if board[y-1][x] == ' ':
            zy = y
            zx = x
            while board[zy][zx] != ' ':
                zy += 1
            return (zy-1, zx, facing) 
        elif board[y-1][x] == '#':
            return (y, x, facing)
        else:
            return (y-1,x, facing)

    elif facing == 'down':
        if board[y+1][x] == ' ':
            zy = y
            zx = x
            while board[zy][zx] != ' ':
                zy -= 1
            return (zy+1, zx, facing) 
        elif board[y+1][x] == '#':
            return (y, x, facing)
        else:
            return (y+1, x, facing)

    elif facing == 'right':

        if board[y][x+1] == ' ':
            if y >= 1 and y <= 50:
                return (50 - y + 101, 100, 'left')
            elif y >= 51 and y <= 100:
                return (50,y-51 + 101, 'up')
            elif y >= 101 and y <= 150:
                return (151 - y,150, 'left')
            elif y >= 151 and y <= 200:
                return (150,y-151 + 51, 'up')
            assert 0

        elif board[y][x+1] == '#':
            return (y,x,facing)
        else:
            return (y, x+1, facing)

    elif facing == 'left':
        if y >= 1 and y <= 50:
            return (151 - y,1,'right')
        if y >= 51 and y <= 100:
            return (101,y - 50 ,'down')
        if y >= 101 and y <= 150:
            return (150 - y + 1, 51, 'right')
        if y >= 151 and y <= 200:
            return (1, 1,'down')


        elif board[y][x-1] == '#':
            return (y,x, facing)
        else:
            return (y, x-1, facing)

def parse_board():
    board = []
    board.append([' ' for y in range(row_length)])

    with open("input22_1.txt") as f:
        
        rows = f.read().split('\n')
        for row in rows:
            board_row = [c for c in row]
            board_row.insert(0, ' ')
            while len(board_row) != row_length:
                board_row.append(' ')
            board.append(board_row)

    board.append([' ' for y in range(row_length)])
    return board

def parse_moves():
    moves = []
    with open("input22_2.txt") as f:
        current = ""

        for c in f.read():
            if c.isdigit():
                current += c
            else:
                moves.append(current)
                moves.append(c)
                current = ""

        if current != "":
            moves.append(current)
    return moves

def get_starting_coords(board):
    y = 1
    for x in range(len(board[y])):
        if board[y][x] != ' ':
            return (y,x)
    assert 0


def simulate_movement(board, moves):
    y,x = get_starting_coords(board)
    print(y,x)
    facing = 'right' # right, left, up, down

    facings_right = ['right', 'down', 'left', 'up', 'right']
    facings_left = ['right', 'up', 'left', 'down', 'right']
    facings_val = {'right':0, 'down':1, 'left':2, 'up': 3}

    for move in moves:
        #print(move, y,x, facing)
        #input()
        if move.isdigit():
            for i in range(int(move)):
                zy,zx, facing = next_tile(y,x, board, facing)
                if board[zy][zx] == '#':
                    continue
                else:
                    y,x = zy,zx
                
        elif move == "R":
            for i in range(len(facings_right)):
                if facings_right[i] == facing:
                    facing = facings_right[i+1]
                    break
            else:
                assert 0
        elif move == "L":
            for i in range(len(facings_left)):
                if facings_left[i] == facing:
                    facing = facings_left[i+1]
                    break
            else:
                assert 0

    print(y,x, facing)
    print(y * 1000 + x * 4 + facings_val[facing])





    
row_length = 250

board = parse_board()
# for r in board:
#     print(''.join(r))
moves = parse_moves()
simulate_movement(board, moves)

