import textwrap
from Scene import Scene

class Hallway(Scene):

    def enter(self, player):
      
        player.setLoc('hallway')
        
        if not player.getItem(0):
            player.addItem(0)

        player.writeSave()

        print
        if player.getState(0):
            print textwrap.dedent("""\
                    You enter an empty room with four doors, one leading
                    to the beginning room, and in the west, north, and east
                    directions.
                    """)

        else:
            print textwrap.dedent("""\
                    HOLY CRAP THIS HALLWAY IS DARK.
                    HOW ARE YOU GOING TO DEAL WITH THIS, HUH?!
                    BY THE WAY YOU HAVE A MATCH. NEAT, HUH?
                    """)
        print

        while True:

            command = raw_input('> ')

            if command == "info":
                player.printInfo()

            elif command == "jump":
                print textwrap.dedent("""\
                        With all your might, you jump straight up, determined 
                        to escape this dark and dreadful place.
                        You fly through the ceiling of the room only be
                        vaporized in the dark void above.
                        """)
                return "death"

            elif command == "light match" or command == "use match" or command == "match":
                if not player.getState(0):
                    if player.getItem(0):
                        print textwrap.dedent("""\
                                The darkened room suddenly becomes illuminated
                                by the tiny match, revealing three doors in
                                the room. One east, one west, and one north.
                                WHATCHA GONNA DO NOW, HUH?
                                """)
                        player.changeState(0, True)
                else:
                    print "The match is already lit. Wtf are you doing?"
            
            elif command == "look" or command == "look around":
                if not player.getState(0):
                    print "It's dark. Really dark. WHAT ELSE DO YOU WANT?!"

                else:
                    print textwrap.dedent("""\
                            There's door to your in front of you, to your
                            left, and to your right. That better?
                            """)
            
            elif command == "go left" or command == "go west":
                
                if not player.getState(0):
                    print textwrap.dedent("""\
                            You walk straight into the wall and fall over.
                            Feel dumb yet?
                            """)
                else:
                    print textwrap.dedent("""\
                            You go into the left room without issues, but I
                            haven't written that room yet, so enjoy your infinite loop
                            """)

            elif command == "go right" or command == "go east":
                
                if not player.getState(0):
                    print textwrap.dedent("""\
                            You right to the right, only to trip over your own
                            shoelaces. Who doesn't tie their shoes these days?
                            """)
                else:
                    print "Oh man this door works! You open it! Prepare for doom!"
                    return 'combat'

            elif command == "go forward" or command == "go north":
                
                if not player.getState(0):
                    print textwrap.dedent("""\
                            You run forward at full speed, only to be met
                            by a door. Ouch.
                            """)
                else:
                    print textwrap.dedent("""\
                            You go into the northern room hopefully, but atm you're
                            stuck cause it ain't done. Luckily some really smart guy is"
                            working on it, so just wait! :D
                            """)
            else:
                print "idk what you just said. i'ma go get tacos now."

            print

