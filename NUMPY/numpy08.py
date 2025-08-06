import numpy as np  

score = np.array([[99, 93, 60], [98, 82, 93], [78, 82, 81]])
print(score.sum())
print(score.sum(axis=0)) # 각 열의 합   
print(score.sum(axis=1)) # 각 행의 합 
print(score.mean()) # 전체 평균
print(score.mean(axis=0)) # 각 열의 평균 
print(score.mean(axis=1)) # 각 행의 평균
print(score.max()) # 전체 최대값
print(score.max(axis=0)) # 각 열의 최대값
print(score.max(axis=1)) # 각 행의 최대값
print(score.min()) # 전체 최소값
print(score.min(axis=0)) # 각 열의 최소값
print(score.min(axis=1)) # 각 행의 최소값
print(score.std()) # 전체 표준편차
print(score.std(axis=0)) # 각 열의 표준편차
print(score.std(axis=1)) # 각 행의 표준편차
print(score.var()) # 전체 분산
print(score.var(axis=0)) # 각 열의 분산
print(score.var(axis=1)) # 각 행의 분산  

input()