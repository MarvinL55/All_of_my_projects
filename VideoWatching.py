import cv2
import moviepy.editor as mp
import speech_recognition as sr
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

recognizer = sr.Recognizer()

def video_to_text(video_path):
    # Video to audio conversion
    video = mp.VideoFileClip(video_path)
    audio_path = 'audio.wav'
    video.audio.write_audiofile(audio_path)

    # Speech recognition using CMU Sphinx (PocketSphinx)
    try:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_sphinx(audio)
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Error during speech recognition: {e}")
        return ""

def summarize_text(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return ''.join(str(sentence) for sentence in summary)

def main():
    video_path = "C:\\Users\\marvi\\Videos\\20230720_164319.mp4"
    video_text = video_to_text(video_path)
    summarized_text = summarize_text(video_text)
    print(summarized_text)

    # Save the summarized text to a text file named "output.txt"
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(summarized_text)

if __name__ == "__main__":
    main()
