import webbrowser


def open_website(command):

    command = command.lower()

    if "youtube" in command:
        webbrowser.open("https://youtube.com")
        return True

    if "google" in command:
        webbrowser.open("https://google.com")
        return True

    if "github" in command:
        webbrowser.open("https://github.com")
        return True

    return False