#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@software: PyCharm
@file: experiment.py
@time: 26/12/2017 13:19
"""
"""
构建了每个粒子的特征向量后，以当前的加速度为标记值，或者以当前的加速度表达密度𝛒，目标函数为（𝛒-𝛒0）
均作尝试

1. 针对每一帧的每一个粒子都需要根据粒子的坐标进行采样，采样方式及采样数目待定，构建特征向量
2. 是否需要进行降维，具体特征向量构建出来之后再行处理
3. 每一个epoch如何按batch_size进行训练样本的获取
4. 边界不滑移条件如何保证
5. 你从来没有搞清楚过损失函数不同情况是怎样的，区分回归和分类问题，二分类多分类，单值回归多值回归，以及不同的损失计量方法总结
"""
import random
import os

import numpy as np
import tensorflow as tf

data_dir_path = "/data/datasets/simulation_data/frames"

def reset_graph(seed=42):
    tf.reset_default_graph()
    tf.set_random_seed(seed)
    np.random.seed(seed)
reset_graph()

def sample_by_filename(filename):
    # selected pirticle

    file_path = os.path.join(data_dir_path, filename)
    frame_particle = np.loadtxt(file_path, dtype=np.str, delimiter=",")
    # 密度，需要进行采样，但这里对所有的粒子进行了求解
    f = open("feature_vectors.csv", "w+")
    f_labels = open("feature_vectors_labels.csv", "w+")
    number_particles = len(frame_particle)
    for i in range(number_particles):
        f.writelines(str(i))
        f.writelines(",")
        for num in range(100):
            theta = random.random()
            for j in range(number_particles):
                if i == j:
                    continue

                if j == number_particles - 1:
                    j = number_particles - 100

                if j == i + 1:
                    # 表面张力
                    delta_px = theta * (float(frame_particle[i, 0]) - float(frame_particle[j, 0]))
                    delta_py = theta * (float(frame_particle[i, 1]) - float(frame_particle[j, 1]))
                    delta_pz = theta * (float(frame_particle[i, 2]) - float(frame_particle[j, 2]))

                    # 粘性力
                    delta_vx = theta * (float(frame_particle[i, 0]) - float(frame_particle[j, 0]))
                    delta_vy = theta * (float(frame_particle[i, 1]) - float(frame_particle[j, 1]))
                    delta_vz = theta * (float(frame_particle[i, 2]) - float(frame_particle[j, 2]))

                    # 密度
                    density = theta * (delta_px + delta_py + delta_pz)

                    # 压强力
                    px = theta * (density * delta_px)
                    py = theta * (density * delta_py)
                    pz = theta * (density * delta_pz)

                    all_props = [delta_px, delta_py, delta_pz, delta_vx, delta_vy, delta_vz, density, px, py, pz]
                    all_props = ",".join(list(map(str, all_props)))

            f.writelines(all_props)
            f.writelines(',')
            f.flush()
        f.writelines('\n')
    # f_labels.write(",".join(list(map(str,[i,frame_particle[i,9], frame_particle[i,10], frame_particle[i,11]]))))
    f.close()

from tensorflow.contrib.layers import fully_connected
def net_structure(X_train=None,y_train=None,X_valid=None,y_valid=None,X_test=None,y_test=None):
    n_inputs = X_train.shape[1]
    n_outputs = y_train.shape[1]


    from datetime import datetime

    def log_dir(prefix=""):
        now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        root_logdir = "tf_logs"
        if prefix:
            prefix += "-"
        name = prefix + "run-" + now
        return "{}/{}/".format(root_logdir, name)
    graph = tf.Graph()
    with graph.as_default():
        X = tf.placeholder(tf.float32, shape=(None, n_inputs), name="X")
        y = tf.placeholder(tf.float32, shape=(None), name="y")

        he_init = tf.contrib.layers.variance_scaling_initializer()
        # TODO 修改隐藏层及每层神经元个数
        def dnn(inputs, n_hidden_layers=5, n_neurons=15, name=None, activation=tf.nn.elu, initializer=he_init):
            with tf.name_scope("dnn"):
                for layer in range(n_hidden_layers):
                    inputs = tf.layers.dense(inputs, n_neurons, activation=activation, \
                                             kernel_initializer=initializer, name="hidden%d" % (layer + 1))
            return inputs

        dnn_outputs = dnn(X)
        logits = fully_connected(dnn_outputs, n_outputs, scope="outputs", activation_fn=None)

        """
        对于损失函数的定义尚有疑虑，再行考虑,目前姑且先使用均方差吧
        """
        with tf.name_scope("train"):
            loss = tf.reduce_mean(np.multiply(logits-y, logits-y))
            optimizer = tf.train.AdamOptimizer()
            training_op = optimizer.minimize(loss)
        """
        添加summary，以调用tensorboard进行检测
        """


        logdir = log_dir("fluids")
        with tf.name_scope("summary"):
            loss_summary = tf.summary.scalar("log_loss", loss)
            file_writer = tf.summary.FileWriter(logdir, tf.get_default_graph())

        init = tf.global_variables_initializer()
        saver = tf.train.Saver()
    print("Build graph end.")
    n_epochs = 1000
    batch_size = 20

    # needed in case of early stopping
    max_checks_without_progress = 20
    checks_without_progress = 0
    best_loss = np.infty
    best_params = None

    checkpoint_path = "/tmp/my_fluid_model.ckpt"
    checkpoint_epoch_path = checkpoint_path + ".epoch"
    final_model_path = "./my_fluid_model"

    # X_train = ""
    # y_train = ""
    # X_valid = ""
    # y_valid = ""
    # X_test = ""
    # y_test = ""


    session = tf.Session(graph=graph)

    def get_model_params(session, graph):
        """Get all variable values (used for early stopping, faster than saving to disk)"""
        with graph.as_default():
            gvars = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES)
        return {gvar.op.name: value for gvar, value in zip(gvars, session.run(gvars))}

    def restore_model_params(session, graph, model_params):
        """Set all variables to the given values (for early stopping, faster than loading from disk)"""
        gvar_names = list(model_params.keys())
        assign_ops = {gvar_name: graph.get_operation_by_name(gvar_name + "/Assign")
                      for gvar_name in gvar_names}
        init_values = {gvar_name: assign_op.inputs[1] for gvar_name, assign_op in assign_ops.items()}
        feed_dict = {init_values[gvar_name]: model_params[gvar_name] for gvar_name in gvar_names}
        session.run(assign_ops, feed_dict=feed_dict)

    with session.as_default() as sess:
        if not os.path.exists(checkpoint_path):
            start_epoch = 0
            sess.run(init)
            print("start epoch 0")
        else:
            with open(checkpoint_epoch_path, 'rb') as f:
                start_epoch = int(f.read())
            print("Training was interrupted. Continuing at epoch", start_epoch)
            saver.restore(sess, final_model_path)
        for epoch in range(start_epoch, n_epochs):
            rnd_idx = np.random.permutation(len(X_train))
            for rnd_indices in np.array_split(rnd_idx, len(X_train) // batch_size):
                X_batch, y_batch = X_train[rnd_indices], y_train[rnd_indices]
                sess.run(training_op, feed_dict={X: X_batch, y: y_batch})

            loss_evl, summary_str = sess.run([loss, loss_summary], feed_dict={X: X_test, y: y_test})
            file_writer.add_summary(summary_str, epoch)
            print(epoch, "loss:", loss_evl)
            if epoch % 5 == 0:
                with open(checkpoint_epoch_path, 'wb') as f:
                    saver.save(sess, checkpoint_path)
                    f.write(b'%d' % (epoch + 1))
            # early stop
            if X_valid is not None and y_valid is not None:
                loss_val = sess.run(loss, feed_dict={X: X_valid, y: y_valid})
                if loss_val < best_loss:
                    best_params = get_model_params(sess, sess.graph)
                    best_loss = loss_val
                    checks_without_progress = 0
                else:
                    checks_without_progress += 1

                print("{}\tValidation loss: {:.6f}\tBest loss: {:.6f}".format(
                    epoch, loss_val, best_loss))

                if checks_without_progress > max_checks_without_progress:
                    print("Early stopping!")
                    break;
            else:
                loss_train = sess.run(loss, feed_dict={X: X_batch, y: y_batch})

                print("{}\tLast training batch loss: {:.6f}".format(epoch, loss_train))


        saver.save(sess, final_model_path)
        os.remove(checkpoint_epoch_path)

        if best_params:
            restore_model_params(best_params)


def object_function():
    """
    很明确的，我需要完善一件事，对于衡量最终结果的处理常用函数的总结
    如分类结果和标签的对比
    """
    y = "分类标签"
    y_ = "预测标签"
    tf.argmax(y, 1) # 最大值所在的索引位置就是类别标签,第二个参数表明的是axis，
    #输入的维度，更一般的0为狭义的x轴，1为狭义的y轴，指出衡量tensor的哪一维度，向量传入0
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    '''
      为了确定正确预测项的比例，我们可以把布尔值转换成浮点数，然后取平均值。
      例如， [True, False, True, True] 会变成 [1,0,1,1] ，取平均值后得到 0.75.
      cast将bool转为1，0
    '''
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    # clssify

    # regression
    return

def show_tensorboard(logdir):
    '''
    tensorboard --logdir=/path/to/log-directory
    :param log_dir:
    :return:
    '''
    training_op = ""
    merged_summary_op = tf.merge_all_summaries()
    total_step = 0
    epochs = 10000
    with tf.Session() as sess:
        summary_writer = tf.train.SummaryWriter('/tmp/mnist_logs', sess.graph)
        for epoch in range(epochs):
            total_step += 1
            sess.run(training_op)
            if total_step % 100 == 0:
                summary_str = sess.run(merged_summary_op)
                summary_writer.add_summary(summary_str, total_step)
    return

if __name__ == '__main__':
    pass