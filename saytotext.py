"""
pip install pyaudio
pip install SpeechRecognition
Tested on Python 2.7.11
Email: khanhnnvn@gmail.com
"""
import speech_recognition
speech_identifier = speech_recognition.Recognizer()

def phrase():

    with speech_recognition.Microphone(device_index=1) as source:
            speech_identifier.adjust_for_ambient_noise(source)
            audio = speech_identifier.listen(source)
    
    try:
            return speech_identifier.recognize_google(audio , language = 'vi-VN')
    except :
            print("I am listen you say...)
    
    return " "
while 1:
    str=phrase()
    print (str)
