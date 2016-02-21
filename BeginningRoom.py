from Scene import Scene


class BeginningRoom(Scene):

    def enter(self):
        print "You're in the start room! Congratulations motherfucker!"
        print "There's a door in front of you. It looks ominous."
        print "What the fuck could you possibly want to do now? \n"

        while True:
            command = raw_input("> ")

            if command == "jump":
                print "You jump so high that your head crashes in to the ceiling"
                print "and you die a slow unfortunate death. \n"
                return 'death'
            elif command == "open door":
                print "You turn the door knob and open the door slowly, "
                print "creaking as if it had been oiled by the devil."
                print "You're likely screwed."

            else:
                print "wow you dumb or something you can't do that \n"
