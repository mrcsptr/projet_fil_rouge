#main

# coding: utf-8

from flask import *
from flask_pymongo import PyMongo
from article import *
from users import *
import datetime
from commentaire import *
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
			line = "Erreur: désolé le pseudo que vous avez choisi existe déjà dans notre base de données! veuillez choisir un autre"
			return render_template('basic.html', line = line)

		email = request.form["mail"]        # récupération du mail
		b = []
		b.append(mongo.db.user.find_one({'email': email}))
		if b != [None]:  # vérifier si le mail existe dans la base
			line = "Erreur: désolé le mail que vous avez entré existe déjà dans notre base de données! Veuillez choisir un autre!"
			return  render_template('basic.html', line = line)
			
		newUser = users(request.form["Nom"],request.form["Pren"],pseudo,request.form["passd"],request.form["tel"],email) # création de l'objet user

		if newUser.isValid(): # tester les conditions sur les données entrées par l'utilisateur
			ajoutUser = mongo.db.demandes.insert(newUser.format) # ajouter la demande d'inscription à la base de donées dans la collections demandes
			line = "Votre demande d'inscription est envoyée à l'Admin du Wiki" # afficher à l'utilisateur un message que sa demande est envoyée
			return render_template('basic.html', line = line)
		else:
			line = "Erreur: Veuillez remplir correctement le formulaire d'inscription. Lire les conditions sur la saisie."
			return render_template('basic.html', line = line)
                        
	return render_template('inscription.html') # envoyer la page d'inscription

@app.route('/demande_inscription/')
def demande_inscrip():
	demande_inscr = []
	demande_inscr.append(mongo.db.demandes.find_one({"tel":{'$exists': True}}))
	if demande_inscr != [None]:
		return render_template("DemandesInscription.html",user = demande_inscr[0])
	else:
		line = "Il n' y a pas des nouvelles demandes d'inscriptions! Merci"
		return render_template('basic.html', line = line)


@app.route('/valider_inscription/', methods=['GET', 'POST'])
def valider_inscrip():
	if request.method == 'POST':
		demande_inscr = []
		demande_inscr.append(mongo.db.demandes.find_one({"tel":{'$exists': True}}))
		newUser = users(demande_inscr[0]["Nom"],demande_inscr[0]["Prenom"],demande_inscr[0]["Pseudo"],demande_inscr[0]["psswd"],demande_inscr[0]["tel"],demande_inscr[0]["email"])
		ajoutUser = mongo.db.user.insert(newUser.format) # ajouter un utilisateur à la base de données
		deleteUser = mongo.db.demandes.delete_one({"tel":demande_inscr[0]["tel"]})
		line = "Félicitation! Un nouveau utilisateur est ajouter à votre base de données"
		return render_template('basic.html', line = line)
	return render_template("valider_inscription.html")

@app.route('/refuser_inscription/', methods=['GET', 'POST'])
def annuler_inscrip():
	if request.method == 'POST':
		demande_inscr = []
		demande_inscr.append(mongo.db.demandes.find_one({"tel":{'$exists': True}}))
		for_del = demande_inscr[0]["tel"]
		deleteUser = mongo.db.demandes.delete_one({"tel":for_del}) 
		line = "Cette demande d'inscription est vient d'être supprimée de la liste des demandes"
		return render_template('basic.html', line = line)
	return render_template("refuser_inscription.html")

@app.route('/demande_ajout_article/')
def demande_ajout_art():
	demande_art = []
	demande_art.append(mongo.db.demandes.find_one({"Mots_cles":{'$exists': True}}))
	if demande_art != [None]:
		return render_template("demande_ajout_article.html",article = demande_art[0])
	else:
		line = "Il n' y a pas des nouvelles demandes d'ajout Article! Merci"
		return render_template('basic.html', line = line)
        
@app.route('/valider_ajout_article/', methods=['GET', 'POST'])
def valider_ajout_art():
	if request.method == 'POST':
		demande_art = []
		demande_art.append(mongo.db.demandes.find_one({"Mots_cles":{'$exists': True}}))
		newArt = article(demande_art[0]["Auteur"],demande_art[0]["Titre"],demande_art[0]["Mots_cles"],demande_art[0]["Contenu"],demande_art[0]["Categorie"],demande_art[0]["Date"])
		ajoutArt = mongo.db.articles.insert(newArt.format) # ajouter un utilisateur à la base de données
		deleteArt = mongo.db.demandes.delete_one({"Mots_cles":demande_art[0]["Mots_cles"]})
		line = "Félicitations! Un nouveau article est ajouté à votre base de données"
		return render_template('basic.html', line = line)
	return render_template("valider_ajout_article.html")

@app.route('/refuser_ajout_article/', methods=['GET', 'POST'])
def annuler_ajout_art():
	if request.method == 'POST':
		demande_art = []
		demande_art.append(mongo.db.demandes.find_one({"Mots_cles":{'$exists': True}}))
		for_del = demande_art[0]["Mots_cles"]
		deleteUser = mongo.db.demandes.delete_one({"tel":for_del}) 
		line = "Cette demande d'ajout article est vient d'être supprimer de la liste des demandes"
		return render_template('basic.html', line = line)
	return render_template("refuser_ajout_article.html")

@app.route('/seConnecter/', methods=['GET', 'POST'])
def seConnecter():
	if request.method == 'POST':
		pseudo = request.form["pseudo"]        # récupération du pseudo
		findUser = mongo.db.user.find_one({'Pseudo': request.form["pseudo"]})
		if findUser == None : 
			line = "Erreur: Aucun compte ne correspond à ce login/mdp. Veuillez créer un compte"
			return render_template('basic.html', line = line)
		elif findUser['Pseudo']== pseudo and findUser['psswd']== request.form["pass"] : 
			if findUser['Pseudo'] == 'Admin': 
				return render_template('espacePersoAdmin.html', pseudo=session[pseudo])
			else:
				return render_template('espacePerso.html', nom=findUser['Nom'], prenom=findUser['Prenom'], pseudo=session[pseudo], pwd=findUser['psswd'], tel=findUser['tel'], email=findUser['email'])   # on renvoit la page perso de l'utilisateur
		else: 
			line = "Erreur: Mot de passe / login incorrect. " 
			return render_template('basic.html', line = line)
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


@app.route('/demande_ajout_commentaire/')
def demande_ajout_comt():
    demande_comt = []
    demande_comt.append(mongo.db.demandes.find_one({"Article":{'$exists': True}}))
    if demande_comt != [None]:
        return render_template("demande_ajout_commentaire.html",commentaire = demande_comt[0])
    else:
        line = "Il n' y a pas des nouvelles demandes d'ajout commentaire! Merci"
        return render_template('basic.html', line = line)

		
@app.route('/valider_ajout_commentaire/', methods=['GET', 'POST'])
def valider_ajout_comt():
    if request.method == 'POST':
        demande_comt = []
        demande_comt.append(mongo.db.demandes.find_one({"Article":{'$exists': True}}))
        newComt = commentaires(demande_comt[0]["Auteur"],demande_comt[0]["Contenu"],demande_comt[0]["Date"],demande_comt[0]["Article"])
        ajoutComt = mongo.db.commentaires.insert(newComt.format) # ajouter un utilisateur à la base de données
        deleteComt = mongo.db.demandes.delete_one({"Article":demande_comt[0]["Article"]})
        line = "Félicitation! Un nouveau commentaire est ajouté à votre base de données"
        return render_template('basic.html', line = line)
    return render_template("valider_ajout_commentaire.html")

	
@app.route('/refuser_ajout_commentaire/', methods=['GET', 'POST'])
def annuler_ajout_comt():
    if request.method == 'POST':
        demande_comt = []
        demande_comt.append(mongo.db.demandes.find_one({"Article":{'$exists': True}}))
        for_del = demande_comt[0]["Article"]
        deleteComt = mongo.db.demandes.delete_one({"Article":for_del})
        line = "Cette demande d'ajout commentaire est vient d'être supprimée de la liste des demandes"
        return render_template('basic.html', line = line)
    return render_template("refuser_ajout_commentaire.html")
	
	
@app.route('/categories/')
def liste_categories():
	categories = mongo.db.articles.distinct('Categorie')			# récupère et classe chaque catégorie dans la collection d'articles
	return render_template('liste_categories.html', categories = categories) 							# page listant toutes les catégories existantes


@app.route('/categories/<chaine>/')
def articles_dunecategorie(chaine):
	nbr_artcateg = mongo.db.articles.find({'Categorie': chaine}).count()						# compte le nombre d'articles de la catégorie "chaine"
	artcateg = mongo.db.articles.find({'Categorie': chaine})	# récupère les titres d'articles d'une catégorie et les classe
	return render_template('liste_artcateg.html', nbr_artcateg = nbr_artcateg, artcateg = artcateg)		# page listant tous les articles de la catégorie sélectionnée
		

if __name__ == '__main__':
	app.run(debug=True)
