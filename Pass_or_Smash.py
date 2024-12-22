import tkinter
from PIL import Image, ImageTk
from pokeAPI import cargarPokemonesRandom, mostrarPokemon,cargarPokemonesOrden

# Creacion de la ventana
ventana = tkinter.Tk()
ventana.geometry("500x400")
ventana.resizable(False, False)
ventana.title("Smash or Pass")
ventana.iconbitmap("assets/icono-pokebola.ico")

# Carga de una imagen

label_imagen = tkinter.Label(ventana)
label_imagen.pack(pady=10)

# Label para mostrar el nombre
label_nombre = tkinter.Label(ventana, font=("Arial", 16))
label_nombre.pack(pady=10)

# cargar la lista de los pokemones
pokemones = cargarPokemonesOrden(100)

index = 0


def siguientePokemon():
    global index
    index += 1
    if index >= len(pokemones):
        index = 0
    mostrarPokemon(index, pokemones, label_imagen, label_nombre)


# Botones Smash y Pass
boton_smash = tkinter.Button(ventana, text="SMASH", bg="blue", fg="white", command=siguientePokemon)
boton_smash.pack(side="left", padx=20, pady=20)

boton_pass = tkinter.Button(ventana, text="PASS", bg="red", fg="white", command=siguientePokemon)
boton_pass.pack(side="right", padx=20, pady=20)

mostrarPokemon(index, pokemones, label_imagen, label_nombre)

ventana.mainloop()
