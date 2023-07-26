from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *     #textni o'ngga surish uchun

global son
son = '0'

app = QApplication([])

oyna = QWidget()
oyna.setFixedSize(355, 650)
oyna.move(800, 50)
oyna.setWindowIcon(QIcon("D:\\Python\\th.jpeg"))
oyna.setStyleSheet("""
    background-color: black;
    font-size: 30px;
    """)

output = QLabel(oyna)
output.setText('0')
output.setGeometry(30, 110, 290, 80)
output.setAlignment(Qt.AlignRight)
output.setStyleSheet("""
    color: white;
    font-size: 60px;
    """)


#1-qator


injener = QPushButton(oyna)
injener.setText('')    

ochirish = QPushButton(oyna)
ochirish.setText("C")
ochirish.setGeometry(15, 210, 70, 70)
ochirish.setStyleSheet("""
    QPushButton {
    background-color: #A5A5A5;
    border-radius: 35px;
    }
    QPushButton:pressed {
    background-color: grey;
    }
""")

foiz = QPushButton(oyna)
foiz.setText("%")
foiz.setGeometry(100, 210, 70, 70)
foiz.setStyleSheet("""
    QPushButton {
    background-color: #A5A5A5;
    border-radius: 35px;
    }
    QPushButton:pressed {
    background-color: grey;
    }
    """)

backspace = QPushButton(oyna)
backspace.setText('⌫')
backspace.setGeometry(185, 210, 70, 70)
backspace.setStyleSheet("""
    QPushButton {
    background-color: #A5A5A5;
    border-radius: 35px;
    }
    QPushButton:pressed {
    background-color: grey;
    }
    """)

boluv = QPushButton(oyna)
boluv.setText('÷')
boluv.setGeometry(270, 210, 70, 70)
boluv.setStyleSheet("""
    QPushButton {
    color: white;
    background-color: #FF9F0C;
    border-radius: 35px;
    }
    QPushButton:pressed {
    background-color: grey;
    }
    """)


# 2-qator
    

yetti = QPushButton(oyna)
yetti.setText("7")
yetti.setGeometry(15, 295, 70, 70)
yetti.setStyleSheet("""
    QPushButton {
    color: white;
    background-color: #343434;
    border-radius: 35px;
    }
    QPushButton:pressed {
    background-color: grey;
    }
""")

sakkiz = QPushButton(oyna)
sakkiz.setText("8")
sakkiz.setGeometry(100, 295, 70, 70)
sakkiz.setStyleSheet("""
    QPushButton {
    color: white;
    background-color: #343434;
    border-radius: 35px;
    }
    QPushButton:pressed {
    background-color: grey;
    }
    """)

toqqiz = QPushButton(oyna)
toqqiz.setText('9')
toqqiz.setGeometry(185, 295, 70, 70)
toqqiz.setStyleSheet("""
    QPushButton {
    color: white;
    background-color: #343434;
    border-radius: 35px;
    }
    QPushButton:pressed {
    background-color: grey;
    }
    """)

x = QPushButton(oyna)
x.setText('x')
x.setGeometry(270, 295, 70, 70)
x.setStyleSheet("""
    QPushButton {
    color: white;
    background-color: #FF9F0C;
    border-radius: 35px;
    }
    QPushButton:pressed {
    background-color: grey;
    }
    """)


# 3-qator
    

tort = QPushButton(oyna)
tort.setText("4")
tort.setGeometry(15, 380, 70, 70)
tort.setStyleSheet("""
    QPushButton {
    color: white;
    background-color: #343434;
    border-radius: 35px;
    }
    QPushButton:pressed {
    background-color: grey;
    }
""")

besh = QPushButton(oyna)
besh.setText("5")
besh.setGeometry(100, 380, 70, 70)
besh.setStyleSheet("""
    QPushButton {
    color: white;
    background-color: #343434;
    border-radius: 35px;
    }
    QPushButton:pressed {
    background-color: grey;
    }
    """)

olti = QPushButton(oyna)
olti.setText('6')
olti.setGeometry(185, 380, 70, 70)
olti.setStyleSheet("""
    QPushButton {
    color: white;
    background-color: #343434;
    border-radius: 35px;
    }
    QPushButton:pressed {
    background-color: grey;
    }
    """)

ayirish = QPushButton(oyna)
ayirish.setText('-')
ayirish.setGeometry(270, 380, 70, 70)
ayirish.setStyleSheet("""
    QPushButton {
    color: white;
    background-color: #FF9F0C;
    border-radius: 35px;
    }
    QPushButton:pressed {
    background-color: grey;
    }
    """)

# 4-qator

bir = QPushButton(oyna)
bir.setText("1")
bir.setGeometry(15, 465, 70, 70)
bir.setStyleSheet("""
    QPushButton {
    color: white;
    background-color: #343434;
    border-radius: 35px;
    }
    QPushButton:pressed {
    background-color: grey;
    }
""")

ikki = QPushButton(oyna)
ikki.setText("2")
ikki.setGeometry(100, 465, 70, 70)
ikki.setStyleSheet("""
    QPushButton {
    color: white;
    background-color: #343434;
    border-radius: 35px;
    }
    QPushButton:pressed {
    background-color: grey;
    }
    """)

uch = QPushButton(oyna)
uch.setText('3')
uch.setGeometry(185, 465, 70, 70)
uch.setStyleSheet("""
    QPushButton {
    color: white;
    background-color: #343434;
    border-radius: 35px;
    }
    QPushButton:pressed {
    background-color: grey;
    }
    """)

plus = QPushButton(oyna)
plus.setText('+')
plus.setGeometry(270, 465, 70, 70)
plus.setStyleSheet("""
    QPushButton {
    color: white;
    background-color: #FF9F0C;
    border-radius: 35px;
    }
    QPushButton:pressed {
    background-color: grey;
    }
    """)

# 5-qator


nol = QPushButton(oyna)
nol.setText("0")
nol.setGeometry(15, 550, 155, 70)
nol.setStyleSheet("""
    QPushButton {
    color: white;
    background-color: #343434;
    border-radius: 35px;
    }
    QPushButton:pressed {
    background-color: grey;
    }
""")

vergul = QPushButton(oyna)
vergul.setText(',')
vergul.setGeometry(185, 550, 70, 70)
vergul.setStyleSheet("""
    QPushButton {
    color: white;
    background-color: #343434;
    border-radius: 35px;
    }
    QPushButton:pressed {
    background-color: grey;
    }
    """)

tenglik = QPushButton(oyna)
tenglik.setText('=')
tenglik.setGeometry(270, 550, 70, 70)
tenglik.setStyleSheet("""
    QPushButton {
    color: white;
    background-color: #FF9F0C;
    border-radius: 35px;
    }
    QPushButton:pressed {
    background-color: grey;
    }
    """)

class Chiqarish:
    
    def chiq(self):
        global son
        output.setText('--')

    def son0(self):
        global son
        if son != '0':
            son += "0"
        output.setText(son)
   	
    def son1(self):
        global son
        if son == '0':
            son = ""
        son += "1"
        output.setText(son)
    
    def son2(self):
        global son
        if son == '0':
            son = ''
        son += "2"
        output.setText(son)

    def son3(self):
        global son
        if son == '0':
            son = ''
        son += "3"
        output.setText(son)
        
    def son4(self):
        global son
        if son == '0':
            son = ''
        son += "4"
        output.setText(son)
    
    def son5(self):
        global son
        son += "5"
        if son == '0':
            son = ''
        output.setText(son)
    
    def son6(self):
        global son
        if son == '0':
            son = ''
        son += "6"
        output.setText(son)
    
    def son7(self):
        global son
        if son == '0':
            son = ''
        son += "7"
        output.setText(son)
    
    def son8(self):
        global son
        if son == '0':
            son = ''
        son += "8"
        output.setText(son)
    
    def son9(self):
        global son
        if son == '0':
            son = ''
        son += "9"
        output.setText(son)
    
    def plus(self):
        global son
        son += '+'
        output.setText(son)
    
    def minus(self):
        global son
        son += '-'
        output.setText(son)

    def multi(self):
        global son
        son += '*'
        output.setText(son)
    
    def divid(self):
        global son
        son += '÷'
        output.setText(son)
    
    def null(self):
        global son
        son = '0'
        output.setText(son)
        
    def backspace(self):
        global son
        if len(son) == 1:
            son = '0'
        else:
            son = son[:-1]
        output.setText(son)
        
    def percent(self):
        global son
        son += '%'
        output.setText(son)
    
    def comma(self):
        global son
        son += ','
        output.setText(son)
        
    def equal(self):
        global son
        while not son[-1].isdigit():
            son = son[:-1]
        try:
            if ',' in son:
                son = son.replace(',', '.')
            if '%' in son:
                son = son.replace('%', '/100*')
            if '÷' in son:
                son = son.replace('÷', '/')
            if eval(son) % 1 == 0:
                son = str(int(eval(son)))
            else:
                son = str(eval(son))
            if '.' in son:
                son = son.replace('.', ',')
            output.setText(son)
        except:
            output.setText("Error!")
            son = '0'
            


c = Chiqarish()
tenglik.clicked.connect(c.equal)
plus.clicked.connect(c.plus)
ayirish.clicked.connect(c.minus)
x.clicked.connect(c.multi)
boluv.clicked.connect(c.divid)
foiz.clicked.connect(c.percent)
vergul.clicked.connect(c.comma)
backspace.clicked.connect(c.backspace)
ochirish.clicked.connect(c.null)
# sonlar
nol.clicked.connect(c.son0)
bir.clicked.connect(c.son1)
ikki.clicked.connect(c.son2)
uch.clicked.connect(c.son3)
tort.clicked.connect(c.son4)
besh.clicked.connect(c.son5)
olti.clicked.connect(c.son6)
yetti.clicked.connect(c.son7)
sakkiz.clicked.connect(c.son8)
toqqiz.clicked.connect(c.son9)

oyna.show()
app.exec_()