import argparse
import logging

import pythonosc
import rtmidi

import cli
import defs


def parse_port(args, ports):
    choice = False
    # If name was specified
    if args.input:
        flag = False
        for e, i in enumerate(ports):
            if args.input in e:
                choice = ports[i]
                flag=True
        if not flag:
            logging.error("Cannot find argument-specified MIDI-In port.")
    # If number was specified
    elif args.input_number:
        try:
            assert(0 <= args.input_number < len(ports))
        except AssertionError:
            logging.error("Argument-specified MIDI-In port number out of range!")
            choice = False
    return choice


def main():
    args = argparse.ArgumentParser()
    group = args.add_mutually_exclusive_group()
    group.add_argument("-ii", "--input", required=False, help="(Partial) name of the input interface")
    group.add_argument("-in", "--input_number", required=False, help="Id of the input interface (0-base)")
    args = args.parse_args()

    # Display intro
    cli.intro()

    # Seek for midi ports
    midi_in = rtmidi.MidiIn()
    ports = midi_in.get_ports()
    if not ports:
        logging.error("No MIDI-In ports found!")
        exit(defs.ERR_NO_MIDI_PORTS)

    # Parse user-choice port
    port_choice = parse_port(args, ports)
    if not port_choice:
        print("Choose your MIDI-in port interface...")
        cli.display_as_list(ports)
        port_choice = cli.user_input_number(0, len(ports)-1)
        print("({}) selected as MIDI-In port.".format(ports[port_choice]))

    # Open port
    try:
        midi_in.open_port(port_choice)
    except BaseException as e:
        logging.error("Could not open specified port! Error: {}".format(e))
        exit(defs.ERR_CANT_OPEN_MIDI_PORT)


if __name__ == "__main__":
    main()
