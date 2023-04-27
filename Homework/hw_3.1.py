'''1. Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания,
если A < B, или в порядке убывания в противном случае.'''


def subsequence():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    subseq = []
    if a > b:
        while a >= b:
            subseq.append(str(a))
            a -= 1
    elif a < b:
        while a <= b:
            subseq.append(str(a))
            a += 1
    print(subseq)


subsequence()


'''2. Есть число n, вывести первые n чисел последовательности Фибоначчи.'''

# 1 1 2 3 5 8 13 21 34 55


def fibon():
    f_1 = f_2 = 1
    n = int(input('Count: '))
    i = 2
    print(f_1, f_2, end=' ')
    while i < n:
        f_1, f_2 = f_2, f_1+f_2
        print(f_2, end=' ')
        i += 1
    # for i in range(2, n):
    # f_1, f_2 = f_2, f_1+f_2
    # print(f_2, end=' ')


fibon()

'''3*. Дан список чисел. Реализуйте "bubble sort" для этого списка и верните, получившееся значение.'''


def  bubble(a):
    count = len(a)
    for _ in range(count):
        for j in range(count - 1):
            if a[j]> a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


print(bubble([1,2,3,12,6,4,123]))
'''4. Написать программу, которая будет конвертировать строку в CamelCase. Например: 
"the-stealth-warrior" -> "theStealthWarrior"  
"The_Stealth_Warrior" -> "TheStealthWarrior"  
"The_Stealth-Warrior" -> "TheStealthWarrior"'''


def camel(to_convert):
    to_delete = '-_'
    for i in to_convert:
        if i in to_delete:
            to_convert = to_convert.replace(i, ' ')
    result = [to_convert.split()[0]]
    for word in to_convert.split()[1:]:
        result.append(word.capitalize())
    return ''.join(result)


print(camel('the-stealth_warrior'))