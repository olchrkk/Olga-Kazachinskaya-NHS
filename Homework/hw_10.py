'''Создать класс Human c атрибутами name, surname, birth_year и двумя методами
full_name(), 
который будет  возвращать полное имя: Name Surname и get_age(), 
возвращающий возраст, созданного экземпляра.'''

class Human:
    def __init__(self, name, surname, birth_year):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def full_name(self):
        return f'{self.name} {self.surname}'

    def get_age(self):
        return 2023 - self.birth_year



human = Human('Alex', 'Bolt', 1998)
print(human.full_name())
print(human.get_age())