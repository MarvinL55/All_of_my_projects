import speech_recognition as sr
import pyttsx3
import yaml
from botocore.response import get_response
from rasa.core.agent import Agent

recognizer = sr.Recognizer()

pyttsx3.init('sapi5')
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

model_path = 'C:\\Users\\marvi\\PycharmProjects\\pythonProject1\\my_model.tar.gz'
agent = Agent.load(model_path)

def handle_user_input(interactions):
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        print("User: ", user_input)
        engine.runAndWait()

        response = get_response(user_input, interactions)

        print("Bot: ", interactions)
        engine.say(response)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand")

def get_rasa_response(user_input):
    # Rasa agent
    rasa_output = agent.handle_message(user_input)

    # Extract intent and entities from Rasa output
    intent = rasa_output[0]['intent']['name']
    entities = rasa_output[0]['entities']

    if intent == 'hi':
        return "Hello"
    elif intent == 'bye':
        return 'Goodbye'
    elif intent == 'weather':
        location = entities[0]['value'] if entities else 'your location'
        return f"The weather in {location} is sunny today"

    return "I'm sorry, I didn't understand"

while True:
    handle_user_input()
