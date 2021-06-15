from TerminalController.PartieController import PartieController


def test_config_partie_nb_correct(monkeypatch):
    """
    Test le controller de partie, et vérifie qu'il permet à l'utilisateur de config une partie correctement,
    avec un nmobre de joueur correct
    :return:
    """
    controller = PartieController()
    monkeypatch.setattr('builtins.input', lambda _: "5")
    controller.configurePartie()
    assert controller.partie.nb_joueur == 5


def test_config_partie_nb_incorrect():
    # TODO tester le message d'erreur en cs d'input invalide
    pass
