#!/usr/bin/env python3

import sys
from functools import partial
from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGridLayout

class Button(QPushButton):

    def __init__(self):
        QPushButton.__init__(self)
        self.setStyleSheet('font-size: 50pt')
    
    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

class App(QWidget):

    def __init__(self):
        super(App, self).__init__()
        self.xTurn = True
        self.setGeometry(500, 150, 500, 500)
        self.setWindowTitle("TicTacToe")
        self.winPosition = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                            [1, 4, 7], [2, 5, 8], [3, 6, 9],
                            [1, 5, 9], [3, 5, 7]]
        position = [(0, 0), (0, 1), (0, 2),
                    (1, 0), (1, 1), (1, 2),
                    (2, 0), (2, 1), (2, 2)]
        self.buttons = []
        self.xClickedPosition = []
        self.oClickedPosition = []
        objectName = 1  
        layout = QGridLayout()
        for i in position:
            button = Button()
            button.setId(objectName)
            button.setFixedHeight((self.height()/3)-17)
            button.setFixedWidth((self.width()/3)-17)
            button.clicked.connect(partial(self.buttonPushed, button))
            layout.addWidget(button, i[0], i[1])
            objectName = objectName + 1
            self.buttons.append(button)
        self.setLayout(layout)
        self.show()

    def buttonPushed(self, button):
        if self.xTurn:
            button.setText("X")
            self.xClickedPosition.append(button.getId())
        else:
            button.setText("O")
            self.oClickedPosition.append(button.getId())
        button.setDisabled(True)
        self.xTurn = not self.xTurn
        for position in self.winPosition:
            if set(position).issubset(set(self.xClickedPosition)) or set(position).issubset(set(self.oClickedPosition)):
                for button in self.buttons:
                    if button.getId() in position:
                        button.setDisabled(False)
                        button.clicked.disconnect()
                    else:
                        button.setDisabled(True)
            
if __name__ == '__main__':
    application = QApplication(sys.argv)
    app = App()
    application.exec_()