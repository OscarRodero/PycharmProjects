import threading
import time
import speech_recognition as sr
import pyttsx3
import webbrowser

def ObtenerTiempo(palabra):    
    if palabra == "destello":
        palabra = "flash"
    elif palabra == "fantasmal":
        palabra = "ghost"
    elif palabra == "prender":
        palabra = "ignite"
    elif palabra == "extenuar":
        palabra = "exhaust"
    elif palabra == "curar":
        palabra = "heal"
    elif palabra == "barrera":
        palabra = "barrier"
    

    if palabra =="flash":
        return 300
    elif palabra == "ghost":
        return 210
    elif palabra == "ignite":
        return 180
    elif palabra == "exhaust":
        return 210
    elif palabra == "heal":
        return 240
    elif palabra == "barrier":
        return 180
    else:
        return 0
    
def audio_a_texto():
    r = sr.Recognizer()
    with sr.Microphone() as origen:
        r.pause_threshold = 0.5
        try:
            audio = r.listen(origen, timeout=3)
            return r.recognize_google(audio, language='es-ES')
        except sr.WaitTimeoutError:
            print("Esperando...")

def hablar(msg):
    newVoiceRate = 160
    engine = pyttsx3.init()
    engine.setProperty('rate', newVoiceRate)
    engine.say(msg)
    engine.runAndWait()

def ConvertirPalabras(pal):
    palabra = pal.lower()
    palabras_similares_a_top = ["hop", "pop", "cop", "chop", "shop","superior"]
    palabras_similares_a_mid = ["meet", "meat", "me", "medio"]
    palabras_similares_a_jungle = ["jangle", "jangl", "jungle", "jungla"]
    palabras_similares_a_adc = ["ad carry", "adcarry", "adc", "tirador", "carry"]
    palabras_similares_a_support = ["supp", "sup", "support", "apoyo"]
    
    if palabra in palabras_similares_a_top:
        return "top"    
    elif palabra in palabras_similares_a_mid:
        return "mid"
    elif palabra in palabras_similares_a_jungle:
        return "jungle"
    elif palabra in palabras_similares_a_adc:
        return "adc"
    elif palabra in palabras_similares_a_support:
        return "support"
    else:
        return palabra
    
def lanzar_cronometro(primera_palabra, ultima_palabra):
    hablar("Lanzando un cronómetro para el "+ultima_palabra+" del "+primera_palabra)
    if primera_palabra in ["top", "mid", "jungla", "adc", "supp"]:
        tiempo_cronometro = ObtenerTiempo(ultima_palabra)
        if tiempo_cronometro > 0:
            print(f"Durmiendo por {tiempo_cronometro} minutos...")
            time.sleep(tiempo_cronometro)
            print("Despertando del sueño")
    
def lanzar_dragon_nashor(mounstruo):
    if mounstruo == "dragón":
        tiempo_cronometro = 300
    else:
        tiempo_cronometro = 1200
    hablar(f"Lanzando un cronómetro para el {mounstruo}")
    print(f"Durmiendo por {tiempo_cronometro} minutos...")
    time.sleep(tiempo_cronometro)
    print("Despertando del sueño")
    hablar(f"El {mounstruo} ha renacido")

def asesinado_dragon_nashor(mounstruo):
    hablar(f"El {mounstruo} ha sido asesinado")
    print(f"El {mounstruo} ha sido asesinado")
    # Tiempo de respawn del mounstruo menos 20 segundos para avisar con tiempo suficiente
    if mounstruo == "dragón":
        tiempo = 280
    else:
        tiempo = 340
    time.sleep(tiempo)
    
    
def jugarPartida():   
    FinPartida = False
    dragon_thread = threading.Thread(target=lambda: lanzar_dragon_nashor("dragón"))
    nashor_thread = threading.Thread(target=lambda: lanzar_dragon_nashor("nashor"))

    dragon_thread.start()
    nashor_thread.start()
    while not FinPartida:
        try:
            mensaje = audio_a_texto()
            if mensaje is not None:
                palabras = mensaje.lower().split()
                print("Frase: "+mensaje)
                if palabras:
                    primera_palabra = palabras[0]
                    ultima_palabra = palabras[-1]
                    primera_palabra = ConvertirPalabras(primera_palabra)
                    if primera_palabra in ["top", "mid", "jungle", "adc", "supp"]:
                        mi_hilo = threading.Thread(target=lambda: lanzar_cronometro(primera_palabra, ultima_palabra))
                        mi_hilo.start()
                    elif primera_palabra == "asesinado":
                        if ultima_palabra == "dragón":
                            mi_hilo = threading.Thread(target=lambda: asesinado_dragon_nashor("dragón"))
                            mi_hilo.start()
                        elif ultima_palabra == "nashor":
                            mi_hilo = threading.Thread(target=lambda: asesinado_dragon_nashor("nashor"))
                            mi_hilo.start()
                    elif primera_palabra == "buscar":
                        if len(palabras) >= 3:
                            segunda_palabra = palabras[1]
                            tercera_palabra = palabras[-1]
                            hablar("Buscando jugador...")
                            webbrowser.open(f'https://www.op.gg/summoners/euw/{segunda_palabra}-{tercera_palabra}')
                            print("Buscando jugador...")
                        else:
                            print("No hay suficientes palabras para buscar. Necesitas al menos tres palabras.")
                    elif primera_palabra == "finalizar":
                        FinPartida = True
                        hablar("Partida Finalizada.")
                        print("Partida Finalizada.")
                        break;
                
                
        except sr.UnknownValueError:
            print('No pude entender lo que dijiste. Por favor, intenta de nuevo.')
            #hablar('No pude entender lo que dijiste. Por favor, intenta de nuevo.')
        except sr.RequestError as e:
            hablar('Error en la conexión al servicio de reconocimiento de voz. Verifica tu conexión a Internet.')
            print(f"Error: {e}")