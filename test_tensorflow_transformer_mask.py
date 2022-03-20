# import tensorflow as tf
#
#
#
# inputs = tf.zeros([2, 5, 6], dtype=tf.float32)
# key_masks = tf.constant([[0., 0., 0., 0., 1., 1.],
#                          [0., 0., 0., 1., 1., 1.]])
#
# padding_num = -2 ** 32 + 1
#
#
# key_masks = tf.to_float(key_masks)
# key_masks = tf.tile(key_masks, [tf.shape(inputs)[0] // tf.shape(key_masks)[0], 1]) # (h*N, seqlen)
# key_masks = tf.expand_dims(key_masks, 1)  # (h*N, 1, seqlen)
# inputs = inputs + key_masks * padding_num
#
#
# diag_vals = tf.ones_like(inputs[0, :, :])  # (T_q, T_k)
# tril = tf.linalg.LinearOperatorLowerTriangular(diag_vals).to_dense()  # (T_q, T_k)
# future_masks = tf.tile(tf.expand_dims(tril, 0), [tf.shape(inputs)[0], 1, 1])  # (N, T_q, T_k)
#
# paddings = tf.ones_like(future_masks) * padding_num
# outputs = tf.where(tf.equal(future_masks, 0), paddings, inputs)
#
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     print(sess.run(outputs))
#
#
#
# # [[ 0.0000000e+00 -4.2949673e+09 -4.2949673e+09 -4.2949673e+09 -4.2949673e+09 -4.2949673e+09]
# #  [ 0.0000000e+00  0.0000000e+00 -4.2949673e+09 -4.2949673e+09 -4.2949673e+09 -4.2949673e+09]
# #  [ 0.0000000e+00  0.0000000e+00  0.0000000e+00 -4.2949673e+09 -4.2949673e+09 -4.2949673e+09]
# #  [ 0.0000000e+00  0.0000000e+00  0.0000000e+00  0.0000000e+00 -4.2949673e+09 -4.2949673e+09]
# #  [ 0.0000000e+00  0.0000000e+00  0.0000000e+00  0.0000000e+00 -4.2949673e+09 -4.2949673e+09]]




import tensorflow as tf
import numpy as np
a = np.arange(12).reshape((2, 3, 2))
b = tf.Variable(a)

embed = tf.Variable(tf.reshape(tf.range(100), (25, 4)))
after = tf.nn.embedding_lookup(embed, a)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(a.shape)
    embed_ = sess.run(embed)
    after_ = sess.run(after)

    print(embed_.shape)
    print(after_)

    print(np.mean(after_, axis = 2))



