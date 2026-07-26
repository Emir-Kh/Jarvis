from collections import Counter
from voice.speak import speak
from vision.detector import detect

def analyze_scene():

    speak("Analyzing your workspace, Sir.")

    objects = detect(5)

    if not objects:
        speak("I couldn't detect any objects.")
        return

    counter = Counter(objects)

    report = []

    for name, count in counter.items():
        report.append(f"{count} {name}")

    sentence = ", ".join(report)

    speak(f"I detected {sentence}.")

    # تحلیل ساده
    if "laptop" in counter and "keyboard" in counter and "mouse" in counter:
        speak("This appears to be a computer workstation.")

    if "cup" in counter or "bottle" in counter:
        speak("I also detected a drink on the desk.")

    if len(counter) > 8:
        speak("Your desk appears crowded.")
    else:
        speak("Your desk appears organized.")