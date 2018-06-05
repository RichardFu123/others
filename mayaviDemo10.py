import numpy as np
from mayavi import  mlab

x,y = np.mgrid[-10:10:200j, -10:10:200j]
z = 100*np.sin(x*y)/(x*y)

mlab.figure(bgcolor=(1,1,1))
surf = mlab.surf(z,colormap="cool")
mlab.show()
