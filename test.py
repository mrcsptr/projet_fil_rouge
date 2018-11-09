# coding: utf-8

from commentaire import *
import datetime

newComment = commentaires('panda', 'BoBlennon', datetime.datetime.now(),
                              'blabla')
							  
print(newComment.format)
print(newComment.contenu_commentControl())
print(newComment.contenu_isValid())

chaine = 'panda'

def ajouterCommentaire(chaine):
	newComment = commentaires(chaine, 'BobLennon', datetime.datetime.now(),
                              'blabla')
	if newComment.contenu_isValid():
		print('ça marche')  # page à renvoyer
#		else:
#			return render_template(
#           'template_FormArticle.html')  # page à renvoyer   / à modifier pour afficher message d'erreur


ajouterCommentaire(chaine)