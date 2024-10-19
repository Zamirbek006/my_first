# users = {"Tom", "Bob", "Alice", "Tom"}
# print(users)
#
# people = ["Mike", "Bill", "Ted", "Bill"]
# print(people)
#
# users = set(people)
# print(users)
#
# users = set()
# print(users)
#
# users = {"Tom", "Bob", "Alice"}
#
# print(len(users))
#
# users = set()
# users.add("Sam")
# print(users)
#
# users = {"Tom", "Bob", "Alice"}
# print(users)
#
# user = "Tom"
#
# if user in users:
#     users.remove(user)
# print(users)
#
# users = {"Tom", "Bob", "Alice"}
#
# users.discard("Tim")
# print(users)
#
# users.discard("Tom")  # элемент "Tom" есть, и метод удаляет элемент
# print(users)  # {"Bob", "Alice"}
#
# users.clear()
# print(users)
#
# users = {"Tom", "Bob", "Alice"}
#
# for user in users:
#     print(user)
#
# users = {"Tom", "Bob", "Alice"}
#
# students = users.copy()
# print(students)
#
# users = {"Tom", "Bob", "Alice"}
#
# users2 = {"Sam", "Kate", "Bob"}
#
# users3 = users.union(users2)
# print(users3)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# print(users | users2)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# users3 = users.intersection(users2)
# print(users3)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# print(users & users2)
#
# users = {"Tom", "Bob", "Alice", "Sam"}
# users2 = {"Sam", "Kate", "Bob"}
#
# users2.intersection_update(users)
# print(users2)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# users3 = users.difference(users2)
# print(users3)
# print(users - users2)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# users3 = users.symmetric_difference(users2)
# print(users3)
#
# users4 = users ^ users2
# print(users4)
#
# users = {"Tom", "Bob", "Alice"}
# superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
#
# print(users.issubset(superusers)) # True
#
# print(superusers.issubset(users)) # False
#
# users = {"Tom", "Bob", "Alice"}
# superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
#
# print(users.issuperset(superusers)) # False
# print(superusers.issuperset(users)) # True
#
# #-----------------frozen set---------------
# users = {"Tom", "Bob", "Alice"}
#
# users = frozenset({"Tom", "Bob", "Alice"})



# python_users = {"Akdil", "Meder", "Zamir", "Mirbek"}
# java_users = {"Tom", "Sam", "Akdil", "Bob"}
#
# def my_set(python_users, java_users):
#     print(python_users.difference(java_users))
#     print(python_users.intersection(java_users))
#
# my_set(python_users, java_users)


# students_python = {"Аяна", "Акдил", "Мирбек", "Талгарбек", "Бибигуль", "Замирбек"}
# students_java = {"Акдил", "Замирбек", "Кудайберди", "Медербек", "Айназик"}
#
# def user(a, b):
#
#     print(students_python.intersection(students_java))
#
#
# user(students_python, students_java)



# sentece = "apple banana orange apple lemon banana"
# words = sentece.split()
# unique_words = set(words)
# print(unique_words)


# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# users = set(list1)
# users2 = set(list2)
# users3 = users.intersection(users2)
# print(users3)


# numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6]
# users = set(numbers)
# print(users)


# text = "hello world"
# unique_chars = set(text)
# print(unique_chars)


# users = frozenset({1, 2, 3, 4, 5})
# users.add(6)
# print(users)


# set1 = frozenset({1, 2, 3, 4, 5})
# set2 = frozenset({4, 5, 6, 7})
# intersection = set1.intersection(set2)
# print(intersection)


# immutable_set = frozenset({1, 2, 3, 4, 5})
# print(immutable_set)
# immutable_set.remove(3)



numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print(frozenset(numbers))




































