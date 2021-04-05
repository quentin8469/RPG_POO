from .Class_perso import Personne


class Guerrier(Personne):
    """
    Classe qui definie un guerrier, classe fille de 'Personne'
    """

    def __init__(self, att_epee):
        """ initialisation d'un guerrier"""
        self.att_epee = 10


def main():
    """ doc"""
    return


if __name__ == "__main__":
    main()
