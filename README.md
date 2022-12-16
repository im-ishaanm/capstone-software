# Demonstration Files
The demo setup is placed under the *demo* folder. This demo aims to demonstrate the
image processing, barcode scanner and LIS all in one go in an infinite loop:

- An image is captured to locate the test tube.
- Once the test tube is located, co-ordinates and color are printed.
- Barcode scanner opens and continues to run until a barcode is scanned.
- Once scanned, the LIS attempts to process the barcode.
- On complete, the process loops.

> Note: Before executing, please ensure that the folder *yolov5* is present in the demo folder.
This folder can be transferred from the *image_processing* folder.

To execute the demonstration, run _testlive.py_

# Modules
## Actuation (Arduino)
The motor actuation code is compiled into _actuation.ino_.
It features an object oriented design to setup and actuate the motors easily using the stepper motor class.

### 1. Requirements
#### Applications
- Arduino _V1.8 or above_: [Download](https://www.arduino.cc/en/software)
#### Libraries
TBD

### 2. Installation / Execution
- Open _actuation.ino_ using Arduino.
- Make any changes to the code where required.
- Click *Verify* to verify and check for any errors.
- Click *Upload* to upload the code to your Arduino device.

## LIS (Python)
The LIS module is responsible for communicating between the hardware and the client database. It features
asynchronous API handling and a local storage failsafe to ensure error handling during network failures.
### 1. Requirements
#### Libraries
- asyncio: `pip install asyncio`
- aiohttp: `pip install aiohttp`

### 2. Installation / Execution
- Create a main python file Eg: _main.py_
- Import the LIS module by writing the following:
```
from LIS.server import processSample, setDebug

setDebug(True) # shows the progress of the LIS at each step
id = "12345" # barcode string
processSample(id)
```

## Image Processing (Python)
The image processing module is capable of detecting test tube samples from the camera using a deep learning algorithm. It is also
capable of detecting test tube cap's color. The image processing module returns the cap color and the x,y co-ordinates of the test
tube located.

### 1. Requirements
#### Libraries
- numpy:   `pip install numpy`
- pytorch: `pip install torch`
- yaml:    `pip install pyyaml`
- cv2:     `pip install opencv-python`

### 2. Installation / Execution
- Open the image_processing folder.
- Ensure _bestcap.pt_ and _yolov5_ are present in the folder.
- Execute _testlive.py_

## Barcode Scanning (Python)
The barcode scanner module is able to scan QR codes and barcodes attached to the test tubes and print out it's value.

### 1. Requirements
#### Libraries
- pyzbar:  `pip install pyzbar`
- cv2:     `pip install opencv-python`
- numpy:   `pip install numpy`

### 2. Installation / Execution
- Open the barcode_scanner folder
- Create a main python file Eg: _main.py_
- Call the barcode_scanner library:
```
from barcode_scanner.barcode_scanner import scan_barcode

scan_barcode()
```



