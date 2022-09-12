#!/usr/bin/env python3
import sys
import os
import glob

import wslpy.convert
import wslpy.exec
import wslpy.system

def findWinSubl():
    program_dirs = ["/mnt/c/Program Files", "/mnt/c/Program Files (x86)"]
    possible_subl_dirs = []
    for program_dir in program_dirs:
        possible_subl_dirs += glob.glob(os.path.join(program_dir, "*ublime*"))
    for possible_subl_dir in possible_subl_dirs:
        subl_path = os.path.join(possible_subl_dir, "subl.exe")
        if os.path.isfile(subl_path):
            return subl_path
    raise Exception("Could not find Sublime Text installation")

SUBLIME_PATH = os.environ.get("SUBLIME_PATH", findWinSubl())

def canonicalize(path):
    return os.path.realpath(os.path.expanduser(path))

def convert(path):
    return wslpy.convert.to_win(canonicalize(path))

def quote(arg):
    return arg.replace(" ", "` ")

def join(args):
    return " ".join(quote(arg) for arg in args)

if __name__=="__main__":
    win_args = [convert(SUBLIME_PATH)]
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
