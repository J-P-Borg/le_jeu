from model.PartieModel import Partie


def test_score():
    """
    Vérifie qu'il est possible de calculer le score d'une partie en cours
    :return:
    """
    partie = Partie(1)
    assert partie.score() == 98
    joueur = partie.list_joueur[0]
    joueur.jouer_carte(joueur.main[0], True, 0)
    assert partie.score() == 97


def test_fin_partie():
    """
    Fait les vérifs sur estGagnee et estPerdue
    :return:
    """
    partie = Partie(1)
    assert not partie.estGagnee()
    assert not partie.estPerdue()
    partie.sabot = []
    partie.list_joueur[0].main = []
    assert partie.estGagnee()
    assert not partie.estPerdue()
    partie.piles_montantes = [[84], [85]]
    partie.piles_descendantes = [[14], [15]]
    partie.list_joueur[0].main = list(range(30, 38))
    assert not partie.estGagnee()
    assert partie.estPerdue()
