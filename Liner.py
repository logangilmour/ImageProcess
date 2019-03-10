import cv2
from numpy import *
import imageio
import matplotlib.pyplot as plt

img = cv2.imread("E:\\photogrammetry\\shoot2tif\\DSC_0247.tiff")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(gray,50,100)

lines = cv2.HoughLines(edges,1,pi/180,600);
abc = concatenate((cos(lines[:,:,1]),sin(lines[:,:,1]),-lines[:,:,0]),axis=1)

p1 = cross(abc,[0,1,0])
p1 = p1/p1[:,2][:,newaxis]
p1 = p1.astype(int)
p2 = cross(abc,[0,1,-img.shape[1]])
p2 = p2/p2[:,2][:,newaxis]
p2 = p2.astype(int)

for i in arange(p1.shape[0]):
    pnt1 = tuple(p1[i,0:2])
    pnt2 = tuple(p2[i,0:2])
    cv2.line(img,pnt1,pnt2,(0,255,0),2)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()