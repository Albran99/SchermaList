import Obbiettivo as obj
class Attivita:
    def __init__(self, nome, categoria, difficolta_media, stress_medio, persone_min, persone_max, obbiettvi, descrione):
        self.nome = nome
        self.categoria=categoria
        self.difficolta_media = difficolta_media
        self.stress_medio = stress_medio
        self.persone_min = persone_min
        self.persone_max = persone_max
        self.obbiettivi = obbiettvi
        self.descrizione = descrione


    def __str__(self):
        string = ''
        for obb in self.obbiettivi:
            string += obb.__str__()
            string += '\n--------------------\n'
        return ("Nome: " + self.nome + "\nCategoria: [" + ', '.join(self.categoria) + "]\nDifficoltà media: "
                + str(self.difficolta_media) + "\nStress medio: " + str(self.stress_medio) + "\nPersone min: "
                + str(self.persone_min) + "\nPersone max: " + str(self.persone_max) + "\nObbiettivi:\n" +
                string + "\nDescrizione: " + self.descrizione)

