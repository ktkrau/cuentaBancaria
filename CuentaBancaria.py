class CuentaBancaria:
    lista_cuentas = []

    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.lista_cuentas.append(self)


    def depositar(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self


    def mostrar_info_cuenta(self):
        print(f"Estado de cuenta: {self.balance}")

    def generar_interes(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.tasa_interes)
        return self
    
    @classmethod
    def imprimir_instancias(cls):
        print("Información de cuentas:")
        for cuentas in cls.lista_cuentas:
            cuentas.mostrar_info_cuenta()
