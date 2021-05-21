import numpy as np
import matplotlib.pyplot as plt
pts = np.array([[100,200 ], [250,300 ],[200,500]])
pts1=np.array([[2,0],[0,2]])# scaling vector

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
plt.show()


d=np.dot(pts,pts1)
print(d)

plot1 = plt.figure(1)
# p1 pit.Polygon (pts, closed=False, facecolor = 'g')
p1 = plt.Polygon(d, closed=True, fill="y", edgecolor='g')
plt.gca().add_patch(p1)

plt.xlim([0, 1000])
plt.ylim([0, 1000])
plt.grid(True)

font1 = {'family': 'serif', 'color': 'black', 'size': 14}
plt.xlabel('x - axis', fontdict=font1)
plt.ylabel('y - axis', fontdict=font1)
plt.title('After scaling Triangle', fontdict=font1)
plt.show()
