import random
jugar = True
while(jugar):
    print("Vamos, intenta adivinar en qué numero estoy pensando (máx 50 mín 1)")
    numero= random.randrange(1,50)
    while(jugar):
        respuesta = int(input("Dime un número"))
        if(respuesta>numero):
            print("El número es demasiado grande")
        elif(respuesta<numero):
            print("El número es demasiado pequeño")