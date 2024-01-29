import threading
from datetime import time
import speech_recognition as sr
import pyttsx3

def ObtenerTiempo(palabra):
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

def lanzar_cronometro(primera_palabra, ultima_palabra):
    print("Primera palabra:", primera_palabra)
    print("Última palabra:", ultima_palabra)
    talk("Lanzando un cronómetro para el "+ultima_palabra+" del "+primera_palabra)
    if primera_palabra in ["top", "mid", "jungla", "adc", "supp"]:
        tiempo_cronometro = ObtenerTiempo(ultima_palabra)
        if tiempo_cronometro > 0:
            print(f"Durmiendo por {tiempo_cronometro} minutos...")
            time.sleep(tiempo_cronometro)
            print("Despertando del sueño")
def talk(msg):
    newVoiceRate = 160
    engine = pyttsx3.init()
    engine.setProperty('rate', newVoiceRate)
    engine.say(msg)
    engine.runAndWait()

def audio_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as origen:
        r.pause_threshold = 0.5
        try:
            audio = r.listen(origen, timeout=3)
            return r.recognize_google(audio, language='es-ES')
        except sr.WaitTimeoutError:
            talk('No se ha detectado ninguna voz. Intenta de nuevo.')

talk("Iniciado el asistente de League of Legends.")
talk('Puedes comenzar a hablar')
while True:
    try:
        mensaje = audio_to_text().lower()
        palabras = mensaje.split()
        print("Frase: "+mensaje)
        if palabras:
            primera_palabra = palabras[0]
            ultima_palabra = palabras[-1]
            if primera_palabra:
                mi_hilo = threading.Thread(target=lanzar_cronometro(primera_palabra, ultima_palabra))


    except sr.UnknownValueError:
        talk('No se pudo entender lo que dijiste. Por favor, intenta de nuevo.')
    except sr.RequestError as e:
        talk('Error en la conexión al servicio de reconocimiento de voz. Verifica tu conexión a Internet.')
        print(f"Error: {e}")
