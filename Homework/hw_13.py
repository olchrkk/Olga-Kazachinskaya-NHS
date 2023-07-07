'''1. Создайте класс "Человек" с атрибутами "имя", "возраст" и "рост".
Используя property декоратор, реализуйте методы получения и установки значений для каждого атрибута.'''

class Human:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nHeight: {self}'

    def __repr__(self):
        return f'name: {self.name}, age:{self.age}, height: {self.height}'

    @property
    def full_inf(self):
        return self.name, self.age, self.height

    @full_inf.deleter
    def full_inf(self):
        self.name = None
        self.age = None
        self.height = None


    @full_inf.setter
    def full_inf(self, value):
        name, age, height = value.split(',')
        self.name = name
        self.age = age
        self.height = height

human = Human('Alex', 23, 192)
print(human.age, human.height, human.name)

human.full_inf = 'Pol, 24, 185'
print(human.age, human.height, human.name)

del human.full_inf
print(human.age, human.height, human.name)

'''2. Создайте класс "Круг" с атрибутом "радиус". Используя property декоратор, реализуйте методы получения и установки значения радиуса. 
Также добавьте метод для вычисления площади круга.'''


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'Радиус:{self.radius}.'

    def __repr__(self):
        return f'radius: {self.radius}'

    @property
    def my_radius(self):
        return f'Радиус:{self.radius}.'

    @my_radius.setter
    def my_radius(self, value):
        self.radius = value

    def square(self):
        return f"Радиус:{self.radius}." \
               f"Площадь - {3.14*self.radius**2}"


circle_1 = Circle(5)
print(circle_1, circle_1.square())
circle_1.radius = 6
print(circle_1, circle_1.square())


'''3. Создайте класс "Банк" с атрибутом "баланс". Используя property декоратор, реализуйте методы получения и установки значения баланса. 
Также добавьте методы для пополнения и снятия денег со счета. '''

class Bank:
    def __init__(self, balance = None):
        self.balance = balance

    def __str__(self):
        return f'Balance:{self.balance}.'

    def __repr__(self):
        return f'balance: {self.balance}'

    @property
    def account(self):
        return f'Balance: {self.balance}'

    @account.setter
    def account(self, value):
        self.balance = value

    @account.deleter
    def account(self):
        self.balance = None

    def replenis(self, value):
        if self.balance is not None:
            self.balance += value
        else:
            print('account closed')


    def withdraw_money(self, value):
        if self.balance is not None:
            self.balance -= value
        else:
            print('account closed')


my_account = Bank(1000)
print(my_account.account)
my_account.account = 500
print(my_account.account)
my_account.replenis(1000)
my_account.withdraw_money(400)
print(my_account.account)



'''4. Создайте класс "Телефон" с атрибутами "модель", "цвет" и "стоимость". 
 Используя property декоратор, реализуйте методы получения и установки значений для каждого атрибута. 
 Также добавьте метод для вычисления скидки на телефон в зависимости от его стоимости.'''


class Phone:
    def __init__(self, model, colore, price: int):
        self.model = model
        self.colore = colore
        self.price = price

    def __str__(self):
        return f'{self.model}{self.colore} price {self.price}'

    def __repr__(self):
        return f'model = {self.model} colore = {self.colore} price = 34{self.price}'

    @property
    def details(self):
        return self.model, self.colore, self.price

    @details.setter
    def details(self, value):
        model, colore, price = value.splite(',')
        self.model = model
        self.colore = colore
        self.price = price

    def discount(self):
        if self.price > 500:
            return f'Your discount is 20%. New price {self.price*20/100}$'
        return f'We have no discount for you. Full price is {self.price}$'


phone_1 = Phone('Apple', 'black', 1100)
print(phone_1.details)
phone_1.colore = 'white'
print(phone_1.discount())

phone_2 = Phone('Apple', 'black', 499)
print(phone_2.discount())
