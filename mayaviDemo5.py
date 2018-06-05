import numpy as np
from mayavi import mlab
s = np.random.random((100,100))

img = mlab.imshow(s,colormap="gist_earth")
mlab.show()
