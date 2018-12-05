import sys
import subprocess
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize   
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import random

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)

		self.setMinimumSize(QSize(400, 400))    
		self.setWindowTitle("Secure Chatting") 

		self.email_label = QLabel(self)
		self.email_label.setStyleSheet("QLabel {color : blue; }");
		self.label_captcha = QLabel(self)
		self.label_captcha.setStyleSheet("QLabel {color : blue; }");
		self.label_captcha2 = QLabel(self)
		self.label_captcha2.setStyleSheet("QLabel {color : brown; }");
		self.label_captcha.setText("CAPTCHA")
		self.label_captcha.setAlignment(Qt.AlignLeft)
		self.box_captcha = QLineEdit(self)
		self.msg_label = QLabel(self)
		self.msg_label.setStyleSheet("QLabel {color : red; }");	
		self.password_label = QLabel(self)
		self.password_label.setStyleSheet("QLabel {color : blue; }");
		self.email_label.setText("EMAIL-ID:")
		self.password_label.setText("PASSWORD:")
		self.email_box = QLineEdit(self)
		self.password_box = QLineEdit(self)	
		self.login_button = QPushButton('LOGIN', self)
		self.login_button.setStyleSheet("background-color: green")
		self.login_button.clicked.connect(self.login_func)	

		self.email_label.setAlignment(Qt.AlignLeft)
		self.password_label.setAlignment(Qt.AlignLeft)
		arr = ["HeLLo##@aa2", "LAKJ^&%VF", "KJ&^%hg&", "*&98GH65H", "HG$%vb%hg"]
		self.email_label.move(0,5)
		self.password_label.move(0,60)
		self.email_box.move(90,0)
		self.password_box.move(90,55)
		self.label_captcha.move(0, 96)
		self.label_captcha2.move(90, 87)
		a = random.choice([0, 1, 2, 3, 4])
		file_captcha = open("captcha.txt","w")
		file_captcha.write(str(a))
		file_captcha.close()
		self.label_captcha2.setText(arr[a])
		self.box_captcha.move(90, 120)
		self.email_box.resize(200,35)
		self.password_box.resize(200,35)
		self.login_button.resize(200,32)
		self.login_button.move(80,170)
		self.msg_label.move(80, 200)
		self.msg_label.setStyleSheet("QLabel {color : red; }");
				

	def login_func(self):
		file_captcha = open("captcha.txt","r")
		index = file_captcha.read()
		file_captcha.close()
		index_final = int(index)
		arr2 = ["HeLLoaa", "LAKJVF", "KJhg", "GHH", "HGvbhg"] 
		mail = self.email_box.text()
		mail = mail.strip()
		captcha = self.box_captcha.text()
		password = self.password_box.text()
		password = password.strip()
		flag = 0
		if captcha == arr2[index_final]:

			mydb = mysql.connector.connect(host="localhost", user="Ajitesh", passwd="Ajitesh56", database="ISS_project")
			mycursor = mydb.cursor()
			mycursor.execute("SELECT * FROM People")
			myresult = mycursor.fetchall()
			for x in myresult:
				if x[1] == mail and x[2] == password:
					flag = 1
					break
					
			if flag == 1:			
				subprocess.check_call(["python3", "chatting_page.py"])
			else:
				self.msg_label.setText("Wrong ID or Password")
		else:
			self.msg_label.setText("Wrong captcha entered")	

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	mainWin = MainWindow()
	mainWin.show()
	sys.exit( app.exec_() )
