import os

from skills.app_launcher.database import save_apps

folders = [

    r"C:\Program Files",

    r"C:\Program Files (x86)",

    os.path.expandvars(r"%LOCALAPPDATA%"),

    os.path.expandvars(r"%APPDATA%")
]


def scan_apps():

    apps = {}

    for folder in folders:

        if not os.path.exists(folder):
            continue

        for root, dirs, files in os.walk(folder):

            for file in files:

                if file.endswith(".exe"):

                    name = file.replace(".exe", "").lower()

                    apps[name] = os.path.join(root, file)

    save_apps(apps)

    return apps