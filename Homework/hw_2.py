'''1. Напишите программу для слияния нескольких словарей в один.'''

dict1={'key1':'value1','key2':'value2'}
dict2={'key3':'value3','key4':'value4'}
#version 1 for 2 dictionaries
dict1.update(dict2)
print(dict1)

#version 2 for more 2 dictionaries
dict3={**dict1, **dict2}
print(dict3)

'''2. Вам дан список вида [1, 2, 2, 3, 4, 6, 7, 7, 7, 8, 1, 1, 2, 312, 23, 2], 
удалите все дубликаты из этого списка и верните этот же  список отсортированный по убыванию.
( Список должен быть тем же, что передается, для проверки используйте функцию возвращающую адрес этого объекта в памяти)'''

list1=[1, 2, 2, 3, 4, 6, 7, 7, 7, 8, 1, 1, 2, 312, 23, 2]
list1=list(set(list1))
print(list1, id(list1))
list1.sort(reverse=True)
print(list1, id(list1))

'''3. Вам дан словарь, состоящий из 3 элементов, верните список, состоящий из ключей этого словаря.'''

dict5={'key5':'value5','key6':'value6','key7':'key7'}
print(list(dict5.keys()))

