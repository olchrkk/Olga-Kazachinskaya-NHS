'''1. "1 2 3 4 5" найдите самое большое и маленькое число в этой строке и верните их кортежем. '''

def min_max(array):
    lst_array = array.split()
    lst_int_array = list(map(int, lst_array))

    return (min(lst_array), max(lst_array))


print(min_max("1 2 3 4 5"))

'''2. Написать программу, которая может принимать любое неотрицательное целое число в качестве аргумента и
возвращать новое максимально возможное значение, составленное из цифр этого же числа.
По сути, просто переставить цифры, чтобы создать максимально возможное число.  '''

def number():
    num = int(input('your number: '))
    if num > 0:
        lst_num = list(str(num))
        lst_num.sort(reverse=True)
        print(int(''.join(lst_num)))
    else:
        raise ValueError('the number is negative')

number()

'''3. Передается список, состоящий из строк и букв, нужно вернуть новый список, содержащий только цифры. '''

def mylistOfNumbers(numbers):
    result = []
    for number in numbers:
        if number.isdigit():
            result.append(int(number))
    return result

print(mylistOfNumbers(['1','Hello', '2', '3', 'Number']))

'''4. С клавиатуры вводится натуральное число. 
Найти его наибольшую цифру. Например, введено число 764580. Наибольшая цифра в нем 8.'''

def findNumber():
    num = input('Your number: ')
    num_lst = list(map(int, num))
    print(max(num))


findNumber()