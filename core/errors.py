class JarvisError(Exception):
    """Base error for JARVIS."""
    pass


class TaskError(JarvisError):
    """A task could not be completed."""
    pass


class SkillError(JarvisError):
    """A skill failed."""
    pass


class ContextError(JarvisError):
    """Context data is missing or invalid."""
    pass