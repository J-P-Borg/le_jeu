import random as rd

import structlog


logger = structlog.getLogger(__name__)


class Partie:
    """
    Model d'une partie, va gérer le sabot et les mains des joueurs
    """

    def __init__(self) -> object:
        self.sabot = list(range(2, 100))
        rd.shuffle(self.sabot)
        logger.debug(f"Sabot : {self.sabot}")
        self.list_joueur = []
        self.piles_descendantes = [[100], [100]]
        self.piles_montantes = [[1], [1]]

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
            self.set_taille_main()
        logger.info(f"Vérifie que l'id_joueur {id_joueur} est valide")
        assert 0 <= id_joueur < self.nb_joueur

    def set_nb_joueur(self, nb_joueur: int):
        """
        :param nb_joueur: nombre de joueur de la partie
        Va affecter le nombre de joueur, et vérifie qu'il est valide (entre 1 et 5 inclus)
        Instancie les joueurs
        :raises: ValueError, si le nombre de joueur n'est pas valide
        """
        from model.JoueurModel import Joueur
        logger.info(f"Config du nombre de joueur, {nb_joueur} joueurs")
        if nb_joueur in range(1, 6):
            logger.info("nombre de joueur correct")
            self.nb_joueur = nb_joueur
            self.set_taille_main()
            self.list_joueur = [Joueur(id=i, partie=self) for i in range(self.nb_joueur)]
            logger.info(f"taille_main =: {self.taille_main}")
            logger.debug(f"list_joueur: {self.list_joueur}")
        else:
            logger.warning("nombre de joueur incorrect")
            raise ValueError("Nombre de joueur incorrect")

    def set_taille_main(self):
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
            logger.error("Le nombre de joueur n'a pas été défini, doit l'être avant l'appel de cette fonction")
            raise AttributeError("le nombre de joueur n'est pas défini")

    def distribueMainsInitiales(self):
        """
        Distribue toutes les mains initiales
        :return: 
        """
        logger.info("Distribution des mains de départ")
        logger.debug(f"liste des joueurs : {self.list_joueur}")
        for joueur in self.list_joueur:
            joueur.complete_main()
