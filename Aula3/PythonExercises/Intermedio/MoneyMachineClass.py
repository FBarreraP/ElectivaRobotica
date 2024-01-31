class MoneyMachine():
    def __init__(self):
        self.profit = 0
        self.payment = 0
    
    COIN_VALUES = {
        "quarto": 0.25,
        "diez centavos": 0.10,
        "cinco centavos": 0.05,
        "un centavo": 0.01
    }
    
    def report(self):
        print(f"Dinero: ${self.profit}")
    
    def calculate_monetary_value(self):
        print("Ingrese el dinero")
        for key, val in self.COIN_VALUES.items():
            self.payment += int(input(f'Ingrese las monedas de {key} de dólar ${val}): $')) * val
        print(f'Total de dinero ingresado: ${self.payment:.2f}')
        
    def check_transaction(self, order):
        if self.payment < order.cost:
            print(f"El dinero ingresado no es suficiente para el {order.name}. Dinero reembolsado")
            return False
        else:
            print('Transacción exitosa')
            change_value = self.payment-order.cost
            print(f"Su cambio es ${change_value:.2f}")
            self.profit += order.cost
            self.payment = 0
            return True