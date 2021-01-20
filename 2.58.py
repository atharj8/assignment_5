from numpy import *
import matplotlib.pyplot as plt
r=5
angle_between_tangents=60
t=linspace(0,2*pi)
plt.axis("equal")
x=r*cos(t);
y=r*sin(t);
plt.plot(x,y)#circle with radius 5 and origin O(0,0)
#let the tangents are drawn from a point with cordinates A(a,b) and the tangent touches circle at pointsB(c,d) and C(e,f)
def angle_between_radius(angle_between_tangents):
    #sum of angles of a quadlateral is 360
    #angle between radius and tangent is 90
    angle_bet_rad=360-angle_between_tangents-90-90
    return angle_bet_rad
#angle between two radii at the end points of which the tangent will touch the circle ,we will represent it by angg
angg=angle_between_radius(angle_between_tangents)
#angle between x axis and radius will be represented as ang1 and ang 2
ang1=angg/2
ang2=-angg/2
h=radians(ang1)
c=cos((radians(ang1)))*r
d=sin((radians(ang1)))*r
e=cos((radians(ang2)))*r
f=sin((radians(ang2)))*r
#calculating cordinates of point A take right angled traingle AOB
a=r/cos((radians(ang1)))
b=0
plt.plot([0,c],[0,d])
plt.plot([0,e],[0,f])
plt.plot([c,a],[d,0])
plt.plot([c,a],[f,0])
plt.show()

