import speech_recognition as sr
#import pyaudio
r = sr.Recognizer()
with sr.WavFile("/opt/speechscript/input.wav") as source:              # use "test.wav" as the audio source
    audio = r.record(source)                        # extract audio data from the file

try:
    print(" " + r.recognize(audio))   # recognize speech using Google Speech Recognition
except LookupError:                                 # speech is unintelligible
    print("Could not understand audio!")


