""" Inspired by : https://gist.github.com/DIYer22/f82dc329b27c2766b21bec4a563703cc
from https://stackoverflow.com/questions/4279478/largest-circle-inside-a-non-convex-polygon """
import cv2
import numpy as np
from Chemin import chemin
import time

test_frames=[1,300,500,1246,4798,6238,418,2171]

path=chemin+'Bad-Apple-circles/Bad Apple frames/'
pathsavetest=chemin+"Bad-Apple-Circle/Tests/"
pathsave=chemin+"Bad-Apple-Circle/Frames/"

debut=time.time()
start=1
#for frame in test_frames:
for frame in range(start,6573):
    print(frame)
    filename=path+str(frame)+".png"

    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    filling=np.count_nonzero(gray == 255)
    filling_percentage=round(100*filling/691200)
    if filling_percentage>50:
        #white background
        ret,thresh = cv2.threshold(gray,50,255,cv2.THRESH_BINARY_INV)
        background=255
        color=0
        filling_percentage=100-filling_percentage
    else:
        #black background
        ret,thresh = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)
        background=0
        color=255

    #for reference 7% filling is good with 100 circles
    quantity=round(filling_percentage*100/7)
    circles={}
    for i in range(quantity):
        dist_map = cv2.distanceTransform(thresh, cv2.DIST_L2, cv2.DIST_MASK_PRECISE)
        _, radius, _, center = cv2.minMaxLoc(dist_map)
        circles[center]=radius
        cv2.circle(thresh, center, int(radius), 0, -1)#0=black -1=filled

    #draws the circles on a clean background
    new=np.zeros((1440,1920),np.uint8)+background
    for center in circles.keys():
        cv2.circle(new, (center[0]*2,center[1]*2), int(circles[center]*2), color, -1)
    cv2.imwrite(pathsave+str(frame)+".png",new)
    #cv2.imwrite(pathsavetest+str(frame)+".png",new)
    print("Mean time : {0}s per frame. Estimated duration : {1}h. Will end on {2}".format(round((time.time()-debut)/(frame+1-start),1), round((6572-frame)*(time.time()-debut)/((frame+1-start)*3600),1), time.asctime(time.localtime(debut+(6572-start)*(time.time()-debut)/(frame+1-start)))))