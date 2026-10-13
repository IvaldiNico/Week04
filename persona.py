# Uso Persona come classe di base, da cui derivo es. la classe Docente

class Persona:

    def __init__(self, nome, cognome):
        self.__nome = nome # Attributi/Variabili di istanza
        self.__cognome = cognome

    def __str__(self):
        return f"{self.__nome} {self.__cognome}"




