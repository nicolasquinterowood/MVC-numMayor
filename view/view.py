import tkinter as tk
from tkinter import ttk
#Metodo para el reajuste de imagenes
from PIL import Image, ImageTk
class View:
  
    #Variable para el texto de la interfaz  
    TEXT_HEADER_FONT =("Century Gothic", 22, "bold")

    #Paragraph font
    TEXT_PARAGRAPH_FONT =("Century Gothic", 12)

    #Paragraph font
    TEXT_HEADER2_FONT =("Century Gothic", 22, "bold")

     #Paragraph font
    TEXT_PARAGRAPH2_FONT =("Century Gothic", 8)

    #Color del texto
    TEXT_COLOR = '#233845'

    #Direccion Imagen fondo
    BACKGROUND_PATH= "C:/Users/nicolas.quintero/Desktop/Development/Sostenibilidad e innovacion/Induccion/elementos/Fondo_1.png"
    #Direccion Imagen boton comparar
    COMPARE_BUTTON_PATH= "C:/Users/nicolas.quintero/Desktop/Development/Sostenibilidad e innovacion/Induccion/elementos/B_Comparar_2.png"
    #Direccion Imagen boton home
    HOME_ICON_PATH ="C:/Users/nicolas.quintero/Desktop/Development/Sostenibilidad e innovacion/Induccion/elementos/B_Inicio.png"
    #Direccion Imagen boton cerrar
    CLOSE_ICON_PATH = 'C:/Users/nicolas.quintero/Desktop/Development/Sostenibilidad e innovacion/Induccion/elementos/B_Cerrar.png'
    
  
    # Validation callback to allow only integer input
    def validate_input(self,action, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        if action == '1':  # Insert action
           if value_if_allowed.isdigit() and len(value_if_allowed)<=2:
             return True
           return False
        return True
     #Para comparar\
    def animacion_boton(self,canvas,widget, root):
        canvas.tag_bind(widget,"<Enter>", lambda event: root.config(cursor="hand2"))
        canvas.tag_bind(widget,"<Leave>", lambda event: root.config(cursor=""))
    
       #Para procesamiento de imagenes
    def resize_image(self,image, width, height):
        resized_image = image.resize((width, height), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(resized_image)
    

    #Metodo de inicio
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.model = None
        self.root.resizable(False, False)
        #Ocultar la barra
        #self.root.overrideredirect(True)
        #Se define la funcion parar cerrar el programa
        def close_program(event):
            self.root.destroy()
 
        #Se establece el titulo del programa
        self.root.title("Numero Mayor")
        
        #Se establecen los pixeles de la ventana
        self.root.geometry('600x333') 
       
        # Se obtiene la imagen que va a ser el fondo de pantalla
        self.bg = tk.PhotoImage(file = self.BACKGROUND_PATH)

        #Se importa la imagen y se ajusta
        self.original_home_Icon = Image.open(self.HOME_ICON_PATH)

        self.home_icon = self.resize_image( self.original_home_Icon, width=20, height=20)

        #Se repite el proceso
        self.original_close_icon = Image.open(self.CLOSE_ICON_PATH)

        self.close_icon = self.resize_image(self.original_close_icon,width=20,height=20)

        # Create Canvas
        self.canvas = tk.Canvas(root, width = 333,
                 height = 600)
        
        # Se muestra el canva
        self.canvas.pack(fill = "both",expand = True)

       # Se despliega la imagen
        self.canvas.create_image( 300,166, image = self.bg)

       # Titulo
        self.titulo= self.canvas.create_text(182,18,text = "¡Número Mayor!", font=self.TEXT_HEADER_FONT, anchor="nw" ,fill =self.TEXT_COLOR)

       # Descripcion
        self.descripcion= self.canvas.create_text(107,78,text = "Ingresa dos números para saber cual es el mayor.", font=self.TEXT_PARAGRAPH_FONT, anchor="nw", fill =self.TEXT_COLOR)

        # Indicador de input A  
        self.numero1=self.canvas.create_text(106,115,text = "Número A", font=self.TEXT_HEADER2_FONT, anchor="nw", fill =self.TEXT_COLOR)

        # Indicador de input B
        self.numero2=self.canvas.create_text(349,115,text = "Número B", font=self.TEXT_HEADER2_FONT, anchor="nw", fill =self.TEXT_COLOR)
     
       #Descripcion
        self.descripcion=self.canvas.create_text(236,310,text = "Designed by Wood © 2023", font=self.TEXT_PARAGRAPH2_FONT, anchor="nw", fill =self.TEXT_COLOR)

        #Se le asigna estilo a las entradas 
        self.color_fondo_entry = "#F5F5F5" 

        self.color_marco = "#03A7BB"
        # Entradas
        self.entry = tk.Entry(master=root,font=self.TEXT_HEADER2_FONT, justify='center', background= '#E7E7E8', foreground=self.TEXT_COLOR, validate='key')
        self.entry_2 = ttk.Entry(master=root,font=self.TEXT_HEADER2_FONT, justify='center', background='#E7E7E8', foreground=self.TEXT_COLOR, validate='key')

        # Validacion de las entradas
        self.validate_input_func = self.root.register(self.validate_input)
                                              
        self.entry.config(highlightbackground=self.color_marco, highlightcolor=self.color_marco, highlightthickness=1,validatecommand=(self.validate_input_func, '%d', '%P', '%s', '%S', '%v', '%V', '%W'))
        self.entry_2.config(validatecommand=(self.validate_input_func, '%d', '%P', '%s', '%S', '%v', '%V', '%W'))


        # Se carga la imagen para el boton
        self.original_image = Image.open(self.COMPARE_BUTTON_PATH)
        
        #Se hace el reajuste de tamanio
        self.compare_image = self.resize_image(self.original_image,width=240,height=50)

        #Se carga la segundia imagen para el boton desactivado
        self.original_image_2 = Image.open("C:/Users/nicolas.quintero/Desktop/Development/Sostenibilidad e innovacion/Induccion/comparar_2.png")
        
        #Se hace el reajuste de tamanio
        self.compare_image_2 = self.resize_image(self.original_image_2,width=240,height=50)
        
        #Se crea el boton
        self.comparing_button = tk.Button(self.root,bd=0,highlightthickness=0, image=self.compare_image,fg="white", compound=tk.CENTER)
        
        # Configure the button's image
        self.comparing_button.image = self.compare_image 
        
        #Se pone la imagen en el boton
        self.comparing_button.config(image=self.compare_image)

        #Se crean los cositos
        self.entry_canvas = self.canvas.create_window( 130, 162,
                                       anchor = "nw",
                                       window = self.entry, width=100, height=53)
        self.entry2_canvas = self.canvas.create_window( 370, 162,
                                       anchor = "nw",
                                       window = self.entry_2, width=100, height=53)


        #Icono de casa
        self.home =self.canvas.create_image(510,30, image= self.home_icon, anchor="nw")

        #Icono de cerrar
        self.close =self.canvas.create_image(550,30,image= self.close_icon, anchor="nw")

        #Se crea la imagen del boton
        self.compare=self.canvas.create_image(182,254,image =self.compare_image, anchor ="nw")
 
        #Se le otorga las animaciones a cada boton
        self.animacion_boton(self.canvas,self.compare,self.root)

        self.animacion_boton(self.canvas,self.close,self.root)

        self.animacion_boton(self.canvas, self.home,self.root)

        #Se le da la funcion a los botones

        self.canvas.tag_bind(self.close,"<Button-1>",close_program)

         #Se le da la funcionalidad al boton de comparar
        self.canvas.tag_bind(self.compare,"<Button-1>",self.compare_numbers)


    def set_model(self, model):
        self.model = model

    def compare_numbers(self, event):
        #Validacion de entradas del usuario
        self.model.num1 = int(self.entry.get())
        self.model.num2 = int(self.entry_2.get())

        #Se le entrega al modelo la informacion
        self.controller.compare_numbers()
        
    #Metodo para actualizar la interfaz en caso de que el numero A sea mayor

    def update_result_label_A(self):

        #Se escribe la respuesta esperada

        new_text= "El numero A: " +str(self.model.num1)+ " es mayor que el numero B: "+ str(self.model.num2)
        
        #Se actualiza el item en la interfaz

        self.canvas.itemconfig(self.descripcion, text=new_text)
        
    #Metodo para actualizar la interfaz en caso de que el numero B sea mayor

    def update_result_label_B(self):
        #Se escribe la respuesta esperada

        new_text= "El numero B: " +str(self.model.num2)+ " es mayor que el numero A: "+ str(self.model.num1)

        #Se actualiza el item en la interfaz

        self.canvas.itemconfig(self.descripcion, text=new_text)
    
    def update_result_label_equal(self):
         #Se escribe la respuesta esperada

        new_text= "Los numeros A y B son iguales!"

        #Se actualiza el item en la interfaz

        self.canvas.itemconfig(self.descripcion, text=new_text)