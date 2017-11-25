# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact

当前itorch和jupyter启动路径
http://202.204.54.230:9312/?token=1b0a9bc00de67a5fb37990d3e084dc42b7654da6205e82e1 :: /data/fluids
http://202.204.54.230:1212/?token=de007706d890dfde43f8ab8283c12fa301fa184da4c89675 :: /data/fluids

### 数据集准备
为了重现在 MNIST、CIFAR10、CelebA 和 SVHN 数据集上的实验，你需要准备这些数据，并使用一个正确的——data_path。

1. 对于 MNIST，你不需要准备数据，并可以提供任意的——data_path；
2. 对于 CIFAR10，请从该地址（https://www.cs.toronto.edu/~kriz/cifar.html）下载和获取数据的 Python 版本；然后使用包含 cifar-10-batchs-py 的目录的路径作为——data_path；
3. 对于 SVHN，请从该地址（http://ufldl.stanford.edu/housenumbers/）下载 train_32x32.mat 和 test_32x32.mat 文件，并使用包含这些文件的目录的路径作为——data_path；
4. 对于 CelebA，你需要安装 OpenCV。数据下载地址：http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html。你需要创建 celebA 文件夹，该文件夹包含 Anno 和 img_align_celeba 子文件夹。其中 Anno 必须包含 list_attr_celeba.txt，img_align_celeba 必须包含.jpg 文件。你还需要通过在——data_path （其中是包含了 celebA 的文件夹的路径）中运行 datasets/crop_faces.py 脚本对图像进行剪裁。训练模型的时候，你需要在——data_path 中使用相同的。

### Python 科学计算（The SciPy ecosystem）概述

Numpy

array和matrix及其基本运算

pandas

SciPy

包含最优化，线性代数，积分，插值，特殊函数，快速傅里叶变换，信号处理和图像处理，常微分方程求解和其他科学与工程中常用的计算







