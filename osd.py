"""
TODO:
 - In process config loading
 - Command line config loading
 - Config save
 - Hot reload
 - Multi mod input
"""

import os
import RPi.GPIO as GPIO
from smbus import SMBus
bus = SMBus(1)

def write_to_ivad(address, msg_1, msg_2):
    bus.write_byte_data(address, msg_1, msg_2)

def apply_config():
    for parm in parms_list:
        write_to_ivad(0x46, parm.offset, user_config[parm.name])

class parm:
    def __init__(
            self, 
            name: str,
            offset: int, 
            min_val: int, 
            max_val: int
        ):
        self.name = name
        self.offset = offset
        self.min_val = min_val
        self.max_val = max_val

# will use number entered as index
parms_list = [
        parm("CONTRAST", 0x00, 0xB5, 0xFF),
        parm("RED DRIVE", 0x01, 0x00, 0xFF),
        parm("GREEN DRIVE", 0x02, 0x00, 0xFF),
        parm("BLUE DRIVE", 0x03, 0x00, 0xFF),
        parm("RED CUTOFF", 0x04, 0x00, 0xFF),
        parm("GREEN CUTOFF", 0x05, 0x00, 0xFF),
        parm("BLUE CUTOFF", 0x06, 0x00, 0xFF),
        parm("HORIZONTAL POSITION", 0x07, 0x80, 0xFF),
        parm("HEIGHT", 0x08, 0x80, 0xFF),
        parm("VERTICAL POSITION", 0x09, 0x00, 0x7F),
        parm("S CORRECTION", 0x0A, 0x80, 0xFF),
        parm("KEYSTONE", 0x0B, 0x80, 0xFF),
        parm("PINCUSHION", 0x0C, 0x80, 0xFF),
        parm("WIDTH", 0x0D, 0x80, 0x7F),
        parm("PINCUSHION BALANCE", 0x0E, 0x80, 0xFF),
        parm("PARALELLOGRAM", 0x0F, 0x80, 0xFF),
        parm("BRIGHTNESS DRIVE", 0x10, 0x00, 0x40),
        parm("BRIGHTNESS", 0x11, 0x00, 0x20),
        parm("ROTATION", 0x12, 0x00, 0x7F),
    ]

user_config = {
    "CONTRAST":            0xFA,
    "RED DRIVE":           0x93,
    "GREEN DRIVE":         0x93,
    "BLUE DRIVE":          0x8F,
    "RED CUTOFF":          0x90,
    "GREEN CUTOFF":        0x8B,
    "BLUE CUTOFF":         0x6D,
    "HORIZONTAL POSITION": 0x8C,
    "HEIGHT":              0xDC,
    "VERTICAL POSITION":   0x49,
    "S CORRECTION":        0x92,
    "KEYSTONE":            0xA2,
    "PINCUSHION":          0xBF,
    "WIDTH":               0x71,
    "PINCUSHION BALANCE":  0xC2,
    "PARALELLOGRAM":       0xD2,
    "BRIGHTNESS DRIVE":    0x40,
    "BRIGHTNESS":          0x09,
    "ROTATION":            0x27
}

hot_reload = False

def main_loop():
    """ 
    Run the main CLI config loop.

    Implicitly makes changes to the user config attached to the crrent process.
    """
    entered_key = '';

    while (entered_key != 'q'):
        os.system('clear');
        for i, parm in enumerate(parms_list):
            print(str(i) + ":", parm.name);
        print()
        print("A: APPLY CONIFG")
        print("R: TOGGLE HOT RELOAD", "ON" if hot_reload else "OFF")
        print("L {name}: LOAD CONFIG")
        print("S {name}: SAVE CONFIG")
        entered_key = input("... ")
        if (entered_key.isdecimal()):
            entered_key_int = int(entered_key)
            if (entered_key_int in range(len(parms_list))):
                mod_parm_loop(entered_key_int)
        else:
            setting_handler(entered_key)

        print(user_config)

def mod_parm_loop(parm_number):
    """Run an interective configuration on parameter at parm_number."""
    parm_info = parms_list[parm_number]
    mod_key = '';

    while (mod_key != 'q'):
        os.system('clear')
        # print("Currently modifiying:")
        print(parm_number, '|', parm_info.name, '| MIN', parm_info.min_val, '| MAX', parm_info.max_val)
        print("CURRENT VALUE:", user_config[parm_info.name])
        mod_key = input("... ")
        mod_handler(parm_info, mod_key)
        if (hot_reload): apply_config()

def setting_handler(setting, option = None):
    """Enact the requested setting with an optional option."""
    if setting == 'A':
        apply_config()
    elif setting == 'R':
        global hot_reload
        hot_reload = not hot_reload
    elif setting == 'L':
        # load config from file
        pass
    elif setting == 'S':
        # save config
        pass

def mod_handler(parm_info, mod):
    """
    Apply the modifier to the given parameter.

        Arguments:
            parm_info (class Parm): The paramter to be modified 
            modifier (string): The modifier to be applied to the user conifg
                paramter that corresponds to parm_info. 

        Returns:
            Nothing for now.
    """
    if mod == '+':
        user_config[parm_info.name] += 1
    elif mod == '-':
        user_config[parm_info.name] -= 1
    elif mod.isdecimal():
        mod_int = int(mod)
        if(mod_int >= parm_info.min_val and mod_int <= parm_info.max_val):
            user_config[parm_info.name] = mod_int
        else:
            print("VALUE OUT OF BOUNDS")
            input()

if __name__ == "__main__":
    # TODO: Add logic for loading in config from script call
    os.system('clear');
    main_loop()

# TODO
# mainloop: if get valid key e.g. "1" for contrast 
#  -> parm_loop(parm): if get valid key e.g. "+", parm.increment() -> mod state
#
#
#
#
