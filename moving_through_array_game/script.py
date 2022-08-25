field = [['@', '*', '.'],
        ['.', '.', '.'],
        ['.', '*', '*']]

print(*field, sep='\n')
x, y = 0, 0

while True:
    command = input()
    if command == 'up':
        if (field[((y + 3) - 1) % 3][x] == '*'):
            print('wall, try again')
            print(*field, sep='\n')
        else:
            field[y][x] = '.'
            y = ((y + 3) - 1) % 3
            field[y][x] = '@'
            print(*field, sep='\n')
    elif command == 'down':
        if (field[((y + 3) + 1) % 3][x] == '*'):
            print('wall, try again')
            print(*field, sep='\n')
        else:
            field[y][x] = '.'
            y = ((y + 3) + 1) % 3
            field[y][x] = '@'
            print(*field, sep='\n')
    elif command == 'left':
        if (field[y][((x + 3) - 1) % 3] == '*'):
            print('wall, try again')
            print(*field, sep='\n')
        else:
            field[y][x] = '.'
            x = ((x + 3) - 1) % 3
            field[y][x] = '@'
            print(*field, sep='\n')
    elif command == 'right':
        if (field[y][((x + 3) + 1) % 3] == '*'):
            print('wall, try again')
            print(*field, sep='\n')
        else:
            field[y][x] = '.'
            x = ((x + 3) + 1) % 3
            field[y][x] = '@'
            print(*field, sep='\n')
    elif command == 'exit':
        break
    else:
        print('unknown command')
