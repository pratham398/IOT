import face_recognition
import sqlite3
import glob
import cv2
import os

IP_Webcam = False
flag = False
name = ""  # Initialize name variable outside the loop
face_encoding = None  # Initialize face_encoding variable outside the loop

if IP_Webcam:
    video_capture = cv2.VideoCapture('http://192.168.1.100:8080/videofeed')  # IP Webcam
else:
    video_capture = cv2.VideoCapture(0)

db = sqlite3.connect('db.sqlite3')
print("Opened Database Successfully !!")

# Get the current working directory
current_directory = os.getcwd()

# Create the full path to the database file
database_path = os.path.join(current_directory, 'db.sqlite3')

# Print the full path
print("Database file is located at:", database_path)

cursor = db.cursor()

# Create database
cursor.execute('''CREATE TABLE IF NOT EXISTS FACES
            (ID  INTEGER  PRIMARY KEY  AUTOINCREMENT,
            FACE_NAME    TEXT  NOT NULL,
            FACE_ENCODING   BLOB  NOT NULL );''')

while True:
    ret, frame = video_capture.read()

    cv2.imshow('Video', frame)
    flag = False

    c = cv2.waitKey(1)
    if 'q' == chr(c & 255):
        print("Exited Operation !!")
        break

    if 'c' == chr(c & 255):
        unknown_face_encodings = face_recognition.face_encodings(frame)
        if len(unknown_face_encodings) > 0:
            while not flag:
                print("Please enter your Name : ")
                name = str(input())
                cursor.execute("SELECT count(*) FROM FACES WHERE FACE_NAME = ?", (name,))
                data = cursor.fetchone()[0]
                if data == 0:
                    file_name = name + ".jpg"
                    cv2.imwrite(file_name, frame)
                    face_encoding = unknown_face_encodings[0]
                    flag = True
                else:
                    print("Name Already Exists, Want to enter another Name ? (Y/N)")
                    s = str(input()).lower()
                    if s == 'y':
                        continue
                    elif s == 'n':
                        file_name = name + ".jpg"
                        cv2.imwrite(file_name, frame)
                        face_encoding = unknown_face_encodings[0]
                        flag = True
                    elif s == 'e':
                        print("Exited Operation !!")
                        flag = True

            if not flag:
                break
        else:
            print("There's no face recognized in the image !!")

    if 's' == chr(c & 255):
        flag = True
        break

if not IP_Webcam:
    video_capture.release()
cv2.destroyAllWindows()

# Insert Operation
if not flag:
    cursor.execute("SELECT count(*) FROM FACES WHERE FACE_NAME = ?", (name,))
    data = cursor.fetchone()[0]
    if data == 0:
        cursor.execute("INSERT INTO FACES (FACE_NAME, FACE_ENCODING) VALUES (?, ?)",
                       (name, sqlite3.Binary(face_encoding)))
        print("Photo Captured Successfully !!")
    else:
        cursor.execute("DELETE FROM FACES WHERE FACE_NAME = ?", (name,))
        cursor.execute("INSERT INTO FACES (FACE_NAME, FACE_ENCODING) VALUES (?, ?)",
                       (name, sqlite3.Binary(face_encoding)))
        print("Photo Overwritten Successfully !!")

# Database Update Operation
print("Updating the Database !!")
for img in sorted(glob.glob("*.jpg")):
    img_name = os.path.basename(img)[:-4]
    cursor.execute("SELECT count(*) FROM FACES WHERE FACE_NAME = ?", (img_name,))
    data = cursor.fetchone()[0]
    if data == 0:
        image = face_recognition.load_image_file(img)
        image_encoding = face_recognition.face_encodings(image)
        if len(image_encoding) > 0:
            cursor.execute("INSERT INTO FACES (FACE_NAME, FACE_ENCODING) VALUES (?, ?)",
                           (img_name, sqlite3.Binary(image_encoding[0])))

db.commit()
print("Done !!")
db.close()
