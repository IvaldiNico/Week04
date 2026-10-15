class Car:
    def __init__(self, licensePlate, color, turnedOn):
        self.licensePlate = licensePlate
        self.color = color
        self.turnedOn = turnedOn

    def __str__(self):
        return f'{self.licensePlate} {self.color} {self.turnedOn}'