import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()

#create a table
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        Student_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Age INTEGER NOT NULL,
        Course TEXT NOT NULL,
        Year INTEGER NOT NULL
    )
''')
conn.commit()

Demodata = [
    ('Michael Reyes', 19, 'BSIT', 1),     # Name, Age, Course, Year
    ('Ana Santos', 20, 'BSCS', 2),
    ('Juan Cruz', 18, 'BSIT', 1),
    ('Maria Lopez', 21, 'BSCE', 3)
]

c.executemany("""
    INSERT INTO users (Name, Age, Course, Year) 
    VALUES (?, ?, ?, ?)
""", Demodata)
conn.commit()
conn.close()
