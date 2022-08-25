field = [['@', '*', '.'],
        ['.', '.', '.'],
        ['.', '*', '*']]

x, y = 0, 0
file = open("command.txt", 'r')
alive = True

for line in file:
    line = line.replace("\n", "")
    if line == 'up':
        if (field[((y + 3) - 1) % 3][x] == '*'):
            print('you lose')
            alive = False
            break
        else:
            field[y][x] = '.'
            y = ((y + 3) - 1) % 3
            field[y][x] = '@'
    elif line == 'down':
        if (field[((y + 3) + 1) % 3][x] == '*'):
            print('you lose')
            alive = False
            break
        else:
            field[y][x] = '.'
            y = ((y + 3) + 1) % 3
            field[y][x] = '@'
    elif line == 'left':
        if (field[y][((x + 3) - 1) % 3] == '*'):
            print('you lose')
            alive = False
            break
        else:
            field[y][x] = '.'
            x = ((x + 3) - 1) % 3
            field[y][x] = '@'
    elif line == 'right':
        if (field[y][((x + 3) + 1) % 3] == '*'):
            print('you lose')
            alive = False
            break
        else:
            field[y][x] = '.'
            x = ((x + 3) + 1) % 3
            field[y][x] = '@'

if alive:
    print(*field, sep='\n')