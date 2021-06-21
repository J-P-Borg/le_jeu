import structlog

from model.PartieModel import Partie

logger = structlog.getLogger(__name__)


class PartieController:
    notEnoughCarteJouee = "Vous n'avez pas joué assez de cartes"
    carteInvalide = "Vous avez joué une carte invalide"

    def __init__(self):
        """
        joueur : indice du joueur qui doit faire son tour
        termine : True quand la partie est finie
        """
        logger.info("Creation du controller de partie")
        self.partie = Partie()
        self.joueur = 0
        self.termine = False

    def configurePartie(self):
        """
        Va appeler les différentes fonctions de config d'une partie
        * Configurer le nombre de joueur
        * Distribuer les mains initiales
        :return:
        """
        from TerminalView import PartieView
        logger.info("Config de la partie dans le controller")
        PartieView.configure_nb_joueur(self)
        self.partie.distribueMainsInitiales()

    def configureNbJoueur(self, nbJoueur: int):
        """
        :param nbJoueur: nombre de joueur renseigné par l'utilisateur dans le model
        :raises ValueError: erreur levée par set_nb_joueur
        """
        logger.info(f"configuration du nombre de joueur, {nbJoueur} demandés")
        logger.debug(f"type de nbJoueur : {type(nbJoueur)}")
        self.partie.set_nb_joueur(nb_joueur=nbJoueur)

    def jouerPartie(self):
        """
        Va tourner tant que la partie n'est pas finie
        Va faire passer les tours les uns après les autres
        :return:
        """
        logger.info("Début de partie")
        self.configurePartie()
        while not self.termine:
            self.jouerTour()

    def jouerTour(self):
        """
        Va jouer le tour du joueur self.joueur
        Va changer passer au joueur suivant une fois le tour du joueur terminé
        :return:
        """
        logger.info(f"Début du tour de {self.joueur}")
        from TerminalView import PartieView
        action, montante, id_pile = PartieView.afficher_jeu(self)
        logger.info(f"action demandée : {action}")
        logger.info(f"montante : {montante}")
        logger.info(f"id_pile: {id_pile}")
        while action and not (self.partie.list_joueur[self.joueur].canFinish()):
            logger.info(f"le joueur peut finir son tour : {self.partie.list_joueur[self.joueur].canFinish()}")
            # Le joueur demande à finir mais n'as pas posé assez de cartes
            if not action:
                logger.warning("Le joueur a demandé à finir son tour sans en avoir le droit")
                PartieView.afficher_jeu(self, message=PartieController.notEnoughCarteJouee)
            # Sinon, on vérifie que la carte demndée est valide
            else:
                try:
                    logger.info(f"Essaie de jouer la carte demandée")
                    self.partie.list_joueur[self.joueur].jouer_carte(id_pile=id_pile, montante=montante,
                                                                     numero_carte=action)
                except:
                    logger.warning("La carte est invalide")
                    action, montante, id_pile = PartieView.afficher_jeu(self, message=PartieController.carteInvalide)
                else:
                    action, montante, id_pile = PartieView.afficher_jeu(self, )
        # Fin de tour valide
        if self.partie.list_joueur[self.joueur].canFinish():
            logger.info("fin du tour")
            self.joueur = (self.joueur + 1) % self.partie.nb_joueur
