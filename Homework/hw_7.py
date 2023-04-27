import string

'''1.Написать функцию, которая будет конвертировать любую переданную ей строку в CamelCase.
"the-stealth-warrior" -> "theStealthWarrior"
"The_Stealth_Warrior" -> "TheStealthWarrior" '''


def camelCase(text: str) -> str:
    on_delete = string.punctuation + ' '
    text = text.title()
    new_text = ''.join(i for i in text if i not in on_delete)
    return new_text


print(camelCase("the-stealth-warrior"))
print(camelCase("The_Stealth_Warrior"))

''' 2. Написать функцию, принимающую число и возвращающую ближайший к этому числу палиндром.
11 -> 22
188 -> 191
191 -> 202
2541 -> 2552 '''


def palindrom(num: int) -> int:
    num += 1
    while str(num) != str(num)[::-1]:
        num += 1
    return num


print(palindrom(188))

''' 3. Написать программу, которая посчитает кол - во одинаковых элементов в списке.
Список будет заполняться рандомными целыми числами. Рекомендую использовать несколько функций
(для заполнения списка целыми числами, для подсчета количества) '''


def symbols_counting(list_num):
    if list_num == set(list_num):
        print('Sorry! There are no the same elements')
    else:
        count = len(list_num) - len(set(list_num))
        print(f'The same numbers appear {count} times')


def my_list():
    while True:
        a = int(input('Enter a number in the list: '))
        list_num.append(a)
        print(f'Your list is ', list_num)
        symbols_counting(list_num)


list_num = []

my_list()
