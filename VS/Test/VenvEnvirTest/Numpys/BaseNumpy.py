import numpy as np

a = np.array([1, 2, 3])              # 一维数组
b = np.array([[1, 2], [3, 4]])       # 二维数组
c = np.zeros((2, 3))                 # 全 0 数组
d = np.ones((3, 3))                  # 全 1 数组
e = np.eye(3)                        # 单位矩阵
f = np.arange(0, 10, 2)              # [0, 2, 4, 6, 8]
g = np.linspace(0, 1, 5)             # 5个点，等间距从0到1


print(g)