from Email import Email
from ManejadorEmail import Manejador
def mostrarMensaje(nom, email):
    print("Estimado " +nom+" enviaremos sus mensajes a "+ email.metodoRetornaEmail())
def crearCuentaNueva(nuevoEmail):
    correo=input("Ingrese una nueva direccion de correo electronico")
    nuevoEmail.crearCuenta(correo)

def prueba ():
    nombre=str(input("Ingrese su nombre "))
    id=input("Ingresar ID de correo")
    dominio=input("Ingrese dominio de la cuenta")
    tipo=input("Ingrese el tipo de dominio")
    contr=input("Ingrese la contraseña")
    otroEmail=Email()
    otroEmail.inicalizar(id,dominio,tipo,contr)
    mostrarMensaje(nombre,otroEmail)
    otroEmail.modificarContraseña()
    nuevoEmail=Email()
    crearCuentaNueva(nuevoEmail)
    unaLista=Manejador()
    unaLista.listarLibros()
    unaLista.mostrar()
    iden=input("ingrese indentidicador de email")
    unaLista.buscarIdentificador(iden)
if __name__ == '__main__':
    prueba()
