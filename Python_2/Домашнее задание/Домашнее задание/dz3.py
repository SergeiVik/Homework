# Задание 1
# num = int(input('Ввдите число от 1 до 100: '))
#
# if num < 1 or num > 100:
#     print('Ошибка! Неверный ввод!')
# elif num % 3 == 0 and num % 5 == 0:
#     print('Fizz Buzz')
# elif num % 3 == 0:
#     print('Fizz')
# elif num % 5 == 0:
#     print('Buzz')

# Задание 2
# num = int(input('Введите число: '))
# degree = int(input('Введите возводимую степень от 1 до 7: '))
#
# if degree == 0:
#     print(num ** degree)
# elif degree == 1:
#     print(num ** degree)
# elif degree == 2:
#     print(num ** degree)
# elif degree == 3:
#     print(num ** degree)
# elif degree == 4:
#     print(num ** degree)
# elif degree == 5:
#     print(num ** degree)
# elif degree == 6:
#     print(num ** degree)
# elif degree == 7:
#     print(num ** degree)

# Задание 3
# price = int(input('Введите сколько минут разговора: '))
# myOper = input('Введите ваш оператор: ')
# oper = input('Введите оператор на который звоните: ')
#
# if myOper == 'Мегафон' and oper == 'Билайн' or myOper == 'Билайн' and oper == 'Мегафон':
#     print('Стоимость равна 0.5 руб. минута')
#     print('Ваш разговор будет стоить', price * 0.5)
# elif myOper == 'МТС' and oper == 'Мегафон' or myOper == 'Мегафон' and oper == 'МТС':
#     print('Стоимость равна 0.4 руб. минута')
#     print('Ваш разговор будет стоить', price * 0.4)
# elif myOper == 'МТС' and oper == 'Билайн' or myOper == 'Билайн' and oper == 'МТС':
#     print('Стоимость равна 0.6 руб. минута')
#     print('Ваш разговор будет стоить', price * 0.6)

# Задание 4
m1 = int(input('Введите сумму продаж для 1-ого менеджера: '))
m2 = int(input('Введите сумму продаж для 2-ого менеджера: '))
m3 = int(input('Введите сумму продаж для 3-ого менеджера: '))

if m1 >= 1000:
    m1 = 200 + 200 + (m2 * 8) / 100
elif m1 >= 500 and m1 < 1000:
    m1 = 200 + (m1 * 5) / 100
elif m1 < 500:
    m1 = 200 + (m1 * 3) / 100
print(m1)
if m2 >= 1000:
    m2 = 200 + 200 + (m2 * 8) / 100
elif m2 >= 500 and m2 < 1000:
    m2 = 200 + (m2 * 5) / 100
elif m2 < 500:
    m2 = 200 + (m2 * 3) / 100
print(m2)
if m3 >= 1000:
    m3 = 200 + 200 + (m2 * 8) / 100
elif m3 >= 500 and m2 < 1000:
    m3 = 200 + (m3 * 5) / 100
elif m3 < 500:
    m3 = 200 + (m3 * 3) / 100
print(m3)
