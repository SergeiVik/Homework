# dictionary = {}
#
#
# def add_word():
#     word = input("Enter a word: ")
#     translation = input("Enter a translation of the word: ")
#     translation1 = input("Enter a translation1 of the word: ")
#     translation2 = input("Enter a translation2 of the word: ")
#     translation3 = input("Enter a translation3 of the word: ")
#     book_dict = {
#         word: translation,
#         translation1: translation2,
#         translation2: translation3,
#         translation3: translation3
#     }
#     dictionary[f"{word} {translation}"] = book_dict
#     print(f"Word {word} was successfully added to the dictionary!")
#
#
# def delete_word():
#     word = input("Enter a word to delete: ")
#     del dictionary[word]
#     print(f"Word {word} was successfully deleted from the dictionary!")
#
#
# command = ''
# while command != 'Exit':
#     command = input("Enter a command: ")
#     if command == 'add':
#         add_word()
#     elif command == 'delete':
#         delete_word()

# Работа с файлами заключается в использовании правильного подхода к открытию и чтению файлов
# open().close()
# Режимы открытия файла по потоку данных: read - r, write - w, append - a
# Режимы открытия файла по типу данных: text - t, bytes - b
# file = open("new.txt", "r", encoding='utf-8')
# Опциональный параметр - кол-во символов для чтения
# print(file.read(2))
# print(file.read())
# Для чтения построчно:
# print(file.readline(2))
# print(file.readline())
# print(file.readline())
# Для чтения всего файла сразу:
# print(file.readlines(7))
# Если передать число, то чтение остановится по превышению кол-ва символов
# После чтения N-строки
# file = open("new.txt", "w", encoding='utf-8')
# file.write("Hello World\n")
# file.write("Bye World!\n")
# file.writelines(["Hello World\n", 'Bye World!'])
# file.close()

# file = open("new.txt", "r+", encoding='utf-8')
# print(file.readable())
# print(file.writable())
# print(file.read())
# file.write("Bye-bye!")

# Режимы открытия файла:
# r - доступно только чтение. Если файла нет, получим исключение
# w - доступна только запись. Если файла нет, он создастся, иначе файл стирается при открытии
# a - доступна только дозапись. Если файла нет, он создастся, иначе просто поставит курсор в конце файла
# + как расширение режима открытия делает возможными обе операции: и чтение, и запись.
# Все остальные свойства режимов останутся прежними

# 1.
# import re
# old_file = open("old.txt", 'r')
# new_file = open("new.txt", 'w')
# old_text = re.split('[\s,.!?;:"]+', old_file.read())
# new_file.writelines([word + '\n' for word in old_text if len(word) >= 7])

# 2.
# old_file = open("old.txt", 'r')
# new_file = open("new.txt", 'w')
# new_file.writelines([line + '\n' if i == 0 else line
#                      for i, line in enumerate(old_file.readlines()[::-1])])

# text = old_file.read().split('\n')[::-1]
# new_file.write('\n'.join(text))

# 3.
# old_file = open("old.txt", 'r')
# new_file = open("new.txt", 'w')
# text = old_file.readlines()
# lines_without_commas = [i for i, l in enumerate(text[::-1]) if ',' not in l]
# if lines_without_commas:
#     last_uncomma_index = len(text) - lines_without_commas[0]
#     text.insert(last_uncomma_index, '*' * 12 + '\n')
# else:
#     text.append('\n' + '*'*12)
# new_file.writelines(text)

# 4.
# old_file = open("old.txt", 'r')
# print(len(old_file.read().replace('\n', '')))

# 5.
# old_file = open("old.txt", 'r')
# print(old_file.read().count('\n') + 1)

# Контекстный менеджер
# with open("old.txt", 'r') as f:
#     # print(f.read())
#     ...
#
# print(f.read())

# 6.
# banned_words = ['Lorem', 'lorem', 'ipsum']
# with open("old.txt", 'r') as old_file:
#     old_text = old_file.read()
# with open("new.txt", 'w') as new_file:
#     new_text = old_text
#     for word in banned_words:
#         new_text = new_text.replace(word, '')
#     new_file.write(new_text)

