MENU = {
    "expreso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "capuchino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_decision(drink, money):
    next = True
    if drink == 'off':
        print('Máquina apagada')
        next = False
    elif drink == 'report':
        print(f"Agua: {resources['water']} ml")
        print(f"Leche: {resources['milk']} ml")
        print(f"Café: {resources['coffee']} g")
        print(f"Dinero: ${money}")
    else:
        ingredients = check_resources(drink)
        if ingredients is True:
            dollars = calculate_monetary_value()
            sale, OK = check_transaction(drink, dollars)
            money += sale
            if OK is True:
                resources_deducted(drink)
        elif ingredients is False:
            print(f'Transacción rechazada para el {drink}. Seleccione otra bebida')
            next = True
        
    return money, next

def check_resources(drink):
    ingredients = True
    for key, val in MENU.items():
        if drink == key:
            for item in val["ingredients"]:
                if resources[item] < val["ingredients"][item]:
                    print(f"No hay {item} suficiente para el {key}")
                    ingredients = False
            break
    return ingredients

def calculate_monetary_value():
    print("Ingrese el dinero")
    quarters = int(input('Ingrese las monedas de quartos de dólar ($0.25): $'))
    dimes = int(input('Ingrese las monedas de diez centavos de dólar ($0.1): $'))
    nickles = int(input('Ingrese las monedas de cinco centavos de dólar ($0.05): $'))
    pennies = int(input('Ingrese las monedas de un centavo de dólar ($0.01): $'))
    payment = (quarters*0.25)+(dimes*0.1)+(nickles*0.05)+(pennies*0.01)
    print(f'Total de dinero ingresado: ${payment:.2f}')
    return payment

def check_transaction(drink, money):
    for key, val in MENU.items():
        if drink == key:
            if money < val["cost"]:
                print(f"El dinero ingresado no es suficiente para el {key}. Dinero reembolsado")
                return 0, False
            else:
                change_value = money-val["cost"]
                print('Transacción exitosa')
                print(f"Su cambio es ${change_value:.2f}")
                sale_value = val["cost"]
                return sale_value, True

def resources_deducted(drink):
    for key, val in MENU.items():
        if drink == key:
            for item in val["ingredients"]:
                resources[item] -= val["ingredients"][item]    
            print(f"Aquí está su {key} ☕. Disfrútelo.")
            break

def CoffeeMachineFunction():
    profit = 0
    next = True
    while next:
        choise = input('Qué quiere tomar?, (expreso, latte, capuchino): ').lower()
        profit, next = check_decision(choise, profit)


# ............................... OPCION 2 ...............................

# MENU = {
#     "expreso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "capuchino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }

# def check_decision(drink, money):
#     if drink == 'off':
#         return False
#     elif drink == 'report':
#         print(f"Agua: {resources['water']} ml")
#         print(f"Leche: {resources['milk']} ml")
#         print(f"Café: {resources['coffee']} g")
#         print(f"Dinero: ${money}")
#     return True

# def check_resources(drink):
#     water = True
#     coffee = True
#     milk = True
#     for key, val in MENU.items():
#         if drink == key:
#             if resources["water"] < val["ingredients"]['water']:
#                 print(f"No hay agua suficiente para el {key}")
#                 water = False
#             if resources["coffee"] < val["ingredients"]['coffee']:
#                 print(f"No hay café suficiente para el {key}")
#                 coffee = False
#             if key in ('latte', 'capuchino'):
#                 if resources["milk"] < val["ingredients"]['milk']:
#                     print(f"No hay leche suficiente para el {key}")
#                     milk = False
#             break
#         if water is True and coffee is True and milk is True:
#             ingredients = True
#         else:
#             ingredients = False
#     return ingredients

# def calculate_monetary_value():
#     print("Ingrese el dinero")
#     quarters = float(input('Ingrese las monedas de quartos de dólar ($0.25): $'))
#     dimes = float(input('Ingrese las monedas de diez centavos de dólar ($0.1): $'))
#     nickles = float(input('Ingrese las monedas de cinco centavos de dólar ($0.05): $'))
#     pennies = float(input('Ingrese las monedas de un centavo de dólar ($0.01): $'))
#     money = (quarters*0.25)+(dimes*0.1)+(nickles*0.05)+(pennies*0.01)
#     print(f'Total de dinero ingresado: ${money:.2f}')
#     return money

# def check_transaction(drink, money):
#     for key, val in MENU.items():
#         if drink == key:
#             if money < val["cost"]:
#                 print(f"El dinero ingresado no es suficiente para el {key}. Dinero reembolsado")
#                 return 0, False
#             elif money == val["cost"]:
#                 print('Transacción exitosa')
#                 print(f"El dinero ingresado es igual al costo de {key}")
#                 sale_value = val["cost"]
#                 return sale_value, True
#             else:
#                 change_value = money-val["cost"]
#                 print('Transacción exitosa')
#                 print(f"Su cambio es ${change_value:.2f}")
#                 sale_value = val["cost"]
#                 return sale_value, True

# def resources_deducted(drink):
#     for key, val in MENU.items():
#         if drink == key:
#             resources["water"] -= val["ingredients"]['water']
#             resources["coffee"] -= val["ingredients"]['coffee']
#             if key in ('latte', 'capuchino'):
#                 resources["milk"] -= val["ingredients"]['milk']
#             print(f"Aquí está su {key}. Disfrútelo.")
#             break

# def CoffeeMachineFunction():
#     profit = 0
#     machine = True
#     next = True
#     while next:
#         choise = input('Qué quiere tomar?, (expreso, latte, capuchino): ').lower()

#         machine = check_decision(choise, profit)
#         if machine is True:
#             ingredients = check_resources(choise)
#             if ingredients is True:
#                 dollars = calculate_monetary_value()
#                 sale, OK = check_transaction(choise, dollars)
#                 profit += sale
#                 if OK is True:
#                     resources_deducted(choise)
#             else:
#                 print('Transacción rechazada')
#                 next = False
#         else:
#             print('Máquina apagada')
#             next = False
