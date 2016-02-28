from Scene import Scene


class BeginningRoom(Scene):

    def enter(self):
        print "You're in the start room! Congratulations motherfucker!"
        print "There's a door in front of you. It looks ominous."
        print "What the fuck could you possibly want to do now?"
        print '\n'

        while True:
            command = raw_input("> ")

            if command == "jump":
                print "You jump so high that your head crashes in to the ceiling"
                print "and you die a slow unfortunate death."
                return 'death'
            elif command == "open door":
                print "You turn the door knob and open the door slowly, "
                print "creaking as if it had been oiled by the devil."
                print "You're likely screwed."
                return "hallway"

            else:
                print "wow you dumb or something you can't do that"

            print '\n'
