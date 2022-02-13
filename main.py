import argparse
import logging
import json

import pythonosc
import rtmidi

import cli
import defs

import midi2osc

def parse_config(config_path):
    config = None
    try:
        config = json.loads(config_path)
    except json.JSONDecodeError:
        logging.error("Could not decode config JSON file.")
    return config

def parse_port(config, ports):
    choice = None
    if config:
        if config["interface"]:
            for i, e in enumerate(ports):
                if config["interface"] in e:
                    choice = i
                    break
    return choice


def main():
    # Display intro
    cli.intro()

    args = argparse.ArgumentParser()
    args.add_argument("-c", "--config_path", required=False, help="JSON configuration filepath.")
    args = args.parse_args()
    config = None

    if args.config_path:
        config = parse_config(args.config_path)

    # Seek for midi ports
    midi_in = rtmidi.MidiIn()
    ports = midi_in.get_ports()
    if not ports:
        logging.error("No MIDI-In ports found!")
        exit(defs.ERR_NO_MIDI_PORTS)

    # Parse user-choice port
    port_choice = parse_port(config, ports)
    if not port_choice:
        print("No MIDI-In port specified or found in configuration.")
        print("Choose your MIDI-in port interface:")
        cli.display_as_list(ports)
        port_choice = cli.user_input_number(0, len(ports)-1)
        print("({}) selected as MIDI-In port.".format(ports[port_choice]))

    # Open port
    try:
        midi_in.open_port(port_choice)
    except BaseException as e:
        logging.error("Could not open specified port! Error: {}".format(e))
        exit(defs.ERR_CANT_OPEN_MIDI_PORT)

    # Poll messages
    while True:
        msg = midi_in.get_message()
        midi2osc.parse_msg(msg)


if __name__ == "__main__":
    main()
