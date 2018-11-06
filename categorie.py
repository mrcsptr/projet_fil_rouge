#classe catégories

# coding: utf-8
import re

class Categories ():
    """ Cette classe permet de créer un objet "catégorie".
    Ses méthodes permettent de contrôler et valider le contenu d'un champ catégorie à la création d'un article du Wiki. """
	
    def __init__(self, categorie):
        self.categorie = categorie                      # nom de la catégorie
        self.format = {'Catégorie': self.categorie}
		
    def categorieControl(self):
        result = 0  																								# initialisation
        lower_mots_interdit = ["bolosse", "salope", "bâtard", "con", "connasse", "couillon", "enfoiré", "pute"]		# liste de mots interdits
        mots_interdit = [elt.upper() for elt in lower_mots_interdit]												# mots interdits en majuscule
        cap_mots_interdit = [elt.capitalize() for elt in lower_mots_interdit]  										# mots interdits qui commencent par une majuscule
        mots_interdit.extend(cap_mots_interdit)																		# fusion des listes
        mots_interdit.extend(lower_mots_interdit)
        for elt in mots_interdit:
            for mot in categorie.split():
                if re.search(elt, mot) is None:
                    x = 0
                else:
                    x = 1
                result += x
        return str(result)
		
    def categorie_isValid (self):
        if self.categorieControl == "0":
            return True
        else:
            return False



