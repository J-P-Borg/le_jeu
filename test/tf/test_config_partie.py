
from TerminalController.PartieController import PartieController


def test_config_partie_nb_correct(monkeypatch):
    """
    Test le controller de partie, et vérifie qu'il permet à l'utilisateur de config une partie correctement,
    avec un nmobre de joueur correct
    :return:
    """
    nb_joueur = 5
    monkeypatch.setattr('builtins.input', lambda _: str(nb_joueur))
    controller = PartieController()
    assert controller.partie.nb_joueur == nb_joueur
    controller.partie.check_config(0)


def test_config_partie_nb_incorrect():
    # TODO tester le message d'erreur en cs d'input invalide
    pass
