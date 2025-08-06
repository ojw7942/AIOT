import matplotlib.pyplot as plt
import matplotlib

# 🔧 한글 폰트 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# 🎨 간단한 그래프
plt.plot([1, 2, 3], [10, 20, 30])
plt.title('그래프 제목')
plt.xlabel('가로축')
plt.ylabel('세로축')
plt.show()
