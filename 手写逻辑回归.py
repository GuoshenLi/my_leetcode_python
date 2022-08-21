import numpy as np
import matplotlib.pyplot as plt



class LR:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.m = np.shape(self.x)[0]
        self.n = np.shape(self.x)[1] + 1
        self.X = np.concatenate([np.ones((self.m, 1)), self.x], axis=-1)
        self.alpha = 0.01
        random_index = np.random.permutation(self.m)
        self.X = self.X[random_index]
        self.y = self.y[random_index]

        self.weight = np.random.normal(size=(self.n, 1))
        self.loss_list = []


    def step(self):
        g_x = self.X @ self.weight
        h_x = 1 / (1 + np.exp(-g_x))

        # 计算损失函数 Cost Function 的损失值loss
        loss = -(np.log(h_x) * self.y + (1 - self.y) * np.log(1 - h_x))
        loss = np.sum(loss) / self.m
        self.loss_list.append(loss)

        # 梯度下降函数更新W权重
        dW = self.X.T @ (h_x - self.y) / self.m
        self.weight = self.weight - self.alpha * dW



num_sample = 10
x1 = 2 * np.random.normal(size=(num_sample, 2)) + 6
x2 = -4 * np.random.normal(size=(num_sample, 2)) - 5
plt.scatter(x1[:, 0], x1[:, 1], c='r')
plt.scatter(x2[:, 0], x2[:, 1], c='g')
x = np.concatenate([x1, x2], axis=0)
y = np.array([[0] for i in range(num_sample)] + [[1] for i in range(num_sample)])

print(x.shape)
print(y.shape)


lr = LR(x, y)
for _ in range(1000):
    lr.step()

print(lr.loss_list)
b, w1, w2 = lr.weight[0][0], lr.weight[1][0], lr.weight[2][0]
res = []
print(lr.weight)
x_1 = np.linspace(-15, 8, 100)
x_2 = (-w1 * x_1 - b) / w2

res = np.array(res)
plt.scatter(x_1, x_2, c='b')
plt.show()
