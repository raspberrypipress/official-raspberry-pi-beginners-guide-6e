#!/usr/bin/python3

# Ein einfaches Textadventure, das Sie mit Ihrem eigenen Code erweitern können

def show_instructions():
    # Zeige ein Hauptmenü und die möglichen Befehle
    print("""
Text Adventure
==============

Erreiche den Garten mit einem Schlüssel und Zaubertrank
Geh den Monstern aus dem Weg!

Befehle:
  gehenach [Richtung]
  nimm [Gegenstand]
""")

def show_status():
    # Zeige den aktuellen Zustand des Spielers
    print("---------------------------")
    print("Du bist im Zimmer: " + current_room)
    # Zeige das aktuelle Inventar
    print("Inventar : " + str(inventory))
    # Zeige einen Gegenstand an, wenn einer im Zimmer vorhanden ist
    if "Gegenstand" in rooms[current_room]:
        print("Du siehst einen " + rooms[current_room]['Gegenstand'])
    print("---------------------------")

# Das Inventar ist beim Start leer
inventory = []

# Ein Dictionary (Wörterbuch) verbindet ein Zimmer mit anderen Zimmern
rooms = {

    'Diele' : { 
        'süden' : 'Küche',
        'osten' : 'Speisezimmer',
        'Gegenstand' : 'Schlüssel'
    },

    'Küche' : {
        'norden' : 'Diele',
        'Gegenstand' : 'Monster'
    },

    'Speisezimmer' : {
        'westen' : 'Diele',
        'süden' : 'Garten',
        'Gegenstand' : 'Zaubertrank'
    },

    'Garten' : {
        'norden' : 'Speisezimmer'
    }



}

# Beim Start ist der Spieler in der Diele
current_room = 'Diele'

show_instructions()

# Ewige Schleife
while True:

    show_status()

   # Warte auf den 'nächsten Spielzug (die nächste Bewegung)' des Spielers
   # .split() teilt ihn in eine Liste (Array) auf
   # Wenn du z.B. 'gehenach osten' eintippst, erhältst du folgende Liste:
   # ['gehenach','osten']
    move = ''
    while move == '':
        move = input('>')

    move = move.split()

    # Wenn das Eingetippte mit 'gehenach' beginnt
    if move[0] == 'gehenach':
        # Prüfe, ob der Spieler auch dorthin gehen kann, wo er hin will
        if move[1] in rooms[current_room]:
            # Mache das neue Zimmer zum aktuellen Zimmer
            current_room = rooms[current_room][move[1]]
        # Es gibt keine Tür (Verbindung) zum neuen Zimmer
        else:
            print("You can't go that way!")

    # Wenn das Eingetippte mit 'nimm' beginnt
    if move[0] == 'nimm':
        # Wenn das Zimmer einen Gegenstand enthält, und du genau diesen
        # Gegenstand nehmen willst
        if ('Gegenstand' in rooms[current_room] 
              and move[1] in rooms[current_room]['Gegenstand']):
            # Füge den Gegenstand dem Inventar hinzu
            inventory += [move[1]]
            # Zeige eine hilfreiche Mitteilung
            print(move[1] + " wurde genommen!")
            # Lösche den Gegenstand vom Zimmer
            del rooms[current_room]['Gegenstand']
        # Andernfalls ist der Gegenstand nicht vorhanden 
        # und kann auch nicht genommen werden
        else:
            # Sage dem Spieler, dass er diesen Gegenstand nicht nehmen kann
            print("Du kannst " + move[1] + " nicht nehmen!")

    # Der Spieler verliert, wenn im Zimmer ein Monster ist
    if ('Gegenstand' in rooms[current_room]
          and 'Monster' in rooms[current_room]['Gegenstand']):
        print('Ein Monster hat dich erwischt... SPIEL AUS!')
        break

    # Mit Schlüssel und Zaubertrank entkommen, um zu gewinnen
    if (current_room == 'Garten' and 'Schlüssel' in inventory
          and 'Zaubertrank' in inventory):
       print('Du hast das Haus verlassen... DU GEWINNST!')
       break
