# Actuation (Arduino)
The motor actuation code is compiled into _actuation.ino_.
It features an object oriented design to setup and actuate the motors easily using the stepper motor class.

## 1. Requirements
#### Applications
a) Arduino _V1.8 or above_: [Download](https://www.arduino.cc/en/software)
#### Libraries
TBD

## 2. Installation / Execution
a) Open _actuation.ino_ using Arduino.
b) Make any changes to the code where required.
c) Click *Verify* to verify and check for any errors.
d) Click *Upload* to upload the code to your Arduino device.

# LIS (Python)
The LIS module is responsible for communicating between the hardware and the client database. It features
asynchronous API handling and a local storage failsafe to ensure error handling during network failures.
## 1. Requirements
#### Libraries
a) asyncio: `pip install asyncio`
b) aiohttp: `pip install aiohttp`

## 2. Installation / Execution
a) Create a main python file Eg: _main.py_
b) Import the LIS module by writing the following:
```
from LIS.server import processSample, setDebug

setDebug(True) # shows the progress of the LIS at each step
id = "12345" # barcode string
processSample(id)
```

# Image Processing (Python)
The image processing module is capable of detecting test tube samples from the camera using a deep learning algorithm. It is also
capable of detecting test tube cap's color. The image processing module returns the cap color and the x,y co-ordinates of the test
tube located.

## 1. Requirements
#### Libraries
a) numpy:   `pip install numpy`
b) pytorch: `pip install torch`
c) yaml:    `pip install pyyaml`
d) cv2:     `pip install opencv-python`

## 2. Installation / Execution
a) Open the image_processing folder.
b) Ensure _bestcap.pt_ and _yolov5_ are present in the folder.
c) Execute _testlive.py_

# Barcode Scanning (Python)
The barcode scanner module is able to scan QR codes and barcodes attached to the test tubes and print out it's value.

## 1. Requirements
#### Libraries
a) pyzbar:  `pip install pyzbar`
b) cv2:     `pip install opencv-python`
c) numpy:   `pip install numpy`

## 2. Installation / Execution
a) Open the barcode_scanner folder
b) Create a main python file Eg: _main.py_
c) Call the barcode_scanner library:
```
from barcode_scanner.barcode_scanner import scan_barcode

scan_barcode()
```
