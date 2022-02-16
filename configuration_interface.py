import defs


def get_dest_cc(config, channel, ctrl):
    for ch in config["messages"]["channels"]:
        if ch["ch_id"] == channel:
            for cc in ch["CC"]:
                if cc["cc_id"] == ctrl:
                    return cc["dest"]
    return defs.ERR_DEST_NOT_FOUND


def get_dest_note_on(config, channel):
    for ch in config["messages"]["channels"]:
        if ch["ch_id"] == channel:
            return ch["notes"]["dest_note_on"]


def get_dest_note_off(config, channel):
    for ch in config["messages"]["channels"]:
        if ch["ch_id"] == channel:
            return ch["notes"]["dest_note_off"]


def get_dest_start(config):
    return config["messages"]["dest_start"]


def get_dest_stop(config):
    return config["messages"]["dest_stop"]
