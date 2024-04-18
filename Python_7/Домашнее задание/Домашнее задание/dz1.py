# Задание 1
# def summ_elements_list(list):
#    new_list = []
#    num = 0
#    for i in list:
#        for j in range(1, i + 1):
#            num += j
#        new_list.append(num)
#        num = 0
#
#    return new_list
#
#
# print(summ_elements_list([2, 10, 9, 4, 16]))

# Задание 2
# def min_element_in_list(list):
#     min_element = list[0]
#     for i in list:
#         if i < min_element:
#             min_element = i
#
#     return min_element
#
#
# print(min_element_in_list([53, 20, 15, 10, 62]))

# Задание 3
# def prime_number_list(list):
#     prime_number = []
#     count = 0
#     for i in list:
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 count += 1
#         if count == 2:
#             prime_number.append(i)
#         count = 0
#
#     return prime_number
#
#
# print(prime_number_list([2, 20, 3, 10, 29]))


# Задание 4
# def del_element(list, number):
#     for i in list:
#         if i == number:
#             list.pop(list.index(i))
#
#     return list
#
#
# print(del_element([2, 20, 2, 10, 29], 2))

# Задание 5
# def common_elements(list_1, list_2):
#     new_list = []
#     for i in list_1:
#         if i in list_2:
#             new_list.append(i)
#     return new_list
#
#
# print(common_elements([53, 20, 15, 10, 62], [2, 20, 2, 10, 29]))


# Задание 6
# def exponentiation(list, degree):
#     new_list = [i ** degree for i in list]
#     return new_list
#
#
# print(exponentiation([53, 20, 15, 10, 62], 2))
