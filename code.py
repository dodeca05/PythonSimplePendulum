import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
plot=plt.figure()
def PolarCoordinates(t,r):
    x=np.sin(np.radians(t))*r
    y=np.cos(np.radians(t))*r
    return x,y
theta=30

r=1
g=9.81
v=0

periphery=2*r*np.pi
px,py=PolarCoordinates(theta,r)
line,=plt.plot([],[],"b-o")
def init():
    line.set_data([],[])
    return line,
def animate(i):
    global theta, v
    a=g*np.sin(np.radians(theta))
    a=a/25
    v=v+a
    vt=v/25
    theta=theta-360*(vt/periphery)
    px,py=PolarCoordinates(theta,r)
    #print(np.sqrt(px**2+py**2))
    X=np.zeros(2)
    Y=np.zeros(2)
    X[1]=px
    Y[1]=-py
    line.set_data(X,Y)
    return line,
anim=ani.FuncAnimation(plot,animate,init_func=init,frames=1,interval=1000/25,blit=False)
plt.axis([-r*1.5,r*1.5,-r*1.5,r*1.5])

plt.show()
