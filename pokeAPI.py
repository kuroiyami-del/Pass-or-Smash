import requests
import random


def pokemonesRandom():
    URL = "https://pokeapi.co/api/v2/pokemon/"
    respuesta = requests.get(URL + str(random.randint(1, 101)))
    datos = respuesta.json()

    for nombre in datos["forms"]:
        return nombre["name"]


def pokemonesOrden():
    URL = "https://pokeapi.co/api/v2/pokemon/"
    for i in range(1, 101):
        respuesta = requests.get(URL + str(i))
        datos = respuesta.json()

        for nombre in datos["forms"]:
            print(nombre["name"])
