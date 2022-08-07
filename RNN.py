import torch
import torch.nn as nn
import torch.nn.functional as F


def get_rnn_params(input_dim, hidden_dim):

    def three():
        return (torch.randn(input_dim, hidden_dim),
                torch.randn(hidden_dim, hidden_dim),
                torch.zeros(hidden_dim))

    W_xh, W_hh, b_h = three()


    return [W_xh, W_hh, b_h]


def init_rnn_state(batch_size, hidden_dim):
    return (torch.zeros(batch_size, hidden_dim),)

def rnn(inputs, hidden_dim):
    batch_size, time_step, input_dim = inputs.shape
    W_xh, W_hh, b_h = get_rnn_params(input_dim, hidden_dim)
    H, = init_rnn_state(batch_size, hidden_dim)
    output = []

    inputs = list(map(lambda x: torch.squeeze(x), torch.chunk(inputs, chunks=time_step, dim=1)))
    for X in inputs:
        H = torch.sigmoid((X @ W_xh) + (H @ W_hh) + b_h)
        output.append(H)

    return torch.stack(output, dim=1), (H, )



output = rnn(inputs=torch.randn(16, 10, 128), hidden_dim=64)
print(output[0].shape)
print(output[1])