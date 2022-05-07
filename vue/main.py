import sys
sys.path.append('.')
from controller.controller import Controller
from model.model import Model
# LES VUES DANS LE CONSOLES ==> life bi metiwul


running = True
while running:
    print("""
            1- Voir les elements d'une table aux choix
            2- Vider une table
            3- Voir les Users connectés
    """)
    m = Model()
    n = Controller()
    choix = int(input('Entrer un choix dans le menu\n'))
    if choix == 1:
        n.all()
    elif choix == 2:
        n.rollback()
    action = input('Appuyer Q|q pour quitter')
    if action == 'q' or action == 'Q':
        break
