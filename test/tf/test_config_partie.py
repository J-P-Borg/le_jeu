import itertools

from TerminalController.PartieController import PartieController


def test_config_partie_nb_correct(monkeypatch):
    """
    Test le controller de partie, et vérifie qu'il permet à l'utilisateur de config une partie correctement,
    avec un nmobre de joueur correct
    :return:
    """
    nb_joueur = 5
    controller = PartieController()
    controller.partie.sabot = list(range(2, 100))
    monkeypatch.setattr('builtins.input', lambda _: str(nb_joueur))
    controller.configurePartie()
    assert controller.partie.nb_joueur == nb_joueur
    mains_attendues = [list(range(99 - (i + 1) * 6 + 1, 99 - i * 6 + 1)) for i in range(5)]
    for joueur, main_attendue in zip(controller.partie.list_joueur, mains_attendues):
        assert joueur.main == main_attendue


def test_config_partie_nb_incorrect():
    # TODO tester le message d'erreur en cs d'input invalide
    pass
