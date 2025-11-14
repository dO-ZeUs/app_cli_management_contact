from contacts_manager import ContactManager
from datetime import datetime

gestionnaire = ContactManager()

def displayMenu():
  """AFFICHAGE DU MENU PRINCIPAL"""   
  print("============== GESTION DES CONTACTS ==============")
  print("1. Ajouter un contact")
  print("2. Afficher tous les contacts")
  print("3. Rechercher un contact")
  print("4. Modifier un contact")
  print("5. Supprimer un contact")
  print("6. Quitter")


def main():
  """FONCTION main.py EST LA FONCTION PRINCIPALE DE L'APPLICATION"""
  while True:
    gestionnaire.load_contacts()
    displayMenu()
    choice = int(input("Votre choix : "))

    if choice == 1:
      """AJOUTER UN CONTACT"""
      print("======== AJOUTER U CONTACT ========")    
      name = input("Nom: ")
      firstname = input("Prénom: ")
      phone = input("Téléphone: ")
      email = input("Email: ")
      address = input("Adresse: ")
      notes = input("VIP|STANDARD: ")
      date = datetime.now()
      date_ajout = date.strftime("%d/%m/%y %H:%M")

      gestionnaire.add_contact(name, firstname, phone, email, address, notes, date_ajout)

    elif choice == 2:
      """AFFICHER TOUS LES CONTACTS"""
      print("======== AFFICHER TOUS LES CONTACTS ========")
      gestionnaire.display_contacts()

    elif choice == 3:
      """RECHERCHER UN CONTACT"""
      print("======== RECHERCHER UN CONTACT ========")
      name = input("Entrez le nom: ")
      firstname = input("Entrez le prénom: ")
      
      gestionnaire.search_contact(name, firstname)

    elif choice == 4:
      """MODIFIER UN CONTACT"""
    elif choice == 5:
      """SUPPRIMER UN CONTACT"""
    elif choice == 6:
      """QUITTER L'APP"""
      print("Au revoir !")
      break
    else:
      print("Choix invalide : choix entre (1-6) !")
      displayMenu()
      choix = int(input("Votre choix: "))


if __name__ == "__main__":
  main()


  
    