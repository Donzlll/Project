import sqlite3

prof = {
    "Name": "Michael Reyes",
    "Student_ID": "25-1018",
    "Course": "BSIT",
    "Section": "BSIT 1-1",
    "Age": 19,
    "Gender": "Male"
}

conn = sqlite3.connect('database.db')
# PERFECT CREATE TABLE (6 columns)
conn.execute('''CREATE TABLE profile (
    Name TEXT,
    Student_ID TEXT,
    Course TEXT,
    Section TEXT,
    Age INTEGER,
    Gender TEXT
)''')

# PERFECT INSERT (6 values)
conn.execute('''INSERT INTO profile VALUES (?,?,?,?,?,?)''',
             (prof["Name"],
              prof["Student_ID"],
              prof["Course"],
              prof["Section"],
              prof["Age"],
              prof["Gender"]))

conn.commit()
conn.close()