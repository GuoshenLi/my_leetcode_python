#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 统计字符出现频率，生成映射表
import heapq


def count_frequency(text):
    chars = []
    ret = []

    for char in text:
        if char in chars:
            continue
        else:
            chars.append(char)
            ret.append((char, text.count(char)))

    return ret


# 节点类
class Node:
    def __init__(self, frequency):
        self.left = None
        self.right = None
        self.father = None
        self.frequency = frequency

    def is_left(self):
        return self.father.left == self

    def __lt__(self, other):
        return self.frequency < other.frequency

# 创建叶子节点
def create_nodes(frequency_list):
    return [Node(frequency) for frequency in frequency_list]


# 创建Huffman树
def create_huffman_tree(nodes):
    heap = heapq.heapify(nodes[:])

    while len(heap) > 1:
        # heap.sort(key=lambda item: item.frequency)
        node_left = heapq.heappop(heap)
        node_right = heapq.heappop(heap)
        node_father = Node(node_left.frequency + node_right.frequency)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        heap.append(node_father)

    heap[0].father = None
    return heap[0]


# Huffman编码
def huffman_encoding(nodes, root):
    huffman_code = [''] * len(nodes)

    for i in range(len(nodes)):
        node = nodes[i]
        while node != root:
            if node.is_left():
                huffman_code[i] = '0' + huffman_code[i]
            else:
                huffman_code[i] = '1' + huffman_code[i]
            node = node.father

    return huffman_code


# 编码整个字符串
def encode_str(text, char_frequency, codes):
    ret = ''
    for char in text:
        i = 0
        for item in char_frequency:
            if char == item[0]:
                ret += codes[i]
            i += 1

    return ret


# 解码整个字符串
def decode_str(huffman_str, char_frequency, codes):
    ret = ''
    while huffman_str != '':
        i = 0
        for item in codes:
            if item in huffman_str and huffman_str.index(item) == 0:
                ret += char_frequency[i][0]
                huffman_str = huffman_str[len(item):]
            i += 1

    return ret


if __name__ == '__main__':
    text = raw_input('The text to encode:')

    char_frequency = count_frequency(text)
    nodes = create_nodes([item[1] for item in char_frequency])
    root = create_huffman_tree(nodes)
    codes = huffman_encoding(nodes, root)

    huffman_str = encode_str(text, char_frequency, codes)
    origin_str = decode_str(huffman_str, char_frequency, codes)

    print('Encode result:' + huffman_str)
    print('Decode result:' + origin_str)