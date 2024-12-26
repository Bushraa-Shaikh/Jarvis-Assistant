import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import sys

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=5)

        try:
            
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query.lower()
        except:
            speak("Sorry, I didn't catch that. Please try again")
            return None
    
def tell_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {time}")

def search_wikipedia(query):
    query = query.replace("wikipedia", "")
    result = wikipedia.summary(query, sentences=1)
    speak(result)

def close_program():
    speak("Goodbye!")
    sys.exit()

def main():
    speak("Hello, I am Jarvis.How can I assist you today")

    while True:
        query = listen()

        if query is None:
            continue

        if 'time' in query:
            tell_time()

        elif 'wikipedia' in query:
            search_wikipedia(query)

        elif 'quit' in query or 'exit' in query:
            close_program()

        else:
            speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    main()