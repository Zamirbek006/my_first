# tom = ("Tom", 22, "Google")
#
# i = 0
# while i < len(tom):
#     print(tom[i])
#     i += 1


# number = (23, 43, 9, 83, 45, 45)
# num = max(number)
# num2 =min(number)
# print(num)
# print(num2)
#
# max_1 = number[0]
# min_1 = number[0]
#
# for i in number:
#     if i > max_1:
#         max_1 = i
#     if i < min_1:
#         min_1 = i
#
# print(max_1)
# print(min_1)



# names = ("Tom", "Sten", "Bob", "Zamir", "Mirbek", "Ayana", "Ainazik")
# name = tuple(names)
# person = tuple(i for i in names if len(i) >= 5)
# print(person)
#
# name2 = [i for i in names if i.startswith("A")]
# print(name2)
#



# my_tuple = (4, 7, 8, 2, 5, 8, 9)
#
# index_of_2 = my_tuple.index(8)
# print(f"Первое вхождение числа 8 находится по индексу {index_of_2}.")


# letters = ('a', 'b', 'c', 'a', 'c', 'a', 'e')
# count_a = letters.count('a')
# print(count_a)


# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# tuple3 = tuple1 + tuple2
# print(tuple3)


# tuple1 = (1, 2, 3)
# tuple2 = (1, 2, 3)
#
# if tuple1 == tuple2:
#     print("Барабар")
# else:
#     print("Барабар эемес")


# string = "Hello"
# tuple_string = tuple(string)
# print(tuple_string)


# tuple1 = (1, 3, 5)
# tuple2 = (2, 4, 6)
# result = tuple(i for i in zip(tuple1, tuple2) for i in i)
# print(result)



tuple1 = (1, 3, 5)
tuple2 = (6, 7, 4)

def sum_tuple(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        print("barabar emes")

    result = []
    for i in range(len(tuple1)):
        result.append(tuple1[i] + tuple2[i])
    return tuple(result)

tuple1 = (1, 3, 5)
tuple2 = (6, 7, 4)
result = sum_tuple(tuple1, tuple2)
print(result)


































