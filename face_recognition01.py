import cv2
import face_recognition
import numpy as np
import os

# Load known image
known_image = face_recognition.load_image_file("your_name.jpg")
known_encodings = face_recognition.face_encodings(known_image)

if not known_encodings:
    print("❌ No face found in your_name.jpg. Use a clear photo.")
    exit()

known_encoding = known_encodings[0]

# Webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Cannot open camera")
    exit()
print("✅ Camera opened successfully")

cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Camera", 800, 600)

# Greeting flags
greeted = False
warned_unknown = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)

    if face_locations:
        try:
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        except Exception as e:
            print(f"⚠️ Encoding error: {e}")
            face_encodings = []

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            match = face_recognition.compare_faces([known_encoding], face_encoding)[0]
            name = "Unknown"

            if match:
                name = "HI MR your_name"
                if not greeted:
                    print("✅ Match found!")
                    os.system("say 'Hi Mister your_name'")
                    greeted = True
                    warned_unknown = False  # reset warning
            else:
                print("❌ Face does not match your_name.")
                if not warned_unknown:
                    os.system("say 'Sorry, I do not know you'")
                    warned_unknown = True
                    greeted = False  # reset greeting

            # Draw and label
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 4)
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("👋 Quit requested")
        break

cap.release()
cv2.destroyAllWindows()
