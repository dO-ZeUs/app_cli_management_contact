from contacts import Contact
import json

FILE = "contacts.json"

class ContactManager:
  """GESTION DU CARNET D'ADRESSE AVEC STOCKAGE JSON"""
  def __init__(self):
    self.contacts = {
      "contacts": [],
      "next_id": 1
    }
    
  def load_contacts(self):
    """CHARGER LES CONTACTS"""
    try:
      with open(FILE, "r", encoding="utf-8") as file:
        self.contacts = json.load(file)
    except (FileNotFoundError, ValueError):
      """Avec python 3.14, jsonDecodeError n'est plus pris en charge or elle hérite de ValueError d'où l'utilisation de cette dernière."""
      with open(FILE, "w", encoding="utf-8") as file:
        self.contacts = {
          "contacts": [],
          "next_id": 1
        }
        json.dump(self.contacts, file)
        print("Fichier créé avec succès !")

  def add_contact(self, name, firstname, phone, email, address, notes, date_ajout):
    """AJOUTER UN CONTACT"""
    if name == "" or firstname == "" or phone == "":
      """forcer l'utilisateur à remplir les champs "nom", "prenom" et "telephone" """
      print("Les champs nom, prénom et téléphone sont obligatoires !")
      return
    for c in self.contacts["contacts"]:
      """vérifier les doublons de contacts"""
      if c["nom"] == name or c["telephone"] == phone:
        print("Ce contact existe déjà !")
        return
    
    """ajoute le contact dans la liste de dictionnaires"""
    newContact = {
      "id": self.contacts["next_id"],
      "nom": name.upper(),
      "prenom": firstname.capitalize(),
      "telephone": phone,
      "email": email,
      "adresse": address,
      "notes": notes,
      "date_ajout": date_ajout
    }
    """ajouter le nouveau contact dans la liste de dictionnaire"""
    self.contacts["contacts"].append(newContact)

    """incrémenter le prochain id"""
    self.contacts["next_id"] += 1

    """sauvegarder le contact dans le fichier json"""
    self.save_contact()
    print(f"Contact '{firstname} {name}' a été ajouté avec succès !")


  def save_contact(self):
    """ajouter les données dans le fichier json"""
    with open (FILE, "w", encoding="utf-8") as file:
      json.dump(self.contacts, file, indent=2, ensure_ascii=False)
    print("Contacts sauvegardés avec succès !")
      
