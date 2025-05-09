"""This class is a container for the notes"""

from dataclasses import dataclass

@dataclass
class Note:
    """Note data"""
    note_id: int
    note_name: str
    note_category: int
    note_format: str
    note_body: list[str]
    note_date: str
    note_edit: str
