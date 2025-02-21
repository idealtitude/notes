# notes

A command line tools for manging notes, their respective categories, and templates (basic notes, memos, etc).

## Installation

**TODO** :  describe the installation process

## Basic Usage

**New Notes**

To create a new note:

```bash

notes note create "Title of my note" -c "Personal"
```

**List Notes**

To list all notes in the "Personal" category:

```bash
notes note list -c "Personal"
```

## Commands Reference

### note

**note create**

```
notes note create <title> [-n <name>] [-c <category>] [-t <template>] [-T <template_path>]
```

Creates a new note.

* <title> (required): The title of the note.
* -n, --name (optional): An alternative name for the note.
* -c, --category (optional): The category of the note.
* -t, --template (optional): The template to use. Or:
* -T, --template-path (optional): The path to a template file.

Examples:

```bash
notes note create "Meeting Notes" -c "Work" -t "meeting_template"
```
