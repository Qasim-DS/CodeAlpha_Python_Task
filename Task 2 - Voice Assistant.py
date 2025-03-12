import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime
import os
import json
import random
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()


# Load or initialize user preferences
def load_preferences():
    try:
        with open('preferences.json', 'r') as file:
            preferences = json.load(file)
    except FileNotFoundError:
        preferences = {}
    return preferences


def save_preferences(preferences):
    with open('preferences.json', 'w') as file:
        json.dump(preferences, file)


preferences = load_preferences()


# Speak a message
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Listen for a command
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            command = None
        except sr.RequestError:
            print("Sorry, I couldn't connect to the service.")
            command = None
    return command


# Function to greet the user
def greet_user():
    if 'name' in preferences:
        name = preferences['name']
        speak(f"Hello {name}, how can I assist you today?")
    else:
        speak("Hello! What's your name?")
        name = listen()
        if name:
            preferences['name'] = name
            save_preferences(preferences)
            speak(f"Nice to meet you, {name}! How can I assist you today?")


# Function to tell the current time
def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")


# Function to tell the date
def tell_date():
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}")


# Function to play a song
def play_music():
    speak("What song would you like me to play?")
    song = listen()
    if song:
        kit.playonyt(song)
        speak(f"Playing {song} for you.")


# Function to search on Google
def search_google():
    speak("What would you like to search for?")
    query = listen()
    if query:
        kit.search(query)
        speak(f"Here are the results for {query}")


# Custom command for telling a joke
def tell_joke():
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my computer I needed a break, now it won’t stop sending me Kit-Kats."
    ]
    joke = random.choice(jokes)
    speak(joke)


# Function to open a website
def open_website():
    speak("Which website would you like to open?")
    website = listen()
    if website:
        url = f"http://{website}.com"
        webbrowser.open(url)
        speak(f"Opening {website} for you.")


# Process commands
def process_command(command):
    command = command.lower()

    if 'hello' in command or 'hi' in command:
        greet_user()

    elif 'time' in command:
        tell_time()

    elif 'date' in command:
        tell_date()

    elif 'play music' in command:
        play_music()

    elif 'search' in command:
        search_google()

    elif 'joke' in command:
        tell_joke()

    elif 'open website' in command:
        open_website()

    elif 'exit' in command:
        speak("Goodbye! Have a great day.")
        exit()

    else:
        speak("Sorry, I didn't understand that. Please try again.")


# Main function to start the assistant
def main():
    speak("Hello, I am your custom assistant. How can I help you today?")
    while True:
        command = listen()
        if command:
            process_command(command)


if __name__ == "__main__":
    main()
