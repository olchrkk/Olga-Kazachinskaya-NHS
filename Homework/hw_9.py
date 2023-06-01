from random import randint

'''Создайте функцию, Коротая генерирует словарь, состоящий из словарей, 
с ключам имя и номер телефонах.
Создайте функцию которая принимает этот словарь и еще один аргумент, 
который мб именем или номером телефона и осуществляет вызов)
Если соотв. Номера или имени нет в переданном словаре, 
то вызвать ошибку ValueError'''

# {'contact_list':({},{},{})}

names = {"Alex", "Bob", "Markus", "Peter", "Elise"}
phone_number = {"80293345672", "80297653428", "80338765432", "80291234567", "80333459876"}

def gen_contact_list()->dict:
    contacts = dict(zip(names, phone_number))
    return {'contact_list':contacts}

def search_contact(contact, value=None):
    phone_magazine = contact['contact_list']
    # for name in phone_magazine.keys():
    #     if name == value:
    #         return phone_magazine[name]
    for name, phone in phone_magazine.items():
        if name == value or phone == value:
            return f'calling {name}\n{phone}...'
    raise ValueError('Contact or name is not defined')


print(search_contact(contact=gen_contact_list(), value='Bob'))


