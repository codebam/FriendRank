#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FriendRank
Author: Sean Behan
Inspired by an idea from Terri Dobbins
"""

import json


def load_save():
    """ Loads saved json file with friend list
    """
    data = {}
    try:
        with open('save.json', 'r') as savefile:
            data = json.load(savefile)
    except FileNotFoundError:
        pass
    return data


def save_dict(person_dict):
    """ Saves json file with friend list

    :person_dict: a dictionary holding all users
    """
    with open('save.json', 'w') as savefile:
        json.dump(person_dict, savefile)


def get_person_info():
    """ Prompts user for friend info
    """
    print("What's their name?")
    name = input()
    print("What's their rank?")
    rank = convert_to_int(input())
    return [name, rank]


def add_new_person(person_dict, name, rank):
    """ adds the new person to the person_dict

    :person_dict: a dictionary holding all users
    :name: new person name to be added
    :rank: rank of person to be added
    :returns: person_dict changed with new person added
    """
    person_dict[name] = rank
    return person_dict


def show_saved(person_dict):
    """ show saved people with their ranks

    :person_dict: a dictionary holding all users
    :returns: output to be displayed to terminal
    """
    if person_dict == {}:
        output = "\nNo names in name list!\n"
        return output
    output = "\n----------------------------\n"
    output += "Name\t\tRank"
    output += "\n"
    for name in person_dict:
        output += ('\n%-*s\t%s' % (10, name, person_dict[name]))
    output += "\n----------------------------"
    return output


def convert_to_int(number):
    """ Converts the user input into an integer or throws an error and retrys

    :number: a string with a numerical value
    :returns: an integer of the string, or None if it cannot be converted
    """
    try:
        int_input = int(number)
        if int_input not in range(101):
            raise ValueError('''\
            Not in the range of numbers that we have programmed for\
            ''')
        return int_input
    except ValueError:
        print("This is not valid input, please try again.")
        return None


PROMPT = '''
You can do a few things here :)

Type a number to choose.

1. Show saved people
2. Add a new person
3. Set an existing persons rank

4. Quit program
'''


def main():
    """ Main function run when the program is started
    """
    print('''\nWelcome to FriendRank!\n''')

    person_dict = load_save()
    listening_for_names = True
    # Initialize some variables

    while listening_for_names:
        print(PROMPT)
        user_input = input("Selection: ")
        user_input_int = convert_to_int(user_input)

        '''
        print('user_input: ', list(user_input))
        print('user_input_int: ', list(str(user_input_int)))
        '''

        if user_input_int == 1:
            print(show_saved(person_dict))
        elif user_input_int in [2, 3]:
            new_person_info = get_person_info()
            person_dict = add_new_person(person_dict, new_person_info[0],
                                         new_person_info[1])
            print(show_saved(person_dict))
            save_dict(person_dict)
        elif user_input_int == 4:
            print("Bye :)")
            quit()


if __name__ == "__main__":
    main()
