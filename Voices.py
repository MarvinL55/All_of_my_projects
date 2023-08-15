import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Get the list of available voices
voices = engine.getProperty('voices')

# Print the available voices
for voice in voices:
    print(voice.id, voice.name)

# Set a specific voice
voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'  # Replace with the desired voice ID
engine.setProperty('voice', voice_id)

# Test the voice
engine.say("Hello, I'm the AI assistant.")
engine.runAndWait()
