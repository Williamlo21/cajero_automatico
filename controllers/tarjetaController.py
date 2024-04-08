from models.tarjeta import Tarjeta
from controllers.transaccionController import TransaccionController
import random
class TarjetaController():
    @staticmethod
    def insertarTarjeta():
        print("***********************************")
        print("...")
        tarjeta = input("Por favor inserte su tarjeta: ")
        tarjetaExiste = Tarjeta()
        confirmarTarjeta = tarjetaExiste.existeTarjeta(tarjeta)
        if confirmarTarjeta:
            claveTarjeta = str(confirmarTarjeta[6])
            clave = input("Ingrese la clave: ")
            if clave == claveTarjeta:
            
                return confirmarTarjeta
            else:
                print("Clave invalida.")
        
    @staticmethod
    def codigoMensaje():
        print("***********************************")
        print("...")
        numero_aleatorio = random.randint(100000, 999999)
        print("***************************************")
        print("*** Mensaje enviado por SMS: "+ str(numero_aleatorio) + " ***")
        print("***************************************")
        numeroMensaje = input("Digite código de verificación: ")
        numeroMensaje = int(numeroMensaje)
        if numero_aleatorio == numeroMensaje:
            return True
        else:
            print("***********************************")
            print("...")
            print("Código de verificación errado.")
            print("Por favor intente nuevamente.")
    # @staticmethod
    