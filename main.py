import random




# num = int(input(" 1-сан "))
# num2 = int(input(" 2-сан "))
# num3 = int(input(" 3-сан жаз "))
#
# print(num + num2 <= num3)

      # 03.09.2024
#
# number = 11
#
# if number == 10:
#     print(f"njmberdin ichi {number}")
# elif number == 11:
#       print(f"njmberdin 11 {number}")
# elif number == 12:
#       print(f"njmberdin 12 {number}")
# else:
#     print(f"njmberdin 13 {number}")



# language = "hghghg"
# if language == "english":
#     print("Hello")
# elif language == "french":
#     print("Bonjour")
# elif language == "german":
#     print("Guten Tag")
# elif language == "spanish":
#     print("Hola")
# elif language == "Kyrgystan":
#     print("Кандай")
# else:
#     print("Привет")


# number = int(input("Саны жазыңыз: "))
#
# if number % 2 == 0:
#     print("Сан так болунот")
# else:
#     print("Сан так болунбойт")


#language = "russian"
#
# daytime = "morning"
#
# if language == "english":
#     if daytime == "morning":
#         print("Good morning")
#     else:
#         print("Good evening")
# else:
#     if daytime == "morning":
#         print("Доброе утро")
#     else:
#         print("Добрый вечер")


# num =int(input( " san jaz "))
#
# if num * num <= 100:
#     print(" tuura ")
# else:
#     print(" andai emes ")




# number = int(input())
#
# if number == 1:
#     print(" pn ")
# elif number == 2:
#     print(" ft ")
# elif number == 3:
#     print(' sd ')
# elif number == 4:
#     print(" chet ")
# elif number == 5:
#     print(" pt ")
# elif number == 6:
#     print(" sb ")
# else:
#     print( " andai kun jok " )


# name = input()
#
# if len(name) < 10:
#     print(" kichine ")
# elif len(name) == 10:
#     print(" barabar ")
# elif len(name) > 10:
#     print(" chon ")
# else:
#     print(" takyr jok ")

#b = " zamir"

# if len(b) < 10:
#     print("q")
# elif len(b) == 10:
#     print()

# z = " zamir "
# if z.isupper():
#     print(z.upper())
# else:
#     print(z.lower())


# name = input()
# if len(name) < 3:
#     if len(name) < 7:
#          print(" jakshy ")
#     else:
#         print(" tuura emes ")
#
# print(" end ")


# number = int(input())
# if number < 100:
#     print( number )
# else:
#     number *= 3
#     print( number )


# name = input()
# probel = input()
# if probel in name :
#     print(" da ")
# else:
#     print(" net ")


# text = input()
# probel = text.replace(" ", "+" )
# print( probel)


# probel = " zamir "
# if probel.islower:
#       print(" chyn ")
# else:
#     print(" kalp ")


# is_true = True
# if is_true:
#     print(" true ")
# else:
#     print(" false ")


# name = input()
# age = int(input())
#
# if age > 18 and 25 > age:
#     print(" student ")
# elif age > 0 and age < 6:
#     print(" malysh ")
# elif age > 6 and age < 18:
#     print(" okuuchu ")
# elif age < 100 and age > 25:
#     print(" kishi ")
# else:
#     print("jok")


# hour = int(input())
# if hour > 5 and hour < 12:
#     print(" utro")
# elif hour > 12 and 16 > hour:
#     print(" den ")
# elif hour > 16 and 22 > hour:
#     print(" fecher ")
# elif hour > 22 and 5 > hour:
#     print(" noch ")
# else:
#     print()
#




# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
#
#
# if num1 > num2:
#     print(f"Большее число: {num1}")
# elif num2 > num1:
#     print(f"Большее число: {num2}")
# else:
#     print("Числа равны.")




# a = float(input("Введите длину первой стороны: "))
# b = float(input("Введите длину второй стороны: "))
# c = float(input("Введите длину третьей стороны: "))
#
#
# if a == b == c:
#     print("Треугольник является равносторонним.")
# elif a == b or b == c or a == c:
#     print("Треугольник является равнобедренным.")
# else:
#     print("Треугольник является разносторонним.")


# num1 = float(input("Введите первое число: "))
# num2 = float(input("Введите второе число: "))
# num3 = float(input("Введите третье число: "))
#
#
# min_num = min(num1, num2, num3)
#
#
# print("{min_num}")


             # ТАПШЫРМА

# num1 = int(input())
# num2 = int(input())
#
# operator = input(" (+, -, *, /): ")
#
# if operator == '+':
#     result = num1 + num2
#     print(f" {result}")
# elif operator == '-':
#     result = num1 - num2
#     print(" {result}")
# elif operator == '*':
#     result = num1 * num2
#     print(" {result}")
# elif operator == '/':
#     if num2 != 0:
#         result = num1 / num2
#         print("{result}")
#     else:
#         print("На ноль делится")
# else:
#     print("Неверный оператор")





# word = input().lower()
#
#
# if word == word[::-1]:
#     print("Палиндром")
# else:
#     print("Не палиндром")




# def is_leap_year(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
#
# month = int(input( " Введите номер месяца "))

# if month in [1, 3, 5, 7, 8, 10, 12]:
#     print("31 день")
# elif month in [4, 6, 9, 11]:
#     print("30 дней")
# elif month == 2:
#     year = int(input("Введите год "))
#     if is_leap_year(year):
#         print("29 дней (високосный год)")
#     else:
#         print("28 кун")
# else:
#     print("Некорректный номер месяца")


                  #TAPSHYRMA

# for i in range(1, 11):
#     print(f"{i}*2 = {i**2}")


# num = int(input("Санды киргизиңиз: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")


# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
# num = int(input("Факториалын таба турган санды киргизиңиз: "))
# print(f"{num}! = {factorial(num)}")


# for i in range(1, 11):
#     print(f"5 x {i} = {5 * i}")


# word = "Python"
# print(word [1 : : 2])

            #TАPSHYRMA

# def two_number(a, b):
#     print(a + b)
#
# two_number(134, 243)


# def min_two(num, num2, num3):
#     print(min(num, num, num3))
#
# min_two(26, 63,17)


# def country(s):
#     print(len(s))
#
# country("kyrgyzstan")


# def multiple(a, b, c):
#     print(a + b + c)
#
# multiple(20, 30, 40)


# def square(x):
#     print(f"{x} ** 2 = {x ** 2}")
#
# square(127)


# def sum_up(n):
#     total = 1
#     for i in range(1, n + 1):
#         total = i
#     print(total)
#
# sum_up(24)


# def factorial(n):
#     result = 1
#     while n > 1:
#         result *= n
#         n -= 1
#     print(result)
#
# factorial(9)


# def word_and_symbol(word, symbol):
#     for char in word:
#         print(char * symbol)
#
# word_and_symbol("python", 5)


# def word_and_symbol2(word, symbol):
#     return symbol in word
# print(word_and_symbol2(" python", "M"))


# def count_symbol(word, symbol):
#     return word.count(symbol)
# print(count_symbol("kakaach", "a"))

       #Tapshyrma

# def table_of_three(n):
#     i = 1
#     result = ""
#     while i <= 10:
#         result += f"{n} * {i} = {n * i}\n"
#         i += 1
#     return result


# def sum_to_n(n):
#     total = 0
#     i = 1
#     while i <= n:
#         total += i
#         i += 1
#     return total


# def find_max(a, b, c):
#     max_num = a
#     if b > max_num:
#         max_num = b
#     if c > max_num:
#         max_num = c
#     return max_num

#find_max(4, 5, 2)

# def multiply_all(*args):
#     product = 1
#     for num in args:
#         product *= num
#     return product
#
# multiply_all(2, 3, 4,)


# def max_of_all(*args):
#     if len(args) == 0:
#         return None
#     max_num = args[0]
#     for num in args[1:]:
#         if num > max_num:
#             max_num = num
#     return max_num



# def list_operations(lst):
#
#     def find_max_in_list(lst):
#         return max(lst)
#
#
#     def remove_duplicates(lst):
#         return list(set(lst))
#
#
#     def reverse_list(lst):
#         return lst[::-1]
#
#
#     def sum_of_list(lst):
#         return sum(lst)
#
#
#     def is_palindrome(lst):
#         return lst == lst[::-1]
#
#
#
#
#     print("Максимум в списке:", find_max_in_list(lst ))
#     print("Список без дубликатов:", remove_duplicates(lst))
#     print("Перевернутый список:", reverse_list(lst))
#     print("Сумма списка:", sum_of_list(lst))
#     print("Является ли палиндромом:", is_palindrome(lst))
#
#
# lst = [1, 2, 3, 4, 3, 2, 1]
# list_operations(lst)

# def find_odd_numbers():
#     num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#     num2 = list(num)
#     print(f"все числы: {num2}")
#     for d in num2:
#         if d % 2 != 0:
#             print(f"четные числы: {d} ")

#
# find_odd_numbers()

#
#
# def random_asia():
#     return random.choice(asia)
#
#
# def find_count_asia():
#     while True:
#         target_asia =random_asia()
#
#         name = input(" Введите имя страна ")
#
#         if name == target_asia:
#             print(f"{name}- это правильный ответ!")
#             break
#         else:
#             print(f"Вы не угадали. Попробуйте еше раз!")
#
#
# find_count_asia()
#


# def filter_by_length(strings, min_length):
#     return [string for string in strings if len(string) >= min_length]
#
# strings = ["apple", "banana", "pear", "kiwi"]
# min_length = 5
# print(filter_by_length(strings, min_length))
#
#
# def contains_substring(strings, substring):
#     return [string for string in strings if substring in string]
#
#
# strings = ["apple", "banana", "grape", "kiwi"]
# substring = "ap"
# print(contains_substring(strings, substring))
#
#
# def capitalize_if_starts_with(strings, letter):
#     return [string.capitalize() if string.startswith(letter) else string for string in strings]
#
# strings = ["apple", "banana", "apricot", "kiwi"]
# letter = "a"
# print(capitalize_if_starts_with(strings, letter))


asia = ["Kyrgystan", "Kazakstan", "Ozbekstan", "Talikstan"]
evropa = ["Fransia", "italia", "ukraina", "rassia"]
america = ["argentina", "columbia", "mecxika", "chili"]
afrika = ["negeria", "kenia", "aljir", "sudan"]

def find_countre():
    print("ugadaite ctrany ")
    print("1: asia")
    print("2: evropa")
    print("3: america")
    print("4: africa")

    while True:
        a = int(input("выберите материк: "))
        if a == 1:
            random_count = random.choice(asia)
            print("Была выбрана Азия")
        elif a == 2:
            random_count = random.choice(evropa)
            print("Была выбрана Европа")
        elif a == 3:
            random_count = random.choice(america)
            print("Была выбрана Америка")
        elif a == 4:
            random_count = random.choice(afrika)
            print("Была выбрана Африка")
        else:
            print("Некорректный число")
            continue
        print(random_count)

        d = input("выберите страну: ")
        if d == random_count:
            print(f"вы угадали {random_count}")
            break
        else:
            print("вы не угадали")

        povtor = input("Желаете попробовать еще раз? yes или no: ")
        if povtor == "no":
            print(f"спасибо за игру!!! загаданная страна было: {random_count}")
            break
        elif a == "yes":
            continue


find_countre()



























