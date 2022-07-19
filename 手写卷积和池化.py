import numpy as np

def conv2d_torch_like_output_1_channel(input_data, kernel, stride, padding):


    '''
    :param input_data: shape: [c, h, w]
    :param kernel: shape: [c, kernel_h, kernel_w]
    :param stride: [stride_h, stride_w]
    :param padding: [padding_h, padding_w]
    :return:

    O = ((I + 2 * padding - kernel) // stride) + 1

    '''

    c, h, w = input_data.shape
    kernel_c, kernel_h, kernel_w = kernel.shape

    if c != kernel_c:
        raise ValueError("channels: input_data{}, kernel:{}".format(c, kernel_c))

    stride_h, stride_w = stride
    padding_h, padding_w = padding
    padding_input = np.pad(input_data, ((0, 0), (padding_h, padding_h), (padding_w, padding_w)))

    out = np.zeros(((h + 2 * padding_h - kernel_h) // stride_h + 1, (w + 2 * padding_w - kernel_w) // stride_w + 1))
    for idx_h, i in enumerate(range(0, h + 2 * padding_h - kernel_h + 1, stride_h)):
        for idx_w, j in enumerate(range(0, w + 2 * padding_w - kernel_w + 1, stride_w)):
            window = padding_input[:, i: i + kernel_h, j: j + kernel_w]
            out[idx_h, idx_w] = np.sum(window * kernel)

    return out


def conv2d(input_data, kernel, stride, padding, output_channel):
    c, h, w = input_data.shape
    kernel_c, kernel_h, kernel_w = kernel.shape
    stride_h, stride_w = stride
    padding_h, padding_w = padding

    out = np.zeros((output_channel, (h + 2 * padding_h - kernel_h) // stride_h + 1, (w + 2 * padding_w - kernel_w) // stride_w + 1))

    for i in range(output_channel):
        out[i, :, :] = conv2d_torch_like_output_1_channel(input_data, kernel, stride, padding)
    return out


print(conv2d_torch_like_output_1_channel(input_data=np.array([[[1,2,3,4,5,6],
                                        [2,3,4,5,6,7],
                                        [3,4,5,6,7,8],
                                        [4,5,6,7,8,9],
                                        [5,6,7,8,9,1],
                                        [6,7,8,9,1,2]]]),
                            kernel=np.array([[[1,2,3],[2,3,1],[3,2,1]]]),
                            stride=[2,2],
                            padding=[2,2]
                            ))


print(conv2d(input_data=np.array([[[1,2,3,4,5,6],
                                        [2,3,4,5,6,7],
                                        [3,4,5,6,7,8],
                                        [4,5,6,7,8,9],
                                        [5,6,7,8,9,1],
                                        [6,7,8,9,1,2]]]),
                            kernel=np.array([[[1,2,3],[2,3,1],[3,2,1]]]),
                            stride=[2,2],
                            padding=[2,2],
                            output_channel=3))



def maxpool_torch_like(input_data, kernel, stride, padding):


    '''
    :param input_data: shape: [c, h, w]
    :param stride: [stride_h, stride_w]
    :param padding: [padding_h, padding_w]
    :return:

    O = ((I + 2 * padding - kernel) // stride) + 1

    '''

    c, h, w = input_data.shape

    stride_h, stride_w = stride
    padding_h, padding_w = padding
    kernel_h, kernel_w = kernel
    padding_input = np.pad(input_data, ((0, 0), (padding_h, padding_h), (padding_w, padding_w)))

    out = np.zeros((c, (h + 2 * padding_h - kernel_h) // stride_h + 1, (w + 2 * padding_w - kernel_w) // stride_w + 1))
    for idx_c in range(c):
        for idx_h, i in enumerate(range(0, h + 2 * padding_h - kernel_h + 1, stride_h)):
            for idx_w, j in enumerate(range(0, w + 2 * padding_w - kernel_w + 1, stride_w)):
                window = padding_input[idx_c, i: i + kernel_h, j: j + kernel_w]
                out[idx_c, idx_h, idx_w] = np.max(window)

    return out


print(maxpool_torch_like(input_data=np.array([[[1,2,3,4,5,6],
                                               [2,3,4,5,6,7],
                                               [3,4,5,6,7,8],
                                               [4,5,6,7,8,9],
                                               [5,6,7,8,9,1],
                                               [6,7,8,9,1,2]]]),
                                         kernel = (3, 3),
                                         stride = (2, 2),
                                         padding = (1, 1)))