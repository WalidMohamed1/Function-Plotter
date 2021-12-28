import re
import sys
from PySide2.QtGui import QIcon
import matplotlib.pyplot as plt
import numpy as np
from PySide2.QtWidgets import( 
    QApplication,
    QDesktopWidget,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QWidget)

allowed_words = [
    'x',
    'sin',
    'cos',
    'sqrt',
    'exp',
    '/',
    '+',
    '*',
    '^',
    '-'
]

replacements = {
    'sin': 'np.sin',
    'cos': 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**',
}

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Build main frame --
        self.setWindowTitle("Function Plotter")
        self.setGeometry(500,400,480,160)
        self.qRect = self.frameGeometry()
        self.centerPoint = QDesktopWidget().availableGeometry().center()
        self.qRect.moveCenter(self.centerPoint)
        self.move(self.qRect.topLeft())
        self.appIcon = QIcon("icon.png")
        self.setWindowIcon(self.appIcon)
        # Build a label of function --
        self.functionLabel = QLabel("Function f(x):",self)
        self.functionLabel.move(15,20)
        # Build a function lineEdit taken by user --
        self.function = QLineEdit(self)
        self.function.move(15,40)
        self.function.resize(450,20)
        # Build a label of min,max --
        self.minLabel = QLabel("Min(x):",self)
        self.minLabel.move(15,75)
        self.maxLabel = QLabel("Max(x):",self)
        self.maxLabel.move(330,75)
        # Build a min,max lineEdit taken by user --
        self.min = QLineEdit(self)
        self.min.move(15,95)
        self.max = QLineEdit(self)
        self.max.move(330,95)
        # Build a plot button --
        self.plotButton = QPushButton("Plot",self)
        self.plotButton.move(165,94)   
        self.plotButton.resize(150,22)
        self.plotButton.clicked.connect(self.plotFunctionButton)
        # Build an error dialog --
        self.checkError = QMessageBox()

    def string2func(self,string):
        # Find all words and check if all are allowed:
        for word in re.findall('[a-zA-Z_]+', string):
            if word not in allowed_words:
                raise ValueError(
                    f"'{word}' is forbidden to use in math expression.\nOnly functions of 'x' are allowed.\ne.g., 5*x^3 + 2/x - 1\nList of allowed words: {', '.join(allowed_words)}"
                )

        for old, new in replacements.items():
            string = string.replace(old, new)

        # To deal with constant functions e.g., y = 1
        if "x" not in string:
            string = f"{string}+0*x"

        def func(x):
            return eval(string)

        return func
          
    def plotFunctionButton(self):
        mn = self.min.text()
        mx = self.max.text()
        fun = self.function.text()
        # To handle error --
        if not mn or not mx or not fun :
            self.showErrorDialog("All fields are required. Please try again.")
        elif float(mn) >= float(mx) :
            self.showErrorDialog("Max value should be greater than min value.")  
        else:
            # Build function plotter --
            try:
                self.buildFunction() 
            # Hanlding error of taken function --
            except ValueError as msg:
                self.showErrorDialog(str(msg)) 
                return    

    def showErrorDialog(self,str):
        self.checkError.setText(str)
        self.checkError.show()

    def buildFunction(self):
        mn = self.min.text()
        mx = self.max.text()
        fun = self.function.text()
        minValue = float(mn)
        maxValue = float(mx)

        x = np.linspace(minValue,maxValue,1000)
        y = self.string2func(fun)(x)
        plt.plot(x,y)
        plt.show()


if __name__ == "__main__":
    myApp = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(myApp.exec_())





