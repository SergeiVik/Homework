# Специальные методы

# class Human:
#     def __init__(self, fio, age):
#         self.fio = fio
#         self.age = age
#
#     def __str__(self):  # - возвращает строковое представление объекта
#         return self.fio + " Человек"
#
#     def __repr__(self):  # метод, аналогичный str, но на уровень ниже
#         return self.fio.split()[1]
#
#     def __add__(self, other):  # Оператор +
#         if isinstance(other, Human):
#             return self.fio + " + " + other.fio
#         elif isinstance(other, int):
#             return self.age + other
#
#     def __sub__(self, other):  # Оператор -
#         if isinstance(other, Human):
#             return self.age - other.age
#
#     def __mul__(self, other):  # Оператор *
#         if isinstance(other, Human):
#             raise NotImplementedError("Cannot multiply human on human")
#
#     def __truediv__(self, other):  # Оператор /
#         if isinstance(other, Human):
#             raise NotImplementedError("Cannot divide human on human")
#
#     def __eq__(self, other):  # Оператор ==
#         return self.fio == other.fio and self.age == other.age
#
#     def __ne__(self, other):  # Оператор !=
#         return self.fio != other.fio or self.age != other.age
#
#     def __gt__(self, other):  # Оператор >
#         pass
#
#     def __ge__(self, other):  # Оператор >=
#         pass
#
#     def __lt__(self, other):  # Оператор <
#         pass
#
#     def __le__(self, other):  # Оператор <=
#         pass


# h = Human("Петров Василий Борисович", 30)
# h2 = Human("Петров Василий Борисович", 30)
# h1 = Human("Васечкин Петр Борисович", 20)
# print(str(h))
# print(h != h1)

# 1.
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
#     def __add__(self, other):
#         new_numerator = (self.numerator * other.denominator +
#                          self.denominator * other.numerator)
#         new_denominator = self.denominator * other.denominator
#         common_part = gcd(new_numerator, new_denominator)
#         return Fraction(new_numerator/common_part,
#                         new_denominator/common_part)
#
#     def __sub__(self, other):
#         new_numerator = (self.numerator * other.denominator -
#                          self.denominator * other.numerator)
#         new_denominator = self.denominator * other.denominator
#         common_part = gcd(new_numerator, new_denominator)
#         return Fraction(new_numerator / common_part,
#                         new_denominator / common_part)
#
#     def __mul__(self, other):
#         new_numerator = self.numerator * other.numerator
#         new_denominator = self.denominator * other.denominator
#         common_part = gcd(new_numerator, new_denominator)
#         return Fraction(new_numerator / common_part,
#                         new_denominator / common_part)
#
#     def __truediv__(self, other):
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
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)


# 2.
# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def __str__(self):
#         return f"{self.day}/{self.month}/{self.year}"
#
#     @staticmethod
#     def is_leap_year(year):
#         return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
#
#     @staticmethod
#     def days_in_month(month, year):
#         months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         if Date.is_leap_year(year):
#             months[1] += 1
#         return months[month - 1]
#
#     def total_days(self):
#         days = 0
#         for year in range(self.year):
#             if Date.is_leap_year(year):
#                 days += 366
#             else:
#                 days += 365
#         for month in range(self.month):
#             days += Date.days_in_month(month, self.year)
#         days += self.day
#         return days
#
#     def __sub__(self, other):
#         return abs(self.total_days() - other.total_days())
#
#     def __iadd__(self, days):  # Оператор +=
#         day = self.day + days
#         month = self.month
#         year = self.year
#         while day > Date.days_in_month(month, year):
#             day -= Date.days_in_month(month, year)
#             month += 1
#             if month > 12:
#                 month = 1
#                 year += 1
#         return Date(day, month, year)
#
#
# a = Date(1, 1, 2000)
# b = Date(30, 4, 2000)
# print(a - b)
# a += 366
# print(a)
# a += 189
# print(a)

