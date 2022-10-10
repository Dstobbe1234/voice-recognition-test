import speech_recognition
from gtts import gTTS

import os

recognizer = speech_recognition.Recognizer()
print("HI")
while True:

    try:

        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(
                mic)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(f"recognized: {text}")
            if text == "hey computer":
                response = "hello david."
                audioFile = gTTS(text=response, lang='en',
                                 slow=False, tld="co.uk")
                audioFile.save("hello.mp3")
                os.system("mpg321 hello.mp3")

    except speech_recognition.UnknownValueError:
        print("unknown value")
        recognizer = speech_recognition.Recognizer()
        continue
