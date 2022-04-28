from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

meniu = Menu()
Coffee_Machine = CoffeeMaker()
money = MoneyMachine()

while True:
    chose = input(f"What would you like? {meniu.get_items()} ").lower()
    if chose == "espresso" or chose == "latte" or chose == "cappuccino":
        drink = meniu.find_drink(chose)
        if Coffee_Machine.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                Coffee_Machine.make_coffee(drink)


    elif chose == "off":
        print("Good by")
        break
    elif chose == "report":
        Coffee_Machine.report()
        money.report()
