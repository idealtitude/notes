#include "notes_core.h"

NotesCore::NotesCore()
	: next_id(1)
{}

int NotesCore::add_note(const std::string& content)
{
	Note newNote = {next_id, content};
	notes.push_back(newNote);
	return next_id++;
}

std::string NotesCore::show_note(int id)
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

std::vector<Note> NotesCore::list_notes()
{
	return notes;
}
