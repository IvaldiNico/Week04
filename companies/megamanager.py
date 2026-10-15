# Posso creare degli alberi di ereditarietà,
# con classi che estendono classi che, a loro
# volta, sono già estensione di altre classi

from companies.ilmiomanager import Manager

class MegaManager(Manager):
    def __init__(self, name, wage, managedUnit, megaAttr):
        # Prima inizializzo la parte Manager dell'Employee
        super().__init__(name, wage, managedUnit)
        # Poi inizializzo la parte specifica
        self.__megaAttr = megaAttr
