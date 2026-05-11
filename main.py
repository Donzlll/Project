import sqlite3
conn = sqlite3.connect('database.db') #Creates/opens database file
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS users") # Delete the existing data

#create a table
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        Student_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Student_Name TEXT NOT NULL,
        Student_Age INTEGER NOT NULL,
        Course TEXT NOT NULL,
        Year_Level INTEGER NOT NULL
    )
''')
conn.commit() #must commit to save changes
#multiple data
testdata = [
    ('Michael Reyes', 19, 'BSIT', 1),     # Name, Age, Course, Year
    ('Ana Santos', 20, 'BSCS', 2),
    ('Juan Cruz', 18, 'BSIT', 1),
    ('Maria Lopez', 21, 'BSCE', 3)
]

c.executemany("""
    INSERT INTO users (Student_Name, Student_Age, Course, Year_Level) 
    VALUES (?, ?, ?, ?)
""", testdata)

conn.commit()
conn.close()
