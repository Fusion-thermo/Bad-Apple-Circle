#https://gist.github.com/DIYer22/f82dc329b27c2766b21bec4a563703cc
import cv2
import numpy as np
from PIL import Image

img_name="C:/Users/jeanb/OneDrive/Documents/Python/Largest circle/Image test.png"
img_name="C:/Users/jeanb/OneDrive/Documents/Python/Bad-Apple-circles/Bad Apple frames/700.png"

img = cv2.imread(img_name)
#cv2.imshow("img",img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("gray", gray)

for i in range(10):
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dist_map = cv2.distanceTransform(gray, cv2.DIST_L2, cv2.DIST_MASK_PRECISE)
    _, radius, _, center = cv2.minMaxLoc(dist_map)

    cv2.circle(gray, tuple(center), int(radius), color=(0,0,0),thickness= -1)#, lineType=cv2.LINE_8)

cv2.imshow("result", gray)
cv2.waitKey(0)