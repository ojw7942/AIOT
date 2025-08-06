import numpy as np

heights = [1.83, 1.76, 1.68, 1.80, 1.90]
weights = [75, 68, 70, 80, 90]

np_heights = np.array(heights)
np_weights = np.array(weights)

bmi = np_weights / (np_heights ** 2)
print("BMI:", bmi)

input()