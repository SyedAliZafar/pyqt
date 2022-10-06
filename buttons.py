from PyQt5.QtWidgets import QApplication,QHBoxLayout,QVBoxLayout,QLabel,QWidget, QPushButton,QFileDialog
import sys
from PyQt5.QtGui import QIcon, QFont
#import runbatch
directory= False
class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.path = ' ' # default value at start (useful if you don't select new directory)
        print("the self to path is",self.path)
        #layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom) 

 
        self.setGeometry(400,400, 600,400)
        self.setWindowTitle("Automatic Detection of Defects [KIRAS Prototype]")
        self.setWindowIcon(QIcon('access.png'))
 
        self.create_buttons()
 
        self.setStyleSheet("QWidget {\n"
"\n"
"background-color:\"darkgreen\"\n"
"\n"
"}")


           

            
    def create_buttons(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        ###########################
        btn1 = QPushButton("Browse Directory", self)
        btn1.setStyleSheet('background-color:green')
        hbox.addWidget(btn1)
        btn1.clicked.connect(self.clicked_btn)
        btn1.clicked.connect(self.path_select)
        ##########################
        btn2 = QPushButton("Choose for executing script", self)
        btn2.setIcon(QIcon("access.png"))
        btn2.setStyleSheet('color:yellow')
        btn2.setStyleSheet('background-color:purple')
        hbox.addWidget(btn2)
        btn2.clicked.connect(self.second_clicked)
        #btn2.clicked.connect(self.second_clicked)
        #btn2.clicked.connect(runbatch.runscript)
        #blunch.clicked.connect(gps.runscript())
 
        self.label = QLabel("Hello, please set the directories before running the program")
        self.label.setFont(QFont("Sanserif", 15))
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)
 
        self.setLayout(vbox)
        #############
    
        #self.setLayout(layout)
        
        #### save file
        btn_confirm = QPushButton("Save the path", self)
        btn_confirm.clicked.connect(self.close)
        vbox.addWidget(btn_confirm)
        
        
        
        
        
        ##########
 
 
    def clicked_btn(self):
        self.label.setText("directory selected")

        #blunch.clicked.connect(gps.runscript())
        #self.label.setText(path_select)
 
 
    def second_clicked(self):
        self.label.setText("Perfekt! Sit Back and relax")
        self.label.setText("Executing Script, the values will be transferred automatically")

    def path_select(self):
        self.path = QFileDialog.getExistingDirectory()
        if self.path:
            print('[inside] path:', self.path)
        else:
            print('[inside] path: - not selected -')

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())