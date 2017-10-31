from sys import exit
from random import randint
from textwrap import dedent

class Scene():
    def enter(self):
        print("this scene is not yet configured")
        print("subclass it and implement enter()")

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map #Map(central_corridor)
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

            current_scene.enter()

class Death(Scene):
    quips = [
        "you died. you kinda suck at this.",
        "your mom would be proud...she she were smarter",
        "such a luster",
        "I have a small puppy that's better at this",
        "you're worse than your dad's jokes"
    ]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship
            and destroyed your entire crew. You are the last surviving
            member and you last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the birdge, and blow
            the ship up after getting into an escape pod.

            You're running down the central corridor the the Weapons
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            teeth, and evil clown costume flowing aroun dhis hate filled
            body. He's blocking the door to the Armory and about to pull a
            weapon to blast you.
            """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                    Quick on the draw you yank out your blaster and fire
                    it at the Gothon. His clown costume is flowing and moving around his body,
                    which throws off your aim. Your laser hits his costume but misses him
                    entirely. This completely ruins his brand new costume his mother bought him,
                    which makes him fly into an insane rage and blast you repeatedly in the face
                    until you are dead. Then he eats you.
                    """))
            return 'death'
        elif action == "dodge!":
            print(dedent("""
                like a world class boxer you dodge, weave, slip and
                slide right as the Gothon's blaster cranks a laser
                past your head. In the middle of you rartful dodge
                your foor slips and you bang your head on the metall wall
                and pass out. You wake up shortly after only to die as the Gothon
                stomps on your head and eats you.
                """))
            return 'death'
        elif action == "tell a joke":
            print(dedent("""
                lucky for you they made you learn gothon insults in the academy. you tell the
                one gothon joke you know: ddfsdsd sddfgsdgf gdfgdfg. The Gothon stops, tries
                not to laugh, then busts out laughing and can't move. While he's laughing you
                run up and shoot him square in the head putting him down. Off to the Weapon
                Armory door.
                """))
            return 'laser_weapon_armory'
        else:
            print("does not compute!")
            return 'central_corridor'




class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
            you do a dive roll into the armory, crouch and scan the room for more gothons that might be hiding.
            it's dead quite. you stand up and run to the far side of the room and find the neutron bomb
            in its container. There's a keypad lock on the box. If you get the code wron 10 times then the
            lock closes forever and you cant get the bomb. The code is 3 digits.
            """))

        code = f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}"
        guess = input("[keypad]>")
        guesses = 0

        while guess != code and guesses < 9:
            print("BZZZZZEDD!")
            guesses += 1
            guess = input("[keypad]> ")
        if guess == code:
            print(dedent("""
                the container clicks open and the seal breaks, letting
                gas out. you grab the neutron bomb and run as fast as
                you can to the bridge where you mist place it in the right spot.
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                the lock buzzes one last time and then you hear a slithering melting sound
                as the mechanism is fused together. you decide to sit there, and
                finally the Gothons blow up the ship from their ship and you die.
                """))
            return 'death'


class TheBridge(Scene):
    def enter(self):
        print(dedent("""
            you burst onto the bridge with the neutron destruct bomb under you rarm and suprise 5 Gothons
            who are trying to to take control of the ship. Each of them has an even uglier
            clown costume than the last. They haven't pulled their weapons out yet, as they see
            the active bomb under you rarm and don't want to set it out.
            """))
        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                in a panic you throw the bomb at the group of gothons and make a leap
                for the door. right as you drop it a gothon shoots you right in the back
                killing you. You die knowing the will probably die as well.
                """))
            return 'death'
        elif action == "slowly place the bomb":
            print(dedent("""
                time to get to the escape pod!!
                """))
            return 'escape_pod'
        else:
            print("does not compute")
            return "the_bridge"


class EscapePod(Scene):
    def enter(self):
        print(dedent("""
            5 pods which do you choose
            """))
        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                the pod implodes with you in it
                """))
            return 'death'
        else:
            print(dedent("""
                good choice - you made it out - smooth sailing
                """))
            return 'finished'

class Finished(Scene):
    def enter(self):
        print("you won! good job")
        return "finished"


class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


# create an instance of map -- pass central_corridor arg __ start_scene == central_corridor
#
a_map = Map('central_corridor')

# pass pass object with scene as arg to engine
a_game = Engine(a_map)

a_game.play()
# opening scene get scene name in dictionary - start scene
# get finished scene in dict
