# Цикл For
# Конец диапазона всегда не включается. Начало всегда включается
# По умолчанию, начало - 0, а шаг - 1
# for i in range(5):
#     print(i)
# for i in range(5, 10):
#     print(i)
# for i in range(5, 15, 3):
#     print(i)
# for i in range(-10, 10):
#     print(i)
# for i in range(10, 0, -2):
#     print(i)

# 1.
# n1 = int(input("Введите начало: "))
# n2 = int(input("Введите конец: "))
# if n1 % 2 == 0:
#     n1 += 1
# for i in range(n1, n2, 2):
#     print(i)


# 2.
# n1 = int(input("Введите число: "))
# n2 = int(input("Введите начало: "))
# if n1 < n2:
#     n1, n2 = n2, n1
# for i in range(n1, n2, -1):
#     print(i)

# 3.
# n1 = int(input("Введите начало: "))
# n2 = int(input("Введите конец: "))
# summa = 0
# for i in range(n1, n2):
#     summa += i
#
# print('Сумма:', summa)
# print("Среднее:", summa / (n2 - n1))

# 4.
# n = int(input('Введите число: '))
# f = 1
# for i in range(2, n + 1):
#     f *= i
#
# print(f)

# 5.
# symbol = input("Введите символ: ")
# length = int(input("Введите длину строки: "))
# print(symbol * length)
#
# for i in range(length):
#     print(symbol, end='')


# Исключения


# try:
#     age = int(input("Сколько вам лет?"))
#     years = int(input("Сколько лет вы тут живете?"))
#     if years < 0:
#         raise RuntimeError
# except ValueError:
#     print('Что-то пошло не так:')
#     # print(age)  # этой переменной может не существовать, поэтому код потенциально опасный
# except TypeError:
#     print("Что-то ОПЯТЬ пошло не так")
# except Exception:
#     print("Неверное количество лет!")
# else:
#     print("Да кто его знает, что тут происходит")
# finally:
#     print("Опасный блок кода завершился")


# 6.
# num = int(input("Введите число: "))
# for i in range(1, 10):
#     print(i, "*", num, "=", i * num)


# Цикл While
# password = input("Введите пароль: ")
# while password != '1234':
#     print("Пароль неверный!")


# 7.
# start = int(input("Введите начало диапазона: "))
# end = int(input("Введите конец диапазона: "))
#
# x = int(input("Введите число: "))
# while x > end or x < start:
#     print("Число не в диапазоне!")
#     x = int(input("Введите число: "))
#
# for i in range(start, end + 1):
#     if i == x:
#         print("!" + str(x) + "!", end=' ')
#     else:
#         print(i, end=" ")


# 8. Угадай число!
import random
import time

print("Я загадал число от 1 до 500. Попробуй его угадать!")
x = random.randint(1, 500)
start = time.time()
n = int(input())
tries = 1
while n != x:
    if n > x:
        print("Моё число меньше, чем твоё!")
    else:
        print("Моё число больше, чем твоё!")
    tries += 1
    n = int(input())

print("Ты угадал число! Поздравляю!")
print(f"Ты смог сделать это за {tries} попыток")
print(f"На это ушло {round(time.time() - start)} секунд")
