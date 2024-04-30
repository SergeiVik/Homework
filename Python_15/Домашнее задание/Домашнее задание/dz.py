# Задача 1
# class Circle:
#     def __init__(self, r):
#         self.r = r
#         self.f = (2 * 3.14) * self.r
#
#     def __eq__(self, other):
#         if isinstance(other, Circle):
#             return self.r == other.r
#         return False
#
#     def __lt__(self, other):
#         if isinstance(other, Circle):
#             return self.f < other.f
#         return False
#
#     def __gt__(self, other):
#         if isinstance(other, Circle):
#             return self.f > other.f
#         return False
#
#     def __le__(self, other):
#         if isinstance(other, Circle):
#             return self.f <= other.f
#         return False
#
#     def __ge__(self, other):
#         if isinstance(other, Circle):
#             return self.f >= other.f
#         return False
#
#     def __add__(self, other):
#         if isinstance(other, Circle):
#             return self.r + other.r
#         return False
#
#     def __sub__(self, other):
#         if isinstance(other, Circle):
#             return self.r - other.r
#
#     def __iadd__(self, other):
#         self.r += other
#         return self
#
#     def __isub__(self, other):
#         self.r -= other
#         return self
#
#     def __str__(self):
#         return f'Circle: {self.r}'
#
#
# c = Circle(14)
# c1 = Circle(14)
# print(c)
# print(c == c1)
# print(c < c1)
# print(c > c1)
# print(c <= c1)
# print(c >= c1)
# print(c + c1)
# print(c - c1)
# c += 1
# print(c)
# c -= 2
# print(c)


# Задача 2
# class Complex:
#     def __init__(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary
#
#     def __add__(self, other):
#         return Complex(self.real + other.real, self.imaginary + other.imaginary)
#
#     def __sub__(self, other):
#         return Complex(self.real - other.real, self.imaginary - other.imaginary)
#
#     def __mul__(self, other):
#         real_part = self.real * other.real - self.imaginary * other.imaginary
#         imaginary_part = self.real * other.imaginary + self.imaginary * other.real
#         return Complex(real_part, imaginary_part)
#
#     def __truediv__(self, other):
#         divisor = other.real ** 2 + other.imaginary ** 2
#         real_part = (self.real * other.real + self.imaginary * other.imaginary) / divisor
#         imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / divisor
#         return Complex(real_part, imaginary_part)
#
#     def __str__(self):
#         return f'{self.real} + {self.imaginary}i'
#
#
# c1 = Complex(2, 3)
# c2 = Complex(1, 4)
# print(c1)
# print(c2)
# print(c1 + c2)
# print(c1 - c2)
# print(c1 * c2)
# print(c1 / c2)


# Задача 3
# class Airplane:
#     def __init__(self, type, passengers):
#         self.type = type
#         self.passengers = passengers
#
#     def __eq__(self, other):
#         return self.type == other.type
#
#     def __iadd__(self, other):
#         self.passengers += other
#         return self
#
#     def __isub__(self, other):
#         self.passengers -= other
#         return self
#
#     def __lt__(self, other):
#         return self.passengers < other.passengers
#
#     def __gt__(self, other):
#         return self.passengers > other.passengers
#
#     def __le__(self, other):
#         return self.passengers <= other.passengers
#
#     def __ge__(self, other):
#         return self.passengers >= other.passengers
#
#     def __str__(self):
#         return f'Самолет: {self.type}, Пассажиров: {self.passengers}'
#
#
# boing = Airplane('Боинг', 30)
# super_jet = Airplane('СуперДжет', 50)
# print(boing)
# print(super_jet)
# print(boing == super_jet)
# boing += 1
# super_jet -= 1
# print(boing)
# print(super_jet)
# print(boing < super_jet)
# print(boing > super_jet)
# print(boing <= super_jet)
# print(boing >= super_jet)


# Задача 4
# class Flat:
#     def __init__(self, square):
#         self.square = square
#
#     def __eq__(self, other):
#         return self.square == other.square
#
#     def __ne__(self, other):
#         return self.square != other.square
#
#     def __lt__(self, other):
#         return self.square < other.square
#
#     def __gt__(self, other):
#         return self.square > other.square
#
#     def __le__(self, other):
#         return self.square <= other.square
#
#     def __ge__(self, other):
#         return self.square >= other.square
#
#     def __str__(self):
#         return f'Площадь квартиры: {self.square}'
#
#
# f = Flat('50')
# f2 = Flat('60')
# print(f)
# print(f2)
# print(f == f2)
# print(f != f2)
# print(f < f2)
# print(f > f2)
# print(f <= f2)
# print(f >= f2)
