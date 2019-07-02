from actors import Wizard, Creature, SmallAnimal, Dragon, Hero
import random
import time

def main():
    print_header()
    game_loop()

def print_header():
    print('--------------')
    print('WIZARD BATTLE')
    print('--------------')

def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, random.randint(10, 50), random.choice([True, False])),
        Wizard('Evil Wizard', 1000), 
    ]

    hero = Hero('Gary', 76)

    while True:

        active_creature = random.choice(creatures)
        if active_creature.name == "Dragon":
            print('It is a DRAGON!')
            if active_creature.breathes_fire == True:
                print('It\'s breathing fire, look out!')
        else:
            print('A {} of level {} has appeared from the darkness!'.format(active_creature.name, active_creature.level))
        print("Gary is level {}!".format(hero.level))

        cmd = input('Do you [a]ttack, [r]un away, or [l]ook around? ').lower()
        if cmd == 'a':
            if hero.attack(active_creature):
                hero.level = hero.level + 150
                creatures.remove(active_creature)
            else:
                print("The wizard runs away to recover his strength...")
                time.sleep(5)
                print("The wizard has recovered")

        elif cmd == 'r':
            print('THE WIZARD BOOKS IT')

        elif cmd == 'l':
            print('The wizard looks around and sees:')
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else: 
            print('Exiting game...')
            break

        if not creatures:
            print("You've defeated the creatures! YOU WIN BUD")
            break

        print()


if __name__ == '__main__':
    main()