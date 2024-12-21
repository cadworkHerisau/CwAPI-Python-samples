import os
import sys

import utility_controller as uc


# set python path for the plugin - add dependencies like numpy to the python path
# assume your packages are int .venv/Lib/site-packages
os.environ['PYTHONPATH'] = os.pathsep.join([
    os.path.join(os.path.dirname(__file__), '.venv', 'Lib', 'site-packages'),
    os.path.join(os.path.dirname(__file__), 'src'),
    os.path.dirname(__file__),
    os.path.join(uc.get_plugin_path()),
])

sys.path.extend(os.environ['PYTHONPATH'].split(os.pathsep))

# numpy version 1.22.2 - cadwork 3d is just compatible with numpy 1.22.2
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

a = np.array([0, 1, 2, 3, 4])
print(a)
print(a.sum())

x = [1, 2, 3]
y = [4, 5, 6]
np.cross(x, y)



