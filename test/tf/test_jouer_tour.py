# from _pytest import monkeypatch
#
# from TerminalController.PartieController import PartieController
#
#
# def test_jouer_tour():
#     """
#     Test qu'un joueur peut jouer correctement son tour
#     Cas à vérifier avec les messages d'erreur:
#     * carte invalide
#     * fin de tour non autorisée
#     * indice de pile invalide
#     Vérifier
#     * tour valide, et passage au joueur suivant
#     * main complétée
#     :return:
#     """
#     nb_joueur = 5
#     controller = PartieController()
#     monkeypatch.setattr('builtins.input', lambda _: str(nb_joueur))
#     controller.configurePartie()
#     # Carte invalide
#     monkeypatch.setattr('builtins.input', lambda _: "100")
