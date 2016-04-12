#File: Start.py
#Author: Alexander Wu
#Purpose: Takes user input to create a new character or load a previous save
#         and launches the game.

import textwrap
from Map import Map
from Engine import Engine
from Player import Player

print textwrap.dedent("""\
        Hello! Welcome to my demo text adventure! Would you like to 
        (1) make a new character or (2) continue from a previous save?
        """)

while True:

    strInput = raw_input('1 or 2: ')

    #Create a new character
    if strInput == '1':
        print "What will be your new character's name? (One word please!)"
        player = Player(raw_input('> '))

        player.changeHealth(5)
        print "\nWelcome to the game " + player.getName() + "! Good luck!\n"
        break

    #Load previous character
    elif strInput == '2':
        print "\nWhat is your character's name?"
        
        while True:

            #Catches IOError in case file doesn't exist
            try:
                name = raw_input('> ')
                saveFile = open(name, 'r')
                break
            except IOError:
                print "This save file does not exist! Try again!"
        
        player = Player(name)
        player.readSave(saveFile)
        print "\nWelcome back " + player.getName() + "! Good luck!\n" 
        break

    else:
        print "\nInvalid option! Try again!"

    print

gameMap = Map()

#If player is past the start room, move player
if player.getLoc() != "beginning":
    gameMap.nextScene(player.getLoc())

gameInstance = Engine(gameMap)
gameInstance.play(player)
