# Задание 1
# import random
#
# students = [
#     {'name': 'Alice', 'math': [random.randint(70, 90) for _ in range(3)],
#      'english': [random.randint(70, 90) for _ in range(3)]},
#     {'name': 'Bob', 'math': [random.randint(70, 90) for _ in range(3)],
#      'english': [random.randint(70, 90) for _ in range(3)]},
#     {'name': 'Eve', 'math': [random.randint(70, 90) for _ in range(3)],
#      'english': [random.randint(70, 90) for _ in range(3)]}
# ]
#
# lst_employee = lambda students: [i['name'] for i in students if (sum(i['math']) / len(i['math'])) > 80 and (
#             sum(i['english']) / len(i['english'])) > 80]
# print(lst_employee(students))


# Задание 2
# products = [
#     {'name': 'Apple', 'price': 1.5, 'quantity': 10},
#     {'name': 'Banana', 'price': 0.75, 'quantity': 20},
#     {'name': 'Cherry', 'price': 2, 'quantity': 5}
# ]
#
# summ_price_products = (lambda products: sum([i['price'] * i['quantity'] for i in products]))(products)
# print(summ_price_products)


# Задание 3
# word_list = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# function_word = (lambda word_list: {i: word_list.count(i) for i in set(word_list)})(word_list)
# print(function_word)
