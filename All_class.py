import random


class Personne:
    """
    def de la class perso general
    """

    def __init__(self, name, pdv, force, intel, attaque, defense, mana):
        """ initialisation d'une personne """
        self.name = name
        self.pdv = pdv
        self.force = force
        self.intel = intel
        self.attaque = attaque
        self.defense = defense
        self.mana = mana

    def presentation(self):
        """ presentation du nouveau personnage"""
        print(
            f"Nom: {self.name}, Points de vie: {self.pdv}, Force: {self.force}, Intelligence: {self.intel},\
 Attaque: {self.attaque}, Defense: {self.defense}, Mana: {self.mana}"
        )
    

class Guerrier(Personne):
    """
    Classe qui definie un guerrier, classe fille de 'Personne'
    """

    def __init__(self, name):
        """ initialisation d'un guerrier"""
        super().__init__(
            name,
            random.randrange(150, 250),
            random.randrange(15, 25),
            random.randrange(10, 15),
            random.randrange(100, 150),
            random.randrange(100, 150),
            random.randrange(10, 20),
        )


class Mage(Personne):
    """
    Classe qui definie un Mage, classe fille de 'Personne'
    """

    def __init__(self, name):
        """ initialisation d'un Mage"""
        super().__init__(
            name,
            random.randrange(100, 150),
            random.randrange(10, 15),
            random.randrange(15, 25),
            random.randrange(10, 15),
            random.randrange(100, 150),
            random.randrange(150, 250),
        )


def main():
    """ doc """

    guerrier_01 = Guerrier("Bryan")
    mage_01 = Mage("jojo")

    return guerrier_01.presentation(), mage_01.presentation()


if __name__ == "__main__":
    main()
