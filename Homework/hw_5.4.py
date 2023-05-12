import time
import datetime

'''1. Напишите программу, которая выводит на экран все числа от 1 до 10.'''

def subsequence():
    for j in range(1,11):
        print(j, end=' ')

subsequence()

'''2. Напишите программу, которая запрашивает у пользователя число n, а затем выводит на экран все числа от 1 до n.'''

def sebsequence_2():
    num = int(input("Enter your number: "))
    for i in range(1, num+1):
        print(i, end=' ')


sebsequence_2()

'''3. Напишите программу, которая выводит на экран все четные числа от 2 до 20.'''

def sebsequence_3():
    for i in range(2,21):
        if i%2==0:
            print(i, end=' ')

sebsequence_3()


'''4. Напишите программу, которая запрашивает у пользователя число n, а затем выводит на экран все четные числа от 2 до n.'''

def sebsequence_4():
    num = int(input("Enter your number: "))
    for i in range(2, num+1):
        if i%2==0:
            print(i, end=' ')


sebsequence_4()

'''5. Напишите программу, которая выводит на экран таблицу умножения от 1 до 10.'''

def sheet():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f'{i} * {j} = {i*j}')


sheet()

'''6. Напишите программу, которая запрашивает у пользователя число n, а затем выводит на экран таблицу умножения от 1 до n.'''

def sheet_2():
    num = int(input("enter your number: "))
    for i in range(1, num+1):
        for j in range(1, num+1):
            print(f'{i} * {j} = {i * j}')


sheet_2()

'''7. Напишите программу, которая запрашивает у пользователя число n, а затем выводит на экран все числа от n до 1 в обратном порядке.'''

def sebsequence_4():
    num = int(input("enter your number: "))
    i = 1
    lst = []
    while i<=num:
        lst.append(str(i))
        i+=1
    lst.reverse()
    print(', '.join(lst))


sebsequence_4()
'''8. Напишите программу, которая выводит на экран все буквы английского алфавита.'''

def alphabet():
    for i in range(ord('a'), ord('z')+1):
        print((chr(i)).upper()+chr(i), end=' ')


alphabet()

'''9. Напишите программу, которая запрашивает у пользователя слово, а затем выводит на экран все буквы этого слова в обратном порядке.'''

def word():
    my_word = input('enter word: ')
    print(f'your word: {my_word}, new word: {my_word[::-1]}')

word()

'''10. Напишите программу, которая запрашивает у пользователя слово, а затем выводит на экран все буквы этого слова, кроме буквы "а".'''

def word_1():
    my_word = input('enter word: ')
    for i in my_word:
        if i == 'a' or i == 'A':
            continue
        else:
            print(i, end=' ')


word_1()

'''1. Создать функцию, которая принимает список чисел и возвращает новый список, состоящий из квадратов чисел, которые больше 10.'''

def my_list(lst):
    res = list(map(lambda x:x*x, lst))
    for i in res:
        if i < 10:
            res.remove(i)
    return res


print(my_list([1,2,3,4,5,6,7,8,9,10]))

'''2. Написать функцию, которая принимает список строк и сортирует их по возрастанию длины каждой строки.'''

def string(array):
    array.sort(key=len)
    return array

print(string(['hello','hi','привет','hola']))

'''3. Написать функцию, которая принимает список целых чисел и проверяет, содержит ли он только простые числа.'''

def is_prime(number):
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            return False
    return True

def all_is_prime(array):
    for i in array:
        if is_prime(i) is False:
            return False
    return True

print(all_is_prime([1,3,5,6,8,9]))

'''4. Написать функцию, которая принимает список словарей, где каждый словарь представляет собой запись об ученике (с ключами 'имя', 'возраст', 'оценки'),
и возвращает список словарей, отсортированный по возрасту учеников в порядке убывания средней оценки каждого ученика.'''

school = [
    {'Name': 'Dasha', 'Age': 9, 'Grade': 6},
    {'Name': 'Pasha', 'Age': 11, 'Grade': 3},
    {'Name': 'Masha', 'Age': 10, 'Grade': 2},
    {'Name': 'Kate', 'Age': 13, 'Grade': 5}
]

def grades(school):
    school.sort(key=lambda x: (x['Age'], x['Grade']))
    return school

print(grades(school))

'''5*. Написать функцию, которая принимает дерево, представленное в виде списка списков, 
где каждый элемент списка может быть либо числом, либо подсписком, и возвращает сумму всех чисел в дереве.'''

lst = [ 2,
    [1,3,4],
    [6,5], 5,
    [1,1,1,1],
]
def sum_of_num(lst):
    my_sum = 0
    for l in lst:
        if type(l) == int:
            my_sum += l
        else:
            for i in l:
                my_sum += i
    return my_sum

print(sum_of_num(lst))


'''6. Написать функцию, которая принимает список дат в формате 'ДД.ММ.ГГГГ' и возвращает список дат в формате 'ГГГГ-ММ-ДД', отсортированный по возрастанию.'''

date_list_upd = []
def date(array):
    for i in range(len(array)):
        date_list_upd.append('-'.join(i.split('.')[::-1]))

print(date(['19-05-2003', '03-06-2004', '21-06-2008','30-05-2023']))
