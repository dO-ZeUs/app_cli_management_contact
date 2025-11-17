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

  def display_contacts(self):
    """fonction : AFFICHER LES CONTACTS"""
    if not self.contacts["contacts"]:
      print("Fichier vide : aucun contact enrégistré !")
      return

    for c in self.contacts["contacts"]:
      print(f"ID: {c["id"]}\n")
      print(f"Nom: {c["nom"]}\n")
      print(f"Prénom: {c["prenom"]}\n")
      print(f"Phone: {c["telephone"]}\n")
      print(f"Email: {c["email"]}\n")
      print(f"Adresse: {c["adresse"]}\n")
      print(f"Notes: {c["notes"]}\n")
      print(f"Ajouté le: {c["date_ajout"]}\n")
      print(f"{"-"}"*40)



  def search_contact(self, name, firstname):
    """fonction : RECHERCHER UN CONTACT"""
    for c in self.contacts["contacts"]:
      if name.upper() == c["nom"] or firstname.capitalize() == c["prenom"]:
        print(f"ID: {c["id"]}\n")
        print(f"Nom: {c["nom"]}\n")
        print(f"Prénom: {c["prenom"]}\n")
        print(f"Phone: {c["telephone"]}\n")
        print(f"Email: {c["email"]}\n")
        print(f"Adresse: {c["adresse"]}\n")
        print(f"Notes: {c["notes"]}\n")
        print(f"Ajouté le: {c["date_ajout"]}\n")
        print(f"{"-"}"*40)
        return
      if not name.upper() == c["nom"] and not firstname.capitalize() == c["prenom"]:
        print("Aucun contact trouvé !")
        return


  def update_contact(self):
    """fonction: MODIFIER UN CONTACT"""
    search_phone = input("Entrer le numéro à rechercher: ")
    found = False
    for c in self.contacts["contacts"]:
      if c["telephone"] == search_phone:
        found = True
        """si le contact a été trouvé"""
        print("Contact trouvé !")
        print(f"{"="}"*40)
        print(f"Nom: {c["nom"]}\n")
        print(f"Prénom: {c["prenom"]}\n")
        print(f"Phone: {c["telephone"]}\n")
        print(f"Email: {c["email"]}\n")
        print(f"Adresse: {c["adresse"]}\n")
        print(f"Notes: {c["notes"]}\n")
        print(f"Ajouté le: {c["date_ajout"]}\n")
        print(f"{"-"}"*40)
        
        print("======== MODIFIER UN CONTACT ========")
        """donner la main à l'utilisateur pour modification"""
        new_name = input("Nouveau nom: ").strip()
        if new_name != "":
          c["nom"] = new_name
        new_firstname = input("Nouveau prénom: ").strip()
        if new_firstname != "":
          c["prenom"] = new_firstname
        new_phone = input("Nouveau numéro de téléphone: ").strip()
        if new_phone != "":
          """vérifier si ce numéro existe déjà"""
          for other in self.contacts["contacts"]:
            if other["telephone"] == new_phone and other != c:
              print("Ce numéro de téléphone existe déjà !")
              break       
          c["telephone"] = new_phone
        new_email = input("Nouveau mail: ").strip()
        if new_email != "":
          c["email"] = new_email
        new_address= input("Nouvelle adresse: ").strip()
        if new_address != "":
          c["adresse"] = new_address
        new_notes= input("Nouveau statut(VIP|Standard): ").strip()
        if new_notes != "":
          c["notes"] = new_notes
        """confirmer la modification du contact"""
        confirm_modif = input("Voulez-vous vraiment apporter ces modifications ? O/N: ")
        if confirm_modif.upper() == "O":
          self.save_contact()
          print("Contact modifié avec succès !")
        else:
          print("Modification annulée")
        return
    """dans le cas où le numéro entré n'existe pas"""    
    if not found:
      print("Contact non trouvé !")
      return
    

  def delete_contact(self):
    """fonction: SUPPRIMER UN CONTACT"""
    delete_phone = input("Entrer le numéro de téléphone à supprimer: ")
    found_contact = None
    for c in self.contacts["contacts"]:
      if c["telephone"] == delete_phone:
        found_contact = c
        print(f"{"="}"*40)
        print(f"Nom: {c["nom"]}\n")
        print(f"Prénom: {c["prenom"]}\n")
        print(f"Phone: {c["telephone"]}\n")
        print(f"Email: {c["email"]}\n")
        print(f"Adresse: {c["adresse"]}\n")
        print(f"Notes: {c["notes"]}\n")
        print(f"Ajouté le: {c["date_ajout"]}\n")
        print(f"{"-"}"*40)

        delete_contact = input("Supprimer vraiment ce contact ? O/N: ").strip()
        if delete_contact.upper() == "O":
          self.contacts["contacts"].remove(found_contact)
          self.save_contact()
          print("Contact supprimé avec succès !")
        else:
          print("Suppression annulée !")
        return
    if found_contact is None:
      print("Contact non trouvé !")
      return
        

          

        

  
  
        
      
        
      
      

      
