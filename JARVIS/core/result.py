from dataclasses import dataclass, field
from typing import Any


@dataclass
class SkillResult:

    success: bool

    message: str = ""

    data: Any = field(default_factory=dict)

    should_speak: bool = False