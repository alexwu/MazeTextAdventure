from Scene import Scene
from Death import Death
from Player import Player
from sys import exit
from random import randint

class CombatRoom(Scene):

    def enter(self, player):

        player.setLoc("combat")
        print "Saving...",
        player.writeSave()
        print "DONE"

        enemy_health = 5
        charging = False
        
        print
        print "You enter a room a well lit room with nothing but a lone,"
        print "dark figure standing at the center. The figure stands facing the"
        print "opposing end of the room, wearing a grey hoodie and dark green"
        print "basketball shorts. Currently, he does not appear to be dangerous."
        print '\n'

        while True:

            if player.getHealth() == 0:
                return "death"
            
            command = raw_input("> ")
            print

            if command == "jump":
                print "You begin to squat very low, focusing all of your chi into"
                print "your lower body. You look up, thinking about all of the"
                print "mysteries above. You have to escape this place. 'Why me?',"
                print "you think to yourself. A tear begins to form in the corner of"
                print "your left eye, as you think of how long you have been trapped"
                print "in this god awful place. Suddenly, you hear a loud ripping sound"
                print "from beneath you! You realize your pants have ripped, leaving"
                print "you know protection from what lies ahead. Hopelessness grabs hold"
                print "of your heart as you die a slow and painful death."
                print

                return "death"

            elif command == "approach figure" or command == "approach" or command == "go forward":
                print "Hearing your footsteps, the dark figure slowly turns to face you."
                print "As the figure's face comes into view, you realize the wide, deathly"
                print "grin on his face. With his eyes wide open, his pupils make contact"
                print "with yours, sending shivers down your spine. The man sticks his hand"
                print "down his pocket and slowly draws his weapon. Now holding a sword as"
                print "large as the man himself, the man began shreaking. 'I AM THE WARDEN"
                print "OF THIS DOMAIN. VACATE THIS SHELTER NOW.'"
                print "A green lightsaber materializes in your hands, as you stand waiting"
                print "to fight your foe."
                print

                while player.getHealth() > 0 and enemy_health > 0:
                    print "Health: ", player.getHealth()
                    print "Enemy Health: ", enemy_health
                    print "Combat Options:"
                    print "\t1.) Attack"
                    print "\t2.) Block"
                    print "\t3.) Counter"
                    print

                    enemy_move = randint(0, 9)
                    command = raw_input("What do you do? ")
                    print

                    if enemy_move < 3:
                        print "The dark figure snarls as he raises his sword and charges"
                        print "toward you like a bull. You ",

                        if command == "Attack" or command == "attack" or command == "1":
                            print "slash out at the figure as he comes into range, but you are unable"
                            print "to stop the sheer power of his attack, as you are thrown against the"
                            print "wall and feel your resolve weakening."
                            #player.Health = health - 1
                            player.changeHealth(-1)

                        elif command == "Block" or command == "block" or command == "2":
                            block_success = randint(0, 3)

                            if block_success == 0:
                                print "plant your feet, raise your self, and brace yourself for impact."
                                print "The collision only moves you back a few inches, but the failed attack"
                                print "attempt has not done any real harm."
                            else:
                                print "are knocked to the ground by his mighty attack. He spits on you"
                                print "and then proceeds to kick you in the nuts repeatedly for the"
                                print "next couple of minutes"
                                #health = health - 2
                                player.changeHealth(-2)

                        elif command == "Counter" or command == "counter" or command == "3":
                            counter_success = randint(0,2)

                            if counter_success == 0:
                                print "dodge just as he comes within range and stab him multiple times in the back."
                                print "The man makes a petrifying sound no normal human can take. The snarl on his face"
                                print "intensifies, clearly in pain."
                                enemy_health = enemy_health - 2
                            else:
                                print "mistime your dodge as he stabs you in the stomach and burps nonstop"
                                print "into your eyes. You scream in pain as your eyes feel as if they're"
                                print "starting to melt. Jesus man, that kind of sucks."
                                #health = health - 3
                                player.changeHealth(-3)

                        else:
                            print "stand around like an idiot not comprehending the charging man before you."
                            print "The man impales you through the chest and kicks you off his sword. He laughs"
                            print " like a drunken babboon, unable to believe to the idiot challenging him."
                            #health = health - 5
                            player.changeHealth(-5)

                    elif enemy_move > 2 and enemy_move < 6:
                        print "The dark figure holds his ground, continuing his large toothy grin."
                        print "You ",

                        counter_success = randint(0, 3)
                        if command == "Attack" or command == "attack" or command == "1":
                            if counter_success == 0:
                                print "see an opportunity to attack and lunge at him. He shreaks in laughter"
                                print "as he kicks you in the groin and cuts off one of your non-vital limbs."
                                #health = health - 2
                                player.changeHealth(-5)
                            else:
                                print "make a successful strike at his chest. 'FUUUUUUUUU' he shouts. Nice job!"
                                print "You actually did something well."
                                enemy_health = enemy_health - 1

                        elif command == "Block" or command == "block" or command == "2":
                            print "realize his plan and hold your ground. Realizing his counter has failed,"
                            print "the man kicks the ground in rage and raises his sword for the next round."
                            print "It's like you're psychic or something."

                        elif command == "Counter" or command == "counter" or command == "3":
                            print "grin like evily, waiting for him to strike. Unfortunately, you both have"
                            print "the same plan, so you both stand there grinning for the next couple of minutes."
                            print "Idiots."

                        else:
                            print "begin to do jumping jacks and sing a bunch of 80's punk at him."
                            print "Thinking you've figured out his plan, a look of fear runs through"
                            print "his face, as he believes he's come face to face with one of the"
                            print "legendary psychics. Boy did you luck out on that one."

                    else:
                        print "The dark figure raises his sword and takes a quick strike at you."
                        print "You ",
            
                        if command == "Attack" or command == "attack" or command == "1":
                            clash_success = randint(0, 1)

                            if clash_success == 0:
                                print "raise your lightsaber and do just the same. Your two weapons meet in fury,"
                                print "as you two stare deeply into each others' eyes, as you each attempt to"
                                print "overpower the other. Hot damn you guys look cool."
                            else:
                                print "You both awkwardly stick each other with the tips of your respective weapons."
                                print "You both grimace awkwardly like a couple having sex for the first time."
                                print "You guys are good at this."
                                #health = health - 1
                                player.changeHealth(-1)
                                enemy_health = enemy_health - 1

                        elif command == "Block" or command == "block" or command == "2":
                            block_success = randint(0, 1)
                            if block_success == 0:
                                print "hold your lightsaber firm against his attack. Nothing can get past your super"
                                print "cool defensive abilities apparently."
                            else:
                                print "you drop your sword as you try to block his weak swing. He chops off one"
                                print "of your ears and blops it into his mouth. He burps in happiness."
                                #health = health - 1
                                player.changeHealth(-1)

                        elif command == "Counter" or command == "counter" or command == "3":
                            counter_success = randint(0, 2)

                            if counter_success == 0:
                                print "stop his attack just in time by kicking him repeatedly in the nuts. Stunned by"
                                print "your defense, you stab him repeatedly in the chest. 'WOOOOOOOOOOOOOOK' the man"
                                print "cries out in pain, as you set yourself up for the next attack."
                                enemy_health = enemy_health - 2
                            else:
                                print "fail your dodge as he strikes off a large chunk of your hair. Oh no."
                                #health = health - 1
                                player.changeHealth(-1)

                        else:
                            print "gladly submit yourself to his attack, as he chops off both of your arms." 
                            print "He then kicks you to the ground and begins to fart nonstop directly into"
                            print "your nostrils. You are broken."
                            #health = health - 5
                            player.changHealth(-5)

                    print '\n'
                    
                    if player.getHealth() <= 0:
                        print "Any last bit of life leaves your body as you collapse to the ground."
                        print "The man laughs as he picks you up, and devours you in one bite."
                        print '\n'
                        return "death"

                    elif enemy_health <= 0:
                        print "The man falls to his knees with a defeated look on his face. 'WEEUUUWEEUUUWEEEUU'"
                        print "he cries out, as he disintegrates before your eyes. Jeez, you're kind of a jerk."
                        print '\n'
                        exit(-1)
            else:
                print "YOU IDIOT WHAT DO YOU THINK YOU'RE SUPPOSED TO DO IN THIS ROOM, HUH?!"
                print '\n'

