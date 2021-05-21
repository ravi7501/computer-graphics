import matplotlib
import matplotlib.pyplot as plt
import numpy as np

Rx1, Ry1 = [int(i) for i in input("Enter (x1,y1) coordinates for the anchor point of the rectangle: ").split()]
w, h = [int(i) for i in input("Enter width and height: ").split()]

p1 = matplotlib.patches.Rectangle((Rx1, Ry1), w, h, fill=None, edgecolor='green')
plt.gca().add_patch(p1)
plt.xlim([0, 1000])
plt.ylim([0, 1000])

x_min = Rx1
y_min = Ry1
x_max = w + x_min
y_max = h + y_min

print("x_min = ", x_min)
print("y_min = ", y_min)
print("x_max = ", x_max)
print("y_max = ", y_max)

Lx1, Ly1 = [int(i) for i in input("Enter Line(x1,y1): ").split()]
Lx2, Ly2 = [int(i) for i in input("Enter Line(x2,y2): ").split()]

Lx = [Lx1, Lx2]
Ly = [Ly1, Ly2]
plt.plot(Lx, Ly, 'or-')
plt.grid(True)
font1 = {'family': 'serif', 'color': 'blue', 'size': 14}
plt.xlabel('x-axis', fontdict=font1)
plt.ylabel('y-axis', fontdict=font1)
plt.title('Line with Clipping Window', fontdict=font1)

# Defining region codes
INSIDE = 0  # 0000
LEFT = 1  # 0001
RIGHT = 2  # 0010
BOTTOM = 4  # 0100
TOP = 8  # 1000


# Function to compute region code for a point(x, y)
def computeCode(x, y):
    code = INSIDE
    if x < x_min:  # to the left of rectangle
        code |= LEFT
    elif x > x_max:  # to the right of rectangle
        code |= RIGHT
    if y < y_min:  # below the rectangle
        code |= BOTTOM
    elif y > y_max:  # above the rectangle
        code |= TOP

    return code


# Implementing Cohen-Sutherland algorithm
# Clipping a line from P1 = (x1, y1) to P2 = (x2, y2)
def cohenSutherlandClip(x1, y1, x2, y2):
    # Compute region codes for P1, P2
    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    accept = False

    while True:

        # If both endpoints lie within rectangle
        if code1 == 0 and code2 == 0:
            accept = True
            break

        # If both endpoints are outside rectangle
        elif (code1 & code2) != 0:
            break

        # Some segment lies within the rectangle
        else:

            # Line Needs clipping
            # At least one of the points is outside,
            # select it
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            # findind intersection point
            # using formulas y = y1 + slope * (x - x1), x = x1 + (1 / slope) * (y - y1)
            if code_out & TOP:

                # point is above the clip rectangle
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max

            elif code_out & BOTTOM:

                # when point is below the clip rectangle
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min

            elif code_out & RIGHT:

                # when point is to the right of the clip rectangle
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max

            elif code_out & LEFT:

                # when point is to the left of the clip rectangle
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            # Now intersection point x, y is found
            # We replace point outside clipping rectangle by intersection point
            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1, y1)

            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2)

    if accept:
        Lx1 = [x1, x2]
        Ly1 = [y1, y2]

        fig = plt.subplots(1, 1)

        p1 = matplotlib.patches.Rectangle((Rx1, Ry1), w, h, fill=None, edgecolor='green')
        plt.gca().add_patch(p1)
        plt.xlim([0, 1000])
        plt.ylim([0, 1000])
        plt.grid(True)
        font1 = {'family': 'serif', 'color': 'blue', 'size': 14}
        plt.xlabel('x-axis', fontdict=font1)
        plt.ylabel('y-axis', fontdict=font1)
        plt.title('Clipped Line', fontdict=font1)
        plt.plot(Lx1, Ly1, 'r')
        plt.show()

    else:
        print("Line rejected")


cohenSutherlandClip(Lx1, Ly1, Lx2, Ly2)