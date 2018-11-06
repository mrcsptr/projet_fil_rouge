# coding: utf-8
import re


class commentaires():
    """ Cette classe permet de créer un objet "commentaire".
    Ses méthodes permettent de contrôler et valider le contenu d'un commentaire fait sur un article du Wiki. """

    def __init__(self, nom, auteur_comment, date_comment, contenu_comment):
        self.nom = nom  # titre de l'article commenté
        self.auteur_comment = auteur_comment  # auteur du commentaire
        self.date_comment = date_comment  # date du commentaire
        self.contenu_comment = contenu_comment  # contenu du commentaire
        self.format = {'Auteur': self.auteur_comment, 'Contenu': self.contenu_comment, 'Article': self.nom}

    def contenu_commentControl(self):
        result = 0  # initialisation
        lower_mots_interdit = ["batârd", "bitch", "biatch", "con", "connasse", "couillon", "enfoiré", "fdp", "crétin",
                               "idiot"]  # liste de mots interdits
        mots_interdit = [elt.upper() for elt in lower_mots_interdit]  # mots interdis en majuscule
        cap_mots_interdit = [elt.capitalize() for elt in
                             lower_mots_interdit]  # mots interdis qui commencent par une majuscule
        mots_interdit.extend(cap_mots_interdit)  # fusion des listes
        mots_interdit.extend(lower_mots_interdit)
        for elt in mots_interdit:
            for mot in contenu_comment.split():
                if re.search(elt, mot) is None:
                    x = 0
                else:
                    x = 1
                result += x
        return str(result)

    def contenu_isValid(self):
        if self.contenu_commentControl == "0":
            return True
        else:
            return False