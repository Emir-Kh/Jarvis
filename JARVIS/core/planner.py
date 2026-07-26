import re


class Planner:

    def plan(self, command: str):

        command = command.strip()

        if not command:
            return []

        parts = re.split(
            r"\s+(?:and then|then|and)\s+",
            command,
            flags=re.IGNORECASE
        )

        tasks = []

        for part in parts:

            part = part.strip()

            if not part:
                continue

            lower = part.lower()

            # -------------------------
            # FIND
            # -------------------------

            if lower.startswith("find "):

                tasks.append({
                    "intent": "find",
                    "command": part
                })

                continue

            # -------------------------
            # VS CODE
            # -------------------------

            if (
                "vs code" in lower
                or "visual studio code" in lower
                or "vscode" in lower
            ):

                tasks.append({
                    "intent": "open_vscode",
                    "command": part
                })

                continue

            # -------------------------
            # SEARCH
            # -------------------------

            if lower.startswith((
                "search ",
                "google ",
                "look up ",
                "search for "
            )):

                tasks.append({
                    "intent": "search",
                    "command": part
                })

                continue

            # -------------------------
            # OPEN
            # -------------------------

            if lower.startswith((
                "open ",
                "launch ",
                "start ",
                "run "
            )):

                tasks.append({
                    "intent": "open",
                    "command": part
                })

                continue

            # -------------------------
            # CHAT
            # -------------------------

            tasks.append({
                "intent": "chat",
                "command": part
            })

        return tasks