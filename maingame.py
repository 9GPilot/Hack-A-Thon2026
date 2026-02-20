from stage import Stage

class MainGame:
    def __init__(self):
        self.stages = []
        self.stageCount = 0
        self.current_stage = 0
    
    def add_stage(self, stageNum, location, prompt):
        stage = Stage()
        stage.set_stageNum(stageNum)
        stage.set_location(location)
        stage.set_prompt(prompt)

        self.stages.append(stage)
        self.stageCount += 1

    def get_stage(self):
        if self.current_stage < self.stageCount:
            self.current_stage += 1
            return self.stages[self.current_stage-1]
        return False
    
    def atLeastOneStage(self):
        return self.stageCount >= 1
        