


import tensorflow as tf

def binary_cross_entropy(logits, y):
    # logits: [bs,]
    # label: [bs,]

    pred = tf.sigmoid(logits)
    return -tf.reduce_mean(y * tf.log(pred) + (1 - y) * tf.log(1 - pred))


def softmax_cross_entropy(logits, y):
    # logits: [bs, #class]
    # label: [bs, #class]

    pred = tf.softmax(logits, axis=-1)
    return -tf.reduce_mean(tf.reduce_sum(y * tf.log(pred), axis=-1))