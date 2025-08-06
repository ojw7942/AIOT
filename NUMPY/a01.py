import matplotlib
matplotlib.use('TkAgg')  # TkAgg 백엔드 사용
import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 그래프 생성
plt.plot(x, y)
plt.show()  # 그래프를 화면에 표시
