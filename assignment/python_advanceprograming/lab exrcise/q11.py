import sqlite3


conn = sqlite3.connect("student.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")


cursor.execute("INSERT INTO student (name, age) VALUES ('Sneha', 21)")
conn.commit()


cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
