#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@software: PyCharm
@file: debug_tensorflow.py
@time: 10/12/2017 09:36
"""
import numpy as np
import tensorflow as tf

def run(f):
    init = tf.global_variables_initializer()
    def tf_session():
        with tf.Session() as sess:
            sess.run(init)
            f(sess)
            sess.close()
    return tf_session

def sample_Z(m, n):
    return np.random.uniform(-1., 1., size=[m, n])

@run
def run_helleworld(sess):
    w = tf.placeholder(tf.float32, shape=(None, 3), name="w")
    hello = sess.run(w, feed_dict={w: sample_Z(4,3)})
    print(hello)

if __name__ == '__main__':
    run_helleworld()
