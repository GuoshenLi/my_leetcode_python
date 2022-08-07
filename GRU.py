import torch
import torch.nn as nn
import torch.nn.functional as F


def get_gru_params(input_dim, hidden_dim):

    def three():
        return (torch.randn(input_dim, hidden_dim),
                torch.randn(hidden_dim, hidden_dim),
                torch.zeros(hidden_dim))

    W_xz, W_hz, b_z = three()
    W_xr, W_hr, b_r = three()
    W_xh, W_hh, b_h = three()

    return [W_xz, W_hz, b_z, W_xr, W_hr, b_r, W_xh, W_hh, b_h]


def init_gru_state(batch_size, hidden_dim):
    return (torch.zeros(batch_size, hidden_dim),)

def gru(inputs, hidden_dim):
    batch_size, time_step, input_dim = inputs.shape
    W_xz, W_hz, b_z, W_xr, W_hr, b_r, W_xh, W_hh, b_h = get_gru_params(input_dim, hidden_dim)
    H, = init_gru_state(batch_size, hidden_dim)
    output = []

    inputs = list(map(lambda x: torch.squeeze(x), torch.chunk(inputs, chunks=time_step, dim=1)))
    for X in inputs:
        Z = torch.sigmoid((X @ W_xz) + (H @ W_hz) + b_z)
        R = torch.sigmoid((X @ W_xr) + (H @ W_hr) + b_r)
        H_tilda = torch.tanh((X @ W_xh) + ((H * R) @ W_hh) + b_h)
        H = Z * H + (1 - Z) * H_tilda

        output.append(H)

    return torch.stack(output, dim=1), (H, )



output = gru(inputs=torch.randn(16, 10, 128), hidden_dim=64)
print(output[0].shape)
print(output[1])