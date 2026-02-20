from stage import Stage







class Game:
    def __init__(self):
        self.stages = []
        self.stageCount = 0
        self.current_stage = 0

    
    def add_stage(self, image_file_location:str, location:str, enemy:str):
        stage = Stage()
        stage.set_file_location(image_file_location)
        stage.set_location(image_file_location)
        stage.set_enemy(image_file_location)

        self.stages.append(stage)
        self.stageCount += 1

    def get_stage(self):
        if self.current_stage < self.stageCount:
            self.current_stage += 1
            return self.stages[self.current_stage-1]
        return False
    
    def atLeastOneStage(self):
        return self.stageCount >= 1
        