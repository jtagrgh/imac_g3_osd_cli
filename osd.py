import os

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

def default_config_generator(parms_list):
    for parm in parms_list:
        yield (parm.name, 0)

# TODO: add modal loops
# main loop & parm loop
def main_loop():

    user_config = {parm: value for parm, value in default_config_generator(parms_list)}

    entered_key = '';
    while (entered_key != 'q'):
        for i, parm in enumerate(parms_list):
            print(i, parm.name);
        entered_key = input("... ")
        # TODO convert in set to chars
        if (entered_key in range(len(parms_list))):
            print("in")
            mod_parm_loop(entered_key)
        os.system('clear');

    return

def mod_parm_loop(parm: int):
    mod_key = '';
    while (mod_key != 'q'):
        print
    return

def mod_parm_mode(parm: int, mod_key: str):
    return

main_loop()

# TODO
# mainloop: if get valid key e.g. "1" for contrast 
#  -> parm_loop(parm): if get valid key e.g. "+", parm.increment() -> mod state
#
#
#
#
