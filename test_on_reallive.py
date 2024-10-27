import cv2
import time
from ultralytics import YOLO
from playsound import playsound

model = YOLO('best_weights.pt')

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()


# Timers for yawning and drowsiness detection
yawn_timer = 0
drowsiness_timer = 0

# Threshold times (in seconds)
yawn_threshold = 1  
drowsiness_threshold = 2  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    detected_classes = []
    for result in results:
        if result.boxes is not None:
            detected_classes.extend(result.boxes.cls.cpu().tolist())  # Get the class predictions

    # Check for yawning (assuming 'yawn' is class 2)
    if 2 in detected_classes:  # Class index for 'yawn'
        if yawn_timer == 0:
            yawn_timer = time.time()  
        elif time.time() - yawn_timer >= yawn_threshold:
            print("Please drink coffee!")
            playsound("yawn_sound.mp3")  
    else:
        yawn_timer = 0  # Reset if no yawn detected

    if 0 in detected_classes:  
        if drowsiness_timer == 0:
            drowsiness_timer = time.time()  #
        elif time.time() - drowsiness_timer >= drowsiness_threshold:
            print("Please wake up!")
            playsound("drowsiness_sound.mp3")  
    else:
        drowsiness_timer = 0  


    # Annotate and show the frame
    annotated_frame = results[0].plot()
    cv2.imshow('YOLO Webcam Test', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()