#Draw a triangle using three points (100, 40), (250, 70) and (190, 130) and
# Perform 2D rotation with reference to the pivot point at (5, 6) by an angle of 60 degrees.

import matplotlib.pyplot as plt
import math
from matplotlib.patches import Polygon

print("Enter The Coordinates Of The Tringle")
x1,y1 = [int(i) for i in input("Enter P1(x1,y1) = ").split()]
x2,y2 = [int(i) for i in input("Enter P2(x2,y2) = ").split()]
x3,y3 = [int(i) for i in input("Enter P3(x3,y3) = ").split()]

points = ([[x1,y1], [x2,y2], [x3,y3]])

plot1=plt.figure(1)
p1 = plt.Polygon(points, closed = False, facecolor='g')
plt.gca().add_patch(p1)

plt.xlim([0,1000])
plt.ylim([0,1000])
plt.grid(True)


xPoint, yPoint = [int(i) for i in input("Enter Distance Point(x,y) = ").split()]
rotat_Angle = int(input('Enter Rotation Angle = '))

cos_t = math.cos(math.radians(rotat_Angle))
sin_t = math.sin(math.radians(rotat_Angle))

new_x1 = round(xPoint+(points[0][0]-xPoint)*cos_t-(points[0][1]-yPoint)*sin_t)
new_y1 = round(yPoint+(points[0][0]-xPoint)*sin_t+(points[0][1]-yPoint)*cos_t)

new_x2 = round(xPoint+(points[1][0]-xPoint)*cos_t-(points[1][1]-yPoint)*sin_t)
new_y2 = round(yPoint+(points[1][0]-xPoint)*sin_t+(points[1][1]-yPoint)*cos_t)

new_x3 = round(xPoint+(points[2][0]-xPoint)*cos_t-(points[2][1]-yPoint)*sin_t)
new_y3 = round(yPoint+(points[2][0]-xPoint)*sin_t+(points[2][1]-yPoint)*cos_t)

points = [[new_x1,new_y1],[new_x2,new_y2],[new_x3,new_y3]]

print("New Points = ",points)

plot2 = plt.figure(2)
p2 = plt.Polygon(points, closed = False, facecolor='r')
plt.gca().add_patch(p2)
plt.xlim([-100,1000])
plt.ylim([-100,1000])
plt.grid(True)
plt.title('Rotation Of A Triangle')
plt.show()

