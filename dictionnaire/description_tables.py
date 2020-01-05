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
           {'nom' : 'Tables FF' , 
           'desc_table' : [{'TUP' : "Table Unifiée du Parcellaire - reconstitution des unités foncières et PDLMP"},
                           {'pnb10_parcelle' : "Table des parcelles"},
                           {'pb0010_local' : 'Table des locaux'},
                           {'proprietaire_droit' : "Table des droits des propriétaires sur chacuns de leurs biens"},
                           {'lots_locaux' : 'Table de correspondance entre les lots et les locaux'},
                           {'pb21_pev' : "Table des parties d'évaluation"},
                           {'pb30_pevexoneration' : "Table d'exonération des parties d'évaluation"},
                           {'pb36_pevtaxation' : "Table de taxation des parties d'évaluation"},
                           {'pb40_pevprincipale' : "Table des parties principales d'habitation"},
                           {'pb50_pevprofessionnelle' : "Table des parties d'évaluation professionnelles"},
                           {'pb60_pevdependances' : "Table des parties d'évaluation dépendances"},
                           {'pdl10_pdl' : "Table des propriétés divisées en lots"},
                           {'pdl20_parcellecomposante' : "Table des parcelles composantes"},
                           {'pdl30_lots' : "Table des lots de copropriété"},
                           {'pnb21_suf' : "Table des subdivisions fiscales"},
                           {'pnb30_sufexoneration' : "Table d'exonération des subdivisions fiscales"},
                           {'pnb36_suftaxation' : "Table de taxation des subdivisions fiscales"}]
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