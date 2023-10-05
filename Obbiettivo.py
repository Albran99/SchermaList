class Obbiettivo:
    def __init__(self, name, difficolta, stress, parti):
        self.name = name
        self.difficolta = difficolta
        self.stress = stress
        self.parti = parti

    def __str__(self):
        return ("name " + self.name + "\ndifficoltà " + str(self.difficolta) + "\nstress " + str(self.stress) +
                "\nparti [" + self.printParti() + "]")

    def printParti(self):
        return ', '.join(self.parti)
