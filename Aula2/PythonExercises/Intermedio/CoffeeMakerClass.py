class CoffeMaker():
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
    
    def report(self):
        print(f"Agua: {self.resources['water']} ml")
        print(f"Leche: {self.resources['milk']} ml")
        print(f"Café: {self.resources['coffee']} g")
        
    def check_resources(self, drink):
        ingredients = True
        for key, val in drink.ingredients.items():
            if self.resources[key] < val:
                print(f"No hay {key} suficiente para el {drink.name}")
                ingredients = False
        return ingredients
        
    def resources_deducted(self, order):
        for key, val in order.ingredients.items():
            self.resources[key] -= val
        print(f"Aquí está su {order.name} ☕. Disfrútelo.")