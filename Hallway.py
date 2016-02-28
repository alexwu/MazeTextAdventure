from Scene import Scene

class Hallway(Scene):

    def enter(self):
        
        light = False;
        
        print
        print "OH SHIT THIS HALLWAY IS DARK."
        print "HOW ARE YOU GOING TO DEAL WITH THIS, HUH?!"
        print "BY THE WAY YOU HAVE A MATCH. NEAT, HUH?"
        print '\n'

        while True:

            command = raw_input('> ')

            if command == "jump":
                print "With all your might, you jump straight up, determined", 
                print "to escape this dark and dreadful place."
                print "You fly through the ceiling of the room only be",
                print "vaporized in the dark void above."
                return "death"

            elif command == "light match" or command == "use match" or command == "match":
                if light == False:
                    print "The darkened room suddenly becomes illuminated by the", 
                    print "tiny match, revealing three doors in the room." 
                    print "One east, one west, and one north."
                    print "WHATCHA GONNA DO NOW, HUH?"
                    light = True
                else:
                    print "The match is already lit. Wtf are you doing (wo)man?"
            
            elif command == "look" or command == "look around":
                if light == False:
                    print "It's dark. Really dark. WHAT ELSE DO YOU WANT?!"

                else:
                    print "There's door to your in front of you, to your",
                    print "left, and to your right. That better?"
            
            elif command == "go left" or command == "go west":
                if light == False:
                    print "You walk straight into the wall and fall over.",
                    print "Feel dumb yet?"
                else:
                    print "You go into the left room without issues, but I",
                    print "haven't written that room yet, so enjoy your infinite loop"

            elif command == "go right" or command == "go east":
                if light == False:
                    print "You right to the right, only to trip over your own", 
                    print "shoelaces. Who doesn't tie their shoes these days?"
                else:
                    print "Oh man this door works! You open it! Prepare for doom!"
                    return 'combat'

            elif command == "go forward" or command == "go north":
                if light == False:
                    print "You run forward at full speed, only to be met"
                    print "by a door. Ouch."
                else:
                    print "You go into the northern room hopefully, but atm you're",
                    print "cause it ain't done. Luckily some really smart guy is"
                    print "working on it, so just wait! :D"
    
            else:
                print "idk what you just said. i'ma go get tacos now."

            print '\n'

            

