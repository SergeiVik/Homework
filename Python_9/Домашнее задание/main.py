# Кортежи - tuple - неизменяемый
# nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # круглые скобки не преобразуют
# набор элементов в кортеж. Это происходит автоматически при присвоении
# нескольких значений в одну переменную
# print(nums[0])  # - не вызовет ошибок
# nums[0] = 5  # - вызовет TypeError
# print(nums.count(123))
# print(nums.index(5))

# nums = 1, 2, 3, 4, 5
# nums = tuple(i for i in range(1, 10))
# nums = tuple(range(1, 10))
# print(nums)

# 1.
# fruits = 'apple', 'banana', 'cherry', 'mango', 'apple', 'banana', 'orange'
# fruit = input("Input fruit name: ")
# print(f"Количество {fruit} в кортеже равно {fruits.count(fruit)}")

# 2.
# fruits = 'apple', 'bananamango', 'cherry', 'mango', 'apple', 'banana', 'orange-banana'
# fruit = input("Input fruit name: ")
# count = sum(1 if fruit in fr else 0 for fr in fruits)
# print(count)
#

# 3.
# cars = 'BMW', 'Toyota', 'Renault', 'Kia', 'Hyundai', 'Ford', 'Honda', 'BMW'
# print(cars)
# car1 = input("Введите, какую марку заменить: ")
# car2 = input("Введите, на что заменить: ")
# # 1.
# new_cars = tuple(car2 if old_car == car1 else old_car for old_car in cars)
#
# print(new_cars)

# 4.
# def slicer(nums, num):
#     if num not in nums:
#         return tuple()
#     if nums.count(num) == 1:
#         return nums[nums.index(num):]
#
#     start = nums.index(num)
#     end = start + 1
#     for n in nums[start + 1:]:
#         end += 1
#         if n == num:
#             break
#     return nums[start:end]
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# 5.
# import random
#
# def create_tuple(start, end):
#     return tuple(random.randint(start, end) for i in range(10))
#
# t1 = create_tuple(0, 5)
# t2 = create_tuple(-5, 0)
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3)
# print(f"0 = {t3.count(0)}")

# 6.
# def get_reversed_unique_items(nums):
#     unique_items = []
#     for num in nums[::-1]:
#         if num not in unique_items:
#             unique_items.append(num)
#     return tuple(unique_items)
#
#
# print(get_reversed_unique_items([1, 2, 3, 3, 2]))
# print(get_reversed_unique_items([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))

# Множества - set() - неупорядочены и уникальны
# nums = set()
# nums = {1, 2, 3, 4, 5, 5, 5}
# # print(nums)
# nums1 = {5, 4, 6, 7, 3, 2, 'a', 'b', 'c'}
# # print(nums1)
# print(f"Пересечение (Логическое И): {nums.intersection(nums1)}")
# print(f"Объединение (Логическое ИЛИ): {nums.union(nums1)}")
# print(f"Вычитание (Логическое НЕ): {nums.difference(nums1)}")
# print(f"Исключающее ИЛИ (XOR): {nums.symmetric_difference(nums1)}")
# print(nums & nums1)
# print(nums | nums1)
# print(nums ^ nums1)
# def summa(a: int | str | float, b: int) -> int | float | str:
#     pass

# 1.
# def to_set(array):
#     return set(array), len(set(array))
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))
