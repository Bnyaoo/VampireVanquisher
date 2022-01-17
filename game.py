"""
Your name: Benny Chao
Your student number: A01270575

All of your code must go in this file.
"""
from termcolor import colored
import random
import time
import math


def game():
    """
    Controls the game flow.

    """
    rows = 26
    columns = 26
    board = make_board(rows, columns)
    character = make_character()
    user_name(character)
    character_class(character)
    achieved_goal = False
    while not achieved_goal:
        level_up_1(character)
        level_up_2(character)
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(character, direction)
        while character['X-coordinate'] == 25 and character['Y-coordinate'] == 24 \
                or character['Y-coordinate'] == 25 and character['X-coordinate'] == 24:
            print(colored(f'\nThe final boss is nearby, do you wish to proceed? '
                          f'(Boss has 200 HP and 22 Power stat)', 'red'))
            final_boss_choice = input(f'Yes {"y"} or No {"n"}')
            if final_boss_choice == "y":
                if valid_move is True:
                    if valid_move:
                        break
            if final_boss_choice == "n":
                if valid_move is True:
                    move_character_backwards(character, direction)
        if valid_move:
            random_elixir_potion(character)
            class_board_interaction(board, character)
            move_character(character, direction)
            game_map(direction)
            describe_current_location(board, character)
            there_is_a_challenger = check_for_foes()
            if there_is_a_challenger:
                foe = make_mob(character)
                fight_foe = flee(foe)
                if fight_foe is True:
                    is_alive(character)
                    combat(character, foe)
                else:
                    flee_penalty(character, foe)
                    is_alive(character)
            achieved_goal = check_if_goal_attained(character)
        else:
            if valid_move is False:
                print(colored(f"\n            !!! You can't go that way !!!", 'red'))
                continue
        while is_alive(character) and not achieved_goal:
            break
        if is_alive(character) is False:
            print('\nThe', (foe.get('Name')), random_death())
            print(colored(f"\n...YOU'RE DEAD...", 'red'))
            break
        else:
            continue
    if is_alive(character) and achieved_goal:
        final_boss()
        print(colored("You swing the doors open to Alukah's chamber... ", 'red'))
        time.sleep(2)
        print(colored("\nhe slowly emerges from his casket...", 'red'))
        time.sleep(2)
        print(colored("\nwith your weapon in hand, you prepare yourself for battle", 'red'))
        time.sleep(2)
        combat(character, final_boss())
        if is_alive(character) is False:
            print(colored(f"So close... but this is where your journey ends...\n You have been SLAIN", 'red'))
        else:
            print(colored(f'\n                 --------------------------------------'
                          f'\n                 | ~~WINNER WINNER, CHICKEN DINNER!~~ |'
                          f'\n                 --------------------------------------', 'yellow'))


def game_map(direction):
    """

    :param direction: user input that corresponds to one of four directions (string)
    :precondition: the plauer must provide a valid input
    :postcondition: prints a map with direction of character
    :return: board a dictionary containing x and y coordinates along with room descriptions

    >>> game_map(direction="NORTH")
    ---- ---- ----
    |  | |🧑| |  |
    ---- ---- ----
    ---- ---- ----
    |  | |  | |  |
    ---- ---- ----
    ---- ---- ----
    |  | |  | |  |
    ---- ---- ----
    [['|  |', '|🧑|', '|  |'], ['|  |', '|  |', '|  |'], ['|  |', '|  |', '|  |']]
    >>> game_map(direction="EAST")
    ---- ---- ----
    |  | |  | |  |
    ---- ---- ----
    ---- ---- ----
    |  | |  | |🧑|
    ---- ---- ----
    ---- ---- ----
    |  | |  | |  |
    ---- ---- ----
    [['|  |', '|  |', '|  |'], ['|  |', '|  |', '|🧑|'], ['|  |', '|  |', '|  |']]
    """
    character_x = 1
    character_y = 1

    character_position = "|🧑|"

    board = [["|  |" for _ in range(3)] for _ in range(3)]

    board[character_x][character_y] = character_position

    while True:

        if direction == "NORTH":
            board[character_x][character_y] = "|  |"
            character_x -= 1
            board[character_x][character_y] = "|🧑|"
            for i in board:
                print("---- ---- ----")
                print(" ".join(i))
                print("---- ---- ----")
        elif direction == "SOUTH":
            board[character_x][character_y] = "|  |"
            character_x += 1
            board[character_x][character_y] = "|🧑|"
            for i in board:
                print("---- ---- ----")
                print(" ".join(i))
                print("---- ---- ----")
        elif direction == "WEST":
            board[character_x][character_y] = "|  |"
            character_y -= 1
            board[character_x][character_y] = "|🧑|"
            for i in board:
                print("---- ---- ----")
                print(" ".join(i))
                print("---- ---- ----")
        elif direction == "EAST":
            board[character_x][character_y] = "|  |"
            character_y += 1
            board[character_x][character_y] = "|🧑|"
            for i in board:
                print("---- ---- ----")
                print(" ".join(i))
                print("---- ---- ----")

        return board


def level_up_1(character):
    """
    First character class advancement.

    :param character: a dictionary containing character data
    :precondition: a valid dictionary is received containing, 'EXP', 'Current HP', 'Power', and 'Class'
    :postcondition: checks if 'EXP' requirement is met then updates character dictionary with added stats
    :return: character dictionary containing updated 'Current HP', 'Power, and 'EXP'

    """
    if character['EXP'] == 10:
        if character['Class'] == "1":
            print(colored(f'Your bloodlust drives you mad...\nYou have been promoted from '
                          'MARAUDER to BERSERKER', 'magenta'))
            character['Current HP'] += 10
            character['Power'] += 5
            character['EXP'] += 1
        elif character['Class'] == "2":
            print(colored(f'You have been corrupted by knowledge...\nYou have been promoted from '
                          'ALCHEMIST to DARK MAGE', 'magenta'))
            character['Current HP'] += 5
            character['Power'] += 10
            character['EXP'] += 1
        elif character['Class'] == "3":
            print(colored(f"You analyze and start to understand how these monsters behave..."
                          f"\nYou have been promoted from "'HUNTER to VANQUISHER', 'magenta'))
            character['Current HP'] += 7
            character['Power'] += 7
            character['EXP'] += 1
        elif character['Class'] == "4":
            print(colored(f'All this killing makes you ecstatic...\nYou have been promoted from '
                          'TORMENTOR to EXECUTIONER', 'magenta'))
            character['Current HP'] += random.choice(range(1, 11))
            character['Power'] += random.choice(range(1, 11))
            character['EXP'] += 1
    return character


def level_up_2(character):
    """
    Second character class advancement.

    :param character: a dictionary containing character data
    :precondition: a valid dictionary is received containing, 'EXP', 'Current HP', 'Power', and 'Class'
    :postcondition: checks if 'EXP' requirement is met then updates character dictionary with added stats
    :return: character dictionary containing updated 'Current HP', 'Power, and 'EXP'

    """
    if character['EXP'] == 21:
        if character['Class'] == "1":
            print(colored(f'You stand over the corpses of your enemies...\nYou have been promoted from '
                          'BERSERKER to WARLORD', 'magenta'))
            character['Current HP'] += 15
            character['Power'] += 10
            character['EXP'] = 22
        elif character['Class'] == "2":
            print(colored(f'You have fully mastered the dark arts...\nYou have been promoted from '
                          'DARK MAGE to MIND SCULPTOR', 'magenta'))
            character['Current HP'] += 10
            character['Power'] += 15
            character['EXP'] = 22
        elif character['Class'] == "3":
            print(colored(f"You have all the knowledge you need to combat monsters now..."
                          f"\nYou have been promoted from "'VANQUISHER to BANE OF MONSTERS', 'magenta'))
            character['Current HP'] += 12
            character['Power'] += 12
            character['EXP'] = 22
        elif character['Class'] == "4":
            print(colored(f'You have shed all sense humanity...\nYou have been promoted from '
                          'EXECUTIONER to THE DAMNED', 'magenta'))
            character['Current HP'] += random.choice(range(5, 30))
            character['Power'] += random.choice(range(5, 30))
            character['EXP'] = 22
    return character


def random_death():
    """
    List of random death scenarios.

    :precondition: death_list only contains strings
    :postcondition: random.choice() selects a string from death_list and stores it in variable, death_text
    :return: a string variable named death_text
    """
    death_list = ['tore your throat out', 'shivved you in the kidney', 'cut you in two', 'set you ablaze',
                  'gauged your eyes out']
    death_text = random.choice(death_list)
    return death_text


def random_elixir_potion(character):
    """
    Random chance for player to gain more HP and Power.

    :param character: a dictionary containing character data
    :precondition: receives a valid character dictionary containing 'Name', 'Current HP', and 'Power'
    :postcondition: if random is less than percentage_chance, character gains HP in a range of 1 to 5
    :postcondition: if random is less than percentage_chance, character gains Power in a range of 1 to 3
    :postcondition: print statement informs the player of updated stats
    :return: character dictionary containing updated 'Current HP' and 'Power'
    """
    percentage_chance = 0.25
    if random.random() < percentage_chance:
        health_gained = 5
        power_gained = 5
        character['Current HP'] += health_gained
        character['Power'] += power_gained
        print('\nYou stumble upon an elixir and consume it...', colored('HP +', 'magenta'),
              colored(health_gained, 'magenta'), colored('Power +', 'magenta'),
              colored(power_gained, 'magenta'), '\n')
    return character


def flee_penalty(character, foe):
    """
    Chance to take damage when fleeing from a foe.

    :param foe: a dictionary containing foe data
    :param character: a dictionary containing character data
    :param: a dictionary containing all foe stats
    :precondition: receives two valid dictionaries with 'Name', 'Current HP', and 'Power'
    :postcondition: if random is less than percentage_chance, character loses HP equal to foe 'Power'
    :postcondition: character 'Current HP' remains the same and a state is printed to update the player
    :return: character dictionary containing updated 'Current HP'

    """
    percentage_chance = 0.20
    if random.random() < percentage_chance:
        print('The', (foe.get('Name')), 'lands a blow while you attempt to flee')
        character['Current HP'] -= foe['Power']
    else:
        print('Escaped the conflict unscathed')

    return character


def flee(foe):
    """
    Prompts player to either engage in combat or flee from foe.

    :param: a dictionary containing all foe stats
    :precondition: player inputs a value of either '1' or '2'
    :postcondition: player either enters a battle stage in game loop or breaks away and is prompted to continue moving
    :return: Boolean (True or False)

    """
    while True:
        print('\n', foe)
        choice = input('\nPrepare yourself for battle...\nWould you like to Fight [1] or Flee [2]: ')
        if choice == '1':
            return True
        elif choice == '2':
            return False
        else:
            print("\nInvalid input, try again.\n")
            continue


def combat(character, foe):
    """
    Combat function for the game.

    :param character: a dictionary containing character data
    :param foe: a dictionary containing foe data
    :precondition: receives two valid dictionaries with 'Name', 'Current HP', and 'Power'
    :precondition: user input must be 1, 2, or 3
    :postcondition: continues looping through until character or foe 'Current HP' == 0 or character flees from combat
    :return: character dictionary containing updated value for 'Current HP'

    """
    character_power = (character.get('Power'))
    character_health = (character.get('Current HP'))
    foe_power = (foe.get('Power'))
    foe_health = (foe.get('Current HP'))
    print('\nYou encounter a', (foe.get('Name')), '...')
    while character_health > 0:
        print(colored('\n------------------------------------Current Stats---------------------------------', 'yellow'))
        print(colored(character, 'yellow'))
        print(colored('\n----------------------------------Foe Current Stats-------------------------------', 'red'))
        print(colored(foe, 'red'))
        user_decision = input(f"\n--Attack [{1}]-----Flee [{2}]-----Special Attack [{3}]--: ")
        if user_decision == '1':
            print('\nYou attack the,', (foe.get('Name')))
            foe_health -= character_power
            time.sleep(1)
            if foe['Name'] == 'Wraith':
                guessing_game(character)
                break
            if foe_health > 0:
                print((foe.get('Name')), 'attacks you')
                character_health -= foe_power
                time.sleep(1)
                character['Current HP'] = character_health
                foe['Current HP'] = foe_health
            if foe_health <= 0:
                if foe['Name'] == 'Vampire':
                    character['Power'] += 2
                    character['Current HP'] += 10
                    character['EXP'] += 2
                    print('You have', colored('SLAIN', 'red'), 'the', (foe.get('Name')))
                    break
                else:
                    character['Power'] += 1
                    character['Current HP'] += 1
                    character['EXP'] += 2
                    print('You have', colored('SLAIN', 'red'), 'the', (foe.get('Name')))
                    break
        elif user_decision == '3':
            print('\nYou unleash your special attack!')
            if character['Class'] == "1":
                percentage_chance = 0.80
                if random.random() < percentage_chance:
                    print(colored('You cleave your foe in two... absorbing some HP in the process', 'green'))
                    character_health += random.choice(range(0, character_power))
                    foe_health -= math.ceil(character_power / 2)
                else:
                    print('Your special attack missed...')
            elif character['Class'] == "2":
                percentage_chance = 0.75
                if random.random() < percentage_chance:
                    print(colored('You successfully cast your most powerful spell', 'green'))
                    foe_health -= character_power * 2
                    time.sleep(1)
                else:
                    print('Your special attack missed...')
            elif character['Class'] == "3":
                user_input = input(f"\n----Tame [{1}]--------Unleash tamed foe [{2}]---: \n")
                if user_input == '1':
                    if foe['Name'] == 'Alukah, the first vampire':
                        print(colored('Alukah can not be persuaded'))
                        time.sleep(0.5)
                        continue
                    percentage_chance = 0.65
                    if random.random() < percentage_chance:
                        print(colored('You have tamed your foe', 'green'))
                        character['Tamed Foe'] = foe_power + character_power
                        time.sleep(1)
                        break
                    else:
                        print('Your special attack missed...')
                elif user_input == '2':
                    print(colored('You coordinate a combination attack with your tamed foe...', 'green'))
                    time.sleep(1)
                    tamed_power = character['Tamed Foe']
                    foe_health -= tamed_power + character_power
                    foe['Current HP'] = foe_health
                else:
                    print("Invalid input, try again.")
                    continue
            elif character['Class'] == "4":
                percentage_chance = 0.75
                if random.random() < percentage_chance:
                    print(colored('You take your foe by surprise and land two consecutive blows', 'green'))
                    foe_health -= character_power
                    time.sleep(0.5)
                    foe_health -= character_power
                    time.sleep(1)
                else:
                    print('Your special attack missed...')
            if foe['Name'] == 'Wraith':
                guessing_game(character)
                break
            if foe_health > 0:
                print((foe.get('Name')), 'attacks you')
                character_health -= foe_power
                time.sleep(1)
                character['Current HP'] = character_health
                foe['Current HP'] = foe_health
            if foe_health <= 0:
                if foe['Name'] == 'Vampire':
                    character['Power'] += 2
                    character['Current HP'] += 10
                    character['EXP'] += 2
                    print('You have', colored('SLAIN', 'red'), 'the', (foe.get('Name')))
                    break
                else:
                    character['Power'] += 1
                    character['Current HP'] += 1
                    character['EXP'] += 2
                    print('You have', colored('SLAIN', 'red'), 'the', (foe.get('Name')))
                    break
        elif user_decision == '2':
            if foe == final_boss():
                print(colored('\nYou cannot escape...'))
                continue
            else:
                flee_penalty(character, foe)
                break
        else:
            print('Invalid input, try again')
            continue
    return character['Current HP']


def user_name(character):
    """
    Asks for player to input a name for character.

    :param character: a dictionary containing character data
    :precondition: receives character dictionary and user input
    :postcondition: converts user input to a string and appends 'Name' key and value to character dictionary
    :return: updated character dictionary with a key ('Name') and its value (character_name)

    """
    print(f'------------------------------------------------')
    character_name = input('Enter your name: ')
    character['Name'] = character_name

    return character


def make_mob(character):
    """
    Randomly generates a mob with 'Power' and 'Current HP' relative to player 'Power' and 'Current HP'.

    :param character: a a dictionary containing character data
    :precondition: receives a character dictionary containing 'Current HP' and 'Power'
    :postcondition: creates a foe dictionary with 'Current HP' and 'Power' belonging to a range of 1 to var upper_bound
    :return: a foe dictionary containing 'Name', 'Current HP' and 'Power'
    """
    upper_bound = character['Power'] * 2
    max_power = round(character['Current HP'] / 2)
    if max_power < 2:
        max_power = 2
    foe = {'Name': '', 'Power': 0, 'Current HP': 0}
    foe_names = ['Reanimated Corpse', 'Bandit', 'Giant Toad', 'Serpent', 'Occultist', 'Witch', 'Ghoul',
                 'Vampire', 'Wraith', 'Knight']
    for _ in foe:
        foe['Power'] = random.choice(range(1, max_power))
        foe['Name'] = random.choice(foe_names)
        foe['Current HP'] = random.choice(range(1, upper_bound))
    if foe['Name'] == 'Vampire':
        foe['Power'] = 10
        foe['Current HP'] = 20
    elif foe['Name'] == 'Wraith':
        foe['Power'] = 5
        foe['Current HP'] = 999
        foe['Guessing Game'] = "Answer correctly and gain tremendous power and vitality"
    print(colored(f'\nSomething approaches...', 'red'))
    return foe


def final_boss():
    """
    Final boss data stored in a dictionary.

    :preconditon: 'Name', 'Current HP, and 'Power' must be in boss dictionary
    :postcondition: 'Name', 'Current HP, and 'Power' are stored in boss dictionary
    :return: dictionary containing final boss data

    >>> final_boss()
    {'Name': 'Alukah, the first vampire', 'Current HP': 200, 'Power': 22}
    """
    boss = {'Name': 'Alukah, the first vampire', 'Current HP': 200, 'Power': 22}
    return boss


def class_board_interaction(board, character):
    """
    Player receives power-up on board grid depending on class.

    :param: board: a dictionary containing coordinate data and list of room names
    :param: character: a a dictionary containing character data
    :precondition: player class and current grid coordinate is valid
    :postcondition: adds 1 to existing 'Power' value in character dictionary and prints a statement with updated stats
    :return: updated character dictionary
    """
    x = (character.get('X-coordinate'))
    y = (character.get('Y-coordinate'))
    current_coordinate = (x, y)
    for _ in character:
        if character['Class'] and board:
            if character['Class'] == "1" and board[current_coordinate] == colored('Ballroom', 'white'):
                character['Power'] += 1
                print(f'\nYou encounter an armory...', colored('Power +1', 'magenta'), '\n')
                return character
            elif character['Class'] == "2" and board[current_coordinate] == colored('Library', 'white'):
                character['Power'] += 1
                print(f'\nYou chance upon some flasks filled with chemicals...', colored('Power +1', 'magenta'), '\n')
                return character
            elif character['Class'] == "3" and board[current_coordinate] == colored('Spiraling staircase', 'white'):
                character['Power'] += 1
                print(f'\nYou create arrows from some wood you randomly encountered...',
                      colored('Power +1', 'magenta'), '\n')
                return character
            elif character['Class'] == "4" and board[current_coordinate] == colored('Flaying room', 'white'):
                character['Power'] += 1
                print(f'\nYou dip your dagger in poisonous sludge...', colored('Power +1', 'magenta'), '\n')
                return character
    print(colored('☠️----------------------------------------------------Your Stats---------------------'
                  '------------------------------  ☠️', 'yellow'))
    print(colored(character, 'yellow'))
    print('Current Location: ', describe_current_location(board, character), x, y)
    return character


def character_class(character):
    """
    Gets user input to select 1 of 4 classes.

    :param character: a dictionary containing character data
    :precondition: player provides an input between "1" to "4" inclusive
    :postcondition: updates character dictionary values and prints chosen class name
    :return: updated character dictionary

    """
    class_options = {"1": "MARAUDER", "2": "ALCHEMIST", "3": "HUNTER", "4": "TORMENTOR"}
    while True:
        user_input = input(f"------------------ Select a Class -----------------"
                           "\nMARAUDER: [1], ALCHEMIST: [2], HUNTER: [3], TORMENTOR: [4]: ")
        if user_input not in class_options:
            print("Invalid input, try again.")
            continue
        character['Class'] = user_input
        for _ in character:
            if character['Class'] == "1":
                character['Current HP'] += 15
                break
            elif character['Class'] == "2":
                character['Power'] += 14
                character['Current HP'] -= 5
                break
            elif character['Class'] == "3":
                character['Power'] += 4
                character['Current HP'] += 5
                character['Tamed Foe'] = 0
                break
            elif character['Class'] == "4":
                character['Power'] += random.choice(range(1, 24))
                character['Current HP'] += random.choice(range(-10, 1))
                break
        for k, v in class_options.items():
            if k == user_input:
                name = v
                print(colored(f"-------------------------------", 'grey', 'on_red'))
                print(colored("You have chosen...             ", 'grey', 'on_red'))
                print(colored(name, 'red'))
                print(colored("-------------------------------", 'grey', 'on_red'))
        return character


def is_alive(character):
    """
    Determines whether or not the character is alive.

    :param: a dictionary containing character data
    :precondition: parameter must be a dictionary containing 'Current HP'
    :postcondition: value of 'Current HP' cannot equal 0
    :return: Boolean (True or False)

    >>> is_alive(character={'Current HP': 0})
    False
    >>> is_alive(character={'Current HP': 5})
    True
    """
    if character['Current HP'] > 0:
        return True
    else:
        return False


def guessing_game(character):
    """
    Guessing game with a range of 1 to 5 inclusive and updates 'Current HP' depending on result.

    :param: a dictionary containing character data
    :precondition: parameter must be a dictionary containing 'Current HP'
    :precondition: input must be within a range of 1 to 5 inclusive
    :postcondition: input is evaluated against a random integer between 1 to 5 inclusive and prints the result
    :return: updated value for 'Current HP'

    """
    hp = (character.get('Current HP'))
    secret_number = random.randint(1, 5)
    guess = int(input(f"\nEnter a number between {1} and {5} inclusive: "))
    if guess == secret_number:
        print(f"You're right!")
        print(f"The Wraith grants you...", (colored("HP +20  Power +5", 'magenta')))
        character['Current HP'] += 20
        character['Power'] += 10
        character['EXP'] += 5
    elif guess < secret_number:
        print(f"Too low, the number was {secret_number}")
        random_damage = random.choice(range(5, 10))
        print(f"The Wraith drains your life force...", (colored("HP -", 'magenta')),
              (colored(random_damage, 'magenta')))
        character['Current HP'] -= random_damage
    else:
        print(f"Too high, the number was {secret_number}")
        random_damage = random.choice(range(5, 10))
        print(f"The Wraith drains your life force...", (colored("HP -", 'magenta')),
              (colored(random_damage, 'magenta')))
        character['Current HP'] -= random_damage
    return hp


def check_for_foes():
    """
    25% Chance to randomly encounter a foe after each move.

    :precondition: player has moved since last input
    :precondition: percentage_chance set to 0.25
    :postcondition: random number is evaluated against percentage chance
    :return: if greater than percentage chance returns True, else returns False
    """
    percentage_chance = 0.20
    if random.random() < percentage_chance:
        return True
    else:
        return False


def check_if_goal_attained(character):
    """
    Checks if player has reached the bottom right corner of game board.

    :param: a dictionary containing character data
    :precondition: x must exist in a range of 0 to 3 inclusive
    :precondition: y must exist in a range of 0 to 3 inclusive
    :postcondition: tuple containing variables x and y, is evaluated against coordinate of final position in game board
    :return: Boolean (True or False)

    >>> check_if_goal_attained(character={'X-coordinate': 25, 'Y-coordinate': 25})
    True
    >>> check_if_goal_attained(character={'X-coordinate': 2, 'Y-coordinate': 1})
    False
    """
    x = (character.get('X-coordinate'))
    y = (character.get('Y-coordinate'))
    if (x, y) == (25, 25):
        return True
    else:
        return False


def make_character():
    """
    Stores X and Y coordinates and current HP of the character.

    :precondition: a dictionary that includes coordinates and current hp is present
    :postcondition: return character
    :return: a dictionary (character), that contains character data

    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Class': 0, 'Current HP': 20, 'Power': 1, 'EXP': 0}
    """
    character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Class': 0, 'Current HP': 20, 'Power': 1, 'EXP': 0}
    return character


def move_character_backwards(character, direction):
    """
    Moves the character backwards in one of four directions.

    :param character: a a dictionary containing character data
    :param: a dictionary containing character data
    :param direction: user input that corresponds to one of four directions (string)
    :precondition: user must provide an input between 1 to 4 inclusive
    :postcondition: Value of coordinate is incremented or decremented by 1, dependant on direction
    :return: a dictionary containing current position and current HP of player

    >>> move_character(character={'X-coordinate': 0}, direction="EAST")
    {'X-coordinate': 1}
    >>> move_character(character={'Y-coordinate': 0}, direction="SOUTH")
    {'Y-coordinate': 1}
    """
    if direction == "EAST":
        character['X-coordinate'] -= 1
    elif direction == "WEST":
        character['X-coordinate'] += 1
    elif direction == "SOUTH":
        character['Y-coordinate'] -= 1
    else:
        character['Y-coordinate'] += 1
    return character


def move_character(character, direction):
    """
    Moves the character in one of four directions.

    :param character: a a dictionary containing character data
    :param: a dictionary containing character data
    :param direction: user input that corresponds to one of four directions (string)
    :precondition: user must provide an input between 1 to 4 inclusive
    :postcondition: Value of coordinate is incremented or decremented by 1, dependant on direction
    :return: a dictionary containing current position and current HP of player

    >>> move_character(character={'X-coordinate': 0}, direction="EAST")
    {'X-coordinate': 1}
    >>> move_character(character={'Y-coordinate': 0}, direction="SOUTH")
    {'Y-coordinate': 1}
    """
    if direction == "EAST":
        character['X-coordinate'] += 1
    elif direction == "WEST":
        character['X-coordinate'] -= 1
    elif direction == "SOUTH":
        character['Y-coordinate'] += 1
    else:
        character['Y-coordinate'] -= 1
    return character


def validate_move(character, direction):
    """
    Checks whether or not player move is within range of the game board.

    :param character: a a dictionary containing character data
    :param direction: user input that corresponds to one of four directions (string)
    :precondition: direction input must correspond with one of four options
    :postcondition: checks x and y values if they are within range of 0 to 3 inclusive
    :return: Boolean (True or False)

    >>> validate_move(make_character(), direction="EAST")
    True
    >>> validate_move({'X-coordinate': 0, 'Y-coordinate': 0}, direction="WEST")
    False
    """
    x = (character.get('X-coordinate'))
    y = (character.get('Y-coordinate'))
    if 26 > x > -1 and 26 > y > -1:
        if direction == "EAST":
            if x != 25:
                x += 1
                return True
            else:
                return False
        elif direction == "WEST":
            if x != 0:
                x += -1
                return True
            else:
                return False
        elif direction == "NORTH":
            if y != 0:
                y += -1
                return True
            else:
                return False
        else:
            if y != 25:
                y += 1
                return True
            else:
                return False
    else:
        return False


def get_user_choice():
    """
    Prompts user to choose a direction.

    :precondition: input must be valid (must be in a range of 1 to 4 inclusive)
    :postcondition: input is compared to values in direction choice, if invalid input, user is prompted for input again
    :return: A string representing direction chosen by user

    """
    direction_options = {"1": "NORTH", "2": "EAST", "3": "SOUTH", "4": "WEST", "q": 'QUIT GAME'}
    while True:
        user_input = input(f"---------------------------------------------------------"
                           "\nWhich direction would you like to go?"
                           "\n[q: QUIT GAME] NORTH: [1], EAST: [2], SOUTH: [3], WEST: [4]: ")
        if user_input == 'q':
            print(colored(f"\nYou have exited your current session\n", 'red'))
            quit(game())
        if user_input not in direction_options:
            print(f"Invalid input, try again.")
            continue
        return direction_options[user_input]


def describe_current_location(board, character):
    """
    Describes current location of player.

    :param: character: a dictionary containing map descriptions
    :param: board: a dictionary containing coordinate data and list of room names
    :precondition: x and y in character must be within range of lower to upper bound of board
    :postcondition: x and y in character are extracted and evaluated in the game board
    :return: string describing current location

    """
    x = (character.get('X-coordinate'))
    y = (character.get('Y-coordinate'))
    current_coordinate = (x, y)
    board_description = board[current_coordinate]

    return board_description


def make_board(rows, columns):
    """
    Generates a board depending on rows and columns provided and assigns descriptions to coordinates.

    :param: integer representing number of rows
    :param: integer representing number of columns
    :precondition: arguments provided must be integers
    :postcondition: board dictionary is generated and room descriptions are associated with keys
    :return: board (dictionary)

    """
    board = {}
    for row in range(rows):
        for column in range(columns):
            board[(row, column)] = random.choice([colored('Corridor', 'white'),
                                                  colored('Flaying room', 'white'),
                                                  colored('Spiraling staircase', 'white'),
                                                  colored('Library', 'white'),
                                                  colored('Ballroom', 'white')])

    return board


def main():
    """
    Drives the program.
    """
    game()


if __name__ == "__main__":
    main()
