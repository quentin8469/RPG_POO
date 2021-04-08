import random


class Personne:
    """
    def de la class perso general
    """

    def __init__(self, name, prof, pdv, force, intel, attaque, defense, mana):
        """ initialisation d'une personne """

        self.name = name
        self.prof = prof
        self.pdv = pdv + random.randrange(50, 100)
        self.force = force + random.randrange(5, 10)
        self.intel = intel + random.randrange(5, 10)
        self.attaque = attaque + random.randrange(10, 50)
        self.defense = defense + random.randrange(10, 50)
        self.mana = mana + random.randrange(50, 100)
        self.degat = self.degats()
        self.protection = self.protections()

    def presentation(self):
        """ presentation du nouveau personnage"""
        print(
            f"Nom: {self.name}, Classe: {self.prof}, Points de vie: {self.pdv}, Force: {self.force}, Intelligence: {self.intel},\
 Attaque: {self.attaque}, Defense: {self.defense}, Mana: {self.mana}, Dégats: {self.degat}, Protection:{self.protection}"
        )

    def degats(self):
        """ docstring"""
        if self.prof == "Guerrier":
            degats = self.attaque + self.force
            return degats
        if self.prof == "Mage":
            degats = self.mana + self.intel
            return degats

    def protections(self):
        """ fonction protection"""
        if self.prof == "Guerrier":
            protec = self.defense + self.force
            return protec
        if self.prof == "Mage":
            protec = self.defense + self.intel
            return protec


class Guerrier(Personne):
    """
    Classe qui definie un guerrier, classe fille de 'Personne'
    """

    def __init__(self, name):
        """ initialisation d'un guerrier"""
        Personne.__init__(
            self,
            name,
            "Guerrier",
            200,
            10,
            5,
            150,
            150,
            10,
        )


class Mage(Personne):
    """
    Classe qui definie un Mage, classe fille de 'Personne'
    """

    def __init__(self, name):
        """ initialisation d'un Mage"""
        Personne.__init__(
            self,
            name,
            "Mage",
            100,
            5,
            10,
            15,
            50,
            200,
        )


class Tournoi:
    """
    def class tournoi pour affrontements
    """

    def __init__(self):
        """ initialisation du tournoi """
        pass

    def entre_dans_arene(self, joueur1, joueur2):
        """ debut du combat """
        self.joueur1 = joueur1
        self.joueur2 = joueur2

        return print(
            f"les combattants {self.joueur1.name} et {self.joueur2.name} sont entrés dans l'arene pret à s'affronter"
        )

    def calcul_initiative(self):
        """ definition de l'initiative """
        self.init_joueur1 = random.randrange(1, 10)
        self.init_joueur2 = random.randrange(1, 10)

        if self.init_joueur1 > self.init_joueur2:
            return print(
                f"{self.joueur1.name} attaque en premier avec une init de {self.init_joueur1}"
            )
        else:
            return print(
                f"Joueur {self.joueur2.name} attaque en premier avec une init de {self.init_joueur2}"
            )

    def debut_du_combat(self):
        """ on fait la bagarre """
        if self.joueur1.pdv > 0 and self.joueur2.pdv > 0:
            return print(
                f"{self.joueur1.name} et {self.joueur2.name} se font face pret a se battre pour leur vie"
            )

    def bagarre(self):
        """ docstring """


def main():
    """ doc """
    print("Nos combattants et leurs statistiques")
    paysan = Personne("pelo", "Paysan", 0, 0, 0, 0, 0, 0)
    guerrier_01 = Guerrier("Bryan")
    mage_01 = Mage("Jojo")
    debut_du_tournoi = Tournoi()

    return (
        paysan.presentation(),
        guerrier_01.presentation(),
        mage_01.presentation(),
        debut_du_tournoi.entre_dans_arene(mage_01, guerrier_01),
        debut_du_tournoi.calcul_initiative(),
        debut_du_tournoi.debut_du_combat(),
    )


if __name__ == "__main__":
    main()
