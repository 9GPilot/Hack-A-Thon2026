class Stage:
    def __init__(self):
        self.stageNum = 0
        self.location = ""
        self.prompt = "" # challenge prompt

    def set_stageNum(self, num):
        self.stageNum = num

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location
    
    def set_prompt(self, prompt):
        self.prompt = prompt

    def get_prompt(self):
        return self.prompt
    