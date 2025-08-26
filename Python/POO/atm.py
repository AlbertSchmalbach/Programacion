class Atm:
    def __init__(self, pin):
        self.__pin = pin #private
        self._balance = 500000 #protec

    def deposit(self, amount):
        self._balance += amount
        print("Deposito exitoso!!!")
        print(f"Saldo actual: $ {self._balance}")
        print("="*60)

    def withdraw(self, amount):
        if self._balance > amount:
            self._balance -= amount
            print("Retiro exitoso!!!!")
            print(f"Cantidad retirada: {amount}")
            print("="*60)
        else:
            print("Saldo insufciente en cuanta")


    def show_balance(self):
        print(f"Tu saldo actual es: ${self._balance}")
        print("="*60)


    
    def change_pin(self, new_pin):
        if self.__pin != new_pin:
            self.__set_pin(new_pin)
            print("pin midificado correctamente!!!")
            print("="*60)
        else:
            print("Estas usando el mismo pin")
            print("="*60)


    def __set_pin(self, new_pin):
        self.__pin = new_pin
        
   