import pytest

from model.PartieModel import Partie


def test_taille_main():
    """
    Vérifie que la variable taille main est correctement définie
    :return:
    """
    partie = Partie()
    aux = [(1, 8), (2, 7), (3, 6), (4, 6), (5, 6)]
    for nb_joueur, taille_main in aux:
        partie.set_nb_joueur(nb_joueur)
        partie.set_taille_main()
        assert partie.taille_main == taille_main


def test_distribution_cartes():
    """
    Test que les cartes sont bien distribuées dans le cas ou il y a assez de cartes dans le sabot
    Test pour un id de joueur correct
    :return:
    """
    for nb_joueur in range(1, 6):
        for id_joueur in range(nb_joueur):
            partie = Partie()
            partie.set_nb_joueur(nb_joueur=nb_joueur)
            partie.sabot = list(range(10))
            partie.complete_main(id_joueur=id_joueur)
            assert partie.sabot + list(reversed(partie.list_mains[id_joueur])) == list(range(10))


def test_distribution_sabot_vide():
    """
    Vérifie que la distribution fonctionnne correctement si le sabot n'a plus assez de cartes
    (Arrive en fin de partie)
    :return:
    """
    partie = Partie()
    partie.set_nb_joueur(3)
    partie.sabot = list(range(4))
    partie.complete_main(1)
    assert partie.sabot == []
    assert partie.list_mains[1] == list(range(3, -1, -1))


def test_distribution_cartes_id_joueur_incorrect():
    """
    Vérifie qu'une erreur est levée si l'id de joueur est incorrect
    :return:
    """
    partie = Partie()
    partie.set_nb_joueur(3)
    with pytest.raises(AssertionError):
        partie.complete_main(-1)
    with pytest.raises(AssertionError):
        partie.complete_main(3)
    with pytest.raises(TypeError):
        partie.complete_main(2.0)
