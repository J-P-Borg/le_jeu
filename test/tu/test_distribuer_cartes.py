import pytest

from model.JoueurModel import Joueur
from model.PartieModel import Partie


def test_taille_main():
    """
    Vérifie que la variable taille main est correctement définie
    :return:
    """
    aux = [(1, 8), (2, 7), (3, 6), (4, 6), (5, 6)]
    for nb_joueur, taille_main in aux:
        partie = Partie(nb_joueur)
        assert partie.taille_main == taille_main


def test_distribution_cartes():
    """
    Test que les cartes sont bien distribuées dans le cas ou il y a assez de cartes dans le sabot
    Test pour un id de joueur correct
    :return:
    """
    for nb_joueur in range(1, 6):
        for id_joueur in range(nb_joueur):
            partie = Partie(nb_joueur)
            partie.sabot = list(range(10))
            partie.list_joueur[id_joueur].main = []
            partie.list_joueur[id_joueur].complete_main()
            assert partie.sabot + list(partie.list_joueur[id_joueur].main) == list(range(10))


def test_main_est_triee():
    """
    Vérifie que la main d'un joueur est triée en permanance
    :return:
    """
    partie = Partie(1)
    partie.sabot = [10, 11, 15, 28, 24, 3, 2, 5, 4, 7, 6, ]
    joueur: Joueur = partie.list_joueur[0]
    joueur.main = []
    joueur.complete_main()
    assert partie.list_joueur[0].main == [2, 3, 4, 5, 6, 7, 24, 28]
    joueur.jouer_carte(numero_carte=6, montante=True, id_pile=0)
    assert partie.list_joueur[0].main == [2, 3, 4, 5, 7, 24, 28]
    joueur.complete_main()
    assert partie.list_joueur[0].main == [2, 3, 4, 5, 7, 15, 24, 28]


def test_distribution_sabot_vide():
    """
    Vérifie que la distribution fonctionnne correctement si le sabot n'a plus assez de cartes
    (Arrive en fin de partie)
    :return:
    """
    partie = Partie(3)
    partie.sabot = list(range(4))
    partie.list_joueur[1].main = []
    partie.list_joueur[1].complete_main()
    assert partie.sabot == []
    assert partie.list_joueur[1].main == list(range(4))
