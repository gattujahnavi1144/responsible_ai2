import sqlite3
 
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id TEXT, name TEXT)")
cursor.executemany("INSERT INTO users VALUES (?, ?)", [("1", "Alice"), ("2", "Bob")])
conn.commit()
 
 
def get_user(user_id):
    query = "SELECT * FROM users WHERE id = ?"
    return cursor.execute(query, (user_id,)).fetchall()
 
 
print("Normal lookup:", get_user("1"))
print("Attack input: ", get_user("1 OR 1=1"))
