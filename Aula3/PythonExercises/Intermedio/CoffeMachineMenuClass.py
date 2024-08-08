class MenuItem():
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.ingredients = {
            "water" : water,
            'milk' : milk,
            'coffee' : coffee
        }
        self.cost = cost
        
        
class Menu():
    def __init__(self):
        self.MENU = [ #Lista de objetos de MenuItem
            MenuItem("expreso", 50, 0, 18, 1.5),
            MenuItem("latte", 200, 150, 24, 2.5),
            MenuItem("capuchino", 250, 100, 24, 3)
        ]

    def get_items(self):
        string = []
        # c = ""
        for item in self.MENU:
            string.append(item.name)
            # c += f"{item.name}/"
        c = "/".join(string)  
        return c
    
    def find_drink(self, order_name):
        for item in self.MENU:
            if order_name == item.name:
                return item
      
