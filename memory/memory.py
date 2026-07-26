from memory.database import database


class Memory:

    def __init__(self):

        self.data = database.load()

    def get(self, key):

        return self.data.get(key)

    def set(self, key, value):

        self.data[key] = value

        database.save(self.data)


memory = Memory()