'''1. Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно.
Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.  '''


def funk(start_new,end_new):
    sum_of = 0
    for i in range(start_new, end_new + 1):
        sum_of += i
    return sum_of


def sum_range(start, end):
    if type(start) == int and type(end) == int:
        if start < end:
            return funk(start, end)
        elif start > end:
            start, end = end, start
            return funk(start, end)
    else:
        raise ValueError('Start and end must be integers')


print(sum_range(5, 1))

''' 2. Написать функцию, которая принимает список и считает кол-во одинаковых элементов в нем. '''


def sum_of_same_numbers(lst):
    my_dict = {}
    my_sum = 0
    for i in lst:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    for j in my_dict:
        if my_dict[j] > 1:
            my_sum += 1
    return my_sum

print(sum_of_same_numbers([1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 5, 5, 6]))

''' 3. Написать функцию, принимающую число и возвращающую ближайший к этому числу палиндром.
11 -> 22
188 -> 191
191 -> 202
2541 -> 2552 '''

def palindrome():
    num = input('Введите число: ')
    sum_of_num = 0
    if num.isdigit():
        if num == num[::-1]:
            return f'Число {num} палиндром'
        else:
            while num != num[::-1]:
                sum_of_num = int(num) + 1
                num = str(sum_of_num)
            return num
    else:
        raise ValueError('Введите число!')


print(palindrome())
