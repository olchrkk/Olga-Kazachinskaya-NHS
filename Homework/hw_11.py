'''1. Реализовать класс Car с атрибутами название, километраж, страна производитель.
Переопределять метод eq (на основании страны производителя), создать метод для обнуления километража.
Реализовать метод, возвращающий значение кол-ва созданных экземпляров.
1.2. Создать функцию для генерирования заданного количества экземпляров.
1.3. Создать функцию, которая будет сортировать полученный список по переданному параметру(атрибут экземпляру)'''

# class Car:
#     __instance_counter = 0
#     def __init__(self, name, mileage, country):
#         self.name = name
#         self.mileage = mileage
#         self.country = country
#         Car.__instance_counter += 1
#
#     def __eq__(self, other):
#         return self.country == other.country
#
#     def null_milage(self):
#         self.milage = 0
#
#     def get_instance_count():
#         return Car.__instance_counter



'''2. Создайте класс "Банк", у которого есть атрибут "счет" и методы для открытия(0) и закрытия счета(None), 
а также методы для пополнения и снятия денег со счета. Пополнение и снятие возможно только для открытого счета.'''

class Bank:
    __dafault = 0
    def __init__(self, check=None):
        self.check = check

    def __str__(self):
        return f'check: {self.check}'

    def open_check(self):
        self.check = Bank.__dafault

    def close_check(self):
        if self.check:
            Bank.__dafault = self.check
        else:
            self.check = None

    def deposite(self, value):
        self.check += value

    def cash(self, value):
        self.check -= value


bank = Bank()
bank.open_check()
print(bank)
bank.deposite(1000)
print(bank)
bank.cash(10)
print(bank)
bank.close_check()
bank.open_check()
print(bank)

