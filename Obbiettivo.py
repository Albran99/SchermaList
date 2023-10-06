class Obbiettivo:
    def __init__(self, name, difficolta, stress, parti):
        self.name = name
        self.difficolta = difficolta
        self.stress = stress
        self.parti = parti

    def __str__(self):
        return ("\tName: " + self.name + "\n\tDifficoltà: " + str(self.difficolta) + "\n\tStress: " + str(self.stress) +
                "\n\tParti: [" + self.printParti() + "]")

    def printParti(self):
        return ', '.join(self.parti)
