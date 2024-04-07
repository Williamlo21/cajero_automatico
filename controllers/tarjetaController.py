from models.tarjeta import Tarjeta
from controllers.transaccionController import TransaccionController
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
            
                seleccionarMonto = TransaccionController()
                seleccionarMonto.seleccionaMonto(confirmarTarjeta)
            else:
                print("Clave invalida.")