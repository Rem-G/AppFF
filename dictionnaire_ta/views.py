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
import csv
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.db.models.query import Q

from .description_tables import TABLES, lister_tables

from .models import Variable, OrdreTables


def accueil_doc(request):
    #Genere un tableau affichant la liste des tables principales
    context = {'tables' : TABLES}
    return render(request, 'accueil_ta.html', context)



def doc_table(request, table, variable_recherche):
    #Documentation d'une table
    nom_tables_permises = lister_tables()
    
    if table not in nom_tables_permises:
        raise Http404('Table inexistante')
       
    variables = Variable.objects.filter(table_associee = table).order_by('id')
    
    liste_ordre = ""
    ordre_table = OrdreTables.objects.filter(table = table)
    for ordre in ordre_table:
        liste_ordre = ordre.str_to_list
            
    return render(request, 'table_ta.html', locals())


def recherche(request):
    if request.method == 'POST':
        contexte_recherche = ContexteRechercheDoc(request.POST)                
        context = {'mots_clefs': contexte_recherche.mots_clefs,
                   'variables' : contexte_recherche.variables,}
        return render(request, 'recherche_doc_ta.html', context)
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