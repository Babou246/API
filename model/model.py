
import mysql.connector as ps
class Model:
    host = ''
    database = ''
    user = ''
    password = ''
    curseur = ''
    #  CONECTION A LA BASE DE DONNÉE
    db = ps.connect(
                    host='localhost',
                    database='APIS',
                    user='root',
                    password='passer', 
                    connection_timeout=180
                    )
    curseur = db.cursor()

    
    curseur.execute('SET FOREIGN_KEY_CHECKS = 0')
    curseur.execute('SET FOREIGN_KEY_CHECKS = 1')
    db.commit()
