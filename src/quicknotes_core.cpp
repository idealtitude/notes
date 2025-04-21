#include "quicknotes_core.h"

QuickNotesCore::QuickNotesCore()
	: next_id(1)
{}

int QuickNotesCore::add_note(const std::string& content)
{
	Note newNote = {next_id, content};
	notes.push_back(newNote);
	return next_id++;
}

std::string QuickNotesCore::show_note(int id)
{
	for (const auto& note : notes)
	{
		if (note.id == id)
		{
			return note.content;
		}
	}

	return "Note not found.";
}

std::vector<Note> QuickNotesCore::list_notes()
{
	return notes;
}
