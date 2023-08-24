class Model:
    def __init__(self):
        self.num1 = None
        self.num2 = None
        self.result = None

    #Metodo en el que se realiza la computacion del numero mayor, 1 indica que el numero 1 es mayor que el numero 2
    #2 indica que el numero 2 es mayor que el numero 1 y 0 indica que el numero 1 y numero 2 son iguales.
    def compare_numbers(self):
        if self.num1>self.num2:
           self.result = 1
        elif self.num1<self.num2:
           self.result = 2
        else:
           self.result = 0
