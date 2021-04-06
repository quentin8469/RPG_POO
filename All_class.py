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
        self.degat = self.degats()
        self.protection = self.protections()

    def presentation(self):
        """ presentation du nouveau personnage"""
        print(
            f"Nom: {self.name}, Points de vie: {self.pdv}, Force: {self.force}, Intelligence: {self.intel},\
 Attaque: {self.attaque}, Defense: {self.defense}, Mana: {self.mana}, Dégats: {self.degat}, Protection:{self.protection}"
        )


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


class Tournoi:
    """
    def class tournoi pour affrontements
    """

    def __init__(self):
        """ initialisation du tournoi """
        self.joueur1 = False
        self.joueur2 = False

    def entre_dans_arene(self, joueur1, joueur2):
        """ debut du combat """
        self.joueur1 = joueur1
        self.joueur2 = joueur2

        return print("les joueurs sont entrés dans l'arene pret à s'affronter")

    def calcul_initiative(self):
        """ definition de l'initiative """
        self.init_joueur1 = random.randrange(1, 10)
        self.init_joueur2 = random.randrange(1, 10)

        if self.init_joueur1 > self.init_joueur2:
            return print(
                f"Joueur 1 attaque en premier avec une init de {self.init_joueur1}"
            )
        else:
            return print(
                f"Joueur 2 attaque en premier avec une init de {self.init_joueur2}"
            )

    def debut_combat(self):
        """ on fait la bagarre """

        return


def main():
    """ doc """

    guerrier_01 = Guerrier("Bryan")
    mage_01 = Mage("jojo")
    bagarre = Tournoi()

    return (
        guerrier_01.presentation(),
        mage_01.presentation(),
        bagarre.entre_dans_arene(mage_01, guerrier_01),
        bagarre.calcul_initiative(),
    )


if __name__ == "__main__":
    main()
