import json
import os

DB_PATH = "memory/data.json"


class Database:

    def load(self):

        if not os.path.exists(DB_PATH):

            return {}

        with open(DB_PATH, "r", encoding="utf-8") as f:

            return json.load(f)

    def save(self, data):

        with open(DB_PATH, "w", encoding="utf-8") as f:

            json.dump(data, f, indent=4)


database = Database()