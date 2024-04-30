# class Circle:
#     def __init__(self, r):
#         self.r = r
#         # self.area = 3.14 * self.r ** 2
#
#     @property  # с en. - "свойство"
#     def area(self):
#         return 3.14 * self.r ** 2
#
#     @area.setter
#     def area(self, value):
#         print("Area of circle shouldn't be changed exclusively!")
#         self.r = (value / 3.14) ** 0.5
#
#     @area.deleter
#     def area(self):
#         raise Exception("Area of circle couldn't be deleted!")
#
#
# c = Circle(5)
# print(c.area)
# c.area = 10
# print(c.area)
# del c.area
# print(c.r)


# ООП - Наследование, Инкапсуляция, Полиморфизм

# Наследование
# class Horse:
#     def __init__(self, legs, weight, height, color):
#         self.legs = legs
#         self.weight = weight
#         self.height = height
#         self.color = color
#
#     def run(self):
#         print(f"Horse {self} is running")
#
#
# class Pegasus(Horse):
#     def __init__(self, legs, weight, height, color, width_of_wings):
#         # Horse.__init__(self, legs, weight, height, color)
#         super().__init__(legs, weight, height, color)
#         self.width_of_wings = width_of_wings
#
#
# p = Pegasus(10, 20, 30, 'red', '')
# p.run()


# class Ship:
#     def __init__(self, length, height, max_speed):
#         self.length = length
#         self.height = height
#         self.max_speed = max_speed
#
#     def get_info(self):
#         return f"Length = {self.length}\nHeight = {self.height}\nSpeed = {self.max_speed}"
#
#
# class Frigate(Ship):
#     def __init__(self, length, height, max_speed, cannons):
#         super().__init__(length, height, max_speed)
#         self.cannons = cannons
#
#     def get_info(self):
#         ship_info = super().get_info()
#         return f"{ship_info}\nCannons = {self.cannons}"
#
#
# ship1 = Ship(100, 100, 20)
# print(ship1.get_info())
# print("-"*20)
# ship2 = Frigate(100, 100, 20, 16)
# print(ship2.get_info())


# Инкапсуляция

# class Human:
#     def __init__(self, fio, address, phone_number):
#         self.__fio = fio
#         self.address = address
#         self.phone_number = phone_number
#
#     def get_fio(self, auth_key):
#         if auth_key == "1234":
#             return self.__fio
#         else:
#             return "Invalid Auth"
#
#     def __autobiography__(self):
#         return "Hi died yong"
#
#
# h = Human("Фамилия Имя Отчество", "123", "+79999999999")
# print(h._Human__fio)
# print(h.get_fio("1234"))
# # print(h.__fio)
# h.__fio = 123
# print(h.__fio)
# print(h.get_fio("1234"))


# Полиморфизм - это свойство объекта подражать другим объектам
# Полиморфизм (программирование) - это возможность сущности(функция или класс)
# вести себя одинаково с разными типами данных

# def summa(a: int | str | float, b: int | str | float) -> int | str | float:
#     return a + b
#
#
# print(summa(1, 2))
# print(summa("1", "2"))
# print(summa(1.5, 2.5))


# Абстрактный класс - это класс, у которого не может быть объектов
# from abc import ABC, abstractmethod

# Абстрактный метод - это декоратор, который обеспечивает, что у
# всех дочерних классов от абстрактного будет реализация этого метода

# class Enemy(ABC):
#     def __init__(self, hp, move_speed, image):
#         self.hp = hp
#         self.move_speed = move_speed
#         self.image = image
#
#     @abstractmethod
#     def move(self):
#         print("Enemy object couldn't move!")
#
#
# class Skeleton(Enemy):
#     def __init__(self, hp=100, move_speed=50, image="images"):
#         super().__init__(hp, move_speed, image)
#
#     def move(self):
#         print(f"Skeleton is moving with move speed: {self.move_speed}")
#
#
# skelet = Skeleton()
# skelet.move()
#
# enemy = Enemy(50, 50, 'images')
# enemy.move()


# class A:
#     def __init__(self):
#         self.aaa = "aaa"
#
#     def a(self):
#         print("a")
#
#
# class B(A):
#     def __init__(self):
#         self.bbb = "bbb"
#
#     def b(self):
#         print("b")
#
#
# class C(A, B):
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#
#
# c = C()
# print(c.aaa)
# print(c.bbb)
# c.a()
# c.b()

