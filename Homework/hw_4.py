'''1. Напишите программу, которая принимает два числа в кач-ве аргументов и считает наименьшее общее кратное для этих чисел. '''

# from math import gcd
#
#
# a = int(input('First int: '))
# b = int(input('Second int: '))
# result = a*b//gcd(a, b)
# print(result)


# a = int(input('First int: '))
# b = int(input('Second int: '))
# list1 = [2, 3, 4, 5, 6, 7, 8, 9]
# list_a = [i*a for i in list1]
# list_b = [g*b for g in list1]
# for i in list_a:
#     for g in list_b:
#         if i == g:
#             print(i)
#             break


'''2. Напишите программу, которая суммирует все целые числа от значения «start» до величины «end» включительно (start, end - вводятся с клавиатуры). 
Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.'''

# start = int(input('Start: '))
# end = int(input('End: '))
# listOfElements = 0
# if start < end:
#     listOfElements = [i for i in range(start, end + 1)]
# elif start > end:
#     start, end = end, start
#     listOfElements = [g for g in range(start, end + 1)]
# print(sum(listOfElements))

'''3. Написать проверку на то, является ли введенное число нарциссическим: 
Пример 153 = 1^3 + 5^3 + 3^3. 153 - число нарцисс (число в степени - длина числе)'''

# number = input("Pls, enter a number: ")
# numberLength = len(number)
# sumOfElements = 0
# for i in range(0,numberLength):
#     sumOfElements += int(number[i]) ** numberLength
# print('Armstrong') if int(number) == sumOfElements else print('Not armstrong')

'''4*. Написать программу, которая выведет первые n чисел последовательности фибоначчи. n - вводится с клавиатуры.'''

# n = int(input('Pls, enter a number: '))
# f1, f2 = 1, 1
# for i in range (2, n):
#     f1, f2 = f2, f1+f2
#     print(f2)
