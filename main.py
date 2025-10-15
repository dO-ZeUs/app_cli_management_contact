"""Fonction principale | Menu"""
def main():
  """Choix fait par l'utilisateur dans le menu"""
  choice = 0
  while choice < 1 or choice > 6:
    print("====== GESTIONNAIRE DE CONTACTS ======")

    print ("1. Ajouter un contact")
    print ("2. Afficher tous les contacts")
    print ("3. Rechercher un contact")
    print ("4. Modiffier un contact")
    print ("5. Supprimer un contact")
    print ("6. Quitter")
    
    choice = int(input("Quelle tâche voulez-vous exécuter ?: "))  

"""Point d'entrée principale"""
if __name__ == '__main__':
  main()
  


  




