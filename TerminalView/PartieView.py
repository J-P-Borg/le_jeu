import sys

import structlog

from TerminalController.PartieController import PartieController

logger = structlog.getLogger(__name__)


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


def afficher_jeu(partieController: PartieController, message="") -> (int, bool, int):
    """
    Affiche la partie avec le jeu du joueur dont c'est le tour
    :param partieController:
    :return: la valeur de la carte à jouer, 0 si fin de tour, is la pile est montante, et l'index de la pile
    """
    logger.info("Appel de afficher_jeu")
    logger.debug(f"Message : {message}")
    sys.stdout.flush()
    print(message)
    spacing = len(" Descendante 0 ")
    print(
        f"{'Descendante 0':<{spacing}}| {'Descendante 1':<{spacing}}| {'Montante 0':<{spacing}}| {'Montante 1':<{spacing}}")
    pile_desc = partieController.partie.piles_descendantes
    pile_asc = partieController.partie.piles_montantes
    print(
        f"{pile_desc[0][-1]:<{spacing}}| {pile_desc[1][-1]:<{spacing}}| {pile_asc[0][-1] :<{spacing}}| {pile_asc[1][-1]:<{spacing}}")
    print(f"Tour du joueur {partieController.joueur}")
    print(f"Main du joueur : {partieController.partie.list_joueur[partieController.joueur].main}")
    while True:
        while True:
            try:
                carte = int(input("Carte à jouer :"))
            except:
                logger.warning("Input carte mal formaté")
                print("Input carte mal formaté, veuillez recommencer")
            else:
                break
        while True:
            try:
                montante = bool(int(input("Montante ? (1 si oui, 0 sinon)")))
            except:
                logger.warning("Input montante mal formaté")
                print("Input montante mal formaté, veuillez recommencer")
            else:
                break
        while True:
            try:
                index_pile = int(input("Indice de pile (0 ou 1)"))
            except:
                logger.warning("Input index_pile mal formaté")
                print("Input index_pile mal formatés, veuillez recommencer")
            else:
                break
        logger.info("Inputs avec format valide")
        break
    return carte, montante, index_pile
