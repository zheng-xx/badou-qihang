#基于numpy实现余弦相似度计算，实现batchnormalization层前向计算
#二维象限 x y  随机256个向量点
def cosine_similarity(x, y, dim=256):
    xx = 0.0  #初始值
    yy = 0.0  #初始值
    xy = 0.0  #初始值
    for i in range(dim):
        xx += x[i] * x[i]
        yy += y[i] * y[i]
        xy += x[i] * y[i]
    xx_sqrt = xx ** 0.5 #xx的对位相乘，累加，然后开方
    yy_sqrt = yy ** 0.5 #yy的对位相乘，累加，然后开方
    cos = xy/(xx_sqrt*yy_sqrt)*0.5+0.5 #余弦相似度公式
    print("" + cos)
    return cos
