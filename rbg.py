import time, sys


class Hero:
    def __init__(self, energy, attack, gold, weapon):
        """ Create a new point at the given coordinates. """
        self.energy = energy
        self.attack = attack
        self.gold = gold
        self.weapon = weapon
        self.weapon_array = ["bare fists", "bow", "dagger", "sword", "longsword"]
        self.weapon_damage = [1, 2, 3, 4, 5]

    def update_energy(self, e_diff):
        self.energy += e_diff

    def equip_weapon(self, weapon_num):
        self.weapon = weapon_num



def check_input(range):
    while True:
        response = raw_input().lower()

        try:
            response = int(response)

            if 0 > response or response > range:
                print_delay("You must choose between 1 and", range, "!")
            else:
                return response

        except ValueError:
            print_delay("You have to enter a number!")


def print_delay(sen):
    for letter in sen:
        time.sleep(0)
        sys.stdout.write(letter)

    print "\n"


def loot_escape():
    global heroGold, heroEnergy

    heroGold += 150

    print_delay("Hero has looted his parents gil.")
    print_delay("Gil increased to " + str(heroGold) + "!")
    print_delay("As hero runs towards the secret cave at the bottom of the dried up well.")
    print_delay("As Hero turns a corner, he is met by three townsmen running towards the gate.")
    print_delay("'All those not for us are against us!', yell the men.")
    print_delay("The lead man barrel rolls unexpectantly 3 meters before Hero.")
    print_delay("Hero perceives a movement too quick to see anything but a flash the color of worn tunic.")
    print_delay("Hero sees all blue and realizes he is on his back looking at the sky.")
    heroEnergy -= 100
    print_delay("Hero's energy has decreased to " + str(heroEnergy) + " hp.")
    check_death()


def defend_gate(h):
    h.equip_weapon(2)
    print_delay("Hero has equipped his " + str(h.weapon_array[h.weapon]) + ".")
    print_delay("Attack with all your might men! Your women and children are at stake!")
    print_delay("An ogre approaches...")
    print_delay("What would you like to do?")
    print_delay("1. Barrel roll and thrust your Dagger into his liver.")
    print_delay("2. Dodge to the left and slice the Ogre's abdomen.")
    print_delay("3. Push the fellow townsman on your left into the path of the oncoming Ogre.\n")


def run(h):

    print_delay("Forgetting to put on his tunic, Hero runs for the hills towards the east side of town.")
    print_delay("Hero makes it over the village wall.")
    print_delay("Hero runs up a stream to in an effort hide his scent from the marauding Ogres.")
    print_delay("Hero takes a breather by a blueberry bush upstream.")
    print_delay("Hero drinks some water.")
    h.update_energy(100)
    print_delay("Hero's energy goes up to " + str(h.energy) + ".")
    print_delay("Hero eats a handful of blueberries.")
    print_delay("They have a bitter aftertaste! Poisonous hollyberries!")
    h.update_energy(-25)
    print_delay("Hero's energy goes down to " + str(h.energy) + ".")
    check_death(h)
    print_delay("Hero is forced to lay down and take a nap.")


def check_death(h):
    # Check if able to continue
    if h.energy <= 0:
        print_delay("Hero can no longer continue.")
        sys.exit()


def main():
    hero = Hero(100, 50, 20, 0)
    print_delay("Hero wakes up on a sunny day in his bedroom.")
    print_delay("Daniel! Daniel! Wake up! Monsters are attacking the village!")
    print_delay("What would you like to do?")
    print_delay("1. Run for the hills.")
    print_delay("2. Grab your dagger and help the men at the gate.")
    print_delay("3. Grab your parents sack of gold and escape down the well.\n")

    choice = check_input(3)

    if choice == 1:
        run(hero)
    elif choice == 2:
        defend_gate(hero)
    else:
        loot_escape()


if __name__ == "__main__":
    main()
