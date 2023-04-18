'''1. Вы вводите с клавиатуры последовательность чисел, разделённых запятой.
Составьте список и кортеж с этими числами.'''

sub = input('Enter a sequence of numbers separated by commas: ')
new_sub = ''.join(i for i in sub if i != ',')
print(list(new_sub), tuple(new_sub))

'''2. Написать программу, которая удаляет первый и последний символы строки. 
Если строка содержит меньше  двух символов - вывести сообщение об ошибке.'''

text = input('Enter str: ')
print(text[1:-1]) if len(text) > 2 else print(f'Error!"{text}" is too small.')

'''3. Напишите программу, которая проверяет есть ли в каком-либо списке дубликаты.'''

list1 = [1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 9, 9]
list2 = {i for i in list1 if list1.count(i) > 1}
print('Yes, ', list2) if list2 else print('No')
