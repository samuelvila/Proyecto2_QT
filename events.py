import var,sys, clients

class Eventos():
    #Eventos Generales

    def Salir(self):
        try:
            sys.exit()
        except Exception as error:
            print('El error es %s' % str(error))

    def comprobar_dni(dni):
        try:
            clients.Clientes.validarDNI(dni)
        except Exception as error:
            print('El error es %s' % str(error))





