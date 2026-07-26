import shutil
import subprocess

from skills.app_launcher.database import load_apps


ALIASES = {
    "vs code": "code",
    "vscode": "code",
    "visual studio code": "code",

    "google chrome": "chrome",
    "chrome browser": "chrome",

    "microsoft edge": "msedge",
}


def normalize_name(name):

    name = name.lower().strip()

    for prefix in [
        "open ",
        "launch ",
        "start ",
        "run ",
    ]:

        if name.startswith(prefix):
            name = name[len(prefix):].strip()

    return name


def launch(app_name):

    app_name = normalize_name(app_name)

    app_name = ALIASES.get(
        app_name,
        app_name
    )

    # 1. Try Windows PATH
    path = shutil.which(app_name)

    if path:

        subprocess.Popen([path])

        return True

    # 2. Try application database
    apps = load_apps()

    # Exact match
    if app_name in apps:

        subprocess.Popen(
            apps[app_name]
        )

        return True

    # Partial match
    for name, path in apps.items():

        if app_name in name or name in app_name:

            subprocess.Popen(path)

            return True

    return False


def open_with_vscode(path=None):

    # -------------------------
    # Try PATH
    # -------------------------

    vscode = shutil.which("code")

    if vscode:

        try:

            if path:

                subprocess.Popen([
                    vscode,
                    path
                ])

            else:

                subprocess.Popen([
                    vscode
                ])

            return True

        except Exception as e:

            print(f"[VS Code PATH Error] {e}")

    # -------------------------
    # Search apps database
    # -------------------------

    apps = load_apps()

    vscode_path = None

    for name, app_path in apps.items():

        name_lower = name.lower()

        if (
            "visual studio code" in name_lower
            or name_lower == "vs code"
            or name_lower == "vscode"
            or name_lower == "code"
        ):

            vscode_path = app_path
            break

    if not vscode_path:

        return False

    try:

        if path:

            subprocess.Popen([
                vscode_path,
                path
            ])

        else:

            subprocess.Popen([
                vscode_path
            ])

        return True

    except Exception as e:

        print(f"[VS Code Error] {e}")

        return False