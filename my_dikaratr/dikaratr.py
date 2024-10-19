
# def my_decorator(func):
#     def wrapper():
#         print("Hllo")
#         resultat = func()
#         print("Bye")
#         return resultat
#     return wrapper
#
# @my_decorator
# def my_func():
#     print("My function")
#
# my_func()
# # n = my_decorator(my_func)
# # n()



# def chek(func):
#     def cat():
#         print(" start osnovnoi funkcii ")
#         resultat = func()
#         print(" konetc osnovnoi funkcii ")
#         return resultat
#     return cat
#
# @chek
# def my_func():
#     print(" менин атым Zamirbek")
#
#
# my_func()


# def decorator(func):
#     def wrapper():
#         print("register")
#         print("login")
#         resultat = func()
#         print("buttu")
#         return resultat
#     return wrapper()
#
#
# @decorator
# def chek():
#     print("afatar koi")
#
# chek()



# def main(func):
#     def wrapper():
#         beginning()
#         point()
#         result = func()
#         the_and()
#         return result
#     return wrapper
#
#
# @main
# def my_func():
#     print("level")
#
# def beginning():
#     print("igra bashtaldy")
#
# def point():
#     print("ochko aluu")
#
# def the_and():
#     print("buttu")
#
# my_func()



# def decorator(func):
#     def wrapper():
#         start()
#         func()
#         stop()
#     return wrapper
#
# def start():
#     print("start sessi")
#
# @decorator
# def order():
#     print("заказ жонотуу")
#
# @decorator
# def text():
#     print("Просмотр товара")
#
# @decorator
# def buy():
#     print("Товар тандоо")
#
# def stop():
#     print("stop sessi")
#
# order()
# text()
# buy()

# import time
#
# def measure(func):
#     def wrapper():
#         start_time = time_time()
#         resultat = func()
#         end_time = time_time()
#         execition_time = start_time - end_time
#         print(f"Время выполнение функции{example_function: } секунд")
#         return resultat
#     return wrapper
#
# @measure
# def example_function(seconds):
#     time.sleep(seconds)
#     return "Функция завершена"
#
# result = example_function(2)
# print(result)


# def calculator(func):
#     def wrapper(a, b):
#         print("start raboty calculatora")
#         result = func(a, b)
#         print(f" resultat operatcii: {result}")
#         print("zavershenie paboty calculatora")
#     return wrapper
#
# @calculator
# def add(a, b):
#     return a + b
#
# @calculator
# def pluse(a, b):
#     return a - b
#
# @calculator
# def minus(a, b):
#     return a * b
#
# @calculator
# def divide(a, b):
#     if b % 2 == 0:
#         return "oshibca delenie"
#     return a / b
#
# add(13, 54)
# pluse(54, 13)
# minus(24, 12)
# divide(34, 3)

# def repeat(times):
#     def decorator(func):
#         def wrapper(*args):
#             for i in range(times):
#                 print(f"Вызов {i+1}:")
#                 result = func(*args)
#
#                 print(result)
#         return wrapper
#     return decorator
#
#
# @repeat(3)
# def greet(name):
#     return f"Привет, {name}!"
#
# greet("Akdil")

# def order_notification(func):
#     def wrapper(name, item):
#         print(" nachinaem obrabotku zakaza.")
#         result = func(name, item)
#         print(" obrabotka zakaza zavershena.")
#         return result
#     return wrapper
#
# @order_notification
# def createa_order(name, item):
#     return f"Zakaz dla klienta {name} na tovar {item} uspeshno sozdan."
#
# order_message = createa_order("Zamir", "iphone")
# print(order_message)




def log_turn(func):
    def wrapper(character_name, enemy_name, damage):
        print(f" hod personaja: {character_name}")
        print(f"{character_name} atakuet {enemy_name} siloi {damage}.")
        func(character_name, enemy_name, damage)
        print(f"Hod {character_name} zavershen.")
    return wrapper

@log_turn
def attack(character_name, enemy_name, damage):
    print(f"{enemy_name} poluchil {damage} urona.")


attack("Zamir", "killer", 50)
attack("orus", "nemis", 30)



























