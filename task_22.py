# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
import random

number_n = int(input("Введите кол-во элементов первого множества: "))
number_m = int(input("Введите кол-во элементов второго множества: "))

some_list1 = [random.randint(50, 1000) for _ in range(number_n)]
some_list2 = [random.randint(50, 1000) for _ in range(number_m)]
some_set1 = set(some_list1)
some_set2 = set(some_list2)
set_intersection = some_set1.intersection(some_set2)
print(*sorted(set_intersection))

