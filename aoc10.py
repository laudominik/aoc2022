def emulate(ticks, instructions):
    
    ip = -1
    cycles_left = 0
    to_add = 0
    reg_x = 1

    pixels = []

    for i in range(0, ticks):
    
        if cycles_left == 0:
            reg_x += to_add
            ip = ip + 1
            if ip >= len(instructions):
                break
            instruction = instructions[ip].split(' ')
            if instruction[0] == 'noop':
                to_add = 0
                cycles_left = 0
            elif instruction[0] == 'addx':
                to_add = int(instruction[1])
                cycles_left = 1
        else:
            cycles_left-=1

        if abs(i % 40 - reg_x) <= 1:
            pixels.append('#')
        else:
            pixels.append('.')

    screen = [pixels[n:n+40] for n in range(0, len(pixels), 40)]
    for row in screen:
        print(''.join(row))

    return reg_x * ticks

with open("input10.txt", "r") as f:
    instructions = f.read().split('\n')
    #print(sum([emulate(x, instructions) for x in range(20,260)[::40]]))
    print(emulate(260,instructions))



