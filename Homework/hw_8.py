'''1.
Написать функцию, которая будет конвертировать любую переданную ей строку в CamelCase.
"the-stealth-warrior" -> "theStealthWarrior"
"The_Stealth_Warrior" -> "TheStealthWarrior" '''

# def camelCase(text:str) -> str:
#     replace_text = text.replace('-', ' ').replace('_', ' ')
#     replace_text = replace_text.title()
#     replace_text = ''.join(replace_text.split())
#     return replace_text
#
#
# print(camelCase('the-stealth-warrior'))
# print(camelCase('The_Stealth_Warrior'))

'''2.
Написать функцию, принимающую число и возвращающую ближайший к этому числу палиндром.
11 -> 22
188 -> 191
191 -> 202
2541 -> 2552 '''


def palindrom(num:str) -> str:
    num = input('number: ')
    length = 0
    while int(num) > 9:
        if num == num[::-1]:
            print(num)
            break
        else:
            length = int(num) + 1


palindrom(10)


'''3. Написать программу, которая посчитает кол - во одинаковых элементов в списке.
Список будет заполняться рандомными целыми числами.
Рекомендую использовать несколько функций
(для заполнения списка целыми числами, для подсчета количества)'''