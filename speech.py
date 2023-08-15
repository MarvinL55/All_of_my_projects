import speech_recognition as sr

def capture_audio():
    # capture audio from microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)
    return audio

def transcribe_audio(audio):
    # transcribe audio using google speech recognition
    r = sr.Recognizer()
    try:
        text = r.recognize_sphinx(audio)
        print("Transcription: " + text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google speech Recognition service ; {0}".format(e))

def save_transcription(text, filename):
    # capture the transcription to a file
    with open(filename, mode='w') as file:
        file.write(text)
    print("Transcription saved to file: " + filename)

# main part
if __name__ == '__main__':
    # capture audio from the mic
    audio = capture_audio()

    # transcribe the audio using Google speech Recognition
    text = transcribe_audio(audio)

    # save the audio to a file
    if text is not None:
        save_transcription(text, 'transcription.txt')