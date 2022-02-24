# Hand Gesture Volume Control
## What it does
System volume control using Hand Detection by MediaPipe & OpenCV libraries for Python

## How it works
* Detects the **Index & Thumb fingers**
* Calculates the **distance between both the fingers** and controls the volume accordingly
* Displays the **Output in 30-40 frames per seconds**

## How is it built
* **Hand Detection Module** : Class containing the *methods to detect hands & hand's postion*. 
* Python's **cv2 and mediapipe** libraries : Provide the *modules and methods to get hand landmarks and draw shapes* to mark them. 

