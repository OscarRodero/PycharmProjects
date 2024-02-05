import threading
import time
import speech_recognition as sr
import pyttsx3
from FuncAux import *

def main():
    hablar("Iniciado el asistente de League of Legends.")
    hablar('Puedes comenzar a hablar')
    while True:
        try:
            mensaje = audio_a_texto()
            if mensaje is not None:
                palabras = mensaje.lower().split()
                print("Frase: "+mensaje)
                if palabras:
                    primera_palabra = palabras[0]
                    ultima_palabra = palabras[-1]
                    if primera_palabra:
                        if primera_palabra == "iniciar" and ultima_palabra == "partida":                                                   
                            jugarPartida()
                        #mi_hilo = threading.Thread(target=lanzar_cronometro(primera_palabra, ultima_palabra))
                        #mi_hilo = threading.Thread(target=lambda: lanzar_cronometro(primera_palabra, ultima_palabra))
                        #mi_hilo.start()
            else:
                print("No se pudo escuchar nada.")

        except sr.UnknownValueError:
            hablar('No pude entender lo que dijiste. Por favor, intenta de nuevo.')
        except sr.RequestError as e:
            hablar('Error en la conexión al servicio de reconocimiento de voz. Verifica tu conexión a Internet.')
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
