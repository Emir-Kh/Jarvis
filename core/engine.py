from voice.listen import listen
from voice.speak import speak

from core.router import route
from core.planner import Planner
from core.task_executor import TaskExecutor

from brain.ai import AIManager


class JarvisEngine:

    def __init__(self):

        self.running = True

        self.ai = AIManager()

        self.planner = Planner()

        self.executor = TaskExecutor(
            router=route,
            ai=self.ai
        )

    def run(self):

        speak("Jarvis is online, Sir.")

        while self.running:

            command = listen()

            if not command:
                continue

            if command.lower().strip() == "exit":

                speak("Goodbye Sir.")

                self.running = False

                break

            tasks = self.planner.plan(command)

            results = self.executor.execute_plan(tasks)

            for result in results:

                if result.should_speak:

                    speak(result.message)