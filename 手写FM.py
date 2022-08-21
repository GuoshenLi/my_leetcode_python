

import numpy as np
'''
    X: (m, n) m为样本数，n为特征数
    V: (n, k) n为特征数，k为embedding维度
'''
m = 10
n = 20
k = 32
X = np.random.normal(size=(m, n))
V = np.random.normal(size=(n, k))
y = (1 / 2) * np.sum(np.square(X @ V) - np.square(X) @ np.square(V), axis=1)
print(y.shape)


