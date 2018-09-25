import numpy as np

x = np.arange(9.).reshape(3, 3)
y = np.where(x > 5)
z = x[y]
c = 1