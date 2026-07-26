import pyttsx3

engine = pyttsx3.init()

from config.settings import settings

engine.setProperty(
    "rate",
    settings.get("voice_rate")
)

engine.setProperty(
    "volume",
    settings.get("voice_volume")
)

voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)


def speak(text):
    print("JARVIS:", text)

    engine.say(text)

    engine.runAndWait()