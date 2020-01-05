'''

Copyright ou © ou Copr. Cerema, (juillet 2018) 

fichiers-fonciers@cerema.fr

Ce logiciel est un programme informatique servant à l'utilisation de la donnée FF

Ce logiciel est régi par la licence CeCILL soumise au droit français et
respectant les principes de diffusion des logiciels libres. Vous pouvez
utiliser, modifier et/ou redistribuer ce programme sous les conditions
de la licence CeCILL telle que diffusée par le CEA, le CNRS et l'INRIA 
sur le site "http://www.cecill.info".

En contrepartie de l'accessibilité au code source et des droits de copie,
de modification et de redistribution accordés par cette licence, il n'est
offert aux utilisateurs qu'une garantie limitée.  Pour les mêmes raisons,
seule une responsabilité restreinte pèse sur l'auteur du programme,  le
titulaire des droits patrimoniaux et les concédants successifs.

A cet égard  l'attention de l'utilisateur est attirée sur les risques
associés au chargement,  à l'utilisation,  à la modification et/ou au
développement et à la reproduction du logiciel par l'utilisateur étant 
donné sa spécificité de logiciel libre, qui peut le rendre complexe à 
manipuler et qui le réserve donc à des développeurs et des professionnels
avertis possédant  des  connaissances  informatiques approfondies.  Les
utilisateurs sont donc invités à charger  et  tester  l'adéquation  du
logiciel à leurs besoins dans des conditions permettant d'assurer la
sécurité de leurs systèmes et ou de leurs données et, plus généralement, 
à l'utiliser et l'exploiter dans les mêmes conditions de sécurité. 

Le fait que vous puissiez accéder à cet en-tête signifie que vous avez 
pris connaissance de la licence CeCILL, et que vous en avez accepté les
termes.

'''

from django.db import models
from builtins import property
    
class DescVariable(models.Model):
    """
    Class de la description de variables, récupère les valeurs associées aux champs de la table  dictionnaire_descvariable
    """
    #Récupère les valeurs des variables dans la table
    code = models.CharField(max_length = 255, null = True, blank=True)
    valeur = models.CharField(max_length = 255, null = True, blank=True)
    description = models.TextField(null = True, blank=True)
    observation = models.TextField(null = True, blank=True)
    millesime = models.CharField(max_length = 255, null = True, blank=True)
    var_associee = models.CharField(max_length = 255, null = True, blank=True)
    table_var_associee = models.CharField(max_length = 255, null = True, blank=True)
    
    def __str__(self):
        return self.code + ' - ' + self.var_associee + ' (' + self.table_var_associee + ')'
    
    @property
    def int_code(self):
        try :
            code_convert=int(float(self.code))
        except :
            code_convert=self.code
        return code_convert
        
    
    @property
    def decrypt_syntax_millesime(self):
        """
        Interprète la syntaxe jusque_millesime depuis_millesime de la table dictionnaire_descvariable
        """
        depuis_millesime = 2009
        jusque_millesime = None
        
        if self.millesime != None:
    
            # AAAA- (Depuis millésime)
            if len(self.millesime) == 5 and self.millesime[4] == "-":
                depuis_millesime = self.millesime[:4]
                jusque_millesime = None
            # AAAA-AAAA (Depuis millésime - jusque millésime)
            elif len(self.millesime) == 9 and self.millesime[4] == "-":
                depuis_millesime = self.millesime.split("-")[0]
                jusque_millesime = self.millesime.split("-")[1]
            # AAAA-AAAA|AAAA- (Depuis millésime et depuis millesime jusque millesime)
            elif "|" in self.millesime:
                depuis_millesime = self.millesime.split("|")[0]+" et depuis "+self.millesime.split("|")[1].split("-")[0]
                if self.millesime.split("|")[1].split("-")[1] == "":
                    jusque_millesime = None
                else:
                    jusque_millesime = self.millesime.split("|")[1].split("-")[1]
    
        return depuis_millesime, jusque_millesime

    
class Variable(models.Model):
    """
    Class des variables des tables principales, récupère les valeurs associées aux champs de la table 
    """
    #Récupère les valeurs des variables dans la table
    numero = models.IntegerField(null = True, blank=True)
    lgr = models.CharField(max_length = 255, null = True, blank=True)
    nat = models.CharField(max_length = 255, null = True, blank=True)
    nom = models.CharField(max_length = 255, null = True, blank=True)
    description = models.TextField(null = True, blank=True)
    observation = models.TextField(null = True, blank=True)
    origine = models.CharField(max_length = 255, null = True, blank=True)
    type = models.CharField(max_length = 255, null = True, blank=True)
    millesime = models.CharField(max_length = 255, null = True, blank=True)
    fiabilite = models.TextField(null = True, blank=True)
    doc = models.CharField(max_length = 255, null = True, blank=True)
    table_associee = models.CharField(max_length = 255, null = True, blank=True)
    modalites = models.ManyToManyField(DescVariable, blank = True)
    
    def __str__(self):
        return self.nom + ' (' + self.table_associee + ')'
    
    @property
    def url_doc(self):
        #Si doc existe, récupère la page associée au guide ou la fiche variable
        if self.doc != None:
            if self.doc.startswith("Doc"):
                return "guide.pdf#page="+self.doc.split()[1]
            elif self.doc.startswith("Fiche"):
                return "fiche_"+ self.doc.split()[1]+".pdf"
        return ''
        
    @property
    def decrypt_syntax_millesime(self):
        """
        Interpète la syntaxe de la colonne millesime pour l'afficher selon les variables depuis_millesime et jusque_millesime
        """
        depuis_millesime = 2009
        jusque_millesime = None
        
        if self.millesime != None:
    
            #AAAA- (Depuis millésime)
            if len(str(self.millesime)) == 5 and str(self.millesime[4]) == "-":
                depuis_millesime = self.millesime[:4]
                jusque_millesime = None
            #AAAA-AAAA (Depuis millésime - jusque millésime)
            elif len(str(self.millesime)) == 9 and str(self.millesime[4]) == "-":
                depuis_millesime = self.millesime.split("-")[0]
                jusque_millesime = self.millesime.split("-")[1]
            #AAAA-AAAA|AAAA- (Depuis millésime et depuis millesime jusque millesime)
            elif "|" in str(self.millesime):
                depuis_millesime = self.millesime.split("|")[0]+" et depuis "+self.millesime.split("|")[1].split("-")[0]
                if self.millesime.split("|")[1].split("-")[1] == "":
                    jusque_millesime = None
                else:
                    jusque_millesime = self.millesime.split("|")[1].split("-")[1]
    
        return depuis_millesime, jusque_millesime
    
    @property
    def modalite_variable(self):
        """
        Récupère toutes les modalites des variables
        """
        modalites_tables = self.modalites.all() 
        liste = []
        for variable_desc in enumerate(modalites_tables):
            liste.append(variable_desc[1])
        return liste
    
    @property
    def url_modalite(self):
        url_mod = None
        #Dans la liste des modalités, si une modalite existe alors variable_desc sera différent de []
        for variable_desc in enumerate(self.modalites.all()):
            if variable_desc[1] != []:
                url_mod = "/ff/doc_fftp/variable/"+self.table_associee+"/"+self.nom
        return url_mod
    
    @property
    def millesimes_dispo(self):
        # commentaire à rajouter
        liste_millesimes = [2009, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
        liste_millesimes_var = list()
        
        depuis_millesime = 2009
        jusque_millesime = None
        
        if self.millesime != None:
    
            # 2009- et AAAA-
            if len(str(self.millesime)) == 5 and self.millesime[4] == "-":
                for k in liste_millesimes:
                    if k >= int(self.millesime[:4]):
                        liste_millesimes_var.append(int(k))
            #AAAA-AAAA
            elif len(str(self.millesime)) == 9 and self.millesime[4] == "-":
                liste_millesimes_var.append(int(self.millesime.split("-")[0]))
                for k in liste_millesimes[liste_millesimes.index(int(self.millesime.split("-")[0])):]:
                    if k <= int(self.millesime.split("-")[1]):
                        liste_millesimes_var.append(int(k))
            #AAAA-AAAA | AAAA- (ex : De 2009 à 2014 et depuis 2015)
            elif "|" in str(self.millesime):
                liste_millesimes_var.append(int(self.millesime.split("|")[0]))
                if self.millesime.split("|")[1].split("-")[1] == "":
                    for k in liste_millesimes:
                        if k >= int(self.millesime.split("|")[1].split("-")[0]):
                            liste_millesimes_var.append(int(k))
            #AAAA-AAAA | AAAA- (ex : De 2009 à 2014 et depuis 2015)
            elif "|" in str(self.millesime):
                liste_millesimes_var.append(int(self.millesime.split("|")[0]))
                if self.millesime.split("|")[1].split("-")[1] == "":
                    for k in liste_millesimes:
                        if k >= int(self.millesime.split("|")[1].split("-")[0]):
                            liste_millesimes_var.append(int(k))
                else:
                    for k in liste_millesimes:
                        if k >= int(self.millesime.split("|")[1].split("-")[1]):
                            liste_millesimes_var.append(int(k))
                        
        return liste_millesimes_var
            
class OrdreTables(models.Model):
    liste = models.CharField(max_length = 2550, null = True, blank=True)
    table = models.CharField(max_length = 2550, null = True, blank=True)

    @property
    #Impossible de stocker type list dans base de données donc str_to_lits recrée la liste
    def str_to_list(self):  
        cpt = 0
        mot = ""
        liste_mots = list()
        for i in list(self.liste):
            if i == "'":
                cpt+=1
            elif cpt != 2 and i not in ["'", "[", "]", ",", " "]:
                mot += i
            elif cpt == 2:
                cpt = 0
                liste_mots.append(mot.replace("'", ""))
                mot = ""
        return liste_mots
