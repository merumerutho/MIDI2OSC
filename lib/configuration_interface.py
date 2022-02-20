import defs


def get_dest_cc(config, channel, ctrl):
    try:
        for ch in config.get("messages").get("channels"):
            if ch.get("ch_id") == channel:
                for cc in ch.get("CC"):
                    if cc.get("cc_id") == ctrl:
                        return cc.get("dest")
    except BaseException:
        return defs.ERR_DEST_NOT_FOUND


def get_dest_note_on(config, channel):
    try:
        for ch in config.get("messages").get("channels"):
            if ch.get("ch_id") == channel:
                return ch.get("notes").get("dest_note_on")
    except BaseException:
        return defs.ERR_DEST_NOT_FOUND


def get_dest_note_off(config, channel):
    try:
        for ch in config.get("messages").get("channels"):
            if ch.get("ch_id") == channel:
                return ch.get("notes").get("dest_note_off")
    except BaseException:
        return defs.ERR_DEST_NOT_FOUND


def get_dest_start(config):
    try:
        return config.get("messages").get("dest_start")
    except BaseException:
        return defs.ERR_DEST_NOT_FOUND


def get_dest_stop(config):
    try:
        return config.get("messages").get("dest_stop")
    except BaseException:
        return defs.ERR_DEST_NOT_FOUND
