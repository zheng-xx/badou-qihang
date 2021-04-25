import numpy as np

'''
余弦相似度计算
写法非常的多，自己要验证一下结果正确
'''

def cosine_distance(x, y):
    return np.sum(x * y) / np.sqrt(np.sum(np.square(x)) * np.sum(np.square(y)))

#两个一致的向量，夹角为0度，余弦值为1
x = np.array([1,2])
y = np.array([1,2])
print(cosine_distance(x, y))

#两个垂直的向量，夹角为90度，余弦值为0
x = np.array([1,0])
y = np.array([0,1])
print(cosine_distance(x, y))

#向量夹角45度，余弦值(根号2)/2
x = np.array([1,1])
y = np.array([0,1])
print(cosine_distance(x, y))

#任意相同维度的向量都可以计算余弦相似度
x = np.array([1,2,3,4,5])
y = np.array([5,4,3,2,1])
print(cosine_distance(x, y))
