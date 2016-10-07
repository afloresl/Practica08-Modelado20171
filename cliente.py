import sys
from PyQt4 import QtGui, uic

class Ventana(QtGui.QMainWindow):
    def __init__(self):
        super(Ventana, self).__init__()
        uic.loadUi('cliente.ui', self)
        self.resizeTable()
        self.show()

    def resizeTable(self):
    	self.TablaCliente.horizontalHeader().setStretchLastSection(True)
    	self.TablaCliente.verticalHeader().setStretchLastSection(True)
    	self.TablaCliente.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
    	self.TablaCliente.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    empieza = Ventana()
    sys.exit(app.exec_())
