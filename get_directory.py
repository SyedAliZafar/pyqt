import sys
import os
import PyQt5
#from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QWizard, QVBoxLayout, QPushButton, QFileDialog


class Window(QWizard):

    def __init__(self):
        super().__init__()

        self.path = '' # default value at start (useful if you don't select new directory)

        #layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom) 
        layout = QVBoxLayout()
        self.setLayout(layout)

        btn_out_dir = QPushButton("Output Directory", self)
        btn_out_dir.clicked.connect(self.path_select)
        layout.addWidget(btn_out_dir)

        btn_confirm = QPushButton("Confirm", self)
        btn_confirm.clicked.connect(self.close)
        layout.addWidget(btn_confirm)

    def path_select(self):
        self.path = QFileDialog.getExistingDirectory()
        if self.path:
            print('[inside] path:', self.path)
        else:
            print('[inside] path: - not selected -')


app = QApplication(sys.argv)

GUI = Window()
GUI.show()

status_code = app.exec_()

print('[outside] path:', GUI.path)