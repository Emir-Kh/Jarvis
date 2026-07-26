import os
import subprocess
from pathlib import Path


SEARCH_FOLDERS = [
    Path.home() / "Desktop",
    Path.home() / "Documents",
    Path.home() / "Downloads",
    Path.home() / "Pictures",
    Path.home() / "Videos",
    Path.home() / "Music",
]


def clean_query(query):
    query = query.lower().strip()

    for prefix in [
        "open file ",
        "open folder ",
        "open ",
        "launch ",
        "start ",
        "run ",
        "find ",
    ]:
        if query.startswith(prefix):
            query = query[len(prefix):].strip()

    return query


def find_file(query):
    query = clean_query(query)

    if not query:
        return None

    # Exact match
    for folder in SEARCH_FOLDERS:

        if not folder.exists():
            continue

        try:
            for path in folder.rglob("*"):

                if path.name.lower() == query:
                    return path

        except (PermissionError, OSError):
            continue

    # Partial match
    for folder in SEARCH_FOLDERS:

        if not folder.exists():
            continue

        try:
            for path in folder.rglob("*"):

                if query in path.name.lower():
                    return path

        except (PermissionError, OSError):
            continue

    return None

def find_file_result(command):

    query = clean_query(command)

    path = find_file(query)

    if path is None:
        return {
            "success": False,
            "path": None,
            "name": query
        }

    return {
        "success": True,
        "path": str(path),
        "name": path.name
    }

def open_file(command):

    query = clean_query(command)

    path = find_file(query)

    if path is None:
        return False

    try:
        os.startfile(str(path))
        return True

    except Exception as e:
        print(f"[File Error] {e}")
        return False