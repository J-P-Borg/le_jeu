import sys

from TerminalController.PartieController import PartieController


def configure_nb_joueur(partieController: PartieController):
    """
    Affiche le champs pour renseigner le nombre de joueur
    Va boucler tant que le nombre de joueur renseigné est incorrect
    :param partieController: controller de partie
    :return:
    """
    sys.stdout.flush()
    print("Configuration du nombre de joueur")
    while True:
        try:
            partieController.configureNbJoueur(int(input("Entrer nombre joueurs (entre 1 et 5)")))
        except:
            print("nombre de joueur incorrect")
        else:
            break
