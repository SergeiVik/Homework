# Задание 1
# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)
#
#
# res = gcd(48, 18)
# print(res)

# Задание 2 "Быки и коровы"

import random


def generate_number():
    return random.randint(1000, 9999)


def cows_and_bulls(secret_num, guess, attempts=1):
    guess_str = str(guess)
    secret_str = str(secret_num)

    bulls = sum([1 for i in range(4) if guess_str[i] == secret_str[i]])
    cows = sum([1 for i in range(4) if guess_str[i] in secret_str and guess_str[i] != secret_str[i]])

    if bulls == 4:
        print(f'Поздравляем! Вы угадали число {secret_num} за {attempts} попыток')

    print(f"Быки: {bulls}, Коровы: {cows}")
    new_guess = int(input('Введите ваше предложение: '))
    cows_and_bulls(secret_num, new_guess, attempts + 1)


secret_number = generate_number()
print('Добро пожаловать в игру "Быки и коровы"!')
print('Попробуй угадать четырехзначное число.')
print(secret_number)
cows_and_bulls(secret_number, '0000')
