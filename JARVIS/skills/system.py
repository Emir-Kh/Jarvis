import os


def system_command(command):

    command = command.lower()

    if "shutdown" in command:
        os.system("shutdown /s /t 5")
        return True

    if "restart" in command:
        os.system("shutdown /r /t 5")
        return True

    if "lock" in command:
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return True

    return False