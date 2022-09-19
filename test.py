# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic
import sys

def on_clicked():
    print("Кнопка нажата. Функция on_clicked()")

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi("main_.ui", self)
        self.pshBttnQuit.clicked.connect(QtWidgets.qApp.quit)
        self.pshBttnReadPath.clicked.connect(self.clickReadPath)

    def clickReadPath(self):
        print('Your name: ' + self.lnEditPath.text())
        self.lineEdit_2.setText(self.lnEditPath.text())

'''
app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("main_.ui")
window.pshBttnQuit.clicked.connect(app.quit)
window.show()
sys.exit(app.exec_())
'''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())