import argparse
import logging
import json

from pythonosc.udp_client import SimpleUDPClient
import rtmidi

import lib.cli as cli
import lib.defs as defs

import lib.midi2osc as midi2osc

# Set logger to
logging.getLogger().setLevel(defs.LOGGING_LEVEL)


def parse_config(config_path):
    config = None
    try:
        with open(config_path) as f:
            config = json.loads(f.read())
    except IOError:
        logging.error("Could not open the config filepath.")
    except json.JSONDecodeError:
        logging.error("Could not decode config JSON file.")
    return config


def parse_midi_port(config, ports):
    choice = None
    if config:
        if config["interface"]:
            for i, e in enumerate(ports):
                if config["interface"] in e:
                    choice = i
                    break
    return choice


def parse_osc_address_port(config):
    ip, port = None, None
    if config:
        ip, port = config.get("osc_ip"), config.get("osc_port")
    return ip, port


def main():
    # Display intro
    cli.intro()

    args = argparse.ArgumentParser()
    args.add_argument("-c", "--config_path", required=True, help="JSON configuration filepath.")
    args = args.parse_args()
    config = None
    osc_client = None

    if args.config_path:
        config = parse_config(args.config_path)

    # Seek for midi ports
    midi_in = rtmidi.MidiIn()
    ports = midi_in.get_ports()
    if not ports:
        logging.error("No MIDI-In ports found!")
        exit(defs.ERR_NO_MIDI_PORTS)

    # Parse user-choice MIDI port
    port_choice = parse_midi_port(config, ports)
    if not port_choice:
        print("No MIDI-In port specified or found in configuration.")
        print("Choose your MIDI-in port interface:")
        cli.display_as_list(ports)
        port_choice = cli.user_input_number(0, len(ports)-1)
        print("({}) selected as MIDI-In port.".format(ports[port_choice]))

    # Access MIDI-IN
    try:
        midi_in.open_port(port_choice)
    except BaseException as e:
        logging.error("Could not open specified port! Error: {}".format(e))
        exit(defs.ERR_CANT_OPEN_MIDI_PORT)
    print("Listening to {}.".format(ports[port_choice]))

    # Parse user-choice OSC address and port
    osc_ip, osc_port = parse_osc_address_port(config)
    if not osc_ip:
        osc_ip = defs.DEFAULT_OSC_IP
    if not osc_port:
        osc_port = defs.DEFAULT_OSC_PORT
    print("Selected {} as OSC Ip.".format(osc_ip))
    print("Selected {} as OSC Port.".format(osc_port))

    # Open OSC client
    try:
        osc_client = SimpleUDPClient(osc_ip, osc_port)
    except BaseException as e:
        logging.error("Could not open OSC address! Error: {}".format(e))
    print("Initiated OSC client.")

    # Infinite cycle
    while True:
        msg = midi_in.get_message()
        midi2osc.eval_midi_msg(config, msg, osc_client)


if __name__ == "__main__":
    main()
