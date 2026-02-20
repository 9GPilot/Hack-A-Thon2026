class BattlePromptStringGenerate:
    def __init__(self, setting: str, enemy: str, defeated_how: str = None):
        """
        Initializes the BattlePrompt object.
        """
        self.setting = setting
        self.enemy = enemy
        self.defeated_how = defeated_how

    def get_prompt_string(self):
        if (self.defeated_how) is None:
            return "GENERATE AN IMAGE in MINIMAL PIXEL STYLE WITH A 10px WHITE BORDER, WITH NO TEXT IN THE IMAGE. SETTING IS: " + self.setting + ". SUBJECT IS: " + self.enemy
        else:
            return "GENERATE AN IMAGE in MINIMAL PIXEL STYLE WITH A 10px WHITE BORDER, WITH NO TEXT IN THE IMAGE. SETTING IS: " + self.setting + ". SUBJECT IS: " + self.enemy + "THE SUBJECT IS DEFEATED BY: " + self.defeated_how

    def set_defeated_how(self, defeated_how: str):
        self.defeated_how = defeated_how

    def __str__(self):
        """
        Returns a formatted string for printing or AI usage.
        """
        return (f"Setting: {self.setting}\n"
                f"Enemy: {self.enemy}\n"
                f"Defeated By: {self.defeated_how}")