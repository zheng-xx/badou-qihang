#coding:utf8
import numpy as np
A = [1,2,3,4]
B = [3,4,5,6]
# print(np.dot(A,B))
# print(np.linalg.norm(A) * np.linalg.norm(B))
def Cosine_simi(A,B):
    x = np.dot(A,B)
    y = np.linalg.norm(A) * np.linalg.norm(B)
    print(x / y)

Cosine_simi(A,B)