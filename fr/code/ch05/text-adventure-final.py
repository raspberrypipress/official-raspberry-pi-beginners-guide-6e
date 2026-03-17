#!/bin/python3

# Une aventure textuelle simple que tu peux améliorer avec ton propre code

def show_instructions():
    # affiche un menu principal et les commandes
    print("""
Text Adventure
==============

Atteins le jardin avec la clé et la potion
Évite les monstres !

Commandes:
  aller [direction]
  prendre [objet]
""")

def show_status():
    # affiche l'état actuel du joueur
    print("---------------------------")
    print("Tu es dans le/la " + current_room)
    # affiche l'inventaire actuel
    print("Inventaire : " + str(inventory))
    # affiche un objet s'il y en a un
    if "objet" in rooms[current_room]:
        print("Tu vois un/une " + rooms[current_room]['objet'])
    print("---------------------------")

# un inventaire, qui est initialement vide
inventory = []

# un dictionnaire liant une pièce à d'autres pièces
rooms = {

    'Hall' : { 
        'sud' : 'Cuisine',
        'est' : 'Salle à manger',
        'objet' : 'clé'
    },

    'Cuisine' : {
        'nord' : 'Hall',
        'objet' : 'monstre'
    },

    'Salle à manger' : {
        'ouest' : 'Hall',
        'sud' : 'Jardin',
        'objet' : 'potion'
    },

    'Jardin' : {
        'nord' : 'Salle à manger'
    }

}

# démarre le joueur dans le Hall
current_room = 'Hall'

show_instructions()

# loop forever
while True:

    show_status()

    # obtenir la prochaine action du joueur
    # .split() le divise en un tableau de liste
    # ex en tapant 'aller est' donnerait la liste:
    # ['aller','est']
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()

    # si il tape 'aller' en premier
    if move[0] == 'aller':
        # vérifie qu'ils sont autorisés peu importe où ils souhaitent aller
        if move[1] in rooms[current_room]:
            # définis la pièce actuelle à une autre pièce
            current_room = rooms[current_room][move[1]]
        # il n'y a pas de porte (lier) à une autre pièce
        else:
            print("Tu ne peux pas aller par là !")

    # s'ils tapent 'prendre' en premier
    if move[0] == 'prendre':
        # si la pièce contient un objet, et l'objet est celui qu'ils souhaitent obtenir
        if 'objet' in rooms[current_room] and move[1] in rooms[current_room]['objet']:
            # ajoute l'objet à leur inventaire
            inventory += [move[1]]
            # affiche un message utile
            print(move[1] + " got!")
            # supprime l'objet de la pièce
            del rooms[current_room]['objet']
        # sinon, si l'objet n'est pas là
        else:
            # leur indiquer qu'ils ne peuvent pas l'avoir
            print("Vous ne pouvez pas l avoir " + move[1] + " !")

    # le joueur perd la partie s'il y a un monstre dans la pièce
    if ('objet' in rooms[current_room]
          and 'monstre' in rooms[current_room]['objet']):
        print('Un monstre t\'a attrapé... TU AS PERDU !')
        break

    # atteins le jardin avec la clé et la potion pour gagner
    if (current_room == 'Jardin' and 'clé' in inventory
          and 'potion' in inventory):
       print('Tu as quitté la maison... TU AS GAGNÉ !')
       break
