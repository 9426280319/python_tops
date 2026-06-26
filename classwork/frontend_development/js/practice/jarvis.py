import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init()

def speak(text):
print(text)
engine.say(text)
engine.runAndWait()

def wish():
hour = datetime.datetime.now().hour

```
if hour < 12:
    speak("Good Morning Sir")
elif hour < 18:
    speak("Good Afternoon Sir")
else:
    speak("Good Evening Sir")

speak("I am Jarvis. How can I help you?")
```

def take_command():
r = sr.Recognizer()

```
with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)

try:
    print("Recognizing...")
    command = r.recognize_google(audio, language="en-in")
    print("You Said:", command)
    return command.lower()

except:
    return ""
```

wish()

while True:

```
query = take_command()

if not query:
    continue

if "wikipedia" in query:
    try:
        topic = query.replace("wikipedia", "").strip()

        if topic:
            result = wikipedia.summary(topic, sentences=2)
            speak(result)
        else:
            speak("Please tell a topic")
    except Exception as e:
        speak("Wikipedia search failed")

elif "open youtube" in query:
    webbrowser.open("https://youtube.com")

elif "open google" in query:
    webbrowser.open("https://google.com")

elif "open stackoverflow" in query:
    webbrowser.open("https://stackoverflow.com")

elif "open chatgpt" in query:
    webbrowser.open("https://chatgpt.com")

elif "time" in query:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(current_time)

elif "open notepad" in query:
    os.system("notepad")

elif "open code" in query:
    os.system("code")

elif "play music" in query:
    music_folder = r"D:\Music"

    if os.path.exists(music_folder):
        songs = os.listdir(music_folder)

        if songs:
            os.startfile(os.path.join(music_folder, songs[0]))
        else:
            speak("No songs found")
    else:
        speak("Music folder not found")

elif "exit" in query or "stop" in query:
    speak("Goodbye Sir")
    break

else:
    speak("Command not found")
```
