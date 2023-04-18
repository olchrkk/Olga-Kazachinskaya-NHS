'''1. Проверьте, если строка имеет одинаковое количество " х " и "о".
Метод должен возвращать логическое True/False если количесвто разное. Без учета регистра.
Примеры строк:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false '''

def same_number(word:str) -> bool:
    x_count = word.lower().count('x')
    o_count = word.lower().count('o')
    if x_count == o_count:
        return True
    return False

print(same_number(word='ooxx'))
print(same_number(word='xooxx'))
print(same_number(word='ooxXm'))
print(same_number(word='zpzpzpp'))
print(same_number(word='zzoo'))

'''2. Реализовать функцию, которая проверяет, является слово изограммой или нет. 
Изограмма - слово,  в котором нет повторяющихся символов.'''

def is_izogramma(word:str) -> bool:
    word_list = len(list(word))
    word_set = len(set(word))
    if word_list == word_set:
        return True
    return False

print(is_izogramma(word='hello'))
print(is_izogramma(word='help'))

'''3. Напишите функцию для проверки, является ли строка палиндромом.
Палиндромом называют фразу, которая читается одинаково как слева направо, так и справа налево.'''

def is_palindrom(word:str) -> bool:
    new_word = word[::-1]
    if word == new_word:
        return True
    return False

print(is_palindrom(word='дед'))
print(is_palindrom(word='собака'))
