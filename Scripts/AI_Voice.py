# Import the Google Text-to-Speech library
from google.cloud import texttospeech
import warnings
warnings.filterwarnings("ignore", "Your application has authenticated using end user credentials")

# Initialize the Text-to-Speech client
client = texttospeech.TextToSpeechClient()

# Define the text input to be synthesized
text_input = texttospeech.SynthesisInput(text="Testing")

# Specify the voice request parameters
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Specify the audio output format
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected voice parameters and audio file type
response = client.synthesize_speech(
    input=text_input, voice=voice, audio_config=audio_config
)

# Save the output to an MP3 file
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print("Audio content written to file 'output.mp3'")
