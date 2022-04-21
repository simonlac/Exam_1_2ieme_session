###################################################################################
###  420-2G2-HU - Programmation orientée objet
###  Travail: Exam 1 joueur d'hockey
###  Nom: Simon Lacaille
###  Description du fichier: classe pour joueurs d'hockey
### méthode d'ajout de commentaire basée sur exemple montrer par le prof
####################################################################################

#######################################
###  IMPORTATIONS - portée globale  ###
#######################################
import joueur as H

##########################################################
###  ajout de la liste ###
##########################################################
l_joueur_hockey = []

#######################################
######avant le programme principal DÉFINITIONS DES FONCTIONS ######
#######################################
def joueur_de_base() -> None:
    """
    fonction est utilisé pour mettre des valeurs de base dans la liste
    :return: None
    """
def InstanciationDejoueurs() :
    """
    Fonction qui permet de créer et d'instancier quelques objets Livre au démarage de l'appli
    :return: None
    """

    #Instanciation d'objets Livre et ajout dans une liste
    #Ici, le constructeur est appelé avec des valeurs pour chacun de ses paramètres
    #En créant les objets de cette façon, il est impératif de s'assurer que les valeurs sont valides et qu'elles
    #   respectent les conditions. Exemple: L'année de parution ne peut pas être supérieure à l'année en cours.
    l_joueur_hockey.append(
        H.hockey("Crosby","Sydney",34,"Sid le Kid"))
    l_joueur_hockey.append(
        H.hockey("Price", "Carey", 35, "Jesus Price"))
    return l_joueur_hockey

def ajouter_un_joueur() -> None:
    """
    ajout de nouveau joueur
    :return: None
    """
    # Entrée du nom du joueur
    while True:
        while True:
            try:
                playername = input("Entrez le nom de famille de votre joueur : ")
            except int:
                print("ERREUR! Une valeur en lettre est nécéssaire. Recommencez...")
            else:
                break

        # La valeur entrée est assignée et passe par la propriété
        hockey_.nom_joueur = playername

        # Vérification si la validation de valeur est OK
        if hockey_.nom_joueur != playername:  # On lit la valeur donc l'accesseur (get) est appelé
            print("La valeur n'est pas bonne reccomencer s'il vous plaît")
        else:
            print("Le nom a été accepté.")
            break
 # Entrée du prénom du joueur
    while True:
        while True:
            try:
                playersurname = input("Entrez le prénom de votre joueur : ")
            except int:
                print("ERREUR! Une valeur en lettre est nécéssaire. Recommencez...")
            else:
                break

        # La valeur entrée est assignée et passe par la propriété
        hockey_.prenom_joueur = playersurname

        # Vérification si la validation de valeur est OK
        if hockey_.prenom_joueur != playersurname:  # On lit la valeur donc l'accesseur (get) est appelé
            print("La valeur n'est pas bonne reccomencer s'il vous plaît")
        else:
            print("Le prénom a été accepté.")
            break
        # Entrée de l'âge
    while True:
        while True:
            try:
                playerage = int(input("Entrez l`âge de votre joueur : "))
            except:
                print("ERREUR! Une valeur en nombre est nécéssaire. Recommencez...")
            else:
                break

        # La valeur entrée est assignée et passe par la propriété
        hockey_.age = playerage

        # Vérification si la validation de valeur est OK
        if hockey_.age != playerage:  # On lit la valeur donc l'accesseur (get) est appelé
            print("La valeur n'est pas bonne reccomencer s'il vous plaît")
        else:
            print("L'âge a été accepté.")
            break
    playernickname = input("entrez le surnom du joueur")

#################################
###### PROGRAMME PRINCIPAL ######
#################################

# montre la liste déjà existant
InstanciationDejoueurs()
#donne le choix

option = input("entrez l'option a pour afficher b pour ajouter c pour le plus vieux ou d pour quitter : ").upper()

while option == "D":
    break
if option == "B"  :
     hockey_ = H.hockey()

     ajouter_un_joueur()

     # Ajout dnas la liste
     l_joueur_hockey.append(hockey_)

     # Affichage du dernier joueur entré
     print(hockey_)

     print()
     option = input("Voulez-vous entrer un nouveau joueur? \nEntrez O pour oui Entrez A pour afficher la liste de joueur v le joueur le plus vieux ou Q pour quitter : ")
     print()
while option == "A" :
        # Affichage de la liste de joueur
        print("#" * 30)
        print("Liste des joueurs représentée")
        print("#" * 30)
        for objhockey in l_joueur_hockey:
            print(objhockey)
            print("*" * 30)
