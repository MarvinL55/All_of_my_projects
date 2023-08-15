from gtts import gTTS
import os
import speech_recognition as sr
from playsound import playsound

recognizer = sr.Recognizer()

# Function to convert text to speech and play the generated audio
def speak(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    playsound("response.mp3")  # Use playsound to play the MP3 file

def listen():
    try:
        with sr.Microphone() as source:
            print("You: ")
            recognizer = sr.Recognizer()  # Create a new recognizer instance
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)
            user_input = recognizer.recognize_google(audio).lower()
            return user_input
    except sr.WaitTimeoutError:
        return "AI Assistant: No speech detected. Please try again."
    except sr.UnknownValueError:
        return "AI Assistant: Sorry, I couldn't understand that. Please try again."


# Rest of the code remains the same...
