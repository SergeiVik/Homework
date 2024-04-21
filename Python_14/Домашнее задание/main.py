# 6. Дан текстовый файл. Найти и заменить в нем заданное слово.
# Что искать и на что заменять определяется пользователем

# word_to_replace = input("Введите слово для замены: ")
# word_for_replace = input("Введите слово, на которое заменим: ")
# words_to_replace = [word_to_replace, word_to_replace.lower(), word_to_replace.capitalize()]
# with open("old.txt", 'r', encoding="utf-8") as in_file:
#     text = in_file.read()
#     for word in words_to_replace:
#         text = text.replace(word, word_for_replace)
#
# with open("old.txt", 'w', encoding="utf-8") as out_file:
#     out_file.write(text)


# ООП - Объектно-Ориентированное Программирование
# Классы - шаблоны, по которым создаются и управляются объекты
# Объекты - это экземпляры класса, которые представляют собой модель
# реальных объектов из жизни.

# У классов могут быть свойства - они также доступны от имени всех объектов.
# Как правило, свойствами наделяют не классы, а объекты в процессе создания
# внутри конструктора класса __init__
# Помимо свойств у классов/объектов есть методы. Методами называются функции,
# которые можно вызвать от имени любого объекта класса
# class Human:
#     def __init__(self, name, arms=2):
#         self.arms = arms
#         self.name = name
#
#     def say_hi(self):
#         print("Hello")
#
#     def get_name(self):
#         return f'**{self.name}**'
#
#
# a = Human("Никита")
# print(a.get_name())
#
# b = Human("Света")
# print(b.get_name())

# 1.
# class Human:
#     def __init__(self, fio, birthdate, phone, city, country, address):
#         self.fio = fio
#         self.birthdate = birthdate
#         self.phone = phone
#         self.city = city
#         self.country = country
#         self.address = address
#
#     def reset_info(self):
#         self.fio = input("Введите новое ФИО: ")
#         self.birthdate = input("Введите новую дату рождения: ")
#         self.phone = input("Введите новый номер телефона: ")
#         self.city = input("Введите новый город: ")
#         self.country = input("Введите новую страну: ")
#         self.address = input("Введите новый адрес: ")
#
#     def print_info(self):
#         print(
#             "Человек: \n"
#             "\tФИО: ", self.fio, '\n'
#             "\tДата рождения: ", self.birthdate, '\n'
#             "\tТелефон: ", self.phone, '\n'
#             "\tГород: ", self.city, '\n'
#             "\tСтрана: ", self.country, '\n'
#             "\tАдрес: ", self.address, '\n'
#         )
#
#     def get_fio(self):
#         return self.fio
#
#     def get_birthdate(self):
#         return self.birthdate
#
#     def get_phone(self):
#         return self.phone
#
#     def get_city(self):
#         return self.city
#
#     def get_country(self):
#         return self.country
#
#     def get_address(self):
#         return self.address
#
#
# a = Human("Семёнов Никита Сергеевич", "15.07.1996", "+7(999)-999-99-99",
#           "Москва", "Россия", "ул. Пушкина д. Колотушкина")
#
# a.print_info()
# a.reset_info()
# print(a.get_fio())
# print(a.get_city())

# 2. Создать класс, который будет представлять окружность.
# Он должен хранить радиус окружности, должен иметь возможность
# Задавать новый радиус и также должен иметь методы, который
# Возвращают площадь окружности и периметр окружности.
# Например:
# a = Circle(10)
# print(a.get_perimeter())
# >> 62.8
# print(a.get_area())
# >> 314
# a.set_radius(5)
# print(a.get_perimeter())
# >> 31.4

# class Circle:
#     def __init__(self, r):
#         self.radius = r
#
#     def set_radius(self, r):
#         self.radius = r
#
#     def get_area(self):
#         return 3.14 * self.radius * self.radius
#
#     def get_perimeter(self):
#         return 2 * self.radius * 3.14
#
#
# a = Circle(10)
# print(a.get_perimeter())
# print(a.get_area())
# a.set_radius(5)
# print(a.get_perimeter())

# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
#
#
# class Fraction:
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator
#
#     def set_numerator(self, numerator):
#         self.numerator = numerator
#
#     def set_denominator(self, denominator):
#         self.denominator = denominator
#
#     def sum(self, other):
#         new_numerator = (self.numerator * other.denominator +
#                          self.denominator * other.numerator)
#         new_denominator = self.denominator * other.denominator
#         common_part = gcd(new_numerator, new_denominator)
#         return Fraction(new_numerator/common_part,
#                         new_denominator/common_part)
#
#     def subtract(self, other):
#         new_numerator = (self.numerator * other.denominator -
#                          self.denominator * other.numerator)
#         new_denominator = self.denominator * other.denominator
#         common_part = gcd(new_numerator, new_denominator)
#         return Fraction(new_numerator / common_part,
#                         new_denominator / common_part)
#
#     def multiply(self, other):
#         new_numerator = self.numerator * other.numerator
#         new_denominator = self.denominator * other.denominator
#         common_part = gcd(new_numerator, new_denominator)
#         return Fraction(new_numerator / common_part,
#                         new_denominator / common_part)
#
#     def divide(self, other):
#         new_numerator = self.numerator * other.denominator
#         new_denominator = self.denominator * other.numerator
#         common_part = gcd(new_numerator, new_denominator)
#         return Fraction(new_numerator / common_part,
#                         new_denominator / common_part)
#
#     # Специальный метод / Магический метод / Dunder method - Double underscore method
#     def __str__(self):
#         return f'{int(self.numerator)}/{int(self.denominator)}'
#
#
# a = Fraction(14, 22)
# b = Fraction(17, 34)
# print(a.sum(b))
# print(a.subtract(b))
# print(a.multiply(b))
# print(a.divide(b))


# Классовый декоратор - staticmethod - используется с теми методами класса, которые не предназначены
# для изменения объекта, от имени которого они могут быть вызваны
# class Calculator:
#
#     @staticmethod
#     def subtract(num1, num2):
#         return num1 - num2
#
#     @staticmethod
#     def add(num1, num2):
#         return num1 + num2
#
#     @staticmethod
#     def multiply(num1, num2):
#         return num1 * num2
#
#     @staticmethod
#     def divide(num1, num2):
#         return num1 / num2
#
#
# print(Calculator.subtract(5, 2))
# print(Calculator.add(5, 2))
# print(Calculator.multiply(5, 2))
# print(Calculator.divide(5, 2))
# c = Calculator()
# print(c.subtract(10, 2))


class Calculator:
    @classmethod
    def subtract(cls, num1, num2):
        print(cls.__name__)
        return num1 - num2

    @classmethod
    def add(cls, num1, num2):
        return num1 + num2

    @classmethod
    def multiply(cls, num1, num2):
        return num1 * num2

    @classmethod
    def divide(cls, num1, num2):
        return num1 / num2


print(Calculator.subtract(5, 2))
print(Calculator.add(5, 2))
print(Calculator.multiply(5, 2))
print(Calculator.divide(5, 2))
c = Calculator()
print(c.subtract(10, 2))
