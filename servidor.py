import sys
from PyQt4 import QtGui, QtCore, uic

class Ventana(QtGui.QMainWindow):
    def __init__(self):
        super(Ventana, self).__init__()
        uic.loadUi('servidor.ui', self)
        self.resizeTable()
        self.show()

    def resizeTable(self):
        self.TablaServidor.verticalHeader().setStretchLastSection(True)
    	self.TablaServidor.horizontalHeader().setStretchLastSection(True)
        self.TablaServidor.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
    	self.TablaServidor.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    empieza = Ventana()
    sys.exit(app.exec_())
