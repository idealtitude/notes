#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the entry point of the app
"""

from typing import Any
import sys
import os
import argparse

# import re
import importlib.resources


# Custom type for argparse return type
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
APP_PATH: str = os.path.dirname(os.path.realpath(__file__))
USER_CWD: str = os.getcwd()
USER_HOME: str = os.path.expanduser("~")


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


def load_config() -> Any:
    """Loading configuration and settings path to db"""
    config_path_in_package: Any = importlib.resources.files("notes").joinpath(
        "data/notes.conf"
    )
    config_content: Any
    with open(config_path_in_package) as f:
        config_content = f.read()

    # Process config_content
    # → config: dict[str, str] = parse_config(config_content)
    # en attendant ↓
    return config_content


def main() -> int:
    """Entry point, main function"""
    args: argparse.Namespace = get_args()
    config: Any = load_config()
    print(f"Conf: {config}")

    if args.command == "add":
        print("Not implemented yet")
    elif args.command == "show":
        print("Not implemented yet")
    elif args.command == "list":
        print("Not implemented yet")
    else:
        print("Rest not implemented either")

    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
