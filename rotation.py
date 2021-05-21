import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import math

x1, y1 = [int(i) for i in input ("Enter point1(x1, y1): ").split()]
x2, y2 = [int(i) for i in input ("Enter point2(x2, y2): ").split()]
x3, y3 = [int(i) for i in input ("Enter point3(x3, y3): ").split()]

pts =([[x1, y1], [x2, y2], [x3, y3]])

#plt.subplot(1, 2, 1)
plot1= plt.figure(1)
p1= plt. Polygon (pts, closed=False, facecolor = 'g')
plt.gca().add_patch(p1)

plt.xlim([0,300])
plt.ylim([0,300])

plt.grid(True)
plt.title('Original Triangle')

print("Old Points: ", pts)

xPt, yPt = [int (i) for i in input ("Enter pivot point (x,y): ").split()]
RT_Angle = int(input('Enter rotation angle='))

cos_T=math.cos(math.radians(RT_Angle)) #converted degree to radians
sin_T=math.sin(math.radians(RT_Angle)) #converted degree to radians

# new points findout using the rotations farmula

New_x1=round (xPt+ (pts [0][0]-xPt) * cos_T-(pts [0][1]-yPt)*sin_T)
New_y1=round (yPt+ (pts [0][0]-xPt) * sin_T+(pts [0][1]-yPt)*cos_T)


New_x2=round (xPt+ (pts [1][0]-xPt) * cos_T-(pts [1][1]-yPt)*sin_T)
New_y2=round (yPt+ (pts [1][0]-xPt) * sin_T+(pts [1][1]-yPt)*cos_T)

New_x3=round (xPt+ (pts [2][0]-xPt) * cos_T-(pts [2][1]-yPt)*sin_T)
New_y3=round (yPt+ (pts [2][0]-xPt) * sin_T+(pts [2][1]-yPt)*cos_T)

pts=[[New_x1, New_y1], [New_x2, New_y2], [New_x3, New_y3]]

print("New Points: ", pts)

plot2 = plt.figure(2)
p2 = plt.Polygon(pts, closed=False, facecolor = 'r')
plt.gca().add_patch(p2)
plt.xlim([0,300])
plt.ylim([0,300])
plt.grid (True)
plt.show()
plt.title('Rotation of a Triangle')
plt.show()