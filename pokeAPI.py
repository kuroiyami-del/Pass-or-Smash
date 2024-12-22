import requests
import random


def cargarPokemonesRandom(cantidad=10):
    lista_pokemones = []

    URL = "https://pokeapi.co/api/v2/pokemon/"

    for i in range(cantidad):
        id_random = random.randint(1, 151)

        respuesta = requests.get(URL + str(id_random))
        datos = respuesta.json()

        nombre = datos["forms"][0]["name"]
        imagen_url = datos["sprites"]["other"]["official-artwork"]["front_default"]

        lista_pokemones.append({"nombre": nombre, "imagen": imagen_url})

    return lista_pokemones


def cargarPokemonesOrden(cantidad=10):
    lista_pokemones = []

    URL = "https://pokeapi.co/api/v2/pokemon/"

    for i in range(cantidad):
        id_ramdon = random.randint(1, 151)
        respuesta = requests.get(URL + str(id_ramdon))
        datos = respuesta.json()

        nombres = datos["forms"]["name"]
        imagen_url = datos["sprites"]["other"]["official-artwork"]["front_default"]

        lista_pokemones.append({"nombre": nombres, "imagen": imagen_url})

    return lista_pokemones
