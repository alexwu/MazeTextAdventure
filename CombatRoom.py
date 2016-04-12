from Scene import Scene
from Death import Death
from Player import Player
from sys import exit
from random import randint
import textwrap



class CombatRoom(Scene):

    def enter(self, player):

        player.setLoc("combat")
        player.writeSave()

        enemy_health = 5
        
        print textwrap.dedent("""\
            You enter a room a well lit room with nothing but a lone,
            dark figure standing at the center. The figure stands facing the
            opposing end of the room, wearing a grey hoodie and dark green
            basketball shorts. Currently, he does not appear to be dangerous.\n
            """)

        print textwrap.dedent("""\
            What would you like to do?
            \t1.) Approach man
            \t2.) Leave room
            """)

        while True:

            if player.getHealth() == 0:
                return "death"
            
            command = raw_input("> ")
            print

            if command == "jump":
                print textwrap.dedent("""\
                    You begin to squat very low, focusing all of your chi into
                    your lower body. You look up, thinking about all of the
                    mysteries above. You have to escape this place. 'Why me?',
                    you think to yourself. A tear begins to form in the corner of
                    your left eye, as you think of how long you have been trapped
                    in this god awful place. Suddenly, you hear a loud ripping sound
                    from beneath you! You realize your pants have ripped, leaving
                    you know protection from what lies ahead. Hopelessness grabs hold
                    of your heart as you die a slow and painful death.
                    """)
                print

                return "death"

            elif command == "1" or command == "approach figure" or command == "approach" or command == "go forward":
                print textwrap.dedent("""\
                    Hearing your footsteps, the dark figure slowly turns to face you.
                    As the figure's face comes into view, you realize the wide, deathly
                    grin on his face. With his eyes wide open, his pupils make contact
                    with yours, sending shivers down your spine. The man sticks his hand
                    down his pocket and slowly draws his weapon. Now holding a sword as
                    large as the man himself, the man began shreaking. 'I AM THE WARDEN
                    OF THIS DOMAIN. VACATE THIS SHELTER NOW.'
                    A green lightsaber materializes in your hands, as you stand waiting
                    to fight your foe.
                    """)

                while player.getHealth() > 0 and enemy_health > 0:
                    print "Health: ", player.getHealth()
                    print "Enemy Health: ", enemy_health
                    print textwrap.dedent("""\
                        Combat Options:
                        \t1.) Attack
                        \t2.) Block
                        \t3.) Counter\n
                        """)

                    enemy_move = randint(0, 9)
                    command = raw_input("What do you do? ")
                    print

                    if enemy_move < 3:
                        print textwrap.dedent("""\
                            The dark figure snarls as he raises his sword and charges
                            toward you like a bull. You"""),

                        if command == "Attack" or command == "attack" or command == "1":
                            print textwrap.dedent("""\
                                slash out at the figure as he comes into range, but you are unable
                                to stop the sheer power of his attack, as you are thrown against the
                                wall and feel your resolve weakening.
                                """)
                            player.changeHealth(-1)

                        elif command == "Block" or command == "block" or command == "2":
                            block_success = randint(0, 3)

                            if block_success == 0:
                                print textwrap.dedent("""\
                                    plant your feet, raise your self, and brace yourself for impact.
                                    The collision only moves you back a few inches, but the failed attack
                                    attempt has not done any real harm.
                                    """)
                            
                            else:
                                print textwrap.dedent("""\
                                    are knocked to the ground by his mighty attack. He spits on you
                                    and then proceeds to kick you in the nuts repeatedly for the
                                    next couple of minutes.
                                    """)
                                player.changeHealth(-2)

                        elif command == "Counter" or command == "counter" or command == "3":
                            counter_success = randint(0,2)

                            if counter_success == 0:
                                print textwrap.dedent("""\
                                    dodge just as he comes within range and stab him multiple times in the back.
                                    The man makes a petrifying sound no normal human can take. The snarl on his face
                                    intensifies, clearly in pain.
                                    """)
                                enemy_health = enemy_health - 2
                            else:
                                print textwrap.dedent("""\
                                    mistime your dodge as he stabs you in the stomach and burps nonstop
                                    into your eyes. You scream in pain as your eyes feel as if they're
                                    starting to melt. Jesus man, that kind of sucks.
                                    """)
                                player.changeHealth(-3)

                        else:
                            print textwrap.dedent("""\
                                stand around like an idiot not comprehending the charging man before you.
                                The man impales you through the chest and kicks you off his sword. He laughs
                                like a drunken babboon, unable to believe to the idiot challenging him.
                                """)
                            player.changeHealth(-5)

                    elif enemy_move > 2 and enemy_move < 6:
                        print "The dark figure holds his ground, continuing his large toothy grin."
                        print "You ",

                        counter_success = randint(0, 3)
                        if command == "Attack" or command == "attack" or command == "1":
                            if counter_success == 0:
                                print textwrap.dedent("""\
                                    see an opportunity to attack and lunge at him. He shreaks in laughter
                                    as he kicks you in the groin and cuts off one of your non-vital limbs.
                                    """)
                                player.changeHealth(-5)
                            else:
                                print textwrap.dedent("""\
                                    make a successful strike at his chest. 'FUUUUUUUUU' he shouts. Nice job!
                                    You actually did something well.
                                    """)
                                enemy_health = enemy_health - 1

                        elif command == "Block" or command == "block" or command == "2":
                            print textwrap.dedent("""\
                                realize his plan and hold your ground. Realizing his counter has failed,
                                the man kicks the ground in rage and raises his sword for the next round.
                                It's like you're psychic or something.
                                """)

                        elif command == "Counter" or command == "counter" or command == "3":
                            print textwrap.dedent("""\
                                grin like evily, waiting for him to strike. Unfortunately, you both have
                                the same plan, so you both stand there grinning for the next couple of minutes.
                                Idiots.
                                """)

                        else:
                            print textwrap.dedent("""\
                                begin to do jumping jacks and sing a bunch of 80's punk at him.
                                Thinking you've figured out his plan, a look of fear runs through
                                his face, as he believes he's come face to face with one of the
                                legendary psychics. Boy did you luck out on that one.
                                """)

                    else:
                        print "The dark figure raises his sword and takes a quick strike at you."
                        print "You ",
            
                        if command == "Attack" or command == "attack" or command == "1":
                            clash_success = randint(0, 1)

                            if clash_success == 0:
                                print textwrap.dedent("""\
                                    raise your lightsaber and do just the same. Your two weapons meet in fury,
                                    as you two stare deeply into each others' eyes, as you each attempt to
                                    overpower the other. Hot damn you guys look cool.
                                    """)
                            else:
                                print textwrap.dedent("""\
                                    both awkwardly stick each other with the tips of your respective weapons.
                                    You both grimace awkwardly like a couple on a first date.
                                    You guys are good at this.
                                    """)
                                player.changeHealth(-1)
                                enemy_health = enemy_health - 1

                        elif command == "Block" or command == "block" or command == "2":
                            block_success = randint(0, 1)
                            if block_success == 0:
                                print textwrap.dedent("""\
                                    hold your lightsaber firm against his attack. Nothing can get past your super
                                    cool defensive abilities apparently.
                                    """)
                            else:
                                print textwrap.dedent("""\
                                    you drop your sword as you try to block his weak swing. He chops off one
                                    of your ears and blops it into his mouth. He burps in happiness.
                                    """)
                                player.changeHealth(-1)

                        elif command == "Counter" or command == "counter" or command == "3":
                            counter_success = randint(0, 2)

                            if counter_success == 0:
                                print textwrap.dedent("""\
                                    stop his attack just in time by kicking him repeatedly in the nuts. Stunned by
                                    your defense, you stab him repeatedly in the chest. 'WOOOOOOOOOOOOOOK' the man
                                    cries out in pain, as you set yourself up for the next attack.
                                    """)
                                enemy_health = enemy_health - 2
                            else:
                                print "fail your dodge as he strikes off a large chunk of your hair. Oh no."
                                player.changeHealth(-1)

                        else:
                            print textwrap.dedent("""\
                                gladly submit yourself to his attack, as he chops off both of your arms.
                                He then kicks you to the ground and begins to fart nonstop directly into
                                your nostrils. You are broken.
                                """)
                            player.changeHealth(-5)

                    print
                    
                    if player.getHealth() <= 0:
                        print textwrap.dedent("""\
                            Any last bit of life leaves your body as you collapse to the ground.
                            The man laughs as he picks you up, and devours you in one bite.
                            """)
                        print 
                        return "death"

                    elif enemy_health <= 0:
                        print textwrap.dedent("""\
                            The man falls to his knees with a defeated look on his face. 'WEEUUUWEEUUUWEEEUU'
                            he cries out, as he disintegrates before your eyes. Jeez, you're kind of a jerk.
                            """)
                        print
                        player.changeState(1, True)
                        exit(-1)

            elif command == "2" or command.lower() == "leave":
               return "hallway"

            else:
                print "YOU IDIOT WHAT DO YOU THINK YOU'RE SUPPOSED TO DO IN THIS ROOM, HUH?!"
                print

