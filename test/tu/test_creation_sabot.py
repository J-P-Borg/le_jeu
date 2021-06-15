from model.PartieModel import Partie


def test_creation_sabot():
    """
    Vérifie que le sabot a bien un jeu avec les cartes de 2 à 99
    :return:
    """
    partie = Partie()
    jeu_trie = list(range(2, 100))
    # Le jeu dois être mélangé
    assert partie.sabot != jeu_trie
    partie.sabot.sort()
    # Le jeu dois contenir les cartes de 2 à 99
    assert partie.sabot == jeu_trie
