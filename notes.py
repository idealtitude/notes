#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the main entry point of the app
"""

import sys
import os
#import re
from cffi import FFI

from typing import Any
import argparse


### App meta ###
__app_name__     : str = "notes"
__author__       : str = "idealtitude"
__version__      : str = "0.0.1"
__license__      : str = "MT108"

### Constants ###
## EXIT_* for readability
EXIT_SUCCESS     : int = 0
EXIT_FAILURE     : int = 1
## Paths used by the app
# APP_PATH   : str = os.path.dirname(os.path.realpath(__file__))
APP_CWD          : str = os.getcwd()
USER_HOME        : str = os.path.expanduser("~")


ffi = FFI()
ffi.cdef("""
    typedef struct notesCore notesCore;
    notesCore* notes_core_new();
    int notes_core_add_note(notesCore* core, const char* content);
    const char* notes_core_show_note(notesCore* core, int id);
""")

lib = ffi.dlopen("./_notes_cffi.so")

core = lib.notes_core_new()


def get_args() -> Any:
    """Parsing command line arguments using subparsers"""
    parser = argparse.ArgumentParser(
        prog=f"{__app_name__}",
        description=f"A minimalist app for taking notes. Read the documentation to discover the features of {__app_name__}",
        epilog=f"Read the documentation to learn how to use {__app_name__}"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add a note command
    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("title", type=str, help="The note title")

    # Show command
    show_parser = subparsers.add_parser("show", help="Show the content of a note")
    show_parser.add_argument("note_id", type=int, help="The ID of the note to show")

    # List command
    list_parser = subparsers.add_parser("list", help="List all notes.")

    return parser.parse_args()


def add_note(note):
    note_id = lib.notes_core_add_note(core, note.encode('utf-8'))
    print(f"Note added with ID: {note_id}")

def show_note(note_id):
    result = lib.notes_core_show_note(core, note_id)
    print(ffi.string(result).decode('utf-8'))

def list_notes():
    # Implement later, as it is more complex with cffi.
    print("Listing notes (not yet implemented)")


def main(arguments: list[str]) -> int:
    """Entry point, main function"""
    if len(arguments) == 1:
        print("Error: missing arguments")
        return EXIT_FAILURE

    args: Any = get_args()

    if args.command == "add":
        add_note(args.title)
    elif args.command == "show":
        show_note(args.note_id)
    elif args.command == "list":
        list_notes()
    else:
        parser.print_help()

    return EXIT_SUCCESS

if __name__ == "__main__":
    sys.exit(main(sys.argv))
