import subprocess

def open_app(command):

    command = command.lower()

    if "chrome" in command:
        subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    elif "notepad" in command:
        subprocess.Popen("notepad")

    elif "calculator" in command:
        subprocess.Popen("calc")

    elif "paint" in command:
        subprocess.Popen("mspaint")

    elif "explorer" in command:
        subprocess.Popen("explorer")

    else:
        return False

    return True