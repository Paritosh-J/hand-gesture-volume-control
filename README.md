# Hand Gesture Volume Control
## What it does
Controls the master volume of the computer

## How it works
* Detects the **Index & Thumb fingers**
* Calculates the **distance between both the fingers** and controls the volume accordingly
* Displays the **Output in 30-40 frames per seconds**

## How is it built
* **Hand Detection Module** : Class containing the *methods to detect hands & hand's postion*. 
* Python's **cv2 and mediapipe** libraries : Provide the *modules and methods to get hand landmarks and draw shapes* to mark them. 

