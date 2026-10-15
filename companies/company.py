# Applicazione che uso per creare oggetti di classe Employee, Manager, ...
from employee import Employee
from ilmiomanager import Manager
from car import Car

print("Stampo un Employee")
e1 = Employee("Mr. Bean", 15000)
print(e1)

print("Stampo un Manager")
m = Manager("B. Boss", 40000, "HR")

# Se in Manager non ho ridefinito il metodo __str()__, questi verrà
# stampato come un Employee (quindi solo con name e wage)

# Se però in Manager c'è una versione del metodo __str()__ in OVERRIDING, allora
# questi verrà stampato anche con managedUnit (se così quel metodo è stato definito)
print(m)

# Idem per l'incremento della paga, se voglio che Studente e Manager, pur
# invocando lo stesso metodo, si COMPORTINO diversamente (POLIMORFISMO)

print("----Incremento della paga----")
e1.increment_wage()
print(e1) # Per l'Employee la paga crescerà di 5000
m.increment_wage()
print(m) # Per il Manager di 10000, se così definiscono i due metodi

# Le strutture dati di Python sono così versatili che posso memorizzare
# al loro interno dati di tipo diverso (int, float, str, list, ...)

print("**** Struttura dati ****")
users = []
users.append(e1)
users.append(m)
users.append("abcefg")
users.append(35)
car1 = Car("AB123CD", "Red", "False")
users.append(car1) # Posso memorizzare di tutto, in quanto la lista memorizza
                   # in effetti degli oggetti, e Python tratta tutti questi
                   # tipi di dato, anche quelli più semplici, come oggetti


# E quando vado a scandire il contenitore e, su ciascun elemento della
# lista chiamo il metodo str(), ovvero __str()__, Python va a chiamare
# il metodo definito per/in ciascuno di quegli oggetti (se disponibile)
for user in users:
    print(f"{str(user)} {type(user)}")

# Esempio, se in Car il metodo __str()__ non è definito, quando
# stampato verrà mostrato nella console il riferimento in memoria

if isinstance(e1, Employee) is True:
    print("e1 è un Employee")
else:
    print("e1 non è un Employee")

