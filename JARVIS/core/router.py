from skills.manager import SkillManager

manager = SkillManager()


def route(command):

    return manager.execute(command)