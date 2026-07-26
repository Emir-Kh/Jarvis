from core.result import SkillResult
from core.context import JarvisContext

from skills.file_manager import find_file_result
from skills.app_launcher.launcher import open_with_vscode


class TaskExecutor:

    def __init__(self, router, ai):

        self.router = router
        self.ai = ai
        self.context = JarvisContext()

    def execute(self, task):

        intent = task["intent"]
        command = task["command"]

        # -------------------------
        # FIND
        # -------------------------

        if intent == "find":

            try:
            
                result = find_file_result(command)
        
                if result["success"]:
                
                    self.context.set(
                        "last_file",
                        result["path"]
                    )
        
                    return SkillResult(
                        success=True,
                        message=f"Found {result['name']}",
                        data=result
                    )
        
                return SkillResult(
                    success=False,
                    message=f"Sir, I couldn't find {command}.",
                    data=result
                )
        
            except Exception as e:
            
                print(f"[Find Error] {e}")
        
                return SkillResult(
                    success=False,
                    message="An error occurred while searching for the file."
                )

        # -------------------------
        # OPEN IN VS CODE
        # -------------------------

        if intent == "open_vscode":

            path = self.context.get("last_file")
        
            if not path:
            
                return SkillResult(
                    success=False,
                    message="Sir, I don't have a file path from the previous task."
                )
        
            try:
            
                success = open_with_vscode(path)
        
                if success:
                
                    return SkillResult(
                        success=True,
                        message=f"Opened {path} in VS Code.",
                        data={
                            "path": path
                        }
                    )
        
                return SkillResult(
                    success=False,
                    message="Sir, I couldn't open VS Code."
                )
        
            except Exception as e:
            
                print(f"[VS Code Error] {e}")
        
                return SkillResult(
                    success=False,
                    message="An error occurred while opening VS Code."
                )

        # -------------------------
        # NORMAL SKILLS
        # -------------------------

        if intent in ("open", "search"):

            try:

                success = self.router(command)

                if success:

                    return SkillResult(
                        success=True,
                        message=f"Completed: {command}",
                        data={
                            "command": command
                        }
                    )

                return SkillResult(
                    success=False,
                    message=f"I could not complete: {command}",
                    data={
                        "command": command
                    }
                )

            except Exception as e:

                return SkillResult(
                    success=False,
                    message=f"Skill error: {e}"
                )

        # -------------------------
        # AI CHAT
        # -------------------------

        if intent == "chat":

            try:

                answer = self.ai.ask(command)

                return SkillResult(
                    success=True,
                    message=answer,
                    data={
                        "answer": answer
                    },
                    should_speak=True
                )

            except Exception as e:

                return SkillResult(
                    success=False,
                    message=f"AI error: {e}"
                )

        return SkillResult(
            success=False,
            message=f"Unknown intent: {intent}"
        )

    def execute_plan(self, tasks):

        self.context.clear()

        results = []

        for index, task in enumerate(tasks):

            result = self.execute(task)

            self.context.set(
                f"task_{index + 1}",
                result.data
            )

            results.append(result)

            if not result.success:

                break

        return results