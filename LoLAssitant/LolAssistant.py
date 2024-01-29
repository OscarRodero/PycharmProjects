import speech_recognition as sr
import pyttsx3

def talk(msg):
    newVoiceRate = 160
    engine = pyttsx3.init()
    engine.setProperty('rate', newVoiceRate)
    engine.say(msg)
    engine.runAndWait()

def audio_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as origen:
        r.pause_threshold = 0.5  # Ajusta este valor según sea necesario
        talk('Puedes comenzar a hablar')
        try:
            audio = r.listen(origen, timeout=3)
            return r.recognize_google(audio, language='es-ES')
        except sr.WaitTimeoutError:
            talk('No se ha detectado ninguna voz. Intenta de nuevo.')

while True:
    try:
        mensaje = audio_to_text().lower()
        talk("Has dicho " + mensaje)
    except sr.UnknownValueError:
        talk('No se pudo entender lo que dijiste. Por favor, intenta de nuevo.')
    except sr.RequestError as e:
        talk('Error en la conexión al servicio de reconocimiento de voz. Verifica tu conexión a Internet.')
        print(f"Error: {e}")
