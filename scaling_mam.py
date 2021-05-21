#Assignment 3: Scaling

#Draw a triangle using three points (100, 200), (250, 300) and (200, 500) and Perform 20 translation by a distance of (150, 260).

import matplotlib.pyplot as plt

from matplotlib.patches import Polygon

x1, y1= [int(i) for i in input("Enter pointl (x1, y1): ").split()]

x2, y2 = [int(i) for i in input ("Enter point2(x2,y2): ").split()]

x3, y3 = [int(i) for i in input("Enter point3(x3,y3):").split()]

pts=([[x1,y1], [x2,y2], [x3,y3]])
plot = plt.figure(1)
pl = plt.Polygon (pts, closed=True, fill=None, edgecolor='g')
plt.gca().add_patch(pl)

plt.xlim([-10,1000])
plt.ylim([-10,1000])
plt.grid(True)

font1 = {'family': 'serif','color': 'blue', 'size':14}
plt.xlabel('x axis', fontdict = font1)
plt.ylabel('y axis', fontdict = font1)
plt.title( 'Original Triangle', fontdict = font1)
xf=(x1+x2+x3)/3
yf=(y1+y2+y3)/3

Sx,Sy =[float(i) for i in input("Enter scaling factor point(x,y): ").split()]
pts_new=[[1,1],[2,2],[3,3]]

pts_new[0][0]=round (Sx*pts[0][0]+xf*(1-Sx))
pts_new[1][0]=round (Sx*pts[1][0]+xf*(1-Sx))
pts_new[2][0]=round (Sx*pts [2][0]+xf*(1-Sx))

pts_new[0][1]=round (Sy*pts[0][1]+yf*(1-Sy))
pts_new[1][1]=round (Sy*pts [1][1]+yf*(1-Sy))
pts_new[2] [1]=round (Sy*pts [2] [1]+yf*(1-Sy))

print (pts_new)

plot2 =plt.figure(2)

p2=plt.Polygon (pts_new, closed= True, fill=None, edgecolor='r')

plt.gca().add_patch(p2)

plt.xlim([-10,1000])
plt.ylim([-18,1000])

plt.grid(True)

plt.xlabel('x _axis',fontdict=font1)

plt.ylabel('y axis', fontdict=font1)
plt.title('Scaled to origin', fontdict=font1)

plt.show()