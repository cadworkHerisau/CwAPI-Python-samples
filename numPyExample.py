import sys

import utility_controller as uc

# get userprofil path
USERPROFIL = uc.get_3d_userprofil_path()

# appending a path
sys.path.append("C:/Users/michael.brunner/PycharmProjects/testCWAPI/CwAPI3D-PYTHON-samples/Lib/site-packages")

# numpy version 1.22.2
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
np.cr
print(arr)

# Create an array of integers from 0 to 4
a = np.array([0, 1, 2, 3, 4])

# Create a 2D array of random floats between 0 and 1
b = np.random.rand(2, 3)

print(b)

print(np.sum(b))


