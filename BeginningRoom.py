#File: BeginningRoom.py
#Author: Alexander Wu
#Purpose: Implements the starting room of the game.


import textwrap
from Scene import Scene

class BeginningRoom(Scene):

    def enter(self, player):
       
        #Autosave on entry of room
        player.writeSave()

        print textwrap.dedent("""\
            You're in the start room! Congratulations dude!
            There's a door in front of you. It looks ominous.
            What the hell do you want to do now?
            """)

        while True:
            command = raw_input("> ")

            if command == "jump" or command == "quit":
                print textwrap.dedent("""\
                      You jump so high that your head crashes in to the ceiling
                      and you die a slow unfortunate death.
                      """)
                return 'death'
            elif command == "open door":
                print textwrap.dedent("""\
                    You turn the door knob and open the door slowly
                    creaking as if it had been oiled by the devil.
                    You're likely screwed.
                    """)
                return "hallway"

            else:
                print "wow you dumb or something you can't do that"
            print
