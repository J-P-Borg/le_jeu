import structlog

from model.PartieModel import Partie

logger = structlog.getLogger(__name__)


class PartieController:
    def __init__(self):
        logger.info("Creation du controller")
        self.partie = Partie()

    def configurePartie(self):
        logger.info("Config de la partie")
        from TerminalView import PartieView
        PartieView.configure_nb_joueur(self)

    def configureNbJoueur(self, nbJoueur: int):
        logger.info(f"configuration du nombre de joueur, {nbJoueur} demandés")
        logger.debug(f"type de nbJoueur : {type(nbJoueur)}")
        self.partie.set_nb_joueur(nb_joueur=nbJoueur)
