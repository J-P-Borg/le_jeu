import pytest

from model.PartieModel import Partie


def test_jouer_descandante_valide():
    """
    Vérifie qu'un joueur peut jouer une carte plus faible sur une pile descendante
    :return:
    """
    partie = Partie()
    partie.set_nb_joueur(1)
    partie.sabot = [99, 98, 97, 2, 3, 4, 87]
    joueur0 = partie.list_joueur[0]
    joueur0.complete_main()
    joueur0.jouer_carte(numero_carte=99, montante=False, id_pile=0)
    assert joueur0.main == [87, 4, 3, 2, 97, 98]
    assert partie.piles_descendantes == [[100, 99], [100]]
    joueur0.jouer_carte(numero_carte=98, montante=False, id_pile=0)
    assert joueur0.main == [87, 4, 3, 2, 97]
    assert partie.piles_descendantes == [[100, 99, 98], [100]]
    joueur0.jouer_carte(numero_carte=97, montante=False, id_pile=1)
    assert joueur0.main == [87, 4, 3, 2]
    assert partie.piles_descendantes == [[100, 99, 98], [100, 97]]
    joueur0.jouer_carte(numero_carte=87, montante=False, id_pile=1)
    assert joueur0.main == [4, 3, 2]
    assert partie.piles_descendantes == [[100, 99, 98], [100, 97, 87]]


def test_jouer_montante_valide():
    """
    Vérifie qu'un joueur peut jouer une carte plus faible sur une pile montante
    :return:
    """
    partie = Partie()
    partie.set_nb_joueur(1)
    partie.sabot = [99, 98, 97, 2, 3, 4, 87]
    joueur0 = partie.list_joueur[0]
    joueur0.complete_main()
    joueur0.jouer_carte(numero_carte=2, montante=True, id_pile=0)
    assert joueur0.main == [87, 4, 3, 97, 98, 99]
    assert partie.piles_montantes == [[1, 2], [1]]
    joueur0.jouer_carte(numero_carte=3, montante=True, id_pile=0)
    assert joueur0.main == [87, 4, 97, 98, 99]
    assert partie.piles_montantes == [[1, 2, 3], [1]]
    joueur0.jouer_carte(numero_carte=4, montante=True, id_pile=1)
    assert joueur0.main == [87, 97, 98, 99]
    assert partie.piles_montantes == [[1, 2, 3], [1, 4]]
    joueur0.jouer_carte(numero_carte=97, montante=True, id_pile=1)
    assert joueur0.main == [87, 98, 99]
    assert partie.piles_montantes == [[1, 2, 3], [1, 4, 97]]


def test_saut_10():
    """
    Vérifie que le saut de 10 est faisable
    :return:
    """
    partie = Partie()
    partie.set_nb_joueur(1)
    joueur0 = partie.list_joueur[0]
    partie.sabot = [99, 98, 97, 2, 14, 4, 87]
    joueur0.complete_main()
    joueur0.jouer_carte(numero_carte=97, montante=True, id_pile=0)
    joueur0.jouer_carte(numero_carte=87, montante=True, id_pile=0)
    assert joueur0.main == [4, 14, 2, 98, 99]
    assert partie.piles_montantes == [[1, 97, 87], [1]]
    joueur0.jouer_carte(numero_carte=4, montante=False, id_pile=1)
    joueur0.jouer_carte(numero_carte=14, montante=False, id_pile=1)
    assert joueur0.main == [2, 98, 99]
    assert partie.piles_descendantes == [[100], [100, 4, 14]]


def test_jouer_carte_trop_forte():
    """
    Vérifie qu'une erreur est levée si une carte trop forte est jouée dans une pile descendante
    :return:
    """
    partie = Partie()
    partie.set_nb_joueur(1)
    partie.sabot = [99, 98, 97, 2, 14, 4, 87]
    joueur0 = partie.list_joueur[0]
    joueur0.complete_main()
    joueur0.jouer_carte(numero_carte=97, montante=False, id_pile=0)
    with pytest.raises(AssertionError):
        joueur0.jouer_carte(numero_carte=99, montante=False, id_pile=0)


def test_jouer_carte_trop_faible():
    """
    Vérifie qu'une erreur est levée si une carte trop faible est jouée dans une pile montante
    :return:
    """
    partie = Partie()
    partie.set_nb_joueur(1)
    partie.sabot = [99, 98, 97, 2, 14, 4, 87]
    joueur0 = partie.list_joueur[0]
    joueur0.complete_main()
    joueur0.jouer_carte(numero_carte=99, montante=True, id_pile=0)
    with pytest.raises(AssertionError):
        joueur0.jouer_carte(numero_carte=97, montante=True, id_pile=0)


def test_jouer_carte_pas_dans_main():
    """
    Vérifie qu'une erreur est levée si une carte pas dans une main est jouée
    :return:
    """
    partie = Partie()
    partie.set_nb_joueur(1)
    partie.sabot = [99, 98, 97, 2, 14, 4, 87]
    joueur0 = partie.list_joueur[0]
    joueur0.complete_main()
    with pytest.raises(AssertionError):
        joueur0.jouer_carte(numero_carte=42, montante=True, id_pile=0)
