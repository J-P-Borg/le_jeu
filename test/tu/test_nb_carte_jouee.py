from model.PartieModel import Partie


def test_nb_carte_jouee():
    """
    Vérifie qu'il est possible de savoir combien de carte le joueur a joué pendant son tour
    :return:
    """
    for nb_joueur in range(1, 6):
        partie = Partie(nb_joueur=nb_joueur)
        joueur = partie.list_joueur[0]
        joueur.main.sort()
        assert joueur.nb_carte_jouee() == 0
        for index, carte in enumerate(joueur.main):
            joueur.jouer_carte(numero_carte=carte, montante=True, id_pile=0)
            assert joueur.nb_carte_jouee() == index + 1
        joueur.complete_main()
        assert joueur.nb_carte_jouee() == 0
