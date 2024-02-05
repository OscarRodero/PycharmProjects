import threading
import time
import speech_recognition as sr
import pyttsx3
from FuncAux import *
import webbrowser, os, subprocess
ruta_lol = "C:\\Riot Games\\League of Legends\\LeagueClient.exe"
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
                            hablar("Iniciando partida...")
                            try:
                                os.chdir(os.path.dirname(ruta_lol))
                                subprocess.run([ruta_lol])
                            except FileNotFoundError:
                                print("No se pudo encontrar el ejecutable de League of Legends. Verifica la ruta.")
                            except Exception as e:
                                print(f"Error al intentar iniciar League of Legends: {e}")                                       
                            jugarPartida()
                        elif primera_palabra == "buscar":
                            if len(palabras) >= 3:
                                segunda_palabra = palabras[1]
                                tercera_palabra = palabras[-1]
                                hablar("Buscando jugador...")
                                webbrowser.open(f'https://www.op.gg/summoners/euw/{segunda_palabra}-{tercera_palabra}')
                                print("Buscando jugador...")
                            else:
                                print("Necesitas especificar el nombre de invocador.")
                        elif primera_palabra == "salir":
                            hablar("Saliendo del asistente, hasta luego.")
                            print("Saliendo del asistente, hasta luego.")
                            break;
            else:
                print("No se pudo escuchar nada.")

        except sr.UnknownValueError:
            hablar('No pude entender lo que dijiste. Por favor, intenta de nuevo.')
        except sr.RequestError as e:
            hablar('Error en la conexión al servicio de reconocimiento de voz. Verifica tu conexión a Internet.')
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
