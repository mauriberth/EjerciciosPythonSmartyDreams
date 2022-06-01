print("Programa DevOps SmartyDreams 2022");
print("@author López Vera Mauricio Alberto");
#Asistente de voz.

#Importaciones de librerías para el proyecto.
import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Opciones de la voz o idioma del asistente.
vi1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
vi2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
vi3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
vi4 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'

#Activar micrófono conectado y devolver lo escuchado como un texto.
def audioToText():
    r = sr.Recognizer()
    with sr.Microphone() as origen:
        r.pause_threshold = 0.8
        print("Adelante, te escucho:")
        audio = r.listen(origen)
        try:
            request = r.recognize_google(audio, language="es-ar")
            print("Escuché lo siguiente: " + request)
            return request
        except sr.UnknownValueError:
            print("Disculpa, no te he entendido.")
            return "Esperando instrucción."
        except sr.RequestError:
            print("Lamento las molestias. En este momento estoy teniendo problemas para conectarme.")
            return "Esperando instrucción."
        except:
            print("¡Uy!, algo ha salido mal.")
            return "Esperando instrucción."


#Escuchar asistente
def talk(mensaje):
    engine = pyttsx3.init()
    engine.setProperty('voice', vi3)
    engine.say(mensaje)
    engine.runAndWait()


#Para obtener la fecha del día.
def getDay():
    dia = datetime.date.today()
    print(dia)
    dayWeek = dia.weekday()
    print(dayWeek)
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}
    talk(f'Hoy es {calendario[dayWeek]}')


#Para obtener la hora
def requestHour():
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)
    talk(hora)

# Saludo inicial.
def saludoInit():
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        thisMoment = 'Que tengas buena noche.'
    elif 6 <= hora.hour < 13:
        thisMoment = 'Hola, buenos días.'
    else:
        thisMoment = 'Hola, buena tarde.'

    # decir el saludo
    talk(f'{thisMoment}, soy AlexaDreams, y estoy aquí para ayudarte. Dime, ¿qué haremos hoy?')
#Función central.
def requestThings():
    saludoInit()
    comenzar = True
    while comenzar:
        request = audioToText().lower()
        if 'abrir youtube' in request:
            talk('Abriendo Youtube. Un momento.')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in request:
            talk('Abriendo el navegador. Un momento.')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in request:
            getDay()
            continue
        elif 'qué hora es' in request:
            requestHour()
            continue
        elif 'busca en wikipedia' in request:
            talk('Abriendo Wikipedia. Un momento.')
            request = request.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            res = wikipedia.summary(request, sentences=1)
            talk('De acuerdo con datos de Wikipedia:')
            talk(res)
            continue
        elif 'busca en internet' in request:
            talk('Abriendo Internet. Un momento.')
            request = request.replace('busca en internet', '')
            pywhatkit.search(request)
            talk('De acuerdo con algo que encontré en la web:')
            continue
        elif 'reproducir' in request:
            talk('Reproduciendo.')
            pywhatkit.playonyt(request)
            continue
        elif 'broma' in request:
            talk(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in request:
            accion = request.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                actionFind = cartera[accion]
                actionFind = yf.Ticker(actionFind)
                priceActual = actionFind.info['regularMarketPrice']
                talk(f'La encontré, el precio de {accion} es {priceActual}')
                continue
            except:
                talk("No he encontrado ese artículo en venta. ")
                continue
        elif 'adiós' in request:
            talk("Voy a dormir. Sin embargo, soy un asistente. Estaré soñando con servidores WAN un ratito, me avisas cualquier cosa.")
            break
requestThings()