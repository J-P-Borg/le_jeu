import structlog

from model.PartieModel import Partie
from model.message_erreur import PAS_ASSEZ_CARTES_JOUEES

logger = structlog.getLogger(__name__)


class PartieController:

    def __init__(self):
        """
        joueur : indice du joueur qui doit faire son tour
        termine : True quand la partie est finie
        """
        logger.info("Creation du controller de partie")
        self.termine = False
        self.initPartie()

    def initPartie(self):
        """
        Va instancier la partie
        Va récupérer le nombre de joueurs, nécesaire pour instancier la partie
        """
        while True:
            try:
                from TerminalView.PartieView import get_nb_joueur
                nbJoueur = get_nb_joueur()
                logger.debug(f"type de nbJoueur : {type(nbJoueur)}")
                logger.info(f"Création d'une partie avec {nbJoueur} demandés")
                self.partie = Partie(nb_joueur=nbJoueur)
            except:
                pass
            else:
                break

    def jouerPartie(self):
        """
        Va tourner tant que la partie n'est pas finie
        Va faire passer les tours les uns après les autres
        :return:
        """
        from TerminalView.PartieView import finPartie
        logger.info("Début de partie")
        while not self.partie.estGagnee() or not self.partie.estPerdue():
            self.jouerTour()
        finPartie(self)
        return 0

    def jouerTour(self):
        """
        Va jouer le tour du joueur self.partie.joueur
        Va changer passer au joueur suivant une fois le tour du joueur terminé
        :return:
        """
        logger.info(f"Début du tour de {self.partie.joueur}")
        from TerminalView import PartieView
        # Récupération des inputs du joueur
        action, montante, id_pile = PartieView.afficher_jeu(self)
        logger.info(f"action demandée : {action}")
        logger.info(f"montante : {montante}")
        logger.info(f"id_pile: {id_pile}")
        # Tant que le joueur joue des cartes et qu'il n'a pas le droit de finir son tour
        while action or not (
        self.partie.list_joueur[self.partie.joueur].canFinish()) or self.partie.estPerdue() or self.partie.estGagnee():
            logger.info(f"le joueur peut finir son tour : {self.partie.list_joueur[self.partie.joueur].canFinish()}")
            # Le joueur demande à finir mais n'as pas posé assez de cartes
            if not action:
                logger.warning("Le joueur a demandé à finir son tour sans en avoir le droit")
                action, montante, id_pile = PartieView.afficher_jeu(self, message=PAS_ASSEZ_CARTES_JOUEES)
            # Sinon, on vérifie que la carte demandée est valide
            else:
                try:
                    logger.info(f"Essaie de jouer la carte demandée")
                    self.partie.list_joueur[self.partie.joueur].jouer_carte(id_pile=id_pile, montante=montante,
                                                                            numero_carte=action)
                # Si la carte est invalide, on redemande une carte
                except Exception as e:
                    logger.warning("La carte est invalide")
                    action, montante, id_pile = PartieView.afficher_jeu(self, message=e)
                # Sinon on demande la prochaine action du joueur
                else:
                    logger.info("La carte demandée est valide")
                    action, montante, id_pile = PartieView.afficher_jeu(self, )
        # Fin de tour valide
        if self.partie.list_joueur[self.partie.joueur].canFinish():
            logger.info("fin du tour")
            self.partie.list_joueur[self.partie.joueur].complete_main()
            self.partie.joueur = (self.partie.joueur + 1) % self.partie.nb_joueur
