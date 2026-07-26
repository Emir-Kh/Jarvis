from skills.browser import open_website
from skills.system import system_command
from skills.file_manager import open_file

from skills.app_launcher.launcher import launch


from logs.logger import info, error


class SkillManager:

    def __init__(self):

        self.skills = [
            open_file,
            launch,
            open_website,
            system_command,
        ]

    def execute(self, command):

        for skill in self.skills:

            try:

                if skill(command):

                    info(
                        f"Skill Executed: "
                        f"{skill.__name__}"
                    )

                    return True

            except Exception as e:

                print(f"[Skill Error] {e}")

                error(
                    f"{skill.__name__}: {e}"
                )

        return False