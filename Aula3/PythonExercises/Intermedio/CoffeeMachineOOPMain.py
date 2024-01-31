from CoffeMachineMenuClass import Menu
from MoneyMachineClass import MoneyMachine
from CoffeeMakerClass import CoffeMaker

# CM_MI = MenuItem()
CM_M = Menu()
CM_CM = CoffeMaker()
CM_MM = MoneyMachine()

CM_CM.report()
CM_MM.report()

next = True
while next:
    options = CM_M.get_items()
    choise = input(f'Qué quiere tomar?, {options} ').lower()
    if choise == 'off':
        print('Máquina apagada')
        next = False
    elif choise == 'report':
        CM_CM.report()
        CM_MM.report()
    else:
        drink = CM_M.find_drink(choise)
        ingredients = CM_CM.check_resources(drink)
        if ingredients is True:
            CM_MM.calculate_monetary_value()
            OK = CM_MM.check_transaction(drink)
            if OK is True:
                CM_CM.resources_deducted(drink)
        elif ingredients is False:
            print(f'Transacción rechazada para el {drink.name}. Seleccione otra bebida')
