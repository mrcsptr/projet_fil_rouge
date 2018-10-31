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
				
	def setNom(self, nom):
		self.nom = nom
		
	def getNom(self):
		return self.nom
		
	def setAuteur(self, auteur):
		self.auteur =auteur
		
	def getAuteur(self, auteur):
		return self.auteur
		
	def setDate(self, date):
		self.date = date
		
	def getDate(self):
		return self.date	
		
	def setContenu(self, contenu):
		self.contenu = contenu
		
	def getDate(self):
		return self.contenu	
		
	def setCategorie(self, categorie):
		self.categorie = categorie
		
	def getCategorie(self):
		return self.categorie
		
	def setKeywords(self, keywords):
		self.keywords = keywords
	
	def getKeywords(self):
		return keywords

def afficherArticle(self):
	