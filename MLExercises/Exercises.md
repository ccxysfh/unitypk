# 机器学习练习题

通过习题，帮助理解机器学习，当然我们更专注于深度学习。

## 卷积神经网络

1. 相比全连接深度神经网络（DNN），卷积神经网络（CNN）在图像识别上有什么优势？

2. 假设构建一个有3层卷积的CNN，网络结构是这样，每层的核为3X3，步长（strides）为2，相同填充（Same Padding），第一层输出100个特征图（feature map），第二层输出200个，第三层输出400个。输入是200X300像素的RGB图像。这个网络的参数数目是多少？如果参数的类型都是32bits的float，那么当网络对单张图片进行学习时，最小需要使用多少内存（RAM）？当处理50张图片时又会占用多大的内存？

3. 当训练一个CNN网络时，GPU的内存耗尽，可以怎样来解决这个问题？

4. 步长一样，为什么要添加一个最大池化层而不是卷积层？

5. 什么时候添加一个局部响应正则化层（local response normalization layer）？

6. 相比LeNet-5，AlexNet有什么创新？GoogleNet和ResNet呢？(在著名的Imagenet竞赛中，AlexNet, GoogleNet, ResNet分别是2012,2014和2015年的取得最高准确率的方案)

7. 构建一个CNN网络，尝试在MNIST数据上取得尽可能高的准确率。

8. 使用Inception v3分类大图像：

   - 下载数据集（选择某一个公共数据集），并使用python加载它们，调整大小或裁剪到299×299像素，并确保它们只有三个通道（RGB），没有透明通道；

   - 下载最新预训练好的Inception v3模型；

   - 通过调用inception_v3()函数创建Inception v3模型，如下所示：

     ```Python
     from tensorflow.contrib.slim.nets import inception 
     import tensorflow.contrib.slim as slim 

     X = tf.placeholder(tf.float32, shape=[None, 299, 299, 3]) 
     with slim.arg_scope(inception.inception_v3_arg_scope()): 
       logits, end_points = inception.inception_v3(X, num_classes=1001, is_training=False) 
       predictions = end_points["Predictions"] 
       saver = tf.train.Saver()                         
     ```

   - 加载刚刚下载的预训练模型；

   - 看看模型在你准备的数据集上的准确率。

9. 大图像分类的迁移学习

   - 创建一个每个类别至少包含100张图片的数据集，比如可以使用花数据集或者MIT的地点数据集；
   - 编写一个图片进行预处理步骤，增加数据增强的随机性，调整图片大小或裁剪到299×299像素；
   - 使用练习8训练好的Inception v3模型，保留输出层之前的所有图层，将输出层神经元数修改你准备的数据集的类别数（例如花数据集有五个互斥的类，所以输出层必须有五个神经元，并使用softmax激活函数）；
   - 将数据集划分为训练集和测试集；在训练集上训练模型，并在测试集上评估这个模型。