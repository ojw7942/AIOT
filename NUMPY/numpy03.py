import numpy as np

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("b:", b)
print("b[0, 1]:", b[0, 1])  # 첫 번째 행, 두 번째 열의 값
print("b[0, 1]:", b[0][1])  # 두 번째 행, 세 번째 열의 원소
print("b[1, :]:", b[1, :])  # 두 번째 

input()
