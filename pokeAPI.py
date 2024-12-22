import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import random


# Funcion para tener pokemones random
def cargarPokemonesRandom(cantidad=10):
    pokelista = []

    URL = "https://pokeapi.co/api/v2/pokemon/"

    for i in range(cantidad):
        id_random = random.randint(1, 151)

        respuesta = requests.get(URL + str(id_random))
        datos = respuesta.json()

        nombre = datos["forms"][0]["name"]
        imagen_url = datos["sprites"]["other"]["official-artwork"]["front_default"]

        pokelista.append({"nombre": nombre, "imagen": imagen_url})

        pokelista_limpia = []
        visto = set()

        for diccionario in pokelista:
            tupla_dicc = tuple(diccionario.items())

            if tupla_dicc not in visto:
                pokelista_limpia.append(diccionario)
                visto.add(tupla_dicc)

    return pokelista_limpia


def mostrarPokemon(index, pokemones, label_imagen, label_nombre):
    """Muestra el Pokémon actual en la interfaz."""
    # Obtiene el Pokémon actual de la lista usando el índice
    pokemon = pokemones[index]

    # Descarga la imagen del Pokémon desde la URL
    response = requests.get(pokemon["imagen"])
    imagen = Image.open(BytesIO(response.content))
    imagen = imagen.resize((200, 200))  # Ajusta el tamaño de la imagen
    pokemon_imagen = ImageTk.PhotoImage(imagen)

    # Actualiza el Label con la nueva imagen
    label_imagen.config(image=pokemon_imagen)
    label_imagen.image = pokemon_imagen  # Importante para evitar que la imagen sea recolectada por el garbage collector

    # Actualiza el Label con el nombre del Pokémon
    label_nombre.config(text=pokemon["nombre"].capitalize())


def cargarPokemonesOrden(cantidad=100):
    pokelista = []

    URL = "https://pokeapi.co/api/v2/pokemon/"

    for i in range(cantidad):
        id_ramdon = random.randint(1, 151)
        respuesta = requests.get(URL + str(id_ramdon))
        datos = respuesta.json()

        nombres = datos["forms"][0]["name"]
        imagen_url = datos["sprites"]["other"]["official-artwork"]["front_default"]

        pokelista.append({"nombre": nombres, "imagen": imagen_url})

        pokelista_limpia = []
        visto = set()

        for diccionario in pokelista:
            tupla_dicc = tuple(diccionario.items())

            if tupla_dicc not in visto:
                pokelista_limpia.append(diccionario)
                visto.add(tupla_dicc)

    return pokelista_limpia



