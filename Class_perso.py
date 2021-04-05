class Personne:
    """
    def de la class perso general
    """

    def __init__(self, name, pdv, force, intel):
        """ initialisation d'une personne """
        self.name = name
        self.pdv = pdv
        self.force = force
        self.intel = intel
        self.attaque = 10
        self.defense = 10
        self.mana = 10


def main():
    """ doc"""
    perso = Personne(
        "polo",
        100,
        12,
        14,
    )
    # print("Nom:" + {}, "pdv:" + {}.format(perso.name, perso.pdv))
    # f"{perso.name}, {perso.pdv}, {perso.force}, {perso.intel}"
    return print(
        f"Nom: {perso.name}, Points de vie: {perso.pdv}, Force: {perso.force}, Intelligence: {perso.intel}, Attaque: {perso.attaque}, Defense: {perso.defense}, Mana: {perso.mana}"
    )


if __name__ == "__main__":
    main()
