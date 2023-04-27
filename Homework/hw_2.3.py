'''1. Создать произвольный список -> Добавить новый элемент типа str в конец списка ->
Добавить новый элемент типа int на место с индексом  0 ->
Добавить новый элемент типа list в конец списка ->
Добавить новый элемент типа tuple на место с индексом 1 ->
Получить элемент по индексу 3 -> Удалить элемент с индексом 0
 -> Найти длину списка '''

# my_list = ['1','Hello', '2', '3', 'Number']
#
# def new_list():
#     my_list.append('Hi')
#     my_list.insert(0, 25)
#     my_list.append([1, 3, 'hi'])
#     my_list.insert(1, (1, 'hi', ))
#     print(my_list[3])
#     my_list.remove(my_list[0])
#     print(len(my_list))
#     return my_list
#
#
# print(new_list())

'''2. Дан список, нужно проверить, есть ли в нем дубликаты '''

# def duplicates(array):
#     array_set = set(array)
#     print('No') if len(array_set) == len(array) else print('Yes')
#
#
# duplicates(['1', 'hi', '2', '3', 'hi', '3'])

'''3. Создать произвольный словарь -> 
Добавить новый элемент с ключом типа str и значением типа int -> 
Добавить новый элемент с ключом типа кортеж(tuple) и значением типа список(list) -> 
Получить элемент по ключу -> Удалить элемент по ключу -> Получить список ключей словаря. '''

my_dict = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}

def new_dict():
    my_dict['fifth'] = 5
    my_dict[('sixth',)] = [1,2,3]
    print(my_dict.get('first'))
    my_dict.pop('second')
    print(my_dict.keys())


new_dict()

'''4. Пользователь  вводит число, необходимо проверять это число на нечетность, 
если оно нечетное, выводить True, иначе False '''

# def odd():
#     number = int(input('enter a number: '))
#     print('False') if number % 2 == 0 else print('True')
#
# odd()