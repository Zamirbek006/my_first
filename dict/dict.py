# users = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }

# user1 = users.get("+55555555")
# print(user1)  # Alice
# user2 = users.get("+33333333", "Unknown user")
# print(user2)  # Bob
# user3 = users.get("+44444444", "Unknown user")
# print(user3)  # Unknown user



# users = {"+1111111": "Tom", "+3333333": "Bob"}
#
# users2 = {"+2222222": "Sam", "+6666666": "Kate"}
# users.update(users2)
#
# print(users)
# print(users2)


# users = {
#     "R ": "Ayana",
#     "M": "Mirbek",
#     "K": "Zamirbek",
#     "A": "Ainazik"
# }
#
# for i in users.values():
#     print(i)
# for i in users.keys():
#     print(i)
# for i in users.items():
#     print(i)


# users_tuple = (
#     ("+111123455", "Tom"),
#     ("+384767557", "Bob"),
#     ("+958758767", "Alice")
# )
# users_dict = dict(users_tuple)
# print(users_dict)

#############################

# my_dict = {}
# my_dict["name"] = "John"
#
# print(my_dict)


# fruits = {'banana': 7, 'apple': 5, 'orage': 10 }
# user = fruits.get('apple')
# print(user)


# person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# user = person.get('age')
# print(user)


# fruits = {'banana': 7, 'apple': 5, 'orage': 10 }
# fruits['banana'] += 2
# print(fruits)

# fruits = {'banana': 7, 'apple': 5, 'orage': 10}
# user = 'apple'in fruits
# print(user)
#
# for i in fruits.keys():
#     print(i)
#
# for i, n in fruits.items():
#     print(i)


# person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# for i in person.keys():
#     print(i)
#
# for i, n in person.items():
#     print(i,n)


# fruits = {'banana': 7, 'apple': 5, 'orage': 10 }
# del fruits['orage']
# print(fruits)
#


# users = {
#     "R ": "Ayana",
#     "M": "Mirbek",
#     "K": "Zamirbek",
#     "A": "Ainazik"
# }
# user = users.clear()
# print(user)



# def invert_dict(d):
#     return {v: k for k ,v in d.items()}
#
# original_dict = {'apple': 5, 'banana': 7, 'orage': 3}
# invert_dict = invert_dict(original_dict)
# print(invert_dict)



# def dist_to_tuple_list(d):
#     return list(d.items())
#
# ages = {'Akdil': 25, 'Fatima': 30, 'Mirbek': 35}
# tuple_list = dist_to_tuple_list(ages)
#
# print(tuple_list)



# def split_drages(grades):
#     passed = {name: grade for name, grade in grades.items() if grade >= 80}
#
#     failed = {name: grade for name, grade in grades.items() if grade < 80}
#     return passed, failed
#
#
# grades = {
#     'Аяна': 96, 'Акдил': 89, 'Талгарбек': 75, 'Бибигул': 69,
#     'Мирбек': 89, 'Айназик': 81, 'Медербек': 80, 'Кудайберди': 86,
#     'Фатима': 84, 'Замирбек': 91, 'Азамат': 13
# }
#
# passed, failed = split_drages(grades)
# print("Прошли" ,passed)
# print("Не прошли", failed)


# def dictionary(grades):
#     passed_items = {}
#     passed_dict = {}
#     for keys, values in grades.items():
#         if values >= 80:
#   split



# text = "Менин менин атым Замирбек жана Замирбек"
#
# def dictionary(text):
#     w = text.lower().split()
#     name = {}
#     for i in w:
#         if i in name:
#             name[i] += 1
#         else:
#             name[i] = 1
#     return name
#
# res = dictionary(text)
# print(res)


# numbers = (2, 3, 4, 5, 6)
#
# def num(numbers):
#     dict ={}
#     for i in numbers:
#         dict[i] = i ** 2
#     return dict
#
# res = num(numbers)
# print(res)
#
#
# n = {i: i ** 2 for i in numbers}
# print(n)


# import random
#
# animals = {
#     'слон': 'Это самое большое наземное животное.',
#     'тигр': 'Это полосатый хищник.',
#     'панда': 'Это черно-белое животное, которое ест бамбук.',
#     'крокодил': 'Это рептилия, которая живет в воде.',
#     'коала': 'Это сумчатое животное, которое обитает в Австралии.',
# }
#
# def guess_animal_game():
#     print("Угадайте животное!")
#     keys, value = random.choice(list(animals.items()))
#     print(f"Подсказка: {value}")
#     guess = input("Введите ваше предположение: ").strip().lower()
#
#     if guess == keys:
#         print("Поздравляем! Вы угадали!")
#     else:
#         print(f"Непровильно. Правилный ответ: {keys}")
#
# guess_animal_game()














