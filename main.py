import sqlite3  # LINE 1 - Import SQLite

# CONNECT & CREATE CURSOR
conn = sqlite3.connect('database.db')  # LINE 4 ✅ Creates/opens file
c = conn.cursor()                     # LINE 6 ✅ SQL executor

# DELETE OLD TABLE
c.execute("DROP TABLE IF EXISTS users")  # LINE 9 ✅ Safe delete

# CREATE TABLE
c.execute('''                                       
    CREATE TABLE IF NOT EXISTS users (               
        Student_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        Student_Name TEXT NOT NULL,                  
        Course TEXT NOT NULL,                         
        Email TEXT,                                   
        Password TEXT,                                
        UNIQUE (Email, Password)                     
    )
''')                                                  # LINE 21
conn.commit()  # LINE 23 ✅ SAVE TABLE TO DISK!

# TEST DATA - FIXED (5 columns to match table)
testdata = [                                        # LINE 26
    ('Mojica Brandon Leonand D.R.', 'BSIT', 'gg@email.com', 'gg198'),     # LINE 27
    ('Ana Santos', 'BSCS', 'ee@email.com', '1223hh')                      # LINE 28
]

# INSERT MULTIPLE - FIXED SYNTAX
c.executemany("""                                   
    INSERT INTO users (Student_Name, Course, Email, Password) 
    VALUES (?, ?, ?, ?)                               
""", testdata)                                        # LINE 36

conn.commit()  # LINE 38 ✅ SAVE DATA!
conn.close()   # LINE 40 ✅ CLEANUP!



