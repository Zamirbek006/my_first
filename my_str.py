# import random
#
#
#
#
# # name = " zamir "
# # name2 = ' zamir '
# #
# # print(type( name ))
# # print(type( name2 ))
# #
# # capit = name.capitalize()
# # print(capit)
# #
# # upper = name.upper()
# #
# # lower =  name.lower()
# # print()
# # from tren import number
#
# # name = " менин атым замир "
# # edited_name = name.replace(" ", "*")
# #
# # print(edited_name)
#
# # name = "менин атым замир. мен он сегиз жаштамын"
# # name = name.startswith(" атым ")
# # print(name)
# #
# #
# #
# # name =str.title()
# # print(name)
#
# # probel = "     men atym zam    "
# # probel =str.strip(probel)
# # print(probel)
#
#
# #language = "russian"
# #
# # daytime = "morning"
# #
# # if language == "english":
# #     if daytime == "morning":
# #         print("Good morning")
# #     else:
# #         print("Good evening")
# # else:
# #     if daytime == "morning":
# #         print("Доброе утро")
# #     else:
# #         print("Добрый вечер")
#
#
# # num =int(input( " san jaz "))
# #
# # if num * num <= 100:
# #     print(" tuura ")
# # else:
# #     print(" andai emes ")
#
#
# ###############################################################################################
#
# # for i in range(11):
# #     print(i)
#
#
# # name = "python"
# #
# # for i in range(1, len(name), 2):
# #     print(i)
#
#
#
#
# # for i in range(0,10,2):
# #     if i % 2 == 0:
# #          print(i**2)
#
#
# # num = 1
# # while num < 6:
# #     print(num)
# #     num = num + 1
#
#
# # fife = 5
# # i = 1
# # while i <= fife:
# #     print(i)
# #     i += 1
#
#
# # three = 3
# # i = 1
# # while i <= three:
# #     print(f"{three} * {i} = {three * i}")
# #     i += 1
#
#
#
# # num = int(input())
# # i = 1
# # while  i <= num:
# #     print(f"{i} ** 3 = {i ** 3}")
# #     i += 1
#
# # num = int(input())
# # i = 1
# # while i <= num:
# #     if num % i == 0:
# #         print(f" tak bolunboit {i ** 2}")
# #     else:
# #         print(f" tak bolunot {i ** 3}")
# #     i +=1
#
#
#        ######  Функция
#
# # def add():
# #     print(2 + 2)
# #
# # add()  # функция без пораметром
#
#
# # def add():
# #     print(" startb func  ")
# #     print(2 + 2)
# #     print(" finish func ")
# #
# # add() # вызов каша менен болот
#
#
# # def multiple(number):
# #     print(number * number )
# #
# # multiple(100)
#
#
# # def upper_word(word):
# #     print(word.upper())
# #
# # upper_word("zamir")
#
#
# # def multiple(number, number2):
# #     print(number * number2 )
# #     print(number + number2)
# #     print(number - number2)
# #     print(number / number2)
# #
# # multiple(100, 50)
#
# # def multiple(number, number2):
# #     print(number * number2 )
# #     print(number + number2)
# #     print(number - number2)
# #     if number2 == 0:
# #         print(" 0 go bolunbjit")
# #     print(number / number2)
# #
# # multiple(100, 50)
#
#
# # def phone_number(number):
# #     if number % 2 ==0:
# #         print(number ** 2 )
# #     else:
# #         print(" bolunboit ")
# #
# # phone_number(6)
#
#
#
#
#
#
# # def factorial(n):
# #     for i in range(1, n):
# #         n *= i
# #     return n
# #
# # print(factorial(5))
# #
# # def factorial_while(n):
# #     factorial = 1
# #     i = 1
# #     while i <= n:
# #         factorial *= 1
# #     i += 1
# #     return factorial
# #
# # print(factorial_while(5))
# #
# # def word_and_symbol(word, symbol):
# #     i = 0
# #     while i < len(word):
# #         print(word[i] * symbol)
# #         i += 1
# #
# # word_and_symbol("python", 10)
# #
# # def word_and_symbol2(word, symbol):
# #     for i in range(len(word)):
# #         print(word[i] * symbol)
# #
# # word_and_symbol2("python", 5)
# #
# # def word_and_symbol(word, symbol):
# #     i = 0
# #     is_in_symbol = False
# #     while i < len(word):
# #         if symbol in word:
# #             is_in_symbol = True
# #         i += 1
# #     print(is_in_symbol)
# #
# #     word_and_symbol("python", "M")
# #
# # def count_symbol(word, symbol):
# #         return word.count(symbol)
# #
# # print(count_symbol("ppythoon", "p"))
#
#
# # def main():
# #         say_hello()
# #         say_goodbye()
# # def say_hello():
# #     print("Hello")
# # def say_goodbye():
# #     print("Good Bye")
# #
# #  main()
#
#
# # def say_hello(name="Ainazik", age=18):
# #     print(f"Hello, {name}")
# #     print(f"You are {age} years old")
# #
# # say_hello("Nursultan", 21)
# # say_hello("Sara", 30)
#
#
# # def print_person(name, /, age=18, *, company):
# #     print(f"Name: {name}  Age: {age}  Company: {company}")
# #
# # print_person("Sam", company="Google")  # Name: Sam  Age: 18  company: Google
# # print_person("Tom", 37, company="JetBrains")  # Name: Tom  Age: 37  company: JetBrains
# # print_person("Bob", company="Microsoft", age=42)
#
#
# # def print_person(*, name, surname, age, company):
# #     print(f"Name: {name}  Age: {age}  Company: {company}")
# #     print(surname)
# #
# #
# # print_person(name="Bob", surname="Smith", age=41, company="Microsoft")
#
#
# # def print_person(name, age):
# #     print(f"Name: {name}  Age: {age}")
# #
# #
# # print_person(age=25, name="John")
#
#
# # def numbers(*studens):
# #     print(studens)
# #
# # numbers("zamir", "takgar")
#
#
# # def number(*numbers):
# #     count = 0
# #     for i in numbers:
# #         count += i
# #     print(count)
# #
# # number( 2, 2, 2, 100, 4500)
#
#
# # def numbers(number):
# #     return 2 * number
# #
# # res  = numbers(5)
# # print(res)
#
#
# # def double(number, number2):
# #     return number % number2 == 0
# #
# # print(double(10, 5))
#
#
# # def number(*numbers):
# #     for i in numbers:
# #         if i < 50:
# #             print(i)
# #
# # number(1, 2, 3, 4, 5, 6, 7, 8, 9, 50, 78, 56, 43, 10)
#
#
# # students = ["Ainazik", "Ayana"]
# # print(students)
# # students.append("Azamat")
# # print(students)
# #
# # students.insert(9, "Nursultan")
# # print(students)
# # print(students[3])
#
#
# # def find_max_in_list(zamirbek):
# #     maximum = zamirbek[0] # 99
# #     for i in zamirbek:
# #         if i > maximum:
# #             maximum = i
# #     return maximum
# #
# #
# # lst = [10, 20, 400, 45, 99]
# # print(find_max_in_list(lst))
# #
# #
# # def remove_duplicates(my_list):
# #     new_list = [] # 10, 20, 30, 50, 60, 40, 80
# #     for i in my_list:
# #         if i not in new_list:
# #             new_list.append(i)
# #     return new_list
# #
# #
# # mirbek = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
# # print(remove_duplicates(mirbek))
# #
# #
# # def reverse_list(lst):
# #     return lst[::-1]
# #     new_list = []
# #     for i in lst:
# #         new_list.insert(0, i)
# #     return new_list
# #
# #
# # lst = [10, 20, 30, 40, 50]
# # print(reverse_list(lst))
# #
# #
# # def sum_of_list(lst):
# #     sum = 0
# #     for i in lst:
# #         sum += i
# #     return sum
# #
# #
# # lst = [10, 20, 30, 40, 50]
# # print(sum_of_list(lst))
# #
# #
# # def is_palindrome(lst):
# #     if lst == lst[::-1]:
# #         return True
# #     else:
# #         return False
# #
# #
# # lst = [10, 20, 10]
# # print(is_palindrome(lst))
# #
#
# # def multiple_list(lst):
# #     result = 1
# #     for i in lst:
# #         result *= i
# #     return result
# #
# #
# # lst = [2, 2, 4, 3, 2]
# # print(multiple_list(lst))
# #
# #
# def odd(lst):
#     new_list = [] # 21, 45, 93
#     new_list2 = []
#     for i in lst:
#         if i % 2 != 0:
#             new_list.append(i)
#     return new_list
#
#
# lst = [10, 21, 4, 45, 66, 93]
# print(odd(lst))

#
#
# # def odd(lst):
# #
# #     new_list = []
# #     number = 1
# #     for i in range(0, lst,1):
# #         number *= 2
# #     return number
# #
# # lst = [2, 3, 4, 5, 6, ]
# # print(odd(lst))
#
#
#
#
# def name_words():
#     words = [" akcha", "unaa", "suu", "kitep"]
#     popitka = 5
#
#     while popitka > 0:
#             name = input("Введите слово ")
#
#             if name == words:
#                 print(f"{name} - это правильный ответ!")
#                 break
#             else:
#                 popitka -= 1
#                 print(f"Вы не угадали. Попробуйте еще раз. У вас осталось {popitka} попыток.")
#                 if popitka < 3:
#                     first_letter = words[0]
#                     print(f"Подсказка: первая буква: {first_letter}")
#
#
#
#     if popitka == 0:
#         print(f"Попытки закончились. Загаданное имя было: {words}")
#
#     answer = input("Желаете попробовать еще раз? (yes/no)\n")
#
#     while answer != "yes" and answer != "no":
#         answer = input("Некорректный ввод. Введите 'yes' или 'no':\n")
#
#     if answer == "no":
#         print(f"Спасибо за игру! Загаданное имя было: {words}")
#         break
#
# name_words()

