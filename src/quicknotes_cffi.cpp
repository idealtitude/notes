#include "quicknotes_core.h"
#include <cstring>

extern "C"
{
	QuickNotesCore* quicknotes_core_new()
	{
		return new QuickNotesCore();
	}

	int quicknotes_core_add_note(QuickNotesCore* core, const char* content)
	{
		return core->add_note(content);
	}

	const char* quicknotes_core_show_note(QuickNotesCore* core, int id)
	{
		std::string result = core->show_note(id);
		char* c_result = new char[result.length() + 1];
		std::strcpy(c_result, result.c_str());
		return c_result;
	}
}
