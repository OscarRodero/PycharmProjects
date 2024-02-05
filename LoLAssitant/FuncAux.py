import threading
import time
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

def jugarPartida():
    FinPartida = False
    while not FinPartida:
        mi_hilo = threading.Thread(target=lambda: lanzar_cronometro(primera_palabra, ultima_palabra))
        mi_hilo.start()