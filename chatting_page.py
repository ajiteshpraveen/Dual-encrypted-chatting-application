import sys
import subprocess
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize   
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import socket  
 

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)

		self.setMinimumSize(QSize(300, 500))    
		self.setWindowTitle("Secure Chatting") 
		
		
		self.message_label = QLabel(self)
		self.message_label.setText("MESSAGE INCOMING:")
		self.message_label.setStyleSheet("QLabel {color : blue; }");
		self.message_label2 = QLabel(self)
		self.message_label2.setText("Server message")		
		self.message_box = QLineEdit(self)			
		self.send_button = QPushButton('SEND MESSAGE', self)
		self.send_button.setStyleSheet("background-color: green")
		self.send_button.clicked.connect(self.send_func)	
		self.message_label.move(0, 0)
		self.message_label.resize(150, 32)
		self.message_label2.resize(260,120)
		self.message_label2.move(20, 32)
		self.message_label2.setStyleSheet("background: cyan");
		self.message_box.move(20, 120)
		self.message_box.resize(260, 150)
		self.message_box.setPlaceholderText("Write Here ") 
		self.send_button.move(70, 330)	
		self.send_button.resize(150,32)
				


	def send_func(self): 
		s = socket.socket()           
		port = 8080                 
		s.connect(('localhost', port))
		msg = str(self.message_box.text())
		file_plain = open("plain_text.txt","w")
		file_plain.write(msg)		
		file_plain.close()	
		subprocess.check_call(["python3", "rail_fence.py"])
		subprocess.check_call(["python3", "aes_encrypt.py"])
		file_cipher = open("encryption_file.txt","r")
		cipher_text = file_cipher.read()
		file_cipher.close()
		s.send(bytes(cipher_text,"utf8"))

		incoming_msg = (s.recv(1024)).decode("utf-8")
		file_cipher_text = open("encryption_file.txt","w")
		file_cipher_text.write(incoming_msg)
		file_cipher_text.close()
		subprocess.check_call(["python3", "aes_decrypt.py"])
		subprocess.check_call(["python3", "rail_fence_decipher.py"])

		file_decode = open("decoded_text.txt","r")
		t = file_decode.read()
		file_decode.close()
		self.message_label2.setText(t)
		s.close()
		
		

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	mainWin = MainWindow()
	mainWin.show()
	sys.exit( app.exec_() )
