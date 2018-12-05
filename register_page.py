import sys
import subprocess
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize   
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector
 

class MainWindow(QMainWindow):

	
	
	
	def __init__(self):
		QMainWindow.__init__(self)

		self.setMinimumSize(QSize(500, 500))    
		self.setWindowTitle("Secure Chatting") 
		
		self.name_label = QLabel(self)
		self.name_label.setStyleSheet("QLabel {color : blue; }");
		self.email_label = QLabel(self)
		self.email_label.setStyleSheet("QLabel {color : blue; }");
		self.password_label = QLabel(self)
		self.password_label.setStyleSheet("QLabel {color : blue; }");
		self.password2_label = QLabel(self)
		self.password2_label.setStyleSheet("QLabel {color : blue; }");
		self.name_label.setText("Name:")
		self.email_label.setText("EMAIL-ID:")
		self.password_label.setText("PASSWORD:")
		self.password2_label.setText("RE-Enter PASSWORD:")
		self.name_box = QLineEdit(self)		
		self.email_box = QLineEdit(self)
		self.password_box = QLineEdit(self)
		self.password2_box = QLineEdit(self)	
		self.register_button = QPushButton('REGISTER', self)
		self.register_button.clicked.connect(self.register_func)	

		self.name_label.setAlignment(Qt.AlignLeft)		
		self.email_label.setAlignment(Qt.AlignLeft)
		self.password_label.setAlignment(Qt.AlignLeft)
		self.password2_label.setAlignment(Qt.AlignLeft)

		self.name_label.move(0, 0)
		self.email_label.move(0, 55)
		self.password_label.move(0, 110)
		self.password2_label.move(0, 165)
		self.name_box.move(90, 0)
		self.email_box.move(90, 55)
		self.password_box.move(90, 110)
		self.password2_box.move(90, 165)
		
		self.name_box.resize(200,35)
		self.email_box.resize(200,35)
		self.password_box.resize(200,35)
		self.password2_box.resize(200, 35)
		self.register_button.move(80,215)	
				


	def register_func(self):
		mydb = mysql.connector.connect(host="localhost", user="Ajitesh", passwd="Ajitesh56", database="ISS_project")
		mycursor = mydb.cursor()
		mycursor.execute("SELECT * FROM People")
		myresult = mycursor.fetchall()
		name = self.name_box.text()
		email = self.email_box.text()
		password = self.password_box.text()
		password2 = self.password2_box.text()
		if password == password2:
			query = "INSERT INTO People(Name, Email, Password)VALUES(%s, %s, %s)"
			input = (name, email, password)
			mycursor.execute(query, input)
			mydb.commit()
			subprocess.check_call(["python3", "chatting_page.py"])
		else:
			print("Both passwords donot match")

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	mainWin = MainWindow()
	mainWin.show()
	sys.exit( app.exec_() )
