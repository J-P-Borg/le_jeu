import structlog

logger = structlog.getLogger(__name__)


class Joueur:
    from model.PartieModel import Partie
    def __init__(self, id: int, partie: Partie):

        """
        
        :param id:numéro du joueur 
        """
        self.partie = partie
        logger.info(f"Vérifie que l'id {id} est valide")
        assert 0 <= id < self.partie.nb_joueur
        self.id = id
        self.main = []

    def complete_main(self):
        """
        Distribue dans la main du joueur self.self.id le nombre de carte nécessaire pour qu'il ait une main valide
        (cf taille_main : variable globale de taille de main, selon le nombre de joueur)
        :param self.self.id: id du joueur (indice du jeu à compléter)
        :return:
        """
        logger.info(f"Completion main joueur {self.id}")
        try:
            logger.info("Vérifie que taille_main et nb_joueur sont définis")
            self.partie.taille_main
            self.partie.nb_joueur
        except:
            logger.warning("taille_main aurait du être défini, non critique (tentative de définition ici)")
            self.partie.set_taille_main()
        logger.debug(f"Id joueur : {self.id}")
        logger.info(f"Main du joueur avant ajout de cartes : {self.main}")
        for _ in range(min(self.partie.taille_main - len(self.main), len(self.partie.sabot))):
            logger.debug(f"Carte ajoutée : {self.partie.sabot[-1]}")
            self.main.append(self.partie.sabot.pop())
            logger.debug(f"Main après ajout : {self.main}")
            logger.debug(f"Sabot après ajout : {self.partie.sabot}")

    def jouer_carte(self, numero_carte: int, montante: bool, id_pile: int):
        """
        joue une carte, vérifie qu'elle est dans la main du joueur
        :param numero_carte: valeur de la carte à jouer (pas l'indice)
        :param montante: true si jouer sur pile montante
        :param id_pile: entre 0 et 1
        :return:
        """
        self.partie.check_config(self.id)
        # Vérifie que la carte
        assert numero_carte in self.main
        # Vérifie que la pile demandée est valide
        assert 0 <= id_pile <= 1
        # Vérifie que la carte est jouable
        if montante:
            derniere_carte = self.partie.piles_montantes[id_pile][-1]
            assert (numero_carte > derniere_carte) or (numero_carte == derniere_carte - 10)
        else:
            derniere_carte = self.partie.piles_descendantes[id_pile][-1]
            assert (numero_carte < derniere_carte) or (numero_carte == derniere_carte + 10)
        # Retirer la carte de la main du joueur
        self.main.remove(numero_carte)
        # L'ajouter dans la pile demandée
        if montante:
            self.partie.piles_montantes[id_pile].append(numero_carte)
        else:
            self.partie.piles_descendantes[id_pile].append(numero_carte)
