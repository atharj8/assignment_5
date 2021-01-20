from numpy import *
import matplotlib.pyplot as plt
plt.plot([0,8],[0,0])
r=4
t=linspace(0,2*pi)
plt.axis("equal")
x=r*cos(t);
y=r*sin(t);
plt.plot(x,y)
r=3
t=linspace(0,2*pi)
plt.axis("equal")
x=8+r*cos(t);
y=r*sin(t);
plt.plot(x,y)
#let the tangent from center of smaller circle meets the bigger circle at point A(a,b) and the tangent from the center of bigger circle meets smaller one at B(m,n)
#the angle between radius OA and the x axis 'Q'can be calculate  from right angled traingle
Q=math.acos(4/8)
#now cordinates of point A can be calculated from rt angled traingle
a=4*cos(Q)
b=4*sin(Q)
plt.plot([0,a],[0,b])
plt.plot([a,8],[b,0])
#similarly the angle between radius O'B and negative X axis can be calculated from rt angled tranigle
W=math.acos(3/8)
#now cordinates of point B can be calculted using rt angled traingle
m=8-3*cos(W)
n=3*sin(W)
plt.plot([8,m],[0,n])
plt.plot([m,0],[n,0])
plt.show()
