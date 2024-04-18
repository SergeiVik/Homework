# Задание 1
print('''Выберите какую фигуру отрисовать!
а)
б)
в)
г)
д)
е)
ж)
з)
и)
к)
''')
alpha_input = ''
while alpha_input != 'стоп':
    alpha_input = input('Введите букву: ')
    e = 12
    if alpha_input == 'а':
        for i in range(7, 0, -1):
            print('  ' * (7 - i), end='')
            print('* ' * i)

    elif alpha_input == 'б':
        for i in range(1, 8):
            print('* ' * i)

    elif alpha_input == 'в':
        for i in range(7, 0, -1):
            if i % 2 != 0:
                print(' ' * (7 - i), end='')
                print('* ' * i)

    elif alpha_input == 'г':
        for i in range(1, 8):
            if i % 2 != 0:
                print(' ' * (7 - i), end='')
                print('* ' * i)

    elif alpha_input == 'д':
        for i in range(7, 0, -1):
            if i % 2 != 0:
                print(' ' * (7 - i), end='')
                print('* ' * i)
        for i in range(1, 8):
            if i % 2 != 0:
                print(' ' * (7 - i), end='')
                print('* ' * i)

    elif alpha_input == 'е':
        for i in range(1, 5):
            print(('* ' * i) + (' ' * (e)) + (' *' * i))
            e = e - 4
        for i in range(0, 4):
            print(('* ' * (3 - i)) + ('    ' * (i + 1)) + ((' *' * (3 - i))))

    elif alpha_input == 'ж':
        for i in range(1, 5):
            print('* ' * i)
        for i in range(0, 4):
            print('* ' * (3 - i))

    elif alpha_input == 'з':
        for i in range(1, 5):
            print(('  ' * i) + (' ' * (e)) + (' *' * i))
            e = e - 4
        for i in range(0, 4):
            print(('  ' * (3 - i)) + ('    ' * (i + 1)) + ((' *' * (3 - i))))

    elif alpha_input == 'и':
        for i in range(0, 8):
            print('* ' * (7 - i))

    elif alpha_input == 'к':
        for i in range(1, 8):
            print('  ' * (7 - i) + (' *' * i))
