PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE notes (
note_id integer primary key,
note_name text,
note_category int,
note_format text,
note_tags text,
note_body text,
note_date datetime,
node_edit datetime
);
CREATE TABLE categories (
category_id integer primary key,
category_name text,
category_parent int,
category_description text,
category_entries int,
category_date datetime,
category_edit datetime
);
CREATE TABLE bookmarks (
bookmark_id integer primary key,
note_id int,
bookmark_rating int
);
CREATE TABLE tags (
tag_id integer primary key,
note_id int,
tag text
);
COMMIT;
