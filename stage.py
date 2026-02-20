class Stage:
    def __init__(self):
        self.location = ""
        self.enemy = ""
        self.prompt = "You encounter " + self.enemy + "at " + self.location+ " ! What will you do? It must make sense." # challenge prompt





    def set_location(self, location):
        self.location = location

    def set_enemy(self, enemy):
        self.enemy = enemy

    def get_location(self):
        return self.location
    
    def set_prompt(self, prompt):
        self.prompt = prompt

    def get_prompt(self):
        return self.prompt
    