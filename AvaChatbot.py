import datetime
import json
import smtplib
import time
import webbrowser
from urllib.request import urlopen

import nltk
import psutil
import pyautogui
import requests
import speech_recognition as sr
import wolframalpha
from nltk.tokenize import word_tokenize
from wikipedia import wikipedia

from tts_utils import speak, listen

nltk.download('punkt')

with open('rules.json', 'r') as rules_file:
    rules = json.load(rules_file)


def retrieval_based_response(query):
    if query in rules:
        return rules[query]
    else:
        return None

def battery():
    battery_info = psutil.sensors_battery()
    if battery_info is not None:
        battery_percent = battery_info.percent
        return f"The battery is at {battery_percent}%"
    else:
        return "Battery information is not available."

def calc(query):
    try:
        client = wolframalpha.Client("U4A7V8-RK47GHT9L9")
        res = client.query(query)
        answer = next(res.results).text
        speak("The answer is " + answer)
    except Exception:
        speak("Sorry, I cant find an answer for that question")


def sendEmail(to, content):
    server = smtplib.SMTP('smpt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("your email id", "your email password")
    server.sendmail("your mail id", to, content)
    server.close()

    if "send a email" in user_input:
        try:
            speak("What should i say")
            content = user_input()
            speak("Whom should i send it to")
            to = user_input()
            sendEmail(to, content)
        except Exception as e:
            print(e)
            speak("I am not able to send this email")

def countdown_timer(x):
    while x >= 0:
        if x == 0:
            print("time is up")
            speak("time is up")
            break
        print(x)
        x -= 1
        time.sleep(1)

def google_search():
    speak("What should I search for?")
    search_query = user_input()
    url = f"https://www.google.com/search?q={search_query}"
    webbrowser.open(url)
    speak("Here are the results " + search_query)

def weather():
    api_key = "2107eb86cf98a0f11bc1e189774d9cd2"
    base_url = "https://api.openweathermap.org/data/2.5/weather?lat=40.659205&lon=-73.890690&appid=0023c10b6c1582cb4741a42787b3a2cd"
    city_name = "Brooklyn"
    complete_url = base_url + "appid = " + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main_data = data["main"]
        current_temperature = main_data["temp"]
        current_pressure = main_data["pressure"]
        current_humidity = main_data["humidity"]
        weather_data = data["weather"]
        weather_description = weather_data[0]["description"]
        print("Temperature (in Kelvin): " + str(current_temperature))
        print("Atmospheric pressure (in hPa): " + str(current_pressure))
        print("Humidity (in percentage): " + str(current_humidity))
        print("Description: " + str(weather_description))
    else:
        speak("City not found")

def get_news():
    try:
        api_key = "9818049735a542b5b783aef100db3d97"
        url = f"https://newsapi.org/v2/top-headlines?country=us&category=general&q=new%20york&apiKey={api_key}"
        jsonObj = urlopen(url)
        data = json.load(jsonObj)
        i = 1

        print("=============== NEW YORK NEWS ===============")
        speak("Here are some of the top headlines")

        for item in data['articles'][:2]:
            print(str(i) + '.' + item['title'] + '\n')
            speak(item['title'])
            speak("Next news")
            i += 1
    except Exception as e:
        print(str(e))


def tell_me_about(term):
    try:
        speak("Searching Wikipedia...")
        term = term.replace("wikipedia", "")
        results = wikipedia.summary(term, sentences=3)
        speak("According to wikipedia")
        print(results)
        speak(results)
    except Exception as e:
        speak("Sorry, I couldn't find any information about " + term)


def reminder():
    remindtime = user_input()
    speak("What should I remind you about?")
    remindtext = user_input()
    remindfile = open("remindfile.txt", "a")
    remindfile.write(remindtime + " " + remindtext + "\n")
    remindfile.close()
    speak("Reminder saved")

while True:

    user_input = listen()
    if user_input.lower() == "exit":
        print("GoodBye")
        break

    print("You: ", user_input)
    response = retrieval_based_response(user_input)
    if response:
        print("Ava: ", response)
        speak(response)

    elif "take a screenshot" in user_input:
        try:
            screenshot = pyautogui.screenshot()

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
            screenshot_filename = f"screenshot_{timestamp}.png"
            screenshot.save(screenshot_filename)

            speak(f"Screenshot taken and saved as '{screenshot_filename}'")
        except Exception as e:
            speak("Sorry, there was an error while taking the screenshot.")

    elif "calculate" in user_input:
        speak("What do you want me to calculate?")
        calc_input = user_input()  # Listen for the calculation query
        calc(calc_input)

    elif "send an email" in user_input:
        try:
            speak("What should I say?")
            content = user_input()  # Listen for the email content
            speak("Whom should I send it to?")
            to = user_input()  # Listen for the email recipient
            sendEmail(to, content)
        except Exception as e:
            print(e)
            speak("I am not able to send this email")

    elif "make a reminder" in user_input:
        speak("When should I remind you? (Provide a specific time)")
        remind_time = user_input()  # Listen for the reminder time
        speak("What should I remind you about?")
        remind_text = user_input()  # Listen for the reminder text

        # Save the reminder to a file or perform your desired action
        # For now, let's just print the reminder information
        print(f"Reminder set for {remind_time}: {remind_text}")
        speak("Reminder set successfully")
    elif "ava" in user_input.lower():
        speak("How can i assist you")

    elif "battery percent" in user_input:
        battery_status = battery()
        print("Ava: ", battery_status)
        speak(battery_status)

    elif "never mind" in user_input:
        speak("Ok")
    else:
        speak("I didn't understand")