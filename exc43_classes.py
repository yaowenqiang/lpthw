from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print('This scene is not yet configured.')
        print('Subclass it and implement enter()')
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
    
        current_scene.enter()

class Death(Scene):

    quips  = [
        "You dead, You kinda  suck at this.",
        "Your moom would be proud ... if she were smatter.",
        "Such a loser",
        "I have a small puppy that's better at this.",
        "You're worse than you Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(0)


class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
            The Gothons of Planet #25 have invaded your ship and 
            Destroyed your entire crew.You are the last surviving
            member and your last mission is to get the neutron destruct
            bluw the ship up after getting into an escape pod.

            You're running down the central corridor to the Weapons Armory 
            when a Gothon jumps out. red scaly skin,dark grimy teeth,
            and evil clown custom flowing around his hate 
            filled body.He's blocking the door to the Armory and 
            about to pull a weapon to blast you
        """))

        action = input('> ')
        if action == 'shoot!':
            print(dedent("""
                Quick on the draw you yank out your blaster and fire 
                it at the Gothon.His clown costume is flowing and 
                moving around his body. which thrown off your aim.
                Your laser hits his costume but missses him entirely.
                This completely ruins his brand new costume his mother
                thought him,which makes him fly into an insane rage
                and blast you repeatedly in the face until you are 
                dead.Then he eats you.
            """))
            return "death"
        elif action == 'dodge!': # 闪躲
            print(dedent("""
                Like a world class boxer you dodge.weave,
                slip and slide right as the Gothon's blaster cranks a 
                laser past your head.In the middle of your artful dodge 
                your foot slips and you bang your head onthe metal wall
                and pass out.Your wake up shortly after only to die as 
                the Gothon stomps on your head and eats you
            """))
            return "death"
        elif aciton == "tell a joke":
            print(dedent("""
                Lucky for you they made you learn Gothon insults in the
                academy.You tell the one Gothon joke you know for 
                fvgf mebhaq gur ubhfr.The Gothon stops.tries not to 
                laugh.then busts out laughing and can't move.
                While he's laughing you run up and shoot him square in
                the head putting him down.then jump through the Weapon 
                Armory door.
            """))     
            return "laser_weapon_armory"
        else:
            print("DOES NOT COMPUTE!")
            return "central_corridor"
            
class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            You do a dive roll into the Weaon Armory.crouch and scan
            the room for more Gothons that might be hiding.It's dead
            quiet,too quiet.You stand up and run to the far side of
            the room and find the neutron bomb in the container.
            There's a keypad lock on the box and you need the code to 
            get the bomb out.If you get the code wrong 10 times then 
            the lock closes forever and you can't get the bomb.The 
            code is 3 digits.
            """))     
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        
        if guess == code:
            print(dedent("""
                The container clicks open and the seal breaks.letting
                gus out. You grab the neatron  bomb and run as fast as 
                you can to the bridge where you must place it in 
                the right spot.
            """))
            return "the_bridge"
        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a 
                sickening melting sound as the mechanism is fuses 
                togher .YOU decide to sit there. and finally the 
                gothons blow up the ship from their ship and you die.
            """))
            return "death"

class EscapePod(Scene):
    def enter(self):
        pass


class Map(object):
    def __init__(self,start_scene):
        pass

    def next_scene(self,scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()


