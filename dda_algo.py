import matplotlib.pyplot as ravi
def round(n):
    return int(n+0.5)
def drawDDA(x1, y1, x2, y2):
        x = [x1]
        y = [y1]
        steps = abs((x2 - x1) if abs(x2 - x1) > abs(y2 - y2) else (y2 - y1))
        dx = (x2 - x1) / float(steps)
        dy = (y2 - y1) / float(steps)
        print(((round(x[0]), round(y[0]))))
        i = 1
        for i in range(steps):
            l = round(x[i] + dx)
            m = round(y[i] + dy)
            x.append(l)
            y.append(m)
            i = i + 1
            print((((x[i]), y[i])))
        ravi.plot(x, y, 'o-', linewidth='1.5')

        ravi.show()
        ravi.grid()
ravi.xlim(0,100)
ravi.xlim(0,100)

a = int(input("Enter x1: "))
b = int(input("Enter y1: "))
c = int(input("Enter x2: "))
d = int(input("Enter y2: "))
drawDDA(a,b,c,d)
