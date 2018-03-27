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

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import tensorflow as tf

data_dir_path = "/data/datasets/simulation_data/frames"
SAMPLE_NUM = 3
PRINT_PARTICLE_EPOCH = 100
PRINT_SAMPLE_EPOCH = 2
"""
记录每个粒子的准确的准确的各种力的值，大概是十几维的向量，作为真实分布，而积分特征作为先验分布，通过GAN网络进行训练
"""

def plot_3d_scater(frame_particle):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = list(map(float, frame_particle[1:, 0]))
    z = list(map(float, frame_particle[1:, 1]))
    y = list(map(float, frame_particle[1:, 2]))
    ax.scatter(x, y, z, c="b", marker='o')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    
    plt.show()

    
# TODO box 为需要采样的盒空间，从正态分布中采样得到盒空间的半径，，以粒子坐标为中心初始化盒空间，对所有粒子判断是否在该盒空间内
class Box(object):

    def __init__(self, edge):
        self.xmin = edge[0]
        self.xmax = edge[1]
        self.ymin = edge[2]
        self.ymax = edge[3]
        self.zmin = edge[4]
        self.zmax = edge[5]

    def is_member(self, x, y, z):
        if x <= self.xmax and x >= self.xmin:
            if y <= self.ymax and y >= self.ymin:
                if z <= self.zmax and z >= self.zmin:
                    return True
        return False

    
# TODO 将粒子对象化没有必要        
class IntegralFeature(object):
    """
    TODO 设想一个完整的训练流程
    得到一帧粒子的所有坐标及速度，需要得到下一位置速度
    所以只能通过当前的坐标及速度计算积分特征，而每个积分特征包含10个分量，粘性力3，表面张力3，压强力3，及不可压缩条件（外力呢）
    采样方式及根据采样半径确定盒空间
    box的成员判断需要输入的参数
    """
    def __init__(self, particles, sample_num=SAMPLE_NUM):
        self.sample_num = sample_num
        self.particles = particles
        return
    
    def integral_volumes(self, x, y, z):
        sum = 0
        zero_box = Box(0, x, 0, y, 0, z)
        for particle in self.particles: # 此处传入的应当为nX6的张量
            if zero_box.is_member(tuple(particle.position)):
                sum += particle.f
        return sum
    
    def convert_float(self, part):
        for i in range(len(part)):
            num_str = part[i]
            pass
            
    def integral_feature(self, particles, box, index, part_origin):
        intefeature = []
        viscosity = []
        surface_tension = []
        pression = []
        incompresion = None
        for pid in range(len(particles)):
            if pid == index or pid == 0: # same particle
                continue
            part = particles[pid]
            part = list(map(float,part[:-1]))
            x = part[0]
            y = part[2]
            z = part[1]
            
            if box.is_member(x, y, z):# 一次判断同步计算
                
                # viscosity
                viscosity = [1, 2, 3]
                # surface_tension
                surface_tension = [4, 5, 6]
                # pression
                pression = [7, 8, 9]
                # incompresion
                incompresion = 10
                
        intefeature.extend(viscosity)
        intefeature.extend(surface_tension)
        intefeature.extend(pression)
        intefeature.append(incompresion)
        return intefeature

    def sample(self, particles):
        """
        将积分特征存入文件中，即一个场景的每一帧所有粒子对应一个积分特征的文件integral_features_screen_num.csv，
        文件的每一行是该粒子的索引和N个10维积分特征
        """
        f = open("feature_vectors.csv","w+") 
        for pid in range(len(particles)):
            if pid == 0:
                continue
            f.writelines(str(pid))
            f.writelines(",")
            part = particles[pid]
            part = list(map(float,part[:-1]))
            x = part[0]
            y = part[2]
            z = part[1]
            for sample_id in range(self.sample_num):
                sample_radius = 3 # TODO 从正态分布中进行采样
                box_params = tuple([x - sample_radius , x + sample_radius, \
                                    y - sample_radius , y + sample_radius, \
                                    z - sample_radius , z + sample_radius])
                box = Box(box_params)
                features = self.integral_feature(particles, box, pid, part)
                all_props = ",".join(list(map(str,features)))
                f.writelines(all_props)
                f.writelines(',')
                # end for N sample for one particle 
                if pid % PRINT_PARTICLE_EPOCH == 0:
                    if sample_id % PRINT_SAMPLE_EPOCH == 0:
                        print("%s particle sample :%s " , (str(pid), str(sample_id)))
            f.writelines('\n')
            f.flush()
        # end for all particles
        f.close()
                
                
                
                
                
                
                
                
                
                
                