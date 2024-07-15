# Чтобы вызвать функцию нужно написать def function_name():

# def function_name():
    # Дальше идет тело функции.
    # print("Hello World")

# Есть возвратные и не возвратные функции.

# function_name()

# function_name это не возвратная функция, а точнее функция-процедура.

# Процедура - вызивается ради побочного эффекта.
# Побочный эффект - у function_name() побочный эффект это вывод текста.

# Для того чтобы передать какую нибуть инфу в функцию используют - Параметр функции.
# P.S. Она в скобках.

# name = input("Как твоё имя? ")
# def function_name_2(name):
#     print(f"Привет {name}")
#
# function_name_2(name)

# ada = int(input())
# def num(num):
#     print(num * 1.8 + 32)
# num(ada)

# import random
#
# simbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#
# def generate_password(n=6): # Продолжи решение тут
#     password = ''
#     for i in range(n):
#         sim = random.choice(simbols)
#         password += sim
#     return password
#
# generate_password()

# new_data = map(int, ['14', '51', '23', '43', '87'])   # передаем функцию int аргументом
# print(new_data)
# new_data = list(new_data)   # map не знает, в какую структуру данных нам нужно поместить полученные данные, поэтому превращаем map-объект в список
# print(new_data)   # [14, 51, 23, 43, 87]

data = map(float, ['55.435656', '23.678546', '76.542465', '10.43433345', '84.323454524', '43.546784132'])
print(data)
data = list(data)
print(data)