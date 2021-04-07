import random

class Mage(Personne):
    """
    Classe qui definie un Mage, classe fille de 'Personne'
    """

    def __init__(self, name):
        """ initialisation d'un Mage"""
        Personne.__init__(
            self,
            name,
            random.randrange(100, 150),
            random.randrange(10, 15),
            random.randrange(15, 25),
            random.randrange(10, 15),
            random.randrange(100, 150),
            random.randrange(150, 250),
        )

    def degats(self):
        """ fonction attaque """
        degats = self.mana + self.intel
        return degats

    def protections(self):
        """ fonction protection"""
        protec = self.defense + self.intel
        return protec

    def Boule_de_feu(self):
        """ lance boule de feu """
        return
