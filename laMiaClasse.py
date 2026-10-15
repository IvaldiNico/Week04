import operator

class LaMiaClasse():
    def __init__(self, attributo):
        self.attributo = attributo

    def __str__(self):
        return f"{self.attributo}"

    def __repr__(self):
        # return f"{type(self)} {self.attributo}"
        return f"{self.__class__.__name__} attributo={self.attributo}"

    # Posso ridefinire il metodo __eq()__ che è
    # il metodo di confronto (in override), andando
    # a scrivere al suo interno l'alg. di confronto
    def __eq__(self, otherObject):
        if self.attributo == otherObject.attributo:
            return True
        else:
            return False

o1 = LaMiaClasse("Pippo")

print("Stampa dell'oggetto con __str()__")
print(str(o1)) # __ str__()

print()
print("Stampa dell'oggetto con __repr__()")
print(o1.__repr__())

o2 = LaMiaClasse("Topolino")

print("\n---------- Confronto tra oggetti ------------")

# Come faccio a confrontare due oggetti o1 ed o2
if o1 == o2:   # o1.__eq__(o2) per confronto con ==
    print("Uguali")
else:
    print("Diversi")


print("\n---------- Ordinamento lista di oggetti ------------")

lista = [o1]
lista.append(o2)
lista.append(LaMiaClasse("Gastone"))

print("Lista prima dell'ordinamento:")
print(lista)

print("\nLista dopo dell'ordinamento:")

lista.sort(key=operator.attrgetter("attributo"))
print(lista)

#listaOrdinata = sorted(lista, key=operator.attrgetter("attributo"))
#print(listaOrdinata)


