import face_recognition
import numpy as np
import sqlite3
import cv2
import os
#import send  # Ensure send.py exists and has a sendSms() function

count = 0

# Initialize video capture using the default camera (index 0)
video_capture = cv2.VideoCapture(0)

known_face_names = []
known_face_encodings = []

# Connect to the SQLite database
db = sqlite3.connect('db.sqlite3')
print("Opened Database Successfully !!")

# Get the current working directory
current_directory = os.getcwd()

# Create the full path to the database file
database_path = os.path.join(current_directory, 'db.sqlite3')

# Print the full path
print("Database file is located at:", database_path)

cursor = db.cursor()

# Check if the FACES table exists
cursor.execute("SELECT * FROM sqlite_master WHERE name ='FACES' and type='table';")
chk = cursor.fetchone()
if chk is not None:
    data = cursor.execute("SELECT FACE_NAME, FACE_ENCODING FROM FACES")
else:
    print("There's no face entry in the Database !!")
    exit()

# Load known faces and encodings from the database
for row in data:
    known_face_names.append(row[0])
    known_face_encodings.append(np.frombuffer(row[1], dtype=np.float64))

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Capture a single frame of video
    ret, frame = video_capture.read()
    if not ret:
        print("Failed to capture image")
        break

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for any known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match was found in known_face_encodings, use the first one
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        height, width, _ = frame.shape
        font = cv2.FONT_HERSHEY_DUPLEX

        if name != "Unknown":
            # Draw a rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, 'Safe !!', (int(width / 4), height - 50), font, 1.0, (255, 255, 255), 1, cv2.LINE_AA)
        else:
            # Draw a rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            cv2.putText(frame, 'INTRUDER ALERT', (int(width / 4), height - 50), font, 1.0, (255, 255, 255), 1, cv2.LINE_AA)
            #if count == 0:
             #   send.sendSms()
              #  count += 1

        # Display the name below the face
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exited Operation !!")
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
