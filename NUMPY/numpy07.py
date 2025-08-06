import numpy as np
import time

np.random.seed(int(time.time()))  # 랜덤 시드 설정
randomNumbers = np.random.randint(1, 100, size=10)
# 1과 100 사이의 랜덤 숫자 10개 생성
print("랜덤 숫자:", randomNumbers)
randomNumbersTwoDim = np.random.randint(1, 100, size=(3, 4))
# 1과 100 사이의 랜덤 숫자 3행 4열 생성
print("2차원 랜덤 숫자:\n", randomNumbersTwoDim)
randomNumbersThreeDim = np.random.randint(1, 100, size=(2, 3, 4))
# 1과 100 사이의 랜덤 숫자 2행 3열 4층 생성
print("3차원 랜덤 숫자:\n", randomNumbersThreeDim)
randomNumbersNormal = np.random.normal(loc=0, scale=1, size=10)
# 평균 0, 표준편차 1인 정규분포에서 랜덤 숫자 10개 생성
print("정규분포 랜덤 숫자:", randomNumbersNormal)

input()