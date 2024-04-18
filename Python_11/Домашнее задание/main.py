# def next_move(board, x, y):
#     moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
#     valid_moves = []
#     for dx, dy in moves:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 0:
#             count = 0
#             for mx, my in moves:
#                 tx, ty = nx + mx, ny + my
#                 if 0 <= tx < len(board) and 0 <= ty < len(board[0]) and board[tx][ty] == 0:
#                     count += 1
#             valid_moves.append((nx, ny, count))
#     if valid_moves:
#         valid_moves.sort(key=lambda x: x[2])
#         return valid_moves[0][:2]
#     return None
#
# def knight_tour_recursive(board, x, y, move_num):
#     n = len(board)
#     board[x][y] = move_num
#     if move_num == n * n:
#         return True
#     next_position = next_move(board, x, y)
#     if next_position:
#         nx, ny = next_position
#         if knight_tour_recursive(board, nx, ny, move_num + 1):
#             return True
#     board[x][y] = 0
#     return False
#
#
# def knight_tour(n, start_x, start_y):
#     board = [[0] * n for _ in range(n)]
#     knight_tour_recursive(board, start_x, start_y, 1)
#     return board
#
#
# def print_board(board):
#     for row in board:
#         print(*row, sep='\t')
#
#
# n = 6
# start_x, start_y = int(input()), int(input())
# tour = knight_tour(n, start_x, start_y)
# print_board(tour)


# 1.
# nums = ['one', 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# nums_dict = {}
#
# for i in range(len(nums)):
#     if type(nums[i]) == str:
#         nums_dict[nums[i]] = []
#         last_key = nums[i]
#     else:
#         nums_dict[last_key].append(nums[i])
#
# print(nums_dict)


# 2.
# person = {'name': 'Kelly', 'age': 25, "salary": 8000, "city": "New York"}
# person['location'] = person.pop('city')
# print(person)


# 3.
# nums = {"один": 2, "два": 5, "три": 3, "четыре": 4}
# print(dict(list(nums.items())[:2]))


# 4.

# def db(**kwargs):
#     for key, value in kwargs.items():
#         my_dict[key] = value
#
#
# my_dict = {"one": 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name="Bob", age=31, weight=61, eyes_color='grey')
# print(my_dict)

# Лямбда - lambda - функции
# Анонимные функции
# lambda <входные параметры>: <выходное значение>
# print((lambda x: x**2)(3))

# sqr = lambda x: x**2
# print(sqr(3))

# words = ['cherry', 'banana', 'apricot', 'pineapple', 'apple']
# sorted_words = sorted(words, key=lambda word: word[-1])
# print(sorted_words)

# 1.
# Создайте лямбда функцию, которая определит
# является ли число четным
# print(is_even(4))
# >> True
# print(is_even(3))
# >> False

# words = ['apple', 'albinos', 'alaska', 'alpine', 'avocado']
# sorted_words = sorted(words, key=lambda word: (word[0], word[-1]))
# print(sorted_words)

# 2.
# Дан список строк:
# nicknames = ['Nikita11', 'Sanya', 'HeavenLord119', 'Egor']
# Необходимо отсортировать строки так, чтобы первее стояли строки
# у которых есть числа и которые длиннее (по приоритету)
# nicknames = ['Nikita11', 'SanyaSidorov', 'HeavenLord119', 'Egor']
# sorted_nicknames = sorted(nicknames, key=lambda word: (word.isalpha(), -len(word)))
# [print(nick) for nick in sorted_nicknames]


# 3.
# Напишите лямбда-функцию, которая принимает список словарей
# (каждый словарь представляет собой человека.
# Функция должна вернуть список имён женщин
# people = [
#     {'name': 'Alice', 'age': 30, 'gender': 'female'},
#     {'name': 'Bob', 'age': 25, 'gender': 'male'},
#     {'name': 'Eve', 'age': 35, 'gender': 'female'}
# ]
# # >> ['Alice', 'Eve']
# get_female_names = lambda people: [person['name'] for person in people if person['gender'] == 'female']
# print(get_female_names(people))

# 4.
# Напишите lambda-функцию, которая принимает список чисел
# А затем увеличивает каждое из чисел на значение его индекса
# [1, 2, 3, 4, 5] > [1, 3, 5, 7, 9]

# print((lambda nums: [nums[i] + i for i in range(len(nums))])([1, 2, 3, 4, 5]))

# print((lambda nums: [x + i for i, x in enumerate(nums)])([1, 2, 3, 4, 5]))

# nums = ['first', 'second', 'third', 'fourth', 'fifth']
# for i, value in enumerate(nums):
#     print(i, value)
#
# nums = ['first', 'second', 'third', 'fourth', 'fifth']
# for i in range(len(nums)):
#     print(i, nums[i])

