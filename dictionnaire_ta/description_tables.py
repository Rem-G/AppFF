#!/usr/bin/env python
#-*- coding: utf-8 -*-
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

# Dictionnaire décrivant les tables DVF+ et DV3F
TABLES = [
           {'nom' : 'Tables agrégées FF' , 
           'desc_table' : [{'TUP' : "Table unifiée du parcellaire"},
                           {'carroyage100' : "Table carroyage 100m"},
                           {'commune' : 'Table des communes'},
                           {'section' : "Table des sections"},
                           {'canton' : 'Table des cantons'},
                           {'arrondissement' : "Table des arrondissements"},
                           {'departement' : "Table des départements"},
                           {'region' : "Table des régions"},
                           {'carroyage' : "Table des carroyages"},
                           {'pdlmp' : "Table des pdlmp"},
                           {'uf' : "Table des unités foncières"},
                           {'batiment' : "Table des bâtiments"},
                           {'carreaux_vides' : "Table des carreaux vides"}]
           }
          ]

def lister_tables():
    nom_tables = []
    for groupe in TABLES:
        descriptions = groupe['desc_table']
        for description in descriptions:
            for nom in description.keys():
                nom_tables.append(nom)        
    return nom_tables


#eof