
import numpy as np
import torch

'''
手动实现torch中的batch1d
'''

#准备一个随机输入。一般网络中第一维是batch_size,第二维是输入维度，这个输入就相当于4个8维向量作为一个batch输入
x = torch.randn(4, 8)
#定义bn层，参数要与输入的维度一致，注意要理解这个维度与batch_size是无关的
bn = torch.nn.BatchNorm1d(8)
#由于默认的bn初始化weight参数都为1，所以容易看不出最后scale的作用，这里随机生成一个新的权重代替初始权重
#去掉这两行当然也应当获得一致的结果，这里相当于增加一点难度
weight = torch.randn(bn.state_dict()["weight"].shape)
bn.weight = torch.nn.Parameter(weight)
#改变后的权重输出看看。也可以去掉上面两行，看下原始的初始化权重，应该是[1,1,1,1...]
print(bn.state_dict()["weight"], "bn层权重")
#使用bn层进行前项计算
y = bn(x)
print(y, "torch bn输出")
#取出参数
w = bn.state_dict()["weight"].numpy()
b = bn.state_dict()["bias"].numpy()
#将输入转成numpy数组
x = x.numpy()
#计算均值，注意是沿batch_size的维度进行均值计算，这也是他为什么被称为batch normalization
p = np.mean(x, axis=0)
#按照公式计算var
v = np.mean(np.square(x - p), axis=0)
#依然是按照公式计算，这里e=1e-5是为了防止分母为零，查看torch源码可以找到，torch中的e也等于1e-5
x = (x - p) / np.sqrt(v + 1e-5)
#最后的scale线性运算
y = w * x + b
print(y, "自定义bn输出")


