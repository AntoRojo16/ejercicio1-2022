class Email:
    __idCuenta=""
    __Dominio=""
    __TipoDominio=""
    __Contraseña=""


    def inicalizar (self, id,dominio,tipo,cont):
        self.__idCuenta=id
        self.__Dominio=dominio
        self.__TipoDominio= tipo
        self.__Contraseña= cont


    def metodoRetornaEmail(self):
        return self.__idCuenta+"@"+self.__Dominio+"."+self.__TipoDominio
    
    def __str__(self):
        return ("Id del correo: >>{} Domino del correo >>{} Tipode dominio >>{} Contraseña >>{}".format(self.__idCuenta,self.__Dominio,self.__TipoDominio,self.__Contraseña))

    def getDominio(self):
        return self.__Dominio

    def getContraseña(self):
        return self.__Contraseña

    def crearCuenta(self, correo,cont="hola"):
        arregl= correo.split(sep="@")
        arreglo2= arregl[1].split('.')
        self.__idCuenta=arregl[0]
        self.__Dominio= arreglo2[0]
        self.__TipoDominio=arreglo2[1]
        self.__Contraseña=cont

    def modificarContraseña(self):
        print("Se modificiara la contraseña")
        cont=input("Ingrese la contraseña")
        if(cont==self.__Contraseña):
            cont=input(" se puede modificar la contraseña, ingrese nueva contraseña ")
            self.__Contraseña=cont
        else: print("No se puede cambiar la contraseña")

    def getId (self):
        return self.__idCuenta

            
