import sqlite3

# CONNECT & CREATE CURSOR
conn = sqlite3.connect('database.db')
c = conn.cursor()

# DELETE OLD TABLE
c.execute("DROP TABLE IF EXISTS users")

# CREATE TABLE
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        Student_ID INTEGER,
        Student_Name TEXT NOT NULL,
        Course TEXT NOT NULL,
        Email TEXT,
        Password TEXT,
        UNIQUE (Email, Password)
    )
''')
conn.commit()

# TEST DATA - 4 columns (exclude auto-ID)
testdata = [
    ('25-2763', 'Mojica Brandon Leonand D.R.', 'BSIT', 'gg@email.com', 'gg198'),
    ('25-2823', 'Ana Santos', 'BSCS', 'ee@email.com', '1223hh'),
    ('25-2112', 'An Santos', 'BSCS', 'eeo1@email.com', '122113hh')
]

# INSERT - FIXED: 4 columns, 4 placeholders
c.executemany("""
    INSERT INTO users (Student_ID, Student_Name, Course, Email, Password)
    VALUES (?, ?, ?, ?, ?)
""", testdata)

conn.commit()
conn.close()







