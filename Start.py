from Map import Map
from Engine import Engine
from Player import Player

print "Hello! Welcome to my demo text adventure! Would you like to (1) make a new"
print "character or (2) continue from a previous save?"

while True:

    strInput = raw_input('1 or 2: ')
    if strInput == '1':
        print "What will be your new character's name?"
        player = Player(raw_input('> '))

        player.changeHealth(5)
        print "Welcome to the game " + player.name + "! Good luck!"
        break
    elif strInput == '2':
        print "What is your character's name?"
        
        while True:
            try:
                name = raw_input('> ')
                saveFile = open(name, 'r')
                break
            except IOError:
                print "This save file does not exist! Try again!"
        
        player = Player(name)
        player.readSave(saveFile)
        print "Welcome back " + player.name + "! Good luck!"
        break
    else:
        print "Invalid option! Try again!"


gameMap = Map()
if player.getLoc() != "beginning":
    gameMap.nextScene(player.getLoc())

gameInstance = Engine(gameMap)
gameInstance.play(player)


