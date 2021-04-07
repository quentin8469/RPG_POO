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
        self.degat = self.degats()
        self.protection = self.protections()

    def presentation(self):
        """ presentation du nouveau personnage"""
        print(
            f"Nom: {self.name}, Points de vie: {self.pdv}, Force: {self.force}, Intelligence: {self.intel},\
 Attaque: {self.attaque}, Defense: {self.defense}, Mana: {self.mana}, Dégats: {self.degat}, Protection:{self.protection}"
        )
