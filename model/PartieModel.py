import random as rd

import structlog

from model.message_erreur import ID_JOUEUR_INCORRECT

logger = structlog.getLogger(__name__)


class Partie:
    """
    Model d'une partie, va gérer le sabot et les mains des joueurs
    """

    def __init__(self, nb_joueur: int) -> object:
        """
        Crée la partie
        Crée le sabot de carte
        Vérifie que le nombre de joueurs est correct
        Distribue les mains initiales
        Initialise les piles
        La partie est jouable
        :param nb_joueur: nombre de joueurs dans la partie
        :raises ValueError: si nb_joueur n'a pas une valeur entre 1 et 5 inclus
        """
        self.sabot = list(range(2, 100))
        logger.debug(f"Sabot pas mélangé: {self.sabot}")
        rd.shuffle(self.sabot)
        logger.debug(f"Sabot : {self.sabot}")
        self._set_nb_joueur(nb_joueur=nb_joueur)
        self._distribueMainsInitiales()
        logger.info(f"taille_main =: {self.taille_main}")
        logger.debug(f"list_joueur: {self.list_joueur}")
        self.piles_descendantes = [[100], [100]]
        self.piles_montantes = [[1], [1]]
        self.joueur = 0

    def check_config(self, id_joueur: int):
        """
        Vérifie que taille_main et nb_joueur ont bien été définis
        (Set taille_main si pas défini)
        Vérifie que l'id du joueur est valide (entre 0 et nombre_joueur - 1)
        :param id_joueur: id du joueur à vérifier
        :raises: AttributeError
        :return:
        """
        try:
            logger.info("Vérifie que taille_main et nb_joueur sont définis")
            self.taille_main
            self.nb_joueur
        except:
            logger.warning("taille_main aurait du être défini, non critique (tentative de définition ici)")
            self._set_taille_main()
        logger.info(f"Vérifie que l'id_joueur {id_joueur} est valide")
        assert 0 <= id_joueur < self.nb_joueur, ID_JOUEUR_INCORRECT

    def _set_nb_joueur(self, nb_joueur: int):
        """
        :param nb_joueur: nombre de joueurs de la partie
        Va affecter le nombre de joueurs, et vérifie qu'il est valide (entre 1 et 5 inclus)
        Instancie les joueurs
        :raises: ValueError, si le nombre de joueurs n'est pas valide
        :raises: TypeError si le type de nb_joueur n'est pas valide
        """
        if not type(nb_joueur) == int:
            logger.error(f"appel de set_nb_joueur avec un mauvais type ({type(nb_joueur)} au lieu de int")
            raise TypeError("Le nombre de joueurs doit être de type int")
        logger.info(f"Config du nombre de joueurs, {nb_joueur} joueurs")
        if nb_joueur in range(1, 6):
            logger.info("nombre de joueurs correct")
            self.nb_joueur = nb_joueur
            from model.JoueurModel import Joueur
            self.list_joueur = [Joueur(id=i, partie=self) for i in range(self.nb_joueur)]
        else:
            logger.warning(
                f"nombre de joueurs {nb_joueur} incorrect, car {nb_joueur} dans range(1,6) : {nb_joueur in range(1, 6)}")
            raise ValueError("Nombre de joueurs incorrect")

    def _set_taille_main(self):
        """
        Configure la taille des mains selon le nombre de joueurs
        8 cartes si 1 joueur
        7 cartes si 2 joueurs
        6 cartes si 3 joueurs ou plus
        :return: None
        :raises: AttributeError si le nombre de joueur n'est pas défini
        """
        try:
            logger.info("Config de la taille des mains")
            self.taille_main = 6 + (self.nb_joueur <= 2) + (self.nb_joueur == 1)
        except:
            logger.error("Le nombre de joueurs n'a pas été défini, il doit l'être avant l'appel de cette fonction")
            raise AttributeError("Le nombre de joueurs n'est pas défini")

    def _distribueMainsInitiales(self):
        """
        Distribue toutes les mains initiales
        :return: 
        """
        self._set_taille_main()
        logger.info("Distribution des mains de départ")
        logger.debug(f"liste des joueurs : {self.list_joueur}")
        for joueur in self.list_joueur:
            joueur.complete_main()

    def score(self):
        """
        Retourne le nombre de cartes restant à jouer, ce qui correspond au score en fin de partie
        :return:
        """
        return len(self.sabot) + sum(map(lambda x: len(x.main), self.list_joueur))

    def estGagnee(self) -> bool:
        """
        Indique si la partie est gagnée
        :return:
        """
        return not self.score()

    def estPerdue(self) -> bool:
        """
        Indique si la partie est perdue
        :return:
        """
        joueur = self.list_joueur[self.joueur]
        return not joueur.canJouer() and not joueur.canFinish()
