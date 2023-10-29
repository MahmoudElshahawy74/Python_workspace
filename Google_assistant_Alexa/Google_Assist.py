# import library
import webbrowser
from time import ctime
import os
import playsound
from gtts import gTTS
import random
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()


# Reading Audio file as source
# listening the audio file and store in audio_text variable
def Bixby_Speak(audios):
    tts = gTTS(text=audios, lang='en', slow=False)
    # tts = gTTS(text=audios, lang='en')
    audioF = 'audio.mp3'
    tts.save(audioF)
    playsound.playsound(audioF)
    print(audios)
    os.remove(audioF)


def record(ask=False):
    with sr.Microphone(device_index=None) as source:
        r.adjust_for_ambient_noise(source)
        if ask:
            Bixby_Speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="en")
        except sr.UnknownValueError:
            Bixby_Speak("sorry i did not get that")
        except sr.RequestError:
            Bixby_Speak("sorry Service is Down")
        return voice_data.lower()


def Respond(voice_data):
    if 'the Name' in voice_data or 'name' in voice_data:
        Bixby_Speak('Mahmoud Elshahawy')
        # Bixby_Speak('Moatasem Big Boss')
    if 'the time' in voice_data or 'time' in voice_data:
        Bixby_Speak(ctime())
    if 'the search' in voice_data or 'search' in voice_data:
        search = record('youtube')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)

    if 'the place' in voice_data or 'place' in voice_data:
        location = record('nasr city')
        url = 'https://google.nl/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)

    if 'exit' in voice_data:
        exit()


Bixby_Speak('Hi Shahawy')
while 1:
    voice_data = record()
    Respond(voice_data)
