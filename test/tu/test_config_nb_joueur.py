import pytest

from model.PartieModel import Partie


def test_nb_joueur_incorrect():
    """
    Vérifie que si une valeur incorrecte est utilisée, alors une erreur est levée
    :return:
    """
    partie = Partie()
    with pytest.raises(ValueError):
        partie.set_nb_joueur(6)
    with pytest.raises(TypeError):
        partie.set_nb_joueur("5")
    with pytest.raises(TypeError):
        partie.set_nb_joueur(5.0)


def test_nb_joueur_correct():
    """
    Vérifie qu'il est possible de configurer une partie avec 1,2,3,4,5 joueurs
    :return:
    """
    partie = Partie()
    for i in range(1, 6):
        partie.set_nb_joueur(i)
        assert partie.nb_joueur == i
