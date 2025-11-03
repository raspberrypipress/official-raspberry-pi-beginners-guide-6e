#!/bin/python3

# A simple text adventure you can enhance with your own code

def show_instructions():
    # print a main menu and the commands
    print("""
Text Adventure
==============
Get to the Garden with a key and a potion
Avoid the monsters!
Commands:
  go [direction]
  get [item]
""")

def show_status():
    # print the player's current status
    print("---------------------------")
    print("You are in the " + current_room)
    # show the current inventory
    print("Inventory : " + str(inventory))
    # show an item if there is one
    if "item" in rooms[current_room]:
        print("You see a " + rooms[current_room]['item'])
    print("---------------------------")

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

    'Hall' : { 
        'south' : 'Kitchen',
        'east' : 'Dining Room',
        'item' : 'key'
    },

    'Kitchen' : {
        'north' : 'Hall',
        'item' : 'monster'
    },
    'Dining Room' : {
        'west' : 'Hall',
        'south' : 'Garden',
        'item' : 'potion'
    },
    'Garden' : {
        'north' : 'Dining Room'
    }

}

# start the player in the Hall
current_room = 'Hall'

show_instructions()

# loop forever
while True:

    show_status()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[current_room]:
            # set the current room to the new room
            current_room = rooms[current_room][move[1]]
        # there is no door (link) to the new room
        else:
            print("You can't go that way!")

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want
        if ('item' in rooms[current_room] 
              and move[1] in rooms[current_room]['item']):
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + " got!")
            # delete the item from the room
            del rooms[current_room]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print("Can't get " + move[1] + "!")

    # player loses if they enter a room with a monster
    if ('item' in rooms[current_room]
          and 'monster' in rooms[current_room]['item']):
        print('A monster has got you... GAME OVER!')
        break

    # player wins if they get to the garden with a key and a potion
    if (current_room == 'Garden' and 'key' in inventory
          and 'potion' in inventory):
       print('You escaped the house... YOU WIN!')
       break