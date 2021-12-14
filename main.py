import speech_recognition as sr
import pyaudio, gtts, os
from playsound import playsound
from datetime import datetime


r = sr.Recognizer()
def get_audio():
    with sr.Microphone() as source:
        print("say something!")
        audio = r.listen(source)
    return audio
"""This function gets an audio from the microphone with the use of packages like speech+recognizer
return type: audio"""

def speech_to_text(audio):
    text = ""
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Sorry you audio could not be recognized")
    except sr.RequestError:
        print("Could not get the request from the API")
    return text
    """Converts audio to text with return type as a text file"""


def play_sound(text):
    try:
        tts = gtts.gTTS(text)
        temfile = "./mp3"
        tts.save(temfile)
        playsound(temfile)
        os.remove(temfile)
    except AssertionError:
        print("Could not play the sound")
        """Plays the audio from a text file with return type sound"""


ACTIVATION = "hey Jane!"
while True:
    a = get_audio()
    note = speech_to_text(a)
    if ACTIVATION in note.lower():
        new_note = get_audio()
        new_note = speech_to_text(new_note)
        
        if note:
            play_sound(note)

            note = datetime.now().astimezone().isoformat()

    

