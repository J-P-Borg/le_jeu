from model.JoueurModel import Joueur
from model.PartieModel import Partie


def test_peut_jouer_carte():
    """
    Vérifie si la fonction peu_jouer_carte vérifie correctement çà
    :return:
    """
    partie = Partie(1)
    joueur: Joueur = partie.list_joueur[0]
    joueur.main = list(range(2, 10))
    partie.piles_montantes = [[6], [5]]
    partie.piles_descendantes = [[2], [3]]
    assert joueur.canJouerCarte(7)
    assert not joueur.canJouerCarte(4)


def test_peut_joueur():
    """
    Vérifie la fonction canjouer
    :return:
    """
    partie = Partie(1)
    joueur: Joueur = partie.list_joueur[0]
    partie.piles_montantes = [[6], [5]]
    partie.piles_descendantes = [[2], [3]]
    joueur.main = []
    assert not joueur.canJouer()
    joueur.main = [4]
    assert not joueur.canJouer()
    joueur.main.append(7)
    assert joueur.canJouer()
