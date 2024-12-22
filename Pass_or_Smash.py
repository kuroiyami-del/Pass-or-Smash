import tkinter
from PIL import Image, ImageTk

# Creacion de la ventana
ventana = tkinter.Tk()
ventana.geometry("500x400")
ventana.resizable(False, False)
ventana.title("Smash or Pass")
ventana.iconbitmap("assets/icono-pokebola.ico")

# Carga de una imagen

imagen = Image.open("assets/rayquaza.png")
imagen = imagen.resize((200, 200))
imagen_tk = ImageTk.PhotoImage(imagen)

# Crear y mostrar el label con imagen
label_imagen = tkinter.Label(ventana, image=imagen_tk)
label_imagen.pack()

# Creacion de los botones y colocacion
botonSmash = tkinter.Button(ventana, text="SMASH", width=10, height=5, bg="blue")
botonPass = tkinter.Button(ventana, text="PASS", width=10, height=5, bg="red")

botonSmash.place(x=100, y=250)
botonPass.place(x=313, y=250)

ventana.mainloop()
