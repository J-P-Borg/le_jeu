import random as rd

import structlog

logger = structlog.getLogger(__name__)


class Partie:
    """
    Model d'une partie, va gérer le sabot et les mains des joueurs
    """

    def __init__(self) -> object:
        self.sabot = list(range(1, 100))
        rd.shuffle(self.sabot)
        logger.debug(f"Sabot : {self.sabot}")

    def set_nb_joueur(self, nb_joueur: int):
        """
        :param nb_joueur: nombre de joueur de la partie
        Va affecter le nombre de joueur, et vérifie qu'il est valide (entre 1 et 5 inclus)
        :raises: ValueError, si le nombre de joueur n'est pas valide
        """
        logger.info(f"Config du nombre de joueur, {nb_joueur} joueurs")
        if nb_joueur in range(1, 6):
            logger.info("nombre de joueur correct")
            self.nb_joueur = nb_joueur
        else:
            logger.warning("nombre de joueur incorrect")
            raise ValueError("Nombre de joueur incorrect")
