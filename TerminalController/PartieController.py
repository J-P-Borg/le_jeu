import structlog

from model.PartieModel import Partie

logger = structlog.getLogger(__name__)


class PartieController:
    def __init__(self):
        logger.info("Creation du controller de partie")
        self.partie = Partie()

    def configurePartie(self):
        """
        Va appeler les différentes fonctions de config d'une partie
        :return:
        """
        from TerminalView import PartieView
        logger.info("Config de la partie dans le controller")
        PartieView.configure_nb_joueur(self)

    def configureNbJoueur(self, nbJoueur: int):
        """
        :param nbJoueur: nombre de joueur renseigné par l'utilisateur dans le model
        :raises ValueError: erreur levée par set_nb_joueur
        """
        logger.info(f"configuration du nombre de joueur, {nbJoueur} demandés")
        logger.debug(f"type de nbJoueur : {type(nbJoueur)}")
        self.partie.set_nb_joueur(nb_joueur=nbJoueur)
