import random


class Personne:
    """
    def de la class perso general
    """

    def __init__(self, name, prof, pdv, force, intel, attaque, defense, mana):
        """ initialisation d'une personne """

        self.name = name
        self.prof = prof
        self.pdv = pdv + random.randrange(2000, 5000)
        self.force = force + random.randrange(5, 10)
        self.intel = intel + random.randrange(5, 10)
        self.attaque = attaque + random.randrange(10, 50)
        self.defense = defense + random.randrange(10, 50)
        self.mana = mana + random.randrange(50, 100)
        self.intiative = random.randrange(1, 10)
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
        else:
            return self.force

    def protections(self):
        """ fonction protection"""
        if self.prof == "Guerrier":
            protec = self.defense + self.force
            return protec
        if self.prof == "Mage":
            protec = self.defense + self.intel
            return protec
        else:
            return " néant"


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

        if self.joueur1 > self.joueur2:
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
        if self.joueur1.intiative == self.joueur2.intiative:
            self.joueur1.intiative = random.randrange(1, 10)
            self.joueur2.intiative = random.randrange(1, 10)

        while self.joueur1.pdv > 0 and self.joueur2.pdv > 0:

            if self.joueur1.intiative > self.joueur2.intiative:
                self.joueur2.pdv = self.joueur2.pdv - self.joueur1.degat
                if self.joueur2.pdv < 0:
                    print(
                        f"{self.joueur1.name} d'un coup d'une violence terrible tranche la tete de {self.joueur2.name}"
                    )
                else:
                    print(
                        f"{self.joueur1.name} fait {self.joueur1.degat} de dégats à {self.joueur2.name} qui se protege de {self.joueur2.protection} et prend {self.joueur1.degat} de dégats , il lui reste {self.joueur2.pdv} point de vie"
                    )
            elif self.joueur2.intiative > self.joueur1.intiative:
                self.joueur1.pdv = self.joueur1.pdv - self.joueur2.degat
                if self.joueur1.pdv < 0:
                    print(
                        f"Le terrible coup de {self.joueur2.name} arrache son dernier souffle à {self.joueur1.name}"
                    )
                else:
                    print(
                        f"{self.joueur2.name} fait {self.joueur2.degat} de dégats à {self.joueur1.name} qui se protege de {self.joueur1.protection} et prend {self.joueur2.degat} de dégats , il lui reste {self.joueur1.pdv} point de vie"
                    )
        print("Le combat est fini")


def main():
    """ doc """
    return


if __name__ == "__main__":
    print("Nos combattants et leurs statistiques")
    # paysan = Personne("pelo", "Paysan", 0, 0, 0, 0, 0, 0)
    guerrier = Guerrier("Bryan")
    mage = Mage("Jojo")
    # paysan.presentation()
    guerrier.presentation()
    mage.presentation()
    debut = Tournoi()
    debut.entre_dans_arene(mage, guerrier)
    debut.debut_du_combat()
    debut.bagarre()
