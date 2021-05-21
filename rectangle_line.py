#python code to add rectangle and line

import matplotlib

import matplotlib.pyplot as plt

x1,y1= [int(i) for i in input("Enter (x1, y1) coordinates for the anchor point of the rectangle: ").split()]
w,h = [int(i) for i in input("Enter width and height: ").split()]

fig=plt.figure(1)

p1=matplotlib.patches.Rectangle((x1, y1),w,h,fill=None, edgecolor = 'green')
plt.gca().add_patch(p1)
plt.xlim([0, 100])
plt.ylim([0, 100])

x_min =x1
y_min= y1

x_max = w+x_min
y_max = h+y_min

print("x_min=",x_min)
print("y_min=",y_min)
print("x_max=",x_max)
print("y_max=",y_max)

x1, y1= [int(i) for i in input("Enter Line1(x1, y1): ").split()]
x2, y2 = [int(i) for i in input("Enter Line1(x2,y2): ").split()]
Lx=[x1,x2]
Ly=[y1, y2]

plt.plot(Lx,Ly, 'or-')

plt.show()