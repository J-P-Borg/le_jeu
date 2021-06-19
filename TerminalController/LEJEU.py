import structlog

import logging_config
from TerminalController.PartieController import PartieController

logger = structlog.getLogger(__name__)


def start_le_jeu():
    """
    Fonction à appeler pour lancer une partie
    :return:
    """
    logging_config.config_logging(terminal=False)
    logger.info("Lancement de la partie")
    partieController = PartieController()
    partieController.configurePartie()


if __name__ == '__main__':
    start_le_jeu()
