'''1. Напишите программу, которая принимает аргумент в виде списка и возвращает словарь,
в котором каждый элемент списка является и ключом и значением.
Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.'''

a = ['apple', 'banana', 'peach']
# 1 solution
dict_a = {fruit: fruit for fruit in a}

# 2 solution
dict_a = dict(zip(a, a))

print(dict_a)

'''2.  Есть число n, возьмите сумму цифр n. Если это значение имеет более одной цифры, 
продолжайте уменьшать таким образом, пока не будет получено однозначное число. Ввод будет неотрицательным целым числом.  
Пример:   
16  -->  1 + 6 = 7  
942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6   
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6   
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2 '''

n = int(input('Enter a number: '))
# 1 solution
new_n = 0
while n>0:
    new = n%10
    new_n += new
    n //= 10
if new_n > 10:
    n1 = new_n // 10
    n2 = new_n % 10
    new_n = n1 + n2
print(new_n)

# 2 solution
res = 0
while len(a) >= 2:
    for i in a:
        res += int(i)
    n = str(res)
else:
    print(a)


'''3.  Написать программу, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, 
если оно простое, и False - иначе.'''

n = int(input('Enter a number: '))

# 1 solution
d = 2
while n % d != 0:
    d += 1
if d == n:
    print('True')
else:
    print('False')

# 2 solution

for el in range(2, int(n ** 0.5) + 1):
    if n % el == 0:
        print(False)
        break
    else:
        print(True)
        break
