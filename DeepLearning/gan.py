#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@software: PyCharm
@file: gan.py
@time: 10/12/2017 00:29
"""
import os

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data/")

he_init = tf.contrib.layers.variance_scaling_initializer()

n_D_inputs = 28*28
n_G_inputs = 100
n_D_outputs = 1
n_G_outputs = 28*28

n_epochs = 20000
batch_size = 128
z_dim = 100

checkpoint_path = "/tmp/my_mnistGAN_model.ckpt"
checkpoint_epoch_path = checkpoint_path + ".epoch"
final_model_path = "./my_mnistGAN_model"

def reset_graph(seed=42):
    tf.reset_default_graph()
    tf.set_random_seed(seed)
    np.random.seed(seed)
def sample_Z(m, n):
    return np.random.uniform(-1., 1., size=[m, n])

def dnn(inputs, n_hidden_layers=1, n_neurons=128, pre_name=None, activation=tf.nn.elu,
        initializer=he_init, reuse=None):
    if pre_name == None:
        pre_name = ""
    with tf.name_scope("dnn"):
        for layer in range(n_hidden_layers):
            inputs = tf.layers.dense(inputs, n_neurons, activation=activation, \
                    kernel_initializer=initializer, name="%shidden%d" % (pre_name, layer + 1), reuse=reuse)
    return inputs

def generator(Z):
    g_latent_out = dnn(Z, pre_name="g_")
    g_logits = tf.layers.dense(g_latent_out, n_G_outputs, kernel_initializer=he_init, name="g_logits")
    g_proba = tf.nn.sigmoid(g_logits, name="g_proba")
    return g_logits, g_proba

def discriminator(X, reuse=None):
    d_latent_out = dnn(X, pre_name="d_",reuse=reuse)
    d_logits = tf.layers.dense(d_latent_out, n_D_outputs, kernel_initializer=he_init, name="d_logits", reuse=reuse)
    d_proba = tf.nn.sigmoid(d_logits)
    return d_logits, d_proba

#CREATE PHOTO
def plot(samples):
    fig = plt.figure(figsize=(4, 4))
    gs = gridspec.GridSpec(4, 4)
    gs.update(wspace=0.05, hspace=0.05)

    for i, sample in enumerate(samples):
        ax = plt.subplot(gs[i])
        plt.axis('off')
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_aspect('equal')
        plt.imshow(sample.reshape(28, 28), cmap='Greys_r')

    return fig

def main():
    reset_graph()
    Z = tf.placeholder(tf.float32, shape=(None, n_G_inputs), name="Z")
    X = tf.placeholder(tf.float32, shape=(None, n_D_inputs), name="X")

    g_logits, g_proba = generator(Z)
    d_logits_data, d_proba_data = discriminator(X)

    d_logits_g, d_proba_g = discriminator(g_proba, reuse=True)

    Variables = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES)
    theta_G = Variables[:4]
    theta_D = Variables[4:]

    xentropy_g = tf.nn.sigmoid_cross_entropy_with_logits(logits=d_logits_g, labels=tf.zeros_like(d_logits_g))
    loss_g = tf.reduce_mean(xentropy_g, name="loss_g")
    xentropy_data = tf.nn.sigmoid_cross_entropy_with_logits(logits=d_logits_data, labels=tf.ones_like(d_logits_data))
    loss_data = tf.reduce_mean(xentropy_data, name="loss_data")
    loss_D = loss_data + loss_g
    xentropy_G = tf.nn.sigmoid_cross_entropy_with_logits(logits=d_logits_g, labels=tf.ones_like(d_logits_g))
    loss_G = tf.reduce_mean(xentropy_G, name="loss_G")

    training_op_d = tf.train.AdamOptimizer().minimize(loss_D, var_list=theta_D)
    training_op_g = tf.train.AdamOptimizer().minimize(loss_G, var_list=theta_G)

    saver = tf.train.Saver()
    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)

        if not os.path.exists('out/'):
            os.makedirs('out/')

        # if not os.path.exists(checkpoint_epoch_path):
        #     start_epoch = 0
        #     sess.run(init)
        # else:
        #     with open(checkpoint_epoch_path, 'rb') as f:
        #         start_epoch = int(f.read())
        #     print("Training was interrupted. Continuing at epoch", start_epoch)
        #     saver.restore(sess, checkpoint_path)
        i = 0
        # for epoch in range(start_epoch, n_epochs):
        for epoch in range(n_epochs):

            X_batch, y_batch = mnist.train.next_batch(batch_size)
            # Z_batch = sample_Z(batch_size, z_dim)
            _, loss_D_val = sess.run([training_op_d, loss_D], feed_dict={X: X_batch, Z: sample_Z(batch_size, z_dim)})
            _, loss_G_val = sess.run([training_op_g, loss_G], feed_dict={Z: sample_Z(batch_size, z_dim)})

            if epoch % 2000 == 0:
                samples = sess.run(g_proba, feed_dict={Z: sample_Z(16, z_dim)})
                fig = plot(samples)
                plt.savefig('out/{}.png'.format(str(i).zfill(3)), bbox_inches='tight')
                i += 1
                plt.close(fig)

            # if epoch % 5000 == 0:
            #     with open(checkpoint_epoch_path, 'wb') as f:
            #         saver.save(sess, checkpoint_path)
            #         f.write(b'%d' % (epoch + 1))

            if epoch % 2000 == 0:
                print('Iter: {}'.format(epoch))
                print('D loss: {:.4}'.format(loss_D_val))
                print('G_loss: {:.4}'.format(loss_G_val))

if __name__ == '__main__':
    # print("data")
    # mnist = input_data.read_data_sets("/Users/changxin/Documents/deeplearning/UnityPK/datasets/MNIST")
    main()

