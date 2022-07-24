import torch
import torch.nn as nn


def instance_norm(x, eps):
    # 默认没有参数的
    _, C, H, W = x.shape
    mean = x.mean(dim=(3, 4), keepdim=True)
    var = ((x - mean) ** 2).mean(dim=(3, 4), keepdim=True)
    x = (x - mean) / torch.sqrt(var + eps)

    return x


