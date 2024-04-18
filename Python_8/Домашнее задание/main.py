# Рекурсия - это повторение какого-то действия
# Рекурсивная функция - это такая функция, которая
# вызывает саму себя внутри себя

# def out(i):
#     print(i)
#     if i > 0:
#         out(i - 1)
#
#
# out(10)

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
#
#
# print(factorial(5))

# 1.
# def power(num, x):
#     if x == 0:
#         return 1
#     return num * power(num, x-1)
#
#
# print(power(5, 3))

# 2.
# def range_summa(a, b):
#     if a == b:
#         return b
#     return a + range_summa(a + 1, b)
#
#
# print(range_summa(9, 10))

# 3. Функция нахождения N числа Фибоначчи

# def fibo(n):
#     if n in (1, 2):
#         return n - 1
#     return fibo(n - 1) + fibo(n - 2)
# print(fibo(40))

# def fibo(n, nums=None):
#     if not nums:
#         nums = [0, 1]
#     if n > 2:
#         nums.append(nums[-1] + nums[-2])
#         fibo(n - 1, nums)
#     return nums[-1]
#
#
# print(fibo(999))


# 4. Крестики-нолики
# def won_game(symbol, field):
#     for row in field:
#         if row[0] == row[1] == row[2] == symbol:
#             return True
#     for col in range(3):
#         if field[0][col] == field[1][col] == field[2][col] == symbol:
#             return True
#     if (field[0][0] == field[1][1] == field[2][2] == symbol) or \
#        (field[0][2] == field[1][1] == field[2][0] == symbol):
#         return True
#     return False
#
#
# field = [['*', '*', '*'],
#          ['*', '*', '*'],
#          ['*', '*', '*']]
# i = 0
# while i < 9:
#     if i % 2 == 0:
#         symbol = "X"
#     else:
#         symbol = 'O'
#     print(f"Ход: {i + 1}. Ходят {symbol}")
#     for row in field:
#         print(*row)
#     try:
#         row = int(input("Введите ряд (1-3): ")) - 1
#         column = int(input("Введите столбик (1-3): ")) - 1
#     except ValueError:
#         print("Неверный ввод! Вы должны ввести только число от 1 до 3!")
#         continue
#     if row < 0 or row > 2 or column < 0 or column > 2:
#         print("Неверный ввод строки или столбца!")
#         continue
#     elif field[row][column] != '*':
#         print("В этой клетке уже что-то стоит!")
#         continue
#     field[row][column] = symbol
#     i += 1
#     if won_game(symbol, field):
#         print(f"{symbol} победили! Игра окончена")
#         for row in field:
#             print(*row)
#         break
# else:
#     print("Ничья")
#     for row in field:
#         print(*row)


# 5.
# import random
#
# def find_min_sum(nums, start=0, min_sum=100, min_pos=0):
#     if start > len(nums) - 10:
#         return min_sum, min_pos
#
#     current_sum = sum(nums[start:start+10])
#
#     if current_sum < min_sum:
#         min_sum = current_sum
#         min_pos = start
#
#     return find_min_sum(nums, start+1, min_sum, min_pos)
#
#
# nums = [random.randint(1, 10) for _ in range(100)]
# min_sum, pos = find_min_sum(nums)
# print(*nums[:pos], '\033[92m', *nums[pos:pos+10], '\033[97m', *nums[pos+10:])
# print(pos, min_sum)
