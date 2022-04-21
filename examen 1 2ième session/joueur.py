###################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Exam 1 joueur d'hockey
###  Nom: Simon Lacaille
###  Description du fichier: classe pour joueurs d'hockey
####################################################################################


class hockey:
    """
    Classe hockey
    """
    ###################################
    #####  constructeur avec paramètre et valeur de défaut  #####
    ###################################
    def __init__(self,n_de_joueur = "Tremblay",p_de_joueur = "Jean-François",age_de_joueur = 10,sur_de_joueur = "Flash",):
     """
       défénir les attributs donner dans la fonction
       méthode avec constructeur et valeur
     """
     self.__nom_joueur = n_de_joueur
     self.__prenom_joueur = p_de_joueur
     self.__age = age_de_joueur
     self.surnom = sur_de_joueur

     ############################################
              #####  méthode str  #####
     ############################################

    def __str__(self):
        """
        utilser avec fonction print() dans le programme principal
        :return: la chaine à mettre dans le programme principal
        """

        affiche = "\nNom du joueur :" + self.__nom_joueur
        affiche += "\nPrénom du joueur :" + self.__prenom_joueur
        affiche += "\nÂge du joueur :" + str(self.__age)
        affiche += "\nsurnom du joueur :" + self.surnom
        return affiche

    ############################################
    #####  ACCÈS ET PROPRIÉTÉS  #####
    ############################################

     # attribut nom de joueur
    # accès pour attribut nom de joueur
    def __getnom_joueur(self) -> str :
        """
        pour accéder à l'attribut no de joueur
        :return: str
        """
        return self.__nom_joueur

    # Mutateur AnneeParution
    def __setnom_joueur(self, n_de_joueur: str) -> None:
        """
        assigner une valeur
        :param n_de_joueur à valider
        :return: None
        """
        if len(n_de_joueur) < 26:
            self.__nom_joueur = n_de_joueur

    # propriété du nom du joueur
    nom_joueur = property(__getnom_joueur, __setnom_joueur)

    # accès pour attribut prénom de joueur
    def __getprenom_joueur(self) -> str:
        """
        pour accéder à l'attribut prenom de joueur
        :return: str
        """
        return self.__prenom_joueur

    # Mutateur AnneeParution
    def __setprenom_joueur(self, p_de_joueur: str) -> None:
        """
        assigner une valeur
        :param p_de_joueur à valider
        :return: None
        """
        if len(p_de_joueur) < 26:
            self.__prenom_joueur = p_de_joueur

    # propriété du nom du joueur
    prenom_joueur = property(__getprenom_joueur, __setprenom_joueur)

    # accès pour attribut prénom de joueur
    def __getage(self) -> int:
        """
        pour accéder à l'attribut age de joueur
        :return: int
        """
        return self.__age

    # Mutateur AnneeParution
    def __setage(self, age_de_joueur: int) -> None:
        """
        assigner une valeur
        :param age_de_joueur à valider
        :return: None
        """
        if age_de_joueur > 0:
            self.__age = age_de_joueur

    # propriété du nom du joueur
    age = property(__getage,__setage)