from model.model import Model
from view.view import View
import tkinter as tk

class Controller:
    def __init__(self, root):
        self.root = root
        self.model = Model()
        self.view = View(root, self)
        
        self.view.set_model(self.model)
        
    def compare_numbers(self):

        #Se computa la comparacion
        self.model.compare_numbers()

        #Se obtiene el resultado de la comparacion
        
        result = self.model.result   
        #Se actualiza la interfaz basandose en el resultado
        if(result== 1):
           self.view.update_result_label_A()
        elif(result==2):
           self.view.update_result_label_B()
        else:
           self.view.update_result_label_equal()
        #Se actualiza la interfaz
        

if __name__ == "__main__":
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()
