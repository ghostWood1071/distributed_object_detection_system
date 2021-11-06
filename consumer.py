import numpy as np

arr = np.arange(480*640*3).reshape(480,640,3)
b = arr.tobytes()
print(b)