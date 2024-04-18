# Задание 1
lst_basketball_players = [{'name': 'Майкл Джордан', 'height': 198},
                          {'name': 'Коби Брайант', 'height': 198},
                          {'name': 'Карим Абдул-Джаббар', 'height': 219},
                          {'name': 'Мэджик Джонсон', 'height': 206}]

print('Поиск баскетболиста: 1')
print('Добавление баскетболиста: 2')
print('Удаление баскетболиста: 3')
print('Посмотреть полный список: 4')
print('Изменение данных: 5')
print('Введите "*" чтобы завершить')
input_number = input('Выберите действие: ')
while input_number != '*':
    c = 0
    # Поиск баскетболиста
    if input_number == '1':
        search_basketball_players = input('Введите имя баскетболиста: ')
        for i in lst_basketball_players:
            if search_basketball_players == i['name']:
                print(f'Есть такой баскетболист {i['name']}, его рост составляет {i['height']} см')
                break
            else:
                c += 1
        if c == len(lst_basketball_players):
            print('Такого баскетболиста нет')
        c = 0

    # Добавление баскетболиста
    elif input_number == '2':
        addendum_basketball_players, height_basketball_players = input('Введите имя баскетболиста: '), int(
            input('Введите рост баскетболиста: '))
        lst_basketball_players.append({'name': addendum_basketball_players, 'height': height_basketball_players})
        print('Добавлен')

    # Удаление баскетболиста
    elif input_number == '3':
        del_basketball_players = input('Введите баскетболиста которого хотите удалить: ')
        for i in lst_basketball_players:
            if del_basketball_players == i['name']:
                lst_basketball_players.pop(lst_basketball_players.index(i))
                print('Удален')
                break
            else:
                c += 1
        if c == len(lst_basketball_players):
            print('Такого баскетболиста нет')

    # Просмотр полного списка
    elif input_number == '4':
        for i in lst_basketball_players:
            print(f'Великий баскетболист {i['name']}, его рост составляет {i['height']} см.')

    # Изменение данных
    elif input_number == '5':
        for i in range(len(lst_basketball_players)):
            print(
                f'{i + 1} {lst_basketball_players[i]['name']}, его рост составляет {lst_basketball_players[i]['height']} см.')
        changing_data_basketball = int(input('Введите номер баскетболиста: '))
        changing_data = input('Что хотели бы изменить (1- имя, 2- рост)? ')
        if changing_data == '1':
            lst_basketball_players[changing_data_basketball - 1]['name'] = input('Введите новое имя: ')
            print("Успешно")
            print('----------------------------')
        elif changing_data == '2':
            lst_basketball_players[changing_data_basketball - 1]['height'] = int(input('Введите новое рост: '))
            print("Успешно")
            print('----------------------------')

    print('Поиск баскетболиста: 1')
    print('Добавление баскетболиста: 2')
    print('Удаление баскетболиста: 3')
    print('Посмотреть полный список: 4')
    print('Изменение данных: 5')
    print('Введите "*" чтобы завершить')
    input_number = input('Выберите действие: ')

print('Сеанс завершен! До свидания!')
