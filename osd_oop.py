import os

# TODO change this to capital P
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

def default_config_generator():
    for parm in parms_list:
        yield (parm.name, parm.min_val)

class Config:
    # The user config
    config = {}
    # The current inputted parameter key (number) being modified
    input_parm_key = ''
    # The current inputted value mofifier
    input_mod_key = ''
    # The current parm (Parm class) being modified
    mod_parm = ''

    def __init__(self):
        # does this need to be a dictionary?
        self.config = {parm: val for parm, val in default_config_generator()}

    def load_config(config):
        self.confg = config

    def run(self):
        while (self.input_parm_key != 'q'):
            os.system("clear")
            # Menu print -- start
            for i, parm in enumerate(parms_list):
                print(i, parm.name)
            self.input_parm_key = input("... ")
            # Menu print -- end
            if (self.input_parm_key.isdecimal()):
                self.input_parm_key = int(self.input_parm_key)
            # less ugly way to do this?
            if (self.input_parm_key in range(len(parms_list))):
                self.mod_parm()

    # Should only be called when self.input_parm_key is a decimal
    def mod_parm(self, parm_key = None):
        if parm_key != None:
            self.input_parm_key = parm_key
        self.mod_parm = parms_list[self.input_parm_key]
        self.mod_parm_value = self.config[self.mod_parm.name]

        while (self.input_mod_key != 'q'):
            os.system("clear")
            print(self.input_parm_key, '|', self.mod_parm.name, '| MIN', self.mod_parm.min_val, '| MAX', self.mod_parm.max_val)
            print("CURRENT VALUE:", self.mod_parm_value)
            self.input_mod_key = input("... ")

if __name__ == "__main__":
    main = Config()
    main.run()



    
