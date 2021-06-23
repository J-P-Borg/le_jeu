import pytest

from model.PartieModel import Partie


def test_nb_joueur_incorrect():
    """
    Vérifie que si une valeur incorrecte est utilisée, alors une erreur est levée
    :return:
    """
    with pytest.raises(ValueError):
        partie = Partie(6)
    with pytest.raises(TypeError):
        partie = Partie("5")
    with pytest.raises(TypeError):
        partie = Partie(5.0)


def test_nb_joueur_correct():
    """
    Vérifie qu'il est possible de configurer une partie avec 1,2,3,4,5 joueurs
    :return:
    """
    for i in range(1, 6):
        partie = Partie(i)
        assert partie.nb_joueur == i
