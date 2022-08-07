import torch
import torch.nn as nn
import torch.nn.functional as F


def get_lstm_params(input_dim, hidden_dim):

    def three():
        return (torch.randn(input_dim, hidden_dim),
                torch.randn(hidden_dim, hidden_dim),
                torch.zeros(hidden_dim))

    W_xi, W_hi, b_i = three()
    W_xf, W_hf, b_f = three()
    W_xo, W_ho, b_o = three()
    W_xc, W_hc, b_c = three()

    return [W_xi, W_hi, b_i, W_xf, W_hf, b_f, W_xo, W_ho, b_o, W_xc, W_hc, b_c]


def init_lstm_state(batch_size, hidden_dim):
    return (torch.zeros(batch_size, hidden_dim),
            torch.zeros(batch_size, hidden_dim))

def lstm(inputs, hidden_dim):
    batch_size, time_step, input_dim = inputs.shape
    W_xi, W_hi, b_i, W_xf, W_hf, b_f, W_xo, W_ho, b_o, W_xc, W_hc, b_c = get_lstm_params(input_dim, hidden_dim)
    H, C = init_lstm_state(batch_size, hidden_dim)
    output = []

    inputs = list(map(lambda x: torch.squeeze(x), torch.chunk(inputs, chunks=time_step, dim=1)))
    for X in inputs:
        I = torch.sigmoid((X @ W_xi) + (H @ W_hi) + b_i)
        F = torch.sigmoid((X @ W_xf) + (H @ W_hf) + b_f)
        O = torch.sigmoid((X @ W_xo) + (H @ W_ho) + b_o)
        C_tilda = torch.tanh((X @ W_xc) + (H @ W_hc) + b_c)
        C = F * C + I * C_tilda
        H = O * torch.tanh(C)

        output.append(H)

    return torch.stack(output, dim=1), (H, C)



output = lstm(inputs=torch.randn(16, 10, 128), hidden_dim=64)
print(output[0].shape)
print(output[1])