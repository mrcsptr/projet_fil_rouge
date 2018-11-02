# coding: utf-8
import os
import re

class Commentaires ():
    """ Cette classe permet:
    - de soumettre un commentaire sur un articles du Wiki,
    - de contrôler le contenu du commentaire,
    - de valider un commentaire par l'admin; ce qui implique :
        - de publier le commentaire en bas de l'article,
        - de mettre à jour la base de données MongoDB.
        - de mettre à jour les stats dans l'espace personnel de l'utilisateur.
        - de mettre à jour l'historique des demandes de l'utilisateur."""

    def __init__(self, titre_article, URL_article, auteur_comment, contenu_comment):
        self.titre_article = titre_article              # attribut: titre de l'article commenté
        self.URL_article = URL_article                  # attribut: URL de l'article commenté
        self.auteur_comment = auteur_comment            # attribut: auteur du commentaire
        self.contenu_comment = contenu_comment          # attribut: contenu du commentaire
        self.motif_control_comment = r" "               # attribut: motif utilisé pour le controle admin des commentaire
        self.mots_interdit = ["Batârd", "Bitch", "Biatch", "Sale chienne", "Con", "Connasse", "Couillon", "Enfoiré", "Fais chié", "Fdp", "Fils de ****", "Ferme la"]        # dictionnaire de gros mots

    # Récupérer/fixer les informations

    def getComment (self):
        return self.contenu_comment

    def setComment (self, contenu_comment):
        self.contenu_comment = contenu_comment

    def getTitre (self):
        return self.titre_article

    def setTitre (self, titre_article):
        self.titre_article = titre_article

    def getURL_article (self):
        return self.URL_article

    def setURL_article (self, URL_article):
        self.URL_article = URL_article

    def getAuteurComment (self):
        return self.auteur_comment

    def setAuteurComment (self, auteur_comment):
        self.auteur_comment = auteur_comment

    # 1 er filtre: faire un controle gros mots

    def controlAuto(self):
        result = 0                           # initialisation
        lower_mots_interdit = ["batârd", "bitch", "biatch", "con", "connasse", "couillon", "enfoiré", "fdp", "crétin",
                               "idiot"]        # liste de mots interdits
        mots_interdit = [elt.upper() for elt in lower_mots_interdit]              # mots interdis en majuscule
        cap_mots_interdit = [elt.capitalize() for elt in lower_mots_interdit]     # mots interdis commençants par une majuscule
        mots_interdit.extend(cap_mots_interdit)             # fusion des listes
        mots_interdit.extend(lower_mots_interdit)

        for elt in mots_interdit:
            for mot in contenu_comment.split():
                if re.search(elt, mot) is None:
                    x = 0
                else:
                    x = 1
                result += x
        return str (result)

    def validationAuto (self):
        if self.controlAuto() == "0":
            return "OK"
        else:
            return "KO"

if __name__=='__main__':
    # Informations à récupérer via formulaire html et BD mongoDB
    titre_article = "à la belle étoile! "
    URL_article = "www.monWiki.io/article1"
    auteur_comment = "Fredia"
    contenu_comment = "Je trouve cet article super. CRÉTIN IDIOT Batârd Bitch fdp"

    # instanciation
    c = Commentaires(titre_article, URL_article, auteur_comment, contenu_comment)
    # test controle gros mots et 1er filtre
    print(c.controlAuto())
    print(c.validationAuto())
