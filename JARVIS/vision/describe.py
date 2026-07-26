from voice.speak import speak
from vision.detector import detect

def describe_scene():

    speak("Scanning the room, Sir.")

    objects = detect(5)

    if not objects:
        speak("I couldn't detect any objects.")
        return

    text = ", ".join(objects)

    speak(f"I detected {text}.")