class Employee:
    def __init__(self, name, wage):
        self.__name = name
        self.__wage = wage

    @property
    def wage(self):
        return self.__wage

    @wage.setter
    def wage(self, wage):
        self.__wage = wage

    def __str__(self):
        return f"{self.__name} {self.__wage}"

    def increment_wage(self):
        self.__wage += 5000

