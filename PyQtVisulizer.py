from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QSlider, QLineEdit
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class MainWindow(QMainWindow):
    def __init__(self, MainGameObject):
        super().__init__()

        self._myMainGameObject = MainGameObject

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
        self.imageLabel = QLabel()
        pixmap = QPixmap(os.path.join(BASE_DIR,"startingImg.png"))
        pixmap = pixmap.scaled(500,500)
        self.imageLabel.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        self.challegePromptLable = QLabel("Challenge Prompt Here")
        self.enterInputBelowLabel = QLabel("Enter your response to the challenge below:")
        self.input = QLineEdit()
        self.input.setPlaceholderText("How would you solve this challange...")

        layout = QVBoxLayout()
        layout.addWidget(self.imageLabel)
        layout.addWidget(self.challegePromptLable)
        layout.addWidget(self.enterInputBelowLabel)
        layout.addWidget(self.input)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def start_game(self):
        """
        Only happens once, after the user enters their paragraph,
        if the MainGameObject has atleast 1 stage ready then GO GO GO 
        """
        if self._myMainGameObject not None and self._myMainGameObject.atLeastOneStage():
            # good to go,show the stage 
        else:
            self.submitBtn.setText("Please wait... generating... ")
            # GET THE TEXT INPUT 
            inputParagraph: str = self.promptInput.text()
            # TODO CALL JAKES FUNCTION HERE TO START GENERATING THE MAIN
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
