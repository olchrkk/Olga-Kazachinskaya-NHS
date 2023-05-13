from statistics import mean
from sympy import isprime


'''1. Напишите функцию, которая принимает строку и возвращает список всех уникальных символов в этой строке.'''
def unique_symbols(string):
    s = sorted(string)
    return list(set(s))

print(unique_symbols('helloworld'))

'''2. Напишите функцию, которая принимает на вход список строк и возвращает новый список,
содержащий только те строки, которые начинаются с буквы 'a' (большой или малой).'''

def a_string(array):
    return list(filter(lambda x: x[0] == 'a' or x[0] == 'A', array))

print(a_string(['hello', 'alex', 'word', 'Adam']))


'''3. Напишите функцию, которая принимает на вход список чисел и возвращает новый список,
содержащий только те числа, которые больше среднего значения всех чисел в списке.'''

def above_average(array):
    return list(filter(lambda x: x > mean(array), array))

print(above_average([2, 5, 6, 7, 8, 9]))

'''4. Напишите функцию, которая принимает на вход список строк и возвращает новый список,
содержащий те же строки, но с замененным первым символом на символ '*' (например, "hello" станет "*ello").'''

def new_first_index(array):
    return list(map(lambda x: '*'+x[1:], array))

print(new_first_index(['hello', 'alex', 'word', 'Adam']))

'''5. Напишите функцию, которая принимает на вход список списков чисел и возвращает новый список, 
содержащий те же числа, но увеличенные на 1.'''

def new_array(array):
    my_array = []
    for num in array:
        res = [i+1 for i in num]
        my_array+=res
    return my_array

print(new_array([[3,5],[4,8]]))

'''1. Напишите функцию, которая принимает на вход список чисел и возвращает новый список,
содержащий те же числа, но отсортированные по возрастанию.'''

def ascending(array):
    return sorted(array, reverse=False)

print(ascending([1,5,3,8,333,888,16]))

'''2. Напишите функцию, которая принимает на вход список слов и возвращает новый список,
содержащий только те слова, которые состоят только из букв (верхнего или нижнего регистра).'''

def only_letter(array):
    return list(filter(lambda x: x.isalpha(), array))

print(only_letter(['hello', '5alex', 'word', '9Adam']))

'''3. Напишите функцию, которая принимает на вход список чисел и возвращает новый список,
содержащий только те числа, которые делятся на 3 без остатка.'''

def without_a_trace(array):
    return list(filter(lambda x: (x % 3) == 0, array))

print(without_a_trace([1,2,4,5,6,3,8,9]))


'''4. Напишите функцию, которая принимает на вход список чисел и возвращает новый список,
содержащий только те числа, которые являются простыми.'''

def isPrime(array):
    return list(filter(lambda x: isprime(x), array))

print(isPrime([1,2,4,5,6,3,8,9]))


'''5. Напишите функцию, которая принимает на вход список строк и возвращает новый список,
содержащий только те строки, которые длиннее 5 символов.'''

def len_more_five(array):
    return list(filter(lambda x: len(x)>5, array))

print(len_more_five(['hello', '5alexxx', 'word', '9Adammmmm']))

'''6. Напишите функцию, которая принимает на вход список чисел и возвращает новый список,
содержащий те же числа, но умноженные на 2.'''

def squared(array):
    return list(map(lambda x: x*2, array))

print(squared([1,2,4,5,6,3,8,9]))

'''7. Напишите функцию, которая принимает на вход список строк и возвращает новый список, 
содержащий только те строки, которые содержат хотя бы одну цифру.'''

def numbers_in_a_word(array):
    ar = []
    for i in array:
        if any(map(str.isdigit, i)):
            ar.append(i)
    return ar
print(numbers_in_a_word(['hello', '5alex', 'word', '9Adam']))

'''8. Напишите функцию, которая принимает на вход список строк и возвращает новый список,
содержащий те же строки, но в верхнем регистре.'''

def numbers_in_a_word(array):
    return list(map(lambda x: x.upper(), array))

print(numbers_in_a_word(['hello', '5alex', 'word', '9Adam']))
