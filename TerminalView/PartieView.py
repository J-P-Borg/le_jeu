import sys

from TerminalController.PartieController import PartieController


def configure_nb_joueur(partieController: PartieController):
    sys.stdout.flush()
    print("Configuration du nombre de joueur")
    while True:
        try:
            partieController.configureNbJoueur(int(input("Entrer nombre joueurs (entre 1 et 5)")))
        except:
            print("nombre de joueur incorrect")
        else:
            break
