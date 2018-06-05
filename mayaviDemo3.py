import numpy as np
from mayavi import mlab

t = np.linspace(0,4*np.pi,20)
x = np.sin(2*t)
y = np.cos(t)
z = np.cos(2*t)
s = 2 + np.sin(t)
points = mlab.points3d(x,y,z,s,colormap='Blues',scale_factor=.25)
mlab.show()
