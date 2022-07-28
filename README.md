# Dynamic-Traffic-Signal

Dynamic Traffic System - This project is based on real time detection of traffic congestion using Python. The system contains raspberry-pi 3B, camera and LED traffic modules. Uses Haar Cascade / Yolo Algorithm to detect and count vehicles. GPIO pins used to control traffic module.

Important Libraries used:
1. OpenCV - Used to detect and capture frames from the camera module.
2. Turtle - For graphical representation of 4 way traffic signal system.

***
This repo contains two folders one on Yolo Algorithm and the other on Haar-Cascade Algorithm. The Yolo ALgorithm uses high amount of RAM (about more than 1GB) but is highly accurate. So this algo cannot be implemented in a raspberry-pi 3B which only supports upto 1GB RAM. Hence the Yolo ALgorithm is implemented to present a virtual simulation (using turtle library) of a Dynamic Traffic System Model on a computer of high RAM. The HAAR-Cascade algo uses very less RAM also has poor accuracy. Hence due to low RAM consumption by this algo it is implemented on practical Dynamic Traffic System Model using raspberry-pi 3B.

<img width="520" alt="Screenshot 2022-07-28 at 10 28 12 PM" src="https://user-images.githubusercontent.com/107111616/181595278-0b0579a8-e717-478d-a4bf-955b0acd5866.png">

***
###IMP: https://drive.google.com/drive/folders/1XwOK6L3GLTz4mmIVy0BKlZB1KSh_JCOt?usp=sharing 
##### The above link contains yolov4.weights it's an 250MB file. If using the Yolo Algorithm, this file needs to be downloaded and placed inside dnn_model folder inside the Yolo Algorithm. Without the yolov4.weights the algorithm wont work. (Couldn't add it to github repo due to its large size)  

**In conclusion use the the Yolo Algorithm Folder if your device supports more than 2GB RAM. For lesser RAM consumption use Haar-Cascade**
