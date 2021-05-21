import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

x1, y1 = [int(i) for i in input("Enter point 1(x1,y1): ").split()]
x2, y2 = [int(i) for i in input("Enter point 2(x2,y2): ").split()]
x3, y3 = [int(i) for i in input("Enter point 3(x3,y3): ").split()]

pts = ([[x1, y1], [x2, y2], [x3, y3]])

# plt.subplot(1, 2, 1)
plot1 = plt.figure(1)
# p1 pit.Polygon (pts, closed=False, facecolor = 'g')
p1 = plt.Polygon(pts, closed=True, fill=None, edgecolor='g')
plt.gca().add_patch(p1)

plt.xlim([0, 1000])
plt.ylim([0, 1000])
plt.grid(True)

font1 = {'family': 'serif', 'color': 'blue', 'size': 14}
plt.xlabel('x - axis', fontdict=font1)
plt.ylabel('y - axis', fontdict=font1)
plt.title('Original Triangle', fontdict=font1)

xt, yt = [int(i) for i in input("Enter distance point(x,y): ").split()]

pts[0][0] += xt
pts[1][0] += xt
pts[2][0] += xt

pts[0][1] += yt
pts[1][1] += yt
pts[2][1] += yt

# plt.subplot(1,2,2)
plot2 = plt.figure(2)
p2 = plt.Polygon(pts, closed=True, fill=None, edgecolor='r')
plt.gca().add_patch(p2)

plt.xlim([0, 1000])
plt.ylim([0, 1000])
plt.grid(True)

plt.xlabel('x - axis', fontdict=font1)
plt.ylabel('y - axis', fontdict=font1)
plt.title('Translated Triangle', fontdict=font1)

plt.show()