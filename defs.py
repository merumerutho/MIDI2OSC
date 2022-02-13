import logging

ERR_NO_MIDI_PORTS =         -1
ERR_INVALID_INPUT =         -2
ERR_WRONG_MIDI_PORT =       -3
ERR_CANT_OPEN_MIDI_PORT =   -4
ERR_INVALID_JSON =          -5

CC_START_RANGE =            176
CC_END_RANGE =              192

NOTE_OFF_START_RANGE =      128
NOTE_OFF_END_RANGE =        143

NOTE_ON_START_RANGE =       144
NOTE_ON_END_RANGE =         159

MIDI_START =                250
MIDI_CONTINUE =             251
MIDI_STOP =                 252

DEFAULT_OSC_IP =            "127.0.0.1"
DEFAULT_OSC_PORT =          55555

LOGGING_LEVEL =             logging.INFO