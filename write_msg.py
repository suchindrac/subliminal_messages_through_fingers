from getkey import getkey, keys
import sys
import base64
import argparse

o_buff = ""

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=str, required=True, help = "File name to save text as")
args = parser.parse_args()
file_name = args.file

while True:
    try:
        key = getkey()
        if key == keys.BACKSPACE:
            o_buff = o_buff[:-1]
        elif key == keys.ENTER:
            fd = open(file_name, "w")
            e_buff_w = e_buff.decode("utf-8")
            fd.write(e_buff_w)
            fd.close()
        else:
            o_buff += key

            o_buff_s = o_buff.encode("utf-8")
            e_buff = base64.b64encode(o_buff_s)
            print(e_buff, end = "\r")
    except:
        print("Exiting")
        sys.exit(1)
