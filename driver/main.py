# Camera Capture Module
cap = cv2.VideoCapture(1)
while True:
    null, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the captured video frame
    cv2.imshow("Drowsiness DETECTOR IN OPENCV2", frame)
    key = cv2.waitKey(9)
    if key == 20:
        break
cap.release()
cv2.destroyAllWindows()



#Face and Eye Detection Module
face_detector = dlib.get_frontal_face_detector()
dlib_facelandmark = dlib.shape_predictor("path/to/shape_predictor_68_face_landmarks1.dat")

faces = face_detector(gray_scale)
for face in faces:
    face_landmarks = dlib_facelandmark(gray_scale, face)
    leftEye = []
    rightEye = []
    # Extracting left and right eye points


# Eye Aspect Ratio Calculation Module
def Detect_Eye(eye):
    poi_A = distance.euclidean(eye[1], eye[5])
    poi_B = distance.euclidean(eye[2], eye[4])
    poi_C = distance.euclidean(eye[0], eye[3])
    aspect_ratio_Eye = (poi_A + poi_B) / (2 * poi_C)
    return aspect_ratio_Eye

# Drowsiness Detection Logic Module
right_Eye = Detect_Eye(rightEye)
left_Eye = Detect_Eye(leftEye)
Eye_Rat = (left_Eye + right_Eye) / 2
Eye_Rat = round(Eye_Rat, 2)

if Eye_Rat < 0.25:
    cv2.putText(frame, "DROWSINESS DETECTED", (50, 100),
                cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 210), 3)
    engine.say("Alert!!!! WAKE UP DUDE")
    engine.runAndWait()


# Audio Alert Module
engine = pyttsx3.init()
engine.say("Alert!!!! WAKE UP DUDE")
engine.runAndWait()


# Visualization and UI Module
cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)  # For eyes
cv2.putText(frame, "DROWSINESS DETECTED", (50, 100),
            cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 210), 3)

#Termination Module
key = cv2.waitKey(9)
if key == 20:
    break
cap.release()
cv2.destroyAllWindows()


