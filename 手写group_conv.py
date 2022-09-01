import torch
from torch import nn


class MyGroup(nn.Module):
    def __init__(self, group_conv):
        super(MyGroup, self).__init__()
        # 传入一个 pytorch 自带的 group_conv 层
        self.group_conv = group_conv

        # 从传入的 group_conv 中获取必要的参数
        in_ch = group_conv.in_channels
        out_ch = group_conv.out_channels
        self.n_groups = group_conv.groups
        kernel_size = group_conv.kernel_size
        stride = group_conv.stride
        padding = group_conv.padding
        bias = (group_conv.bias is not None)

        # 初始化一个 ModuleList，用于存储子卷积
        self.convs = nn.ModuleList()

        # 每个子卷积的输入/输出通道数
        self.in_ch_group = in_ch // self.n_groups
        self.out_ch_group = out_ch // self.n_groups

        # 定义 n_group 个子卷积，并保存到上面定义的 ModuleList 中
        for _ in range(self.n_groups):
            conv = nn.Conv2d(self.in_ch_group, self.out_ch_group,
                             kernel_size, stride, padding, bias=bias)
            self.convs.append(conv)

        # 初始化各子卷积的 weight 和 bias
        self._init_weight_bias()

    def _init_weight_bias(self):
        # 获取传入的 group_conv 的 weight 和 bias
        group_weight = self.group_conv.weight.data
        group_bias = self.group_conv.bias.data

        # 将 group_conv 的 weight 和 bias 切分成 n_group 块
        weights = torch.chunk(group_weight, self.n_groups, dim=0)
        biases = torch.chunk(group_bias, self.n_groups, dim=0)

        # 循环取出 ModuleList 中的各个子卷积
        for idx in range(self.n_groups):
            conv = self.convs[idx]
            # 用第 idx 块的 weight 和 bias 初始化子卷积
            conv.weight.data = weights[idx]
            conv.bias.data = biases[idx]

    def forward(self, x):
        # 将输入在 channel 维度上切分成 n_group 块
        x = torch.chunk(x, self.n_groups, dim=1)
        # 初始化一个 list，保存每个子卷积的结果
        out = []
        # 循环遍历每个子卷积
        for idx in range(self.n_groups):
            # 第 idx 个子卷积，卷积第 idx 块输入
            conv_i = self.convs[idx]
            x_i = x[idx]
            out_i = conv_i(x_i)
            out.append(out_i)

        # 在 channel 维度上拼接各子卷积结果
        out = torch.cat(out, dim=1)
        return out


if __name__ == '__main__':
    # 定义一个 group convolution
    Group = nn.Conv2d(32, 64, kernel_size=3, stride=1,
                      padding=1, groups=4, bias=True)
    # 用 pytorch 的 Group 来初始化上面定义的 MyGroup
    my_group = MyGroup(Group)

    feat = torch.rand(10, 32, 128, 128)
    out = Group(feat)
    out_my = my_group(feat)
    diff = torch.sum((out_my-out)**2)
    print(diff.item()) # 0.0