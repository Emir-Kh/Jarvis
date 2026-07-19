from brain.ai import ask
from voice.listen import listen
from voice.speak import speak
from skills.apps import open_app

from skills.apps import open_app
from skills.browser import open_website
from skills.system import system_command
from skills.music import play_music

speak("Good evening Sir. JARVIS is online.")

while True:

    user = listen()

    if user == "":
        continue

    if open_app(user):
        speak("Opening application, Sir.")
        continue

    if open_website(user):
        speak("Opening website, Sir.")
        continue

    if system_command(user):
        speak("Executing command, Sir.")
        continue

    if "music" in user.lower():
        play_music()
        speak("Opening your music folder.")
        continue


    if user.lower() == "exit":
        speak("Goodbye Sir.")
        break

    answer = ask(user)

    speak(answer)
    
        