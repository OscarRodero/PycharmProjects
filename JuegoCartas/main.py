from random import random


def generarBaraja():
    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    baraja = [{'valor': valor, 'palo': palo} for valor in valores for palo in palos]
    random.shuffle(baraja)
    return baraja


def calcularPuntos(cartas):

    pass

def juegaJugador(cartasJugador):
    print("Tienes "+calcularPuntos(cartasJugador)+ "puntos")
    eleccion = input(print("¿Quieres otra 'carta' o prefieres 'plantarte'?"))
    if eleccion== "carta":
        pass
def juegaDealer():
    pass


def jugar():
    print("¡Bienvenido al BlackYack!")
    mi_baraja = generarBaraja()
    cartasJugador = []
    cartasDealer = []
    Continuar = True
    while Continuar:
        juegaJugador(cartasJugador)
        juegaDealer()


jugar()


