# 1.	Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.

# n = input("Введите число: ")
# sum = 0
# for i in range(len(n)):
#     if (n[i].isdigit):
#         sum = sum + int(n[i])
#     else:
#         i += 1
# print(sum)


# 2.	Напишите программу, которая принимает на вход число N и выдает набор
# произведений чисел от 1 до N.

# n = int(input("Введите число: "))
# prod = 1
# for i in range (1, n + 1):
#     prod = prod * i
#     print(prod)


# 3. Задайте список из n чисел последовательности(1 + 1 / n) ^ n
# выведите на экран их сумму.

# n = int(input("Введите число: "))
# sum = 0
# for i in range(1, n):
#     sum += (1 + 1 / i) ** i
#     print(sum, end=", ")

# 4.	Задайте числами список из N элементов, заполненных из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

sp = [-4, -2, 0, 2, 4]
pos1 = 1
pos2 = 4
prod = sp[pos1] * sp[pos2]
print("Список: ")
print(sp)
print("Произведение заданных элементов: ")
print(prod)


# 5.	Реализуйте алгоритм перемешивания списка
# (shuffle использовать нельзя, другие методы из библиотеки random - можно).

# import random
# def shuf_sp(sp_start):
#     sp_final = sp_start[:]
#     last_index = len(sp_final) - 1
#     for i in range(last_index):
#         new_index = random.randint(0, last_index)
#         temp = sp_final[i]
#         sp_final[i] = sp_final[new_index]
#         sp_final[new_index] = temp
#     return sp_final
#
# sp = [1, 2, 3, 4, 5]
# mixed_sp = shuf_sp(sp)
# print("Исходный список: ")
# print(sp)
# print("Перемешанный список: ")
# print(mixed_sp)