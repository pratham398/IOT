import sqlite3
import os


db = sqlite3.connect('db.sqlite3')
print("Opened Database Successfully !!")
# Get the current working directory
current_directory = os.getcwd()

# Create the full path to the database file
database_path = os.path.join(current_directory, 'db.sqlite3')
# Print the full path
print("Database file is located at:", database_path)

cursor = db.cursor()

print("Do you want to reset the table yFACES ? (Y/N)")
s = str(input()).lower()
if s == 'y':
    cursor.execute("DROP TABLE FACES")
    print("Reset Database Successfully !!")
elif s == 'n':
    print("Exited Operation !!")

db.commit()
db.close()
