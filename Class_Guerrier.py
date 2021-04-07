import random
from .Class_perso import Personne


class Guerrier(Personne):
    """
    Classe qui definie un guerrier, classe fille de 'Personne'
    """

    def __init__(self, name):
        """ initialisation d'un guerrier"""
        Personne.__init__(
            self,
            name,
            random.randrange(150, 250),
            random.randrange(15, 25),
            random.randrange(10, 15),
            random.randrange(100, 150),
            random.randrange(100, 150),
            random.randrange(10, 20),
        )

    def degats(self):
        """ fonction attaque """
        degats = self.attaque + self.force
        return degats

    def protections(self):
        """ fonction protection"""
        protec = self.defense + self.force
        return protec

    def sword(self):
        """ coup d'épée """
        return

def main():
    """ doc"""
    return


if __name__ == "__main__":
    main()
