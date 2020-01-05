#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Created on 25 juil. 2018

@author: remi.gosselin
'''

import xlrd
import sqlite3      
    
def xls2dictionnaire_ta_variable():
    """
    Ecrit le tableur xls dans la base de données (table dictionnaire_variable)
    L'écriture se fait à la suite, la table n'est pas supprimée auparavant 
    """
    classeur = xlrd.open_workbook('C:/Users/remi.gosselin/Desktop/categories_ccocac.xls')
    
    
    liste_tables = ['section', 'commune', 'canton', 'arrondissement', 'departement', 'region', 'carroyage100', 'carroyage', 'pdlmp', 'uf', 'batiment', 'carreaux_vides', 'TUP']

                                
    for feuille in classeur.sheet_names():
        
        if feuille != "":
            
            feuille_act = classeur.sheet_by_name(feuille)
    
            conn = sqlite3.connect('db.sqlite3')
            c = conn.cursor()

            description = code = valeur = str()
            cpt_ligne=0
    
            for i in range(feuille_act.nrows):
                ligne = feuille_act.row(i)

                for cell in ligne[:2]:
                    if len(ligne[:2][1].value) == 0:
                        description = str(ligne[:2][0].value).replace("'", "''")
                    elif len(ligne[:2][0].value) > 0 and len(ligne[:2][1].value) > 0: 
                        if len(cell.value) == 4:
                            code = str(cell.value).replace("'", "''")
                            cpt_ligne +=1
                        else:
                            valeur = str(cell.value).replace("'", "''")
                            cpt_ligne = 0
                        if cpt_ligne == 0:
                            sql = """INSERT INTO dictionnaire_descvariable VALUES(NULL, '{0}', '{1}', '{2}', '2017-', '{3}', '{4}', '')""".format(code, valeur, description, "ccocac", "pb21_pev_ccocac")
                            c.execute(sql)
                            conn.commit()
                            print(description, code, valeur)
                            code = valeur = str()

    conn.close()
    
if str(input("Envoyer xls tables principales vers base ? /!\ Si des données sont déjà présentes dans la table, ces dernières ne seront pas supprimées /!\ [y/n]" )) == "y":
    xls2dictionnaire_ta_variable()
else:
    print("Execution interrompue")
        
        




