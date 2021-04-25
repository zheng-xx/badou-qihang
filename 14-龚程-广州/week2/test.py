import torch
import numpy as np
import SimilarityCalculation
import DiyBn

if __name__ == "__main__":
    print('>>>>>>>>>>>>>       Test Cosine Similarity       <<<<<<<<<<<<<<<<')
    vec_1 = np.random.rand(2, 2)  # [0, 1) 均匀分布
    vec_2 = np.random.randn(2, 2)  # 标准正态分布
    similarity = SimilarityCalculation.cosine(vec_1, vec_2)
    print('输入向量1：\n', vec_1)
    print('输入向量2：\n', vec_2)
    print('余弦相似度：', similarity)

    print('>>>>>>>>>>>>           Test BN Forward           <<<<<<<<<<<<<<<<')
    input_vec = np.random.rand(3, 2)
    print('输入向量:\n', input_vec)
    print('自定义bn标准化:\n', DiyBn.forward(input_vec))
    bn = torch.nn.BatchNorm1d(2)
    print('torch.bn:\n', bn(torch.from_numpy(input_vec).to(torch.float)))