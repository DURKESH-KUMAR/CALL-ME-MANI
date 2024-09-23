import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from playsound import playsound
playsound("intro.mpeg")
# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to make Jarvis speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get the current time
def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {current_time}")

# Function to greet the user based on the time of day
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am MANI, how can I assist you?")

# Function to take voice commands from the user
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Could not understand audio, please say that again...")
        return "None"
    return query.lower()

# Main logic for handling commands
if __name__ == "__main__":
    wish_me()

    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening YouTube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening Google")

        elif 'play music' in query:
            playsound("play song.mpeg")

        elif 'time' in query:
            get_time()

        elif 'quit' in query or 'exit' in query:
            playsound("quit.mpeg")
            break
        elif 'alert me' in query:
            playsound("alert me.mpeg")

        elif 'are you a joker' in query:
            playsound("are you a joker.mpeg")

        elif 'are you feeling sad' in query:
            playsound("are you feeling sad.mpeg")

        elif 'are you hungry' in query:
            playsound("are you hungry.mpeg")
        elif 'bus will come' in query:
            playsound("bus will come.mpeg")

        elif 'do some work' in query:
            playsound("do some work.mpeg")

        elif 'give me respect' in query:
            playsound("give respect.mpeg")

        elif 'how to work' in query:
            playsound("how to work.mpeg")

        elif 'i am a good boy' in query:
            playsound("i am a good boy.mpeg")

        elif 'i am going to work' in query:
            playsound("i am going to work.mpeg")

        elif 'i am king' in query:
            playsound("i am king.mpeg")

        elif 'i hate you' in query:
            playsound("i hate you.mpeg")

        elif 'mabel' in query:
            playsound("mabel.mpeg")

        elif 'mani was worst' in query:
            playsound("mani was worst.mpeg")

        elif 'make tea' in query:
            playsound("make tea.mpeg")

        elif 'why are you telling lie' in query:
            playsound("politics.mpeg")

        elif 'shutup' in query:
            playsound("shutup.mpeg")

        elif 'tell about me' in query:
            playsound("tell about me.mpeg")

        elif 'tell about you' in query:
            playsound("tell about you.mpeg")

        elif 'tell about your history' in query:
            playsound("tell about your history.mpeg")

        elif 'what is your history' in query:
            playsound("what is your history.mpeg")

        elif 'who are you' in query:
            playsound("who are you.mpeg")

        
        elif 'call friend' in query:
            os.system("python xr.py")
        
        elif 'open official website' in query:
            webbrowser.open("https://mani-mental-health-qg2ve95.gamma.site/")
        else:
            webbrowser.open("https://mani-mental-health-qg2ve95.gamma.site/")

