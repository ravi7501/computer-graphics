import matplotlib.pyplot as plt
def bresenhams(x1 , y1 , x2 , y2):
    dy,dx=(y2-y1),(x2-x1)
    m=dy/dx
    x=[x1]
    y=[y1]
    p=(2*dy)-(dx)
    if (m<1):
        while(x1<x2):
            if(p<0):
                x1=x1+1
                y.append(y1)
                x.append(x1)
                p=p+2*dy
            else:
                x1=x1+1
                y1=y1+1
                x.append(x1)
                y.append(y1)
                p=p+2*dy-2*dx
    elif(m>=1):
        while(x1<x2):
            if(p<0):
                y1=y1+1
                x.append(x1)
                y.append(y1)
                p = p + 2*dx
            else:
                x1=x1+1
                y1=y1+1
                x.append(x1)
                y.append(y1)
                p=p+2*dx-2*dy

    else:
        print("wrong input")
    plt.plot(x, y, 'o-', linewidth='1.5')
    plt.show()
    plt.grid()
a = int(input("Enter x1: "))
b = int(input("Enter y1: "))
c = int(input("Enter x2: "))
d = int(input("Enter y2: "))
bresenhams(a,b,c,d)