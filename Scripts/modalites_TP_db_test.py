import sqlite3

'''
Script permettant de faire l'association variables - descriptions de variable

IMPORTANT : Dans la base, les champs id_variable et id_descvariable doivent être des INTEGER
'''

def read_table_dictionnaire_variable(db_file):
    conn = sqlite3.connect(db_file)
    dict_table = dict()
    liste_dict_table = list()
     
    cur = conn.cursor()
    cur.execute("SELECT * FROM dictionnaire_variable")
 
    lignes = cur.fetchall()
 
    for ligne in lignes:
        dict_table['id'] = ligne[0]
        dict_table['nom'] = ligne[4]
        dict_table['table_associee'] = ligne[12]
        liste_dict_table.append(dict_table)
        dict_table = dict()
    
    return liste_dict_table

def read_table_dictionnaire_descvariable(db_file):
    conn = sqlite3.connect(db_file)
    dict_table = dict()
    liste_dict_table = list()
     
    cur = conn.cursor()
    cur.execute("SELECT * FROM dictionnaire_descvariable")
 
    lignes = cur.fetchall()
 
    for ligne in lignes:
        dict_table['id'] = ligne[0]
        dict_table['table_var_associee'] = ligne[7]
        liste_dict_table.append(dict_table)
        dict_table = dict()
    
    return liste_dict_table

def ecriture_modalites(db_file):
    compteur_modalites = 0
    table_variables = read_table_dictionnaire_variable(db_file)
    table_descriptions = read_table_dictionnaire_descvariable(db_file)
    
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    
    for ligne_table in table_variables:
        for ligne_desc in table_descriptions:
            if ligne_table['table_associee']+"_"+ligne_table['nom'] == ligne_desc['table_var_associee']:
                variable_id = int(ligne_table['id'])
                descvariable_id = int(ligne_desc['id'])
                sql = """INSERT INTO dictionnaire_variable_modalites VALUES(NULL, '{0}', '{1}')""".format(variable_id, descvariable_id)      
                cur.execute(sql)
                conn.commit()
                compteur_modalites += 1
                print("Modalité n°:", compteur_modalites, ligne_desc['table_var_associee'])
                
            if ligne_table['table_associee']+"_"+ligne_table['nom'][:len(ligne_table['nom'])-3] == ligne_desc['table_var_associee'] and ligne_table['nom'][::-1][:3] == 'txt':
                for k in table_variables:
                    if k['table_associee']+"_"+k['nom'] == ligne_desc['table_var_associee']:
                        variable_id = int(ligne_table['id'])
                        descvariable_id = int(ligne_desc['id'])
                        sql = """INSERT INTO dictionnaire_variable_modalites VALUES(NULL, '{0}', '{1}')""".format(variable_id, descvariable_id)      
                        cur.execute(sql)
                        conn.commit()
                        compteur_modalites += 1
                        print("Modalité n°:", compteur_modalites, ligne_desc['table_var_associee'], ligne_table['nom']) 
    conn.close()
    
ecriture_modalites('db_test.sqlite3')