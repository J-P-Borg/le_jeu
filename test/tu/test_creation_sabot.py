
from model.PartieModel import Partie


def test_creation_sabot(monkeypatch):
    """
    Vérifie que le sabot a bien un jeu avec les cartes de 2 à 99
    :return:
    """
    partie = Partie(1)
    jeu_trie = list(range(2, 100))
    # Le jeu dois être mélangé
    assert partie.sabot != jeu_trie
    # La main du joueur a été distribuée, il faut la prendre en compte
    partie.sabot.extend(partie.list_joueur[0].main)
    partie.sabot.sort()
    # Le jeu doit contenir les cartes de 2 à 99
    assert partie.sabot == jeu_trie
