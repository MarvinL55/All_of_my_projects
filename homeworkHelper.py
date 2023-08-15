from random import random

import nltk
from nltk.tokenize import word_tokenize
import requests
from bs4 import BeautifulSoup
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, download
from transformers import pipeline

download('averaged_perceptron_tagger')
download('wordnet')

def solve_math_equation(equation):
    try:
        result = eval(equation)
        return result

    except:
        return "Sorry, I couldn't solve that equation."

def lookup_topic(topic):
    # format the query to search
    query = topic.replace(' ', '+')

    # make a GET request to the Google search results page
    url = f'https://www.google.com/search?q={query}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)

    # parse the HTML of the response using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # find the first search result link and return the text of the anchor tag
    try:
        result = soup.find('div', class_='r').find('a').text
        return result
    except:
        return "Sorry, I couldn't find any information on that topic."


def check_spelling_and_grammar(text):
    # Tokenize the text
    tokens = word_tokenize(text)

    # Get the part-of-speech tags for each token
    pos_tags = pos_tag(tokens)

    # Lemmatize the tokens using their part-of-speech tags
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word, pos in pos_tags:
        # Convert the part-of-speech tag to a format that WordNet understands
        if pos.startswith('J'):
            pos = wordnet.ADJ
        elif pos.startswith('V'):
            pos = wordnet.VERB
        elif pos.startswith('N'):
            pos = wordnet.NOUN
        elif pos.startswith('R'):
            pos = wordnet.ADV
        else:
            pos = wordnet.NOUN  # default to NOUN if unknown POS tag

        # Lemmatize the word using its POS tag
        lemma = lemmatizer.lemmatize(word, pos=pos)
        lemmas.append(lemma)

    # Reconstruct the text with the lemmatized words
    text = ' '.join(lemmas)

    # TODO: code to check spelling and grammar goes here

    return text



def analyze_user_input(input_text):
    # use NLTK to tokenize the user's input
    tokens = word_tokenize(input_text)

    # identify keywords in the user's input and determine what type of help they need
    if 'math' in tokens:
        return 'math'
    elif 'topic' in tokens:
        return 'topic'
    elif 'spelling' in tokens or 'grammar' in tokens:
        return 'spelling_and_grammar'
    elif 'writing' in tokens or 'prompt' in tokens:
        return 'writing_prompt'
    else:
        return None

def get_help():
    input_text = input("What is your problem?: ")
    help_type = analyze_user_input(input_text)

    if help_type == 'math':
        # call solve_math_equation function
        result = solve_math_equation(input_text)
        return result
    elif help_type == 'topic':
        # call lookup_topic function
        information = lookup_topic(input_text)
        return information
    elif help_type == 'spelling_and_grammar':
        # call check_spelling_and_grammar function
        corrected_text = check_spelling_and_grammar(input_text)
        return corrected_text
    else:
        return "I'm sorry, I don't understand how to help you with that."


