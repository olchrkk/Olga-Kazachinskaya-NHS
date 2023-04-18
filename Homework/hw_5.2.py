from sympy import isprime

'''1. Передается список, содержащий элементы разных типов (строки, int, float и тд)
Необходимо посчитать целых чисел из этого списка.'''

list1 = ['hello', 1, 2.3, 5, 7.3, 8]

# 1 solution
sum_list1 = 0
for i in list1:
    if isinstance(i, int):
        sum_list1 += i
print(sum_list1)

# 2 solution
res =0
for elem in list1:
    if isinstance(elem, int):
        res += 1
    else:
        continue
print(res)


'''2. Есть два списка одинаковой длины, необходимо составить словарь из этих двух списков. Напримр:
products = [apple, milk, orange]
count = [1, 3, 12]
Результат должен быть: {apple: 1, milk: 3, orange: 12}'''

products = ['apple', 'milk', 'orange']
count = [1, 3, 12]
new_dict = dict(zip(products, count))
print(new_dict)

'''3. Написать программу на определение, является ли введенное число простым. 
Число должно вводится с клавиатуры любое количество раз без запуска программы заново, 
завершение программы произойдет только при вводе пользователем слова "exit" вместо числа.'''

a = ''
d = ''
while True:
    a = input('Enter a number: ')
    if a == 'exit':
        break
    elif not a.isdigit() or int(a) == 0:
        print('Pls, enter a number')
    else:
        a = int(a)

# solution 1
        d = 2
        while a % d != 0:
            d += 1
        print(f'Number {a} is simple') if d == a else print(f'Number {a} is composite')
#
#solution 2
        print(f'Number {a} is simple') if isprime(a) else print(f'Number {a} is composite')

