import random


def generarBaraja():
    palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]
    rangos = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    baraja = []

    for palo in palos:
        for rango in rangos:
            carta = (palo, rango)
            baraja.append(carta)
    random.shuffle(baraja)
    return baraja
def valorCarta(carta):
    rango = carta[1]
    if rango.isdigit():
        return int(rango)
    elif rango == "A":
        return 1
    elif rango == "J":
        return 11
    elif rango == "Q":
        return 12
    elif rango == "K":
        return 13

def calcularPuntos(cartas):
    puntos = 0
    for carta in cartas:
        puntos += valorCarta(carta)
    return puntos

def juegaJugador(cartasJugador, baraja):
    plantarse = True
    while plantarse:
        print("Tienes "+str(calcularPuntos(cartasJugador))+ "puntos")
        eleccion = input("¿Quieres otra 'carta' o prefieres 'plantarte'?")
        if eleccion == "carta":
            cartasJugador.append(baraja.pop(0))
        if eleccion == "plantarme":
            plantarse = False
        if calcularPuntos(cartasJugador)>21 or plantarse==False:
            print("Te plantaste con "+str(calcularPuntos(cartasJugador)))
            plantarse=False
def juegaDealer(cartasDealer, cartasJugador, baraja):
    while calcularPuntos(cartasDealer)<16 or calcularPuntos(cartasDealer)<calcularPuntos(cartasJugador) and calcularPuntos(cartasDealer)<21:
        cartasDealer.append(baraja.pop(0))

def jugar():
    print("¡Bienvenido al BlackYack!")
    Continuar = True
    while Continuar:
        mi_baraja = generarBaraja()
        cartasJugador = []
        cartasDealer = []
        juegaJugador(cartasJugador, mi_baraja)
        juegaDealer(cartasDealer, cartasJugador, mi_baraja)
        if calcularPuntos(cartasJugador) > 21:
            print("Has perdido, te pasaste de 21 puntos.")
        elif calcularPuntos(cartasDealer) > 21:
            print("La banca se pasó de 21 puntos. ¡Has ganado!")
        elif calcularPuntos(cartasJugador) > calcularPuntos(cartasDealer):
            print("Has ganado, tienes más puntos que la banca.")
        elif calcularPuntos(cartasJugador) < calcularPuntos(cartasDealer):
            print("La banca gana, tiene más puntos que tú.")
        else:
            print("Empate, ambos tienen la misma cantidad de puntos.")

        if input("¿Quieres seguir jugando?(S/N)").lower()!="s":
            Continuar=False

jugar()


