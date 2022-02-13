import defs


def parse_msg(msg):
    known_midi = False
    if msg:
        delta = msg[1]
        msg = msg[0]
        # Now, parse message through the currently supported methods
        known_midi = check_cc(msg) or check_note(msg) or check_start_continue(msg) or check_stop(msg)
        if not known_midi:
            print(msg)
    return


def check_cc(msg):
    if defs.CC_START_RANGE <= msg[0] < defs.CC_END_RANGE:
        cmd = msg[0]
        ctrl = msg[1]
        data = msg[2]
        channel = (cmd - defs.CC_START_RANGE)
        print("Midi CC: channel {}, control {}, data {}".format(channel, ctrl, data))
        return True


def check_note(msg):
    if defs.NOTE_ON_START_RANGE <= msg[0] < defs.NOTE_ON_END_RANGE:
        channel = msg[0] - defs.NOTE_ON_START_RANGE
        note = msg[1]
        velocity = msg[2]
        print("Midi note on: channel {}, note {}, velocity {}".format(channel, note, velocity))
        return True
    elif defs.NOTE_OFF_START_RANGE <= msg[0] < defs.NOTE_OFF_END_RANGE:
        channel = msg[0] - defs.NOTE_OFF_START_RANGE
        note = msg[1]
        velocity = msg[2]
        print("Midi note off: channel {}, note {}, velocity {}".format(channel, note, velocity))
        return True


def check_start_continue(msg):
    pass


def check_stop(msg):
    pass
