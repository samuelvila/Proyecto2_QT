from ventana import *
import sys, var, events, clients

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_VenPrincipal()
        var.ui.setupUi(self)

        #Código de conexión de los eventros
        '''
        Botones
        '''
        #var.ui.btnAceptar.clicked.connect(events.Eventos.Saludo)
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)
        var.ui.btnAceptar.clicked.connect()
        '''
        Controles del menubar
        '''


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())