# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)
#
#
# num1 = 48
# num2 = 18
# result = gcd(num1, num2)
# print(f"НОД чисел {num1} и {num2} равен {result}")


# def generate_secret_number():
#     # Генерируем случайное четырёхзначное число без повторяющихся цифр
#     from random import sample
#     return ''.join(sample('0123456789', 4))
#
#
# def compare_numbers(secret, guess):
#     bulls, cows = 0, 0
#     for i in range(4):
#         if secret[i] == guess[i]:
#             cows += 1
#         elif secret[i] in guess:
#             bulls += 1
#     return bulls, cows
#
#
# def play_game(secret, attempts=0):
#     guess = input("Введите вашу догадку (четырёхзначное число): ")
#     if not guess.isdigit() or len(guess) != 4:
#         print("Пожалуйста, введите четырёхзначное число.")
#         return play_game(secret, attempts)
#
#     bulls, cows = compare_numbers(secret, guess)
#     attempts += 1
#     print(f"Быки: {bulls}, Коровы: {cows}")
#
#     if cows == 4:
#         print(f"Поздравляем! Вы угадали число за {attempts} попыток.")
#     else:
#         play_game(secret, attempts)
#
#
# if __name__ == "__main__":
#     secret_number = generate_secret_number()
#     print(secret_number)
#     print("Добро пожаловать в игру 'Быки и коровы'!")
#     play_game(secret_number)


# 1.
# sets = [{1, 2}, {2, 3}, {1, 4, 5}, {6}, {5, 6, 7}]
# all_sets = set()
# # for my_set in sets:
# #     for el in my_set:
# #         all_sets.add(el)
# [all_sets.update(my_set) for my_set in sets]
# print(all_sets)
# print(len(all_sets))
# print('Min:', min(all_sets))
# print('Max:', max(all_sets))

# 2.
# drawing = {'Marina', 'Jenya', 'Sveta'}
# music = {'Kostya', 'Jenya', 'Ilya'}
# print('Only one hobby:', drawing.symmetric_difference(music))
# print("Both hobbies:", drawing.intersection(music))
# drawing.discard('Jenya')
# print("Drawing artists:", drawing)

# set.issubset(set)
# set.issuperset(set)
# 3.
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
#
# print("Объединение множеств: ", set1.union(set2))
# print("Пересечение множеств: ", set1.intersection(set2))
# print("Симметричная разность множеств: ", set1.symmetric_difference(set2))
# discarding_els = set1.intersection(set2)
# print("Элементы из второго множество входящие в первое: ", discarding_els)
# set1 -= discarding_els
# print("Первое множество после вычитания элементов:", set1)
# print('set2 является надмножеством для:', {4, 5, 7}, set2.issuperset({4, 5, 7}))
# print('set2 является надмножеством для:', {8, 3, 4}, set2.issuperset({8, 3, 4}))
# set3 = {5, 8, 4, 7, 6}
# print('set2 является правильным надмножеством для:', set3, set2.issuperset(set3) and set2 != set3)

# Словари - dict() - dictionary
# my_dict = {1: 2, 3: 4, 3: 5}
# print(type(my_dict))
# print(len(my_dict))
# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# print(my_dict[1])
# print(my_dict)
# Ключом в словаре может быть только неизменяемый тип данных
# Кортеж, Строка, Число, Булевое значение, NoneType
# my_dict = {[1]: {2: 3}, False: 2}
# print(my_dict)

# color = input("Какой свет горит на светофоре?")
# color_dict = {'Красный': "Жди зеленого!",
#               'Жёлтый': "Приготовься ехать!",
#               "Зеленый": "Газу! Газу!"}
# print(color_dict.get(color, "Такого света на светофоре быть не может!"))

# my_dict = {1: 2, 3: 4, 4: 5}
# Чтобы добавить что-то в словарь или изменить, что уже есть:
# print(my_dict)
# my_dict[5] = '12'
# print(my_dict)
# my_dict[5] = '20'
# print(my_dict)

# Удалить что-то из словаря:
# my_dict.pop(5)
# print(my_dict)
# del my_dict[5]
# print(my_dict)

# Способы генерации словарей
# nums = [1, 2, 3, 4, 5]
# my_dict = dict.fromkeys(nums, 0)
# print(my_dict)
# my_dict = {i: i**0.5 for i in range(10)}
# print(my_dict)

# Скорее всего никогда не используете
# my_dict = {1: 2, 3: 4, 4: 5}
# my_dict.setdefault(3, 10)
# print(my_dict)

# 1.
# nums = {"x1": 3, "x2": 7, "x3": 4}
# mul = 1
# for i in nums.values():
#     mul *= i
# print(mul)


# 2.
# veggies = {}
# for i in range(1, 5):
#     veg = input("Введите овощь: ")
#     veggies[i] = veg
# print(veggies)
# el = int(input("Какой элемент исключить: "))
# veggies.pop(el)
# print(veggies)

# 3.
# x = {"a": 1, "b": 2}
# y = {"b": 3, "c": 4}
# c = {}
# for key in x:
#     c[key] = x[key]
# for key in y:
#     c[key] = y[key]
# print(c)

# 4.
# person = {'name': 'Kelly', 'age': 25, "salary": 8000, "city": "New York"}
# name_and_salary = {'name': person["name"], 'salary': person["salary"]}
# print(name_and_salary)
# [person.pop(key) for key in name_and_salary]
# print(person)
