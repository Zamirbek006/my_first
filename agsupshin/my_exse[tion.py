# try:
#     number1 = int(input("Введите первое число: "))
#     number2 = int(input("Введите второе число: "))
#     print("Результат деления:", number1/number2)
#     my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     print(my_list[10])
# except ValueError:
    #print("Преобразование прошло неудачно")
# except ZeroDivisionError:
#     print("Попытка деления числа на ноль")
# except BaseException:
#     print("Общее исключение")
# finally:
#     print("Блок try завершил выполнение")


# try:
#     num1 = int(input("Введите число:"))
#     num2 = int(input("Введите число:"))
#     print(num1 / num2)
# except ZeroDivisionError as e:
#     print("Преобразование прошло неудачно")
# except ValueError as e:
#     print("Преобразование прошло неудачно")
# finally:
#     print("Завершил работу")



# numbers = input("Введите список чисел, разделенных пробелами: ").split()
# num = 0
# for i in numbers:
#     try:
#         num += int(i)
#     except ValueError as e:
#         print(e)
#
# print(num)


# try:
#     num1 = int(input("Введите число:"))
#     num2 = int(input("Введите число:"))
#     try:
#         print(num1 / num2)
#     except ZeroDivisionError as e:
#         print("На ноль делить нелзя :", e)
# except ValueError as e:
#     print(e)

# def chek_password_strengh(password):
#     try:
#         password = input("Введите пароль:")
#     except len(password) < 8:
#         print("8 белгиден кем болбошу керек")
#     except not ValueError:
#         print("пароль тамга камтышы керек")
# password = input("Введите пароль:")
# print(chek_password_strengh(password))



# def check_password_strengh(password):
#     if len(password) < 8:
#         return "Пароль должен не короче 8 символов."
#     if not any(i.isdigit() for i in password):
#         return "Пароль должен содержать минимум одну цифру."
#     if not any(i.isupper() for i in password):
#         return "Пароль должен содердать минимум одну букву в верхнем регистре."
#     if not any(i.islower() for i in password):
#         return "Пароль должен содердать минимум одну букву в нижнем регистре."
#
#     return "Пароль надежный."
#
# password = input("Введите пароль.")
# print(check_password_strengh(password))



# users = {
# "admin": "admin123",
# "user1": "pass123",
# "guest": "guestpass",
# }
#
# def login(username, password):
#     if username in users and users[username] == password:
#         return True
#     else:
#         raise ValueError("Логин же пароль туура эмес.")
#
# while True:
#     try:
#         username = input("Логинди киргизиниз:")
#         password = input("Паролду киргизиниз:")
#
#         if login(username, password):
#             print(f"Кош келиниз, {username}")
#             break
#     except ValueError as e:
#         print(e)
#         print("Кайра аракет кылыныз.") 


# shop = {
#     "kylych": 100,
#     "kalkan": 150,
#     "ilgich": 50
# }
# balance = 300
#
# def buy_item(item, quantity, balance):
#     if item in shop:
#         total_price = shop[item] * quantity
#         if total_price <= balance:
#             balance -= total_price
#             print(f"siz {item} satyp aldynyz. Jany balans {balance} som.")
#         else:
#             print("sizde karajt jetishciz")
#     else:
#         print(f"{item} dukoyu jok")
#
#
# while True:
#     item = input("Товар жазыныз")
#     if item.lower() == "чыгыш":
#         break
#     try:
#         quantity = int(input("саны"))
#         buy_item(item, quantity,balance)
#     except ValueError:
#         print("Туура сан киргизиниз.")



# def get_student_data():
#     while True:
#         try:
#             name = input("Атынызды жазыныз:")
#             if not name.isalpha():
#                 raise ValueError("atynyzda tamgalar gana bolushu kerek.")
#             age = input("Jashynyzdy jazynyz:")
#             if not age.isdigit():
#                 raise ValueError("Jash butun san bolushu kerek.")
#             phone = input("Telephone nomerin kirgiziniz:")
#             if not phone.isdigit():
#                 raise ValueError("Telephone nomeri sandardy gana kamtyshy kerek")
#             print("Maallymat tuura!")
#             break
#         except ValueError as e:
#             print(e)
#             print("Kaira araket kylynyz.")
#
# get_student_data()









































