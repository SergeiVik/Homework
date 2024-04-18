# print("Hello World!")
# name = 'Егор'  # str - string - нить(строка)
# age = 20  # int - integer - целое число
# exp = 3.5  # float - floating point number - число с плавающей точкой
# trained = True  # (False) bool - boolean - булевы числа
# None - NoneType - ничего (заглушка)

# Типизация в JavaScript - Неявная Слабая Динамическая
# Типизация в Python - Неявная Сильная Динамическая
# Неявная - не нужно указывать тип данных при создании переменной
# Сильная - запрещены операции с неявным приведением типов данных
# Динамическая - переменная может менять тип данных по ходу программы

# Правила именования переменных:
# JavaScript - lowerCamelCase
# Python - snake_case
# Латинские символы, цифры и "_" и переменная не может начинаться с цифры

# name = input("Введите ваше имя: ")

# Арифметические операторы
# +,-,*,/,
# // - целочисленное деление
# % - остаток от деления
# ** - возведение в степень
# name = 'Егор'
# age = 10
# years = 3.5
# result = True

# print(age + years)  # int + float
# print(age + result)  # int + bool
# print(name + age)  # can only concatenate str (not "int") to str
# print(age + name)  # unsupported operand type(s) for +: 'int' and 'str'
# print(name * age)
# print(name * years)  # can't multiply sequence by non-int of type 'float'
# print(name + ' Крутой')

# int, float, str, bool
# type
# name = 'Егор'  # str
# age = 10  # int
# years = 3.5  # float
# exp = '1.5'  # str
# result = True  # bool
# print(int(years))
# print(type(str(age)))
# print(type(age))
# print(float(exp))
# age = str(age)
# print(type(age))

# print(bool(5)) - True
# print(bool(-1)) - True
# print(bool('Hello')) - True
# print(bool(' ')) - True
# print(bool(0)) - False
# print(bool('')) - False
# print(bool(None)) - False
# print(bool(False)) - False
# print(print())

# age = input('Введите ваш возраст: ')
# print(type(age))
# a = 999999
# b = '999999'
# print(id(a))
# print(id(b))

# ! Всё в Python является объектом
# a = print
# print(a)
# a(10 + 15)
# print("Nothing \nwill work \nunless you do")
# print("""Nothing
# will work
# unless you do""")

# print(
#                             1
#
# )
# print('Nothing ' 'will work ' 'unless you do')

# print("Nothing \n\twill work \n\t\tunless you do")
# print("""Nothing
#     will work
#         unless you do""")

# print(123)

# num = int(input('Введите число: '))
# print(num // 10)
# print(num % 10)

# num = int(input('Введите число: '))
# a = num // 100
# b = num // 10 % 10
# c = num % 10
# print(a)
# print(b)
# print(c)
# print(a + b + c)


# num1 = int(input('Введите цифру: '))
# num2 = int(input('Введите цифру: '))
# print(num1 * 10 + num2)
