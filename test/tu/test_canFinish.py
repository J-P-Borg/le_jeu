from model.JoueurModel import Joueur
from model.PartieModel import Partie


def test_canFinish_sabot_plein():
    """
    Vérifie canFinish, quand il reste des cartes dans le sabot
    0 et 1 carte : FALSE
    2 : TRUE
    :return:
    """
    partie = Partie()
    partie.set_nb_joueur(2)
    partie.distribueMainsInitiales()
    joueur0: Joueur = partie.list_joueur[0]
    # Aucune carte jouée : NON
    assert not joueur0.canFinish()
    # Une carte jouée : NON
    joueur0.jouer_carte(numero_carte=joueur0.main[0], montante=True, id_pile=0)
    assert not joueur0.canFinish()
    # Deux cartes jouées : OUI
    joueur0.jouer_carte(numero_carte=joueur0.main[0], montante=True, id_pile=1)
    assert joueur0.canFinish()


def test_canFinish_sabot_vide():
    """
    Vérifie canFinish, quand il reste des cartes dans le sabot
    0 et 1 carte : FALSE
    2 : TRUE
    :return:
    """
    partie = Partie()
    partie.set_nb_joueur(2)
    partie.distribueMainsInitiales()
    joueur0: Joueur = partie.list_joueur[0]
    partie.sabot = []
    # Aucune carte jouée : NON
    assert not joueur0.canFinish()
    # Une carte jouée : OUI
    joueur0.jouer_carte(numero_carte=joueur0.main[0], montante=True, id_pile=0)
    assert joueur0.canFinish()
    # Deux cartes jouées : OUI
    joueur0.jouer_carte(numero_carte=joueur0.main[0], montante=True, id_pile=1)
    assert joueur0.canFinish()
