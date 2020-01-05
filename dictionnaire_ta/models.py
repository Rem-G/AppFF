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

class Variable(models.Model):
    """
    Class des variables des tables principales, récupère les valeurs associées aux champs de la table 
    """
    numero = models.IntegerField()
    nom = models.CharField(max_length = 255, null = True, blank=True)
    description = models.TextField(null = True, blank=True)
    observation = models.TextField(null = True, blank=True)
    formule_ini = models.CharField(max_length = 255, null = True, blank=True)
    origine = models.CharField(max_length = 255, null = True, blank=True)
    nature = models.CharField(max_length = 255, null = True, blank=True)
    lgr = models.CharField(max_length = 255, null = True, blank=True)
    table_associee = models.CharField(max_length = 255)
    
    
    def __str__(self):
        return self.nom + ' (' + self.table_associee + ')'
    
    @property
    def nature_variable(self):
        if self.nature=='X':
            nature='Caractère('+str(self.lgr)+')'
        elif self.nature=='Xt':
            nature='Tableau de caractères'
        elif str(self.nature)=='9' or str(self.nature)=='9.0':
            nature='Entier'
        elif self.nature=='9t':
            nature='Tableau de numériques'
        elif self.nature=='G':
            nature='Géométrie'
        else :
            nature='Non spécifié'
    
        return nature
    
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
            if cpt != 2 and i not in ["'", "[", "]", ",", " "]:
                mot += i
            if cpt == 2:
                cpt = 0
                liste_mots.append(mot.replace("'", ""))
                mot = ""
                
        return liste_mots
