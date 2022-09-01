#!/usr/bin/env python3
import sys
import os

import wslpy.convert
import wslpy.exec

# TODO: auto-detect?
SUBLIME_PATH = "C:\\Program Files\\Sublime Text\\subl.exe"

def canonicalize(path):
    return os.path.realpath(os.path.expanduser(path))

def convert(path):
    return wslpy.convert.to_win(canonicalize(path))

def quote(arg):
    return arg.replace(" ", "` ")

def join(args):
    return " ".join(quote(arg) for arg in args)

if __name__=="__main__":
    win_args = [SUBLIME_PATH]
    suppress_conversion = False
    always_convert = False
    for arg in sys.argv[1:]:
        if suppress_conversion:
            suppress_conversion = False
            win_args.append(arg)
        elif always_convert:
            win_args.append(convert(arg))
        elif arg.startswith("--command"):
            suppress_conversion = True
            win_args.append(arg)
        elif arg == "--":
            always_convert = True
            win_args.append(arg)
        elif arg.startswith("-"):
            win_args.append(arg)
        else:
            win_args.append(convert(arg))
    cmd_string = join(win_args)
    result = wslpy.exec.winps(cmd_string)
    sys.stdout.write(result.stdout)
    sys.stderr.write(result.stderr)
    sys.exit(result.returncode)
