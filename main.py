import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS users")
conn.commit()

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
conn.commit() #must commit to save changes

# ✅ FIXED: Proper INSERT with correct column order
Demodata = [
    ('Michael Reyes', 251018, 19, 'BSIT', 1),
    ('Ana Santos', 251019, 20, 'BSCS', 2),
    ('Juan Cruz', 251020, 18, 'BSIT', 1)
]


c.executemany("""
    INSERT INTO users (Name, Student_ID, Age, Course, Year) 
    VALUES (?, ?, ?, ?, ?)
""", Demodata)
conn.commit()
conn.close()

