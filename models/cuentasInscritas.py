from database.conexionDB import Conexion
class CuentaInscrita():

    @staticmethod
    def consultarCuentasInscritas(cuentaOrigen):
        cuentaOrigenId = cuentaOrigen[0]
        conexion = Conexion()
        mycursor = conexion.mycursor
        mycursor.execute("SELECT cuenta_bancaria_inscrita.id, cuenta_bancaria_inscrita.numero_cuenta, \
                        cuenta_bancaria_inscrita.tipo_cuenta,  \
                        usuarios.nombres, \
                        usuarios.apellidos \
                        FROM cuentas_inscritas \
                        JOIN cuenta_bancaria ON cuenta_bancaria.id = cuentas_inscritas.cuenta_bancaria_id \
                        JOIN cuenta_bancaria AS cuenta_bancaria_inscrita ON cuenta_bancaria_inscrita.id = cuentas_inscritas.cuenta_bancaria_inscrita_id \
                        JOIN usuarios ON usuarios.id = cuenta_bancaria_inscrita.user_titular_id\
                        WHERE cuentas_inscritas.cuenta_bancaria_id = %s", (cuentaOrigenId,))
        resultado = mycursor.fetchall()
        if resultado:
            return resultado
        else:
            print("***********************************")
            print("...")
            print("No hay cuentas inscritas")