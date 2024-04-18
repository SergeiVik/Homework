# def hello():
#     print("Hello")
#
#
# hello()

# def summa(a, b):
#     print(a + b)
#
#
# summa(3, 4)


# 1.
# def get_odd_nums_between(start, end):
#     [print(num) for num in range(start, end) if num % 2 != 0]
#
#
# get_odd_nums_between(1, 20)


# 2.
# def draw_line(length, direction, symbol):
#     end_of_line = ' ' if direction == 'h' else '\n'
#     [print(symbol, end=end_of_line) for _ in range(length)]
#     print()
#
#
# draw_line(15, 'h', '&')
# draw_line(5, 'v', '*')

# def division(a, b):
#     if b == 0:
#         print("Неверный делитель!")
#         return
#
#     return a / b
#
#
# print(division(5, 0))


# 3.
# def range_sum(start, end):
#     return sum(range(start, end + 1))
#
#
# print(range_sum(10, 15))


# 4.
# def is_prime(number):
#     return number > 1 and all(number % i for i in range(2, number // 2))
#
#
# print(is_prime(18))


# 5.
# def draw_rectangle(size, symbol, filled):
#     def is_edge(pos, size):
#         return pos[0] == 0 or pos[0] == size - 1 or pos[1] == 0 or pos[1] == size - 1
#
#     for i in range(size):
#         for j in range(size):
#             if not filled and not is_edge((i, j), size):
#                 print(" ", end=' ')
#             else:
#                 print(symbol, end=' ')
#         print()
#
#
# draw_rectangle(6, "*", True)


# 6.
# def is_palindrome(number):
#     new_num = 0
#     old_num = number
#     while old_num > 0:
#         new_num = new_num * 10 + old_num % 10
#         old_num //= 10
#     return new_num == number
#
#
# print(is_palindrome(493394))


# Позиционные аргументы и аргументы по ключу
# def hello(name="Имя", surname=''):
#     print("Привет", name, surname)
#
#
# hello(name='Никита', surname="Зайцев")

# 7.
# def draw_line(length=20, symbol='-'):
#     print(length * symbol)
#
#
# draw_line()
# draw_line(symbol='*')
# draw_line(10)
# draw_line(5, '&')

# Аннотация типов данных
# def summa(a: int, b: int) -> int:
#     """
#     Summarize two ints
#     :param a: Это первое число
#     :param b: Это второе число
#     :return: Int number
#     """
#     return a + b
#
#
# print(summa('new', 'vegas'))


# 8.
# def sum_of_digits(number, even_digits=True):
#     digits = list(map(int, list(str(number))))
#     start = 1 if even_digits else 0
#     return sum(digits[i] for i in range(start, len(digits), 2))
#
#
# print(sum_of_digits(9874023, False))
