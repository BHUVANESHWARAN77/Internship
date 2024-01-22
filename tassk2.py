
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("I am your virtual assistant. How can I help you today?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User: {query}\n")
    except Exception as e:
        print(e)
        return None
    return query.lower()

if __name__ == "__main__":
    wish_me()

    while True:
        query = take_command()

        if query:
            # Task 1: Wikipedia search
            if 'wikipedia' in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia...")
                speak(result)

            # Task 2: Open a website
            elif 'open website' in query:
                speak("Opening website...")
                webbrowser.open("https://www.example.com")

            # Task 3: Check the time
            elif 'time' in query:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The current time is {current_time}")

            # Task 4: Exit the program
            elif 'exit' in query or 'quit' in query:
                speak("Goodbye!")
                exit()

            else:
                speak("I'm sorry, I didn't understand that. Can you please repeat?")

# Note: This is a simple example, and you can extend it by adding more functionalities based on your requirements.
