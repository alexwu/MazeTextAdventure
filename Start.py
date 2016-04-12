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
    if strInput == '1':
        print "What will be your new character's name?"
        player = Player(raw_input('> '))

        player.changeHealth(5)
        print "\nWelcome to the game " + player.getName() + "! Good luck!\n"
        break
    elif strInput == '2':
        print "\nWhat is your character's name?"
        
        while True:
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
if player.getLoc() != "beginning":
    gameMap.nextScene(player.getLoc())

gameInstance = Engine(gameMap)
gameInstance.play(player)


