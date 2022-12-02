import torch
import torch.nn as nn


def group_norm(x, gamma, beta, G, eps):
    _, C, H, W = x.shape
    x = torch.reshape(x, (-1, G, C // G, H, W))
    mean = x.mean(dim=(2, 3, 4), keepdim=True)
    var = ((x - mean) ** 2).mean(dim=(2, 3, 4), keepdim=True)
    x = (x - mean) / torch.sqrt(var + eps)
    x = torch.reshape(x, (-1, C, H, W))
    return x * gamma + beta

class GroupNorm(nn.Module):
    def __init__(self, num_channels):
        super().__init__()

        shape = (1, num_channels, 1, 1)
        # 参与求梯度和迭代的拉伸和偏移参数，分别初始化成1和0
        self.gamma = nn.Parameter(torch.ones(shape))
        self.beta = nn.Parameter(torch.zeros(shape))

    def forward(self, X, G):
        Y = group_norm(X, self.gamma, self.beta, G, eps=1e-5)
        return Y
