import csv
from Email import Email
class Manejador:
    def __init__(self):
        self.__Lemail=[]

    def AgregarEmail (self,email):
        self.__Lemail.append(email)
    def listarLibros(self):
        archivo=open("Emails.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera= True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                correo=fila[0]
                contraseña=fila[1]
                unEmail=Email()
                unEmail.crearCuenta(correo,contraseña)
                self.AgregarEmail(unEmail)

        archivo.close()

    def mostrar(self):
        for email in self.__Lemail:
            print(email)

    def buscarIdentificador(self,iden):
        cont=0
        for email in self.__Lemail:
            if email.getId()==iden:
                cont+=1

        if cont>1:
            print("el Identificador si se repite")

