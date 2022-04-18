import csv

class Manejador:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def inicializarLista(self):
        archivo=open("Emails.csv")
