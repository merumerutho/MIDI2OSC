import defs
import logging

def intro():
    print("*"*80)
    print("*\t Welcome to MIDI2OSC.")
    print("*")
    print("*\t Converts MIDI-IN to OSC messages.")
    print("*\t Author: merumerutho (meru.cloud, github.com/merutochan)")
    print("*"*80)


def display_as_list(lst):
    for i, e in enumerate(lst):
        print("\t{}) {}".format(i, e))


def user_input_number(min_val, max_val):
    usr_in = input(">")
    try:
        usr_in = int(usr_in.strip())
        assert(min_val <= usr_in <= max_val)
    except ValueError or TypeError:
        logging.error("Invalid data. Input must be a number.")
    except AssertionError:
        logging.error("Invalid number.")
        exit(defs.ERR_INVALID_INPUT)
    return usr_in
