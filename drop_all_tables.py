import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Disable foreign keys
cursor.execute('PRAGMA foreign_keys = OFF;')

# Begin transaction
cursor.execute('BEGIN TRANSACTION;')

# Fetch all table names excluding sqlite_sequence
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name!='sqlite_sequence';")
tables = cursor.fetchall()

# Drop all tables
for table in tables:
    cursor.execute(f'DROP TABLE IF EXISTS {table[0]};')

# Commit transaction and enable foreign keys
cursor.execute('COMMIT;')
cursor.execute('PRAGMA foreign_keys = ON;')

# Close the connection
conn.close()

print("All tables dropped successfully, excluding sqlite_sequence.")