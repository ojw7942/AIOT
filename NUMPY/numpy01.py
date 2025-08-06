import numpy as np

ftemp = [63, 73, 80, 86, 84, 78, 66, 54, 45, 63]

f = np.array(ftemp)
c = (f - 32) * 5 / 9
print(f)

import matplotlib.pyplot as plt
plt.plot(f)
plt.show()
