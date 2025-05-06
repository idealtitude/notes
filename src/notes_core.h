#ifndef NOTES_CORE_H
#define NOTES_CORE_H

#include <string>
#include <vector>

struct Note
{
	int id;
	std::string content;
};

class NotesCore
{
  public:
	NotesCore();

	int add_note(const std::string& content);
	std::string show_note(int id);
	std::vector<Note> list_notes();

  private:
	std::vector<Note> notes;
	int next_id;
};

#endif // NOTES_CORE_H
