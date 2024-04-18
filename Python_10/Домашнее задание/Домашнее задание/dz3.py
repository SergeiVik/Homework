# Задание 3
lst_search_employee = [
    {'name': 'Иванов Иван Иванович', 'tel': '+7(930) 524 66 57', 'email': 'ivanuv@mail.ru', 'post': 'Инженер',
     'skype': 'IvanovIvan'},
    {'name': 'Зайцев Роман Романович', 'tel': '+7(931) 624 63 54', 'email': 'zaytcev@mail.ru', 'post': 'Учитель',
     'skype': 'Zaytcev'},
    {'name': 'Борисов Александр Владимирович', 'tel': '+7(932) 564 76 17', 'email': 'bor@mail.ru',
     'post': 'Начальник склада', 'skype': 'BorisovA'},
    {'name': 'Гусейнов Магомед Гусейнович', 'tel': '+7(933) 525 16 07', 'email': 'gus@mail.ru', 'post': 'Врач',
     'skype': 'gusM'}]

print('Поиск сотрудника: 1')
print('Добавление сотрудника: 2')
print('Удаление сотрудника: 3')
print('Посмотреть полный список: 4')
print('Изменение данных: 5')
print('Введите "*" чтобы завершить')
input_number = input('Выберите действие: ')
while input_number != '*':
    c = 0
    # Поиск сотрудника
    if input_number == '1':
        search_employee = input('Введите имя сотрудника: ')
        for i in lst_search_employee:
            if search_employee == i['name']:
                print(
                    f'Есть такой сотрудника {i['name']}, его данные {i['tel']}, {i['email']}, {i['post']}, {i['skype']}')
                break
            else:
                c += 1
        if c == len(lst_search_employee):
            print('Такого сотрудника нет')
        c = 0

    # Добавление сотрудника
    elif input_number == '2':
        addendum_employee = input('Введите имя сотрудника: ')
        lst_search_employee.append({'name': addendum_employee, 'tel': 'пусто', 'email': 'пусто', 'post': 'пусто',
                                    'skype': 'пусто'})
        print('Добавлен')

    # Удаление сотрудника
    elif input_number == '3':
        del_employee = input('Введите сотрудника которого хотите удалить: ')
        for i in lst_search_employee:
            if del_employee == i['name']:
                lst_search_employee.pop(lst_search_employee.index(i))
                print('Удален')
                break
            else:
                c += 1
        if c == len(lst_search_employee):
            print('Такого сотрудника нет')

    # Просмотр полного списка
    elif input_number == '4':
        for i in lst_search_employee:
            print(f'Сотрудник {i['name']}, его данные {i['tel']}, {i['email']}, {i['post']}, {i['skype']}')

    # Изменение данных
    elif input_number == '5':
        for i in range(len(lst_search_employee)):
            print(
                f'{i + 1} {lst_search_employee[i]['name']}, его данные {lst_search_employee[i]['tel']}, {lst_search_employee[i]['email']}, {lst_search_employee[i]['post']}, {lst_search_employee[i]['skype']}')
        changing_employee = int(input('Введите номер сотрудника: '))
        changing_data = input('Что хотели бы изменить (1- имя, 2- телефон, 3- почту, 4- должность, 5- скайп)? ')
        if changing_data == '1':
            lst_search_employee[changing_employee - 1]['name'] = input('Введите новое имя: ')
            print("Успешно")
            print('----------------------------')
        elif changing_data == '2':
            lst_search_employee[changing_employee - 1]['tel'] = input('Введите новый номер: ')
            print("Успешно")
            print('----------------------------')
        elif changing_data == '3':
            lst_search_employee[changing_employee - 1]['email'] = input('Введите новую почту: ')
            print("Успешно")
            print('----------------------------')
        elif changing_data == '4':
            lst_search_employee[changing_employee - 1]['post'] = input('Введите новую должность: ')
            print("Успешно")
            print('----------------------------')
        elif changing_data == '5':
            lst_search_employee[changing_employee - 1]['skype'] = input('Введите новый скайп: ')
            print("Успешно")
            print('----------------------------')

    print('Поиск сотрудника: 1')
    print('Добавление сотрудника: 2')
    print('Удаление сотрудника: 3')
    print('Посмотреть полный список: 4')
    print('Изменение данных: 5')
    print('Введите "*" чтобы завершить')
    input_number = input('Выберите действие: ')

print('Сеанс завершен! До свидания!')
