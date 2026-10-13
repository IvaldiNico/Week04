from employee import Employee

class Manager(Employee): # Classe che deriva da Employee
    def __init__(self, name, wage, managedUnit):

        # Prima istruzione del costruttore di una classe
        # figlia è l'invocazione della costruzione del padre
        # in virtù dell'approccio "a cipolla" super().__init()__
        super().__init__(name, wage)
        self.__managedUnit = managedUnit

    # Con la OOP posso andare a ridefinire i metodi che
    # non mi piacciano del padre, andando a specificare
    # comportamenti specializzati nel figlio

    # Ad esempio, il metodo __str()__ se voglio che il Manager
    # si descriva in modo diverso da come fa L'Employee

    # Se gli attributi dell'Employee sono privati, non posso che
    # usare il metodo __str()__ fornito dall'Employee per
    # inserire nella stringa "la parte" Employee del Manager ...

    def __str__(self):
        return f"{super().__str__()} {self.__managedUnit}" # ... a cui poi concateno la __managednUnit

    # I metodi ridefiniti nei figli con lo stesso nome del padre
    # si dicono in OVERRIDING (è una forma di POLIMOSRFIMO di Python)

    def increment_wage(self):
        self.wage+=10000 # Per il Manager incremento di una quantità maggiore rispetto all'Employee