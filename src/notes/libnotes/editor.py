"""This class is the default editor for taking and editing notes and categories"""

from typing import Any

# Third-party packages
from prompt_toolkit.shortcuts import PromptSession
from prompt_toolkit import print_formatted_text as pfmt
from prompt_toolkit.key_binding import KeyBindings


class Editor:
    """The internal editor of notes"""
    def __init__(sellf) -> None:
        self.content: list[str]

    def textarea(self, editor_prompt: str) -> None:
        """This method use `prompt_toolkit` to create a \"textarea\""""
        bindings: KeyBindings = KeyBindings()
        # `Ctrl+S` to exit
        @bindings.add('c-s')
        def _(event: Any):
            event.app.exit(result=event.app.current_buffer.text)

        session: PromptSession = PromptSession(
            pfmt("> "),
            multiline=True,
            key_bindings=bindings,
        )
        text = session.prompt()
        print("\nVous avez entré :")
        print(text)
