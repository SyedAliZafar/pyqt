from PyQt5.QtWidgets import QApplication,QHBoxLayout,QVBoxLayout,QLabel,QWidget, QPushButton,QFileDialog
import sys
from PyQt5.QtGui import QIcon, QFont
#import runbatch
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.path = '' # default value at start (useful if you don't select new directory)

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



    def path_select(self):
        self.path = QFileDialog.getExistingDirectory()
        if self.path:
            print('[inside] path:', self.path)
            self.label.setText("Directory Selected")
        else:
            print('[inside] path: - not selected -') 
            self.label.setText("No Directory Selected")
 
 
    def create_buttons(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
 
 
        btn1 = QPushButton("Set the directories", self)
        btn1.setIcon(QIcon("access.png"))
        btn1.setStyleSheet('color:red')
        btn1.setStyleSheet('background-color:green')
        hbox.addWidget(btn1)
        btn1.clicked.connect(self.clicked_btn)
 
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
        #self.show()
        btn_out_dir = QPushButton("Browse Directory", self)
        btn_out_dir.clicked.connect(self.path_select)
        vbox.addWidget(btn_out_dir)
        print("output file is ",btn_out_dir)
        
        #### save file
        btn_confirm = QPushButton("Save the path", self)
        btn_confirm.clicked.connect(self.close)
        vbox.addWidget(btn_confirm)
        
        
        
        
        
        ##########
 
 
    def clicked_btn(self):
        self.label.setText("No directory slot available")
        #blunch.clicked.connect(gps.runscript())
        #self.label.setText(path_select)
 
 
    def second_clicked(self):
        self.label.setText("Perfekt! Sit Back and relax")
        self.label.setText("Executing Script, the values will be transferred automatically")

 

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())