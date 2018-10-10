from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QVBoxLayout,  QTextEdit
from PyQt5.QtGui import QFont
import speech_recognition as sr
import sys

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "Audio a texto MCC"
        self.top = 10
        self.left = 30
        self.width = 400
        self.height = 200

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()

        self.textedit = QTextEdit(self)
        self.textedit.setFont(QFont("Times", 15))
        vbox.addWidget(self.textedit)

        self.btn2 = QPushButton("Procesar Audio")
        vbox.addWidget(self.btn2)
        self.btn2.clicked.connect(self.convertirAudio)

       # self.btn2 = QPushButton("Guardar Txt")
       # vbox.addWidget(self.btn2)
       # self.btn2.clicked.connect(self.guardartexto)

        self.setLayout(vbox)
  
    def convertirAudio(self):
        r = sr.Recognizer()
        sound = 'M3 180926143117656_MIT_10253_2.wav'
        

        with sr.AudioFile(sound) as source:
            sound = r.listen(source)
        
        try:
            text = r.recognize_google(sound,language='es-CO')
            self.textedit.setText(text)

            self.print = text
            print (self.print)

            archivo = open("archivo.txt","w")
            archivo.write(self.print)
            archivo.close()

        except Exception as e:
            print('Error al Procesar el audio')
    
   # def guardartexto(self): 
          
     #  archivo = open("archivito.txt","w")
     #  archivo.write(self.print)
     #  archivo.close()     

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
