from Scene import Scene

class BeginningRoom(Scene):

  def enter(self):
    print "You're in the start room! Congratulations motherfucker!"
    print "What the fuck could you possibly want to do now? \n"

    command = raw_input("> ")

    if command == "jump":
      print "You jump so high that your head crashes in to the ceiling"
      print "and you die a slow unfortunate death. \n"
      return 'death'

    else:
      print "wow you dumb or something you can't do that \n"
      return 'beginning'
