#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the main entry point of the app
"""

# TODO: implement `uv` Workspace:
# https://docs.astral.sh/uv/concepts/projects/workspaces/#workspace-layouts

import sys
import os

# import re
from cffi import FFI

from typing import Any
import argparse

type TuplAny = tuple[Any, Any, Any]


# Meta
__app_name__: str = "notes"
__app_author__: str = "idealtitude"
__app_version__: str = "0.0.1"
__app_license__: str = "MT108"

# Constants
EXIT_SUCCESS: int = 0
EXIT_FAILURE: int = 1
# Paths used by the app
LIB_DIR: str = "libnotes"
APP_PATH: str = os.path.dirname(os.path.realpath(__file__))
APP_LIB_PATH: str = os.path.join(APP_PATH, LIB_DIR)
USER_CWD: str = os.getcwd()
USER_HOME: str = os.path.expanduser("~")


def load_lib() -> TuplAny:
    ffi = FFI()
    ffi.cdef(
        """
        typedef struct NotesCore notesCore;
        notesCore* Notes_core_new();
        int Notes_core_add_note(notesCore* core, const char* content);
        const char* Notes_core_show_note(notesCore* core, int id);
    """
    )

    core: Any = None
    lib: Any = None
    lib_path: str = f"{APP_LIB_PATH}/notes_cffi.so"
    try:
        core = ffi.dlopen(lib_path)
        lib = core.Notes_core_new()
    except FileNotFoundError as ex:
        print(f"Error while loading libnotes; expected location:\n{lib_path}")

    return ffi, core, lib


def get_args() -> argparse.Namespace:
    """Parsing command line arguments using subparsers"""
    parser = argparse.ArgumentParser(
        prog=f"{__app_name__}",
        description=f"A minimalist app for taking notes. Read the documentation to discover the features of {
            __app_name__}",
        epilog=f"Read the documentation to learn how to use {__app_name__}",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add a note command
    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("name", type=str, help="The note name")
    add_parser.add_argument(
        "-c",
        "--category",
        nargs="?",
        type=str,
        help="Specify the category of the new note",
    )
    add_parser.add_argument(
        "-t", "--template", nargs="?", type=str, help="Specify the template to use"
    )

    # Show command
    show_parser = subparsers.add_parser("show", help="Show the content of a note")
    show_parser.add_argument(
        "-i",
        "--id",
        nargs="?",
        type=int,
        help="Display note by its identifier (integer)",
    )
    show_parser.add_argument(
        "-n", "--name", nargs="?", type=int, help="Display note by its name (string)"
    )

    # List command
    list_parser = subparsers.add_parser("list", help="List all notes.")
    list_parser.add_argument(
        "category", nargs="?", type=str, help="Filter notes by category (optional)"
    )

    return parser.parse_args()


class Notes:
    """libnotes API calls"""

    def __init__(self) -> None:
        """Calling load_lib from here"""
        libres: TuplAny = load_lib()
        self.ffi: Any = libres[0]
        self.core: Any = libres[1]
        self.lib: Any = libres[2]

    def add_note(self, note_name: str) -> None:
        note_id = self.lib.Notes_core_add_note(self.core, note_name.encode("utf-8"))
        print(f"Note added with ID: {note_id}")

    def show_note(self, note_id: int) -> None:
        result = self.lib.Notes_core_show_note(self.core, note_id)
        print(self.ffi.string(result).decode("utf-8"))

    def list_notes(self) -> None:
        # Implement later, as it is more complex with cffi.
        print("Listing notes (not yet implemented)")


def main(arguments: list[str]) -> int:
    """Entry point, main function"""
    if len(arguments) == 1:
        print("Error: missing arguments")
        return EXIT_FAILURE

    args: argparse.Namespace = get_args()
    notes: Notes = Notes()

    if notes.core is None:
        return EXIT_FAILURE

    if args.command == "add":
        notes.add_note(args.name)
    elif args.command == "show":
        notes.show_note(args.note_id)
    elif args.command == "list":
        notes.list_notes()
    else:
        args.print_help()

    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main(sys.argv))
