from datetime import datetime
import re

class Contact:
  """INITILISATION DE CONTACT"""
  def __init__(self, id, name, firstname, phone, email="", address="", notes=""):
    verifyPhone = r"/^(?:(?:\+|00)229[\s.-]{0,3}(?:\(0\)[\s.-]{0,3})?|0)[1-9](?:(?:[\s.-]?\d{2}){4}|\d{2}(?:[\s.-]?\d{3}){2})$/"
    """valider le format du téléphone"""
    if not re.match(verifyPhone, phone)  or len(phone) != 10:
      raise ValueError("Numéro de téléphone invalide !")
    
    """valider les champs vides"""
    if not email or not address or not notes:
      email = "Non défini"
      address = "Non défini"
      notes = "Non défini"

    """valider le format de l'email"""
    if email and not re.match(r"^[a-zA-Z0-9'_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
      raise ValueError("Email invalide !")
    

    self.id = id
    self.name = name
    self.firstname = firstname
    self.phone = phone
    self.email = email 
    self.address = address
    self.notes = notes
    self.date_ajout = datetime.now()


  def __str__(self):
    return (
      f"ID: {self.id}\n"
      f"Nom: {self.name}\n"
      f"Prénom: {self.firstname}\n"
      f"Phone: {self.phone}"
      f"Email: {self.email}"
      f"Adresse: {self.address}"
      f"Notes: {self.notes}"
      f"Ajouté le: {self.date_ajout.strftime("%d/%m/%y %H:%M")}"
      f"{"-"}"*20
    )  
  
    
