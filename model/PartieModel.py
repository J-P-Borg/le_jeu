import random as rd

import structlog

logger = structlog.getLogger(__name__)


class Partie:
    def __init__(self) -> object:
        self.sabot = list(range(1, 100))
        rd.shuffle(self.sabot)
        logger.debug(f"Sabot : {self.sabot}")

    def set_nb_joueur(self, nb_joueur: int):
        logger.info(f"Config du nombre de joueur, {nb_joueur} joueurs")
        if nb_joueur in range(1, 6):
            logger.info("nombre de joueur correct")
            self.nb_joueur = nb_joueur
        else:
            logger.warning("nombre de joueur incorrect")
            raise ValueError("Nombre de joueur incorrect")
