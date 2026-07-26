import json


class Settings:

    def __init__(self):

        with open(
            "config/settings.json",
            "r",
            encoding="utf-8"
        ) as file:

            self.data = json.load(file)

    def get(self, key):

        return self.data.get(key)


settings = Settings()