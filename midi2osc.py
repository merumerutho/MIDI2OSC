import defs
import logging
from pythonosc.udp_client import SimpleUDPClient

def eval_midi_msg(config, msg, client):
    known_midi = False
    if msg:
        delta = msg[1]
        msg = msg[0]
        # Now, parse message through the currently supported methods
        known_midi = check_cc(config, msg, client) or\
                     check_note(config, msg, client) or\
                     check_start_continue(config, msg, client) or\
                     check_stop(config, msg, client)

        if not known_midi:
            logging.info(msg)
    return


def check_cc(config, msg, client):
    if defs.CC_START_RANGE <= msg[0] < defs.CC_END_RANGE:
        cmd, ctrl, data = msg[0], msg[1], msg[2]
        channel = (cmd - defs.CC_START_RANGE)
        logging.info("Midi CC: channel {}, control {}, data {}".format(channel, ctrl, data))

        return True


def check_note(config, msg, client):
    if defs.NOTE_ON_START_RANGE <= msg[0] < defs.NOTE_ON_END_RANGE:
        channel, note, velocity = (msg[0] - defs.NOTE_ON_START_RANGE), msg[1], msg[2]
        logging.info("Midi note on: channel {}, note {}, velocity {}".format(channel, note, velocity))

        return True
    elif defs.NOTE_OFF_START_RANGE <= msg[0] < defs.NOTE_OFF_END_RANGE:
        channel, note, velocity = (msg[0] - defs.NOTE_OFF_START_RANGE), msg[1], msg[2]
        logging.info("Midi note off: channel {}, note {}, velocity {}".format(channel, note, velocity))

        return True


def check_start_continue(config, msg, client):
    if defs.MIDI_START == msg[0] or defs.MIDI_CONTINUE == msg[0]:
        logging.info("Midi Start/Continue")

        return True


def check_stop(config, msg, client):
    if defs.MIDI_STOP == msg[0]:
        logging.info("Midi Stop")

        return True
