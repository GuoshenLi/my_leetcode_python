import torch
from torch import nn

def layer_norm(X, gamma, beta, eps):
    assert len(X.shape) in (2, 3)
    if len(X.shape) == 2:
        # 使用全连接层的情况，计算特征维上的均值和方差
        mean = X.mean(dim=1, keepdim=True)
        var = ((X - mean) ** 2).mean(dim=1, keepdim=True)
    else:
        mean = X.mean(dim=(1, 2), keepdim=True)
        var = ((X - mean) ** 2).mean(dim=(1, 2), keepdim=True)

    # 训练模式下，用当前的均值和方差做标准化
    X_hat = (X - mean) / torch.sqrt(var + eps)
    Y = gamma * X_hat + beta  # 缩放和移位
    return Y


class LayerNorm(nn.Module):
    # num_features：完全连接层的输出数量或卷积层的输出通道数。
    # num_dims：2表示完全连接层，3表示rnn输入
    def __init__(self, num_features, num_dims):
        super().__init__()
        if num_dims == 2:
            shape = (1, num_features)
        else:
            shape = (1, num_features, num_dims)
        # 参与求梯度和迭代的拉伸和偏移参数，分别初始化成1和0
        self.gamma = nn.Parameter(torch.ones(shape))
        self.beta = nn.Parameter(torch.zeros(shape))

    def forward(self, X):
        Y = batch_norm(X, self.gamma, self.beta, eps=1e-5)
        return Y
