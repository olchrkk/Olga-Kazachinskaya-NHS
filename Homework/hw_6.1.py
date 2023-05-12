from collections import Counter

"""1. Напишите функцию, которая принимает список чисел и возвращает список квадратов этих чисел. """
def square(array):
    return list(map(lambda x: x**2, array))

print(square([1,2,3,4]))

'''2. Напишите функцию, которая принимает на вход список строк и возвращает список строк, длина которых больше 5 символов. '''

def length_of_string(array):
    return list(filter(lambda x: len(x)>5, array))

print(length_of_string(['hello', 'world', 'hi', 'blablala']))
'''3. Напишите функцию, которая принимает на вход список чисел и возвращает только четные числа из этого списка. '''

def even_numbers(array):
    return list(filter(lambda x: x%2 == 0, array))

print(even_numbers([1,2,3,4,5,6,7,8,9]))

'''4. Напишите функцию, которая принимает на вход список чисел и возвращает сумму квадратов четных чисел из этого списка. '''

def sum_of_squares(array):
    even_num = list(filter(lambda x: x%2 == 0, array))
    squares = list(map(lambda x: x**2, even_num))
    return sum(squares)

print(sum_of_squares([1,2,3,4]))
'''5. Напишите функцию, которая принимает на вход список строк и возвращает список строк, которые начинаются с буквы "a". '''

def first_index_A(array):
    return list(filter(lambda x: x[0]=='a', array))

print(first_index_A(['apple', 'banana', 'america']))

'''6. Напишите функцию, которая принимает на вход список чисел и возвращает список чисел, которые больше 10 и меньше 20. '''

def between_numbers(array):
    return list(filter(lambda x: x in range(10,20), array))

print(even_numbers([20, 1, 11, 5, 18, 25]))

'''7. Напишите функцию, которая принимает на вход список строк и возвращает список строк, которые содержат букву "e". '''

def find_string(array):
    return list(filter(lambda x: 'e' in x, array))

print(find_string(['hello','hi','lera','lola']))

'''8. Напишите функцию, которая принимает на вход список чисел и возвращает True, если все числа в списке положительные, и False в противном случае. '''

def positive_numbers(array):
    for i in array:
        if i<=0:
            return False
        else:
            return True

print(positive_numbers([1, 2, 3, 4, 5]))


'''9. Напишите функцию, которая принимает на вход список строк и возвращает список строк, которые содержат только цифры. '''

def numbers(array):
    return list(filter(lambda x: x.isdigit(), array))

print(numbers(['123', 'hello', '25', 'hi']))

'''10. Напишите функцию, которая принимает на вход список чисел и возвращает список чисел, которые являются степенями двойки.'''

def two(array):
    return list(filter(lambda x: x & (x - 1) == 0, array))

print(two([8,4,12,11,64, 33]))
'''1. Напишите функцию, которая принимает на вход список строк и возвращает наиболее часто встречающуюся строку.'''

def popular_string(lst):
    if len(lst) != set(lst):
        count_lst = Counter(lst)
        max_val = max(count_lst, key=count_lst.get)
        return max_val
    else:
        return 'None'


print(popular_string(['hello','hi','hola','hi']))

'''2. Напишите функцию, которая принимает на вход два списка и возвращает новый список, содержащий элементы, которые есть в обоих списках. '''

a = [1,2,3,4]
b = [5,6,7,8]
def two_lists(a,b):
    return a.extend(b)

print(two_lists(a,b))

'''3. Напишите функцию, которая принимает на вход строку и возвращает количество слов в этой строке, в которых есть более 3-х гласных (a, e, i, o, u).'''


