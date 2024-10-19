# numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_numbers = [n for n in numbers if n % 2 == 0]
# print(new_numbers)
#
#
# number = [str(i)for i in numbers]
# print(number)
#
# from tkinter.tix import Select

# text = [ " banan, ananas, kiwi"]
# new_text = [ i.upper() for i in text]
# print(new_text)


# text = [ "banana", "ananas", "kiwi", "apple"]
# # new_text = [ len(i) for i in text]
# # print(new_text)
#
# new_text = [ i.upper() if len(i) > 5 else i for i in text]
# print(new_text)




# elements = []
# for i in range(5):
#     element = input(f"Введите элемент {i+1}: ")
#     elements.append(element)
#
# print("Список элементов:", elements)



import time


def sabak():

    hours = int(input("Сабак канча саат болот? "))
    minutes = hours * 60

    print(f"Сабак {minutes} минатадан кийин бутот.")
    # time.sleep(minutes * 60)
    time.sleep(5)

    print(f"\nСабак бутту!")


sabak()
