import torch
import numpy as np
import cv2
import imutils
import sys
import time 
import yaml
import os
import json
import pathlib
import warnings
import io
from time import sleep

# from imageprocessing.capcolor import detect_color


global i

warnings.filterwarnings("ignore")

def detect_color(fn):
    
    color_confidence = []
    
    # load image
    img = cv2.imread(fn)
    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #                                                          RED
    # define range of wanted color in HSV 
    # you should get these values from the dict  => here I use RED
    lower_val_red = np.array([156, 43, 46]) 
    upper_val_red = np.array([180, 255, 255]) 
    # Threshold the HSV image - any red color will show up as white
    mask = cv2.inRange(hsv, lower_val_red, upper_val_red)
    hasRed = np.sum(mask)
    color_confidence.append(("RED", hasRed))
    if hasRed > 1000:
        print('Red detected!')
        print(f'Amount: {hasRed}')
    # display images
        # cv2.imshow("Input", img)
        # cv2.imshow("Mask", mask)   
    cv2.waitKey(0)  
    #                                                          Yellow
    # define range of wanted color in HSV 
    # you should get these values from the dict  => here I use RED
    lower_val_yellow = np.array([11, 43, 46]) 
    upper_val_yellow = np.array([34, 255, 255]) 
    # Threshold the HSV image - any green color will show up as white
    mask = cv2.inRange(hsv, lower_val_yellow, upper_val_yellow)
    # if there are any white pixels on mask, sum will be > 0
    hasYellow = np.sum(mask)
    color_confidence.append(("YELLOW", hasYellow))
    if hasYellow > 1000:
        print('Yellow detected!')
        print(f'Amount: {hasYellow}')
    # display images
        # cv2.imshow("Input", img)
        # cv2.imshow("Mask", mask)
    cv2.waitKey(0)  

    #                                                          Purple
    # define range of wanted color in HSV 
    # you should get these values from the dict  => here I use RED
    lower_val_purple = np.array([125, 43, 46]) 
    upper_val_purple = np.array([155, 255, 255]) 
    # Threshold the HSV image - any green color will show up as white
    mask = cv2.inRange(hsv, lower_val_purple, upper_val_purple)
    # if there are any white pixels on mask, sum will be > 0
    hasPurple= np.sum(mask)
    color_confidence.append(("PURPLE", hasPurple))
    if hasPurple > 1000:
        print('Purple detected!')
        print(f'Amount: {hasPurple}')
    # display images
        # cv2.imshow("Input", img)
        # cv2.imshow("Mask", mask)
    cv2.waitKey(0)  

    #                                                          Blue
    # define range of wanted color in HSV 
    # you should get these values from the dict  => here I use RED
    lower_val_blue = np.array([100, 43, 46]) 
    upper_val_blue = np.array([124, 255, 255]) 
    # Threshold the HSV image - any green color will show up as white
    mask = cv2.inRange(hsv, lower_val_blue, upper_val_blue)
    # if there are any white pixels on mask, sum will be > 0
    hasBlue = np.sum(mask)
    color_confidence.append(("BLUE", hasBlue))
    if hasBlue > 1000:
        print('Blue detected!')
        print(f'Amount: {hasBlue}')
    # display images
        # cv2.imshow("Input", img)
        # cv2.imshow("Mask", mask)
    cv2.waitKey(0) 

    #                                                          GREY
    # define range of wanted color in HSV 
    # you should get these values from the dict  => here I use RED
    lower_val_grey = np.array([0, 0, 46]) 
    upper_val_grey = np.array([180, 43, 220]) 
    # Threshold the HSV image - any green color will show up as white
    mask = cv2.inRange(hsv, lower_val_grey, upper_val_grey)
    # if there are any white pixels on mask, sum will be > 0
    hasGrey = np.sum(mask)
    color_confidence.append(("GREY", hasGrey))
    if hasGrey > 1000:
        print('grey detected!')
        print(f'Amount: {hasGrey}')
    # display images
        # cv2.imshow("Input", img)
        # cv2.imshow("Mask", mask)
    cv2.waitKey(0)


    #                                                          WHITE
    # define range of wanted color in HSV 
    # you should get these values from the dict  => here I use RED
    lower_val_white = np.array([0, 0, 221]) 
    upper_val_white = np.array([180, 30, 255]) 
    # Threshold the HSV image - any green color will show up as white
    mask = cv2.inRange(hsv, lower_val_white, upper_val_white)
    # if there are any white pixels on mask, sum will be > 0
    hasWhite = np.sum(mask)
    color_confidence.append(("WHITE", hasWhite))
    if hasWhite > 1000:
        print('white detected!')
        print(f'Amount: {hasWhite}')
    # display images
        
        # cv2.imshow("Input", img)
        # cv2.imshow("Mask", mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    print(color_confidence)
    highest_confidence = sorted(color_confidence, key = lambda x: x[1])
    print("\n The color of the cap is:", highest_confidence[-1][0])


def get_coordinates(i):
    k=str(i)
    
    # https://github.com/ultralytics/yolov5/issues/6460#issuecomment-1023914166
    # https://github.com/ultralytics/yolov5/issues/36


    # Loading Model
    model = torch.hub.load('yolov5', 'custom', path="bestcap.pt", source='local', force_reload = True)  # local repo
    #model = torch.hub.load("yolov5", 'custom', path="yolov5/runs/train/exp/weights/yolo_weights.pt", source='local', force_reload=True)  # local repo


    # Configuring Model
    model.cpu()  #  .cpu() ,or .cuda()
    model.conf = 0.50 # NMS confidence threshold
    model.iou = 0.45  # NMS IoU threshold
    model.agnostic = False  # NMS class-agnostic
    model.multi_label = False  # NMS multiple labels per box
    model.classes = None  # (optional list) filter by class, i.e. = [0, 15, 16] for COCO persons, cats and dogs
    model.max_det = 20  # maximum number of detections per image
    model.amp = False  # Automatic Mixed Precision (AMP) inference
    
    img = "Frame" + k +".jpg"
    print(img)
    frame = cv2.imread(img)          
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # OpenCV image (BGR to RGB)
            
    # Inference
    results = model(image, size=720) #includes NMS

    # Results
    #results.print()  # .print() , .show(), .save(), .crop(), .pandas(), etc.
    print('RESULTS')
    results.print() 

    results.xyxy[0]  # im predictions (tensor)
    results.pandas().xyxy[0]  # im predictions (pandas)
    #      xmin    ymin    xmax   ymax  confidence  class    name
    # 0  749.50   43.50  1148.0  704.5    0.874023      0  person
    # 2  114.75  195.75  1095.0  708.0    0.624512      0  person
    # 3  986.00  304.00  1028.0  420.0    0.286865     27     tie
            
    
    #Results in JSON
    json_results = results.pandas().xyxy[0].to_json(orient="records") # im predictions (JSON)
    print("\n",json_results,"\n")
    results.show()
    results.save()
    
    #cm_per_pixel = number_of_cm_in_Resolution_width/1280
    
    f = io.StringIO(json_results)
    data = json.load(f)
    if len(data) > 0:
        for record in data:
            print(record['confidence'])

        f = io.StringIO(json_results)
        data = json.load(f)
        for record in data:
            print("\n max confidence:",record['confidence'])
            print("\n record of max efficiency detected:",record,"\n")
            xmin,ymin,xmax,ymax = record['xmin'],record['ymin'],record['xmax'], record['ymax'];
            #coordinates in pixels
            # finalx1=xmin
            # finaly1=(ymax+ymin)/2.0
            # finalx2=xmax
            # finaly2=(ymax+ymin)/2.0
            print('rectangle boundary coordinates:x1=%f y1=%f x2=%f y2=%f' %(xmin,ymin,xmax,ymax),"\n")
            
            finalx=(xmax+xmin)/2.0
            finaly=(ymax+ymin)/2.0
            print('final coordinates x=%f y=%f' %(finalx ,finaly),"\n")
            
            crop_img = frame[int(ymin):int(ymax),int(xmin):int(xmax)]
            # cv2.imshow("cropped", crop_img)
            crop_img_file = 'cap{}.jpg'.format(i)
            cv2.imwrite(crop_img_file, crop_img)
            detect_color(crop_img_file)


            return True

            cv2.waitKey(0)
            
            #coordinates in cm
            #finalx1cm=finalx1* cm_per_pixel
            #finaly1cm=finaly1* cm_per_pixel
            #finalx2cm=finalx2* cm_per_pixel
            #finaly2cm=finaly2* cm_per_pixel
            #print('x1cm=%f y1cm=%f x2cm=%f y2cm=%f' %(finalx1cm ,finaly1cm ,finalx2cm,finaly2cm))
            break
        i+=1
    
    return False
    
def take_pic():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    i = 0
    while(cap.isOpened()):
        sleep(5)
        ret, frame = cap.read()
        #cv2.imshow('WebCam', frame)
        # This condition prevents from infinite looping
        # incase video ends.
        if ret == False:
            break
        
        # Save Frame by Frame into disk using imwrite method
        file_name = "Frame{}.jpg".format(i)
        cv2.imwrite(file_name, frame)
        
        
        
        break
        #picadd=os.path.abspath(frame)
        #print(picadd)
        cap.release()  
    cv2.destroyAllWindows()
    res = get_coordinates(i)

    print("FINAL RESULT: ", res)
    return res
   
    
   
     
def handle_exception():
    print("Error in Main Loop\n",e)
    cv2.destroyAllWindows()
    sys.exit()
    
if __name__ == "__main__":    
    try:
        while(True):
            sleep(1)
            result = take_pic()
            if(result == False):
                # Didn't find test tube, start from the beginning
                continue
            

    except Exception as e:
        handle_exception()
     
    
cv2.destroyAllWindows()