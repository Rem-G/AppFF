'''

Copyright ou © ou Copr. Cerema, (juillet 2018) 

fichiers-fonciers@cerema.fr

Ce logiciel est un programme informatique servant à l'utilisation de la donnée FF

Ce logiciel est régi par la licence CeCILL soumise au droit français et
respectant les principes de diffusion des logiciels lib res. Vous pouvez
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
import re
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.db.models.query import Q
from django.contrib.auth.decorators import login_required

from .description_tables import TABLES, lister_tables
from .models import Variable, OrdreTables
from appff.settings import BASE_DIR


@login_required
def dump(request):
    import os
    os.system(os.path.join(BASE_DIR, 'dumpdata.sh'))
    return HttpResponse('Dump terminé')

def accueil_tables(request):
    #Page d'accueil -> choix tables principales / tables agregees
    return render(request, 'accueil_tables.html')


def accueil_doc(request):
    #Genere un tableau affichant la liste des tables principales
    context = {'tables' : TABLES}
    return render(request, 'accueil.html', context)

def doc_table(request, table, url_millesime, variable_recherche):
    #correspond au niveau du tableau dune table
    #table et url_millesime proviennent de l'url
    #Si la table est innexistante, renvoie une erreur
    if table not in lister_tables():
        raise Http404('Table inexistante')
    
    #Si aucun millésime spécifique est demandé, affiche multi-millesime
        
    liste_ordre = ""
    ordre_table = OrdreTables.objects.filter(table = table)
    for ordre in ordre_table:
        liste_ordre = ordre.str_to_list
    
    #Récupère les objets de la classe Variable en fonction de la table (récupérée par l'url)  et les trie par id
    variables = Variable.objects.filter(table_associee = table).order_by('id')    
    liste_variables_millesime = list()

    liste_millesimes = [2009, 2011, 2012, 2013, 2014, 2015, 2016, 2017]#Ajouter année nouveau millesime pour modifer menu choix millesime

    for var in variables:
        #Dans le aucun où aucun millesime n'est demandé, affiche multi-millesime
        if url_millesime == "Multi":
            liste_variables_millesime.append(var)
        else:
            #Si le millesime demandé est présent dans la liste des millesimes de la variable, alors celle-ci est ajoutée
            try:
                if int(url_millesime) in var.millesimes_dispo:
                    liste_variables_millesime.append(var)
            except:
                raise Http404('Erreur de millésime')

    try:
        url_millesime = int(url_millesime)
    except:
        pass

    return render(request, 'table.html', locals())
    # locals renvoie toutes les variables de la fct doc_table

def desc_var(request, table, variable):
    #Si la table est innexistante, renvoie une erreur
    if table not in lister_tables():
        raise Http404('Table inexistante')
    #Récupère les objets de la classe Variable en fonction de la table (récupérée par l'url)  et les trie par id
    variables_desc_var = Variable.objects.filter(nom = variable).filter(table_associee = table).order_by('id')
    
    #Verifie si la variable existe
    if len(variables_desc_var) == 0:
        raise Http404('Variable inexistante')
    
    #Verifie si des modalites existent pour la variable concernée 
    #variables_desc_var est un QuerySet, le [0] permet de récuperer sa valeur
    variable = variables_desc_var[0]
    variable_desc = variable.modalite_variable
    #Conditions de vérification d'existence de modalités
    if variable_desc is None or len(variable_desc) == 0:
        raise Http404('Pas de modalités pour cette variable')
    
    return render(request, 'table_desc.html', locals())


def recherche(request):
    if request.method == 'POST':
        contexte_recherche = ContexteRechercheDoc(request.POST)                
        context = {'mots_clefs': contexte_recherche.mots_clefs,
                   'variables' : contexte_recherche.variables,}
        return render(request, 'recherche_doc.html', context)
    else:
        raise Http404('Méthode POST incorrecte')

class ContexteRechercheDoc():

    def __init__(self, post):
        self.variables = []
        self.mots_clefs = '' 
        if 'motclef' in post:
            self.recherche(post['motclef'])
    
    def recherche(self, motclef):
        mots_clefs = self.decoupage(motclef)
        self.variables = self.resultat(mots_clefs)
        self.mots_clefs = ' '.join(mots_clefs)
    
    def decoupage(self, motclef):
        mots_clefs = re.findall(r'[\w]+',str(motclef))
        return [mot for mot in mots_clefs if (mot != '' and len(mot) >= 2)]
    
    def resultat(self, mots_clefs):
        y = Q()
        for mot in mots_clefs:
            y = y & (Q(nom__icontains=mot) | Q(description__icontains=mot))
        return Variable.objects.filter(y).distinct().order_by('nom')



