# coding: utf-8
import os
import re

class Commentaires ():
    """ Cette classe définit les commentaires effectués pour les articles du Wiki."""

    def __init__(self, contenu_commentaire= " "):
        self.titre_article = " "                  # attribut: nom de l'article à commenter
        self.auteur_commentaire = " "         # attribut: auteur du commentaire
        self.contenu_commentaire = contenu_commentaire                     # attribut: contenu du commentaire
        self.motif_control_comment = r" "                   # attribut: motif utilisé pour le controle admin des commentaire
        self.mots_interdit = ["Batârd", "Bitch", "Biatch", "Sale chienne", "Con", "Connasse", "Couillon", "Enfoiré", "Fais chié", "Fdp", "Fils de ****", "Ferme la"]        # dictionnaire de gros mots

    def getCommentaire (self):
        return self.contenu_commentaire

    def setCommentaire (self, contenu_commentaire):
        self.contenu_commentaire = contenu_commentaire

    def __repr__(self):
        print("commentaire: {0}".format(self.getCommentaire()))

    def afficher (self):
        print ( "commentaires", end=' ')

    def controle_ajout(self):
        res = 0
        for elt in self.mots_interdit :
            if re.search(elt, self.contenu_commentaire):
                x = 0
            else:
                x = 1
            res += x
        if res == 0 :
            return False
        else :
            return True


    def ajout_commentaire (self):
        if controle_ajout() == True :
            file_comments = open("comments.txt", "a")
            file_comments.write(self.contenu_commentaire)
            file_comments.close()
            return
        else :
            return setCommentaire(contenu_commentaire)

    def statut_affichage_commentaire (self):
        if ajout_commentaire () == True :
            return "Online"


    def supprimer_commentaire (self):
        return

    def controle_suppression (self):
        return

    def retour (self):
        return

    #nom_article = property(_get_titre_article, _set_titre_article, ._del_titre_article)


if __name__=='__main__':
    contenu_commentaire = input("Saisir commentaire : ")
    c = Commentaires(contenu_commentaire)
    print (Commentaires.controle_ajout())
    #c.getCommentaire()

