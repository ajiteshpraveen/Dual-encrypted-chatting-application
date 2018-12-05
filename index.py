import sys
import subprocess
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize   
 

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)

		self.setMinimumSize(QSize(300, 300))    
		self.setWindowTitle("Secure Chatting") 

		self.message_label = QLabel(self)
		self.message_label.setText("SELECT LOGIN OR REGISTER")
		self.message_label.move(35, 30)
		self.message_label.resize(300,20)
		self.message_label.setStyleSheet("QLabel {color : blue; }");

		self.login_button = QPushButton('LOGIN', self)
		self.login_button.setStyleSheet("background-color: green")
		self.login_button.clicked.connect(self.login_func)
		self.login_button.resize(100,32)
		self.login_button.move(50, 90)
		
		self.register_button = QPushButton('REGISTER', self)
		self.register_button.setStyleSheet("background-color: green")
		self.register_button.clicked.connect(self.register_func)
		self.register_button.resize(100,32)  
		self.register_button.move(150, 90)
		      

	def login_func(self):
		self.hide()
		subprocess.check_call(["python3", "login_page.py"])

	def register_func(self):
		subprocess.check_call(["python3", "register_page.py"])

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	mainWin = MainWindow()
	mainWin.show()
	sys.exit( app.exec_() )
