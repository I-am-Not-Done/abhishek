import cv2
import dlib
import pyautogui
import numpy as np

# Load face detector and shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # Download separately

# Get screen size
screen_width, screen_height = pyautogui.size()

# Define indexes for left and right eyes
LEFT_EYE_POINTS = list(range(36, 42))
RIGHT_EYE_POINTS = list(range(42, 48))

# Get eye center from landmarks
def get_eye_center(landmarks, eye_points):
    eye_region = np.array([(landmarks.part(point).x, landmarks.part(point).y) for point in eye_points])
    x = int(np.mean(eye_region[:, 0]))
    y = int(np.mean(eye_region[:, 1]))
    return (x, y)

# Webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Mirror image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)

        left_eye_center = get_eye_center(landmarks, LEFT_EYE_POINTS)
        right_eye_center = get_eye_center(landmarks, RIGHT_EYE_POINTS)

        # Midpoint between both eyes
        eyes_center = ((left_eye_center[0] + right_eye_center[0]) // 2,
                       (left_eye_center[1] + right_eye_center[1]) // 2)

        # Map coordinates from webcam to screen size
        rel_x = eyes_center[0] / frame.shape[1]
        rel_y = eyes_center[1] / frame.shape[0]

        screen_x = int(screen_width * rel_x)
        screen_y = int(screen_height * rel_y)

        pyautogui.moveTo(screen_x, screen_y)

        # Draw circles on eyes
        cv2.circle(frame, left_eye_center, 3, (0, 255, 0), -1)
        cv2.circle(frame, right_eye_center, 3, (0, 255, 0), -1)

    cv2.imshow("Eye Controlled Cursor", frame)

    if cv2.waitKey(1) == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
