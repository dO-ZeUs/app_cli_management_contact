"""FONCTION main.py EST LA FONCTION PRINCIPALE DE L'APPLICATION"""

"""AFFICHAGE DU MENU PRINCIPAL"""   

def afficherMenu():
  print("============== GESTION DES CONTACTS ==============")
  print("1. Ajouter un contact")
  print("2. Afficher tous les contacts")
  print("3. Rechercher un contact")
  print("4. Modifier un contact")
  print("5. Supprimer un contact")
  print("6. Quitter")


def main():
  while True:
    afficherMenu()
    choix = int(input("Votre choix: "))

    if choix == 1:
      pass
    elif choix == 6:
      print("Au revoir !")
      break
    else:
      print("Choix invalide : veuillez rééssayer !")
      afficherMenu()
      choix = int(input("Votre choix: "))


if __name__ == "__main__":
  main()


  
    