import mysql.connector 

from PyQt6.QtWidgets import *
app = QApplication([])

class login(QMainWindow):  
  def tiklama1(self):
    ## print("Tiklanti")
     ka1   =  self.a.text()
     sifre =  self.sf.text()
     dogruSf = "q"
     dogruKa = "q"
    
     mesaj = QMessageBox()
     if ka1 == dogruKa and sifre == dogruSf:
            # mesaj.setText("Programa girebilirsin")
        self.close()
        self.a1 = anaekran()
        self.a1.show()
     else:
         mesaj.setText("yetkin yok")
         mesaj.exec()

     

  def __init__(self):
     super().__init__()

     


     icerik = QVBoxLayout()
     icerik.addWidget(QLabel("kullanici adi"))
     self.a = QLineEdit()
     icerik.addWidget(self.a)
     icerik.addWidget(QLabel("şifre::"))
     self.sf = QLineEdit()
     icerik.addWidget(self.sf)
     bt = QPushButton("Giriş Yap")
     icerik.addWidget(bt)    

     bt.clicked.connect(self.tiklama1)
  
     pencere = QWidget()
     pencere.setLayout(icerik)
     self.setCentralWidget(pencere)
class anaekran(QMainWindow):  
  def tiklama1(self):
    ## print("Tiklanti")
    
     sifre =  self.sf.text()
     dogruSf = "q"
     dogruKa = "q"
     mesaj = QMessageBox()
     mesaj.setText(f"Kullanici adi:{ka1}, sifre:{sifre}")
 
     

  def __init__(self):
     super().__init__()

     icerik = QVBoxLayout()
     
     icerik.addWidget(QLabel("seçiminizi giriniz::"))
     self.sf = QLineEdit()
     icerik.addWidget(self.sf)
     bt = QPushButton("Giriş Yap")
     icerik.addWidget(bt)    

     bt.clicked.connect(self.tiklama1)
  
     pencere = QWidget()
     pencere.setLayout(icerik)
     self.setCentralWidget(pencere)

 
ekran = login()
ekran.show()
app.exec()
