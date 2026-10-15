from persona import Persona
# Per dire che la classe Docente EREDITA da Persona
# devo inserire il nome della classe tra ( )

class Docente (Persona):
    def __init__(self, nome, cognome, dipartimento): # Il costruttore riceve i parametri per inizializzare
                                                     # gli attributi dell'Employee, ed anche del Manager

        # SBAGLIATO RIPETERE LA DEFINIZIONE DI ATTRIBUTI DEL PADRE
        # self.__nome = nome
        # self.__cognome = cognome

        super().__init__(nome, cognome) # Costruisce "la parte" Persona del Docente

        # Poi si vanno ad inizializzare gli attributi specifici del Docente
        self.dipartimento = dipartimento


    def __str__(self):
        #return f"{self.__nome} {self.__cognome} {self.dipartimento}"
        return f"{super().__str__()} {self.dipartimento}"