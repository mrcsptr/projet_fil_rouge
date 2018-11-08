# Class utilisateurs

# coding: utf-8

from PIL import Image # Pour utiliser PIL il faut installer Pillow
import re


class users:

    def __init__(self,nom,pren,pseudo,psw,tel,mail,image = "images.png"):
        self.nom = nom
        self.pren = pren
        self.pseudo = pseudo
        self.psw = psw
        self.tel = tel
        self.mail = mail
        self.image = image
        self.re_nom = re.compile("^[A-Za-z]+(-[A-Za-z]*)*$")   # mon: on peut mettre que des lettres
        self.re_pren = re.compile("^[A-Z][a-z]+(-[A-Z][a-z]*)*$") # prenom : on peut mettre que des lettres
        self.re_tel = re.compile("^[0][1-9]([-._]?[0-9]{2}){4}$") # tel: il commence par 0, on peut séparer chque deux chiffres par -ou_ou. total = 10 chiffres
        self.re_mail = re.compile(r"^\w(.)*[a-zA-Z]+[\.a-zA-Z]*(\.fr)$") # que des mails .fr, il ne faut pas oublier le @
        self.re_image = re.compile(r"(\.png|\.jpeg|\.jpg)$") # format images accéptées: png,jpeg et jpg


    def getImage(self):
        return(Image.open("self.image"))

    def valid_nom(self):
        if self.re_nom.search(self.nom)is not None:
            return True
        else:
            return False
        
    def Valid_pren(self):
        if self.re_pren.search(self.pren)is not None:
            return True
        else:
            False
            
    def Valid_tel(self):
        if self.re_tel.search(self.tel)is not None:
            return True
        else:
            return False
        
    def Valid_mail(self):
        if self.re_mail.search(self.mail)is not None:
            return True
        else:
            return False
        
    def Valid_image(self):
        if self.re_image.search(self.image)is not None:
            return True
        else:
            return False

    def isValid(self):
        a= self.valid_nom() and self.Valid_pren() and self.Valid_tel() and self.Valid_mail() and self.Valid_image()
        if a:
            return True
        else:
            return False

# Afficher nom et prénom du User:
    def affichage(self):
        return "Pseudo = {}\n nom: {}\n prenom: {}\n".format(self.pseudo, self.nom,self.pren)


        
