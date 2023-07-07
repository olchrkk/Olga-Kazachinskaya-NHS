'''Создайте класс "Ресторан", у которого есть атрибут "Меню" и
методы для добавления и удаления блюд из меню, а также метод "заказ",
который выводит на экран список заказанных блюд.'''

menu = ['pizza', 'cheese', 'ice-cream']
class Restaurant:
    def __init__(self, menu: list):
        self.menu = menu

    def add_dish_to_menu(self, dish: list):
        self.menu.extend(dish)

    def del_dish_from_menu(self, del_item):
        if del_item in self.menu:
            self.menu.remove(del_item)

    def order(self, list_of_dish):
        return [x for x in list_of_dish if x in self.menu]


rest = Restaurant(menu)
rest.add_dish_to_menu(['burger', 'milk'])
print(rest.menu)
rest.del_dish_from_menu('milk')
print(rest.menu)