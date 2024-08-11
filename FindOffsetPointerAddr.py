import struct
import argparse

# enable Virtual Terminal Processing for windows command prompt colours
# import os
# if os.name == 'nt':
#     os.system('')

# class colours for terminal colours
class colours:
    import os
    if os.name == 'nt':
        os.system('')
    '''Colors class:reset all colors with colors.reset; two
    sub classes fg for foreground
    and bg for background; use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
    underline, reverse, strike through,
    and invisible work with the main class i.e. colors.bold'''
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'
    
    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'

def read_memory_dump(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def difference(first_dump, n_dumps,differences):
    possible_address=[]
    for i in range(0, len(first_dump)-4):  # Compare every 4 bytes (32-bit)
        first_val = struct.unpack('<I', first_dump[i:i+4])[0]
        for a in range(len(n_dumps)):
            nth_val = struct.unpack('<I', n_dumps[a][i:i+4])[0]
            if abs(nth_val- first_val) == differences[a]:
                if a == len(n_dumps)-1:
                    possible_address.append((i,first_val))
                    break
                continue
            else:
                break
    return possible_address

def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Offset pointer address finder for DS memory dump.')
    parser.add_argument('dump1', type=str, help='dump1.bin path')
    parser.add_argument('rest',metavar='dumpN dumpN_DIFF', nargs='+', help=f'''dumpN is the Nth additional dump path. eg dump2.bin.
                        dumpN_DIFF is the difference in {colours.fg.red}decimal integers{colours.reset} 
                        between the interested addresses in dump1 and Nth dump''')
    args = parser.parse_args()

    dump1 = read_memory_dump(args.dump1)
    rest = args.rest
    ndumpsstr = []
    differences = []
    for i in range(len(rest)):
        if is_int(rest[i]):
            differences.append(int(rest[i]))
        else:
            ndumpsstr.append(rest[i])
    n_dumps = []
    for x in ndumpsstr:
        n_dumps.append(read_memory_dump(x))

    possible_address= difference(dump1,n_dumps,differences)
    for i in possible_address:
        u_offset = "0x02000000"  # add universal offset
        u_offset_int = int(u_offset, 16)
        
        print(f"Possible pointer address: [{colours.fg.lightred}{i[0]+u_offset_int:#010x}{colours.reset}] = {i[1]:#010x} in file 1")