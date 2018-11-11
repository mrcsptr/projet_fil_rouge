#main

# coding: utf-8

from flask import *
from flask_pymongo import *
from article import *
from users import *
import datetime
from commentaire import *
from users import *
import re

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/wiki"
mongo = PyMongo(app)
app.secret_key = 'my secret key'  # clé secrète et unique à fixer pour pouvoir 
# utiliser la messagerie flash. Cette messagerie utilise un mécanisme de stockage 
# de la session pour contenir les messages entre les demandes. Il disparaîtra la 
# prochaine fois qu'on arrive à la page automatiquement.

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		article = mongo.db.articles.find_one({'Titre': request.form['search']}) # recherche de l'article dans la base
		if article is None:
			return render_template('index.html')
		else:
			return redirect(url_for('connexion_article', chaine = article['Titre'])) # redirection vers la page de l'article
	return render_template('index.html') # affichage page d'accueil
	

<<<<<<< HEAD
@app.route('/conditions/', methods=['GET', 'POST'])
def conditions():
	return render_template('conditions.html')

@app.route("/inscription/", methods=['Get','Post'])
def inscription():

        if request.method == 'POST':
                pseudo = request.form["pseudo"]        # récupération du pseudo
                a = []
                a.append(mongo.db.user.find_one({'Pseudo': pseudo}))
                if a != [None]: # vérifier si le pseudo existe dans la base
                        return "Erreur: désolé le pseudo que vous avez choisi existe déjà dans notre base de données! veuillez choisir un autre"

                email = request.form["mail"]        # récupération du mail
                b = []
                b.append(mongo.db.user.find_one({'email': email}))
                if b != [None]:  # vérifier si le mail existe dans la base
                        return "Erreur: désolé le mail que vous avez entré existe déjà dans notre base de données! veuillez choisir un autre!"

                
                newUser = users(request.form["Nom"],request.form["Pren"],pseudo,request.form["passd"],request.form["tel"],email) # création de l'objet user

                if newUser.isValid(): # tester les conditions sur les données entrées par l'utilisateur
                        ajoutUser = mongo.db.demandes.insert(newUser.format) # ajouter la demande d'inscription à la base de donées dans la collections demandes
                        return "Votre demande d'inscription est envoyée à l'Admin du Wiki" # afficher à l'utilisateur un message que sa demande est envoyée
                else:
                        return "Erreur: Veuillez remplir correctement le formulaire d'inscription. Lire les conditions sur la saisie."
                        
        return render_template('inscription.html') # envoyer la page d'inscription
=======
@app.route('/inscription/', methods=['GET', 'POST'])
def sInscrire():
	if request.method == 'POST':
		pseudo = request.form["pseudo"]        # récupération du pseudo
		if pseudo in session:                  # si le pseudo était déjà enrégistré
			return " Le login que vous avez saisi, existe déjà. Veuillez en choisir un autre."     
		else:
			session[pseudo] = pseudo			# si le pseudo n'était pas encore enregistré
			session[mdp] = mdp           		# si le pseudo n'était pas encore enregistré			
			newUser = users(request.form["nom"],request.form["prenom"], pseudo , request.form["pass"] , request.form["tel"], request.form["mail"] ,image = "images.png")
			if newUser.isValid():
				ajoutUser = mongo.db.users.insert_one(newUser.afficher())
				return render_template('NewespacePerso.html', pseudo=session[pseudo])    # on renvoit la page perso du nouvel utilisateur avec le message bienvenue
			else:
				return "Erreur: Veuillez remplir correctement le formulaire d'inscription. Lire les conditions sur les saisies."
	return render_template('inscription.html')
>>>>>>> upstream/master


@app.route('/seConnecter/', methods=['GET', 'POST'])
def seConnecter():
	if request.method == 'POST':
		pseudo = request.form["pseudo"]        # récupération du pseudo
<<<<<<< HEAD
		findUser = mongo.db.users.find_one({'pseudo': pseudo})
		if findUser == None : 
			return "Erreur: Aucun compte ne correspond à ce login/mdp. Veuillez créer un compte"     
		elif findUser['pseudo']== pseudo and findUser['mdp']== request.form["pass"] : 
=======
		findUser = mongo.db.users.find_one({'Pseudo': request.form["pseudo"]})
		if findUser == None : 
			return "Erreur: Aucun compte ne correspond à ce login/mdp. Veuillez créer un compte"     
		elif findUser['Pseudo']== request.form["pseudo"] and findUser['psswd']== request.form["pass"] :
>>>>>>> upstream/master
			return render_template('espacePerso.html', pseudo=session[pseudo])   # on renvoit la page perso de l'utilisateur
		else: 
			return "Erreur: Mot de passe / login incorrect. "    
	return render_template('seConnecter.html')
	
@app.route('/<chaine>/', methods=['GET', 'POST'])
def connexion_article(chaine):
	article = mongo.db.articles.find_one({'Titre': chaine}) # recherche de l'article dans la base
	return render_template('article.html', article = article) # redirection vers la page de l'article

@app.route('/ajouterArticle/', methods=['GET', 'POST'])
def ajouterArticle():
	if request.method == 'POST': # création article
		newArticle = article(request.form["titre_article"],request.form["Auteur_name"], datetime.datetime.now(), 
			request.form["contenu_article"], request.form["categorie_article"], request.form["Mots_cles_article"])
		if newArticle.isValid(): # vérification que l'article est valide
			ajoutArticle = mongo.db.articles.insert_one(newArticle.format)
			return render_template('temp_Conf_soumissionArticle.html')
		else:
			return render_template('template_FormArticle.html')
			
	return render_template('template_FormArticle.html')
	

@app.route('/<chaine>/commentaires/', methods=['GET', 'POST'])
def ajouterCommentaire(chaine):
	if request.method == 'POST':
		newComment = commentaires(chaine, request.form["Auteur_comment"], datetime.datetime.now(),
                              request.form["contenu_comment"])   # création d'un nouvel objet commentaire avec les information saisies par l'utilisateur
		if newComment.contenu_isValid():
			ajoutComment = mongo.db.commentaires.insert_one(newComment.format)    # on rajoute les nouvelles informations saisies dans la base de données commentaires
			return render_template('temp_Conf_soumissionComment.html')  # on renvoit la page de confirmation de soumission du commentaire.
		else:
			return render_template(
           'template_FormArticle.html')  # on renvoit la page de l'article # à modifier...
	
	comment = mongo.db.commentaires.find({'Article': chaine})   # on récupère la liste de tous les commentaires de l'article.
	return render_template('template_FormCommentaires.html', comment = comment)  # page à consulter pour récupérer les informations nécessaires


@app.route('/categories/')
def liste_categories():
	categories = mongo.db.articles.find().distinct('Categorie')		# récupère et classe chaque catégorie dans la collection d'articles
	return render_template('liste_categories.html', categories = categories) 							# page listant toutes les catégories existantes

	
@app.route('/categories/<chaine>/')
def articles_dunecategorie(chaine):
	print(chaine)
	nbr_artcateg = mongo.db.articles.find({'Categorie': chaine}).count()						# compte le nombre d'articles de la catégorie "chaine"
	artcateg = mongo.db.articles.find({'Categorie': chaine}) 	# récupère les titres d'articles d'une catégorie et les classe
	return render_template('liste_artcateg.html', nbr_artcateg = nbr_artcateg, artcateg = artcateg, chaine = chaine)		# page listant tous les articles de la catégorie sélectionnée
	
	
if __name__ == '__main__':
	app.run(debug=True)
