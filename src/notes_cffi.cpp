#include "notes_core.h"
#include <cstring>

extern "C"
{
	NotesCore* Notes_core_new()
	{
		return new NotesCore();
	}

	int Notes_core_add_note(NotesCore* core, const char* content)
	{
		return core->add_note(content);
	}

	const char* Notes_core_show_note(NotesCore* core, int id)
	{
		std::string result = core->show_note(id);
		char* c_result = new char[result.length() + 1];
		std::strcpy(c_result, result.c_str());
		return c_result;
	}
}
