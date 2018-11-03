#classe article

# coding: utf-8

class article:

	def __init__(self, nom, auteur, date, contenu, categorie, keywords):
		self.nom = nom
		self.auteur = auteur
		self.date = date
		self.contenu = contenu
		self.categorie = categorie
		self.keywords = keywords
		self.format = 	{'Auteur': self.auteur , 'Titre': self.nom, 'Mots_cles': self.keywords,'Contenu': self.contenu, 'Categorie': self.categorie}	


	def nameControl(self):
		if self.nom != '':
			return True
		else:
			return False
			
	def auteurControl(self):
		if self.auteur != '':
			return True
		else:
			return False
			
	def keywordsControl(self):
		if self.keywords != '':
			return True
		else:
			return False
			
	def contenuControl(self):
		if self.contenu != '':
			return True
		else:
			return False
			
	def categorieControl(self):
		if self.categorie != '':
			return True
		else:
			return False		

	def isValid(self):
		check = [self.nameControl(), self.auteurControl(), self.keywordsControl(), self.contenuControl(), self.categorieControl()]
		if all(check):
			return True
		else:
			return False
	