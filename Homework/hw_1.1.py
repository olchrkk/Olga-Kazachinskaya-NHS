import math as m

'''1. При заданном целом числе n посчитайте n + nn + nnn.
Например, если n = 3, нужно посчитать сумму 3 + 33 + 333 и вывести результат)'''

def sum_of_n(n:str)->int:
    n=str(n)
    x, y, z = n, n+n, n+n+n
    return int(x)+int(y)+int(z)

print(sum_of_n(3))

'''2. Есть две переменные, поменяйте их значение местами.'''

x, y = 1, 2
x, y = y, x
print(x, y)

'''3. Вы вводите c клавиатуры число - длина стороны равностороннего треугольника. 
Выведите высоту, площадь и периметр треугольника. Вывод должен быть вида:
"Высота треугольника: 12.5
Площадь треугольника: 24.3
Периметр треугольника: 18.2" '''


def triangle():
    num = float(input('enter num: '))
    print(f'Высота треугольника: {round(num * m.sqrt(3) / 2, 1)}\n'
          f'Площадь треугольника: {round(num ** 2 * m.sqrt(3) / 4, 1)}\n'
          f'Периметр треугольника: {round(3 * num, 1)}')


triangle()