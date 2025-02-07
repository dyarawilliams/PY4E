import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

str_data = open('roster_data_sample.json').read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0]
    title = entry[1]
    role = entry[2]

    print((name, title))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ? )''',
        ( user_id, course_id, role ) )

    conn.commit()

# SQLite
# CREATE TABLE User (
#     id     INTEGER PRIMARY KEY,
#     name   TEXT UNIQUE
# );

# CREATE TABLE Course (
#     id     INTEGER PRIMARY KEY,
#     title  TEXT UNIQUE
# );

# CREATE TABLE Member (
#     user_id     INTEGER,
#     course_id   INTEGER,
#     role        INTEGER,
#     PRIMARY KEY (user_id, course_id)
# );

# SELECT * FROM Course
# JOIN Member ON Course.id = Member.course_id
# JOIN User ON Member.user_id = User.id;

# DROP TABLE Member;

# CREATE TABLE Member (
#     user_id     INTEGER,
#     course_id   INTEGER,
#     role_id     INTEGER,
#     PRIMARY KEY (user_id, course_id, role_id)
# );

# CREATE TABLE Role (
#     id          INTEGER PRIMARY KEY,
#     name        TEXT UNIQUE
# );

# INSERT INTO Role (id, name) VALUES (0, 'Student');
# INSERT INTO Role (id, name) VALUES (1, 'Instructor');