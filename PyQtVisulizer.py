from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QSlider, QLineEdit
from PyQt5.QtCore import QSize, QTimer
from PyQt5.QtGui import QPixmap
import os
import gemini_functions

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._myMainGameObject = None
        self._currentStage = None

        self.setWindowTitle("Story Game!")
        #self.setFixedSize(QSize(800,1000))
        self.show_intro_screen()

    def show_intro_screen(self):
        """
        The screen asking the user for a paragraph input
        """
        self.promptInput = QLineEdit()
        self.promptInput.setPlaceholderText("Describe yourself...")
        self.submitBtn = QPushButton("Start Game")
        self.submitBtn.clicked.connect(self.start_game) # On click, check if the MainGame object is initulized. If so then start
        layout = QVBoxLayout()
        layout.addWidget(QLabel("We would like you to describe yourself. Do so below"))
        layout.addWidget(self.promptInput)
        layout.addWidget(submitBtn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def show_stage_screen(self):
        """
        Shows the screen displaying the setting image and the challange prompt
        """
        currentStage = self._currentStage

        self.imageLabel = QLabel()
        imageLoc = currentStage.get_location() # pulls from the stage object given
        pixmap = QPixmap(os.path.join(BASE_DIR,imageLoc))
        pixmap = pixmap.scaled(500,500)
        self.imageLabel.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        self.challegePromptLable = QLabel(currentStage.get_prompt())
        self.enterInputBelowLabel = QLabel("Enter your response to the challenge below:")
        self.input = QLineEdit()
        self.input.setPlaceholderText("How would you solve this challange...")
        self.geminiResponse = QLable()

        self.input.returnPressed.connect(self.validateUserSolution)

        layout = QVBoxLayout()
        layout.addWidget(self.imageLabel)
        layout.addWidget(self.challegePromptLable)
        layout.addWidget(self.enterInputBelowLabel)
        layout.addWidget(self.input)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


    def validateUserSolution(self):
        """
        After the current stage has a enter pressed on the input, that means
        a solution was passed in, validate this solution or not 
        """
        # get the user solution
        userSolution = self.input.text()
        currentChalenge = self._currentStage.get_prompt()
        result: bool = gemini_functions.is_reasonable_solution_GEMINI_API("Spider","Building",userSolution)
        if result == False:
            self.geminiResponse("Your response is not good enough.. Try again")
        else:
            self.geminiResponse("NICE JOB! SUCCESS")
            self._currentStage = self._myMainGameObject.get_stage()
            QTimer.singleShot(2000, self.show_stage_screen)




    def start_game(self):
        """
        Only happens once, after the user enters their paragraph,
        if the MainGameObject has atleast 1 stage ready then GO GO GO 
        """
        if self._myMainGameObject not None and self._myMainGameObject.atLeastOneStage():
            self._currentStage = self._myMainGameObject.get_stage()
            self.show_stage_screen()
        else:
            self.submitBtn.setText("Please wait... generating... ")
            inputParagraph: str = self.promptInput.text()
            self._myMainGameObject = controler.initialize_gamestate(inputParagraph)
            return False

def main(mainGameObject):
    """
    This is going to accept a `MainGame` object, this object will be used
    to pull current stage that we are at. Then using this `Stage` object
    we will grab the image in our folder, and the challenge prompt and ask 
    the user how they are going to pass this challenge. This 
    "challengeInput" will be given to gemini to ask if its a valid input 
    for the challange presented

    MainGameObject:
        + getNextStage(): StageObj


    Goal: Have space for an image, 
    have space for text
    have space for input 
    """

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()



if __name__ == "__main__":
    main(None)
