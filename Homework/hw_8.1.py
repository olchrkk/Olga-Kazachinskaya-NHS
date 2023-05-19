from datetime import time
from itertools import zip_longest
from random import randint
import random
from collections import Counter

'''1. Напишите декоратор timer, который измеряет время выполнения функции и выводит его на экран.
Используйте модуль time для измерения времени.'''

# def timer()

'''2. Написать функцию, которая принимает на вход два списка чисел и возвращает новый список, 
содержащий суммы соответствующих элементов этих списков.'''

lst1 = [1,2,3]
lst2 = [4,5,6,7]

def sum_of_lst(a, b):
    # return list(map(sum, zip(a,b))) - the same quantity of numbers
    return [x+y for x, y in zip_longest(a, b, fillvalue=0)]

print(sum_of_lst(lst1, lst2))

'''3. Написать программу, которая посчитает кол-во одинаковых элементов в списке. 
Список будет заполняться рандомными целыми числами.
Рекомендую использовать несколько функций (для заполнения списка целыми числами, для подсчета количества, для вывода)'''

lst = [randint(1, 20) for i in range(20)]
print(lst)
# sol 1
# s = Counter(lst)
# print(s)
# sol 2
# s = set(lst)
# for i in s:
#     print(f"'{i}': {lst.count(i)}")


'''4.'''
first_name= ['Sasha', 'Pasha', 'Dasha', 'Masha']
last_name= ['Petrov', 'Hitrov', 'Popok', 'Mashrov']
full_name= random.choice(first_name)+' '+random.choice(last_name)
age = randint(10, 70)
gpa = random.uniform(0.0, 10.0)

# gen_dict = (lambda: (dict([('name', full_name) for _ in range(10)])))
# print(gen_dict())