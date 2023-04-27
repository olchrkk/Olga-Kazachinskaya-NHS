'''1. Написать программу, которая удаляет первый и последний символы строки.
Если строка содержит меньше  двух символов - вывести сообщение об ошибке. '''


def delete_symbols():
    word = input('enter a word: ')
    raise ValueError('len <=2') if len(word) <= 2 else print(word[1:-1])


delete_symbols()

'''2. Напишите программу которая настроит отображение комментария к отметке 'мне нравится' в условном посте. 
Список имен передается в кач-ве аргумента.  
Например:   
[]                                -->  "no one likes this"   
["Peter"]                         -->  "Peter likes this"   
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"   
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"   
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this" '''


def likes():
    names = ["Alex", "Jacob", "Mark", "Max", 'Kitty']
    if len(names) == 0:
        print('no one likes this')
    elif len(names) == 1:
        print(f'{names[0]} likes this')
    elif len(names) == 2:
        print(f'{names[0]} and {names[1]} like this')
    elif len(names) == 3:
        print(f'{names[0]},{names[1]} and {names[2]} like this')
    elif len(names) > 3:
        print(f'{names[0]}, {names[1]} and {len(names)-2} others like this')


likes()

'''3. Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором. '''


def my_lists():
    list1 = input('enter the first list: ')
    list2 = input('enter the second list: ')
    list1 = set(list1.split(sep=','))
    list2 = set(list2.split(sep=','))
    print(list1.difference(list2))


my_lists()

'''4. Создайте простой калькулятор, который считывает из строки ввода
(пример: «1 + 13» три подстроки: 1-ое число, 2-ое число и операцию, после чего применяет операцию к введённым числам, 
а затем выводит результат на экран. '''


def calculator():
    num1 = float(input('first number: '))
    num2 = float(input('second number: '))
    operation = input('enter operation: +, -, /, * ')
    if operation == '+':
        print(num1+num2)
    elif operation == '-':
        print(num1-num2)
    elif operation == '*':
        print(num1*num2)
    elif operation == '/':
        print(num1/num2)
    else:
        print('Please, check your operation')


calculator()

'''5. Вы вводите с клавиатуры последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами.'''


def subsequence():
    subseq = input('Enter subsequence: ')
    print(f"List: {subseq.split(sep=',')}\nTuple: {tuple(subseq.split(sep=','))}")


subsequence()