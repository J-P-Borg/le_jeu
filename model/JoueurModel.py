import structlog

from model.message_erreur import MESSAGE_CARTE_PAS_DANS_MAIN, ID_JOUEUR_INCORRECT, NUMERO_PILE_INCORRECT, \
    CARTE_TROP_PETITE, CARTE_TROP_GRANDE

logger = structlog.getLogger(__name__)


class Joueur:
    from model.PartieModel import Partie
    def __init__(self, id: int, partie: Partie):
        """
        
        :param id:numéro du joueur 
        """
        self.partie = partie
        logger.info(f"Vérifie que l'id {id} est valide")
        assert 0 <= id < self.partie.nb_joueur, ID_JOUEUR_INCORRECT
        self.id = id
        self.main = []

    def nb_carte_jouee(self) -> int:
        """
        Calcule le nombre de cartes jouées par le joueur en fonction de la taille de sa main et de la taille d'une main
        (qui dépend du nombre de joueurs de la partie)
        :return:
        """
        logger.info("Appel nb_carte_jouee")
        logger.debug(f"taille main max : {self.partie.taille_main}, nombre de cartes du joueur : {len(self.main)}")
        return self.partie.taille_main - len(self.main)

    def complete_main(self):
        """
        Distribue dans la main du joueur self.self.id le nombre de cartes nécessaire pour qu'il ait une main valide
        (cf taille_main : variable globale de taille de main, selon le nombre de joueurs)
        :param self.id: id du joueur (indice du jeu à compléter)
        :return:
        """
        logger.info(f"Completion main joueur {self.id}")
        self.partie.check_config(self.id)
        logger.debug(f"Id joueur : {self.id}")
        logger.info(f"Main du joueur avant ajout de cartes : {self.main}")
        for _ in range(min(self.partie.taille_main - len(self.main), len(self.partie.sabot))):
            logger.debug(f"Carte ajoutée : {self.partie.sabot[-1]}")
            self.main.append(self.partie.sabot.pop())
            logger.debug(f"Main après ajout : {self.main}")
            logger.debug(f"Sabot après ajout : {self.partie.sabot}")
        self.main.sort()

    def jouer_carte(self, numero_carte: int, montante: bool, id_pile: int):
        """
        joue une carte, vérifie qu'elle est dans la main du joueur
        :param numero_carte: valeur de la carte à jouer (pas l'indice)
        :param montante: true si jouer sur pile montante
        :param id_pile: entre 0 et 1
        :raises AssertionError: erreur si la carte n'est pas valide
        :return:
        """
        self.partie.check_config(self.id)
        # Vérifie que la carte ???
        logger.info(f"demande pour jouer la carte {numero_carte} pour le joueur {self.id}")
        logger.debug(f"Main du joueur : {self.main}")
        logger.info("Vérification carte dans main")
        assert numero_carte in self.main, MESSAGE_CARTE_PAS_DANS_MAIN
        # Vérifie que la pile demandée est valide
        logger.info("Vérification indice de pile entre 0 et 1")
        assert 0 <= id_pile <= 1, NUMERO_PILE_INCORRECT
        # Vérifie que la carte est jouable sur la pile demandée
        if montante:
            derniere_carte = self.partie.piles_montantes[id_pile][-1]
            logger.debug(f"Dernière carte pile demandée : {derniere_carte}")
            logger.info("Vérification carte jouable")
            assert (numero_carte > derniere_carte) or (numero_carte == derniere_carte - 10), CARTE_TROP_PETITE
        else:
            derniere_carte = self.partie.piles_descendantes[id_pile][-1]
            logger.debug(f"Dernière carte pile demandée : {derniere_carte}")
            logger.info("Vérification carte jouable")
            assert (numero_carte < derniere_carte) or (numero_carte == derniere_carte + 10), CARTE_TROP_GRANDE
        # Retirer la carte de la main du joueur
        self.main.remove(numero_carte)
        # L'ajouter dans la pile demandée
        if montante:
            self.partie.piles_montantes[id_pile].append(numero_carte)
        else:
            self.partie.piles_descendantes[id_pile].append(numero_carte)

    def canJouer(self):
        """
        Vérifie si le joueur peut encore jouer des cartes
        :return:
        """
        return any(map(lambda x: self.canJouerCarte(x), self.main))

    def canJouerCarte(self, carte: int) -> bool:
        """
        Regarde si la carte est jouable
        :param carte: carte à vérifier
        :return: le booléan indiquant si la carte est jouable
        """
        logger.info(f"Vérifie si la carte {carte} est jouable")
        jouable = False
        for pile in self.partie.piles_montantes:
            jouable = jouable or ((carte > pile[-1]) or (carte == pile[-1] - 10))
        for pile in self.partie.piles_descendantes:
            jouable = jouable or ((carte < pile[-1]) or (carte == pile[-1] + 10))
        logger.debug(f"La carte {carte} est jouable : {jouable}")
        return jouable

    def canFinish(self) -> bool:
        """
        Renvoie ??? si un joueur a joué assez de cartes pour finir son tour (2 si sabot non vide, 1 sinon)
        :return:
        """
        logger.info(f"Appel de canFinish pour le joueur {self.id}")
        logger.debug(f"nombre de cartes jouées : {self.nb_carte_jouee()}, taille du sabot : {len(self.partie.sabot)}")
        return self.nb_carte_jouee() >= 1 + (len(self.partie.sabot) > 0)
