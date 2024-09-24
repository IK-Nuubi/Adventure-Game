import time
import random


def print_pause(narration):
    print(narration)
    time.sleep(2)


def player_choice(question, options):
    while True:
        decision = input(question).lower()
        for option in options:
            if decision in option:
                return decision


def intro(monster):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumour has it that a {monster} is somewhere "
                "around and terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand is your "
                "trusty (but not very efficient) dagger.\n")


def scary_house(game_stash, monster):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the "
                f"door opens and out steps a {monster}.")
    print_pause(f"Eep! this is the {monster}'s house!")
    print_pause(f"The {monster} attacks you!")
    if "sword" not in game_stash:
        print_pause("You feel a bit under prepared for "
                    "this with only your tiny dagger in hand.\n")
    else:
        print_pause("But with your magical sword of Ikenga "
                    "in hand, you feel prepared.\n")
    fight_or_not = input("would you like to (1) fight or (2) Run away?\n")
    if fight_or_not == "1":
        if "sword" in game_stash:
            print_pause(f"As the {monster} moves to attack, "
                        "you unsheath your new sword.")
            print_pause("The sword of Ikenga shines brightly in your hand "
                        "as you brace yourself for the attack.")
            print_pause(f"But the {monster} takes one look "
                        "at your shiny sword and runs away!.")
            print_pause(f"You have rid the town of the {monster}. "
                        "You are Victorious!!!\n")
            play_again(game_stash, monster)
        else:
            print_pause("You do your best...")
            print_pause(f"But your dagger is no match for the {monster}.")
            print_pause("You have been defeated!\n")
            play_again(game_stash, monster)
    elif fight_or_not == "2":
        print_pause("You run back into the field, luckily you "
                    "don't seem to have been followed\n")
        player_decision(game_stash, monster)
    else:
        return fight_or_not


def magic_cave(game_stash, monster):
    print_pause("You peer cautiously into the cave.")
    if "sword" in game_stash:
        print_pause("You have been here before and gotten all the good stuff.")
        print_pause("It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")
        player_decision(game_stash, monster)
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ikenga!")
        game_stash.append("sword")
        print_pause("You discard your old dagger and take the sword with you.")
        print_pause("You walk back out to the field.\n")
        player_decision(game_stash, monster)


def player_decision(game_stash, monster):
    print_pause("enter 1 to knock on the door of the house.")
    print_pause("enter 2 to peer into the cave.")
    print_pause("what would you like to do?")
    choice = player_choice("Please enter 1 or 2:\n", ["1", "2"])
    if choice == "1":
        scary_house(game_stash, monster)
    elif choice == "2":
        magic_cave(game_stash, monster)
    else:
        return choice


def play_again(game_stash, monster):
    another_round = player_choice("Would you love to play "
                                  "again? (y/n)", ["y", "n"])
    if "y" in another_round:
        print_pause("Excellent! Restarting the game")
        intro(monster)
        player_decision(game_stash, monster)
    elif "n" in another_round:
        print_pause("Thanks for playing! See you next time.")


def adventure_game():
    enemies = ("gorgon", "wicked fairy", "pirate", "troll",
               "dragon", "beast", "vampire")
    game_stash = []
    monster = random.choice(enemies)
    intro(monster)
    player_decision(game_stash, monster)


adventure_game()
