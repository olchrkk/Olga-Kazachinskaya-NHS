import datetime


'''1. Напишите программу, которая примет в кач-ве аргумента integer (секунды) и вернет итоговое время в формате HH:MM:SS.
Например: (seconds=3666) -> 01:01:06 '''

sec = int(input('Enter: '))
hours = sec // 3600
minutes = (sec // 60) % 60
seconds = sec % 60
a = datetime.time(hours, minutes, seconds)
print(a)

'''2. Напишите программу которая настроит отображение комментария к отметке 'мне нравится' в условном посте. Список имен передается в кач-ве аргумента. 
Например:  
[]                                -->  "no one likes this"  
["Peter"]                         -->  "Peter likes this"  
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"  
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"  
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this" '''

names = input('Enter names: ')
list1 = names.split(sep=',')
print(len(list1), list1)
if len(list1) == 0:
    print('no one likes this')
elif len(list1) == 1:
    print(f'{list1[0]} likes this')
elif len(list1) > 1:
    print(f'{list1[0]} and {list1[1]} likes this')


users = []
if len(users) == 0:
    print('no one likes this')
elif len(users) == 1:
    print(f'{users[0]} likes this')
elif len(users) == 2:
    print(f'{users[0]} and {users[1]} like this')
elif len(users) == 3:
    print(f'{users[0]},{users[1]} and {users[2]} like this')
else:
    print(f'{users[0]},{users[1]} and {len(users) -2} like this')